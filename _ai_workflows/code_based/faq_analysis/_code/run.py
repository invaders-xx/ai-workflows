"""Script that runs an AI workflow from YAML configuration files.

This script:
1. Sets up logging to track progress
2. Loads workflow settings from config.yaml and instructions.yaml
3. Runs the workflow
4. Handles any errors that occur

The workflow itself and what it does is defined in the YAML files:
- config.yaml: Technical settings (AI models, etc.)
- instructions.yaml: What tasks to run and how they connect
"""

import logging
from pathlib import Path

from ai_workflows import setup_logging, Workflow


def main() -> None:
    """Runs the workflow defined in the YAML files.

    Steps:
    1. Sets up logging
    2. Finds the configuration files
    3. Creates and runs the workflow
    4. Handles any errors

    Note:
        The workflow results contain:
        - loading_status: Whether each information source loaded correctly
        - task_outputs: What each task produced
        - content: Final result (usually text)
        This can be logged or saved to a file.
    """
    # Set up logging (with INFO level for base messages, DEBUG for details)
    setup_logging(logging.INFO)
    logger = logging.getLogger(__name__)

    # Find configuration files
    current_dir = Path(__file__).parent
    config_path = current_dir / 'config.yaml'
    instructions_path = current_dir / 'instructions.yaml'

    try:
        # Create and run the workflow
        workflow = Workflow(
            config_path=config_path,             # Technical settings
            instructions_path=instructions_path  # What to do
        )
        result = workflow.run()

        logger.info('\nFinal content:')
        logger.info(result.content)
        # Optional: Log additional results

    except Exception as e:
        logger.error(f'Workflow execution failed: {e}', exc_info=True)
        raise


if __name__ == '__main__':
    main()
