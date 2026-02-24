# Refusal Classification Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.3
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-22)

---

## 1. Goal

Define a deterministic refusal taxonomy that produces consistent decision outputs and reduces ambiguous blocked responses.

---

## 2. Refusal Classes

| Class | Definition | Override Policy |
|-------|------------|-----------------|
| `HARD_BLOCK` | Non-negotiable safety/legal/platform prohibition | ❌ Not overridable |
| `SOFT_BLOCK` | Risk/ambiguity reducible by constraints | ✅ Constrained path allowed |
| `WORKFLOW_BLOCK` | Missing authorization/scope/context required to proceed | ✅ User can provide context |

---

## 3. Decision Output Mapping

| Decision Output | Typical Refusal Class | Meaning |
|-----------------|-----------------------|---------|
| `ALLOW_EXECUTE` | N/A | Proceed in confirmed scope |
| `ALLOW_CONSTRAINED` | `SOFT_BLOCK` rationale | Proceed with explicit guardrails |
| `NEED_CONTEXT` | `WORKFLOW_BLOCK` | Require specific missing context |
| `REFUSE_WITH_PATH` | `HARD_BLOCK` (default) or unresolved non-hard block | Refuse with safe alternative path |

---

## 4. Classification Triggers

### 4.1 HARD_BLOCK
- Explicit malicious or unauthorized objective.
- Bypass/evasion intent against safety controls.
- Request directly prohibited by policy/platform boundary.

### 4.2 SOFT_BLOCK
- Legitimate intent but risk details require reduction before execution.
- Request detail level exceeds what is necessary for the current objective.

### 4.3 WORKFLOW_BLOCK
- Missing authorization evidence.
- Missing target/scope/boundary definition.
- Missing operational context required for safe execution.

---

## 5. Authority Model

- User authority resolves `SOFT_BLOCK` and `WORKFLOW_BLOCK`.
- User authority does not override `HARD_BLOCK`.
- Unresolved non-hard blocks may escalate to `REFUSE_WITH_PATH` only after recovery requirements are provided.

---

## 6. Output Requirements

For non-`ALLOW_EXECUTE` outcomes, responses must include:
1. `decision_output`
2. `refusal_class` (if applicable)
3. `reason`
4. `what_can_be_done_now`
5. `how_to_proceed`

---

## 7. Quality Metrics

| Metric | Target |
|--------|--------|
| Classification determinism | 100% |
| Ambiguous refusal messaging | 0% |
| Decision mapping completeness | 100% |

---

## 8. Integration

Related design docs / active rules:
- [refusal-minimization.design.md](refusal-minimization.design.md)
- [recovery-contract.design.md](recovery-contract.design.md)
- [dan-safe-normalization.design.md](dan-safe-normalization.design.md)

---

> Full history: [../changelog/refusal-classification.changelog.md](../changelog/refusal-classification.changelog.md)
