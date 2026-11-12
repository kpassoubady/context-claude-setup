# Context Engineering for Claude Code — Setup

Standalone pre-class setup repository for **Context Engineering for Claude Code**. It contains everything you need to prepare your machine before the session: the course outline, installation guides for macOS and Windows, and a script that verifies your environment.

## Start Here

Read [Welcome.md](Welcome.md) first.

## Course Outline

[Course outline](catalog/context-engineering-for-claude-code-4-hour-am-pm-outline.md): the 4-hour session schedule, learning outcomes, and prerequisites.

## Installation Guides

- [Overview and tool list](install/install.md)
- [macOS](install/install-mac.md)
- [Windows](install/install-win.md)

## Verify Your Setup

Run the checks from the root of this repository (see [quickstart-project/README.md](quickstart-project/README.md)):

```bash
python3 quickstart-project/test_setup.py
```

On Windows, use `python quickstart-project\test_setup.py`. Success looks like:

```text
ALL SETUP CHECKS PASSED. You are ready for class.
```

Your Claude sign-in is not tested by the script. Run `claude` once and confirm it opens without asking you to log in.

## Troubleshooting

- **Command not found after install:** close and reopen your terminal.
- **Anything else:** run `claude doctor` and share the output with your instructor.
