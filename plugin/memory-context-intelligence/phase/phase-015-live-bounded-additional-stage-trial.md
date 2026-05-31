# Phase 015 - Live bounded additional-stage trial

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 015
> **Status:** Completed
> **Design References:** [../design/05-additional-staging-and-promotion.design.md](../design/05-additional-staging-and-promotion.design.md), [../design/02-topic-list-and-choice-flow.design.md](../design/02-topic-list-and-choice-flow.design.md)
> **Patch References:** [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

---

## Objective

Run one bounded live trial that emits a selected candidate to `/additional/` before the runtime is considered usable.

## Why this phase exists

The user selected `/additional/` as the trial stage before main RULES merge. A live bounded trial is the first evidence that the runtime can safely produce useful rule material under real conditions.

## Goal

Demonstrate end-to-end runtime behavior in a controlled live trial without promoting to main RULES.

## Output

- selected live topic and evidence basis
- approved candidate packet
- trial-stage rule material emitted to `/additional/`
- observation notes on usefulness, risk, and required revisions
- clear statement that main RULES merge has not happened

## Completed output

- selected live topic: `topic-001` — `Normalize recurring workflow pattern around memory-context-intelligence / design / changelog`
- evidence basis: bounded live intake sampled 7 memory records with source signal `signal-002` and controlled recorded source fixture support
- candidate packet state: packet built and approved for trial write with no packet stop gates
- emitted additional-stage artifact: `<user-runtime-rules>/additional/memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md`
- disposition: `continue`
- main RULES status: root-level main RULES markdown hash snapshot was unchanged after the live trial in checked scope

## Gate

The phase is complete when a bounded live trial succeeds in `/additional/`, verification confirms main RULES were not changed, and the trial output has a clear continue / revise / retire status.

## Gate result

Completed. The approved live trial emitted one selected trial artifact under the approved additional root, reported disposition `continue`, verified the emitted material contains success criteria and rollback notes, and kept main RULES unchanged in the checked root-level markdown hash scope.

## Owner

Runtime implementation owner plus user approval for any live `/additional/` write.

## Files

- runtime package source: `<repo-root>/plugin/memory-context-intelligence/`
- approved emitted trial file: `<user-runtime-rules>/additional/memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md`
- approved additional-stage root used for this local trial: `<user-runtime-rules>/additional/`
- trial report output: `/tmp/mci-phase015-d42465eb/phase015-live-trial-emitted.json`
- preview trial report output: `/tmp/mci-phase015-d42465eb/phase015-live-trial-preview.json`
- controlled source fixture: `/tmp/mci-phase015-d42465eb/phase015-sources.json`

## Verification

- selected topic and candidate packet were verified before write through the phase-015 preview and approved trial reports
- explicit approval for `/additional/` emission was supplied through `--approved-write` for the approved trial command
- emitted trial material exists at `<user-runtime-rules>/additional/memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md`
- emitted material contains `## Success criteria` and `## Rollback notes`
- root-level main RULES markdown hashes matched before and after the approved live trial in checked scope

Exact verification commands and results:

```bash
python3 -m unittest discover -s "<repo-root>/plugin/memory-context-intelligence/tests"
```

Result: 26 package tests passed.

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" trial --memory-root "<workspace-root>/.memsearch/memory" --scope memory-context-intelligence --sources-fixture "/tmp/mci-phase015-d42465eb/phase015-sources.json" --owner-domain "memory-context-intelligence" --main-rule-target "RULES/plugin/memory-context-intelligence" --additional-root "<user-runtime-rules>/additional" --additional-relative-path "memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md"
```

Result: preview returned `trial-preview`, candidate packet approved for trial write, no file written, and preview material included success criteria plus rollback notes.

```bash
bash "<repo-root>/plugin/memory-context-intelligence/bin/memory-context-intelligence" trial --memory-root "<workspace-root>/.memsearch/memory" --scope memory-context-intelligence --sources-fixture "/tmp/mci-phase015-d42465eb/phase015-sources.json" --owner-domain "memory-context-intelligence" --main-rule-target "RULES/plugin/memory-context-intelligence" --additional-root "<user-runtime-rules>/additional" --additional-relative-path "memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md" --approved-write
```

Result: emitted one file to `<user-runtime-rules>/additional/memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md`, selected `topic-001`, returned disposition `continue`, and reported success criteria plus rollback notes present.

```bash
cmp -s "/tmp/mci-phase015-d42465eb/main-rules-before.sha256" "/tmp/mci-phase015-d42465eb/main-rules-after.sha256"
```

Result: root-level main RULES markdown hash snapshot was unchanged after the live trial in checked scope.

## Risks / rollback notes

This phase includes live file creation in the trial stage. Deletion or rollback of emitted files requires explicit action-and-scope confirmation. Failed trial output should be revised or retired before any promotion discussion.

The emitted trial file is trial-stage material only. It is not usable-runtime proof, install proof, publication proof, stable-behavior proof, or main RULES promotion approval.

Rollback is scoped to the emitted additional-stage trial file and the package phase-015 runtime additions. Main RULES rollback is not needed because main RULES were not mutated.
