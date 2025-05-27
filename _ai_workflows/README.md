<div align="center">
  <h1>🏭 AI Workflows Library</h1>
  <p><i>Turn Complex AI Tasks into Simple, Repeatable Steps</i></p>
</div>

## What's This Library For?

Ever wished you could:
- Save your best AI conversations and reuse them?
- Share your AI expertise with your team?
- Make sure AI gives you consistent results?
- Build on what works instead of starting from scratch?

That's exactly what this library helps you do! Think of it as your collection of AI recipes that:
- Work reliably every time
- Get better with each use
- Anyone can learn and apply
- Scale across teams

## Getting Started

### 1. Use an Existing Workflow
It's as simple as:
1. Open Cursor AI's Composer (CMD/CTRL + I)
2. Copy any `run.md` file content
3. Fill in your specific details
4. Press Enter and watch it work!

### 2. Create Your Own Workflow
The easiest way:
1. Go to `factory/new_workflow/`
2. Follow the steps in `run.md`
3. Get a professional workflow in seconds

## Library Organization

```
_ai_workflows/
├── code_based/            # Workflows with Python automation
│   └── faq_analysis/      # Example: FAQ improvement workflow
├── factory/               # Create new workflows
│   ├── new_workflow/      # Complete workflow template
│   └── new_instructions/  # Single task template
├── templates/             # Reusable patterns
└── text_based/            # Text-only workflows
```

## Two Ways to Use Workflows

### 1. Text-Based Workflows
Perfect for when you want to:
- Experiment quickly
- Discuss ideas with AI
- Refine things interactively
- Keep things simple

### 2. Code-Based Workflows
Better when you need to:
- Run things automatically
- Have more control
- Integrate with other tools
- Be independent from AI assistants

## Types of Workflows

### Complete Workflows
For processes you'll repeat:
```
workflow_name/
├── instructions/    # Step-by-step guide
│   └── instructions_v1.0.0.md
└── run.md          # Ready to execute
```

### Single Instructions
For one-time complex tasks:
```
project_name/
└── instructions_v1.0.0.md
```

## Best Practices

### Keep Track of Changes
- Use version numbers (v1.0.0)
- Document what changed
- Keep previous versions

### Ensure Quality
- Files start with `__validation_required`
- Always check the results
- Remove the suffix after validation
- Test with different inputs

### Design Guidelines
- One clear goal per workflow
- Standard inputs and outputs
- Clear success criteria
- Regular improvements

## Try an Example

Check out the FAQ analysis workflow in `code_based/faq_analysis/`:
- Text version for quick experiments
- Code version for automation
- Complete documentation
- Ready to use!

## Learn More

- Start by creating your own workflow with our [factory](factory/new_workflow/run.md)
- Check out the [tutorials](_ai_workflows_tutorials/README.md)

## Want to Contribute?

1. Try existing workflows
2. Test in your projects
3. Document what you learn
4. Share improvements

---

<div align="center">
  <sub>Built with ❤️ by AI Swiss</sub>
</div>
