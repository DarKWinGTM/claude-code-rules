# Always-on Plan-file-backed Goal Model Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.35
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P130 wave.

It packages one bounded doctrine refinement so governed `/goal` creation becomes plan-first and goal-second by default: prepare a full detailed plan file first, then emit a compact `/goal` that references that plan file while keeping `/goal` as the objective owner and keeping the plan file as route-only support.

---

## Analysis

The released P125 model already integrated planning into the goal-centric surface and demoted `/plan` from the ordinary paired next surface. That was the right direction, but it still left planning conditional and still allowed the route artifact to appear only when route-heavy complexity or overflow made it useful.

The user wants a stricter posture:
- if assistant actually creates or promotes a `/goal`, the route should already exist as a full plan file
- the emitted `/goal` should stay compact and objective-owned
- the emitted `/goal` should reference the prepared plan file as route-only support
- `/plan` should remain available only for explicit standalone planning, later route revision, or overflow beyond an already plan-backed selected goal
- completing plan steps must not substitute for the selected goal gate

This update stays bounded. It does not make the plan file objective authority, does not turn `/goal` into a mini-spec dump, does not require `/goal` for trivial non-governed next steps, does not weaken transcript-visible proof discipline, and does not expand the runtime install set.

---

## Change Items

### 1) Plan-first goal-authoring refinement

- **Target artifact:** touched execution owner governing advisory `/goal` construction, goal creation, and selected-goal route handling
- **Change type:** refinement
- **Current state:** governed `/goal` authoring may conditionally use internal planning and may optionally reference a plan file when route support is useful
- **Target state:** any actual governed `/goal` creation prepares a full detailed plan file first, then emits a compact `/goal` that references that plan file as route-only support
- **Review point:** preserve `/goal` objective ownership and do not let the plan file become the new objective surface

### 2) Governed execution-surface refinement

- **Target artifact:** touched phase/TODO execution owner governing `/goal` sourcing and selected-goal route handling
- **Change type:** refinement
- **Current state:** governed execution surfaces still teach conditional pre-goal planning and still keep room for direct/simple goal emission without mandatory plan-file preparation
- **Target state:** governed execution surfaces normalize plan-first authoring for any actual `/goal` creation and treat the referenced plan file as the default selected-goal route artifact
- **Review point:** preserve direct continuation for non-goal next steps and keep `/plan` out of the ordinary next-surface role

### 3) Visible route-context refinement

- **Target artifact:** touched presentation owner governing advisory `/goal` output shapes
- **Change type:** refinement
- **Current state:** visible output may show `Plan reference` as optional route context when planning shaped the goal
- **Target state:** promoted or selected governed `/goal` output uses `Plan reference` as the normal compact route-context companion, while full detail stays in the referenced plan file
- **Review point:** keep the visible goal compact and avoid turning it into a mini-spec dump

### 4) Release-surface sync

- **Target artifact:** touched README/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces still identify `v10.37 / P129` as the latest released baseline
- **Target state:** touched master surfaces open and later close `v10.38 / P130` consistently and record the plan-first plan-reference-backed goal model
- **Review point:** keep release wording evidence-calibrated and tied to actual install/update/push/release proof

---

## Verification

Required checks before release closeout:
- touched owners require plan-first authoring for any actual governed `/goal` creation
- touched owners require a referenced full detailed plan file as route-only support for emitted governed goals
- touched owners preserve `/goal` as objective owner and keep the plan file subordinate to the goal
- touched owners preserve `/plan` as explicit standalone planning, later route revision, or overflow only
- touched owners preserve goal-gate closeout as stronger than plan-step completion
- touched release/master surfaces align to `v10.38 / P130`
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install/update verification copies only the source-owned active root runtime rules and parity/body-sufficiency checks pass
- `git diff --check` passes
- remote `master` shows the promoted source state after push/update
- GitHub release `v10.38` is created and verified before closeout wording claims release completion

---

## Implementation Status

P130 is completed.

The checked direction was established, the bounded improvement target was selected, and phase/patch execution surfaces were opened and closed. Touched runtime-owner refinement, companion/changelog sync, release-surface sync, install/update verification, parity/body-sufficiency verification, `git diff --check`, push/update, release verification, and final closeout alignment all completed.
