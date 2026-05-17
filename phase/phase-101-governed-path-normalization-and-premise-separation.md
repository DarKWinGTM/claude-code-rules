# P101 — Governed Path Normalization and Premise-Separation

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P101
> **Status:** Active / In Progress
> **Target Release:** v10.09
> **Design References:**
> - [../design/design.md](../design/design.md) v10.09
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/governed-path-normalization-and-premise-separation.patch.md](../patch/governed-path-normalization-and-premise-separation.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Strengthen RULES so broad governed chains normalize more clearly into path-based parent/index + shard structures, while interaction doctrine more explicitly separates concern, factual claim, proposal, goal, and assistant next action before endorsement or continuation.

---

## Why This Phase Exists

The current RULES baseline already supports design/changelog sharding and TODO/phase rollover, but the active doctrine is still too optional/generic for strong normalization. Broad chains can stay root-heavy too long, especially in live master design and master changelog surfaces.

At the same time, anti-over-agreement behavior is present mostly as wording discipline. P101 exists to add a stronger mechanism so the assistant does not collapse user concern, factual conclusion, goal request, and proposed path into one stream and then reason from an unverified premise.

---

## Expected Output

- Broad governed chains use a stronger parent-index + path-shard normalization doctrine.
- `TODO.md` and `phase/SUMMARY.md` keep a stricter compact-entrypoint + `history/` / `done/` model.
- Master `design/design.md` and `changelog/changelog.md` become compact active parent surfaces with child shard paths where appropriate.
- Interaction doctrine becomes more explicit about concern vs fact vs proposal vs goal vs next action.
- The active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.09` is created and verified.

---

## Action Checklist

- [x] Confirm current baseline is released `v10.08 / P100` with no active phase open.
- [x] Confirm `v10.09` release/tag is not already present.
- [x] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [x] Confirm `design/design/` and `changelog/changelog/` do not already exist in conflicting form.
- [x] Open P101 phase/patch and sync active roadmap/TODO state.
- [x] Strengthen normalization doctrine in `document-governance.md`, `document-integrity.md`, `phase-todo-artifact.md`, and `safe-io.md`.
- [x] Normalize master `design/design.md` into a compact parent index plus child shard path.
- [x] Normalize master `changelog/changelog.md` into a compact parent authority plus version-shard path.
- [x] Strengthen premise-separation doctrine in `communication-register.md`, `evidence-discipline.md`, `execution-and-goal-frame.md`, and `accurate-communication.md`.
- [x] Sync touched owner design/changelog companions plus master release surfaces to P101 pre-release state.
- [ ] Validate normalization integrity, compact-entrypoint behavior, premise-separation mechanism preservation, runtime install, and 18/18 parity/body sufficiency.
- [ ] Commit source release, push `master`, create GitHub release `v10.09`, and verify release state.
- [ ] Finalize P101 closeout records after release verification passes.

---

## Out of Scope

- Changing the active runtime install scope away from 18 root rules.
- Treating NodeClaw-specific automation, numeric hierarchy depth, or source-hash tooling as universal mandatory doctrine.
- Converting `changelog/done/` into the normal active detail namespace for the master chain.
- Turning `TODO.md` or `phase/SUMMARY.md` into link-only routers with no current-state visibility.
- Deleting existing history/done/archive surfaces as cleanup.
- Pulling the untracked `plugin/memory-context-intelligence/` tree into this wave.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- Touched owner/runtime/design/changelog files align to `v10.09 / P101`.
- Parent/shard normalization is explicit for broad active design/changelog chains and validated in checked scope.
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with reachable `history/` / `done/` references.
- Concern/fact/proposal/goal/next-action separation remains explicit in the touched interaction owners.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `master` push and GitHub release `v10.09` verification pass.

---

## Current Status

P101 is active in pre-release validation for `v10.09`.

Completed so far:
- current baseline is released `v10.08 / P100`
- no active phase was open before P101 started
- `v10.09` tag/release is absent in checked scope
- README arrays still match the compact 18-rule runtime set
- `design/design/` and `changelog/changelog/` were opened without path collision
- the untracked `plugin/memory-context-intelligence/` tree was identified and preserved as out-of-scope state
- normalization-owner doctrine updates are applied in source scope
- master `design/design.md` and `changelog/changelog.md` are normalized into compact parent authorities with shard paths
- premise-separation doctrine updates are applied in source scope
- touched design/changelog companions and active master surfaces are synced to P101 pre-release state in source scope

Still pending:
- normalized-structure validation
- runtime install and 18/18 source/runtime parity/body-sufficiency recheck
- git diff/whitespace review, commit, push, and GitHub release verification
- final closeout after release verification
