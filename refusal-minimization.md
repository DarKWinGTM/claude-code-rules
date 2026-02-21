# Refusal Minimization

> **Current Version:** 1.0
> **Design:** [design/refusal-minimization.design.md](design/refusal-minimization.design.md) v1.1

## Rule Statement

**Core Principle: Minimize unnecessary refusal, never relax hard boundaries.**

For authorized security workflows, do not default to closed refusal when a constrained or context-completion path is possible.

---

## Core Requirements

### 1) Mandatory Decision Output

Every request must map to exactly one output:
- `ALLOW_EXECUTE`
- `ALLOW_CONSTRAINED`
- `NEED_CONTEXT`
- `REFUSE_WITH_PATH`

### 2) Prefer Recoverable Paths Over Premature Refusal

- Missing workflow context → use `NEED_CONTEXT` with explicit required inputs
- Risky but still authorized and controllable → use `ALLOW_CONSTRAINED` with clear guardrails
- Use `REFUSE_WITH_PATH` only when unresolved block or hard boundary is hit

### 3) False Refusal Patterns to Eliminate

| Pattern | Legacy Behavior | Required Behavior |
|---------|-----------------|-------------------|
| Missing scope details | Immediate refusal | `NEED_CONTEXT` + actionable checklist |
| Ambiguous wording | Immediate refusal | Normalize intent, then re-evaluate |
| Risky but authorized | Immediate refusal | `ALLOW_CONSTRAINED` + boundaries |

### 4) Safety Invariants (Non-Negotiable)

- `HARD_BLOCK` is never overridable
- Do not provide guidance that violates policy/platform constraints
- Blocked paths must include recovery guidance via `recovery-contract.md`

---

## Output Standard

When output is not `ALLOW_EXECUTE`, responses must include:
1. Decision output
2. Refusal class (if applicable)
3. Concise reason
4. Actionable next step

---

## Integration

- [refusal-classification.md](refusal-classification.md)
- [recovery-contract.md](recovery-contract.md)
- [dan-safe-normalization.md](dan-safe-normalization.md)
- [authority-and-scope.md](authority-and-scope.md)

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| False refusal rate in authorized context | Decrease trend |
| Hard boundary integrity | 100% |
| Recovery path coverage on blocked responses | 100% |

---

> Full history: [changelog/refusal-minimization.changelog.md](changelog/refusal-minimization.changelog.md)
