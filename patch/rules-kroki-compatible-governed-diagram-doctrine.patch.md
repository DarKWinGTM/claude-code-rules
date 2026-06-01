# RULES Kroki-Compatible Governed Diagram Doctrine Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/document-governance.design.md](../design/document-governance.design.md) v1.12
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch packages the bounded follow-up wave that strengthens the RULES diagram lane after the earlier P128 unified-diagram correction.

The correction target is RULES doctrine and release surfaces only. governed-docs implementation remains downstream and out of scope.

---

## Analysis

P128 established `diagram/` as a dedicated governed visual lane and opened `diagram/STRUCTURE.md` as the whole-repo visual anchor, but it left the rendering/source contract implicit.

P129 closes that gap by making governed `diagram/` source mandatory Kroki-compatible, defining allowed breadth as Kroki-compatible + governance-suitable, and strengthening `diagram/STRUCTURE.md` into a bodyful whole-project detailed visual structure authority instead of a shallow router.

---

## Change Items

### 1) Kroki-compatible source contract

- **Target artifact:** touched document-governance and design-support owner surfaces
- **Change type:** refinement
- **Current state:** governed `diagram/` lane exists, but Kroki-compatible source is not yet mandatory
- **Target state:** active owner docs explicitly require governed `diagram/` source to stay Kroki-compatible and define allowed breadth as Kroki-compatible + governance-suitable
- **Review point:** do not let “all suitable formats” collapse into “anything a renderer happens to accept”

### 2) Whole-project detailed structure authority

- **Target artifact:** `diagram/STRUCTURE.md`
- **Change type:** refinement
- **Current state:** the file is a whole-repo visual anchor, but it can still read too much like a bootstrap router
- **Target state:** one bodyful top-level visual structure surface exists that helps readers understand the project through diagram-first structural detail as much as practical
- **Review point:** keep it whole-project and detail-rich without turning it into semantic text authority over `design/`

### 3) Inline-diagram boundary retention

- **Target artifact:** touched explanation/presentation and phase-template surfaces
- **Change type:** refinement
- **Current state:** inline answer/phase-local text-diagram boundaries are already separate from repository diagram doctrine, but the new Kroki requirement could be misread as applying everywhere
- **Target state:** inline explanatory text diagrams remain outside governed source truth and outside mandatory Kroki enforcement unless explicitly promoted into `diagram/`
- **Review point:** preserve the boundary cleanly so the governed lane strengthens without overreaching into ordinary explanation output

### 4) Release-surface sync

- **Target artifact:** touched README/TODO/phase/changelog surfaces
- **Change type:** synchronization
- **Current state:** latest released baseline is `v10.36 / P128`
- **Target state:** release/current-state surfaces consistently close `v10.37 / P129` as the new latest released baseline and expose the mandatory Kroki-compatible diagram doctrine as current repo truth
- **Review point:** keep release wording aligned to the checked proof actually held

---

## Verification

Required checks before this patch can be called synchronized:
- touched owner surfaces make governed `diagram/` source mandatory Kroki-compatible
- touched owner surfaces define allowed breadth as Kroki-compatible + governance-suitable
- `diagram/STRUCTURE.md` is bodyful and clearly whole-project/detail oriented rather than index/router shaped
- touched owner surfaces preserve `design/` semantic authority over `diagram/`
- touched owner surfaces keep inline answer/phase-local text diagrams outside governed source truth unless explicitly promoted
- touched TODO/phase/changelog/patch surfaces align to `v10.37 / P129`
- `git diff --check` passes
- branch/default-branch/tag/release evidence aligns

---

## Rollback approach

If this correction wave proves wrong before release:
- revert the touched owner-surface sync
- restore the previous released `v10.36 / P128` current-state surfaces
- preserve doctrinal evidence in changelog/spec history rather than silently deleting the wave
