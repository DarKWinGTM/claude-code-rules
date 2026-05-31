---
name: scan
allowed-tools: Bash, Read
---

Run a governed-docs scan against one explicit target workspace path.

Usage:
- `/governed-docs:scan <explicit-target-workspace-path>`

Rules:
- always require one explicit target workspace path
- never fall back to ambient cwd
- fail closed when the path is missing or invalid

Command:
```bash
"${CLAUDE_PLUGIN_ROOT}/bin/governed-docs" scan "$@"
```
