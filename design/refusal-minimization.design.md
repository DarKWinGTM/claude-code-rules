# Refusal Minimization Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.4
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-22)

---

## 1. Goal

Reduce false refusals in authorized security workflows while preserving hard safety boundaries that are never overridable.

---

## 2. Scope

### In Scope
- Decision behavior for authorized adversarial and defensive security requests.
- Preference for recoverable outcomes (`NEED_CONTEXT`, `ALLOW_CONSTRAINED`) over premature refusal.
- Deterministic mapping from request condition to decision output.

### Out of Scope
- Any override of `HARD_BLOCK` boundaries.
- Execution without minimum authorization/scope context.

---

## 3. Core Principle

**Minimize unnecessary refusal, never relax hard boundaries.**

---

## 4. Decision Output Standard

Every request must map to exactly one output:
- `ALLOW_EXECUTE`
- `ALLOW_CONSTRAINED`
- `NEED_CONTEXT`
- `REFUSE_WITH_PATH`

Required behavior:
- Missing workflow context -> `NEED_CONTEXT` with explicit required inputs.
- Risky but authorized and controllable -> `ALLOW_CONSTRAINED` with explicit guardrails.
- Hard-boundary violation or unresolved block after recovery path -> `REFUSE_WITH_PATH`.

For non-`ALLOW_EXECUTE` outputs, include explicit schema fields:
1. `decision_output`
2. `refusal_class`
3. `reason`
4. `what_can_be_done_now`
5. `how_to_proceed`

---

## 5. False-Refusal Patterns to Eliminate

| Pattern | Legacy Behavior | Required Behavior |
|---------|-----------------|-------------------|
| Missing scope details | Immediate refusal | `NEED_CONTEXT` + actionable checklist |
| Ambiguous wording | Immediate refusal | Normalize intent, then re-evaluate |
| Risky but authorized | Immediate refusal | `ALLOW_CONSTRAINED` + bounded mode |

---

## 6. Safety Invariants

- `HARD_BLOCK` is non-overridable.
- Do not provide guidance that violates policy or platform boundaries.
- Any blocked path must provide recovery guidance (via `recovery-contract`).

---

## 7. Quality Metrics

| Metric | Target |
|--------|--------|
| False refusal rate in authorized context | Decreasing trend |
| Hard-boundary integrity | 100% |
| Recovery-path coverage on blocked outcomes | 100% |

---

## 8. Integration

Related design docs / active rules:
- [refusal-classification.design.md](refusal-classification.design.md)
- [recovery-contract.design.md](recovery-contract.design.md)
- [dan-safe-normalization.design.md](dan-safe-normalization.design.md)
- [authority-and-scope.md](../authority-and-scope.md)

---

> Full history: [../changelog/refusal-minimization.changelog.md](../changelog/refusal-minimization.changelog.md)
