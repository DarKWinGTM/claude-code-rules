---
name: present-sync
allowed-tools: Bash, Read
---

Rebuild and resync the governed-docs preview portal under root `preview/` for the named target workspace.

Usage:
- `/governed-docs:present-sync <explicit-target-workspace-path>`

Rules:
- always require one explicit target workspace path
- never fall back to ambient cwd
- mutate only `preview/**`
- never rewrite governed source docs
- treat preview output as a presentation/support surface, not semantic authority

Command:
```bash
"${CLAUDE_PLUGIN_ROOT}/bin/governed-docs" present-sync "$@"
```
