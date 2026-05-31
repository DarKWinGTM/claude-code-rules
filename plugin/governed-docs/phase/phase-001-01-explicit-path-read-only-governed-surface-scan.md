# P001-01 — explicit-path read-only governed surface scan

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P001-01
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/explicit-path-read-only-governed-surface-scan.patch.md](../patch/explicit-path-read-only-governed-surface-scan.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Implement the first real governed-docs runtime slice: require one explicit target workspace path, validate it safely, inventory governed document surfaces from that path, and return a read-only scan result.

## Why this subphase existed

This was the safest first implementation slice because it directly implemented the strongest design constraint without creating hidden governance authority.

What it unlocked:
- every later skill or command can rely on one checked target-path gate
- later evaluator / repair / normalize / release-gate work can build on stable scanner output instead of re-inventing inventory logic
- the plugin can now provide useful report-only behavior without mutating any governed documents

## Design References

- [01-architecture-layers.design.md](../design/01-architecture-layers.design.md)
- [02-governed-surface-inventory.design.md](../design/02-governed-surface-inventory.design.md)
- [06-action-policy-and-release-gate.design.md](../design/06-action-policy-and-release-gate.design.md)

## Lineage Basis

- **Why not current-phase update:** P001 was a design-only bootstrap and stayed closed at that gate
- **Why this still fit the same family:** the work continued the governed-docs bootstrap family and still served the same RULES-specific companion rollout
- **Why not a new major:** a distinct top-level rollout family had not emerged yet, so the smallest bounded continuation remained an existing-family subphase

## Expected Output

- one explicit target-path validation module
- one read-only governed-surface scanner module
- one scan-result model that separates observed facts from later doctrine judgment
- one report-only scan command entry point
- focused tests proving the hard-stop and no-ambient-cwd rules

## Completion Gate

- missing target path hard-stops before scan work starts
- non-existent target path hard-stops before scan work starts
- the scanner inventories known governed families from the named target path only
- the scanner does not use ambient cwd as an implicit target
- the scanner reports inactive `history/` / `done/` surfaces as inactive/referenced rather than junk
- no governed files are edited by this slice
- focused tests pass for the path gate and read-only scanner boundary

## Lane Closeout

### Lane A — implementation
Completed in checked scope:
- explicit target-path gate
- scan result model
- read-only surface scanner
- report-only scan entry point

### Lane B — verification
Completed in checked scope:
- missing-path hard stop
- non-existent-path hard stop
- file-path hard stop where a directory is required
- no ambient-cwd fallback
- report-only / no-mutation behavior

### Lane C — governance sync
Completed in checked scope:
- TODO / phase / changelog / patch sync for the first runtime slice
- separate-later-phase note for Markdown/article HTML presentation based on the checked NodeClaw reference

## Out of Scope

- doctrine evaluator
- repair planner
- normalization executor
- hooks
- custom agents
- release-gate decisions
- article-style HTML presentation for Markdown
- any auto-fix beyond read-only inventory

## Affected Artifacts

Implementation surfaces created:
- `src/governed_docs/target_path.py`
- `src/governed_docs/scan_result.py`
- `src/governed_docs/surface_scanner.py`
- `src/governed_docs/commands/scan.py`
- `tests/test_target_path.py`
- `tests/test_surface_scanner.py`
- `tests/test_scan_command.py`

Governed sync surfaces updated:
- `TODO.md`
- `phase/SUMMARY.md`
- `changelog/changelog.md`
- `patch/explicit-path-read-only-governed-surface-scan.patch.md`

## Development Verification / TestKit Coverage

Verification route used: `new_focused_test`

Why this route was appropriate:
- the slice changed deterministic path validation and a local read-only scanner contract
- focused tests were stronger and cheaper than a larger scenario harness for this first layer
- no live/provider/runtime verification was required because the slice stayed local and read-only

Verification record:
- Ran: `python3 -m unittest discover -s tests -v`
- Result: passed (9 tests)
- Covers: target path validation, no ambient-cwd fallback, inactive history/done classification, report-only command behavior
- Does not cover: evaluator, repair planning, normalization, hook wiring, installation wiring, article-style presentation
- Confidence: verified in checked scope for the first bounded scanner slice

## Risks / Rollback Notes

Primary risks that were contained:
- reading the wrong target because the command falls back to cwd
- mixing scanner output with doctrine judgment too early
- letting inventory code imply cleanup authority over inactive surfaces

Containment used:
- scanner stayed read-only
- scan output stayed separate from doctrine evaluation
- no later layer was opened inside this subphase

## Closeout Summary

Delivered result:
- the explicit target-path doctrine now exists as checked runtime behavior
- the plugin can inventory the first governed surface foundation from a named path and explicitly report that no files were edited

Impact:
- later phases can build on stable local inventory evidence instead of design-only intent
- the most dangerous early failure mode — ambient-cwd target guessing — is now blocked in checked scope

Next phase state:
- no next implementation phase is selected yet
- the strongest next candidates are doctrine evaluation, repair planning, and a separately opened later phase for Markdown/article HTML presentation
