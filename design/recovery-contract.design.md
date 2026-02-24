# Recovery Contract Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.4
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-22)

---

## 1. Goal

Ensure every blocked or constrained outcome has a deterministic recovery path and never leaves the user with a dead-end refusal.

---

## 2. Contract Schema (Mandatory)

For `NEED_CONTEXT`, `ALLOW_CONSTRAINED`, or `REFUSE_WITH_PATH`, responses must include all fields:

1. **Reason** - Why execution is blocked or constrained.
2. **What can be done now** - Safe immediate actions available.
3. **How to proceed** - Exact required context or constraints to continue.

---

## 3. Response Pattern

```text
decision_output: <ALLOW_CONSTRAINED | NEED_CONTEXT | REFUSE_WITH_PATH>
refusal_class: <SOFT_BLOCK | WORKFLOW_BLOCK | HARD_BLOCK>
reason: ...
what_can_be_done_now:
- ...
how_to_proceed:
- ...
```

---

## 4. Class-Specific Requirements

### 4.1 HARD_BLOCK
- Reason explicitly identifies non-negotiable boundary type.
- Immediate actions are safe alternatives only.
- Proceed guidance must not suggest bypass routes.

### 4.2 WORKFLOW_BLOCK
- Reason identifies missing information precisely.
- Proceed guidance is a short actionable checklist.

### 4.3 SOFT_BLOCK
- Reason identifies reducible risk.
- Proceed guidance defines constrained-mode requirements.

---

## 5. Quality Metrics

| Metric | Target |
|--------|--------|
| Blocked/constrained responses with full contract | 100% |
| Dead-end refusal rate | 0% |
| Next-step clarity | High |

---

## 6. Integration

Related design docs / active rules:
- [refusal-classification.design.md](refusal-classification.design.md)
- [refusal-minimization.design.md](refusal-minimization.design.md)
- [authority-and-scope.md](../authority-and-scope.md)

---

> Full history: [../changelog/recovery-contract.changelog.md](../changelog/recovery-contract.changelog.md)
