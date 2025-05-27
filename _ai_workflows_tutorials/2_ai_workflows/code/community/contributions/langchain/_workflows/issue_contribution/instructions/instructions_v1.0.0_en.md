| Version | Date | Description | Human |
| :- | :- | :- | :- |
| 1.0.0 | 2024-11-26 | Initial instructions | Charles-Edouard Bardyn |

# Instructions

## Goal

Analyze a project issue (e.g., GitHub) and generate clear instructions to resolve it, without modifying the source code.

## Output

IMPORTANT: Create all your files in the existing `code/community/contributions/langchain/_workflows/issue_contribution` folder and `_<ticket_number>/` subfolder. Nowhere else.

## Tasks

### 0. Input Collection
- Request all necessary inputs from the user:
  * Issue: Ticket URL
  * Code: Project source code folder
  * Guidelines: Link to project contribution guidelines
  * Template: Template to use for creating `instructions_v1.0.0.md`
- Do NOT proceed until ALL inputs have been provided.

### 1. Technical Analysis (`1_technical_analysis.md`)
- Identify the core problem
- Analyze the impacted code
- Document technical constraints
- List dependencies

### 2. Implementation Proposals (`2_implementation_options.md`)
- Identify 3-5 possible approaches
- For each approach:
  * Technical description
  * Pros/Cons
  * Estimated complexity
- Recommend the best approach

### 3. Contribution Instructions (`instructions_v1.0.0.md` in a `3_contribution_workflow/` subfolder)
- Create the instructions file according to the provided template
- Include tests and validation criteria

### 4. Final Validation
- Check document consistency
- Confirm guidelines compliance
- Validate instruction completeness
- Validation criteria:
  * [ ] Template followed
  * [ ] Impact on existing code minimized
  * [ ] Project guidelines respected
  * [ ] Tests well defined 