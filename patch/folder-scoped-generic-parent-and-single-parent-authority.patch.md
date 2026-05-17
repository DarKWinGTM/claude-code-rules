# Folder-Scoped Generic Parent and Single-Parent Authority Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.13
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.13 / P105`.

It packages a corrective structure-selection refinement so AI may use `design/design.md` and `changelog/changelog.md` in folder-scoped single-chain namespaces while still enforcing exactly one active parent model per chain.

---

## Analysis

The released `v10.12 / P104` wave reduced confusion around semantic parent naming and bootstrap-first behavior, but it still over-restricted generic parent use.

The first issue is namespace scope: when a folder already fully scopes one chain, repeating the subject again in the parent filename can add noise rather than clarity.

The second issue is authority ambiguity: the real danger is not generic parent naming itself, but allowing a generic parent and a semantic parent to coexist as active owners for the same chain.

---

## Change Items

### 1) Folder-scoped generic parent allowance

- **Target artifact:** `document-governance.md`, `phase-todo-artifact.md`
- **Change type:** corrective refinement
- **Current state:** P104 favors semantic parent filenames for non-master chains too strongly.
- **Target state:** RULES explicitly allows `design/design.md` and `changelog/changelog.md` when the current folder fully scopes one chain.
- **Review point:** keep this as parent-model refinement only; do not weaken P102 shape taxonomy.

### 2) Single-parent-per-chain authority rule

- **Target artifact:** `document-governance.md`, `document-integrity.md`, `worker-routing-and-context.md`, `phase-todo-artifact.md`
- **Change type:** corrective refinement
- **Current state:** generic-parent confusion and semantic-parent confusion are treated mainly as naming issues.
- **Target state:** RULES explicitly requires exactly one active parent model per chain and treats dual-parent coexistence as the real anti-pattern.
- **Review point:** preserve bootstrap-first and shard-opening checks while changing the generic-parent allowance rule.

### 3) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P105 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.12 / P104` as the current released wave with no active phase open.
- **Target state:** master surfaces identify `v10.13 / P105` as the active folder-scoped generic-parent correction wave until release verification passes.
- **Review point:** keep runtime install count at 18 and keep the `plugin/` tree observed-only and out of release scope.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- The selected owners explicitly allow generic parents in folder-scoped single-chain namespaces.
- The selected owners explicitly require one active parent model per chain.
- No touched owner allows generic and semantic active parents to coexist for one chain.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- The untracked `plugin/` tree remains outside staged release scope.
- Git diff has no whitespace errors.
- GitHub release `v10.13` was created and verified before closeout wording claimed release completion.

---

## Implementation Status

P105 is released as `v10.13`.

Phase/patch startup, touched doctrine-owner wording, companion/master-surface sync, doctrine validation, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification all passed from the released `v10.12 / P104` baseline.

Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.13

Release tag `v10.13` resolves to commit `b1eba20b8c31041afd794625650a1107d8702e05`.

Published at `2026-05-17T13:43:03Z`.

---

## Rollback Approach

If P105 is reversed after release, restore the prior `v10.12 / P104` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.
