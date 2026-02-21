# Refusal Classification

> **Current Version:** 1.0
> **Design:** [design/refusal-classification.design.md](design/refusal-classification.design.md) v1.1

## Rule Statement

**Core Principle: Classify refusal deterministically before deciding response mode.**

All blocked or constrained outcomes must be traceable to a clear refusal class.

---

## Refusal Classes

| Class | Definition | Override Policy |
|-------|------------|-----------------|
| `HARD_BLOCK` | Non-negotiable safety/legal/platform prohibition | ❌ Not overridable |
| `SOFT_BLOCK` | Risk/ambiguity that can be reduced with constraints | ✅ Constrained path allowed |
| `WORKFLOW_BLOCK` | Missing authorization/scope/context required to proceed | ✅ User can provide context |

---

## Decision Output Mapping

| Decision Output | Typical Refusal Class | Meaning |
|-----------------|-----------------------|---------|
| `ALLOW_EXECUTE` | N/A | Proceed in confirmed scope |
| `ALLOW_CONSTRAINED` | `SOFT_BLOCK` rationale | Proceed with explicit guardrails |
| `NEED_CONTEXT` | `WORKFLOW_BLOCK` | Require specific missing context |
| `REFUSE_WITH_PATH` | `HARD_BLOCK` (or unresolved block) | Refuse with safe alternative path |

---

## Classification Triggers

### HARD_BLOCK
- Explicit malicious/unauthorized objective
- Evasion or bypass intent against safety controls
- Directly prohibited by policy/platform boundary

### SOFT_BLOCK
- Legitimate intent but high-risk details need reduction
- Request detail level exceeds what is necessary for current objective

### WORKFLOW_BLOCK
- Missing proof of authorization
- Missing target/scope/boundary definition
- Missing required operational context

---

## Authority Model

- User authority resolves `SOFT_BLOCK` and `WORKFLOW_BLOCK`
- User authority does not override `HARD_BLOCK`

---

## Output Requirements

For non-`ALLOW_EXECUTE` responses, include at minimum:
1. `decision_output`
2. `refusal_class` (if applicable)
3. `reason`
4. `next_step`

---

## Integration

- [refusal-minimization.md](refusal-minimization.md)
- [recovery-contract.md](recovery-contract.md)
- [dan-safe-normalization.md](dan-safe-normalization.md)

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Classification determinism | 100% |
| Ambiguous refusal messages | 0% |
| Decision mapping completeness | 100% |

---

> Full history: [changelog/refusal-classification.changelog.md](changelog/refusal-classification.changelog.md)
