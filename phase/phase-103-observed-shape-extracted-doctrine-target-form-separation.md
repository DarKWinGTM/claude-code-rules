# P103 — Observed Shape, Extracted Doctrine, and Selected Target Form Separation

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P103
> **Status:** Active / In Progress
> **Target Release:** v10.11
> **Design References:**
> - [../design/design.md](../design/design.md) v10.11
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/observed-shape-extracted-doctrine-target-form-separation.patch.md](../patch/observed-shape-extracted-doctrine-target-form-separation.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Strengthen RULES so AI must keep observed project shape, extracted doctrine, and selected target form separate when using checked examples to justify documentation normalization or governance recommendations.

---

## Why This Phase Exists

P102 made chain-shape selection explicit, but it still left one wording/evidence gap open.

The current RULES can now decide between bootstrap, flat sibling, and same-stem nested normalization, yet the assistant can still talk about a selected target form as if it were literally the observed pattern of a checked project or example.

P103 exists to make that separation explicit so checked examples ground doctrine without being overclaimed as one-to-one proof of the selected RULES target form.

---

## Expected Output

- RULES explicitly separates `observed project shape`, `extracted doctrine`, and `selected target form`.
- The assistant must not describe a selected RULES target form as the literal project pattern unless checked equivalence evidence exists.
- `docs_analysis` grows to include observed shape, extracted doctrine, selected target form, and equivalence-claim basis.
- Current P102 chain-shape doctrine remains intact.
- The active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.11` is created and verified.

---

## Action Checklist

- [x] Confirm current baseline is released `v10.10 / P102` with no active phase open.
- [x] Confirm `v10.11` release/tag is not already present.
- [x] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [x] Confirm the untracked `plugin/` tree remains preserved and out of scope.
- [x] Open P103 phase/patch and sync active roadmap/TODO state.
- [x] Add observed-shape / extracted-doctrine / selected-target separation and equivalence-basis wording to the touched runtime owners.
- [x] Sync touched owner design/changelog companions plus master release surfaces to P103 pre-release state.
- [x] Validate wording/equivalence integrity, compact-entrypoint behavior, runtime install, and 18/18 parity/body sufficiency.
- [ ] Commit source release, push `master`, create GitHub release `v10.11`, and verify release state.
- [ ] Finalize P103 closeout records after release verification passes.

---

## Out of Scope

- Changing the active runtime install scope away from 18 root rules.
- Reopening P102 chain-shape selection as if it were unsettled again.
- Reopening `plugin/` as an active release scope for this wave.
- Converting `changelog/done/` into the normal active detail namespace.
- Turning `TODO.md` or `phase/SUMMARY.md` into link-only routers with no current-state visibility.
- Deleting existing history/done/archive surfaces as cleanup.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- Touched owner/runtime/design/changelog files align to `v10.11 / P103`.
- The five target owners explicitly separate observed project shape, extracted doctrine, and selected target form.
- `docs_analysis` explicitly records equivalence-claim basis when a checked example is used.
- Current P102 chain-shape doctrine remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `master` push and GitHub release `v10.11` verification pass.

---

## Current Status

P103 is active in pre-release implementation for `v10.11`.

Completed so far:
- current baseline is released `v10.10 / P102`
- no active phase was open before P103 started
- `v10.11` tag/release is absent in checked scope
- README arrays still match the compact 18-rule runtime set
- the untracked `plugin/` tree remains preserved as out-of-scope state
- phase/patch startup and active roadmap/TODO sync are open in source scope
- touched doctrine-owner wording updates are complete in source scope
- touched owner design/changelog companions plus master release surfaces are synced to P103 pre-release state
- wording/equivalence validation passed in checked source scope
- runtime install plus 18/18 source/runtime parity and source/destination body sufficiency passed locally
- `git diff --check` passed with no whitespace errors

Still pending:
- source release commit, push, and GitHub release verification
- final closeout after release verification
