# P125 — Integrated Goal-with-Planning Objective

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P125
> **Status:** Completed / Released
> **Target Release:** v10.33
> **Design References:**
> - [../design/design.md](../design/design.md) v10.33
> **Patch References:** [../patch/integrated-goal-planning-objective.patch.md](../patch/integrated-goal-planning-objective.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so `/goal` and planning work as one integrated surface for governed non-trivial or route-heavy requests. When route uncertainty would otherwise make the emitted goal vague, assistant should automatically run an internal planning / plan-mode-style pass before final goal emission. The visible output must still stay one goal-centric surface, `/goal` must remain the objective owner for outcome/done condition/proof/scope, planning support must remain subordinate route context inside or adjacent to that goal surface, and `/plan` plus any plan file must remain overflow or explicitly requested route artifacts only rather than normal paired output.

---

## Why This Phase Exists

The unreleased P124 predecessor already moved RULES from selected-goal helper support toward pre-goal plan-backed goal authoring. That was a meaningful improvement, but it still framed planning as a distinct stage that can read like a neighboring surface beside `/goal`. The user wants a tighter model: goal and planning should cooperate as one continuous behavior, not as two sideways outputs where assistant offers one `/goal` block and one `/plan` block.

P125 exists to normalize that target shape. `/goal` should still be the visible contract, internal planning should still happen only when necessary, simple goals should still emit directly, helper output should still stay subordinate and never count as completion proof, and `/plan` should still exist only when route detail no longer fits the integrated goal-centric surface or the user explicitly asks for standalone planning.

---

## Expected Output

- `execution-and-goal-frame.md` no longer treats `/plan` as the ordinary paired next surface for route-heavy goal requests; instead it treats integrated planning support as part of the goal-centric emission flow and keeps `/plan` for overflow or explicit standalone planning only
- `phase-todo-artifact.md` sources governed `/goal` output from execution surfaces with automatic-when-necessary internal planning support and without sideways `/goal` + `/plan` output
- `explanation-and-presentation.md` teaches one visible goal-centric output block with subordinate route context instead of sibling goal/plan blocks
- `communication-register.md` teaches wording that makes `/plan` read as overflow route handling only, not as a second equal recommendation surface
- `worker-routing-and-context.md` treats subagent help as integrated goal-authoring support rather than as a separate planning stage competing with the goal surface
- at least one related playground/reference case shows candidate goals leading into one advisory `/goal` with integrated route support and no separate `/plan` block unless overflow route detail is genuinely needed
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.33 / P125`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch verification, and GitHub release `v10.33` verification pass before final closeout wording claims release completion

---

## Action Checklist

- [x] Open P125 phase and patch execution surfaces while preserving P123 as the latest released baseline.
- [x] Mark P124 as an unreleased predecessor draft superseded by the broader P125 target model.
- [x] Tighten integrated goal-with-planning doctrine in `execution-and-goal-frame.md`.
- [x] Tighten governed `/goal` execution-surface doctrine in `phase-todo-artifact.md` so automatic planning support remains inside the goal-centric surface.
- [x] Tighten presentation/register owners so visible output no longer reads like `/goal` and `/plan` are two sideways branches.
- [x] Tighten worker-routing doctrine so helper/subagent lanes support integrated goal authoring and not a competing planning surface.
- [x] Sync the directly affected design companions and owner changelog parents.
- [x] Update one related playground/reference case and any directly required reference surface.
- [x] Sync touched master surfaces in README, design, changelog, TODO, phase, and patch.
- [x] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [x] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [x] Run `git diff --check` clean.
- [x] Commit the source release state and push the branch.
- [x] Update the remote default branch so the repo view reflects the released state.
- [x] Create and verify GitHub release `v10.33`.
- [x] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- adding a new user-facing command or command flag for this behavior
- forcing internal planning for every `/goal` regardless of complexity
- emitting `/goal` and `/plan` as equal-level paired surfaces in normal operator output
- making `/goal` a mini-`/plan` or replacing `/plan` as the route owner everywhere
- treating `/plan` or a plan file as the objective owner
- treating plan draft, plan reference, plan file, or helper output as sufficient goal-completion proof by itself
- expanding the active runtime install set beyond 18 files
- adding `playground/` to runtime install payloads
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched owners preserve `/goal` as the objective owner while integrated planning support stays subordinate route context inside or adjacent to the goal-centric surface
- touched owners allow automatic internal planning / plan-mode-style support only when governed non-trivial or route-heavy requests truly need it
- touched owners keep simple goals on the direct `/goal` path without forced planning
- touched owners no longer teach `/plan` as the ordinary paired next-step surface for route-heavy goal requests
- touched owners preserve `/plan` and plan files as overflow or explicitly requested route artifacts only
- touched owners keep helper lanes and integrated planning support as subordinate input rather than a new public owner pattern
- the updated playground/reference case shows one integrated goal-with-planning surface rather than two sideways branches
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.33 / P125`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch verification, and GitHub release `v10.33` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P125 is completed.

Current checked progress:
- released baseline before P125 startup was `v10.31 / P123`
- the selected improvement direction now ships one integrated goal-with-planning visible surface for governed non-trivial or route-heavy work while keeping `/goal` as the objective owner and `/plan` as overflow or explicitly requested standalone route handling only
- touched runtime owners, design companions, owner changelog parents, one related playground/reference case, and touched master surfaces are updated in source scope
- runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `playground/` runtime exclusion recheck, and `git diff --check` all passed
- branch push, remote default-branch verification, GitHub release `v10.33` verification, and final closeout alignment all passed
