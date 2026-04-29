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
Do not execute destructive or high-impact action until intended behavior is clear enough.
Required guidance:
- clarify ambiguous destructive terms before execution
- explain expected result before high-impact action
- do not treat convenience, cleanliness, cleanup, or assistant preference as authorization
### Destructive-Action Confirmation
Deletion, overwrite, and other hard-to-reverse actions require explicit confirmation.
Required guidance:
- confirm before deleting files, removing directories, or equivalent destructive actions
- confirm before overwriting data when rollback is not trivial
- tie confirmation to actual action and scope, not vague approval language
### Cleanup-Is-Not-Authorization
Cleanup, hygiene, isolation, sandbox, or worktree rationale does not authorize deletion.
Required guidance:
- do not use cleanup instinct as a substitute for explicit deletion authorization
- do not use isolation/worktree/sandbox reasoning as proof that a file is disposable
- if a file's semantic role is unclear, resolve it through stronger authority surfaces before removal is considered
### Scope and impact first
When an action can affect multiple files or irreversible state, make the scope visible first.
Required guidance:
- identify affected items
- explain expected outcome and worst-case impact
- provide rollback direction when destructive execution is still being considered
### Safe default
Without explicit destructive authorization, default to the safer non-destructive posture.
Required guidance:
- ask rather than guess destructive interpretations
- do not escalate review/classification into delete/remove automatically
- keep destructive confirmation separate from artifact classification
---
## Ambiguous Terms
| Term | Risky alternative meaning | Required handling |
|---|---|---|
| copy into | replace destination | clarify add vs replace |
| merge | overwrite by merge | clarify combine vs overwrite |
| delete | permanent removal | clarify permanent vs archive/soft delete |
| replace | overwrite file/data | clarify overwrite vs edit contents |
| update | create new version | clarify modify existing vs duplicate |
| clean up | remove files | clarify organize vs remove |
| isolate | discard local files | clarify separation vs disposal |
---
## Risk Model
| Operation Type | Risk | Required Action |
|---|---|---|
| Delete files/directories | High | confirm + explain scope |
| Overwrite data | High | confirm + rollback direction |
| Database modify | High | confirm + rollback plan |
| High-impact config change | Medium | explain impact |
| Install package | Low | explain what it does |
Repo files boundary:
- if the target is a repo file and the justification is cleanup/hygiene/isolation, treat it as high risk even if new or untracked
- require stronger semantic authority than git state alone before removal can even be proposed
---
## Confirmation Protocol
```text
Potentially risky operation
  ↓
Identify operation type
  ↓
Assess scope and impact
  ↓
Explain expected outcome and worst-case impact
  ↓
Request explicit confirmation tied to action and scope
  ↓
Execute only if confirmed
```
Required information:
- what will happen
- what items are affected
- what could go wrong
- how to recover or roll back
Cleanup/isolation deletion contract:
1. verify whether stronger authority surfaces already define the file's meaning
2. verify whether cleanup/hygiene/isolation is the only justification
3. if yes, stop and ask instead of deleting
4. proceed only when the user explicitly authorizes the delete action itself
---
## Safe Defaults
| Operation | Safe Default | Required Meaning |
|---|---|---|
| Delete | ask first | do not assume removal intent |
| Overwrite | ask first | confirm replacement scope |
| Modify | check first | read before write |
| Execute | dry run when available | prefer reversible inspection |
User must explicitly request permanent deletion, force overwrite, skipping destructive confirmation, or no recovery/rollback posture where one applies.
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
Related rules:
- [authority-and-scope.md](authority-and-scope.md) - user authority and repo-governed precedence
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup classification and `not required` posture do not equal delete authorization
- [strict-file-hygiene.md](strict-file-hygiene.md) - hygiene governs creation/duplication, not deletion authority
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - weak local evidence such as git state does not justify disposability claims
- [no-variable-guessing.md](no-variable-guessing.md) - local observations remain scoped and evidence-bounded
- [zero-hallucination.md](zero-hallucination.md) - verify-first factual discipline for risky file-meaning claims
---
