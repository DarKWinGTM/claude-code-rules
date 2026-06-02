# RULES Diagram Infrastructure Doctrine Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/design.md](../design/design.md) v10.35
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P131 wave.

It packages one bounded doctrine refinement so diagram documentation becomes required RULES infrastructure: `diagram/` is now the only governed diagram authority family, `diagram/STRUCTURE.md` is the mandatory compact active whole-project diagram-side entrypoint, child diagrams stay subordinate members of the same family, and future `diagram/history/` / `diagram/done/` remain preservation infrastructure rather than cleanup.

---

## Analysis

The released P128/P129 direction was already mostly correct:
- `diagram/` existed as a governed visual lane
- governed source was mandatory Kroki-compatible
- `diagram/STRUCTURE.md` was treated as a bodyful whole-project structure authority
- inline answer/phase-local diagrams were kept outside governed source truth unless promoted

But the active model still left one important gap: it had not yet promoted the observed good pattern into explicit RULES infrastructure doctrine. That left room for readers to treat diagram docs as optional companions rather than as a required governed document family with one clear root entrypoint and one clear boundary against `design/**`.

The selected correction is therefore:
- `diagram/` becomes required RULES governed-docs infrastructure
- all governed diagram authority stays under `diagram/`
- `diagram/STRUCTURE.md` becomes the mandatory compact active diagram-side entrypoint
- `diagram/STRUCTURE.md` owns whole-project concept mapping, source/folder topology mapping, authority-boundary explanation, and diagram-to-diagram navigation
- `design/**` remains semantic authority if text and diagram conflict
- future `diagram/history/` / `diagram/done/` remain preservation infrastructure rather than cleanup/disposal authority

This stays bounded. It does not reopen plugin implementation work, does not make diagram docs semantic authority, does not require every subsystem to open a child diagram immediately, and does not expand the runtime install set.

---

## Change Items

### 1) Required diagram family refinement

- **Target artifact:** `document-governance.md` and its design/changelog companions
- **Change type:** refinement
- **Current state:** `diagram/` exists as a governed lane but can still read as conditional/companion infrastructure
- **Target state:** `diagram/` is explicit required governed-docs infrastructure for RULES
- **Review point:** the runtime owner, design companion, and chain changelog all agree on required diagram infrastructure wording

### 2) STRUCTURE ownership refinement

- **Target artifact:** `document-governance.md`, doctrine spec, and `diagram/STRUCTURE.md`
- **Change type:** refinement
- **Current state:** `diagram/STRUCTURE.md` is already bodyful, but its mandatory ownership and role boundaries are not yet fully normalized in the target source path
- **Target state:** `diagram/STRUCTURE.md` is mandatory and explicitly owns concept/folder/topology/boundary/navigation mapping
- **Review point:** the file is bodyful, not a shallow router, and its current-doctrine section states the target posture directly

### 3) Diagram authority boundary refinement

- **Target artifact:** `document-governance.md`, design companion, doctrine spec, and `diagram/STRUCTURE.md`
- **Change type:** refinement
- **Current state:** diagram semantics and design semantics are separated in direction, but the target source path still needs final normalization and release sync
- **Target state:** governed diagram authority stays under `diagram/`, while `design/**` remains semantic authority if text and diagram differ
- **Review point:** no touched surface promotes diagram docs above design authority

### 4) Preservation-infrastructure refinement

- **Target artifact:** `document-governance.md`, doctrine spec, and `diagram/STRUCTURE.md`
- **Change type:** refinement
- **Current state:** history/done governance exists generally, but diagram-specific future preservation wording is not yet released in this wave
- **Target state:** future `diagram/history/` / `diagram/done/` are explicitly preservation infrastructure rather than cleanup authority
- **Review point:** touched wording rejects cleanup/disposal semantics for those future surfaces

### 5) Release-surface sync

- **Target artifact:** touched README/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** latest released baseline is `v10.38 / P130`
- **Target state:** touched master surfaces open and later close `v10.39 / P131` consistently
- **Review point:** release wording remains evidence-calibrated and tied to actual install/push/release proof

---

## Verification

Required checks before release closeout:
- touched owner/runtime/design/spec/structure surfaces agree that `diagram/` is required governed-docs infrastructure for RULES
- touched surfaces agree that governed diagram authority is `diagram/`-scoped only
- touched surfaces agree that `diagram/STRUCTURE.md` is mandatory and bodyful
- touched surfaces agree that `diagram/STRUCTURE.md` owns whole-project concept/folder/topology/boundary/navigation mapping
- touched surfaces preserve `design/**` as semantic authority over diagram docs
- touched surfaces preserve future `diagram/history/` / `diagram/done/` as preservation infrastructure rather than cleanup authority
- touched README/changelog/TODO/phase/patch surfaces align to `v10.39 / P131`
- runtime install/update verification and parity/body-sufficiency checks pass in scope for the touched active runtime owners
- `git diff --check` passes
- remote `master` shows the promoted source state after push/update
- GitHub release `v10.39` is created and verified before closeout wording claims release completion

---

## Implementation Status

P131 is completed.

The source doctrine was tightened in the target RULES path, the doctrine spec and `diagram/STRUCTURE.md` were materialized, touched release surfaces were synchronized, runtime install/update parity for the touched active runtime owners passed in checked scope, `git diff --check` passed, push/update to `master` passed, GitHub release verification passed, and the final closeout state now treats diagram infrastructure as released current doctrine rather than as an unreleased companion direction.
