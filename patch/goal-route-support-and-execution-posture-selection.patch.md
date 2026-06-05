# Goal Route Support and Execution Posture Selection Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.22
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P139 wave.

It packages one bounded doctrine refinement: plain goal requests should receive the smallest sufficient route support automatically when needed, and selected goal/plan execution should choose posture internally from checked context instead of exposing a default user-facing routing choice menu.

---

## Analysis

Before this wave:
- governed `/goal` support already existed, but plain goal requests still leaned too heavily on explicit `goal plan file` phrasing
- selected non-trivial goal/plan execution already preferred Subagent-Driven first, but user-facing wording still left routing-label leakage and menu-like behavior loopholes
- `Plan reference:` ordering and route-only semantics already existed, but the durable plan-file pointer still needed stricter exact-label and existing-file truth alignment across wording owners

The better posture is:
- treat plain goal requests as objective requests that can trigger planning-depth resolution automatically
- choose the smallest sufficient route support instead of forcing either bare `/goal` or durable plan files for every case
- keep `/goal` as objective authority and any plan file as route-only support
- keep execution posture internal by default, with Subagent-Driven first when worker-suitable and Inline only as a checked fallback
- expose chosen action/result to the user instead of a routing-label choice menu

---

## Change Items

### 1) Goal/plan owner hardening

- **Target artifacts:** `execution-and-goal-frame.md`, `phase-todo-artifact.md`
- **Change type:** released doctrine refinement
- **Current state:** goal authoring and selected execution already had plan-backed and Subagent-Driven-first behavior, but plain `goal` requests and internal routing-label leakage were not fully resolved.
- **Target state:** plain goal requests now trigger planning-depth resolution, durable route-only plan files appear only when justified, and selected execution no longer emits a default routing-label choice menu.
- **Review point:** `/goal` remains the objective owner while plan files stay route-only support.

### 2) Routing and wording hardening

- **Target artifacts:** `worker-routing-and-context.md`, `communication-register.md`, `accurate-communication.md`, `explanation-and-presentation.md`
- **Change type:** released doctrine refinement
- **Current state:** routing labels and `goal plan file` phrasing could still leak into user-facing wording.
- **Target state:** internal routing labels are kept internal by default, plain goal requests receive ordinary route-support language, and exact `Plan reference:` is reserved for the durable route-only plan-file pointer only.
- **Review point:** exact labels remain available only for workflow/governance discussion or exact copied artifact wording.

### 3) Companion and release-surface sync

- **Target artifacts:** touched design companions, per-chain changelogs, `README.md`, `TODO.md`, `phase/SUMMARY.md`, `phase/phase-139-goal-route-support-and-execution-posture-selection.md`, `patch/goal-route-support-and-execution-posture-selection.patch.md`, `changelog/changelog.md`, and `changelog/changelog/v10.47-released-goal-route-support-and-execution-posture-selection.changelog.md`
- **Change type:** release synchronization
- **Current state:** released baseline was `v10.46 / P138`, while P139 existed only as a selected goal and route plan.
- **Target state:** current-state and history surfaces now align to one promoted `v10.47 / P139` baseline.
- **Review point:** release wording matches actual install/parity/branch/tag/release evidence.

---

## Verification

Required checks before release closeout:
- plain goal requests now resolve planning depth automatically when route pressure or governed complexity requires support
- users do not need `goal plan file` phrasing to receive proper governed route support
- durable `Plan reference:` only points to a route-only plan file that already exists in checked scope or was successfully written in the same governed authoring flow
- selected goal/plan execution no longer emits a default user-facing `Subagent-Driven` / `Inline Execution` choice menu
- touched design/changelog/README/TODO/phase/patch/master-changelog/detail surfaces align to `v10.47 / P139`
- touched runtime owners are installed/updated and verified for source/runtime parity + body sufficiency
- `git diff --check` passes
- the selected scope is committed, pushed to `master`, tagged, and GitHub release verification passes

---

## Implementation Status

P139 is completed.

The touched doctrine owners now auto-resolve plain goal route support when needed, keep selected execution posture internal by default, align exact `Plan reference:` semantics to real durable plan-file truth, synchronize the touched owner-chain and release surfaces to `v10.47 / P139`, and publish the bounded wave with install/parity/push/tag/release verification.
