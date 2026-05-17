# Semantic Parent Naming and Bootstrap-First Design Normalization Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.12
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.12 / P104`.

It packages a structure-selection refinement wave so AI must choose semantic parent naming and bootstrap-first design normalization before it opens same-stem shard directories or treats generic compatibility parents as steady-state active owners.

---

## Analysis

The released `v10.11 / P103` wave separated observed project shape from extracted doctrine and selected target form, but it still left one normalization gap open.

The first issue is naming: the assistant can still treat placeholder examples or generic compatibility parents such as `design/design.md` as if they were acceptable steady-state active owners for non-master chains.

The second issue is timing: the assistant can still open same-stem shard directories too early, before a chain has a checked `bootstrap_exit_trigger` or real `shard_opening_basis`.

---

## Change Items

### 1) Semantic parent naming and master-parent reservation

- **Target artifact:** `document-governance.md`, `phase-todo-artifact.md`
- **Change type:** additive refinement
- **Current state:** chain-shape doctrine exists, but generic compatibility parents and placeholder example names can still be confused with active semantic owners.
- **Target state:** RULES explicitly reserves generic master parents for master-chain or compatibility-only roles and requires semantic parent filenames derived from the actual chain subject for non-master chains.
- **Review point:** keep this as naming/selection refinement only; do not reopen P102 shape taxonomy.

### 2) Bootstrap-first and explicit shard-opening basis

- **Target artifact:** `document-governance.md`, `document-integrity.md`, `worker-routing-and-context.md`, `phase-todo-artifact.md`
- **Change type:** additive refinement
- **Current state:** same-stem sharding is allowed and preferred for broad mature chains, but bootstrap-first timing is not explicit enough.
- **Target state:** RULES makes `single-file-bootstrap` the explicit default while a chain still has one compact design body and requires explicit `bootstrap_exit_trigger` and `shard_opening_basis` before same-stem shard directories are opened.
- **Review point:** preserve existing parent authority, no-orphan, and append-vs-shard structure checks while tightening the order of normalization decisions.

### 3) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P104 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.11 / P103` as the current released wave with no active phase open.
- **Target state:** master surfaces identify `v10.12 / P104` as the active semantic-parent/bootstrap-first normalization wave until release verification passes.
- **Review point:** keep runtime install count at 18 and keep the `plugin/` tree as observed evidence only and out of release scope.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- The selected owners explicitly reserve generic master parents and require semantic parent filenames for non-master chains.
- `docs_analysis` explicitly records chain subject, parent naming basis, bootstrap exit trigger, and shard-opening basis.
- No touched owner treats placeholder examples as mandatory literal active names.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- The untracked `plugin/` tree remains outside staged release scope.
- Git diff has no whitespace errors.
- GitHub release `v10.12` must be created and verified before closeout wording claims release completion.

---

## Implementation Status

P104 is released as `v10.12`.

Phase/patch startup, touched doctrine-owner wording, companion/master-surface sync, local validation, runtime install, 18/18 parity/body-sufficiency checks, `master` push, and GitHub release verification all passed from the released `v10.11 / P103` baseline.

Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.12
Release tag `v10.12` resolves to commit `a5dfb34ab7a26dc91bff3861ca3425bf00c99d8a`.
Published at `2026-05-17T09:16:12Z`.

---

## Rollback Approach

If P104 is reversed after release, restore the prior `v10.11 / P103` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.
