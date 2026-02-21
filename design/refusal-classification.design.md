# Refusal Classification Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-21)

---

## 1. Goal

Establish clear refusal taxonomy to reduce ambiguous refusals and enforce traceable decision outputs.

---

## 2. Refusal Classes

| Class | Definition | Override Policy |
|-------|------------|-----------------|
| `HARD_BLOCK` | Non-negotiable (safety/legal/platform) | ❌ Not overridable |
| `SOFT_BLOCK` | has risk/ambiguity that can be reduced with constraints | ✅ User may select constrained path |
| `WORKFLOW_BLOCK` | Missing evidence or context according to workflow | ✅ User can supply missing context |

---

## 3. Decision Output Mapping

| Decision Output | Typical Refusal Class | Meaning |
|-----------------|-----------------------|---------|
| `ALLOW_EXECUTE` | N/A | Can be executed according to the confirmed scope |
| `ALLOW_CONSTRAINED` | Optional `SOFT_BLOCK` rationale | Operable under guardrails |
| `NEED_CONTEXT` | `WORKFLOW_BLOCK` | Requires additional information before proceeding |
| `REFUSE_WITH_PATH` | `HARD_BLOCK` (or explicit unresolved block) | Refuse with safe path to continue |

---

## 4. Classification Rules

### 4.1 HARD_BLOCK Triggers
- The request clearly intends illegal/out-of-bounds use. authorization
- The request aims to circumvent system security limitations.
- Request at policy/platform Specify prohibition directly

### 4.2 SOFT_BLOCK Triggers
- The work intention is still righteous but the risk is high. There must be constraints first.
- Technical details beyond what is necessary for the current objective.

### 4.3 WORKFLOW_BLOCK Triggers
- Lack of authorization evidence
- Lack of engagement scope (target, boundary, methods)
- Lack of operational context needed to make decisions

---

## 5. Authority Model

- User authority applies to resolution of `SOFT_BLOCK` and `WORKFLOW_BLOCK`
- User authority does not override `HARD_BLOCK`

---

## 6. Output Requirements

When not `ALLOW_EXECUTE`, at least:
1. decision_output
2. refusal_class (if any)
3. reason (concise)
4. next step (via recovery-contract)

---

## 7. Quality Metrics

| Metric | Target |
|--------|--------|
| Classification determinism | 100% same input classifiable same way |
| Ambiguous refusal messages | 0% |
| Output mapping completeness | 100% |

---

## 8. Integration

Related design docs / active rules:
- [recovery-contract.design.md](recovery-contract.design.md)
- [refusal-minimization.design.md](refusal-minimization.design.md)
- [dan-safe-normalization.design.md](dan-safe-normalization.design.md)

---

> Full history: [../changelog/refusal-classification.changelog.md](../changelog/refusal-classification.changelog.md)
