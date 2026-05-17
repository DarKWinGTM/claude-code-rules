# P102 — Chain-Shape Normalization and Append-vs-Shard Gate

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P102
> **Status:** Active / In Progress
> **Target Release:** v10.10
> **Design References:**
> - [../design/design.md](../design/design.md) v10.10
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/chain-shape-normalization-and-append-vs-shard-gate.patch.md](../patch/chain-shape-normalization-and-append-vs-shard-gate.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Strengthen RULES so AI must classify governed document chain shape before appending or sharding, explicitly allowing flat sibling shards for bootstrap/small chains while keeping same-stem parent + subfolder normalization as the strong-preferred form for broad mature chains.

---

## Why This Phase Exists

P101 made normalized parent/index + shard structures much clearer for broad chains, but it still left one practical doctrine gap open.

The current RULES explain the desired normalized end state well, yet they still do not explicitly tell the assistant how to choose between continuing a single parent file, opening flat sibling shards in the existing folder, or escalating to a same-stem nested shard directory.

Because that decision model is still implicit, AI can keep appending to parent design/changelog files even when a clearer shard transition would better match the intended analysis form.

---

## Expected Output

- RULES explicitly names governed chain-shape states such as `single-file-bootstrap`, `flat-sibling-shards`, and `same-stem-subfolder-normalized`.
- RULES adds an explicit append-vs-shard gate before parent design/changelog authority files receive new detail.
- RULES adds a compact `docs_analysis` normalization form in the correct owner surface.
- Flat sibling shard mode becomes an allowed governed pattern when the current folder already acts as the chain namespace.
- Same-stem nested parent + subfolder normalization remains the strong-preferred form for broad mature or God-file-prone chains.
- The active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.10` is created and verified.

---

## Action Checklist

- [x] Confirm current baseline is released `v10.09 / P101` with no active phase open.
- [x] Confirm `v10.10` release/tag is not already present.
- [x] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [x] Confirm the untracked `plugin/` tree remains preserved and out of scope.
- [x] Open P102 phase/patch and sync active roadmap/TODO state.
- [ ] Add chain-shape classification, flat sibling shard doctrine, append-vs-shard gate, and `docs_analysis` form to the touched runtime owners.
- [ ] Sync touched owner design/changelog companions plus master release surfaces to P102 pre-release state.
- [ ] Validate chain-shape doctrine integrity, compact-entrypoint behavior, runtime install, and 18/18 parity/body sufficiency.
- [ ] Commit source release, push `master`, create GitHub release `v10.10`, and verify release state.
- [ ] Finalize P102 closeout records after release verification passes.

---

## Out of Scope

- Changing the active runtime install scope away from 18 root rules.
- Weakening same-stem normalized parent + subfolder doctrine for broad mature chains.
- Treating flat sibling shard mode as unbounded free-form sharding with no parent map.
- Reopening `plugin/memory-context-intelligence/` as an active release scope for this wave.
- Converting `changelog/done/` into the normal active detail namespace.
- Turning `TODO.md` or `phase/SUMMARY.md` into link-only routers with no current-state visibility.
- Deleting existing history/done/archive surfaces as cleanup.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- Touched owner/runtime/design/changelog files align to `v10.10 / P102`.
- Chain-shape doctrine explicitly supports `single-file-bootstrap`, `flat-sibling-shards`, and `same-stem-subfolder-normalized`.
- The append-vs-shard gate and `docs_analysis` form are explicit in the touched owner surfaces.
- Parent/shard integrity covers both same-stem and flat sibling modes.
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `master` push and GitHub release `v10.10` verification pass.

---

## Current Status

P102 is active in pre-release implementation for `v10.10`.

Completed so far:
- current baseline is released `v10.09 / P101`
- no active phase was open before P102 started
- `v10.10` tag/release is absent in checked scope
- README arrays still match the compact 18-rule runtime set
- the untracked `plugin/` tree remains preserved as out-of-scope state
- phase/patch startup and active roadmap/TODO sync are open in source scope

Still pending:
- touched doctrine-owner updates
- companion/master-surface sync
- normalized chain-shape validation
- runtime install and 18/18 source/runtime parity/body-sufficiency recheck
- git diff/whitespace review, commit, push, and GitHub release verification
- final closeout after release verification
