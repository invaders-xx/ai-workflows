| Version | Date | Description | Human |
| :- | :- | :- | :- |
| 1.0.0 | 2024-12-17 | Initial instructions | Charles-Edouard Bardyn |

# Instructions

## Goal

Analyze an existing FAQ, identify uncovered questions, and generate answer suggestions to enrich the FAQ.

## Requirements

- Extract Q&A pairs from a URL
- Analyze new user questions
- Generate relevant suggestions

## Specifications

### Writing style for suggested answers
- Professional and clear
- Concise but complete
- Consistent with existing answers' style
- Structured for easy reading

### Output

IMPORTANT: Create all your files in the existing folder `2024-12_workflows_ia_code/_ai_workflows/code_based/faq_analysis/_text/` and subfolder `_output/`. Nowhere else.

## Tasks

### 0. Input Collection
- Ask the user for all necessary inputs:
  * URL of the FAQ to analyze
  * Markdown file containing new questions
- Do NOTHING until ALL inputs have been provided.

### 1. Existing FAQ Extraction (`1_existing_faq.md`)
- Analyze the provided web page
- Extract ALL question-answer pairs
- Structure the data as follows:
  ```markdown
  # Existing FAQ
  
  ## Extracted Q&As
  ### Q1: <question>
  <answer>
  
  ### Q2: <question>
  <answer>

  Etc.
  ```

### 2. New Questions Analysis (`2_questions_analysis.md`)
- Compare with existing FAQ
- Identify uncovered questions
- Evaluate relevance for the FAQ
- Record in this format:
  ```markdown
  # New Questions Analysis
  
  ## Uncovered Questions
  1. <question>
     - Relevance: <score/5>
     - Justification: <why this question is relevant>
  
  ## Questions Similar to Existing Ones
  1. <new question>
     - Corresponds to: Q<n> in existing FAQ
     - Differences: <analysis of nuances>
  ```
- Don't skip any question!

### 3. Suggestions Generation (`3_suggestions.md`)
For each relevant new question:
- Generate 3 different answer proposals
- Adapt style to match existing FAQ tone
- Record in this format:
  ```markdown
  # Answer Suggestions
  
  ## Question 1: <question>
  
  ### Suggestion 1.1
  <answer>
  
  ### Suggestion 1.2
  <answer>
  ```

### 4. Report Production (`4_report.md`)
Create a report consolidating:
- Analysis summary
- List of new questions
- Answer suggestions
- Prioritization recommendations based on relevance scores

### 5. Validation
Verify:
- [ ] Complete extraction of existing FAQ
- [ ] Relevance of identified new questions
- [ ] Quality and consistency of suggested answers
- [ ] Report format and structure