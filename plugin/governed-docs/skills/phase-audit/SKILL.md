---
name: phase-audit
allowed-tools: Bash, Read
---

Run a governed-docs phase audit against one explicit target workspace path.

Usage:
- `/governed-docs:phase-audit <explicit-target-workspace-path>`

Rules:
- always require one explicit target workspace path
- never fall back to ambient cwd
- keep output focused on phase grammar and lineage signals

Command:
```bash
"${CLAUDE_PLUGIN_ROOT}/bin/governed-docs" phase-audit "$@"
```
