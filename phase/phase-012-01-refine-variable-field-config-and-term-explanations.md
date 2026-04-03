# Phase 012-01 - Refine variable, field, config, and internal-term explanations

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 012-01
> **Status:** Implemented - Pending Review
> **Design References:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/variable-field-config-and-term-explanation.patch.md](../patch/variable-field-config-and-term-explanation.patch.md)

---

## Objective

Refine the communication/explanation/presentation owner trio so identifier-heavy answers explain what variables, fields, config keys, enum-like values, and internal labels mean before the deeper reasoning depends on them.

## Why this phase exists

The current RULES system already supports human-language glosses, layered explanation, and compact presentation structures, but the user-facing failure mode still appears when answers rely on raw identifiers as if their names were self-explanatory. This phase closes that gap without creating a new first-class rule chain.

## Action points / execution checklist

- [x] update `accurate-communication` as the wording owner
- [x] update `explanation-quality` as the explanation-flow support owner
- [x] update `answer-presentation` as the presentation support owner
- [x] update touched design/changelog artifacts for the three owner chains
- [x] preserve the checked-scope / evidence boundary rather than expanding ownership into `no-variable-guessing`

## Verification

- the touched owner trio now explicitly supports explaining what the identifier is, what role it plays, where it sits in the flow, and what important values mean
- at least one canonical example now shows identifier clarification before deeper reasoning
- the presentation owner now supports a compact glossary / variable-role structure for identifier-heavy answers
- the refinement remains bounded to the existing owner trio and does not create unnecessary ownership drift

## Exit criteria

- raw identifiers are no longer treated as self-explanatory in the touched owner chains
- the new behavior is clearly split across wording, explanation-flow, and presentation ownership
- the implementation remains a bounded refinement wave rather than a new first-class doctrine chain
