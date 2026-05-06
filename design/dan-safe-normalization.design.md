# DAN-Safe Normalization Design

## 0) Document Control

> **Parent Scope:** Claude Code Rules - Authorized Adversarial Workflow
> **Current Version:** 1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-06)

---

## 1. Goal

Convert request with format DAN/jailbreak/ambiguous framing into clear, bounded intent before entering the decision engine

---

## 2. Core Principle

**Normalize form, then evaluate intent and scope.**

The system does not judge by "Provocative rhetoric" only, but extract real work objectives and examine policy according to the normal framework.

---

## 3. Normalization Pipeline

1. **Extract Intent** - Extract the objective that the user actually wants.
2. **Strip Wrapper** - wrap non-objective jailbreak framing instructions
3. **Bind Scope** - Bind intent to available authorization/scope
4. **Classify** - forward refusal-classification
5. **Decide** - forward decision output contract

---

## 4. Normalization Outcomes

| Outcome | Meaning | Next Step |
|---------|---------|-----------|
| Clear + Authorized | Intent clear and within scope | Evaluate for ALLOW_EXECUTE/ALLOW_CONSTRAINED |
| Clear but Missing Context | Intent clear but not enough information | `NEED_CONTEXT` + WORKFLOW_BLOCK |
| Prohibited Intent | Intent is clearly a hard violation | `REFUSE_WITH_PATH` + HARD_BLOCK |

---

## 5. Guardrails

- Do not interpret normalization as bypass policy.
- Do not convert prohibited intent into allowed intent.
- If the intent cannot be clearly normalized, use `NEED_CONTEXT`, not guess.

---

## 6. Quality Metrics

| Metric | Target |
|--------|--------|
| Prompt-form bias in refusal decisions | Minimized |
| Intent extraction clarity | High |
| Wrongful allow from normalization | 0% |

---

## 7. Integration

Related design docs / active rules:
- [refusal-minimization.design.md](refusal-minimization.design.md)
- [refusal-classification.design.md](refusal-classification.design.md)
- [recovery-contract.design.md](recovery-contract.design.md)
- [zero-hallucination.md](../zero-hallucination.md)

---

> Full history: [../changelog/dan-safe-normalization.changelog.md](../changelog/dan-safe-normalization.changelog.md)
