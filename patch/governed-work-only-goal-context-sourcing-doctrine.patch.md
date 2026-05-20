# Governed-Work-Only Goal Context Sourcing Doctrine Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** In progress
> **Target Design:** [design/design.md](../design/design.md) v10.21
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.21 / P113`.

It packages a doctrine refinement so advisory `/goal` behavior stays concise for trivial non-governed successor work, but becomes design-first and governed-surface-sourced when bounded repo-governed successor work needs explicit execution context to define done correctly.

---

## Analysis

The released `v10.20 / P112` baseline still carries the earlier P107 `/goal` doctrine.

That baseline already separates direct continuation from some advisory `/goal` cases, but it does not yet make one operational distinction explicit enough: when a successor objective is governed enough that design truth, active execution state, release/current-state truth, or before/after review boundaries should shape the command.

The first issue is trigger ambiguity: a bounded successor objective is not always a governed-work successor objective.

The second issue is sourcing ambiguity: governed repo work should not improvise `/goal` from generic next-step prose when design, phase, TODO, task, changelog, patch, or README materially shape what done means.

The third issue is output-shape ambiguity: even when governed context is needed, `/goal` should still stay compact and high-signal instead of becoming a long template dump.

---

## Change Items

### 1) Governed-work-only `/goal` trigger doctrine

- **Target artifact:** `execution-and-goal-frame.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** RULES allows bounded, transcript-provable `/goal` suggestions, but it does not yet require the successor objective to be repo-governed before governed-surface context is pulled in.
- **Target state:** RULES explicitly limits heavy governed `/goal` construction to bounded governed-work successor objectives and keeps trivial non-governed next steps light.
- **Review point:** preserve continuation-first behavior when safe direct continuation already exists.

### 2) Design-first governed `/goal` sourcing order

- **Target artifact:** `phase-todo-artifact.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** RULES translates Goal/Output/Gate/Verification into `/goal`, but it does not yet make the design-first sourcing order and material-only changelog/patch/README inclusion explicit enough.
- **Target state:** RULES explicitly sources governed `/goal` from design first, then active execution surfaces, and includes changelog/patch/README only when they materially shape completion, review, or current-state impact.
- **Review point:** preserve existing durable tracking and phase/TODO/task execution-surface boundaries.

### 3) Compact governed output-shape doctrine

- **Target artifact:** `explanation-and-presentation.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** RULES already keeps `/goal` compact, but it does not yet explicitly say trivial non-governed next steps should stay ordinary next-step wording or a very light command.
- **Target state:** RULES keeps governed `/goal` compact by default and prevents heavy governed-surface framing from leaking into small non-governed successor work.
- **Review point:** preserve advisory output and avoid mini-spec dumps.

### 4) Example outputs and master-surface sync

- **Target artifact:** README/design/changelog/TODO/phase/patch release surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces still identify `v10.20 / P112` as the released baseline with no active P113 wave open.
- **Target state:** master surfaces open and later close P113 consistently, while preserving two concrete `/goal` outputs for review.
- **Review point:** keep the active runtime install scope at 18 and stay inside repo scope only.

---

## Example `/goal` Outputs

### Example 1 — governed non-release successor work

```text
/goal Done when the governed-work-only `/goal` doctrine is implemented in the mapped owner files and the touched design/changelog companions are synced. Prove with: show diffs for `execution-and-goal-frame.md`, `phase-todo-artifact.md`, `explanation-and-presentation.md`, their touched design/changelog companions, and run `git diff --check` clean. Scope: `/home/node/workplace/AWCLOUD/TEMPLATE/RULES` only. Keep: preserve advisory `/goal` behavior, keep trivial non-governed next steps concise, and do not expand the active runtime install set beyond 18.
```

### Example 2 — governed release-closeout successor work

```text
/goal Done when `v10.21 / P113` is installed, verified, pushed, released, and closed out across the governed master surfaces. Prove with: install the active runtime rules into `~/.claude/rules`, verify 18/18 source/runtime parity plus source/destination body sufficiency, run `git diff --check` clean, show the push result, verify the GitHub release URL and tag target, and sync README/design/changelog/TODO/phase/patch closeout state. Scope: the RULES repo and its active runtime install target only. Keep: use design-first governed `/goal` sourcing, include changelog/patch/README only when materially relevant, and do not drift into unrelated plugin/runtime work.
```

---

## Verification

Required checks before release closeout:
- touched active doctrine explicitly distinguishes trivial non-governed next steps from bounded governed repo successor work
- exact trigger conditions explicitly state when governed-surface context becomes mandatory
- governed `/goal` sourcing is explicitly design-first, then active execution surfaces, with changelog/patch/README included only when materially needed
- at least two example `/goal` outputs remain available for audit and review
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set
- `git diff --check` passes
- GitHub release `v10.21` is created and verified before closeout wording claims release completion

---

## Implementation Status

P113 is in progress.

The owner-runtime doctrine update is underway; companion/master-surface sync, runtime install/parity, commit/push, GitHub release verification, and final closeout alignment remain pending.

---

## Rollback Approach

If P113 is reversed, restore the prior released `v10.20 / P112` source state through a governed rollback wave while keeping the compact 18-rule runtime install scope unchanged unless a later rollback gate selects another install action.

Do not treat unrelated runtime destination extras, observed-only files, or history/done/archive surfaces as cleanup targets during rollback.
