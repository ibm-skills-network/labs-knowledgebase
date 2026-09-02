---
sidebar_position: 20
---

# Vibe Coding Studio

Vibe Coding Studio is a development environment designed for “vibe coding,” where developers and AI collaborate fluidly in real time. It enables rapid prototyping, live execution, and iterative refinement of web applications, all within a browser-based workspace that supports multiple LLM backends.

### General Layout

#### Left Side
This area is divided into two sections:
 - Tai's Chat Interface: This interface facilitates communication between the learner and Tai, featuring chat history, and learners' message input field.
 - Lab instructions: These instructions guide learners through the learning activities and exercises.

#### Right Side: Vibe Coding Studio

The Vibe Coding Studio environment resides here, providing the tools for code development and execution.

### Vibe Coding Studio UI

The homepage of Vibe Coding Studio is a chat interface where you can select a provider (e.g. OpenAI, Anthropic) and a model. You can describe what you want to build in Vibe Coding Studio and the LLM agent will attempt to build it with you. After the agent actually starts writing code, an IDE will appear on the right. On the bottom of the IDE is a terminal where you can see commands the agent is running, as well as run your own commands. Above the terminal is a text editor with 3 tabs: Code, Diff, and Preview. Code is a code browser where you can see all your files, and make changes to them. Diff will show you a diff of the changes. Preview will allow you to access a web server that you're running in the terminal (allows you to view your application / website).

Users may view previous chat histories by hovering on the top left corner of the screen to view the history panel and selecting a previous conversation.

### Vibe Coding Studio Environment

#### Capabilities
Vibe Coding Studio operates in WebContainer, an in-browser Node.js runtime that emulates a Linux system:
- Runs in browser, not full Linux system or cloud VM
- Shell emulating zsh
- Cannot run native binaries (only JS, WebAssembly)
- Python limited to standard library (no pip, no third-party libraries)
- No C/C++/Rust compiler available
- Git not available
- Available commands: cat, chmod, cp, echo, hostname, kill, ln, ls, mkdir, mv, ps, pwd, rm, rmdir, xxd, alias, cd, clear, curl, env, false, getconf, head, sort, tail, touch, true, uptime, which, code, jq, loadenv, node, python, python3, wasm, xdg-open, command, exit, export, source


#### Vibe Coding Studio Standards 

Preferred Frameworks / Tools / Libraries:
- Vite is the preferred framework for Vibe Coding Studio.
- React Navigation for navigation
- Built -in React Native styling
- Zustand / Jotai for state management
- React Query / SWR for data fetching

Vibe Coding Studio will try to stick to these requirements:
- Feature - rich screens(no blank screens)
- Include index.tsx as main tab
- Domain - relevant content(5 - 10 items minimum)
- All UI states(loading, empty, error, success)
- All interactions and navigation states
- Use Pexels for photos

Vibe Coding Studio will try to use this directory structure:
- app /
  - (tabs) /
    - index.tsx
    - _layout.tsx
  - _layout.tsx
  - components /
  - hooks /
  - constants /
  - app.json

Things to know about Vibe Coding Studio:


#### Troubleshooting:
- This tool is in alpha and you may encounter bugs or features that aren't working properly. If you're trying to use a feature not explicitly referenced in the lab instructions, it may not work.
- OpenAI gpt-5 models in particular may respond slowly, please be patient
- If Vibe Coding Studio stops responding, please try refreshing the page
- Vibe Coding Studio may occasionally "forget" to create files during execution and instead respond in chat with the code. You can try asking "please actually create the files" to prompt it to actually create the files.
