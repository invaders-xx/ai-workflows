| Version | Date | Description | Human |
| :- | :- | :- | :- |
| 1.0.0 | 2024-11-26 | Initial instructions | Charles-Edouard Bardyn |

# Instructions

## Goal

Generate the necessary files for a new workflow, taking inspiration from existing workflows.

## Requirements

IMPORTANT: Create these files in the existing `_ai_workflows/factory/new_workflow/` folder, in a sub-folder `_generated/<workflow_name>/`:
- A new `run.md` file
- An `instructions` folder containing a file `instructions_v1.0.0.md`

Folder structure to create:
  ```
  _ai_workflows/factory/new_workflow/_generated/
    <workflow_name>/
      instructions/
        instructions_v1.0.0.md
      run.md
  ```
Do NOT modify any existing files!

## Specifications

N/A

## Tasks

### 0. Input Collection
- Ask the user for all necessary inputs:
  * Description: Description of the workflow
  * Context: @Codebase for access to existing workflows
- Do NOTHING until ALL inputs have been provided.

### 1. Workflow File Generation
Taking inspiration from existing workflows in @Codebase.

### 2. Validation
Verify:
- [ ] The workflow's consistency with the given description
