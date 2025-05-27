# FAQ Analysis: Two Ways to Work with AI 🚀

Ever wondered how to make your AI workflows more powerful? This example shows you two ways to analyze and improve FAQs:
1. Using natural text instructions with an AI assistant
2. Using structured code that runs independently

## What This Example Does 🎯

Takes an existing FAQ and makes it better by:
- Finding questions that aren't answered yet
- Analyzing what's missing
- Suggesting new answers
- Creating a complete improvement report

## Try Both Approaches 🤝

### 1. Text Version: Quick and Interactive
Perfect for exploration and quick iterations.

```
_text/
├── run.md         # What to run
├── instructions/  # What to do
└── _output/       # Where results go
```

**To Try It:**
1. Open your AI assistant
2. Copy the content from `_text/run.md`
3. Watch the AI work through tasks
4. Discuss and refine as needed

### 2. Code Version: Structured and Independent
Perfect for automation and more control.

```
_code/
├── run.py             # Python runner
├── instructions.yaml  # Structured tasks
├── config.yaml        # AI settings
└── _output/           # Where results go
```

**To Try It:**
```bash
cd _code
python run.py
```

## ⚠️ Before You Start

1. **Set Up Python Environment**
   - Follow the [setup guide](_ai_workflows_packages/ai_workflows/README.md)
   - Make sure to activate the Python environment after installation

2. **Get API Access**
   - Create a free account at [Groq](https://console.groq.com)
   - Generate an API key
   - Add your API key to `config.yaml`:
     ```yaml
     llm:
       type: "langchain_groq.ChatGroq"
       api_key: "your-api-key-here"  # Replace with your actual key
     ```

Need help? Check the [tutorial](_ai_workflows_tutorials/3_ai_workflows_as_code/) for more information.

## Compare the Results 📊

Both versions create these files in `_output/`:
1. `1_existing_faq.md`: What's in the current FAQ
2. `2_questions_analysis.md`: What's missing
3. `3_suggestions.md`: Proposed new answers
4. `4_report.md`: Complete analysis

## When to Use Each Approach 🤔

### Text Version is Great When You:
- Want to experiment quickly
- Need to discuss ideas with AI
- Want to refine things interactively
- Don't need automation

### Code Version is Better When You:
- Want to run things automatically
- Need more control over the process
- Want to integrate with other tools
- Want independence from AI assistants

## How to Create Your Own 🛠️

### Start with Text
1. Look at `_text/instructions/instructions_v1.0.0.md`
2. See how tasks are described in plain language
3. Notice how outputs are specified clearly

### Move to Code When Ready
1. Check `_code/instructions.yaml`
2. See how the same tasks are structured
3. Notice how inputs and outputs are explicit

---

<div align="center">
  <sub>Built with ❤️ by AI Swiss</sub>
</div>
