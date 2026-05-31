---
name: review
allowed-tools: Bash, Read
---

Run a governed-docs review against one explicit target workspace path.

Usage:
- `/governed-docs:review <explicit-target-workspace-path>`

Rules:
- always require one explicit target workspace path
- never fall back to ambient cwd
- keep the review read-only

Command:
```bash
"${CLAUDE_PLUGIN_ROOT}/bin/governed-docs" review "$@"
```
