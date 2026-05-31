# P126 — Phase Grammar Forms and Release Sync

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P126
> **Status:** Completed / Released
> **Target Release:** v10.34
> **Design References:**
> - [../design/design.md](../design/design.md) v10.34
> - [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.35
> - [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.21
> **Patch References:** [../patch/phase-grammar-forms-and-release-sync.patch.md](../patch/phase-grammar-forms-and-release-sync.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so NodeClaw-informed phase identity grammar is explicit rather than inferred. The released doctrine must make `phase-NNN`, `phase-NNN-NN`, and `phase-NNN-NN-NN` forward-valid numeric execution forms, preserve lineage-first child-phase selection across those three depths, classify observed alphanumeric forms such as `phase-NNN-NNa` as legacy-only unless a later doctrine explicitly normalizes them, keep deeper hybrid forms such as `phase-NNN-NN-NNb` out of the forward-valid grammar by default, and finish the governed sync/release wave across runtime/design/changelog/TODO/phase/patch plus install/parity/release proof.

---

## Why This Phase Exists

The checked NodeClaw phase inventory already contains major phases, ordinary subphases, nested numeric child phases, and observed alphanumeric suffix forms. The old RULES doctrine still named only `NNN` and `NNN-NN`, which left nested numeric depth looking tolerated by precedent rather than explicitly allowed. It also left alphanumeric forms unclassified, which made it too easy for future naming drift to grow from observation into implied doctrine.

P126 exists to close that authority gap without mutating NodeClaw filenames in the same wave. The release target is not a rename campaign. The target is a clear doctrine: explicit forward-valid numeric forms, explicit legacy-only handling for observed alphanumeric variants, explicit rejection of deeper hybrid forms by default, and consistent release-facing sync across governed surfaces.

---

## Expected Output

- `phase-todo-artifact.md` explicitly teaches `NNN`, `NNN-NN`, and `NNN-NN-NN` as forward-valid numeric phase forms
- `phase-todo-artifact.md` explicitly treats observed alphanumeric forms such as `NNN-NNa` as legacy-only unless a later doctrine normalizes them
- `design/phase-implementation.design.md` and related design summaries/checklists sync to the explicit three-level numeric grammar and alphanumeric legacy-only posture
- repository-facing guidance in `README.md` and `document-governance.md` no longer relies on broad `phase-NNN*` wording where exact forward-valid forms matter
- touched changelog/TODO/phase/patch surfaces open and close `v10.34 / P126` consistently
- runtime install into `~/.claude/rules`, 18/18 parity, source/destination body sufficiency, `git diff --check`, branch push, remote default-branch verification, and GitHub release `v10.34` verification all pass

---

## Action Checklist

- [x] Confirm the checked NodeClaw inventory and phase-doc precedent for major, subphase, nested numeric, and alphanumeric forms.
- [x] Compare at least three doctrine approaches and select one evidence-grounded recommendation.
- [x] Tighten the primary runtime doctrine owner so nested numeric child phases are explicitly allowed and alphanumeric forms are explicitly classified.
- [x] Sync directly affected design companions and phase grammar design surfaces.
- [x] Sync repository-facing governance/overview wording where exact phase file forms matter.
- [x] Open and later close touched master surfaces in changelog, TODO, phase, and patch.
- [x] Preserve the no-rename / non-destructive migration posture for NodeClaw filenames in this wave.
- [x] Re-install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [x] Run `git diff --check` clean.
- [x] Commit the release wave, push the branch, update the remote default branch, and verify GitHub release `v10.34`.

---

## Out of Scope

- renaming or migrating real NodeClaw phase files in this wave
- inventing deeper hybrid forms as new forward-valid grammar
- silently treating observed alphanumeric forms as future-valid naming precedent
- expanding the active runtime install set beyond 18 files
- bringing `playground/` into the runtime install payload
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched doctrine owners explicitly allow `phase-NNN`, `phase-NNN-NN`, and `phase-NNN-NN-NN`
- touched doctrine owners explicitly classify observed `phase-NNN-NNa`-style forms as allowed / legacy-only / disallowed forward with no ambiguity left in scope
- touched doctrine owners do not silently allow deeper hybrid forms such as `phase-NNN-NN-NNb`
- before/after examples and non-destructive migration posture are visible in checked scope
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.34 / P126`
- no NodeClaw file rename/migration is claimed or performed in this wave
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch verification, and GitHub release `v10.34` verification pass

---

## Current Status

P126 is completed.

Current checked progress:
- the checked NodeClaw inventory and phase-doc precedent were reviewed before doctrine selection
- the selected doctrine now makes nested numeric child phases explicit forward-valid grammar and keeps observed alphanumeric forms preserved as legacy-only rather than future-valid naming
- touched runtime/design/changelog/TODO/phase/patch/README/document-governance surfaces are updated in source scope
- runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `playground/` runtime exclusion recheck, and `git diff --check` passed
- branch push, remote default-branch verification, GitHub release `v10.34` verification, and closeout alignment passed
