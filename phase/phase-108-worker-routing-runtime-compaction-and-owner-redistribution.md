# P108 — Worker-Routing Runtime Compaction and Owner Redistribution

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P108
> **Status:** Active / In Progress
> **Target Release:** v10.16
> **Design References:**
> - [../design/design.md](../design/design.md) v10.16
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/worker-routing-runtime-compaction-and-owner-redistribution.patch.md](../patch/worker-routing-runtime-compaction-and-owner-redistribution.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Reduce `worker-routing-and-context.md` below the performance threshold by moving non-routing doctrine to the correct RULES owners while preserving routing, topology, handoff, and leader-verification behavior as an active body-sufficient runtime rule.

---

## Why This Phase Exists

The released `v10.15 / P107` wave improved compact advisory `/goal` suggestions, but the active worker-routing runtime rule is still too large and now triggers a performance warning.

The current issue is owner overload rather than missing doctrine. `worker-routing-and-context.md` still carries routing behavior plus document-density, God-file, append-vs-shard, compact/thrash repair, and delegated governed-document repair doctrine that belongs more naturally to `document-integrity.md` and `document-governance.md`.

P108 exists to compact the worker-routing runtime rule without deleting meaning: keep routing-core behavior where it belongs, move non-routing doctrine to the correct owners, and preserve the compact 18-rule runtime install set.

---

## Expected Output

- `worker-routing-and-context.md` is reduced below the performance threshold while staying body-sufficient.
- Routing-core doctrine remains in `worker-routing-and-context.md`.
- Non-routing document-density / God-artifact / compact-thrash / delegated governed-document repair doctrine moves to `document-integrity.md`.
- Append-vs-restructure-and-shard and parent/shard authority-shape doctrine moves to `document-governance.md`.
- Touched design companions and owner changelog parents stay aligned.
- The active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.16` is created and verified.

---

## Action Checklist

- [x] Confirm current baseline is released `v10.15 / P107` with no active phase open.
- [x] Confirm `v10.16` release/tag is not already present.
- [x] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [x] Confirm the untracked `plugin/` tree remains preserved and out of scope.
- [x] Open P108 phase/patch and sync active roadmap/TODO state.
- [x] Move non-routing doctrine out of `worker-routing-and-context.md` and compact its runtime body.
- [x] Sync touched owner design/changelog companions plus master release surfaces to P108 pre-release state.
- [ ] Validate redistribution integrity, runtime install, and 18/18 parity/body sufficiency.
- [ ] Commit source release, push `master`, create GitHub release `v10.16`, and verify release state.
- [ ] Finalize P108 closeout records after release verification passes.

---

## Out of Scope

- Expanding the active runtime install scope beyond 18 root rules.
- Deleting doctrine instead of moving it to the correct owner.
- Weakening routing/topology/handoff/leader-verification behavior.
- Reopening `plugin/` as an active edit or release scope for this wave.
- Treating compaction as cleanup/deletion authority.
- Solving unrelated master governance density rollover in the same wave.

---

## Completion Gate

- `worker-routing-and-context.md` falls below the performance threshold.
- Moved doctrine is preserved under the correct active owners.
- Touched worker-routing/document-integrity/document-governance runtime/design/changelog files align to `v10.16 / P108`.
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `plugin/` remains outside staged release scope.
- `master` push and GitHub release `v10.16` verification pass.

---

## Current Status

P108 is active in pre-release implementation for `v10.16`.

Completed so far:
- the current released baseline is `v10.15 / P107`
- no active phase was open before P108 started
- `v10.16` tag/release is absent in checked scope
- README arrays still match the compact 18-rule runtime set
- the untracked `plugin/` tree remains preserved as out-of-scope observed evidence
- P108 phase/patch startup and active roadmap/TODO sync are open in source scope
- redistribution mapping has been identified: routing-core remains in `worker-routing-and-context.md`, non-routing document-repair doctrine moves to `document-integrity.md`, and append-vs-shard authority-shape doctrine moves to `document-governance.md`

Still pending:
- runtime install and 18/18 source/runtime parity/body-sufficiency recheck
- git diff/whitespace review, commit, push, and GitHub release verification
- final closeout after release verification