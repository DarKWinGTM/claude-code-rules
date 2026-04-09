# Phase 025-01 - Refine compact table defaults

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 025-01
> **Status:** Completed
> **Design References:** [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md)
> **Patch References:** [../patch/compact-markdown-table-default-and-minimal-table-usage.patch.md](../patch/compact-markdown-table-default-and-minimal-table-usage.patch.md)

---

## Objective

Refine the presentation/explanation owner set so compact markdown tables become the default table form when a table is genuinely useful, while sequence and simple status content stay list-first.

## Why this phase exists

The user wants tables to remain available because they help understanding, but wants the default answer-table shape to become lighter, less decorative, and less bulky than full-frame boxed tables. This phase closes that gap without creating a new first-class doctrine chain.

## Entry conditions / prerequisites

- the compact-table refinement is explicitly bounded to the presentation/explanation owner set
- the governing patch artifact for this wave is already established
- `flow-diagram-no-frame.md` remains a boundary reference, not the main owner of ordinary answer-table behavior

## Action points / execution checklist

- [x] update `answer-presentation` as the primary table/layout owner
- [x] update `explanation-quality` as the supporting decision-flow owner
- [x] update touched design/changelog artifacts for the two owner chains
- [x] create a bounded governed patch artifact for this refinement wave
- [x] keep the refinement bounded and avoid creating a new standalone rule chain

## Out of scope

- changing `flow-diagram-no-frame.md` into a table-format owner
- broad markdown-style cleanup outside table/list choice
- touching wording/tone owners unless a contradiction appears

## Affected artifacts

- `answer-presentation.md`
- `explanation-quality.md`
- touched design and changelog companions for those two chains
- bounded patch and phase artifacts for wave `025`

## TODO coordination

- record the bounded compact-table refinement as completed work in `TODO.md`
- leave unrelated deferred enhancements unchanged

## Changelog coordination

- add per-chain changelog entries for `answer-presentation` and `explanation-quality`
- add one repository-level master changelog entry for release-level visibility

## Verification

- [x] compact markdown tables are now explicitly preferred when a table is genuinely useful
- [x] full-frame ASCII / boxed tables are no longer the default ordinary answer-table shape
- [x] sequence content now explicitly prefers numbered lists
- [x] simple status pairs now explicitly prefer bullets/grouped blocks unless side-by-side scan materially helps

## Risks / rollback notes

- over-applying list-first behavior could hide legitimate comparison value if a real table is actually needed
- rollback should narrow the examples/anti-patterns first rather than removing the compact-table default entirely
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `025-02` sync master docs and runtime install parity
- no additional rollout family is required unless later audit finds drift beyond the touched owner set

## Exit criteria

- [x] compact-table behavior is clearly split across presentation and explanation ownership
- [x] the implementation remains a bounded refinement wave rather than a new first-class doctrine chain
- [x] the touched owner set expresses one coherent compact-table / list-first behavior
