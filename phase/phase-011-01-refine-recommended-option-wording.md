# Phase 011-01 - Refine recommended-option wording

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 011-01
> **Status:** Implemented - Pending Review
> **Design References:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/recommended-option-and-why-this-first.patch.md](../patch/recommended-option-and-why-this-first.patch.md)

---

## Objective

Refine RULES so when multiple next actions are shown and one path is clearly better-supported, the answer presents a recommended option first and explains briefly why it should happen first.

## Why this phase exists

The earlier continuation-first refinement reduced unnecessary option prompting, but it still left a smaller decision-friction gap: when options are genuinely needed, the user can still be forced to infer the preferred path unless the system names it explicitly.

## Action points / execution checklist
- [x] update `accurate-communication` as the primary wording owner
- [x] update `explanation-quality` as the explanation-layer support owner
- [x] update `answer-presentation` as the layout-layer support owner
- [x] sync touched design/changelog artifacts

## Verification
- multiple-option next-step guidance now supports an explicit recommended path
- the recommendation includes a short plain-language why-first reason
- continuation-first behavior remains intact
- touched chains stay within their existing ownership boundaries

## Exit criteria
- the recommendation-plus-reason behavior is explicit in the touched owner chains
- the refinement remains bounded and does not reopen broad option-first behavior
