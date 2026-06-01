# P130 — Always-on Plan-file-backed Goal Model

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P130
> **Status:** Completed / Released
> **Target Release:** v10.38
> **Design References:**
> - [../design/design.md](../design/design.md) v10.35
> **Patch References:** [../patch/always-on-plan-file-backed-goal-model.patch.md](../patch/always-on-plan-file-backed-goal-model.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Refine RULES so actual governed `/goal` creation becomes plan-first and goal-second by default. The assistant should prepare a full detailed plan file as route-only support before final goal emission, then emit a compact `/goal` that references that plan file. `/goal` must remain the objective owner for outcome, proof/checks, scope, and hard guardrails; the plan file must remain subordinate route detail rather than objective authority or completion proof.

---

## Why This Phase Exists

The released P125 model already integrated planning support into the goal-centric surface, but it still kept planning conditional and left room for simple/direct goals to bypass plan-file preparation. The user now wants a stricter model: once assistant actually creates or promotes a `/goal`, the route should already exist as a full plan file, and the emitted `/goal` should reference that file instead of trying to carry full route detail itself.

P130 exists to harden that model without breaking the objective/route split. `/goal` should remain the visible objective contract, the plan file should remain route-only support, `/plan` should remain a route tool rather than the ordinary paired next surface, and goal-gate closeout should remain stronger than plan-step completion.

---

## Expected Output

- `execution-and-goal-frame.md` teaches that any actual governed `/goal` creation prepares a full detailed plan file before final goal emission
- `phase-todo-artifact.md` teaches governed `/goal` sourcing as plan-first authoring with a mandatory plan-file reference in the emitted goal
- `explanation-and-presentation.md` teaches that `Plan reference` is the normal route-context companion for promoted or selected governed `/goal` output
- touched design companions and owner changelog parents are synced to the new doctrine
- touched README/changelog/TODO/phase/patch surfaces align to `v10.38 / P130`
- runtime install/update verification, source/runtime parity, source/destination body sufficiency, `git diff --check`, push/update, and release verification all pass before closeout claims release completion

---

## Action Checklist

- [x] Open P130 phase and patch execution surfaces on top of the released `v10.37 / P129` baseline.
- [x] Tighten `execution-and-goal-frame.md` so governed `/goal` creation is always plan-first and emitted goals always reference the prepared plan file.
- [x] Tighten `phase-todo-artifact.md` so governed `/goal` sourcing and selected-goal execution surfaces normalize the referenced plan file as the default route artifact.
- [x] Tighten `explanation-and-presentation.md` so plan-backed governed `/goal` output presents `Plan reference` as the normal compact route-context companion.
- [x] Sync the directly affected design companions and owner changelog parents.
- [x] Sync touched master surfaces in README, changelog, TODO, phase, and patch.
- [x] Re-verify that the active runtime install scope remains 18 root runtime rules only.
- [x] Run RULES install/update verification, source/runtime parity, source/destination body sufficiency, and `git diff --check`.
- [x] Commit the release state, push the update, verify remote `master`, and publish GitHub release `v10.38`.
- [x] Finalize closeout records so runtime/design/changelog/TODO/phase/patch agree.

---

## Out of Scope

- making the plan file objective authority or completion proof
- turning `/plan` into the ordinary public next surface for every selected goal
- forcing `/goal` onto trivial non-governed next steps or unselected future work
- expanding the active runtime install set beyond 18 files
- unrelated rule waves, plugin work, or non-RULES repo changes

---

## Completion Gate

- touched owners require plan-first authoring for any actual governed `/goal` creation
- touched owners require the emitted `/goal` to reference a prepared full detailed plan file as route-only support
- touched owners preserve `/goal` as the objective owner and keep the referenced plan file subordinate to the goal
- touched owners preserve `/plan` as explicit standalone route handling, later route revision, or overflow only rather than the ordinary paired next surface
- touched owners preserve goal-gate closeout as stronger than plan-step completion
- touched master/design/changelog/TODO/phase/patch surfaces align to `v10.38 / P130`
- active runtime install scope remains 18 root rules only
- runtime install/update verification, source/runtime parity, source/destination body sufficiency, `git diff --check`, remote `master` verification, and GitHub release verification all pass

---

## Current Status

P130 is completed.

Current checked progress:
- released baseline before P130 startup was `v10.37 / P129`
- selected improvement direction now ships always-on plan-file-backed `/goal` authoring for actual governed goal creation
- touched runtime owners, design companions, and owner changelog parents are updated in source scope
- touched README/changelog/TODO/phase/patch surfaces are aligned to `v10.38 / P130`
- runtime install/update verification passed with 18 active source/runtime rule files plus manifest
- targeted parity and source/destination body sufficiency passed for the touched active runtime owners
- `git diff --check`, push/update to remote `master`, GitHub release verification, and final closeout alignment all passed
