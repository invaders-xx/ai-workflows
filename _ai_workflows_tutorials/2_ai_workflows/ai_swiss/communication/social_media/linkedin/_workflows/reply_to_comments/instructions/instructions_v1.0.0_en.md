| Version | Date | Description | Human |
| :- | :- | :- | :- |
| 1.0.0 | 2024-11-26 | Initial instructions | Charles-Edouard Bardyn |

# Instructions

## Goal

Generate personalized response options to recent comments on AI Swiss members' LinkedIn posts.

## Output

IMPORTANT: Create all your files in the `ai_swiss/communication/social_media/linkedin/_workflows/reply_to_comments/` folder, in a `_generated` subfolder. Nowhere else.

## Requirements

- Consistency with each member's tone on LinkedIn

## Specifications

- Writing style:
  * Professional
  * In line with the person on whose behalf you are writing

## Documentation

N/A

## Tasks

### 0. Input collection
- Ask the user for all necessary inputs:
  * Link(s) to posts containing comments to process
  * Link to posts of the person on whose behalf you must write responses
- Do NOTHING until ALL inputs have been provided.

### 1. Comment analysis
- Identification of unanswered comments
- Categorization of comments (question, feedback, suggestion, etc.)

### 2. Context analysis
- Evaluation of comment tone
- Identification of key points to address

### 3. Response generation (`reply_to_comments.md`)
- Writing 5 possible responses for each comment

### 4. Quality control
- Verify:
  * [ ] Tone and style consistent with the person on whose behalf you are writing
  * [ ] Length within LinkedIn limits 