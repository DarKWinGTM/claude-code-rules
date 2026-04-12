# Phase 031-01 - Easy-to-picture concise phase/progress explanation refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 031-01
> **Status:** Completed
> **Design References:** [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md)
> **Patch References:** none

---

## Objective

Make phase and progress explanations easier to picture and easier to read before the denser governance or execution detail appears.

## Why this phase exists

The user identified that some phase/progress explanations were technically correct but still hard to picture quickly. This bounded follow-up refined the explanation-owner set so progress reporting starts with a short plain-language framing layer instead of dropping the reader directly into denser execution detail.

## Entry conditions / prerequisites

- the touched communication/explanation/presentation owners already exist
- the refinement remains bounded to phase/progress explanation shape
- no new first-class doctrine chain is needed if the touched owners can absorb the change cleanly

## Action points / execution checklist

- [x] update `explanation-quality` so phase/progress explanations favor easy-to-picture plain-language framing before deeper detail
- [x] update `accurate-communication` so phase/progress communication opens with short human-readable framing when that improves orientation
- [x] update `answer-presentation` so phase-heavy explanations support concise grouped presentation without becoming overlong
- [x] synchronize touched design/changelog/master surfaces and runtime copies
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Out of scope

- reopening unrelated communication-owner behavior
- changing burden-of-proof or authority semantics
- creating push/release artifacts before sync and verification complete

## Affected artifacts

- `explanation-quality.md`
- `accurate-communication.md`
- `answer-presentation.md`
- touched design/changelog/master surfaces for the bounded follow-up wave

## TODO coordination

- record the bounded follow-up wave in `TODO.md`
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- ensure touched per-chain changelogs align with the already-recorded follow-up changes
- ensure the master changelog records the bounded follow-up wave

## Verification

- [x] phase/progress explanations now begin with easier-to-picture plain-language framing when that materially improves understanding
- [x] denser execution detail now comes after the orienting explanation layer instead of before it
- [x] the refinement remains bounded to the touched explanation/communication/presentation owners

## Risks / rollback notes

- wording could become too repetitive if the plain-language layer restates what is already obvious
- rollback should narrow the framing examples first rather than dropping the readability improvement entirely
- preserve the bounded follow-up history instead of silently erasing it

## Next possible phases

- none required for this bounded follow-up wave
- later explanation refinements should open a new rollout family if needed

## Exit criteria

- [x] easy-to-picture phase/progress explanation behavior is explicit and reviewable
- [x] the bounded follow-up remains separate from unrelated communication-owner changes
- [x] the touched owner set expresses one coherent phase/progress readability improvement
