# 🚀 "Industrialize" your AI workflows

> "AI is just a tool - your methodology makes the difference between amateur and professional."

AI is revolutionizing how we work, but having access to GPT-4 or Claude isn't enough. The key? A solid methodology. A workflow is your recipe for success: a series of documented steps that transform a complex task into a reliable and feasible process. In this tutorial, we'll explore how to move from "testing AI" to "mastering AI".

## 💡 Why industrialize your AI workflows?

Let's imagine two scenarios:

**Scenario A: The amateur approach**
```
Prompt → AI → Result → Hope
```
- ❌ "Works half the time"
- ❌ "Only Peter knows how to do it"
- ❌ "Impossible to train the team"
- ❌ "Quality? Cross your fingers"

**Scenario B: The pro approach**
```
Proven workflow → Systematic validation → Continuous improvement → Excellence
```
- ✅ "Works every time"
- ✅ "Anyone can do it"
- ✅ "30-minute training"
- ✅ "Guaranteed quality"

The difference? **A structured methodology.**

## 💡 The three pillars of an industrialized workflow

Here's my recipe for transforming chaos into excellence. It's not the only possible way, but it has the advantage of being simple and proven, and to my knowledge still unknown:

### 1. The structure - Your GPS to success
```
my_project/
└── _workflows/
    └── use_case/
        ├── instructions/
        │   └── instructions_v1.0.0.md
        └── run.md
```

This architecture is your foundation:
- `_workflows/`: Your library of proven solutions
- `use_case/`: Organized by use case
- `instructions/`: The detailed manual for each workflow
- `run.md`: Your "Action!" button

### 2. Versioning - Your quality assurance
Each workflow is versioned (v1.0.0) to:
- 📈 Track your progress
- 🔄 Return to stable versions when needed
- 🤝 Facilitate teamwork

### 3. Validation - Your guarantee of excellence
A `__validation_required` suffix is automatically added to the end of AI-generated file names, as your safeguard to:
- ⚡ Instantly identify elements to verify
- 🎯 Force quality verification
- 💪 Sleep soundly

## 🛠️ Anatomy of a workflow

Let's dive into a concrete example: generating a LinkedIn post for an event.

### The instructions file - Your recipe for success

First, we need a recipe for the workflow. Here's what ours looks like, inspired by the template available under `_workflows/templates/instructions_v1.0.0.md`:

```markdown
| Version | Date       | Description      | Author |
|---------|------------|------------------|---------|
| 1.0.0   | 2024-11-26| Initial version  | Charles-Edouard Bardyn |

# Instructions

## Purpose
Generate a detailed invitation for a Brain2Brain.Lab event
👉 A clear goal = precise results

## Output
- `linkedin_post.md` in the event folder
👉 We know exactly what we want

## Requirements
- Format consistent with past invitations
👉 Consistency is key

## Specifications
- Writing style:
  * Professional but accessible
  * Direct and concise, gets to the point
  * Educational and well-structured
  * Authentic and personal
  * Pragmatic, focus on applicability
  * Touch of humor when relevant
  * Clear and spacious structure
👉 Precise criteria = no surprises

## Tasks
1. Input collection
   - Event information
   - Examples of past LinkedIn posts
2. Introduction writing
   - Catchy title
   - Direct and concise summary
3. Main content writing
   - Key learning points
   - Target audience
4. Quality control
👉 A clear action plan
```

### The execution file - Your dashboard

Next, we create a `run.md` file as a cockpit to launch a workflow. Simple but powerful:

```markdown
# LinkedIn Post

## Instructions
@instructions_v1.0.0.md

## Input
- Event details: @2024-11-26_workflows_ia/raw_information.md
- Examples of past LinkedIn posts: @events

@
```

## 🎓 How to launch a workflow

Once your workflow is ready, launching it is simple:

1. Open Composer (CMD + I (MacOS) or CTRL + I (Windows))
2. Create a new conversation
3. Copy-paste the contents of your `run.md` file
4. Press Enter

The AI will then:
1. Read the referenced instructions (@instructions_v1.0.0.md)
2. Analyze the provided inputs (like @raw_information.md)
3. Execute the requested tasks
4. Produce a result for validation (with `__validation_required` suffix)

**Tip**: Co-creation is a dialogue. If the result isn't perfect:
- Explain what's wrong ("The tone isn't professional enough")
- Suggest adjustments ("Can you make it more formal?")
- Let the AI adjust
- Iterate until satisfied

You can review the previous Brain2BrainLab video for more details on co-creation: https://www.youtube.com/watch?v=niPQvA7uxxk

## 🎓 How to start with a new workflow

### 1. Choose your first win
Start with a task that:
- You do frequently
- You know how to recognize success
- Needs consistent results (same quality every time)

**Tip**: Why reinvent the wheel? Take a look at existing workflows in the `_workflows/` folders. You can also use the "Factory workflow" described below to create a workflow more quickly.

### 2. Structure your approach
1. Use the Factory workflow to generate the basic structure
2. Draw inspiration from similar existing workflows
3. Write instructions based on examples
4. Test the run.md

**Tip**: Start simple, iterate often

### 3. Validate and improve
- Test with different inputs
- Collect feedback
- Refine instructions
- Share with colleagues for example to enrich the workflow library

## 🌟 Best practices

### For instructions
- ✅ **Be specific**
  * ❌ "Write a good post"
  * ✅ "Write a LinkedIn post of 1000-1200 characters about event X"

- ✅ **Include examples**
  * ❌ "Use the right tone"
  * ✅ "Use a professional but accessible tone, as in @examples/post_123.md"

- ✅ **Define clear validation criteria**
  * ❌ "Check that it's good"
  * ✅ "Verify: correct length, all key points present, clear call-to-action"

### For execution
- ✅ **One goal per workflow**
  * ❌ "Create the LinkedIn post and newsletter"
  * ✅ "Create the LinkedIn post" (use a separate workflow for the newsletter)

- ✅ **Standardized inputs**
  * ❌ "Get the info somewhere in the folder"
  * ✅ "Use @event_details.md as the main source"

- ✅ **Explicit validation points**
  * ❌ "Check everything is fine"
  * ✅ "Validate:
    1. Format respected
    2. Consistent tone
    3. Key message present"

### For maintenance
- ✅ **Document changes**
  * Update the version (v1.0.0 → v1.0.1)
  * Note modifications in history
  * Explain why (not just what)

- ✅ **Keep track of successes**
  * Keep the best examples
  * Note positive feedback
  * Share successful use cases

- ✅ **Iterate intelligently**
  * Don't change everything at once
  * Test modifications one by one
  * Validate before moving forward

## 📚 Examples of workflows in production

### 0. Tutorial workflow - The meta-example 🤓
```
ai_swiss/events/brain2brainlab/2024-11-26_workflows_ia/_workflows/tutorial/
└── instructions/
    └── instructions_v1.0.0.md
└── run.md
```
- 🎯 **Purpose**: Create this tutorial you're reading right now
- ✨ **Special feature**: A workflow that explains itself!
- 📥 **Inputs used**:
  * Existing workflows (@ai_swiss) for inspiration
  * Formatting rules (@.cursorrules) for consistency
- 🔑 **Result**: The guide you're currently reading

### 1. New workflow workflow - The workflow creator
```
_workflows/factory/new_workflow/
└── instructions/
    └── instructions_v1.0.0.md
└── run.md
```
- 🎯 **Purpose**: An assistant for creating new workflows
- ✨ **Special feature**: Generates the complete structure of a new workflow
- 🔑 **Usage**: When you want to create a new workflow from a vague idea
- 💡 **Example**: "I'd like to create a workflow for sending personalized outreach emails based on LinkedIn profiles" → The New workflow workflow generates all necessary files

### 2. New instructions workflow - The instructions generator
```
_workflows/factory/new_instructions/
└── instructions/
    └── instructions_v1.0.0.md
└── run.md
```
- 🎯 **Purpose**: An assistant for creating a new instructions file
- ✨ **Special feature**: Focuses on the instructions part, the heart of a workflow
- 🔑 **Usage**: When you want to complete a project once, without necessarily creating a workflow to do it again
- 💡 **Example**: "I'd like to create a chatbot with Langchain" → The New instructions workflow generates an appropriate instructions_v1.0.0.md file

### 3. LinkedIn post workflow - The communicator
```
ai_swiss/events/_workflows/communication/linkedin_post/
└── instructions/
    └── instructions_v1.0.0.md
└── run.md
```
- 🎯 **Purpose**: Generate engaging LinkedIn posts
- ✨ **Special feature**: Maintains a consistent voice on social networks
- 🔑 **Usage**: Event communication that hits the mark

### 4. Reply to comments workflow - The engager
```
ai_swiss/communication/social_media/linkedin/_workflows/reply_to_comments/
└── instructions/
    └── instructions_v1.0.0.md
└── run.md
```
- 🎯 **Purpose**: Personalized responses to LinkedIn comments
- ✨ **Special feature**: Responds while preserving your tone
- 🔑 **Usage**: Community engagement

### 5. Issue contribution workflow - The developer
```
code/community/contributions/langchain/_workflows/issue_contribution/
└── instructions/
    └── instructions_v1.0.0.md
└── run.md
```
- 🎯 **Purpose**: Contribute effectively to open source
- ✨ **Special feature**: Structures problem-solving from analysis to code production
- 🔑 **Usage**: Active participation in open source projects

## 🎓 What these workflows teach us

### 1. Specialization
Each workflow has its mission:
- 📚 Tutorial: Training, documentation
- 🏭 Factory: Creation of new structured workflows
- 📢 LinkedIn Post: Event communication
- 💬 Reply: Social media engagement
- 🛠️ Issue: Code development

### 2. Hierarchy
A clear organization for effective workflows:
```
_workflows/
└── use_case/
    ├── communication/
    └── development/
```

### 3. Reusability
Solid foundations for all workflows:
- 📋 Standardized structure = intuitive navigation
- 🔄 Consistent versioning = controlled evolution
- ✅ Systematic validation = guaranteed quality

## 🎯 Beyond textual workflows

The workflows we've seen so far are designed to dialogue directly with AI through textual instructions. This is perfect for most cases. But sometimes, you'll need more power.

Let's take an example: a law firm that wants to automate legal document drafting based on legal texts. This case requires:
- Absolute precision
- Multiple data sources
- Complex validation
- Complete automation

This is where programmed workflows come in (which we won't cover in depth today).

### Textual vs. programmed workflows

**Textual workflows (this guide)**
- ✅ Natural conversation with AI
- ✅ Set up in minutes
- ✅ Accessible to everyone
- ✅ Perfect for daily tasks
- ❌ Limited for fine-tuned automation

**Programmed workflows**
- 🔧 Coded in Python or other languages
- 🔧 Use specialized libraries (Langchain, etc.)
- 🔧 Total automation possible
- 🔧 Integration with other systems
- ❌ Require technical skills

### How to create a programmed workflow (overview)?

1. **Start as usual**
   ```
   project/
   └── instructions/
       └── instructions_v1.0.0.md
   ```
   Describe your project as a workflow, using for example the template available in `_workflows/templates/instructions_v1.0.0.md`, detailing:
   - Purpose
   - Requirements
   - Specifications
   - Documentation
   - Tasks

2. **Co-create code on Composer**
   - Develop step by step with AI
   - Test each component
   - Document technical choices
   - Keep track of trials/errors

3. **Industrialize**
   - Version your code (git)
   - Add automated tests
   - Document installation/usage
   - Plan for maintenance

This hybrid approach gives you the best of both worlds:
- The productivity gain of AI workflows
- The power of code

## 🎯 Next steps

1. **Today** - Your first win
   - Choose a simple workflow
   - Use the Factory workflow
   - Do a first test
   - Celebrate your success!

2. **This week** - Consolidation
   - Refine instructions
   - Share with friends, colleagues
   - Gather feedback

3. **This month** - Expansion
   - Identify your use cases
   - Create your library
   - Train your team
   - Measure gains

## 💫 Conclusion

Industrializing AI workflows isn't just about organization - it's a transformation of how you work with AI. By following this methodology and building on existing workflows, you're laying the foundations for professional, scalable, and reliable AI use.

Technology will continue to evolve, but the principles seen here - structure, validation, continuous improvement - will remain relevant. It's your methodology on flexible interfaces that makes the difference, not the raw power of AI or consumer interfaces.

Start small, but start now. Each structured workflow is a step toward operational excellence.

---

Copyright 2024 Cursor AI (with help from Charles-Edouard Bardyn, executing the Tutorial workflow)

**Note**: This tutorial is alive! Don't hesitate to share your feedback and improvements. The strength of workflows also comes from the community that uses and evolves them.

## 📚 Glossary

- **Workflow**: Series of steps to follow to accomplish a task
- **Prompt**: Message or instruction given to AI
- **Versioning**: System for numbering versions (v1.0.0, v1.0.1, etc.)
- **Input**: Information provided as input
- **Output**: Result produced by the workflow
- **Validation**: Quality verification of the result
- **Iteration**: Progressive improvement cycle
- **Factory workflow**: Special workflow that helps create other workflows
- **LLM**: Large Language Model, the type of AI used here
- **Co-creation**: Creation process in collaboration with AI
