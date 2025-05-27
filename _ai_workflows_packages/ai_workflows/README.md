<div align="center">
  <h1>🤖 AI Workflows Framework</h1>
  <p><i>Transform AI Assistant Chats into Powerful Python Code</i></p>
</div>

## Why This Framework?

You love working with AI assistants - writing instructions in plain text, having natural conversations, getting quick results. But sometimes you need more:

- Want to run the same workflow reliably, again and again?
- Need to process data from multiple sources first?
- Want precise control over how the AI thinks?
- Need to integrate with your existing tools?

That's where this framework comes in. It helps you transform your text-based AI workflows into Python code that:
- Runs independently of any AI assistant
- Uses proven open-source libraries
- Gives you complete control over execution
- Adapts to your needs

## Prerequisites

1. **Python Environment**
   - Python 3.10 or higher
   - Poetry (package manager)

2. **API Access to AI Models**
   - You can for example create a free account at [Groq](https://console.groq.com) and generate an API key

## Quick Example

See the [FAQ Analysis example](_ai_workflows/code_based/faq_analysis) for a complete working example.

## Installation

1. **Get the Code**
   - Clone the repository: `git clone https://github.com/cbardyn/ai-swiss-workflows`
   - Navigate to package: `cd _ai_workflows_packages/ai_workflows`

2. **Install Dependencies**
   - Install with Poetry: `poetry install`
   - Activate environment:
     - Linux/macOS: `source .venv/bin/activate`
     - Windows: `.\.venv\Scripts\activate`

3. **Verify Installation**
   - Try running an example: `cd ../../_ai_workflows/code_based/faq_analysis/_code && python run.py`

## Step-by-Step Usage Guide

### 1. Create Your Project Structure
Create three main files in your project directory:
- config.yaml (AI configuration)
- instructions.yaml (Your workflow tasks)
- run.py (Python runner)

### 2. Write Your Instructions File
In instructions.yaml, define:
- Your workflow goal
- Tasks to perform
- Input files to analyze
- Output files to generate

Pro tip: Start with a text-based workflow in instructions_v1.0.0.md and use your AI assistant to convert it to YAML format.

### 3. Configure AI Tools
In config.yaml, specify:
- Your AI model choice (e.g., Groq's LLaMA)
- Your API key
- Model parameters (temperature, etc.)

### 4. Create Your Runner
In run.py, use the framework to:
- Set up logging
- Load your configuration
- Execute your workflow

### 5. Run Your Workflow
Simply execute: `python run.py`

## Getting Help

1. Check the [FAQ Analysis example](_ai_workflows/code_based/faq_analysis) for a complete working example
2. Review the code-based workflows [tutorial](_ai_workflows_tutorials/3_ai_workflows_as_code/)

## Framework Features

### Smart Context Management
The framework automatically:
- Loads files and URLs
- Creates searchable vector databases
- Finds relevant information for each task

### Task Orchestration
The framework handles:
- Task sequencing
- Information passing between tasks
- Progress tracking

### Error Handling
Built-in handling for:
- Missing files
- API failures
- Invalid configurations

## Possible Improvements

- More connectors to external systems (Dropbox, Google Drive, etc.)
- Better testing: No automated tests yet to ensure everything works perfectly
- Better security: API keys are stored in simple text files
- Better performance: Tasks run one after another instead of in parallel
- Better reliability: No backup AI models if the main one fails
- Better data safety: No automatic backups of your data
- Better monitoring: Can't track how well the system performs
- And more!

---

<div align="center">
  <sub>Built with ❤️ by AI Swiss</sub>
</div>
