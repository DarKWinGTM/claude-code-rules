# Phase Grammar Forms and Release Sync Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.34
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the released `v10.34 / P126` wave.

It packages one bounded doctrine + release-sync refinement so RULES explicitly support the NodeClaw-informed phase identity grammar in checked scope: `phase-NNN`, `phase-NNN-NN`, and `phase-NNN-NN-NN` are forward-valid numeric execution forms; observed alphanumeric forms such as `phase-NNN-NNa` remain preserved as legacy-only unless a later doctrine explicitly normalizes them; and deeper hybrid forms such as `phase-NNN-NN-NNb` are not treated as forward-valid grammar by default.

---

## Analysis

The checked NodeClaw evidence shows three important realities at once:
- major phases and ordinary subphases are already stable doctrine
- nested numeric child phases exist in checked lineage and should not remain merely tolerated precedent
- observed alphanumeric forms exist, but checked docs do not prove they should become future-valid doctrine

The better posture is therefore:
- make the three numeric forms explicit doctrine
- preserve lineage-first child-phase selection across those numeric depths
- preserve observed alphanumeric forms without renaming them now
- classify those alphanumeric forms as legacy-only instead of silently turning them into future grammar
- keep deeper hybrid forms blocked by default until a later doctrine explicitly selects them

This update stays bounded. It does not rename NodeClaw phase files, does not invent a fourth numeric depth, does not silently legalize deeper hybrid forms, does not expand the runtime install set, and does not move `playground/` into the runtime payload.

---

## Change Items

### 1) Explicit numeric phase grammar doctrine

- **Target artifact:** touched phase doctrine owners and related design surfaces
- **Change type:** refinement
- **Current state:** `NNN` and `NNN-NN` were explicit, while `NNN-NN-NN` still read as tolerated precedent rather than explicit doctrine
- **Target state:** `NNN`, `NNN-NN`, and `NNN-NN-NN` are explicit forward-valid numeric phase forms
- **Review point:** preserve lineage-first selection and keep nested numeric depth tied to one bounded parent family / gate

### 2) Alphanumeric legacy-only classification

- **Target artifact:** touched phase grammar/runtime/design/release-facing surfaces
- **Change type:** refinement
- **Current state:** observed forms such as `phase-055-74b ... 74p` existed in checked scope without an explicit doctrine decision
- **Target state:** observed `NNN-NNa`-style forms remain preserved as legacy-only unless a later doctrine explicitly normalizes them
- **Review point:** preserve current evidence without turning observation into future-valid grammar

### 3) Deeper hybrid rejection by default

- **Target artifact:** touched doctrine and verification surfaces
- **Change type:** refinement
- **Current state:** no checked owner surface explicitly closed off hybrid forms such as `NNN-NN-NNb`
- **Target state:** deeper hybrid forms are not forward-valid grammar by default
- **Review point:** stop future drift without retroactive destructive cleanup

### 4) Release-surface and install-proof sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces plus install/parity verification outputs
- **Change type:** release synchronization
- **Current state:** latest released baseline was `v10.33 / P125`
- **Target state:** touched master surfaces open and later close `v10.34 / P126` consistently while preserving the 18-file runtime install scope and the non-runtime `playground/` boundary
- **Review point:** keep runtime install scope at 18 and make no claim that NodeClaw filenames were renamed in this wave

---

## Verification

Required checks before release closeout:
- touched doctrine owners explicitly allow `phase-NNN`, `phase-NNN-NN`, and `phase-NNN-NN-NN`
- touched doctrine owners explicitly classify observed `phase-NNN-NNa`-style forms as allowed / legacy-only / disallowed forward with no ambiguity left in checked scope
- touched doctrine owners do not silently allow deeper hybrid forms such as `phase-NNN-NN-NNb`
- before/after examples and non-destructive migration posture are visible in checked scope
- touched release/master surfaces align to `v10.34 / P126`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the updated master surfaces after update
- GitHub release `v10.34` is created and verified before closeout wording claims release completion

---

## Implementation Status

P126 is completed.

The checked NodeClaw inventory and phase-doc precedent were established, the bounded doctrine direction was selected, and the release wave was closed without renaming NodeClaw phase files. Touched runtime/design/changelog/TODO/phase/patch/README/document-governance surfaces were synchronized, runtime install-boundary proof plus 18/18 parity/body-sufficiency verification passed, `git diff --check` passed, branch/default-branch push verification passed, and GitHub release verification passed.
