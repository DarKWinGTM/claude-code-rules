# RULES Unified Diagram Doctrine Correction Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/document-governance.design.md](../design/document-governance.design.md) v1.11
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch packages the bounded doctrine-correction wave that follows the user's rejection of the earlier fragmented diagram-companion assumption.

The correction target is repo doctrine and governed current-state surfaces first. Plugin/runtime implementation remains downstream and is intentionally not reopened in this patch.

---

## Analysis

The earlier direction assumed diagrams should stay inside `design/**` and split in a companion-friendly pattern. That made tooling shape the doctrine too early and pushed the visual lane toward text-shard symmetry.

The revised target is stricter:
- `design/` remains textual target-state truth
- `diagram/` becomes the governed visual synthesis lane
- `diagram/STRUCTURE.md` becomes the top-level whole-repo visual anchor
- integrated subject diagrams become the default subject shape
- split happens only when visual complexity or genuinely distinct visual questions justify it
- plugin/preview/manifest/report behavior stays downstream and support-only

---

## Change Items

### 1) Document-role correction

- **Target artifact:** touched documentation-governance owner surfaces
- **Change type:** refinement
- **Current state:** active repo role doctrine recognizes README/design/changelog/TODO/phase/patch, but not a dedicated governed `diagram/` lane
- **Target state:** active owner docs explicitly recognize `diagram/` as a first-class governed visual lane with `design/` retaining semantic authority
- **Review point:** do not let the new lane compete with `design/` for semantic truth

### 2) Bootstrap visual anchor

- **Target artifact:** `diagram/STRUCTURE.md`
- **Change type:** additive
- **Current state:** no checked RULES `diagram/` lane bootstrap surface exists in this worktree
- **Target state:** one bodyful top-level visual anchor exists and explains whole-repo structure plus authority boundaries
- **Review point:** keep it bodyful and orientation-first rather than a shallow link-only router

### 3) Inline-diagram boundary correction

- **Target artifact:** touched explanation/diagram-formatting and phase-template surfaces
- **Change type:** refinement
- **Current state:** inline answer/phase-local text-diagram rules are easy to misread as the whole repository diagram doctrine
- **Target state:** inline explanatory diagrams stay governed as answer/presentation aids while repository diagram-lane authority lives under document governance and `diagram/`
- **Review point:** preserve no-frame text-diagram formatting without turning it into repository diagram ownership

### 4) Release-surface sync

- **Target artifact:** touched README/TODO/phase/changelog surfaces
- **Change type:** synchronization
- **Current state:** released baseline is `v10.35 / P127` and no active wave reflects the revised diagram doctrine
- **Target state:** release/current-state surfaces consistently close `v10.36 / P128` as the new latest released baseline and expose the unified diagram doctrine as current repo truth
- **Review point:** keep release wording aligned to the proof actually held

---

## Verification

Required checks before this patch can be called synchronized:
- touched owner surfaces consistently separate textual authority from visual-lane authority
- `diagram/STRUCTURE.md` exists and remains bodyful
- no touched active surface still claims the fragmented companion model as the selected doctrine
- touched TODO/phase/changelog/patch surfaces align to `v10.36 / P128`
- `git diff --check` passes
- if touched runtime owners remain in the active install set, install/parity/body-sufficiency proof is rerun and reported
- no push/release claim is made without explicit approval

---

## Rollback approach

If this correction wave proves wrong before release:
- revert the touched owner-surface sync
- remove the bootstrap `diagram/` lane artifacts opened only for this wave
- restore the previous released `v10.35 / P127` current-state surfaces
- keep the superseded support spec/plan history rather than silently deleting the doctrinal evidence
