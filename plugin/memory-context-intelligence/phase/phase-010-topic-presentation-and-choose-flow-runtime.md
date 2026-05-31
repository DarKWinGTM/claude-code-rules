# Phase 010 - Topic presentation and choose flow runtime

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 010
> **Status:** Completed
> **Design References:** [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md), [../design/00-core-concept.design.md](../design/00-core-concept.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Implement the user-facing topic list and choice flow runtime.

## Why this phase exists

The user must see meaningful options before deeper work begins. The runtime should present medium-detail topics, explain why each topic surfaced, and wait for user selection before any research enrichment or candidate-packet work.

## Goal

Make topic review readable, language-aware, and choice-driven.

## Output

- list-first presentation renderer
- output modes such as `auto`, `native-first`, `bilingual`, and `fixed`
- topic explanation fields for purpose, signal basis, behavior impact, mechanism, expected output, and research need
- choose flow that records the selected topic and rejects unselected automatic promotion

## Gate

The phase is complete when generated topics can be presented to the user and a selected topic can be carried forward without starting enrichment or emission automatically.

## Owner

Runtime implementation owner for presentation and interaction flow.

## Files

Implemented package-local runtime and verification files under `<repo-root>/plugin/memory-context-intelligence/`:
- `lib/presentation.py` — list-first presentation and choose-flow helper
- `bin/memory-context-intelligence` — added `present` and `choose` command dispatch
- `tests/test_presentation.py` — focused presentation and choose-flow tests
- package-local README, design, changelog, phase summary, skill, plugin metadata, and patch docs

Synced capsule governance files:
- `README.md`
- `design/design.md`
- `design/02-topic-list-and-choice-flow.design.md`
- `changelog/changelog.md`
- `changelog/v0.1.16-completed-topic-presentation-and-choose-flow.changelog.md`
- `phase/SUMMARY.md`
- this phase file
- `patch/memory-context-intelligence-design-only-baseline.patch.md`
- `<repo-root>/TODO.md`

## Verification

- `PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' ... compile(...) ... PY`
  - Result: `compiled=5`; compiled `lib/intake.py`, `lib/signals.py`, `lib/presentation.py`, `tests/test_signals.py`, and `tests/test_presentation.py` from source without writing package bytecode caches.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s "<repo-root>/plugin/memory-context-intelligence/tests" -p "test_*.py"`
  - Result: 8 tests passed.
  - Covers: sample topic rendering in `auto`, `native-first`, `bilingual`, and `fixed`; canonical identifier preservation; selection-required carry-forward; advisory-only unselected topics.
- `bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" --help`
  - Result: help/status lists `present` and `choose`, and states research, candidate packet building, `/additional/` emission, main RULES mutation, install, and publication are not performed.
- Controlled `signals -> present -> choose` sample using temporary JSON files under `/tmp`.
  - Result: `present` rendered one topic in each supported output mode with `carry_forward=False`, `choose=False`, `research=False`, and `additional=False`; `choose` selected `topic-001` with selected carry-forward true and research/packet/additional/main-rules flags false.
- `python3 - <<'PY' ... Path('<user-runtime-rules>/additional').exists() ... PY`
  - Result: `additional_path_exists=False` in the checked local environment.

## Risks / rollback notes

The risk is either over-compressing topics so the user cannot decide or over-expanding them into a report dump. Roll back by removing the `present`/`choose` dispatch, `lib/presentation.py`, and `tests/test_presentation.py`, then returning package docs to the phase-009 internal-analysis state while retaining internal topic structures.

## Closeout summary

Phase 010 is complete in checked scope. The runtime now presents phase-009 topic candidates as a list-first user-facing surface, supports `auto`, `native-first`, `bilingual`, and `fixed` output modes, preserves canonical technical identifiers, and records exactly one selected topic before any carry-forward. Unselected topics remain advisory only. Research enrichment, candidate packet building, `/additional/` emission, install/publication, and main RULES mutation remain gated by phase 011+.
