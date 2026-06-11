# Hybrid Progress Reporting Surface Alignment Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** In Progress
> **Target Design:** [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md) v1.20
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P143 wave.

It packages one bounded repository-behavior refinement: non-trivial Claude progress updates should become easier to scan and easier to trust by using one compact hybrid snapshot shape, while still preserving evidence-strength wording, continuation-first execution, and the existing route-only `/goal` authoring boundary.

---

## Analysis

Before this wave:
- several runtime owners already described evidence-calibrated status wording, compact snapshots, continuation-first execution, phase-backed closeout, and goal-authoring stop boundaries
- but the rules did not yet define one compact shared in-flight progress shape that ties those pieces together
- as a result, active updates could still be technically correct but uneven to scan: the reader had to infer what was done, what was happening now, what remained, and what came next

The better posture is:
- keep the existing evidence and continuation doctrine
- add one bounded hybrid snapshot for non-trivial in-flight updates
- keep `Done so far` visibly bounded to checked scope
- keep progress narration from turning into a stop reason or milestone-only ceremony
- preserve the P141 rule that route-only governed `/goal` authoring ends at the goal artifact plus subordinate route support

---

## Change Items

### 1) Runtime-owner hybrid progress snapshot additions

- **Target artifacts:** `accurate-communication.md`, `explanation-and-presentation.md`, `communication-register.md`, `execution-and-goal-frame.md`, `phase-todo-artifact.md`
- **Change type:** bounded runtime doctrine refinement
- **Current state:** the owners already contain the ingredients for honest progress reporting, but not one shared compact shape.
- **Target state:** the owners explicitly support `Current` / `Done so far` / `In progress` / `Remaining` / `Blockers / Notes` / `Next` as a compact progress snapshot for non-trivial in-flight work, while keeping evidence strength and continuation discipline intact.
- **Review point:** the new shape must improve scanability without becoming mandatory ceremony for trivial replies.

### 2) Design and per-chain changelog companion sync

- **Target artifacts:** the design and per-chain changelog companions for each touched runtime owner
- **Change type:** owner-companion synchronization
- **Current state:** the companion surfaces do not yet describe the hybrid progress-reporting refinement.
- **Target state:** each touched owner design and per-chain changelog records the new refinement and its bounded intent.
- **Review point:** companion sync should describe the refinement clearly without overstating release or runtime-install state.

### 3) Active execution-surface sync

- **Target artifacts:** `TODO.md`, `phase/SUMMARY.md`, `phase/phase-143-hybrid-progress-reporting-surface-alignment.md`, and this patch file
- **Change type:** active phase/TODO synchronization
- **Current state:** latest released baseline is `v10.50 / P142`, no active wave is selected in the clean worktree, and the new refinement exists only as a selected goal plus route plan.
- **Target state:** active execution surfaces show `P143 / v10.51` as the bounded in-progress wave, explain why it is a new major phase, and keep release scope separate until release-level verification is actually selected and complete.
- **Review point:** active surfaces must not claim release, tag, or publish alignment before those checks actually happen.

### 4) Optional release-scope synchronization

- **Target artifacts:** `changelog/changelog.md` and a `changelog/changelog/v10.51-*.changelog.md` detail shard if the wave is promoted through release closeout
- **Change type:** release-history synchronization
- **Current state:** latest released baseline in checked clean scope is `v10.50 / P142`.
- **Target state:** master release-history surfaces advance only if the wave is actually carried through release-level verification and closeout.
- **Review point:** release-history wording must match the real evidence held; no `released` claim from edit-only progress.

---

## Verification

Required checks before strong closeout wording:
- the touched runtime owners all expose a consistent hybrid progress-reporting shape in checked scope
- `Done so far` is bounded to checked scope and does not read like total completion
- progress narration does not become a stop gate or milestone-only pause when safe continuation exists
- route-only `/goal` authoring still ends at the goal artifact plus subordinate route support without leaking a default execution-mode menu
- design/per-chain changelog companions align to the touched runtime owners
- TODO/phase/patch surfaces align to the active `P143 / v10.51` execution state
- `git diff --check` passes
- runtime install/update parity plus body sufficiency pass if runtime install verification is selected
- master changelog, release shard, tag, and publish evidence are updated only if release scope is actually selected and verified

---

## Rollback Approach

If the hybrid snapshot proves too heavy, keep the evidence-strength and continuation doctrine, then reduce only the visible marker set or where it is triggered; do not roll back by restoring narrative-only progress updates that hide checked scope or by reopening default execution-mode menus after route-only goal authoring.

---

## Implementation Status

P143 is in progress.

The selected runtime-owner doctrine updates plus their design/per-chain changelog companions are already in place in checked clean-worktree scope. Active TODO/phase/patch synchronization and any optional release-scope closeout remain pending.
