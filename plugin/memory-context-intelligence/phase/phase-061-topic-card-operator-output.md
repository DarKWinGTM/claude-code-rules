# Phase 061 - topic-card operator output

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

061

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/08-memory-evidence-source-model.design.md](../design/08-memory-evidence-source-model.design.md)

## Patch References

- [../patch/analysis-topic-card-operator-output.patch.md](../patch/analysis-topic-card-operator-output.patch.md)

## Objective

Replace the wrapper-style first response for `/memory-context-intelligence:analysis` with repeated topic-card operator output so each surfaced topic is rendered separately using one stable per-topic pattern.

## Why this phase exists

Phase 060 improved internal spine cleanliness, but the user-visible result was still organized around wrapper sections instead of around the topics themselves. The user explicitly corrected that the output had become harder to read because several topics were still being explained through one combined wrapper flow. This phase exists to restore topic-level scanability as the primary UX unit.

## Gate

Phase 061 closes only when all of the following are true in checked scope:
- focused RED/GREEN tests prove default `build_presentation()` now returns repeated `topic_cards`
- focused RED/GREEN tests prove old wrapper keys such as `presentation`, `recommendation`, `proposal`, `related_variants`, `first_response_spine`, `first_response_contract`, and legacy `topic_list` are no longer part of the default operator-facing payload
- focused RED/GREEN tests prove repeated topic cards preserve conditional `Evidence examples`, `Before behavior`, and `After behavior` sections when usable bounded preview evidence exists and omit them when it does not
- focused RED/GREEN tests prove the runtime analysis surface forwards repeated topic cards rather than wrapper sections
- focused RED/GREEN tests prove the public skill contract now requires repeated topic cards and forbids wrapper-style top-level sections for normal operator output
- focused presentation / analysis-surface / skill-contract tests pass
- the full `memory-context-intelligence` suite passes
- one real local `/memory-context-intelligence:analysis` run shows separate repeated topic cards instead of one merged wrapper-style explanation block
- governed/runtime-facing docs are synchronized to the repeated topic-card operator-output contract

## Verification / closeout

Phase 061 is completed in checked scope.

This closeout now holds:
- `lib/presentation.py` now renders default operator-facing output as repeated `topic_cards`
- each topic card carries its own title, status, provenance/evidence summary, and repeated per-topic sections instead of being split across wrapper sections
- `lib/analysis_surface.py` now forwards `topic_cards` and no longer leaks the old wrapper payload keys into the operator-facing runtime output
- focused RED/GREEN proof passed for `tests/test_presentation.py`, `tests/test_analysis_surface.py`, and `tests/test_analysis_skill_contract.py`
- the full runtime/source suite passed with `78` tests
- one checked source-authority `/memory-context-intelligence:analysis` run via `--plugin-dir` now shows separate repeated topic cards (`Topic 1`, `Topic 2`, `Topic 3`) instead of one merged wrapper-style explanation block

## Boundaries preserved after closeout

Phase 061 still does not claim:
- incident-level topic titles or rollback of the doctrine-level title model
- context-only promotion without trace evidence
- fabricated examples when usable bounded preview evidence is absent
- raw memory dumps in operator-facing output
- a change to `/additional/`
- plugin-managed auto-flow proof
- publication or external marketplace release
- stable behavior or broad production readiness
- main RULES promotion
- main RULES mutation
- main RULES merge

## Rollback notes

Phase 061 is a presentation-contract correction layered on top of the existing historical-first, doctrine-level, evidence-grounded proposal contract. Rolling it back would restore the wrapper-style first-response model while keeping historical-first scope, doctrine-level titles, and conditional evidence-example sections intact unless a broader rollback is explicitly selected.
