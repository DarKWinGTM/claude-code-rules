# Governed Goal Routing-Choice Surface Hardening Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.24
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P141 wave.

It packages one bounded doctrine refinement: governed `/goal` or route-only plan-support authoring should end at the emitted goal artifact plus subordinate route support when execution was not yet selected, instead of leaking a follow-up execution-mode menu.

---

## Analysis

Before this wave:
- plain governed goal requests already triggered planning-depth resolution
- durable route-only plan support already had the plan-file-first and in-artifact `Plan reference:` protections
- selected goal/plan execution already suppressed default user-facing routing menus in the execution-ready posture

The remaining gap was the authoring stop boundary:
- a goal/plan-file authoring turn could still finish the authoring work and then append a `Which approach?` menu
- that menu exposed internal routing labels even when the user had not selected execution yet
- the leak made authoring and execution transition read like one stage when they should remain distinct

The better posture is:
- keep `/goal` as the objective surface
- keep route support subordinate to that goal
- stop cleanly at the authoring surface when the turn is still only goal/plan-file authoring
- preserve internal execution-posture choice for the later execution transition only

---

## Change Items

### 1) Goal-authoring boundary hardening

- **Target artifacts:** `execution-and-goal-frame.md`, `design/execution-and-goal-frame.design.md`, `changelog/execution-and-goal-frame.changelog.md`
- **Change type:** active doctrine refinement
- **Current state:** goal authoring and execution transition can still blur together after a bounded governed goal artifact is emitted.
- **Target state:** goal/plan-file authoring now has an explicit stop boundary; execution-posture selection remains a later internal transition.
- **Review point:** bounded authoring turns no longer auto-spill into a `Subagent-Driven` / `Inline Execution` menu.

### 2) Execution-surface gating refinement

- **Target artifacts:** `phase-todo-artifact.md`, `design/phase-todo-artifact.design.md`, `changelog/phase-todo-artifact.changelog.md`
- **Change type:** active doctrine refinement
- **Current state:** task materialization and execution-mode suppression already exist, but the transition from goal authoring into live execution is not explicit enough.
- **Target state:** authoring-only turns stop at the goal-centric surface; task materialization waits until execution is actually selected or clearly implied.
- **Review point:** authoring support does not prematurely become execution-mode UI.

### 3) Wording/register/presentation alignment

- **Target artifacts:** `accurate-communication.md`, `design/accurate-communication.design.md`, `changelog/accurate-communication.changelog.md`, `communication-register.md`, `design/communication-register.design.md`, `changelog/communication-register.changelog.md`, `explanation-and-presentation.md`, `design/explanation-and-presentation.design.md`, `changelog/explanation-and-presentation.changelog.md`
- **Change type:** active doctrine refinement
- **Current state:** wording already suppresses internal labels in execution-ready contexts, but authoring-only turns can still drift into execution-choice language.
- **Target state:** user-facing wording now reports the emitted goal plus route support and stops there unless a real decision boundary remains.
- **Review point:** internal routing labels stay hidden by default outside governance/exact-artifact contexts.

### 4) Current-state and release-surface sync

- **Target artifacts:** `TODO.md`, `phase/SUMMARY.md`, `phase/phase-141-governed-goal-routing-choice-surface-hardening.md`, `patch/governed-goal-routing-choice-surface-hardening.patch.md`, `changelog/changelog.md`, and `changelog/changelog/v10.49-released-governed-goal-routing-choice-surface-hardening.changelog.md`
- **Change type:** execution/release synchronization
- **Current state:** the latest released baseline is still `v10.48 / P140`; P141 exists only as the selected goal and route plan.
- **Target state:** current-state and release-history surfaces align to one promoted `v10.49 / P141` baseline after verification/publish closeout.
- **Review point:** release wording must follow actual verification and publish evidence rather than anticipatory success wording.

---

## Verification

Required checks before release closeout:
- governed goal/plan-file authoring now stops at the emitted goal artifact plus subordinate route support when execution was not yet selected
- default user-facing `Subagent-Driven` / `Inline Execution` authoring leakage is gone
- execution-posture selection remains internal for actual execution-ready work
- touched design/changelog/TODO/phase/patch/master-changelog/detail surfaces align to `v10.49 / P141`
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check` passes
- the selected scope is pushed to `master`, tagged, and GitHub release verification passes

---

## Rollback Approach

If the P141 wording/mechanism split proves too aggressive, roll back only the goal-authoring stop-boundary clauses and companion sync for this wave while preserving the already-released P139/P140 architecture: plain goal requests still get smallest-sufficient route support, plan files remain route-only, and selected execution posture remains internally chosen.

---

## Implementation Status

P141 is completed.

The touched runtime owners now carry the authoring stop-boundary refinement, companion design/changelog/TODO/phase/patch/master-changelog/detail surfaces are aligned to `v10.49 / P141`, touched runtime install/update parity is aligned, `git diff --check` passed, and push to `master`, tag `v10.49`, and GitHub release verification passed. Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.49
