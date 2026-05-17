# Chain-Shape Normalization and Append-vs-Shard Gate Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.10
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.10 / P102`.

It packages a doctrine refinement wave so AI must explicitly classify governed document chain shape before appending or opening shards, with flat sibling shards becoming an allowed normalized form for bootstrap/small chains that already live inside a scoped folder namespace.

---

## Analysis

The released `v10.09 / P101` wave clarified normalized parent/index + shard structures for broad chains and made premise-separation more explicit, but it still left one migration/decision gap open.

The first issue is structural: RULES says broad chains should strongly prefer same-stem parent + shard paths, yet it does not explicitly tell the assistant how to choose between staying in a single-file bootstrap state, opening flat sibling shards in the current folder, or escalating to a same-stem nested shard directory.

The second issue is procedural: because append-vs-shard selection is still implicit, AI can keep appending detail into parent design/changelog files instead of switching to the right shard mode early enough.

---

## Change Items

### 1) Chain-shape doctrine and append-vs-shard gate

- **Target artifact:** `document-governance.md`, `phase-todo-artifact.md`, `worker-routing-and-context.md`
- **Change type:** additive refinement
- **Current state:** same-stem normalized broad-chain doctrine exists, but chain-shape classification and append-vs-shard selection are still implicit.
- **Target state:** RULES explicitly names chain shapes such as `single-file-bootstrap`, `flat-sibling-shards`, and `same-stem-subfolder-normalized`, and requires a compact `docs_analysis` gate before meaningful governed design/changelog normalization work.
- **Review point:** keep flat sibling mode bounded by parent index + shard-map discipline instead of turning it into free-form sharding.

### 2) Integrity and read-order expansion

- **Target artifact:** `document-integrity.md`, `safe-io.md`
- **Change type:** additive refinement
- **Current state:** parent/shard integrity and parent-first reading focus mostly on same-stem parent + nested shard structures.
- **Target state:** integrity and read-order doctrine explicitly covers both flat sibling shard mode and same-stem nested shard mode.
- **Review point:** preserve parent-first + smallest-relevant-shard reading while avoiding mixed-mode orphan or competing authority drift.

### 3) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P102 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.09 / P101` as the current released wave with no active phase open.
- **Target state:** master surfaces identify `v10.10 / P102` as the active chain-shape normalization + append-vs-shard wave until release verification passes.
- **Review point:** keep runtime install count at 18 and keep the `plugin/` tree reference-only and out of release scope.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- Chain-shape doctrine explicitly supports `single-file-bootstrap`, `flat-sibling-shards`, and `same-stem-subfolder-normalized`.
- The append-vs-shard gate and `docs_analysis` form are explicit in checked owner doctrine.
- Parent/shard integrity is explicit for both flat sibling and same-stem nested modes.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- The untracked `plugin/` tree remains outside staged release scope.
- Git diff has no whitespace errors.
- GitHub release `v10.10` must be created and verified before closeout wording claims release completion.

---

## Implementation Status

P102 is active and not yet released.

Phase/patch startup state is open from the released `v10.09 / P101` baseline. Doctrine updates, companion/master-surface sync, runtime install/parity validation, push, GitHub release creation, and closeout verification are still pending.

---

## Rollback Approach

If P102 is reversed after release, restore the prior `v10.09 / P101` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.
