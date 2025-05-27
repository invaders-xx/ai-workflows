| Version | Date | Description | Human |
| :- | :- | :- | :- |
| 1.0.0 | 2024-11-26 | Initial instructions | Charles-Edouard Bardyn |

# Instructions

## Goal

Generate a new instructions file for executing a project, drawing inspiration from existing instruction files.

## Requirements

IMPORTANT: Create this in the existing `_ai_workflows/factory/new_instructions/` folder, in a sub-folder `_generated/<project_name>/`:
- A folder `instructions` containing a file `instructions_v1.0.0.md`

Folder structure to create:
  ```
  _ai_workflows/factory/new_instructions/_generated/
    <project_name>/
      instructions/
        instructions_v1.0.0.md
  ```
Do NOT modify any existing files!

## Specifications

N/A

## Tasks

### 0. Input Collection
- Ask the user for all necessary inputs:
  * Description: Project description
  * Template: Instructions file template to use
  * Context: @Codebase for access to existing instructions
- Do NOTHING until ALL inputs have been provided.

### 1. Instructions File Generation
Based on the template, while also drawing inspiration from existing instruction files in @Codebase.

### 2. Validation
Verify:
- [ ] Compliance of the instructions file with the template