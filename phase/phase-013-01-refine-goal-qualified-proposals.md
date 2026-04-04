# Phase 013-01 - Refine goal-qualified proposals

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 013-01
> **Status:** Implemented - Pending Review
> **Design References:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/goal-qualified-proposal-boundary.patch.md](../patch/goal-qualified-proposal-boundary.patch.md)

---

## Objective

Refine the communication/authority/explanation/presentation owner set so future-work ideas remain allowed but are expressed as goal-qualified proposals instead of implied queued execution.

## Why this phase exists

The current RULES system already supports continuation-first execution, recommendation formatting, and bounded endings, but a remaining failure mode appears when the assistant suggests future work without a clear goal/output contract or phrases the proposal like the next automatic step. This phase closes that gap without creating a new first-class doctrine chain.

## Action points / execution checklist

- [x] update `accurate-communication` as the primary wording owner
- [x] update `authority-and-scope` as the proposal boundary owner
- [x] update `explanation-quality` as the explanation-flow support owner
- [x] update `answer-presentation` as the layout support owner
- [x] update touched design/changelog artifacts for the touched owner chains
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Verification

- future-work proposals are explicitly marked as advisory
- proposals now state a concrete goal plus expected improvement/result
- proposals no longer read like implied queued execution when the user has not selected them
- the touched owner set remains narrow and role-specific

## Exit criteria

- proposal behavior is clearly split across wording, authority boundary, explanation support, and layout support
- future-wave concepts remain useful without sounding like automatic continuation
- the implementation remains a bounded refinement wave rather than a new first-class doctrine chain
