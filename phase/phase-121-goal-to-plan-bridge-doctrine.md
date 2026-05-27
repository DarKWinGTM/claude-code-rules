# P121 — Goal-to-Plan Bridge Doctrine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P121
> **Status:** Active / In Progress
> **Target Release:** v10.29
> **Design References:**
> - [../design/design.md](../design/design.md) v10.29
> **Patch References:** [../patch/goal-to-plan-bridge-doctrine.patch.md](../patch/goal-to-plan-bridge-doctrine.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so `/goal` explicitly owns the objective layer while `/plan` explicitly owns the route layer: `/goal` should lock outcome, done condition, proof, and scope; `/plan` should lock sequence, approach, and task breakdown; non-trivial governed goals should bridge into `/plan` without turning `/plan` into a mandatory requirement for every goal; and closeout should verify back against the goal gate rather than treating plan completion by itself as success.

---

## Why This Phase Exists

The released `v10.28 / P120` baseline already teaches stronger successor surfacing, language alignment, and strategy-before-patch correction posture, but it still does not make the `/goal` ↔ `/plan` relationship explicit enough.

The remaining gap is structural. Without a clearer doctrine, AI can drift into two opposite errors:
- overloading `/goal` so it behaves like a mini-plan instead of an objective contract
- over-trusting `/plan` completion as if it automatically proves the goal is complete

P121 exists to harden that boundary while preserving the governed-work-only `/goal` doctrine, direct continuation priority, candidate-goal shaping, and the non-trivial-only bridge into `/plan`.

---

## Expected Output

- `execution-and-goal-frame.md` encodes a goal-to-plan bridge where `/goal` owns objective and `/plan` owns route
- `phase-todo-artifact.md` encodes when a governed non-trivial goal should bridge into `/plan` and how governed execution surfaces should supply that bridge
- `explanation-and-presentation.md`, `communication-register.md`, and `accurate-communication.md` encode user-visible wording that keeps goal/objective meaning distinct from plan/route meaning and returns closeout to the goal gate
- at least one related playground case is updated so the behavior delta stays inspectable
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.29 / P121`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.29` verification pass before final closeout wording claims release completion

---

## Action Checklist

- [x] Confirm released baseline is `v10.28 / P120` with no active wave open before P121 startup.
- [x] Open P121 phase and patch execution surfaces.
- [x] Tighten objective-vs-route doctrine in `execution-and-goal-frame.md`.
- [x] Tighten governed `/goal` → `/plan` bridge sourcing and non-trivial trigger guidance in `phase-todo-artifact.md`.
- [x] Tighten presentation/register/wording owners so `/goal` stays objective-shaped, `/plan` stays route-shaped, and closeout returns to the goal gate.
- [x] Sync the directly affected design companions and owner changelog parents.
- [x] Update one related playground case and any directly required reference surface.
- [x] Sync touched master surfaces in README, design, changelog, TODO, phase, and patch.
- [x] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [x] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [x] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Update the remote default branch so the repo view reflects the released state.
- [ ] Create and verify GitHub release `v10.29`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- making `/plan` mandatory for every `/goal`
- turning `/goal` into a mini task list or route document
- changing candidate-goal doctrine into automatic `/plan` creation for all successor recommendations
- weakening governed-surface sourcing, direct continuation priority, language alignment, or strategy-before-patch doctrine
- expanding the active runtime install set beyond 18 files
- adding `playground/` to runtime install payloads
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched owners clearly distinguish objective ownership from route ownership
- the bridge into `/plan` is limited to non-trivial governed goals rather than all goals by default
- closeout wording and execution doctrine verify back against the goal gate instead of plan completion alone
- the updated playground case shows the goal/objective vs plan/route behavior delta clearly enough to inspect
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.29 / P121`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.29` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P121 is active.

Current checked progress:
- released baseline before P121 startup is `v10.28 / P120`
- the selected improvement direction is a bounded goal-to-plan bridge that preserves `/goal` as the objective contract and `/plan` as the execution route
- touched runtime owners, design companions, owner changelog parents, one related playground case, and touched master surfaces are updated in source scope
- runtime install into `~/.claude/rules`, 18/18 source/runtime parity, source/destination body sufficiency, `playground/` runtime exclusion recheck, and `git diff --check` have already passed
- commit/push/default-branch update, GitHub release verification, and final closeout alignment still remain
