---
name: present-md
allowed-tools: Bash, Read
---

Render one governed-docs-owned Markdown source into an article-style HTML preview.

Usage:
- `/governed-docs:present-md <explicit-target-workspace-path> <markdown-source-relative-path>`

Rules:
- always require one explicit target workspace path
- always require one explicit Markdown source path inside that target
- never fall back to ambient cwd
- never reuse NodeClaw ownership surfaces as implementation authority

Command:
```bash
"${CLAUDE_PLUGIN_ROOT}/bin/governed-docs" present-md "$@"
```
