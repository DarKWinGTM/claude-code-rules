# P123 — Goal Internal Native Subagent Assistance Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P123
> **Status:** Active / In Progress
> **Target Release:** v10.31
> **Design References:**
> - [../design/design.md](../design/design.md) v10.31
> **Patch References:** [../patch/goal-internal-subagent-assistance-refinement.patch.md](../patch/goal-internal-subagent-assistance-refinement.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so `/goal` may conditionally use internal native subagent assistance for analysis, verification, testing, and bounded plan drafting when the selected governed goal remains non-trivial or route-heavy. `/goal` must remain the objective owner for outcome/done condition/proof/scope, `/plan` must remain the route owner for sequence/task breakdown/verification order, subagent help must remain internal helper behavior only, main-controller synthesis and proof wording must remain leader-owned, and closeout must continue to verify back against the goal gate rather than treating plan draft or worker output alone as success.

---

## Why This Phase Exists

The released `v10.30 / P122` baseline already hardened the objective-vs-route boundary and made `/plan` the explicit default next surface when a selected governed goal remains route-heavy.

That boundary is correct, but one practical workflow gap still remains. In some turns, the user wants `/goal` to stay the only visible command surface instead of adding another user-facing command or switching directly into `/plan`, while still getting stronger help with analysis, verification, testing, and bounded route drafting for non-trivial work.

P123 exists to refine the existing pattern rather than layering a new one on top: `/goal` should stay objective-owned, `/plan` should stay route-owned, and native subagent help should remain conditional internal assistance that strengthens goal execution without becoming a new public owner or a mini-`/plan` surface.

---

## Expected Output

- `execution-and-goal-frame.md` encodes that `/goal` may conditionally use internal native subagent assistance for analysis, verification, testing, and bounded plan drafting while still preserving `/goal` objective ownership and `/plan` route ownership
- `worker-routing-and-context.md` encodes the bounded internal-helper lane contract and leader-owned synthesis/proof boundary for goal-assisted subagent use
- `phase-todo-artifact.md` encodes governed execution-surface behavior for goal-assisted internal helper use without replacing `/plan` as the route owner
- `explanation-and-presentation.md`, `accurate-communication.md`, and `communication-register.md` encode visible wording that keeps internal helper use subordinate, keeps plan draft distinct from goal completion proof, and avoids creating a new public pattern
- at least one related playground/reference case is updated so the behavior delta stays inspectable
- touched master/design/changelog/TODO/phase/patch surfaces sync to `v10.31 / P123`
- runtime install boundary recheck, 18/18 parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.31` verification pass before final closeout wording claims release completion

---

## Action Checklist

- [x] Confirm released baseline is `v10.30 / P122` with no active wave open before P123 startup.
- [x] Open P123 phase and patch execution surfaces.
- [ ] Tighten goal-owned internal-helper doctrine in `execution-and-goal-frame.md`.
- [ ] Tighten bounded goal-assisted subagent lane doctrine in `worker-routing-and-context.md`.
- [ ] Tighten governed `/goal` execution-surface doctrine in `phase-todo-artifact.md` so internal helper use stays subordinate and `/plan` remains the route owner.
- [ ] Tighten presentation/register/wording owners so plan draft, worker help, and goal proof stay visibly distinct.
- [ ] Sync the directly affected design companions and owner changelog parents.
- [ ] Update one related playground/reference case and any directly required reference surface.
- [ ] Sync touched master surfaces in README, design, changelog, TODO, phase, and patch.
- [ ] Re-verify that `playground/` stays outside the 18-file runtime install payload.
- [ ] Install the active runtime rules into `~/.claude/rules` and verify 18/18 source/runtime parity plus source/destination body sufficiency.
- [ ] Run `git diff --check` clean.
- [ ] Commit the source release state and push the branch.
- [ ] Update the remote default branch so the repo view reflects the released state.
- [ ] Create and verify GitHub release `v10.31`.
- [ ] Finalize closeout records so runtime/design/changelog/TODO/phase/patch status agree.

---

## Out of Scope

- adding a new user-facing command or command flag for this behavior
- making `/goal` a mini-`/plan` or replacing `/plan` as the route owner
- treating subagent help as a new public owner or visible route surface
- forcing subagent spawn for every goal regardless of complexity
- treating plan draft or worker output as sufficient goal-completion proof by itself
- expanding the active runtime install set beyond 18 files
- adding `playground/` to runtime install payloads
- unrelated plugin/runtime work outside this repo

---

## Completion Gate

- touched owners preserve `/goal` as the objective owner and `/plan` as the route owner
- touched owners allow conditional internal native subagent assistance for analysis, verification, testing, and bounded plan drafting when selected governed goals remain non-trivial or route-heavy
- touched owners keep subagent help as internal helper behavior only rather than a new public owner pattern
- touched owners keep leader-owned synthesis/proof wording and goal-gate closeout rather than worker-output completion wording
- the updated playground/reference case shows the goal-assisted internal-helper behavior delta clearly enough to inspect
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.31 / P123`
- `playground/` remains outside the active runtime install payload and the active runtime count remains 18
- runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and `git diff --check` pass
- branch push, remote default-branch update, and GitHub release `v10.31` verification pass
- closeout records agree across runtime/design/changelog/TODO/phase/patch

---

## Current Status

P123 is active.

Current checked progress:
- released baseline before P123 startup is `v10.30 / P122`
- the selected improvement direction is to keep `/goal` as the only visible objective surface while allowing conditional internal native subagent assistance for analysis, verification, testing, and bounded plan drafting when route complexity remains material
- P123 phase/patch startup artifacts and active master execution surfaces are now opened
- touched runtime owner refinement, companion/changelog sync, reference-case update, runtime install verification, release verification, and final closeout alignment still remain