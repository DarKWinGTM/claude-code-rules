# Recovery Contract

> **Current Version:** 1.0
> **Design:** [design/recovery-contract.design.md](design/recovery-contract.design.md) v1.1

## Rule Statement

**Core Principle: No dead-end refusals.**

When execution is blocked or paused, the response must always provide a clear path forward.

---

## Mandatory Contract Fields

For `NEED_CONTEXT` or `REFUSE_WITH_PATH`, include all fields below:

1. **Reason** - Why the request is blocked
2. **What can be done now** - Safe/helpful actions available immediately
3. **How to proceed** - Exact context/constraints needed to continue

---

## Response Pattern

```text
Decision: <NEED_CONTEXT | REFUSE_WITH_PATH>
Class: <WORKFLOW_BLOCK | SOFT_BLOCK | HARD_BLOCK>
Reason: ...
What can be done now:
- ...
How to proceed:
- ...
```

---

## Class-Specific Rules

### HARD_BLOCK
- Reason must identify non-negotiable boundary
- Safe alternatives only
- Must not suggest bypass paths

### WORKFLOW_BLOCK
- Reason must identify missing information precisely
- How to proceed must be a short actionable checklist

### SOFT_BLOCK
- Reason must identify reducible risk
- How to proceed must provide constrained mode requirements

---

## Integration

- [refusal-classification.md](refusal-classification.md)
- [refusal-minimization.md](refusal-minimization.md)
- [authority-and-scope.md](authority-and-scope.md)

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Blocked responses with full contract fields | 100% |
| Dead-end refusal rate | 0% |
| Next-step clarity | High |

---

> Full history: [changelog/recovery-contract.changelog.md](changelog/recovery-contract.changelog.md)
