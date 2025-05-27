"""AI Workflows - A framework for running text-based workflows as code.

This package helps you run workflows where:
- Tasks are defined in a YAML instructions file
- Each task processes text using AI
- Information flows between tasks
- Results are saved as text files

Example:
    ```python
    from ai_workflows import setup_logging, Workflow

    # Set up logging to track progress
    setup_logging()

    # Run workflow from YAML files
    workflow = Workflow(
        config_path='path/to/config.yaml',             # Technical settings (AI models, etc.)
        instructions_path='path/to/instructions.yaml'  # Workflow definition (tasks, inputs, outputs)
    )
    result = workflow.run()

    # Check what was produced
    print(f'Generated content: {result.content}')
    ```

The YAML instructions file (instructions.yaml) is meant to be the direct counterpart of instructions files for
text-based workflows. It defines:
- What each task should do
- What information it needs
- Where to save results
- How tasks connect together

The config file (config.yaml) sets up:
- Which AI models to use
- How to handle information
- Where to find input files
- Technical parameters
"""
import os

from .config import setup_logging
from .workflow import Workflow

# Prevent tokenizer warnings
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

__all__ = ['setup_logging', 'Workflow']
