# P105 — Folder-Scoped Generic Parent and Single-Parent Authority

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P105
> **Status:** Active / In Progress
> **Target Release:** v10.13
> **Design References:**
> - [../design/design.md](../design/design.md) v10.13
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/folder-scoped-generic-parent-and-single-parent-authority.patch.md](../patch/folder-scoped-generic-parent-and-single-parent-authority.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Strengthen RULES so AI may use `design/design.md` and `changelog/changelog.md` in folder-scoped single-chain namespaces when the folder already fully scopes one chain, while still forbidding dual-parent ambiguity and preserving bootstrap/shard discipline.

---

## Why This Phase Exists

P104 reduced confusion around semantic parent naming and bootstrap-first normalization, but it still pushed too hard toward semantic parent filenames for non-master chains.

The current RULES still under-support one valid normalization case: when a folder already fully scopes one chain, a generic parent such as `design.md` or `changelog.md` can be clearer than repeating the subject again in the filename.

P105 exists to make that distinction explicit so AI chooses the parent model from namespace scope first and then enforces exactly one active parent model per chain.

---

## Expected Output

- RULES explicitly allows `design/design.md` and `changelog/changelog.md` inside folder-scoped single-chain namespaces.
- RULES explicitly requires one active parent model per chain: generic parent or semantic parent, never both.
- Generic-parent allowance depends on namespace scope, not on master-only status.
- Bootstrap/shard timing discipline remains intact.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- The active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.13` is created and verified.

---

## Action Checklist

- [x] Confirm current baseline is released `v10.12 / P104` with no active phase open.
- [x] Confirm `v10.13` release/tag is not already present.
- [x] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [x] Confirm the untracked `plugin/` tree remains preserved and out of scope.
- [x] Open P105 phase/patch and sync active roadmap/TODO state.
- [x] Replace master-only/generic-parent restriction with folder-scoped single-chain allowance plus single-parent-per-chain doctrine in the touched runtime owners.
- [x] Sync touched owner design/changelog companions plus master release surfaces to P105 pre-release state.
- [ ] Validate doctrine integrity, compact-entrypoint behavior, runtime install, and 18/18 parity/body sufficiency.
- [ ] Commit source release, push `master`, create GitHub release `v10.13`, and verify release state.
- [ ] Finalize P105 closeout records after release verification passes.

---

## Out of Scope

- Changing the active runtime install scope away from 18 root rules.
- Weakening the released P102 chain-shape taxonomy or same-stem preference for broad mature chains.
- Weakening the released P103 separation between observed project shape, extracted doctrine, selected target form, and equivalence basis.
- Reopening `plugin/` as an active edit or release scope for this wave.
- Allowing generic and semantic parents to coexist as active owners for one chain.
- Deleting existing history/done/archive surfaces as cleanup.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- Touched owner/runtime/design/changelog files align to `v10.13 / P105`.
- The selected owners explicitly allow generic parents in folder-scoped single-chain namespaces.
- The selected owners explicitly require one active parent model per chain.
- Bootstrap/shard timing discipline remains intact.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `master` push and GitHub release `v10.13` verification pass.

---

## Current Status

P105 is active in pre-release implementation for `v10.13`.

Completed so far:
- current baseline is released `v10.12 / P104`
- no active phase was open before P105 started
- `v10.13` tag/release is absent in checked scope
- README arrays still match the compact 18-rule runtime set
- the untracked `plugin/` tree remains preserved as out-of-scope observed evidence
- phase/patch startup and active roadmap/TODO sync are open in source scope
- touched doctrine-owner wording updates are complete in source scope
- touched owner design/changelog companions plus master release surfaces are synced to P105 pre-release state

Still pending:
- doctrine validation
- runtime install and 18/18 source/runtime parity/body-sufficiency recheck
- git diff/whitespace review, commit, push, and GitHub release verification
- final closeout after release verification
