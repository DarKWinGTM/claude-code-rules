---
name: release-gate
allowed-tools: Bash, Read
---

Run a governed-docs release gate against one explicit target workspace path.

Usage:
- `/governed-docs:release-gate <explicit-target-workspace-path>`

Rules:
- always require one explicit target workspace path
- never fall back to ambient cwd
- treat release-gate results as evidence-bounded doc-governance verdicts only

Command:
```bash
"${CLAUDE_PLUGIN_ROOT}/bin/governed-docs" release-gate "$@"
```
