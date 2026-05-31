# P001-02 — doctrine evaluator and problem-class classification

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P001-02
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/doctrine-evaluator-and-problem-class-classification.patch.md](../patch/doctrine-evaluator-and-problem-class-classification.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Design References

- [01-architecture-layers.design.md](../design/01-architecture-layers.design.md)
- [02-governed-surface-inventory.design.md](../design/02-governed-surface-inventory.design.md)
- [03-maintenance-problem-classes.design.md](../design/03-maintenance-problem-classes.design.md)
- [06-action-policy-and-release-gate.design.md](../design/06-action-policy-and-release-gate.design.md)

## Objective

Implement Layer B so scanner output can be compared against RULES doctrine and classified into stable finding states and maintenance problem classes.

## Why this phase existed

The scanner could report observed surface facts, but it did not yet know what those facts meant under RULES. This phase added the first doctrine-aware judgment layer while keeping mutation out of scope.

## Expected Output

- evaluator module(s) that consume scan results and doctrine inputs
- classification states such as `compliant`, `legacy-but-allowed`, `drift`, `ambiguous-needs-basis`, `safe-auto-repair`, and `blocked`
- maintenance problem-class mapping such as role drift, structure drift, rollover pressure, phase grammar drift, release sync drift, and preservation risk
- focused tests proving doctrine evaluation stays separate from scanner facts and repair planning

## Completion Gate

- evaluator consumes scanner output without falling back to ambient cwd or ad hoc file reads outside the checked target path
- classification states are explicit and testable
- problem-class results are produced from checked doctrine rules rather than string cleanup heuristics
- evaluator remains read-only and does not create repair artifacts or mutate governed files
- focused tests pass for the evaluator boundary

## Out of Scope

- repair-plan generation
- generated review packets
- bounded normalization
- hook wiring
- skill installation wiring
- release-gate verdict output
- article-style Markdown presentation implementation

## Affected Artifacts

Implementation surfaces created:
- `src/governed_docs/finding_models.py`
- `src/governed_docs/doctrine_evaluator.py`
- `tests/test_doctrine_evaluator.py`

Scanner/runtime surfaces preserved and consumed:
- `src/governed_docs/scan_result.py`
- `src/governed_docs/surface_scanner.py`
- `tests/test_surface_scanner.py`
- `tests/test_scan_command.py`
- `tests/test_target_path.py`

Governed sync surfaces updated:
- `phase/SUMMARY.md`
- `TODO.md`
- `changelog/changelog.md`
- `patch/doctrine-evaluator-and-problem-class-classification.patch.md`

## Development Verification / TestKit Coverage

Verification route used: `new_focused_test`

Why this route was appropriate:
- this phase introduced deterministic policy classification logic
- focused tests were the strongest first proof for classification state, maintenance problem-class mapping, and non-mutation boundaries
- release-ready wording remained out of scope

Verification record:
- Ran: `python3 -m unittest discover -s tests -v`
- Result: passed (17 tests)
- Covers: required classification states, maintenance problem-class mapping for the main classes, read-only evaluator boundary, scanner/evaluator compatibility in checked scope, no ambient-cwd fallback preserved
- Does not cover: repair planning, generated artifacts, bounded execution, hook wiring, public skill installation, release-gate flow, article-style presentation
- Confidence: verified in checked scope for the evaluator slice

## Entry Conditions

- P001-01 was completed in checked scope
- the scan result model was stable enough to be consumed by a separate evaluator layer
- doctrine inputs remained the stronger semantic source of truth

## Risks / Rollback Notes

Primary risks that were contained:
- mixing observed facts with judgments too early
- collapsing legacy-only forms into false failures
- letting evaluator output imply repair authority

Containment used:
- evaluator output stayed purely classificatory
- warning-prefix mapping remained explicit and testable
- no repair planner or executor behavior was opened inside this phase

## Closeout Summary

Delivered result:
- Layer B doctrine evaluation now exists as checked runtime behavior on top of the scanner foundation
- required classification states are implemented and proven in focused tests
- main maintenance problem classes are mapped explicitly in the evaluator contract

Impact:
- later phases can now build repair planning and release gating from doctrine-aware findings rather than from raw scan output alone
- the plugin now separates observed facts from RULES judgments in checked scope

Next phase state:
- **P001-03** is the selected next implementation slice for repair planning and generated review artifacts
- article-style Markdown presentation remains a separate later phase and is not implemented here
