# Phase 024-01 - Refine purpose-first communication

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 024-01
> **Status:** Completed
> **Design References:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/natural-professional-communication.design.md](../design/natural-professional-communication.design.md)
> **Patch References:** [../patch/purpose-first-communication-framing.patch.md](../patch/purpose-first-communication-framing.patch.md)

---

## Objective

Refine the communication-owner set so diagnosis, test, recommendation, proposal, and implementation-update answers state what they are doing before the supporting detail expands.

## Why this phase exists

The user identified a concrete failure mode where the explanation became understandable only after several detailed sentences, even though the core point could be stated directly at the top. This phase closes that gap without creating a new first-class doctrine chain.

## Entry conditions / prerequisites

- the purpose-first refinement is explicitly bounded to the communication-owner set rather than a new standalone rule chain
- the touched owner set is limited to wording, explanation, presentation, and style owners
- the governing patch artifact for this wave is already established

## Action points / execution checklist

- [x] update `accurate-communication` as the primary wording owner
- [x] update `explanation-quality` as the explanation-flow support owner
- [x] update `answer-presentation` as the layout support owner
- [x] update `natural-professional-communication` as the style-calibration owner
- [x] update touched design/changelog artifacts for the touched owner chains
- [x] create a bounded governed patch artifact for this refinement wave
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Out of scope

- creating a new first-class doctrine chain just for purpose-first behavior
- changing burden-of-proof, source-trust, or contradiction semantics outside the touched owner set
- broadening the wave into unrelated wording or runtime-governance areas

## Affected artifacts

- `accurate-communication.md`
- `explanation-quality.md`
- `answer-presentation.md`
- `natural-professional-communication.md`
- touched design and changelog companions for the four owner chains
- bounded patch and phase artifacts for wave `024`

## TODO coordination

- record the bounded purpose-first refinement as completed work in `TODO.md`
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- add per-chain changelog entries for the four touched owner chains
- add one repository-level master changelog entry for release-level visibility

## Verification

- [x] operational answers now state what they are doing earlier when the reader would otherwise need to infer the point from later detail
- [x] explanation flow now includes a purpose-first step before deeper mechanism detail where needed
- [x] presentation guidance now supports a compact purpose-first framing line near the start
- [x] natural professional style now treats purpose-before-detail wording as part of sounding like a strong human operator

## Risks / rollback notes

- over-applying purpose-first framing to already-clear short answers could add unnecessary ceremony
- rollback should narrow the examples/layout support first rather than removing the wording-owner requirement entirely
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `024-02` sync master docs and runtime install parity
- no additional rollout family is required unless later evidence shows the touched owner set still drifts after sync

## Exit criteria

- [x] purpose-first behavior is clearly split across wording, explanation, presentation, and style ownership
- [x] the implementation remains a bounded refinement wave rather than a new first-class doctrine chain
- [x] the touched owner set expresses one coherent purpose-first behavior
