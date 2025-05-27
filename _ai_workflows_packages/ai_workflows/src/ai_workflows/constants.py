"""Default settings and fixed values used throughout AI workflows.

This module defines important constants that control how workflows operate:
- File and directory paths for inputs and outputs
- Default settings for processing text and documents
- Rules for prioritizing and organizing information
"""

from pathlib import Path

# Directory structure for workflows
RUN_DIR = Path('.')               # Where the workflow is being run from
WORKFLOW_DIR = RUN_DIR.parent     # Parent directory containing workflow files
OUTPUT_DIR = RUN_DIR / '_output'  # Where results and logs are saved
DATA_DIR = OUTPUT_DIR / '_data'   # Where processed data is stored

# Default settings for processing documents
DEFAULT_CHUNK_SIZE = 1000    # How many characters to include in each text chunk
DEFAULT_CHUNK_OVERLAP = 200  # How many characters should overlap between chunks
DEFAULT_MAX_DOCS = 3         # Maximum number of documents to process at once
DEFAULT_PRIORITY = 1         # Default priority level for information sources
MIN_PRIORITY = 1             # Lowest possible priority
MAX_PRIORITY = 5             # Highest possible priority

# Pattern for finding files
GLOB_PATTERN = '**/*'  # Matches all files in all subdirectories

# How to split text into meaningful parts
TEXT_SEPARATORS = [
    '\n## ',  # Headers first (markdown level 2)
    '\n\n',   # Then paragraph breaks
    '\n',     # Then line breaks
    '. ',     # Then sentence endings
    ', ',     # Then clause separators
    ' '       # Finally, individual words
]
