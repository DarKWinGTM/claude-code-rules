# Functional intent verification
> **Current Version:** 1.2
> **Design:** [design/functional-intent-verification.design.md](design/functional-intent-verification.design.md) v1.2
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/functional-intent-verification.changelog.md](changelog/functional-intent-verification.changelog.md)
---
## Rule Statement
**Core Principle: Clarify destructive, ambiguous, or high-impact intent before execution so cleanup, isolation, or convenience rationale cannot silently become authorization for irreversible actions.**
This rule owns intent clarification, Destructive-Action Confirmation, impact explanation, and safe defaults for risky operations.
---
## Core Contract
### Clarify before execute
Do not execute destructive or high-impact action until intended behavior is clear enough. Clarify ambiguous destructive terms, explain expected result before high-impact action, and do not treat convenience, cleanliness, cleanup, or assistant preference as authorization.

### Destructive-Action Confirmation
Deletion, overwrite, and other hard-to-reverse actions require explicit confirmation tied to the actual action and scope, not vague approval language. Confirm before deleting files/directories/equivalents or overwriting data when rollback is not trivial.

### Cleanup-Is-Not-Authorization
Cleanup, hygiene, isolation, sandbox, or worktree rationale does not authorize deletion or prove a file is disposable. If a file’s semantic role is unclear, resolve it through stronger authority surfaces before removal is considered.

### Scope and impact first
When an action can affect multiple files or irreversible state, identify affected items, explain expected outcome and worst-case impact, and provide rollback direction when destructive execution is still being considered.

### Safe default
Without explicit destructive authorization, choose the safer non-destructive posture: ask rather than guess destructive interpretations, do not escalate review/classification into delete/remove automatically, and keep destructive confirmation separate from artifact classification.
---
## Ambiguous Terms and Risk Model
Ambiguous destructive terms require clarification: `copy into` may mean add or replace; `merge` may overwrite; `delete` may mean permanent removal or archive; `replace` may overwrite; `update` may mean edit existing or create a duplicate/version; `clean up` may remove files; `isolate` may discard local files.

Operation requirements:
- Delete files/directories: high risk; confirm and explain scope.
- Overwrite data: high risk; confirm and give rollback direction.
- Database modify: high risk; confirm and provide rollback plan.
- High-impact config change: medium risk; explain impact.
- Install package: low risk; explain what it does.

Repo files boundary: if the target is a repo file and the justification is cleanup/hygiene/isolation, treat it as high risk even if new or untracked; stronger semantic authority than git state is required before removal can even be proposed.
---
## Confirmation Protocol
```text
Potentially risky operation
  ↓
Identify operation type, scope, impact, and rollback path
  ↓
Explain what will happen, affected items, worst-case result, and recovery
  ↓
Request explicit confirmation tied to action and scope
  ↓
Execute only if confirmed
```
Cleanup/isolation deletion contract:
1. verify whether stronger authority surfaces already define the file’s meaning
2. verify whether cleanup/hygiene/isolation is the only justification
3. if yes, stop and ask instead of deleting
4. proceed only when the user explicitly authorizes the delete action itself

User must explicitly request permanent deletion, force overwrite, skipping destructive confirmation, or no recovery/rollback posture where one applies. Prefer dry-run/reversible inspection when available.
---
## Examples
Destructive confirmation needed:
```text
This would delete repository files. Before I do that, I need explicit confirmation of the removal itself, the affected scope, and the intended outcome.
```
Cleanup/isolation is not enough:
```text
Cleanup or isolation explains why the file looks suspicious, but it is not deletion authority. I need to verify governed meaning before any delete step is considered.
```
---
## Quality Metrics
| Metric | Target |
|---|---|
| Ambiguity resolution for destructive terms | 100% |
| Confirmation rate for destructive actions | 100% |
| Cleanup/isolation used as delete authorization | 0 critical cases |
| Scope/impact explanation before destructive execution | 100% |
---
## Integration
Related rules: `authority-and-scope.md` owns user authority and repo-governed precedence; `artifact-initiation-control.md` keeps `not required` from meaning deletion authorization; `strict-file-hygiene.md` owns creation/duplication hygiene only; evidence/no-guessing/zero-hallucination chains keep risky file-meaning claims verified and scoped.
---
