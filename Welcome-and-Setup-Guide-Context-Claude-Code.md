# Welcome to Context Engineering for Claude Code

Thank you for registering for **Context Engineering for Claude Code**, a 4-hour instructor-led course. This message lists what to complete before class so we can start hands-on work right away.

## Course Overview

You will learn how context engineering extends prompt design across instructions, files, tools, and memory in Claude Code. The session covers runtime context loading and retrieval, compaction and handoffs for long tasks, subagents, and evaluating context quality. It includes demonstrations, a quiz, and two breakout labs. Read the full [course outline](https://github.com/kpassoubady/context-claude-setup/blob/main/catalog/context-engineering-for-claude-code-4-hour-am-pm-outline.md).

## Pre-Class Setup

Allow 20 to 30 minutes. Follow the guide for your operating system:

| Operating system | Guide |
| :--- | :--- |
| macOS | [install-mac.md](https://github.com/kpassoubady/context-claude-setup/blob/main/install/install-mac.md) |
| Windows | [install-win.md](https://github.com/kpassoubady/context-claude-setup/blob/main/install/install-win.md) |

The [overview guide](https://github.com/kpassoubady/context-claude-setup/blob/main/install/install.md) lists every tool:

| Tool | Version |
| :--- | :--- |
| Git | 2.30 or later |
| Python | 3.11 or later |
| Visual Studio Code | Latest |
| Claude Code CLI | Latest |
| Claude Code extension for VS Code | Latest |

You also need a Claude account with Claude Code access (a Pro or Max subscription, or an Anthropic Console account with API credits). Sign in before class by running `claude` once in a terminal.

## Verify Your Setup

Run the [verification script](https://github.com/kpassoubady/context-claude-setup/blob/main/quickstart-project/README.md) from the root of this repository:

```bash
python3 quickstart-project/test_setup.py
```

On Windows, run `python quickstart-project\test_setup.py`. A successful run ends with `ALL SETUP CHECKS PASSED`.

## Checklist

- [ ] Git 2.30 or later is installed
- [ ] Python 3.11 or later is installed
- [ ] Visual Studio Code is installed and the `code` command works
- [ ] Claude Code CLI is installed and `claude --version` works
- [ ] The Claude Code extension is installed in VS Code
- [ ] You are signed in to Claude Code
- [ ] The verification script prints `ALL SETUP CHECKS PASSED`

## Quick Links

- [Course outline](https://github.com/kpassoubady/context-claude-setup/blob/main/catalog/context-engineering-for-claude-code-4-hour-am-pm-outline.md)
- [Installation overview](https://github.com/kpassoubady/context-claude-setup/blob/main/install/install.md)
- [macOS guide](https://github.com/kpassoubady/context-claude-setup/blob/main/install/install-mac.md)
- [Windows guide](https://github.com/kpassoubady/context-claude-setup/blob/main/install/install-win.md)
- [Verification script](https://github.com/kpassoubady/context-claude-setup/blob/main/quickstart-project/README.md)

## Need Help?

Run `claude doctor` and the verification script, then send the output to your instructor before class. Lab materials are shared during the session, so there is nothing else to download in advance.

We look forward to seeing you in class.
