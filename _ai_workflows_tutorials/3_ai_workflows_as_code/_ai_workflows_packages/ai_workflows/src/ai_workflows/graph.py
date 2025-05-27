"""Manages how tasks are connected and executed in AI workflows.

This module is like a recipe manager that:
- Organizes tasks in the right order
- Makes sure each task has what it needs
- Collects and shares results between tasks
- Keeps everything running smoothly

Uses LangGraph to handle the task sequence.
"""

import logging
import time
from typing import Any, Callable

from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, Field

from .config import InstructionsConfig, TaskConfig
from .context import WorkflowContext

logger = logging.getLogger(__name__)


class WorkflowState(BaseModel):
    """Keeps track of everything during workflow execution.

    Like a notepad that records:
    - Current progress (content)
    - Important details we need (context)
    - Results from each task (task_outputs)
    """
    content: str = ''
    context: dict[str, Any] = Field(default_factory=dict)
    task_outputs: dict[str, dict[str, str]] = Field(default_factory=dict)


class TaskNode(BaseModel):
    """Settings for one task in the workflow.

    Example:
        ```python
        node = TaskNode(
            id='analyze_text',   # Task name
            function=analyze_fn  # What to do
        )
        ```
    """
    model_config = {'arbitrary_types_allowed': True}

    id: str
    function: Callable


# Instructions for the AI assistant
TASK_SYSTEM_TEMPLATE = '''
You are an AI assistant executing a single task within a larger workflow. You execute your task and nothing else, even
if you have information about the workflow.

CRITICAL RULES:
1. Focus ONLY on your specific task
2. Use ONLY the provided information
3. DO NOT ask for additional information
4. Stay CONSISTENT with workflow requirements
5. BE PRECISE in your output format
'''

# What to tell the AI about each task
TASK_USER_TEMPLATE = '''
<TASK>
{task_description}
</TASK>

<AVAILABLE_INFORMATION>
{context}
</AVAILABLE_INFORMATION>

<WORKFLOW_CONTEXT>
Goal:
{goal}

Requirements:
{requirements}

Specifications:
{specifications}
</WORKFLOW_CONTEXT>

<PREVIOUS_OUTPUTS>
{current_content}
</PREVIOUS_OUTPUTS>

<OUTPUT_GUIDELINES>
1. Focus on your task ALONE
2. Use "Available Information" carefully - DO NOT ask for additional information
3. Only use "Workflow Context" if directly related to your task
4. BE CONSISTENT with workflow goal, requirements and specifications
</OUTPUT_GUIDELINES>
'''

TASK_PROMPT = ChatPromptTemplate.from_messages([
    ('system', TASK_SYSTEM_TEMPLATE),
    ('user', TASK_USER_TEMPLATE)
])


class TaskPrompt:
    """Creates clear instructions for each task.

    Example:
        ```python
        messages = TaskPrompt.create(
            task=task_config,             # What to do
            instructions=workflow_info,   # Overall rules
            context="Available info...",  # Background info
            current_content="Previous results..."
        )
        ```
    """

    task_prompt = TASK_PROMPT

    @staticmethod
    def create(task: TaskConfig, instructions: InstructionsConfig, context: str, current_content: str) -> list:
        """Creates instructions for a task.

        Args:
            task: What this task should do
            instructions: Overall workflow rules
            context: Background information
            current_content: Previous task results

        Returns:
            List of messages for the AI
        """
        return TaskPrompt.task_prompt.format_messages(
            task_description=task.description,
            context=context,
            goal=instructions.goal,
            requirements=instructions.requirements,
            specifications=instructions.specifications,
            current_content=current_content if current_content else 'No previous tasks output.'
        )


class WorkflowGraph:
    """Creates and manages the sequence of workflow tasks.

    Think of it as a recipe that:
    1. Lists all steps in order
    2. Makes sure each step has what it needs
    3. Passes results between steps
    4. Keeps everything organized

    Example:
        ```python
        # Define the steps
        nodes = [
            TaskNode(id='extract', function=extract_fn),
            TaskNode(id='analyze', function=analyze_fn)
        ]

        # Create and run
        graph = WorkflowGraph.create_sequential(nodes)
        result = graph.invoke(initial_state)
        ```
    """

    @staticmethod
    def create_sequential(nodes: list[TaskNode]) -> StateGraph:
        """Creates a workflow where tasks run in sequence.

        Args:
            nodes: List of tasks to run in order

        Returns:
            Ready-to-run workflow
        """
        graph = StateGraph(WorkflowState)

        # Add all tasks first
        for node in nodes:
            graph.add_node(node.id, node.function)

        # Connect tasks in sequence
        if nodes:
            # Start with first task
            graph.add_edge(START, nodes[0].id)

            # Connect tasks in order
            for i in range(len(nodes) - 1):
                current = nodes[i].id
                next_node = nodes[i + 1].id
                graph.add_edge(current, next_node)

            # Connect last task to end
            graph.add_edge(nodes[-1].id, END)

        return graph.compile()

    @staticmethod
    def create_node_function(
        task: TaskConfig,
        instructions: InstructionsConfig,
        llm: BaseLanguageModel,
        context: WorkflowContext,
    ) -> Callable:
        """Creates a function that runs one task.

        Args:
            task: What this task should do
            instructions: Overall workflow rules
            llm: AI model to use
            context: System for finding information

        Returns:
            Function that executes the task
        """
        parser = StrOutputParser()

        def node_function(state: WorkflowState) -> WorkflowState:
            # Calculate progress
            total_tasks = len(instructions.tasks)
            current_task = next(
                (i + 1 for i, t in enumerate(instructions.tasks) if t.key == task.key),
                0
            )
            logger.info(
                f'\n{"="*50}\n'
                f'Task {current_task}/{total_tasks} ({(current_task/total_tasks)*100:.0f}%): {task.key}\n'
                f'- Description: {task.description[:100]}...\n'
                f'- Required inputs: {len(task.inputs)}\n'
                f'- Expected outputs: {len(task.outputs)}\n'
                f'{"="*50}'
            )

            # Get needed information
            context_parts = []
            for input_config in task.inputs:
                try:
                    if input_config.from_context:
                        logger.info(f'Fetching context from sources: {input_config.from_context}')
                        context_text = context.get_relevant(task.description, input_config.from_context)
                        if context_text:
                            context_parts.append(context_text)
                            logger.debug(
                                f'Retrieved context from {input_config.from_context}:\n'
                                f'- Size: {len(context_text):,} chars\n'
                                f'- Preview: {context_text[:200]}...\n'
                            )
                        else:
                            logger.warning(f'No context found for sources: {input_config.from_context}')

                    elif input_config.from_tasks:
                        logger.info(f'Fetching outputs from tasks: {input_config.from_tasks}')
                        for task_key, output_key in input_config.from_tasks:
                            task_output = state.task_outputs.get(task_key, {}).get(output_key)
                            if task_output is None:
                                raise ValueError(f'Missing required output: {task_key}.{output_key}')
                            context_parts.append(
                                f'Output from {task_key} ({output_key}):\n\n{task_output}'
                            )
                            logger.debug(
                                f'Retrieved output from {task_key}.{output_key}:\n'
                                f'- Size: {len(task_output):,} chars'
                            )
                except Exception as e:
                    logger.error(
                        f'Error gathering input for {task.key}:\n'
                        f'- Input config: {input_config}\n'
                        f'- Error: {str(e)}'
                    )
                    raise

            combined_context = '\n\n---\n\n'.join(filter(None, context_parts))
            logger.info(
                f'Context summary for {task.key}:\n'
                f'- Parts: {len(context_parts)}\n'
                f'- Total size: {len(combined_context):,} chars\n'
                f'- Average part size: {len(combined_context)/len(context_parts):,.0f} chars'
                if context_parts else 'No context parts available'
            )

            # Run the task
            try:
                messages = TaskPrompt.create(
                    task=task,
                    instructions=instructions,
                    context=combined_context,
                    current_content=state.content
                )

                logger.debug(
                    f'Prompt for {task.key}:\n'
                    f'- Messages: {len(messages)}\n' +
                    '\n'.join(f'- {m.type}: {len(m.content)} chars' for m in messages)
                )

                start_time = time.time()
                response = llm.invoke(messages)
                execution_time = time.time() - start_time

                # Get usage statistics if available
                usage = getattr(response, 'usage', None)
                if usage:
                    logger.info(
                        f'LLM metrics for {task.key}:\n'
                        f'- Execution time: {execution_time:.2f}s\n'
                        f'- Input tokens: {usage.prompt_tokens:,}\n'
                        f'- Output tokens: {usage.completion_tokens:,}\n'
                        f'- Total tokens: {usage.total_tokens:,}\n'
                        f'- Tokens/second: {usage.total_tokens/execution_time:.1f}'
                    )

                content = response.content if isinstance(response, AIMessage) else response
                clean_content = parser.parse(content)

                # Update what we know
                new_state = WorkflowState(
                    content=clean_content,
                    context=state.context,
                    task_outputs={**state.task_outputs}
                )

                # Save task results
                new_state.task_outputs[task.key] = {
                    output.key: clean_content for output in task.outputs
                }

                logger.info(
                    f'Task {task.key} completed:\n'
                    f'- Execution time: {execution_time:.2f}s\n'
                    f'- Output size: {len(clean_content):,} chars\n'
                    f'- Saved outputs: {list(new_state.task_outputs[task.key].keys())}'
                )

                return new_state

            except Exception as e:
                logger.error(
                    f'Error executing {task.key}:\n'
                    f'- Error type: {type(e).__name__}\n'
                    f'- Error message: {str(e)}\n',
                    exc_info=True
                )
                raise

        return node_function
