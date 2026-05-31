---
name: repair-plan
allowed-tools: Bash, Read
---

Generate a governed-docs repair plan from one explicit target workspace path.

Usage:
- `/governed-docs:repair-plan <explicit-target-workspace-path>`

Rules:
- always require one explicit target workspace path
- never fall back to ambient cwd
- output must remain reviewable and non-mutating

Command:
```bash
"${CLAUDE_PLUGIN_ROOT}/bin/governed-docs" repair-plan "$@"
```
