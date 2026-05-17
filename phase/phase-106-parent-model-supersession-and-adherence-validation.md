# P106 — Parent-Model Supersession and Adherence Validation

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P106
> **Status:** Complete / Released
> **Target Release:** v10.14
> **Design References:**
> - [../design/design.md](../design/design.md) v10.14
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/parent-model-supersession-and-adherence-validation.patch.md](../patch/parent-model-supersession-and-adherence-validation.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Strengthen RULES so AI treats the active P105 doctrine as the current authority, does not revive the older P104 semantic-parent-only restriction out of chronology, and validates chronology/supersession explicitly before answering structure-selection questions.

---

## Why This Phase Exists

P105 corrected the active runtime doctrine: folder-scoped single-chain namespaces may use `design/design.md` and `changelog/changelog.md`, while shared folders still use semantic parents and each chain keeps exactly one active parent model.

The remaining gap is adoption and chronology. Some active design companions and reachable completed P104 artifacts still preserve strong P104-era wording without an explicit superseded-by-P105 guard, which can make AI answer from older wording out of chronology even though the active runtime rule is already correct.

---

## Expected Output

- Active doctrine/design surfaces explicitly state that P105 supersedes the older P104 master-only/generic-parent restriction for folder-scoped single-chain namespaces.
- P104 bootstrap-first and shard-opening discipline remains explicitly preserved as active doctrine.
- Reachable completed P104 phase/patch surfaces gain compact historical guard wording so they are not misread as current authority after P105.
- Verification doctrine explicitly checks chronology and supersession across active doctrine versus reachable completed history.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- Current P105 folder-scoped generic-parent and single-parent-authority doctrine remains intact.
- The active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.14` is created and verified.

---

## Action Checklist

- [x] Confirm current baseline is released `v10.13 / P105` with no active phase open before P106 startup.
- [x] Confirm `v10.14` release/tag is not already present.
- [x] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [x] Confirm the untracked `plugin/` tree remains preserved and out of scope.
- [x] Open P106 phase/patch/changelog startup artifacts and sync active roadmap/TODO state.
- [x] Add active-doctrine supersession wording in the touched runtime/design owners.
- [x] Add compact historical guard wording to selected completed P104 artifacts without rewriting their historical truth.
- [x] Extend verification doctrine so chronology/supersession review is explicit.
- [x] Sync touched owner design/changelog companions plus master release surfaces for the P106 release path.
- [x] Validate doctrine integrity, chronology clarity, runtime install, and 18/18 parity/body sufficiency.
- [x] Commit source release, push `master`, create GitHub release `v10.14`, and verify release state.
- [x] Finalize P106 closeout records after release verification passes.

---

## Out of Scope

- Changing the active runtime install scope away from 18 root rules.
- Reopening automated validation script work as a required deliverable in this wave.
- Reopening integration-testing automation as a required deliverable in this wave.
- Weakening the released P102 chain-shape taxonomy or same-stem preference for broad mature chains.
- Weakening the released P103 separation between observed project shape, extracted doctrine, selected target form, and equivalence basis.
- Weakening the released P105 folder-scoped generic-parent and single-parent-authority doctrine.
- Reopening `plugin/` as an active edit or release scope for this wave.
- Deleting existing history/done/archive surfaces as cleanup.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- Touched owner/runtime/design/changelog files align to `v10.14 / P106`.
- Active doctrine explicitly states that P105 supersedes the older P104 master-only/generic-parent restriction for folder-scoped single-chain namespaces.
- Active doctrine still preserves bootstrap/shard timing discipline from the released baseline.
- Reachable completed P104 artifacts include compact historical guard wording where needed so they are not misread as current authority after P105.
- Verification doctrine explicitly reviews chronology/supersession across active doctrine versus reachable completed history.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- Current P105 folder-scoped generic-parent and single-parent-authority doctrine remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `master` push and GitHub release `v10.14` verification pass.

---

## Current Status

P106 is released as `v10.14`.

Release verification summary:
- the current released baseline before the wave was opened was `v10.13 / P105`
- no active phase was open before P106 startup
- `v10.14` tag/release was absent in checked scope before release work began
- README Bash and PowerShell arrays still matched the compact 18-rule runtime set
- the untracked `plugin/` tree remained preserved as out-of-scope observed evidence
- the user selected the full combined scope: active-doctrine supersession hardening, historical guard wording, and bounded manual adherence-validation hardening
- P106 phase/patch/changelog startup plus active roadmap/TODO sync completed in source scope
- active-doctrine supersession wording, selected historical guard wording, and chronology/adherence verification hardening completed in source scope
- runtime install plus 18/18 source/runtime parity and source/destination body sufficiency passed locally
- `git diff --check` passed with no whitespace errors
- `master` push passed
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.14
- Release tag `v10.14` resolves to commit `3e163fc7be7922230155ef0f184f2484b73509a6`
- Published at `2026-05-17T23:36:10Z`.
- Published at `2026-05-17T23:36:10Z`.
