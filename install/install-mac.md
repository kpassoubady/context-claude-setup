# macOS Installation

Tested on macOS 13 or later.

## 1. Install Homebrew

Skip this step if `brew --version` works.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the on-screen instructions to add Homebrew to your `PATH`, then reopen the terminal.

## 2. Install Git and Python

```bash
brew install git python@3.12
```

## 3. Install Visual Studio Code

```bash
brew install --cask visual-studio-code
```

Alternatively, download it from <https://code.visualstudio.com/>. To enable the `code` command, open VS Code, press `Cmd+Shift+P`, and run **Shell Command: Install 'code' command in PATH**.

## 4. Install Claude Code CLI

Use the native installer (no Node.js required):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Or with Homebrew:

```bash
brew install --cask claude-code
```

Reopen the terminal, then sign in:

```bash
claude
```

Follow the browser prompts to authenticate.

## 5. Install the Claude Code Extension in VS Code

From the terminal:

```bash
code --install-extension anthropic.claude-code
```

Or in VS Code:

1. Press `Cmd+Shift+X` to open Extensions.
2. Search for **Claude Code** (publisher: Anthropic).
3. Click **Install**.
4. Open the Claude Code panel from the Spark icon in the editor toolbar or the Activity Bar, and sign in if prompted.

## 6. Verify

```bash
git --version
python3 --version
code --version
claude --version
claude doctor
code --list-extensions | grep -i claude
```

Expected results:

- Git 2.30 or later
- Python 3.11 or later
- VS Code prints a version number
- `claude --version` prints a version and `claude doctor` reports no errors
- `anthropic.claude-code` appears in the extension list

Quick Python check:

```bash
python3 -c "import unittest, ast, pathlib; print('Python OK')"
```

Then run the automated check from the root of this repository. It should end with `ALL SETUP CHECKS PASSED`:

```bash
python3 quickstart-project/test_setup.py
```
