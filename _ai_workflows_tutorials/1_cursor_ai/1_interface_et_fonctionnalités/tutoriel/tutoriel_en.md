# Welcome to the World of Cursor!

## First: Why a Tutorial in ".md" Format?

The file you're currently reading is in "Markdown" (.md). It's a text format that allows you to describe formatting directly in the text, rather than clicking buttons and menus. Instead of selecting text and clicking "Italic" like in Word, you simply add two asterisks around the text. Simple and efficient!

The advantage? First, the formatting works everywhere. That's why Markdown is very popular, from personal note-taking to technical documentation writing.

The advantage here? It's the ideal format for writing instructions for AI.

### Markdown Essentials

#### Headings

To create a heading, use the `#` symbol. The more `#` you add, the smaller the heading:
# Large heading
## Medium heading
### Small heading
#### Etc.

#### Styled Text

- *For italics*, surround with *asterisks*
- **For bold**, use **two asterisks**
- To combine both: ***bold italic text***

#### Lists

For a simple list:
- One item
- Another item
  - A sub-item (with 2 spaces before the dash)
  - Another one

For a numbered list:
1. First thing
2. Second thing
   1. Sub-point
   2. Another sub-point

#### Links

To create a link, it's like a mini-equation:
[What people see](the-link-address)

For example: [The AI Swiss website](https://www.a-i.swiss)

### To Learn More

- [Markdown Guide in English](https://joplinapp.org/help/apps/markdown/)
- [Online Markdown Editor](https://dillinger.io/) to practice

The best way to learn? Experiment directly in this file! Modify the text and observe the result.

## Let's Get to the Heart of the Matter: Why Cursor?

Now that you've mastered the basics of Markdown, let's discover the tool that will transform your way of working:

[Cursor AI (or Cursor)](https://cursor.com) is an intelligent file editor that revolutionizes your way of working with AI. It's based on [VS Code](https://code.visualstudio.com/), Microsoft's very popular code editor.

Cursor evolves alongside VS Code, benefiting from all its features while enriching it with increasingly powerful AI capabilities.

Cursor is often perceived as a tool reserved for developers, but we'll prove that's wrong: if a tool can handle thousands of interconnected code files, maintain context across different programming languages, and orchestrate coherent modifications on a large scale... wouldn't it be perfect for other types of complex projects?

At AI Swiss, we're convinced that Cursor is currently (as of 2024-11-12) the most powerful editor for working with AI, and we'll show you why.

**Note**:

Cursor is **currently** (as of 2024-11-12) the most powerful tool for working with AI, but the field is evolving rapidly: [GitHub Copilot](https://github.com/features/copilot), also based on VS Code, offers an experience that's approaching Cursor's and could one day become superior.

Rest assured, the methods we'll explore are transferable to any tool.

### Cursor's Strengths

1. **Everything in One Place**
   No more juggling between applications. You can create, organize, and modify your files with AI in the same place.

2. **Context Galore**
   Unlike ChatGPT and its peers, Cursor can take into account all the files in your project. This allows for much more relevant interactions.

3. **Efficient Interface and Shortcuts**
   This is the advantage of a tool designed for coders: there are shortcuts for everything.
   - `Ctrl/⌘ + L` to open a conversation with AI
   - `Ctrl/⌘ + K` to ask for AI help at any specific location
   - `Ctrl/⌘ + I` for intelligent multi-file editing with "Composer", unleashing Cursor's full power as we'll see later
   - Etc.

Ready to explore this magical but real world? Let's go!

### Installation (probably already done)

1. Download Cursor from [cursor.com](https://cursor.com)
2. Install it like any other application

For VS Code users: you can import your existing settings at first launch.

### Cursor AI, GitHub Copilot...: Powerful Tools, Yes, But Never Free

Powerful AI models like Claude 3.5 Sonnet or GPT-4o have become basic infrastructure for AI tools. And all infrastructure has a cost. You have three options (in order of recommendation):

1. **Cursor Pro**
   - USD 192.00 per year (or USD 16.00 per month)
   - Access to major cutting-edge models (Claude 3.5 Sonnet, GPT-4o, etc.)

2. **GitHub Copilot**
   - USD 100.00 per year (or USD 8.33 per month)
   - Access to major cutting-edge models (Claude 3.5 Sonnet, GPT-4o, etc.)
   - Also based on VS Code, but currently with more limited AI features (even in the new Copilot Spark).

You can also use Cursor by providing access to models via API keys, thus paying for model access to other providers like OpenAI. The disadvantage is that costs are often higher in the end, and Cursor's models enabling intelligent autocompletion notably won't be available. See [here](https://docs.cursor.com/advanced/api-keys) for details.

### Privacy and Security

Cursor and its peers (GitHub Copilot, notably) take data protection very seriously as they are used for code in large companies.

By activating "Privacy Mode" in Cursor's settings (important!), you ensure in principle that:
  - No data is stored
  - No data is used for model training
  - No data is shared with third parties

The details:
- [Security Policy](https://www.cursor.com/security)
- [Privacy Policy](https://www.cursor.com/privacy)

## Let's Move on to the Fun Part: Cursor's Magical Features!

### The Essential AI Chat

Chat has become the basic interface for interacting with AI. To use it in Cursor:

1. Open the chat with `Ctrl/⌘ + Alt/Option + L` (L for "Light of supreme knowledge")
2. Select an AI model (at AI Swiss, we have a soft spot for `claude-3-5-sonnet`, as of 2024-11-12)
3. Ask a question (make a "prompt")
4. Validate with `Enter` or click `Chat`

Several options are available for each message:
- `Edit` to refine your prompt
- `Reply` above each AI response to reply specifically to it
- `Copy message` to copy a message to the clipboard

#### Practical Example

1. Open the chat (`Ctrl/⌘ + Alt/Option + L`)
2. Select `claude-3-5-sonnet`
3. Write a prompt like:
   "What is the meaning of life, the Universe, and everything?"
4. Observe the response.

You'll notice here that the responses are framed by "---". This is due to our `.cursorrules` file that defines a response style. We'll see that later.

#### Conversation History

Cursor offers two methods to access history:

1. **From the chat**
   - By clicking on `Previous Chats` in the top right (`Ctrl/⌘ + Alt/Option + L`)

2. **From your file explorer**
   - Conversations are saved in Cursor application data. But good luck finding and especially using them!

We recommend **local** saving options instead:

1. **Automatic saving**
   - Use [cursor-chat-export](https://github.com/somogyijanos/cursor-chat-export) to export the complete history to a `.history` file in your project

2. **Selective manual saving**
   - Create a `.history.md` file in your project
   - Copy the most important conversations there as your project progresses

Advantages of local saving:
- **Easy to browse**: quickly find your conversations
- **Always available**: even if you change computers
- **Versioned with your project**: for those using Git for example

### Adding Context: The Key to Effectively Interacting with AI

Like chat, adding context is essential for AI tools. In Cursor, you can easily add:

#### 1. Local Files
- Click on `+ Add context` in the top left
- Or mention a file directly in your message:
  - Option 1: Click on `@ Mention` or `Image`
  - Option 2: Type `@Files` and select a file
  - Option 3: Drag and drop a file

Example prompt:
```
Does this report contain elements about Switzerland? @ai_commission_report_france.md
```

Note: Cursor doesn't yet digest PDFs. To use them, copy their content into a text file (.md for example).

#### 2. Individual Web Pages
Type `@` followed by the URL:
```
What is AI Swiss's next event? @https://www.a-i.swiss
```

Note: Cursor won't explore beyond the mentioned page, so choose well! It's the same on ChatGPT.

#### 3. Websites
1. Type `@Docs`
2. Click on `+ Add new doc`
3. Enter the URL and a simple name (example: `https://www.a-i.swiss` → `AI Swiss`)

```
What is AI Swiss's next event? @AI Swiss
```

Notes:
- @Docs context remains active for the entire conversation until manually removed.
- It's often better to use `@Web` (described below) to allow AI to search pages on the internet on its own.

#### 4. Live Web Searches
Add `@Web` to your prompt to allow AI to do its own research (to get up-to-date information, verify facts, etc.):
```
What are the 10 most recent articles about AI on https://www.nature.com? Collect the articles with title, link, date, and brief summary of their importance. Then give me the list in chronological order. @Web
```

#### 5. An Entire Project
To include your entire project:
- Option 1: Type `@Codebase` in your prompt
- Option 2: Use `Ctrl/⌘ + Enter` to send your prompt (instead of clicking `chat` or pressing `Enter`)

The advantage of `@Codebase` is that it allows you to specify search parameters (files to include, exclude, reasoning step, etc.) directly in the prompt window.

Example:
```
Am I talking about what the "Codebase" mention does on Cursor in my project? @Codebase
```

Tip: Create a `.cursorignore` file at the project root to systematically exclude irrelevant files from `@Codebase` searches.

## Intelligent Editing with Cursor: The Little Extras That Make All the Difference

### Predictive Autocompletion

Cursor offers suggestions as you write:
- Start writing
- Observe suggestions appear in gray
- Accept with `Tab` or continue typing

Test it yourself:
Write "Cursor is a..." and let the magic happen.

### Intelligent Navigation

Cursor predicts where you'll likely make your next changes:
- When an orange-outlined `tab` indicator appears, press `Tab` to jump directly to the predicted location

Very simple example:
Transform this list into a bullet list:
```
Title
Introduction
Method
Discussion
Conclusion
```

1. Add a dash (`-`) to the first element
2. Observe the suggestion to add a dash to other elements
3. Use `Tab` to accept
4. Cursor suggests a jump with Cursor Tab, accept with `Tab`
5. Continue with `Tab` for the following elements

### Local Assisted Editing

For targeted modifications, use `Ctrl/⌘ + K` anywhere in the text. Cursor can:
- Correct spelling and grammar
- Translate
- Rephrase for clarity
- Adapt style according to your needs
- Optimize text structure
- Etc.

Example requests:
```
- "Spelling?"
- "Improve"
- "Add examples"
- "Rephrase for a non-coder"
- Etc.
```

## And Finally: Composer, the Multi-file Editor That Changes Everything

You now master the basics of Cursor. It's time to discover its most powerful feature: Composer, a tool that allows you to create and modify multiple files simultaneously!

To use it:
1. Open Composer with `Ctrl/⌘ + I` (I for "I want this")
2. Describe what you want to create
3. Refine the results according to your needs

### Practical Example

```
Create a starter kit for my AI book club including:
- A 2025 meeting calendar (calendar_2025.md)
- A reading sheet template (reading_sheet_template.md)
- A past readings tracking table (library.csv)
- A discussion facilitation guide (facilitation_guide.md)
- A monthly newsletter template (newsletter_template.md)
- Suggested discussion questions (typical_questions.md)
Search @Web for recent must-read books
```

Composer will generate all these files in a single operation, with the ability to refine each file according to your needs. We'll see later how to use it in a concrete case.

To fully appreciate Composer's power, try to accomplish the same task with other tools like ChatGPT or Claude. You'll see how Cursor stands out!

## Some Tips to Get the Best Out of Cursor

Finally, here are some configurations and tips that will make your experience even more productive:

### Customization with .cursorrules

Create a `.cursorrules` file to customize AI's global behavior according to your needs:

1. Create a `.cursorrules` file **at your project root**
2. Add a customization prompt
3. Test in a new chat

#### Simple Example
```
Always respond by starting with "I'm responding, but only because it's you."
```

For more useful examples, check the [cursorrules_examples](./cursorrules_examples) folder. The `.cursorrules_for_learning` file in particular turns Cursor into a programming and AI instructor that guides you through each interaction.

### "Long Context" Mode

"Long Context" mode allows taking into account more elements from the specified context. To activate it:

#### Activation
1. Go to Cursor settings under the "Beta" tab
2. Activate "Long Context Chat"

#### Usage
1. New chat (`Ctrl/⌘ + L`)
2. Select "Long Context Chat" instead of "Normal Chat" in the top right
3. Choose `claude-3-5-sonnet-200k` (our recommendation as of 2024-11-12)

To learn more: [Official Documentation](https://docs.cursor.com/advanced/models#long-context-only-models)

And that's it! If you've made it this far, you know everything!