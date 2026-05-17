# P104 — Semantic Parent Naming and Bootstrap-First Design Normalization

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P104
> **Status:** Complete / Released
> **Target Release:** v10.12
> **Design References:**
> - [../design/design.md](../design/design.md) v10.12
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/semantic-parent-naming-and-bootstrap-first-normalization.patch.md](../patch/semantic-parent-naming-and-bootstrap-first-normalization.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Strengthen RULES so AI must choose semantic parent naming and bootstrap-first design normalization before it opens same-stem shard directories or confuses generic compatibility parents with active semantic owners.

---

## Why This Phase Exists

P103 separated observed project shape, extracted doctrine, and selected target form, but it still left one structure-selection gap open.

The current RULES can classify chain shape and keep example evidence separate, yet the assistant can still treat generic parents such as `design/design.md` or placeholder example names as if they were valid steady-state active owners for non-master chains.

P104 exists to make master-versus-subject chain distinction, semantic parent naming, bootstrap-first behavior, and explicit shard-opening triggers deterministic so design normalization does not drift into confusing dual-parent structures.

---

## Expected Output

- RULES explicitly reserves generic master parents such as `design/design.md` and `changelog/changelog.md` for master-chain or explicit compatibility-only roles.
- Non-master chains use semantic parent filenames derived from the actual chain subject.
- `single-file-bootstrap` becomes the explicit default while a chain still has one compact design body.
- Same-stem shard directories open only after explicit `bootstrap_exit_trigger` and `shard_opening_basis` justification.
- Placeholder example names remain illustrative only and must not be treated as mandatory literal active filenames.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- The active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.12` is created and verified.

---

## Action Checklist

- [x] Confirm current baseline is released `v10.11 / P103` with no active phase open.
- [x] Confirm `v10.12` release/tag is not already present.
- [x] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [x] Confirm the untracked `plugin/` tree remains preserved and out of scope.
- [x] Open P104 phase/patch and sync active roadmap/TODO state.
- [x] Add semantic parent naming, bootstrap-first, and no-dual-parent wording to the touched runtime owners.
- [x] Sync touched owner design/changelog companions plus master release surfaces to P104 pre-release state.
- [x] Validate doctrine integrity, compact-entrypoint behavior, runtime install, and 18/18 parity/body sufficiency.
- [x] Commit source release, push `master`, create GitHub release `v10.12`, and verify release state.
- [x] Finalize P104 closeout records after release verification passes.

---

## Out of Scope

- Changing the active runtime install scope away from 18 root rules.
- Weakening the released P102 chain-shape taxonomy or same-stem preference for broad mature chains.
- Weakening the released P103 separation between observed project shape, extracted doctrine, selected target form, and equivalence basis.
- Reopening `plugin/` as an active edit or release scope for this wave.
- Treating placeholder example names as mandatory literals.
- Deleting existing history/done/archive surfaces as cleanup.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- Touched owner/runtime/design/changelog files align to `v10.12 / P104`.
- The selected owners explicitly reserve generic master parents and require semantic parent filenames for non-master chains.
- `docs_analysis` explicitly records chain subject, parent naming basis, bootstrap exit trigger, and shard-opening basis.
- Current P102 chain-shape doctrine remains intact.
- Current P103 evidence-layer separation remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `master` push and GitHub release `v10.12` verification pass.

---

## Current Status

P104 is released as `v10.12`.

Release verification summary:
- current baseline before the wave was released was `v10.11 / P103`
- no active phase was open before P104 started
- `v10.12` tag/release was absent in checked scope before release work began
- README arrays still matched the compact 18-rule runtime set
- the untracked `plugin/` tree remained preserved as out-of-scope observed evidence
- touched doctrine-owner wording and companion/master-surface sync completed in source scope
- doctrine validation passed in checked source scope
- runtime install plus 18/18 source/runtime parity and source/destination body sufficiency passed locally
- `git diff --check` passed with no whitespace errors
- `master` push passed
- Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.12
- Release tag `v10.12` resolves to commit `a5dfb34ab7a26dc91bff3861ca3425bf00c99d8a`
- Published at `2026-05-17T09:16:12Z`.
