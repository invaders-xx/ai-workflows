"""Handles configuration settings for AI workflows.

This module manages how AI workflows are configured and run. It:
- Sets up logging to track progress
- Creates AI tools from configuration files
- Defines workflow tasks and their connections
- Structures the overall workflow instructions

Uses Pydantic models to validate all settings before running.
"""

from importlib import import_module
import logging
from typing import Any

from pydantic import BaseModel, Field

from .constants import OUTPUT_DIR


def setup_logging(level: int = logging.INFO) -> None:
    """Sets up logging to track workflow progress.

    Creates:
    1. A detailed log file in the output directory
    2. Console messages for important updates

    Args:
        level: How detailed the logging should be (default: INFO)
    """
    # Create output directory if needed
    output_dir = OUTPUT_DIR
    output_dir.mkdir(exist_ok=True)

    # Set up logging to both file and console
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(output_dir / 'run.log', mode='w'),
            logging.StreamHandler()
        ]
    )

    # Reduce noise from third-party libraries
    noisy_loggers = [
        'asyncio',
        'charset_normalizer',
        'filelock',
        'httpcore',
        'httpcore.connection',  # HTTP client internals
        'httpcore.http11',
        'httpx',
        'huggingface_hub',
        'transformers',
        'tqdm',
        'unstructured',
        'urllib3'
    ]
    for logger_name in noisy_loggers:
        logging.getLogger(logger_name).setLevel(logging.ERROR)

    # Keep important operational messages
    important_loggers = {
        'groq._base_client': logging.INFO,
        'groq': logging.INFO,
        'langchain': logging.WARNING,
        'qdrant_client': logging.WARNING,
        'sentence_transformers': logging.INFO
    }
    for logger_name, log_level in important_loggers.items():
        logging.getLogger(logger_name).setLevel(log_level)


class ConfigWithType(BaseModel):
    """Creates working objects from configuration settings.

    Example:
        ```yaml
        type: "langchain.chat_models.ChatGroq"
        model_name: "mixtral-8x7b"
        temperature: 0.7
        ```
        This creates a working ChatGroq model with those settings.

    Attributes:
        type: Full Python path to the class (e.g., 'langchain.chat_models.ChatGroq')
    """
    type: str

    def create_object(self) -> Any:
        """Creates a working instance from the configuration settings."""
        module_path, class_name = self.type.rsplit('.', 1)
        module = import_module(module_path)
        cls = getattr(module, class_name)
        kwargs = self.model_dump(exclude={'type'})
        return cls(**kwargs)


class TaskOutput(BaseModel):
    """Defines where to save a task's results.

    Example:
        ```yaml
        outputs:
          - key: "analysis"
            file: "results/analysis.md"  # Optional
        ```

    Attributes:
        file: Where to save the output (optional)
        key: Name to identify this output
    """
    file: str | None = None
    key: str


class TaskInputType(BaseModel):
    """Specifies where a task gets its input from.

    Example:
        ```yaml
        inputs:
          - from_context: ["docs", "examples"]
          - from_tasks: [["analyze", "summary"]]
        ```

    Attributes:
        from_context: Names of information sources to use
        from_tasks: List of [task_name, output_name] pairs
    """
    from_context: list[str] | None = None
    from_tasks: list[tuple[str, str]] | None = None


class TaskConfig(BaseModel):
    """Configuration for one step in the workflow.

    Example:
        ```yaml
        key: "analyze_text"
        description: "Find key themes in the text"
        inputs:
          - from_context: ["source_text"]
        outputs:
          - key: "themes"
            file: "themes.md"
        ```

    Attributes:
        key: Unique name for this task
        description: What this task should do
        inputs: Where to get input data
        outputs: What to do with results
    """
    model_config = {'extra': 'forbid'}

    key: str = Field(..., description='Unique name for this task')
    description: str = Field(..., description='What this task should do')
    inputs: list[TaskInputType] = Field(..., description='Where to get input data')
    outputs: list[TaskOutput] = Field(default_factory=list, description='How to handle results')


class InstructionsConfig(BaseModel):
    """The complete workflow configuration.

    Example:
        ```yaml
        key: "text_analysis"
        version: "1.0.0"
        goal: "Find key themes in documents"
        requirements: "Need text files and AI model"
        specifications: "Focus on main topics"
        context:
          docs: {type: "folder", path: "./docs"}
        tasks:
          - key: "analyze"
            description: "Extract themes..."
        ```

    Attributes:
        key: Unique name for this workflow
        version: Version number
        goal: What to achieve
        requirements: What's needed
        specifications: Rules to follow
        context: Available information sources
        tasks: Steps to execute
    """
    model_config = {'extra': 'forbid'}

    key: str = Field(..., description='Unique name for this workflow')
    version: str = Field(..., description='Version number')
    goal: str = Field(..., description='What to achieve')
    requirements: str = Field(..., description='What needs to be done')
    specifications: str = Field(..., description='Rules to follow')
    context: dict = Field(..., description='Available information')
    tasks: list[TaskConfig] = Field(..., description='Steps to execute')
