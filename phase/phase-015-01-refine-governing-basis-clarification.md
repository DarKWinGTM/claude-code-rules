# Phase 015-01 - Refine governing-basis clarification

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 015-01
> **Status:** Completed
> **Design References:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/governing-basis-clarification-before-branching.patch.md](../patch/governing-basis-clarification-before-branching.patch.md)

---

## Objective

Refine the ambiguity-handling owner set so materially different governing bases are clarified first through a compact structured question instead of being explored through unnecessary deep branch analysis.

## Why this phase exists

The user reported a real failure mode where the assistant kept exploring multiple pricing-policy interpretations even though the real unblock was to ask which governing basis should control the answer. Once the basis was chosen, the problem collapsed quickly. This phase closes that gap without creating a new first-class doctrine chain.

## Action points / execution checklist

- [x] update `accurate-communication` as the primary governing-basis clarification owner
- [x] update `authority-and-scope` as the user-owned basis-selection boundary owner
- [x] update `evidence-grounded-burden-of-proof` as the unresolved-governing-basis uncertainty owner
- [x] update `explanation-quality` as the over-elaboration restraint owner for unresolved basis ambiguity
- [x] update `answer-presentation` as the compact clarification-form layout owner
- [x] update touched design/changelog artifacts for the touched owner chains
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Verification

- materially different governing bases now trigger clarification before deep branching
- unresolved basis selection is no longer treated like permission to silently pick one active frame
- explanations no longer deepen several mutually exclusive branches before the active basis is chosen
- presentation now supports a compact governing-basis clarification block

## Exit criteria

- governing-basis clarification is clearly split across wording, authority, burden-of-proof, explanation restraint, and layout ownership
- the implementation remains a bounded refinement wave rather than a new doctrine chain
- the touched owner set expresses one coherent ask-before-branch behavior
