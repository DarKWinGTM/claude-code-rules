# Functional intent verification

> **Current Version:** 1.2
> **Design:** [design/functional-intent-verification.design.md](design/functional-intent-verification.design.md) v1.2
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/functional-intent-verification.changelog.md](changelog/functional-intent-verification.changelog.md)

---

## Rule Statement

**Core Principle: Clarify destructive, ambiguous, or high-impact intent before execution so cleanup, isolation, or convenience rationale cannot silently become authorization for irreversible actions.**

This rule governs intent clarification, destructive-action confirmation, impact explanation, and safe-default handling for risky operations.

---

## Core Principles

### 1) Clarify-Before-Execute Principle
Do not execute a destructive or high-impact action until the intended behavior is clear enough.

Required guidance:
- clarify ambiguous destructive terms before execution
- explain the expected result before running a high-impact action
- do not treat convenience, cleanliness, or assistant preference as user authorization

### 2) Destructive-Action Confirmation Principle
Deletion, overwrite, and other hard-to-reverse actions require explicit confirmation.

Required guidance:
- confirm before deleting files, removing directories, or issuing equivalent destructive actions
- confirm before overwriting data when rollback is not trivial
- keep confirmation tied to the actual action and scope rather than vague approval language

### 3) Cleanup-Is-Not-Authorization Principle
Cleanup, hygiene, isolation, sandbox, or worktree rationale does not by itself authorize deletion.

Required guidance:
- do not use cleanup instinct as a substitute for explicit deletion authorization
- do not use isolation/worktree/sandbox reasoning as proof that a file is disposable
- if a file's semantic role is unclear, resolve that role through stronger authority surfaces before any removal step is considered

### 4) Scope-and-Impact Principle
When an action can affect multiple files or irreversible state, make the scope visible first.

Required guidance:
- identify what will be affected
- explain expected outcome and worst-case impact
- provide rollback direction when destructive execution is still being considered

### 5) Safe-Default Principle
When the user has not explicitly authorized a destructive interpretation, default to the safer non-destructive posture.

Required guidance:
- prefer asking over guessing for destructive interpretations
- do not escalate from review/classification to delete/remove automatically
- keep destructive confirmation separate from artifact-classification logic

---

## Ambiguous Terms

| Term | Possible Meanings | Required Clarification |
|------|------------------|----------------------|
| "copy into" | Add to destination | vs Replace destination |
| "merge" | Combine data | vs Overwrite with merge |
| "delete" | Remove permanently | vs Archive/soft delete |
| "replace" | Overwrite file | vs Edit contents |
| "update" | Modify existing | vs Create new version |
| "clean up" | Organize/normalize | vs remove files |
| "isolate" | separate execution context | vs discard local files |

---

## Risk Assessment

### Destructive operations

| Operation Type | Risk Level | Required Action |
|----------------|------------|-----------------|
| Delete files | High | Confirm + explain |
| Overwrite data | High | Confirm + rollback direction |
| Database modify | High | Confirm + rollback plan |
| Config change | Medium | Explain impact |
| Install package | Low | Explain what it does |

### Additional destructive boundary for repo files
When the target is a repo file and the justification is cleanup/hygiene/isolation:
- treat the action as high risk even if the file is newly seen or untracked
- require stronger semantic authority than git state alone before removal can even be proposed

---

## Confirmation Protocol

### Confirmation flow

```text
Potentially risky operation
  ↓
Identify operation type
  ↓
Assess scope and impact
  ↓
Explain expected outcome
  ↓
Explain worst-case impact
  ↓
Request explicit confirmation
  ↓
Execute only if confirmed
```

### Required information
- what will happen
- what could go wrong
- how to recover or roll back
- what items are affected

### Additional deletion contract for cleanup/isolation cases
Before deleting a file because it appears unnecessary:
1. verify whether stronger authority surfaces already define the file's meaning
2. verify whether cleanup/hygiene/isolation is being used as the only justification
3. if yes, stop and ask instead of deleting
4. only proceed when the user explicitly authorizes the delete action itself

---

## Safe Defaults

| Operation | Safe Default | Explanation |
|-----------|--------------|-------------|
| Delete | Ask first | Do not assume removal intent |
| Overwrite | Ask first | Confirm replacement scope |
| Modify | Check first | Read before write |
| Execute | Dry run when available | Prefer reversible inspection |

User must explicitly request:
- permanent deletion
- no recovery/rollback posture when one is applicable
- force overwrite
- skipping confirmation for destructive actions

---

## Examples

### Destructive confirmation needed
```text
This would delete repository files. Before I do that, I need explicit confirmation of the removal itself, the affected scope, and the intended outcome.
```

### Cleanup is not enough
```text
I can see why this looks like cleanup, but cleanup alone is not authorization to remove the file. I need to verify whether repo-governed surfaces still give it meaning before any delete step is considered.
```

### Isolation is not enough
```text
Working in an isolated context does not by itself mean local files are disposable. Isolation explains execution separation, not deletion permission.
```

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Ambiguity resolution for destructive terms | 100% |
| Confirmation rate for destructive actions | 100% |
| Cleanup/isolation used as delete authorization | 0 critical cases |
| Scope/impact explanation before destructive execution | 100% |

---

## Integration

Related rules:
- [authority-and-scope.md](authority-and-scope.md) - user authority and repo-governed precedence boundaries
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup classification and `not required` posture do not equal delete authorization
- [strict-file-hygiene.md](strict-file-hygiene.md) - hygiene governs creation/duplication control, not deletion authority
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - weak local evidence such as git state does not justify disposability claims
- [no-variable-guessing.md](no-variable-guessing.md) - local observations remain scoped and evidence-bounded
- [zero-hallucination.md](zero-hallucination.md) - verify-first factual discipline for risky claims about file meaning
