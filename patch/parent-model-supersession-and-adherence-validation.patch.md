# Parent-Model Supersession and Adherence Validation Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.14
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.14 / P106`.

It packages a chronology/adherence correction so AI follows the active P105 doctrine instead of reviving the older P104 semantic-parent-only restriction from companion or historical surfaces out of chronology.

---

## Analysis

The released `v10.13 / P105` wave corrected the active runtime doctrine, but some active design companions and reachable completed P104 artifacts still preserve strong P104-era wording without an explicit superseded-by-P105 guard.

The first issue is active-doctrine reinforcement: assistants can still merge old and new wording instead of treating P105 as the active authority for folder-scoped single-chain namespaces.

The second issue is chronology leakage: completed P104 phase/patch surfaces can still be read as current authority instead of historical provenance unless they are guarded explicitly.

The third issue is verification posture: current release checks still validate doctrine and parity, but chronology/supersession review is not explicit enough as a manual gate.

---

## Change Items

### 1) Active-doctrine supersession hardening

- **Target artifact:** `document-governance.md`, touched design companions, master design surfaces
- **Change type:** corrective refinement
- **Current state:** active runtime doctrine is correct, but some reachable active design surfaces still preserve older P104-era wording without explicit supersession language.
- **Target state:** active doctrine explicitly states that P105 supersedes the older P104 master-only/generic-parent restriction for folder-scoped single-chain namespaces while preserving bootstrap/shard timing discipline.
- **Review point:** strengthen authority precedence without weakening P102/P103/P105 doctrine.

### 2) Historical guard wording

- **Target artifact:** selected completed P104 phase/patch surfaces, and optional historical detail surfaces if the sweep still shows risk
- **Change type:** chronology clarification
- **Current state:** completed P104 artifacts preserve historically correct wording but can still be misread as current authority after P105.
- **Target state:** completed P104 artifacts keep their historical truth while adding compact guard wording that they are superseded by active P105 doctrine for folder-scoped single-chain namespaces.
- **Review point:** preserve provenance; do not rewrite history into fake P105 history.

### 3) Adherence-validation hardening

- **Target artifact:** verification-oriented design/runtime surfaces
- **Change type:** corrective refinement
- **Current state:** doctrine/parity checks exist, but chronology and supersession review are not explicit enough as a release gate.
- **Target state:** manual verification explicitly checks active-doctrine precedence versus reachable completed-history surfaces.
- **Review point:** keep automation/integration-testing expansion deferred unless explicitly selected later.

### 4) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P106 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.13 / P105` as the current released wave with no active phase open.
- **Target state:** master surfaces identify `v10.14 / P106` as the active supersession/adherence correction wave until release verification passes.
- **Review point:** keep runtime install count at 18 and keep the `plugin/` tree observed-only and out of release scope.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- Active doctrine explicitly states that P105 supersedes the older P104 master-only/generic-parent restriction for folder-scoped single-chain namespaces.
- Active doctrine still preserves bootstrap-first and shard-opening discipline.
- Selected completed P104 artifacts keep historical truth while adding compact chronology guards where needed.
- Chronology/supersession review is explicit in the touched verification doctrine.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- Current P105 folder-scoped generic-parent and single-parent-authority doctrine remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- The untracked `plugin/` tree remains outside staged release scope.
- Git diff has no whitespace errors.
- GitHub release `v10.14` must be created and verified before closeout wording claims release completion.

---

## Implementation Status

P106 is active and not yet released.

Phase/patch startup is open from the released `v10.13 / P105` baseline. Active-doctrine supersession hardening, selected historical guard wording, chronology/adherence verification hardening, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and pre-release master-surface sync are complete in source scope. Push, GitHub release creation, and closeout verification are still pending.

---

## Rollback Approach

If P106 is reversed after release, restore the prior `v10.13 / P105` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.
