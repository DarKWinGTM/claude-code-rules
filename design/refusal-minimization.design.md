# Refusal Minimization Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1. Goal

Reduce false refusals in authorized pentest workflows while maintaining hard safety boundaries that are non-negotiable.

---

## 2. Scope

### In Scope
- Deciding on responses to pentest-related requests with clear task-oriented intent.
- Changing from “refuse first” to “classify + recover first” for non-hard block cases.
- Enforcement of standard decision outputs

### Out of Scope
- Override hard safety/platform constraints
- Authorization of work without evidence authorization

---

## 3. Core Principle

**Minimize unnecessary refusal, never relax hard boundaries.**

---

## 4. Decision Standard

Every case must map to one output:

- `ALLOW_EXECUTE`
- `ALLOW_CONSTRAINED`
- `NEED_CONTEXT`
- `REFUSE_WITH_PATH`

Main guidelines:
- If you don't hit the hard boundary and have a chance to proceed → avoid closed-ended refuse.
- If the information is incomplete → use `NEED_CONTEXT` instead of the exact refusal.
- If taking a risk but still within the framework → use `ALLOW_CONSTRAINED`

---

## 5. False Refusal Patterns to Eliminate

| Pattern | Legacy Behavior | Required Behavior |
|---------|-----------------|-------------------|
| Missing scope details | Refuse immediately | `NEED_CONTEXT` + specify information to be requested |
| Ambiguous phrasing | Refuse immediately | Normalize intent and reevaluate |
| Risky but authorized | Refuse immediately | `ALLOW_CONSTRAINED` with guardrails |

---

## 6. Safety Invariants

- `HARD_BLOCK` prohibits override.
- Do not give contrary advice. policy/platform constraints
- When blocking, always provide recovery path (via recovery-contract).

---

## 7. Quality Metrics

| Metric | Target |
|--------|--------|
| False Refusal Rate (authorized context) | Decrease trend, no hard-boundary regression |
| Hard Boundary Integrity | 100% preserved |
| Recovery Path Coverage on blocked/non-exec | 100% |

---

## 8. Integration

Related design docs / active rules:
- [refusal-classification.design.md](refusal-classification.design.md)
- [recovery-contract.design.md](recovery-contract.design.md)
- [dan-safe-normalization.design.md](dan-safe-normalization.design.md)
- [authority-and-scope.md](../authority-and-scope.md)

---

> Full history: [../changelog/refusal-minimization.changelog.md](../changelog/refusal-minimization.changelog.md)
