# P122 — Goal-to-Plan Default Next-Surface Hardening

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P122
> **Status:** Completed / Released
> **Target Release:** v10.30
> **Design References:**
> - [../design/design.md](../design/design.md) v10.30
> **Patch References:** [../patch/goal-to-plan-default-next-surface-hardening.patch.md](../patch/goal-to-plan-default-next-surface-hardening.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so when a selected governed `/goal` is still route-heavy, AI does not merely preserve the abstract bridge into planning but explicitly recommends `/plan` as the default next surface. `/goal` must remain the objective owner for outcome/done condition/proof/scope, `/plan` must remain the route owner for sequence/task breakdown/verification order, and closeout must continue to verify back against the goal gate rather than treating plan completion alone as success.

---

## Why This Phase Exists

The released `v10.29 / P121` baseline already made the `/goal` ↔ `/plan` boundary explicit, but one practical behavior gap still remains.

The current doctrine says `/goal` can bridge into `/plan` when route complexity is materially non-trivial. That is better than before, but it still leaves too much room for AI to respond with broad prose follow-up rather than explicitly recommending `/plan` as the next working surface.

The result is that goal and plan are now structurally separated, but they still do not cooperate as intentionally as the user wants in actual next-step behavior.

P122 exists to harden that next-step recommendation posture without turning `/plan` into an automatic or mandatory surface for every goal.

---

## Expected Output

- `execution-and-goal-frame.md` encodes that selected governed non-trivial goals should explicitly recommend `/plan` as the default next surface rather than leaving the route as broad prose
- `phase-todo-artifact.md` encodes that governed execution surfaces should carry that explicit `/plan` recommendation when route complexity remains material
- `explanation-and-presentation.md`, `communication-register.md`, and `accurate-communication.md` encode visible wording that says why `/plan` is next and keeps route completion distinct from goal completion
- at least one related playground case is updated so the behavior delta between broad prose follow-up and explicit `/plan` recommendation stays inspectable
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.30 / P122`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.30` verification pass before final closeout wording claims release completion

---

## Action Checklist

- [x] Confirm released baseline is `v10.29 / P121` with no active wave open before P122 startup.
- [x] Open P122 phase and patch execution surfaces.
- [x] Tighten default-next-surface doctrine in `execution-and-goal-frame.md`.
- [x] Tighten governed `/goal` → `/plan` execution-surface recommendation guidance in `phase-todo-artifact.md`.
- [x] Tighten presentation/register/wording owners so AI explicitly recommends `/plan` when the selected governed goal remains route-heavy.
- [x] Sync the directly affected design companions and owner changelog parents.
- [x] Update one related playground case and any directly required reference surface.
- [x] Sync touched master surfaces in README, design, changelog, TODO, phase, and patch.
- [x] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [x] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [x] Run `git diff --check` clean.
- [x] Commit the source release state and push the branch.
- [x] Update the remote default branch so the repo view reflects the released state.
- [x] Create and verify GitHub release `v10.30`.
- [x] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- making `/plan` mandatory for every `/goal`
- turning `/goal` into a mini-plan or route document
- auto-opening `/plan` without route-complexity justification
- weakening candidate-goal behavior, governed-surface `/goal` sourcing, direct continuation priority, or goal-gate closeout doctrine
- expanding the active runtime install set beyond 18 files
- adding `playground/` to runtime install payloads
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched owners explicitly recommend `/plan` as the default next surface when a selected governed goal remains materially route-heavy
- `/goal` still remains the objective owner and `/plan` still remains the route owner
- closeout wording and execution doctrine still verify back against the goal gate instead of plan completion alone
- the updated playground case shows the behavior delta between broad prose follow-up and explicit `/plan` recommendation clearly enough to inspect
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.30 / P122`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.30` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P122 is completed.

Current checked progress:
- released baseline before P122 startup was `v10.29 / P121`
- the selected improvement direction hardened explicit `/plan` next-surface recommendation while preserving `/goal` as the objective contract and `/plan` as the route contract
- touched runtime owners, design companions, owner changelog parents, one related playground case, and touched master surfaces are updated in source scope
- runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `playground/` runtime exclusion recheck, and `git diff --check` all passed
- branch push, remote default-branch verification, GitHub release `v10.30` verification, and final closeout alignment all passed
