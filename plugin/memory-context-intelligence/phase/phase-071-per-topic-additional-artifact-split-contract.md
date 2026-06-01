# Phase 071 - per-topic additional artifact split contract

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

071

## Status

Completed

## Design References

- [../design/design.md](../design/design.md)
- [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
- [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md)

## Patch References

- none

## Objective

Make the plugin-level packet/additional contract explicit: one selected topic must always map to one packet and one additional-stage artifact, and any future multi-topic carry-forward must split into separate per-topic artifacts instead of combining several selected topics into one file.

## Why this phase exists

Phase 070 closed the plugin-scoped release wave, but the packet/additional behavior was still only implicit in the checked code path. The plugin already behaved as one selected topic to one packet to one artifact in the normal path, yet it lacked an explicit contract guard, negative tests, and governed wording that forbids combined multi-topic additional output.

## Gate

Phase 071 closes only when all of the following are true in checked scope:
- `lib/candidate_packet.py` rejects multi-topic packet-derived input that tries to combine several selected topics into one additional artifact
- packet/additional reports and rendered material explicitly state one selected topic per artifact and that combined multi-topic output is forbidden
- orchestration, presentation, and analysis-surface metadata keep adaptive multi-topic deepening advisory-only before selection and preserve the one-topic-per-artifact downstream boundary
- focused tests fail if combined multi-topic additional output is attempted and pass once the guard is implemented
- governed docs explain that multi-topic topic cards remain advisory comparison output only and do not authorize one combined packet/additional artifact

## Development Verification / TestKit Coverage

- Verification route: `new_focused_test`
- Focused commands:
  - `python3 -m unittest discover -s tests -p 'test_candidate_packet.py' -v`
  - `python3 -m unittest discover -s tests -p 'test_orchestration.py' -v`
  - `python3 -m unittest discover -s tests -p 'test_presentation.py' -v`
  - `python3 -m unittest discover -s tests -p 'test_analysis_surface.py' -v`
  - `python3 -m unittest discover -s tests -p 'test_analysis_skill_contract.py' -v`
  - `python3 -m unittest discover -s tests -p 'test_live_trial.py' -v`
  - `python3 -m unittest discover -s tests -p 'test_historical_replay.py' -v`
- Full suite command:
  - `python3 -m unittest discover -s tests -v`
- Proof path:
  - one checked packet-path dry run showing that single-topic preview material includes the explicit topic-scope section and that multi-topic packet-derived input is rejected before emit

## Verification / closeout

Phase 071 is completed in checked scope.

This closeout now holds:
- packet/additional emission explicitly stays one selected topic per artifact
- combined multi-topic additional output is rejected in the runtime packet path instead of remaining an undocumented assumption
- adaptive deepening may still inspect multiple advisory topics before selection, but that advisory multi-topic state cannot be turned into one combined packet/additional artifact
- focused runtime/tests/docs surfaces are aligned to the same split-contract truth

## Boundaries preserved after closeout

Phase 071 still does not claim:
- any weakening of `trace_evidence` as the live promotion anchor
- a changed public surface for `/memory-context-intelligence:analysis`
- reopening `review` or `packet` as public commands
- main RULES mutation, promotion, or merge
- stable/broad production readiness beyond checked scope
