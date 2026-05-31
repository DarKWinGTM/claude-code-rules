# P001-03 — repair planner and generated review artifacts

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P001-03
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/repair-planner-and-generated-review-artifacts.patch.md](../patch/repair-planner-and-generated-review-artifacts.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Design References

- [01-architecture-layers.design.md](../design/01-architecture-layers.design.md)
- [03-maintenance-problem-classes.design.md](../design/03-maintenance-problem-classes.design.md)
- [05-generated-artifacts-and-hook-posture.design.md](../design/05-generated-artifacts-and-hook-posture.design.md)
- [06-action-policy-and-release-gate.design.md](../design/06-action-policy-and-release-gate.design.md)

## Objective

Implement Layer C so doctrine-classified findings can be converted into reviewable repair plans and generated maintenance artifacts without mutating governed files.

## Why this phase existed

The evaluator could say what a finding means, but it still could not package that finding into a bounded, reviewable next action. This phase created the planning bridge between classification and any later executor or release gate.

## Expected Output

- repair-planner module(s)
- generated artifact models for scan review, repair plans, phase-audit records, normalization previews, or release-gate inputs where appropriate
- preservation notes and approval-boundary fields in generated outputs
- focused tests proving the planner produces review artifacts rather than hidden mutation

## Completion Gate

- doctrine-classified findings can be transformed into bounded repair outputs
- generated artifacts record checked scope, observed facts, classification result, recommended action, and unresolved ambiguity or approval boundary
- planner output does not mutate governed files
- planner does not collapse into executor behavior
- focused tests pass for artifact generation and approval-boundary handling

## Out of Scope

- direct normalization execution
- hook-driven automation
- user-facing skill installation wiring
- release-ready claims

## Affected Artifacts

Implementation surfaces created:
- `src/governed_docs/generated_artifacts.py`
- `src/governed_docs/repair_planner.py`
- `src/governed_docs/commands/repair_plan.py`
- `tests/test_generated_artifacts.py`
- `tests/test_repair_planner.py`

Governed sync surfaces updated:
- `phase/SUMMARY.md`
- `TODO.md`
- `changelog/changelog.md`
- `patch/repair-planner-and-generated-review-artifacts.patch.md`

## Development Verification / TestKit Coverage

Verification route used: `new_focused_test`

Verification record:
- Ran: `python3 -m unittest discover -s tests -v`
- Result: passed in checked scope
- Covers: repair recommendation mapping, approval-boundary handling, generated repair-plan artifact output, read-only planner boundary
- Does not cover: executor mutation behavior, hook activation, release-gate verdicts, article-style presentation
- Confidence: verified in checked scope for the repair planner slice

## Risks / Rollback Notes

Contained risks:
- generated artifacts becoming hidden owner surfaces
- planner outputs implying approval that was never given
- artifact scope widening beyond the checked finding boundary

Containment used:
- generated artifacts stay review-only
- approval-boundary fields stay explicit per plan item
- planner does not mutate governed files or auto-progress into executor behavior

## Closeout Summary

Delivered result:
- doctrine findings can now be transformed into reviewable repair-plan items
- generated repair-plan artifacts now preserve checked scope, observed facts, recommended action, approval boundary, and preservation notes

Impact:
- later executor and release-gate phases can build from stable review artifacts instead of recomputing repair intent from raw findings

Next phase state:
- P001-04 is completed in checked scope as the operator entry-surface layer
- no later phase depends on reopening P001-03
