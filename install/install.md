# Installation Guide

Complete these steps before class. Setup takes about 20 to 30 minutes.

## What You Will Install

| Tool | Version | Purpose |
| :--- | :--- | :--- |
| Git | 2.30+ | Version control for lab repositories |
| Python | 3.11+ | Runs lab verification scripts (`verify_lab.py`) and unit tests |
| Visual Studio Code | Latest | Editor for labs |
| Claude Code CLI | Latest | The tool this course teaches |
| Claude Code extension for VS Code | Latest | Claude Code inside the editor |

Lab scripts use only the Python standard library, so no `pip install` is needed. `pytest` is optional.

You also need a Claude account with Claude Code access (a Pro or Max subscription, or an Anthropic Console account with API credits).

## OS-Specific Guides

- [macOS](install-mac.md)
- [Windows](install-win.md)

## After Installing

1. Sign in to Claude Code by running `claude` in a terminal and following the prompts.
2. Open VS Code, open the Claude Code panel, and confirm it is signed in.
3. Run the verification script from the root of this repository. All checks should pass before class:

   ```bash
   python3 quickstart-project/test_setup.py
   ```

   On Windows, use `python quickstart-project\test_setup.py`. See [quickstart-project/README.md](../quickstart-project/README.md).

Lab materials are shared in class. You do not need to clone anything else before the session.

## Troubleshooting

- **Command not found after install:** Close and reopen your terminal so the updated `PATH` loads.
- **Login fails:** Run `claude` again and choose the login method that matches your account. Behind a corporate proxy, set `HTTPS_PROXY` first.
- **Anything else:** Run `claude doctor` and share the output with your instructor.
