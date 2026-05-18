# Lineage-First Phase Selection and Subphase Enforcement Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.17
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.17 / P109`.

It packages a phase-lineage enforcement correction so AI must choose the smallest truthful phase identity first instead of opening a new major phase too early.

---

## Analysis

The released `v10.16 / P108` wave corrected worker-routing ownership, but phase selection still has a behavioral gap.

The first issue is ordered enforcement: current doctrine already names current-phase update, subphase, and new major, but does not force AI to test them in that order.

The second issue is negative proof: AI can still justify a new major phase from a local output/gate change without first showing why the current phase and existing-family subphase do not fit.

The third issue is continuation drift: phase-shaped next work can still become a fresh major phase by momentum if current/subphase checks are not applied explicitly during next-work discovery.

---

## Change Items

### 1) Strict lineage-first phase identity gate

- **Target artifact:** `phase-todo-artifact.md`
- **Change type:** corrective refinement
- **Current state:** phase identity doctrine exists, but current phase / subphase / new major selection still reads like criteria rather than a strict fall-through algorithm.
- **Target state:** RULES explicitly enforces current phase → existing-family subphase → new major → ask/record basis, with visible why-not-current / why-not-subphase requirements before a new major phase is allowed.
- **Review point:** preserve current phase/goal/output/gate doctrine and avoid creating a new standalone runtime owner.

### 2) Matching continuation enforcement

- **Target artifact:** `execution-and-goal-frame.md`
- **Change type:** corrective refinement
- **Current state:** execution doctrine already warns against new-major-by-momentum, but still relies on preference wording.
- **Target state:** active continuation applies the same ordered phase identity handling before phase-shaped follow-up becomes a new major phase.
- **Review point:** keep direct safe continuation and next-work discovery behavior intact.

### 3) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P109 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.16 / P108` as the current released wave with no active phase open.
- **Target state:** master surfaces identify `v10.17 / P109` as the active phase-lineage correction wave until release verification passes.
- **Review point:** keep runtime install count at 18 and keep the `plugin/` tree observed-only and out of release scope.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- `phase-todo-artifact.md` enforces current phase → subphase → new major → ask/record basis as a strict fall-through order.
- New-major selection requires visible why-not-current / why-not-subphase basis.
- `execution-and-goal-frame.md` applies the same order during phase-shaped continuation and next-work discovery.
- Current phase/goal/output/gate doctrine remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- The untracked `plugin/` tree remains outside staged release scope.
- Git diff has no whitespace errors.
- GitHub release `v10.17` must be created and verified before closeout wording claims release completion.

---

## Implementation Status

P109 is active and not yet released.

Phase/patch startup, lineage enforcement edits, touched release-surface sync, README-driven runtime install, and 18/18 source/runtime parity/body-sufficiency validation are complete from the released `v10.16 / P108` baseline. `master` push, GitHub release creation, and closeout verification are still pending.

---

## Rollback Approach

If P109 is reversed after release, restore the prior `v10.16 / P108` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.