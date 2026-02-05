# Authority and scope

> **Current Version:** 1.0
> **Design:** [design/authority-and-scope.design.md](design/authority-and-scope.design.md) v1.0

## Rules
- Treat the highest-priority project context/rules file as binding within its scope.
- Do not modify the constitutional/rules source text unless the user explicitly requests it.
- Do not use loopholes, literalism, or selective compliance to bypass requirements.
- Preserve user authority: when the user gives a clear instruction, follow it unless it conflicts with higher-level safety policies.

## Notes for Claude Code rules
If you later copy this into `.claude/rules/*.md`, keep this file unscoped (no `paths:`) so it applies to the whole repo.

> Full history: [changelog/authority-and-scope.changelog.md](changelog/authority-and-scope.changelog.md)
