# Phase 021-01 - Tighten systemMessage review-required wording

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 021-01
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/compact-reference-first-review-trigger-refinement.patch.md](../patch/compact-reference-first-review-trigger-refinement.patch.md)

---

## Objective

Make the compact SessionStart navigator line explicitly say that review is required before continuation.

## Why this phase exists

The previous navigator line pointed to the right stored session location, but the user wants the visible signal to say clearly that review is required instead of only exposing a path.

## Action points / execution checklist

- [x] prepend `review-required` semantics to success-path `systemMessage`
- [x] prepend `review-required` semantics to fallback `systemMessage`
- [x] keep reviewRoot/review pointers visible
- [x] keep the line short enough to remain navigator-oriented

## Verification

- success-path `systemMessage` contains `review-required`
- fallback `systemMessage` contains `review-required`
- reviewRoot/review pointers remain visible

## Exit criteria

- the visible compact signal now clearly says review is required before continuation
