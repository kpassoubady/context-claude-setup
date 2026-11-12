# Context Engineering for Claude Code — Setup

Standalone pre-class setup repository for **Context Engineering for Claude Code** (4-hour course). It holds the course outline, installation guides, a read-only verification script, and the student welcome message.

## Tech Stack

- **Primary Tool:** Anthropic Claude Code CLI
- **Prerequisites:** Git 2.30+, Python 3.11+ (standard library only), VS Code, Claude Code extension (`anthropic.claude-code`)
- **Supported OS:** macOS and Windows

## Project Structure

| Path | Purpose |
| :--- | :--- |
| `Welcome-and-Setup-Guide-Context-Claude-Code.md` | Student welcome and setup guide; absolute GitHub links only (`blob/main`) |
| `README.md` | Entry point with relative links |
| `catalog/` | Copy of the detailed course outline; do not edit here |
| `install/` | `install.md`, `install-mac.md`, `install-win.md` |
| `quickstart-project/` | `test_setup.py` read-only environment check and its README |
| `scripts/` | Template build tooling; not used for student setup |
| `llm-context/` | Context and reference material for LLM agents |

## Key Commands

```bash
python3 quickstart-project/test_setup.py   # macOS; prints "ALL SETUP CHECKS PASSED" on success, exits 1 on failure
python quickstart-project\test_setup.py    # Windows
```

## Conventions

- Keep the repository independently usable before students receive other course materials.
- Link only to files inside this repository. Do not name or link to any other course repository.
- Keep install guides, `test_setup.py`, and `Welcome-and-Setup-Guide-Context-Claude-Code.md` consistent on tools and versions.
- Markdown follows `.markdownlint.json`.
