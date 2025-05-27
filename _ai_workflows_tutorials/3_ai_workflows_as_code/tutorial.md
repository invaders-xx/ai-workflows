<div align="center">
  <h1>🤖 AI Workflows Framework</h1>
  <p><i>From AI Assistant Chats to Standalone Code</i></p>
</div>

## Why This Framework?

Imagine you're writing instructions for an AI assistant like Cursor AI. It's intuitive - you write what you want in plain text, discuss details with the AI, and get results. But sometimes you need more:
- What if you need to process data from external sources first?
- What if you want to run the same workflow automatically, without opening an AI assistant?
- What if you want more control over how the AI processes your instructions?

That's where this framework comes in. It helps you transform your text-based workflows into Python code that:
- Runs independently of any AI assistant
- Uses open-source libraries you control
- Gives you more power over the execution

## Understanding the Two Approaches

### Text-based Workflows: Powerful but Sometimes Limited
```
You → Write instructions in plain text → Chat with AI assistant → Get results
```

**Perfect When You Need:**
- Quick experimentation
- Natural back-and-forth with AI
- Easy modifications on the fly
- No coding required

**Not Great When You Need:**
- To process external data first
- To run things automatically
- To integrate with other systems
- Precise control over execution

### Code-based Workflows: More Powerful but Less Interactive
```
You → Write structured YAML → Run Python code → Get results
```

**Perfect When You Need:**
- Independence from AI assistants
- Automated execution
- Integration with other tools
- More control over the process

**Not Great When You Need:**
- Quick changes on the fly
- To discuss edge cases with AI
- To explore creative solutions
- To avoid writing code

## How This Framework Helps

We've created tools (in `_ai_workflows_packages/ai_workflows/`) that help you:

1. **Keep Writing Simple Instructions**
   ```yaml
   # instructions.yaml - Still readable like text!
   goal: |
     Analyze an FAQ and suggest improvements
   tasks:
     - Extract Q&A from website
     - Analyze gaps in coverage
     - Generate new answer suggestions
   ```

2. **Choose Your AI Tools**
   ```yaml
   # config.yaml - Pick the AI models you want
   llm:
     type: "langchain_groq.ChatGroq"
     model_name: "llama-3.3-70b-versatile"
   ```

3. **Run Anywhere**
   ```python
   # Simple Python code to execute your workflow
   from ai_workflows import Workflow
   
   workflow = Workflow('config.yaml', 'instructions.yaml')
   result = workflow.run()
   ```

## See It In Action: FAQ Analyzer

Let's look at a real example that:
- Reads FAQs from websites
- Finds gaps in coverage
- Suggests new answers

### 1. First, Try It as a Text Workflow
In `_ai_workflows/code_based/faq_analysis/_text/`:

1. **Write Simple Instructions**
   ```markdown
   # Instructions
   1. Extract FAQ from website
   2. Analyze new questions
   3. Suggest answers
   4. Create report
   ```

2. **Run in Your AI Assistant**
   - Copy the content from `run.md`
   - Chat with the AI about results
   - Refine as needed

### 2. Then, Try It as Code
In `_ai_workflows/code_based/faq_analysis/_code/`:

1. **Same Instructions, More Structure**
   ```yaml
   tasks:
     - key: 'extract_faq'
       description: 'Get Q&A from website'
     - key: 'analyze_questions'
       description: 'Find gaps'
   ```

2. **Run Anywhere**
   ```bash
   python run.py
   ```

Both create the same outputs in `_output/`:
- FAQ extracted from website
- Analysis of missing topics
- Suggested new answers
- Complete report

But the code version:
- Runs without an AI assistant
- Gives you more control
- Integrates better with other tools
- Handles errors better

## Try It Yourself

1. **Set Up (One Time)**
   ```bash
   # Get the code
   git clone https://github.com/cbardyn/ai-swiss-workflows
   cd _ai_workflows_packages/ai_workflows
   
   # Install dependencies
   poetry install
   source .venv/bin/activate  # (or .\.venv\Scripts\activate on Windows)
   ```

2. **Run the Example**
   ```bash
   cd ../../_ai_workflows/code_based/faq_analysis/_code
   python run.py
   ```

3. **Create Your Own**
   - Start with text instructions
   - Convert to YAML when ready
   - Configure your AI tools
   - Run independently

## When to Use What

### Stay with Text When:
- You're exploring new ideas
- You need AI's creative input
- You want quick iterations
- You don't need automation

### Move to Code When:
- You need automation
- You want more control
- You need to integrate with other tools
- You want independence from AI assistants

## Learn More
- Framework details: `_ai_workflows_packages/ai_workflows/README.md`
- Examples: `_ai_workflows/code_based/*/README.md`

---

<div align="center">
  <sub>Built with ❤️ by AI Swiss</sub>
</div>
