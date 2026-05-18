# Worker-Routing Runtime Compaction and Owner Redistribution Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.16
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.16 / P108`.

It packages a runtime compaction and owner-redistribution correction so `worker-routing-and-context.md` can stay under the performance threshold while preserving routing behavior and moving non-routing doctrine to the correct RULES owners.

---

## Analysis

The released `v10.15 / P107` wave added compact advisory `/goal` suggestion doctrine, but the active worker-routing runtime rule is still oversized.

The first issue is owner overload: `worker-routing-and-context.md` still mixes routing-core behavior with document-density, God-file, append-vs-shard, compact/thrash repair, and delegated governed-document repair doctrine.

The second issue is runtime performance: the active installed worker-routing rule now exceeds the performance warning threshold.

The third issue is owner clarity: the non-routing doctrine already fits `document-integrity.md` and `document-governance.md` better than the routing owner.

---

## Change Items

### 1) Worker-routing runtime compaction

- **Target artifact:** `worker-routing-and-context.md`, `design/worker-routing-and-context.design.md`
- **Change type:** corrective refinement
- **Current state:** worker-routing still carries routing plus non-routing document compaction/repair doctrine.
- **Target state:** worker-routing keeps routing-core behavior, short deferrals to the correct owners, and a body-sufficient compact runtime contract below the performance threshold.
- **Review point:** preserve routing/topology/handoff/leader-verification behavior.

### 2) Document-integrity owner uptake

- **Target artifact:** `document-integrity.md`, `design/document-integrity.design.md`
- **Change type:** owner redistribution
- **Current state:** document-integrity already owns consistency/no-drift/rollover behavior but not the full document-density and God-artifact repair doctrine currently duplicated in worker-routing.
- **Target state:** document-integrity owns moved document-density, compact/thrash, God-line/God-file, density-aware verification, and delegated governed-document repair doctrine.
- **Review point:** preserve preservation-first, no-delete, and no-drift semantics.

### 3) Document-governance owner uptake

- **Target artifact:** `document-governance.md`, `design/document-governance.design.md`
- **Change type:** owner redistribution
- **Current state:** document-governance already owns document-role and parent/shard authority, but worker-routing still carries the large append-vs-restructure-and-shard decision gate.
- **Target state:** document-governance owns the moved append-vs-restructure-and-shard gate and compact governed parent authority-shape selection doctrine.
- **Review point:** preserve current chain-shape and parent-model doctrine without widening install scope.

### 4) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P108 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.15 / P107` as the current released wave with no active phase open.
- **Target state:** master surfaces identify `v10.16 / P108` as the active worker-routing compaction wave until release verification passes.
- **Review point:** keep runtime install count at 18 and keep the `plugin/` tree observed-only and out of release scope.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- `worker-routing-and-context.md` falls below the performance threshold.
- Routing/topology/handoff/leader-verification behavior remains explicit in `worker-routing-and-context.md`.
- Moved document-density / God-artifact / compact-thrash / delegated governed-document repair doctrine is preserved in `document-integrity.md`.
- Moved append-vs-restructure-and-shard doctrine is preserved in `document-governance.md`.
- Current P102/P103/P105/P106/P107 doctrine remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- The untracked `plugin/` tree remains outside staged release scope.
- Git diff has no whitespace errors.
- GitHub release `v10.16` was created and verified before closeout wording claimed release completion.

---

## Implementation Status

P108 is released as `v10.16`.

Phase/patch startup, redistribution edits, companion/master-surface sync, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, `master` push, and GitHub release verification all passed from the released `v10.15 / P107` baseline.

Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.16

Release tag `v10.16` resolves to commit `731624622af67e68869469d74f419d5c67a6752d`.

Published at `2026-05-18T05:01:02Z`.

---

## Rollback Approach

If P108 is reversed after release, restore the prior `v10.15 / P107` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.