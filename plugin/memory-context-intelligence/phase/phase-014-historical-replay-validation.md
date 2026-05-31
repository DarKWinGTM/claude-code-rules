# Phase 014 - Historical replay validation

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 014
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/01-memsearch-required-dependency.design.md](../design/01-memsearch-required-dependency.design.md), [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md), [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Validate the runtime against historical memory traces before using it on live work.

## Why this phase exists

Historical replay gives a safer signal than jumping directly into live rule experimentation. It can show whether bounded intake, signal extraction, topic presentation, selected-topic carry-forward, controlled enrichment, orchestration, candidate packet building, and dry-run emit preview behave consistently on known work traces.

## Goal

Prove the runtime can analyze historical input and produce safe, useful, non-mutating validation evidence.

## Output

Phase 014 delivered package-local runtime support under `<repo-root>/plugin/memory-context-intelligence/`:

- `lib/historical_replay.py` deterministic no-dependency historical replay helper
- `replay` command surface in `bin/memory-context-intelligence`
- bounded replay options for memory root, scope, shard count, record count, character count, shard bytes, selected topic, output mode, language, source fixture, source limit, owner domain, candidate path fields, additional root, and optional emit preview skip
- in-process replay across intake, signals, present, choose, enrich, orchestrate, packet, and dry-run emit preview
- explicit fixture-backed enrichment or no-live-web research skip behavior
- structured replay report covering stage status, bounded historical input metadata, selected topic, topic quality notes, false-positive or weak-signal findings, lane behavior summary, candidate packet safety findings, no-write authority-boundary audit, and adjustments before phase 015
- focused tests in `tests/test_historical_replay.py`
- package-local README, design, changelog, phase, patch, skill, and plugin metadata sync to version `0.7.0`

## Gate

Completed in checked package scope: replay can run the existing chain over bounded historical input, choose a sample topic deterministically, produce a candidate packet, preview additional-stage material without writing, and audit that approved writes, live web access, external agent spawning, install/publication, additional emission, and main RULES mutation are unavailable or unperformed.

The bounded real-corpus replay completed with adjustments. That is acceptable for phase 014 because replay is validation evidence and the reported stop gates/adjustments are the inputs needed before phase 015. This gate is not live `/additional/` trial proof, usable-release proof, install proof, publication proof, or main RULES promotion approval.

## Owner

Runtime implementation owner for validation and replay evidence.

## Files

Phase 014 added or updated:

- `<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence`
- `<repo-root>/plugin/memory-context-intelligence/lib/historical_replay.py`
- `<repo-root>/plugin/memory-context-intelligence/tests/test_historical_replay.py`
- `<repo-root>/plugin/memory-context-intelligence/README.md`
- `<repo-root>/plugin/memory-context-intelligence/design/design.md`
- `<repo-root>/plugin/memory-context-intelligence/changelog/changelog.md`
- `<repo-root>/plugin/memory-context-intelligence/phase/SUMMARY.md`
- `<repo-root>/plugin/memory-context-intelligence/patch/historical-replay-validation.patch.md`
- `<repo-root>/plugin/memory-context-intelligence/skills/memory-context-intelligence/SKILL.md`
- `<repo-root>/plugin/memory-context-intelligence/.claude-plugin/plugin.json`

Capsule governance updates:

- `README.md`
- `design/design.md`
- `changelog/changelog.md`
- `changelog/v0.1.20-completed-historical-replay-validation.changelog.md`
- `phase/SUMMARY.md`
- this phase file
- `patch/memory-context-intelligence-design-only-baseline.patch.md`

## Verification

### Development Verification / TestKit Coverage

Exact commands and actual results from phase-014 closeout:

- `bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" --help`
  - Result: command exited successfully and listed `replay`, replay usage, dry-run replay preview, approved-write unavailability, and main RULES non-mutation boundaries.
- `bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" status`
  - Result: command exited successfully and reported historical replay validation available with dry-run emit preview only and approved writes unavailable.
- `python3 "<repo-root>/plugin/memory-context-intelligence/tests/test_historical_replay.py"`
  - Result: `Ran 3 tests in 0.015s`; `OK`.
- `python3 -m unittest discover -s "<repo-root>/plugin/memory-context-intelligence/tests"`
  - Result: `Ran 24 tests in 0.035s`; `OK`.
- `bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" replay --memory-root "<workspace-root>/.memsearch/memory" --max-shards 2 --max-records 8 --max-chars 6000 --max-shard-bytes 65536 --additional-root "$ADD_ROOT" > "$OUT"`
  - Result: bounded real-corpus replay returned `status=replay-completed-with-adjustments`, `records_sampled=8`, `selected_topic_id=topic-001`, all replay stages `ok=True`, `authority_boundary_ok=True`, `emit_preview_dry_run=True`, `approved_write_available_in_replay=False`, `additional_emission_performed=False`, `main_rules_mutation_performed=False`, `live_web_access_performed=False`, `external_agent_process_spawned=False`, `preview_destination_exists=False`, `additional_root_entries=[]`, and `adjustments_count=2`.

## Risks / rollback notes

The main risk is treating replay output as stronger evidence than it is. Replay validates deterministic behavior on bounded historical input; it does not prove live `/additional/` behavior or runtime usability.

Roll back by removing only the `replay` dispatch path, `lib/historical_replay.py`, `tests/test_historical_replay.py`, and package-local phase-014 docs from the isolated runtime package under `<repo-root>/plugin/memory-context-intelligence/`. No replay-approved writes should exist because replay does not expose approved writes. If a separate direct `emit --approved-write` command created a trial file, remove it only after explicit destructive confirmation.
