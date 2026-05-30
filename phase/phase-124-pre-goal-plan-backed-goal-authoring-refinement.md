# P124 — Pre-goal Plan-backed Goal Authoring Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P124
> **Status:** Superseded predecessor draft / Not selected for release
> **Target Release:** v10.32 (historical predecessor draft)
> **Design References:**
> - [../design/design.md](../design/design.md) v10.32
> **Patch References:** [../patch/pre-goal-plan-backed-goal-authoring-refinement.patch.md](../patch/pre-goal-plan-backed-goal-authoring-refinement.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so advisory `/goal` creation for governed non-trivial or route-heavy work may conditionally run an internal pre-goal planning pass before final goal emission. That pass may use native subagent assistance for analysis, route drafting, verification ordering, and optional plan-file reference synthesis when separate context materially improves the route basis. `/goal` must remain the objective owner for outcome/done condition/proof/scope, `/plan` and any referenced plan file must remain route artifacts only, simple goals must still emit directly without forced pre-planning, helper output must remain subordinate input rather than completion proof, and closeout must still verify the goal gate rather than treating plan draft, plan file, or helper output as success by itself.

---

## Why This Phase Exists

The released `v10.31 / P123` baseline already allows conditional internal helper support inside selected governed `/goal` work and keeps `/goal` as the objective owner while `/plan` remains the route owner.

That boundary is still correct, but one design gap remains before the goal is emitted. When the user asks for a governed `/goal` command itself, the current model still tends to surface the command before enough route synthesis exists, then tries to bridge later into `/plan` or helper output. The user wants a different shape: for governed non-trivial or route-heavy work, route synthesis should happen first as internal planning support, then the emitted `/goal` should already reflect that route basis without making `/plan` or the plan file the objective owner.

P124 exists to refine the existing pattern rather than layering a new one on top: `/goal` should stay objective-owned, `/plan` should stay route-owned, plan files should stay route artifacts only, simple goals should stay direct, and internal planning help should remain conditional internal assistance that strengthens goal authoring without turning `/goal` into a mini-`/plan` or adding a new user-facing command.

---

## Expected Output

- `execution-and-goal-frame.md` encodes conditional internal pre-goal planning pass behavior before advisory `/goal` emission while still preserving `/goal` objective ownership and `/plan` route ownership
- `worker-routing-and-context.md` encodes bounded pre-goal helper lanes for analysis, route drafting, verification ordering, and optional plan-file reference synthesis with leader-owned normalization/proof boundaries
- `phase-todo-artifact.md` encodes governed execution-surface behavior for conditional plan-backed goal authoring, optional plan-file reference behavior, and direct simple-goal emission without replacing `/plan` as the route owner
- `explanation-and-presentation.md`, `accurate-communication.md`, and `communication-register.md` encode visible wording that keeps plan-backed goal authoring compact, keeps plan file/reference output subordinate to `/goal`, and avoids creating a new public pattern
- at least one related playground/reference case is updated so the pre-goal planning-pass behavior delta stays inspectable
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.32 / P124`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch verification, and GitHub release `v10.32` verification pass before final closeout wording claims release completion

---

## Action Checklist

- [ ] Confirm released baseline is `v10.31 / P123` with no active wave open before P124 startup.
- [ ] Open P124 phase and patch execution surfaces.
- [ ] Tighten goal-owned pre-goal planning-pass doctrine in `execution-and-goal-frame.md`.
- [ ] Tighten bounded pre-goal helper lane doctrine in `worker-routing-and-context.md`.
- [ ] Tighten governed `/goal` execution-surface doctrine in `phase-todo-artifact.md` so plan-backed goal authoring stays conditional, plan file stays reference-only, and `/plan` remains the route owner.
- [ ] Tighten presentation/register/wording owners so pre-goal planning pass, plan reference, and goal proof stay visibly distinct.
- [ ] Sync the directly affected design companions and owner changelog parents.
- [ ] Update one related playground/reference case and any directly required reference surface.
- [ ] Sync touched master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Update the remote default branch so the repo view reflects the released state.
- [ ] Create and verify GitHub release `v10.32`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- adding a new user-facing command or command flag for this behavior
- forcing the internal pre-goal planning pass for every `/goal` regardless of complexity
- making `/goal` a mini-`/plan` or replacing `/plan` as the route owner
- treating `/plan` or a plan file as the objective owner
- treating plan draft, plan file, or helper output as sufficient goal-completion proof by itself
- expanding the active runtime install set beyond 18 files
- adding `playground/` to runtime install payloads
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched owners preserve `/goal` as the objective owner while `/plan` and any plan file remain route artifacts only
- touched owners allow a conditional internal pre-goal planning pass for governed non-trivial or route-heavy work before final `/goal` emission
- touched owners keep simple goals on the direct `/goal` path without forced pre-planning
- touched owners keep helper lanes and plan-backed route synthesis as subordinate input rather than a new public owner pattern
- touched owners keep leader-owned normalization/proof wording and goal-gate closeout rather than plan-file or helper-output completion wording
- the updated playground/reference case shows the pre-goal planning-pass behavior delta clearly enough to inspect
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.32 / P124`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch verification, and GitHub release `v10.32` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P124 is now retained as a superseded predecessor draft.

Current checked status:
- released baseline before P124 startup remained `v10.31 / P123`
- the P124 direction established the move toward conditional pre-goal plan-backed goal authoring while still keeping `/goal` as the objective owner, `/plan` as the route owner, and plan file behavior reference-only
- the broader P125 integrated goal-with-planning objective now supersedes P124 as the active target model
- this file remains provenance for the design step between selected-goal helper support and the newer integrated one-surface model; it is not the active release target
