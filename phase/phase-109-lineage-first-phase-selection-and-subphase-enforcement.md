# P109 — Lineage-First Phase Selection and Subphase Enforcement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P109
> **Status:** Completed / Released
> **Target Release:** v10.17
> **Design References:**
> - [../design/design.md](../design/design.md) v10.17
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/lineage-first-phase-selection-and-subphase-enforcement.patch.md](../patch/lineage-first-phase-selection-and-subphase-enforcement.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Make phase selection lineage-first so AI must check current phase reuse first, then same-family subphase fit, and only open a new major phase when a distinct goal/output/gate/release/rollback boundary is proven.

---

## Why This Phase Exists

The released `v10.16 / P108` wave compacted worker-routing successfully, but phase selection still shows one behavior gap: AI can open a new major phase too early instead of checking whether work should stay in the current phase or become a truthful subphase.

The current RULES already contains the necessary concepts, but the lineage logic is still expressed as criteria and preference wording rather than a strict ordered fall-through gate.

P109 exists to turn phase identity selection into an explicit decision order so AI cannot jump directly to a new major phase by topic change, momentum, or a merely local output/gate difference.

---

## Expected Output

- `phase-todo-artifact.md` enforces a strict ordered phase identity decision gate: current phase → existing-family subphase → new major → ask/record basis.
- `execution-and-goal-frame.md` enforces the same order during active continuation and next-work discovery.
- New-major selection requires visible why-not-current / why-not-subphase basis.
- Phase-shaped continuation no longer treats milestone closure, task-list continuation, or topic drift as automatic new-major authority.
- Touched design companions and owner changelog parents stay aligned.
- The active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.17` is created and verified.

---

## Action Checklist

- [x] Confirm current baseline is released `v10.16 / P108` with no active phase open.
- [x] Confirm `v10.17` release/tag is not already present.
- [x] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [x] Confirm the untracked `plugin/` tree remains preserved and out of scope.
- [x] Open P109 phase/patch and sync active roadmap/TODO state.
- [x] Add lineage-first phase identity enforcement to `phase-todo-artifact.md`.
- [x] Add matching continuation/next-work enforcement to `execution-and-goal-frame.md`.
- [x] Sync touched owner design/changelog companions plus master release surfaces to the P109 source-release state.
- [x] Validate lineage enforcement integrity, runtime install, and 18/18 parity/body sufficiency.
- [x] Commit source release, push `master`, create GitHub release `v10.17`, and verify release state.
- [x] Finalize P109 closeout records after release verification passes.

---

## Out of Scope

- Expanding the active runtime install scope beyond 18 root rules.
- Rewriting phase doctrine into a new standalone runtime owner.
- Treating every new topic, lane, milestone, or task change as a new major phase boundary.
- Reopening `plugin/` as an active edit or release scope for this wave.
- Deleting doctrine instead of strengthening current owner enforcement.

---

## Completion Gate

- Phase identity selection is strict fall-through: current phase → subphase → new major → ask/record basis.
- New-major selection requires visible why-not-current / why-not-subphase reasoning.
- Phase-shaped continuation no longer allows major-phase creation by momentum.
- Touched `phase-todo-artifact` / `execution-and-goal-frame` runtime/design/changelog files align to `v10.17 / P109`.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `plugin/` remains outside staged release scope.
- `master` push and GitHub release `v10.17` verification pass.

---

## Current Status

P109 is completed and released for `v10.17`.

Completed delivery:
- the current released baseline advanced from `v10.16 / P108` to `v10.17 / P109`
- strict ordered fall-through now checks current active phase first, then existing-family subphase, then new major, then ask/record basis
- new-major selection now requires visible why-not-current / why-not-subphase basis
- touched runtime/design/changelog/master surfaces are synchronized in checked scope
- README-driven runtime install passed with 18/18 source/runtime parity and source/destination body sufficiency
- the untracked `plugin/` tree remained preserved as out-of-scope observed evidence
- GitHub release `v10.17` is published at https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.17
- release tag `v10.17` resolves to commit `a330d414c6fd20febf2222288651cc166d0c62b0` and was published at `2026-05-18T14:01:40Z`

Still pending:
- none