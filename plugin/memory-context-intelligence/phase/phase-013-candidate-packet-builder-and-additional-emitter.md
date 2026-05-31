# Phase 013 - Candidate packet builder and additional emitter

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 013
> **Status:** Completed
> **Design References:** [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md), [../design/00-core-concept.design.md](../design/00-core-concept.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Build promotion-ready candidate packets and emit selected trial material to `/additional/` as the first real rule-experiment stage.

## Why this phase exists

The runtime becomes useful only if it can turn a selected, evidence-backed topic into a reviewable candidate. The selected destination is `/additional/`, not direct main RULES mutation.

## Goal

Create a safe bridge from selected topic evidence to trial-stage rule material.

## Output

Phase 013 delivered package-local runtime support under `<repo-root>/plugin/memory-context-intelligence/`:

- `lib/candidate_packet.py` candidate packet builder from orchestration `phase_013_candidate_input` or a direct candidate-input payload
- `packet` command surface that emits structured candidate-packet JSON to stdout only
- candidate packet body with summary, signal/evidence basis, owner-domain mapping, proposed additional-stage path, trial-first rationale, risks, success criteria, stop gates, and leader verification needs
- `emit` command surface that previews additional-stage trial material by default
- explicit `--approved-write` path for writing only under a selected additional root
- explicit `--allow-overwrite` gate for replacing an existing emitted trial file
- additional-root late binding through `--additional-root`, `MEMORY_CONTEXT_INTELLIGENCE_ADDITIONAL_ROOT`, `MCI_ADDITIONAL_ROOT`, or the runtime default `~/.claude/rules/additional`
- path-safety refusal for path escapes, absolute paths, hidden segments, main RULES roots, packet stop gates, and unapproved overwrites
- focused tests in `tests/test_candidate_packet.py`
- package-local README, design, changelog, phase, patch, skill, and plugin metadata sync to version `0.6.0`

## Gate

Completed in checked package scope: a selected topic can produce a candidate packet, dry-run emission previews trial-stage material without writing, and explicit approved emission writes only under a controlled additional root without changing main RULES.

This gate is not live trial evaluation, usable-release proof, or main RULES promotion approval. Those remain future phases.

## Owner

Runtime implementation owner for candidate packet generation and additional-stage emission.

## Files

Phase 013 added or updated:

- `<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence`
- `<repo-root>/plugin/memory-context-intelligence/lib/candidate_packet.py`
- `<repo-root>/plugin/memory-context-intelligence/tests/test_candidate_packet.py`
- `<repo-root>/plugin/memory-context-intelligence/README.md`
- `<repo-root>/plugin/memory-context-intelligence/design/design.md`
- `<repo-root>/plugin/memory-context-intelligence/changelog/changelog.md`
- `<repo-root>/plugin/memory-context-intelligence/phase/SUMMARY.md`
- `<repo-root>/plugin/memory-context-intelligence/patch/candidate-packet-builder-and-additional-emitter.patch.md`
- `<repo-root>/plugin/memory-context-intelligence/skills/memory-context-intelligence/SKILL.md`
- `<repo-root>/plugin/memory-context-intelligence/.claude-plugin/plugin.json`

## Verification

- focused candidate packet generation from orchestration result passed
- dry-run emission preview passed and did not write a file
- approved emission to a controlled temporary additional root passed
- overwrite refusal and explicit overwrite allowance passed
- path-safety refusal passed for escaping paths and main RULES-like roots
- full package test discovery passed in checked scope
- CLI help/status reported `packet` and `emit`
- controlled CLI packet/emit smoke check produced packet, preview, and emitted statuses while reporting `main_rules_mutation_performed=False`

Exact commands and actual results are recorded in the phase-013 final closeout report and package patch verification section.

## Risks / rollback notes

The risk is writing trial material without enough evidence or approval. The implementation mitigates this by previewing by default, refusing approved writes when packet stop gates remain, requiring `--approved-write`, requiring `--allow-overwrite` for replacement, and containing output under the selected additional root.

Roll back by removing only the `packet`/`emit` dispatch, `lib/candidate_packet.py`, `tests/test_candidate_packet.py`, and package-local phase-013 docs. Remove any emitted trial file only after explicit destructive confirmation and keep candidate packets as audit context when needed.
