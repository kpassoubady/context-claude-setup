"""Read-only environment check for Context Engineering for Claude Code."""

import importlib
import re
import shutil
import subprocess
import sys

MIN_PYTHON = (3, 11)
MIN_GIT = (2, 30)
EXTENSION_ID = "anthropic.claude-code"
STDLIB_MODULES = ["unittest", "ast", "pathlib", "fnmatch"]


def run(cmd):
    exe = shutil.which(cmd[0])
    if not exe:
        return None
    try:
        proc = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return proc.stdout.strip() if proc.returncode == 0 else None


def parse_version(text):
    match = re.search(r"(\d+)\.(\d+)(?:\.(\d+))?", text or "")
    return tuple(int(p) for p in match.groups(default="0")) if match else None


def fmt(v):
    return ".".join(map(str, v))


def check_python():
    v = sys.version_info[:3]
    return v >= MIN_PYTHON, f"Python {fmt(v)}", f"need {fmt(MIN_PYTHON)}+"


def check_git():
    out = run(["git", "--version"])
    v = parse_version(out)
    if not v:
        return False, "not found", "install Git (see install guide)"
    return v >= MIN_GIT, out, f"need {fmt(MIN_GIT)}+"


def check_stdlib():
    missing = []
    for name in STDLIB_MODULES:
        try:
            importlib.import_module(name)
        except ImportError:
            missing.append(name)
    return not missing, "unittest, ast, pathlib, fnmatch", f"missing: {', '.join(missing)}"


def check_vscode():
    out = run(["code", "--version"])
    if not out:
        return False, "not found", "install VS Code and add `code` to PATH"
    return True, f"VS Code {out.splitlines()[0]}", ""


def check_claude():
    out = run(["claude", "--version"])
    if not out:
        return False, "not found", "install Claude Code CLI, then reopen your terminal"
    return True, out.splitlines()[0], ""


def check_extension():
    out = run(["code", "--list-extensions"])
    if out is None:
        return False, "could not list extensions", "requires the `code` command"
    found = EXTENSION_ID in out.lower().splitlines()
    return found, EXTENSION_ID if found else "not installed", f"run: code --install-extension {EXTENSION_ID}"


CHECKS = [
    ("Python 3.11+", check_python),
    ("Python standard library", check_stdlib),
    ("Git", check_git),
    ("VS Code", check_vscode),
    ("Claude Code CLI", check_claude),
    ("Claude Code VS Code extension", check_extension),
]


def main():
    print("Context Engineering for Claude Code - setup check\n")
    failed = 0
    for label, fn in CHECKS:
        ok, detail, hint = fn()
        failed += not ok
        print(f"[{'PASS' if ok else 'FAIL'}] {label}: {detail}" + ("" if ok else f"  ({hint})"))
    print()
    if failed:
        print(f"{failed} check(s) failed. Fix the items above using the install guide, then rerun.")
        return 1
    print("ALL SETUP CHECKS PASSED. You are ready for class.")
    print("Reminder: run `claude` once to confirm you are signed in.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
