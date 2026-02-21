# Recovery Contract Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1. Goal

Make every block have a clear “pathway forward”, reducing dead-end refusals and helping users resolve context immediately.

---

## 2. Contract Schema (Mandatory)

When output is `NEED_CONTEXT` or `REFUSE_WITH_PATH` the following fields must be present:

1. **Reason** - Why was it blocked? (Concise, unambiguous)
2. **What can be done now** - Things that can help immediately without violating the boundary.
3. **How ​​to proceed** - Information or conditions that must be filled in in order to proceed.

---

## 3. Response Pattern

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

## 4. Class-Specific Requirements

### 4.1 HARD_BLOCK
- Reason must clearly refer to the boundary type.
- What can be done now must be in safe alternative only.
- How to proceed: Do not propose a route bypass hard boundary.

### 4.2 WORKFLOW_BLOCK
- Reason must point out information that is missing in an actionable way.
- How to proceed must be a short checklist that the user can actually fill in.

### 4.3 SOFT_BLOCK
- Reason must point out risks that can be reduced.
- How to proceed must present a clear constrained mode.

---

## 5. Quality Metrics

| Metric | Target |
|--------|--------|
| Blocked responses with full contract | 100% |
| Dead-end refusal rate | 0% |
| Actionable next-step clarity | High (human-readable, concise) |

---

## 6. Integration

Related design docs / active rules:
- [refusal-classification.design.md](refusal-classification.design.md)
- [refusal-minimization.design.md](refusal-minimization.design.md)
- [authority-and-scope.md](../authority-and-scope.md)

---

> Full history: [../changelog/recovery-contract.changelog.md](../changelog/recovery-contract.changelog.md)
