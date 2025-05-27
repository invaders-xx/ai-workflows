"""Core workflow implementation for AI-powered task automation.

This module is like a project manager that:
- Reads instructions from configuration files
- Sets up the AI tools needed
- Organizes information sources
- Runs tasks in sequence
- Saves results properly

Example:
    ```python
    # Create and run a workflow
    workflow = Workflow(
        config_path='config.yaml',      # Technical setup
        instructions_path='tasks.yaml'  # What to do
    )
    result = workflow.run()

    # See what was produced
    print(f'Main output: {result.content}')
    ```
"""

from importlib import import_module
import logging
from pathlib import Path
import time
from typing import Any
import yaml

from langchain.schema import BaseMessage
from langgraph.graph import StateGraph
from pydantic import BaseModel, Field

from .config import ConfigWithType, InstructionsConfig
from .constants import OUTPUT_DIR
from .context import ContextSource, WorkflowContext, WorkflowContextConfig
from .graph import TaskNode, WorkflowGraph, WorkflowState

logger = logging.getLogger(__name__)


class LLMConfig(ConfigWithType):
    """Settings for the AI language model.

    Example:
        ```yaml
        type: "langchain.chat_models.ChatGroq"  # Which AI to use
        temperature: 0.7                        # Creativity (0-2)
        model_name: "mixtral-8x7b"             # Model version
        api_key: "your-key-here"               # Access key
        max_tokens: 2000                       # Max output size
        rate_limiter: null                     # Speed limit
        ```
    """
    type: str = Field(..., description='Full path to model class')
    temperature: float = Field(default=0.0, ge=0.0, le=2.0)
    model_name: str
    api_key: str
    max_tokens: int
    rate_limiter: ConfigWithType | None = None

    def create_object(self) -> Any:
        """Creates a working AI model from the settings."""
        kwargs = self.model_dump(exclude={'type', 'rate_limiter'})

        if self.rate_limiter:
            kwargs['rate_limiter'] = self.rate_limiter.create_object()

        module_path, class_name = self.type.rsplit('.', 1)
        module = import_module(module_path)
        cls = getattr(module, class_name)
        return cls(**kwargs)


class EmbeddingsConfig(ConfigWithType):
    """Settings for understanding text similarity.

    Example:
        ```yaml
        type: "langchain.embeddings.HuggingFaceEmbeddings"
        model_name: "all-MiniLM-L6-v2"  # Which model to use
        model_kwargs: {device: "cpu"}   # How to run it
        ```
    """
    type: str = Field(..., description='Full path to embeddings class')
    model_name: str
    model_kwargs: dict = Field(default_factory=dict)


class ContextConfig(BaseModel):
    """Settings for handling information.

    Example:
        ```yaml
        max_docs_per_source: 3      # How many docs to use
        chunk_size: 1000            # Size of each piece
        chunk_overlap: 200          # Overlap between pieces
        recreate_collection: false  # Start fresh?
        ```
    """
    max_docs_per_source: int = Field(default=3, ge=1)
    chunk_size: int = Field(default=1000, ge=100)
    chunk_overlap: int = Field(default=200, ge=0)
    recreate_collection: bool = Field(default=False)


class WorkflowConfig(BaseModel):
    """Main settings that control how the workflow runs.

    Example:
        ```yaml
        llm:         # Main AI settings
          type: "langchain.chat_models.ChatGroq"
          model_name: "mixtral-8x7b"
        embeddings:  # Text understanding
          type: "langchain.embeddings.HuggingFaceEmbeddings"
          model_name: "all-MiniLM-L6-v2"
        context:     # Information handling
          max_docs_per_source: 3
          chunk_size: 1000
        ```
    """
    llm: LLMConfig
    embeddings: EmbeddingsConfig
    context: ContextConfig = Field(default_factory=ContextConfig)


class WorkflowResult(BaseModel):
    """What you get back after running a workflow.

    Attributes:
        content: The main output text
        task_outputs: What each task produced
        loading_status: Whether information loaded correctly
    """
    content: str
    task_outputs: dict[str, dict[str, str]]
    loading_status: dict[str, str]


def load_config(path: Path) -> WorkflowConfig:
    """Reads settings from a YAML file."""
    with path.open() as f:
        raw_config = yaml.safe_load(f)
    return WorkflowConfig.model_validate(raw_config)


class Workflow:
    """Main class that runs AI workflows.

    Think of it as a smart assistant that:
    1. Reads your instructions
    2. Gets all tools ready
    3. Runs tasks in order
    4. Saves all results

    Example:
        ```python
        # Set up the workflow
        workflow = Workflow(
            config_path='config.yaml',      # How to run
            instructions_path='tasks.yaml'  # What to do
        )

        # Run and check results
        result = workflow.run()
        print(f'Output size: {len(result.content)} chars')

        # See what each task did
        for task, outputs in result.task_outputs.items():
            print(f'\nTask: {task}')
            for name, content in outputs.items():
                print(f'- {name}: {len(content)} chars')
        ```
    """

    def __init__(self, config_path: Path, instructions_path: Path):
        """Sets up a new workflow.

        Args:
            config_path: Technical settings file
            instructions_path: Task instructions file
        """
        # Load settings
        config = load_config(config_path)
        with instructions_path.open() as f:
            instructions_dict = yaml.safe_load(f)
        self._instructions = InstructionsConfig(**instructions_dict)

        # Set up AI models
        self._llm = config.llm.create_object()
        self._embeddings = config.embeddings.create_object()

        # Set up information system
        context_sources = {
            name: ContextSource(**source_config)
            for name, source_config in self._instructions.context.items()
        }
        context_config = WorkflowContextConfig(
            sources=context_sources,
            max_docs_per_source=config.context.max_docs_per_source,
            chunk_size=config.context.chunk_size,
            chunk_overlap=config.context.chunk_overlap,
            recreate_collection=config.context.recreate_collection
        )
        self._context = WorkflowContext(context_config, self._embeddings)
        self._context.setup(self._instructions.key)

        # Create task sequence
        self._graph = self._build_graph()

    def _build_graph(self) -> StateGraph:
        """Creates the sequence of tasks to run."""
        nodes = []

        for task in self._instructions.tasks:
            node = TaskNode(
                id=task.key,
                function=WorkflowGraph.create_node_function(
                    task=task,
                    instructions=self._instructions,
                    llm=self._llm,
                    context=self._context
                )
            )
            nodes.append(node)

        return WorkflowGraph.create_sequential(nodes)

    def run(self) -> WorkflowResult:
        """Runs the workflow.

        Returns:
            Results from all tasks
        """
        logger.info(f'Starting workflow: {self._instructions.key}')
        start_time = time.time()

        loading_status = self._context.load_all()
        logger.debug(f'Context loading status: {loading_status}')

        initial_state = WorkflowState(
            content='',
            context={},
            task_outputs={}
        )

        # Run all tasks
        final_state = self._graph.invoke(initial_state)
        state_dict = dict(final_state.value) if hasattr(final_state, 'value') else dict(final_state)

        # Save outputs
        workflow_output_dir = OUTPUT_DIR
        workflow_output_dir.mkdir(parents=True, exist_ok=True)

        for task in self._instructions.tasks:
            task_outputs = state_dict.get('task_outputs', {}).get(task.key, {})
            for output_config in task.outputs:
                content = task_outputs.get(output_config.key, '')
                if content:
                    # Handle different content types
                    content = (
                        content.content if isinstance(content, BaseMessage)
                        else content.get('content', content) if isinstance(content, dict)
                        else content
                    )

                    output_path = workflow_output_dir / output_config.file
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    output_path.write_text(content)
                    logger.debug(f'Saved {task.key}/{output_config.key} to {output_path}')

        total_output_size = sum(
            len(content) for outputs in final_state["task_outputs"].values() for content in outputs.values()
        )
        logger.info(
            f'Workflow {self._instructions.key} completed in {time.time() - start_time:.1f}s\n'
            f'Tasks executed: {len(self._instructions.tasks)}\n'
            f'Total output size: {total_output_size} chars'
        )

        return WorkflowResult(
            content=state_dict.get('content', ''),
            task_outputs=state_dict.get('task_outputs', {}),
            loading_status=loading_status
        )
