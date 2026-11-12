# Windows Installation

Tested on Windows 10 (22H2) and Windows 11. Run commands in PowerShell.

## 1. Install Git for Windows

```powershell
winget install --id Git.Git -e
```

Git for Windows includes Git Bash, which Claude Code uses on native Windows. Close and reopen PowerShell afterward.

## 2. Install Python

```powershell
winget install --id Python.Python.3.12 -e
```

If `python` opens the Microsoft Store, disable the aliases under **Settings > Apps > Advanced app settings > App execution aliases**, or use the `py` launcher.

## 3. Install Visual Studio Code

```powershell
winget install --id Microsoft.VisualStudioCode -e
```

Or download it from <https://code.visualstudio.com/> and keep **Add to PATH** checked in the installer.

## 4. Install Claude Code CLI

Use the native installer (no Node.js required):

```powershell
irm https://claude.ai/install.ps1 | iex
```

Or with WinGet:

```powershell
winget install Anthropic.ClaudeCode
```

Reopen PowerShell, then sign in:

```powershell
claude
```

Follow the browser prompts to authenticate.

## 5. Install the Claude Code Extension in VS Code

From PowerShell:

```powershell
code --install-extension anthropic.claude-code
```

Or in VS Code:

1. Press `Ctrl+Shift+X` to open Extensions.
2. Search for **Claude Code** (publisher: Anthropic).
3. Click **Install**.
4. Open the Claude Code panel from the Spark icon in the editor toolbar or the Activity Bar, and sign in if prompted.

## 6. Verify

```powershell
git --version
python --version
code --version
claude --version
claude doctor
code --list-extensions | Select-String claude
```

Expected results:

- Git 2.30 or later
- Python 3.11 or later
- VS Code prints a version number
- `claude --version` prints a version and `claude doctor` reports no errors
- `anthropic.claude-code` appears in the extension list

Quick Python check:

```powershell
python -c "import unittest, ast, pathlib; print('Python OK')"
```

Then run the automated check from the root of this repository. It should end with `ALL SETUP CHECKS PASSED`:

```powershell
python quickstart-project\test_setup.py
```

## Optional: WSL

Claude Code also runs inside WSL 2 if you prefer a Linux environment. Install it with `wsl --install`, then follow the Linux install steps inside the distribution. The VS Code extension can connect through the WSL extension.
