# Setup Verification

A read-only script that confirms your tools are installed before class. It does not change your system or contact any network service.

## What It Checks

- Python 3.11 or later and the standard library modules used by the labs
- Git 2.30 or later
- VS Code (the `code` command)
- Claude Code CLI (the `claude` command)
- The Claude Code extension (`anthropic.claude-code`) in VS Code

## Run It

From the root of this repository:

macOS:

```bash
python3 quickstart-project/test_setup.py
```

Windows (PowerShell):

```powershell
python quickstart-project\test_setup.py
```

## Expected Output

```text
[PASS] Python 3.11+: Python 3.12.4
...
ALL SETUP CHECKS PASSED. You are ready for class.
```

A failed check prints a hint. Fix it using the guide in `install/`, reopen your terminal, and run the script again.

## Not Checked

Your Claude sign-in is not tested by the script. Run `claude` once in a terminal and confirm it opens without asking you to log in.
