# Phase 022-01 - Refine direct human-readable wording

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 022-01
> **Status:** Completed
> **Design References:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/natural-professional-communication.design.md](../design/natural-professional-communication.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** [../patch/direct-human-readable-wording-over-metaphor-heavy-shorthand.patch.md](../patch/direct-human-readable-wording-over-metaphor-heavy-shorthand.patch.md)

---

## Objective

Refine the communication-owner set so direct human-readable action/result wording is preferred over metaphor-heavy internal shorthand when both can express the same practical meaning.

## Why this phase exists

The user identified a concrete communication failure where metaphor-heavy internal wording made the practical meaning harder to understand than a direct statement of what changed or what the user could do. This phase closes that gap without creating a new first-class doctrine chain.

## Action points / execution checklist

- [x] update `accurate-communication` as the primary wording owner
- [x] update `explanation-quality` as the explanation-flow support owner
- [x] update `natural-professional-communication` as the style-calibration owner
- [x] update `answer-presentation` as the gloss-near-term layout support owner
- [x] update touched design/changelog artifacts for the touched owner chains
- [x] create a bounded governed patch artifact for this refinement wave
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Verification

- direct human-readable wording is explicitly preferred when a metaphor-heavy shorthand would make the practical meaning harder to grasp
- architecture-first wording is translated into user-visible or action-visible meaning before deeper explanation depends on it
- natural-professional communication no longer treats abstraction-heavy wording as automatically professional
- structured answers now support near-term glossing when an abstract phrase still appears

## Exit criteria

- human-readable wording preference is clearly split across wording, explanation, style, and layout ownership
- the implementation remains a bounded refinement wave rather than a new first-class doctrine chain
- the touched owner set expresses one coherent direct-over-metaphor behavior
