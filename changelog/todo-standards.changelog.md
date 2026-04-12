# Changelog - TODO Standards

> **Parent Document:** [../todo-standards.md](../todo-standards.md)
> **Current Version:** 2.10
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.10 | 2026-04-13 | **[Clarified request-style handoff naming in the shared task board](#version-210)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.9 | 2026-04-13 | **[Deferred multi-session shared-board coordination to the new coordination owner](#version-29)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.8 | 2026-04-12 | **[Used execution surfaces to discover next unfinished work](#version-28)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.7 | 2026-04-12 | **[Kept the same task list across one active objective](#version-27)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.6 | 2026-04-12 | **[Aligned live task-list behavior to continuous execution mode](#version-26)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.5 | 2026-04-11 | **[Linked active task lists explicitly to the current phase](#version-25)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.4 | 2026-04-10 | **[Added live task-list execution tracking for non-trivial work](#version-24)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.3 | 2026-03-28 | **[Materialized TODO startup-establishment semantics and created first authority changelog](#version-23)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Created authoritative changelog history for the TODO standards chain and added a startup bridge so TODO presence is resolved early when meaningful governed work requires tracking | |
| 2.2 | 2026-03-08 | **[Existing simplified TODO standards baseline](#version-22)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Established the simplified TODO structure, pending-only discipline, and TODO-last synchronization order that the active chain already used | |

---

<a id="version-210"></a>
## Version 2.10: Clarified request-style handoff naming in the shared task board

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.9 to v2.10.
- Updated `design/todo-standards.design.md` from v2.9 to v2.10.
- Added explicit guidance that cross-session request tasks should use request/handoff naming rather than carrying the sender's phase as the default visible title label.
- Added explicit guidance that accepted work needing phase/objective tracking should be remapped by the receiving session into its own execution structure.
- Added explicit guidance that source trace should remain in description / handoff notes when that distinction matters.

### Summary
TODO standards now keep shared task-board naming aligned to request/handoff semantics instead of leaking sender phase labels into receiving-side work titles.

---

<a id="version-29"></a>
## Version 2.9: Deferred multi-session shared-board coordination to the new coordination owner

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.8 to v2.9.
- Updated `design/todo-standards.design.md` from v2.8 to v2.9.
- Added explicit deferral that multi-session shared-board semantics such as session lease, handoff, retention/aging, anti-overclear behavior, and optional memsearch support now live in `shared-execution-coordination.md`.
- Preserved durable-vs-live tracking, current-phase-first behavior, same-objective retention, and task-list-first next-work discovery.

### Summary
TODO standards now keep their tracking role while deferring multi-session shared-board coordination protocol details to the new coordination owner.

---

<a id="version-28"></a>
## Version 2.8: Used execution surfaces to discover next unfinished work

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.7 to v2.8.
- Updated `design/todo-standards.design.md` from v2.7 to v2.8.
- Added guidance that the current task list is the first active discovery surface for the next unfinished work within the same objective.
- Added bounded fallback guidance that if the task list alone is insufficient, the assistant should inspect the active phase, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state before waiting for a restated user prompt.

### Summary
TODO standards now treat the task list as the first next-work discovery surface and explicitly allow bounded fallback to the broader execution surfaces when the task list alone is not enough.

---

<a id="version-27"></a>
## Version 2.7: Kept the same task list across one active objective

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.6 to v2.7.
- Updated `design/todo-standards.design.md` from v2.6 to v2.7.
- Added an explicit same-objective retention rule so the current task list is reused and extended by default instead of being replaced with a fresh set.
- Added explicit guidance that completed tasks remain visible until the active objective is genuinely closed or explicitly reset.

### Summary
TODO standards now keep task-list continuity visible within the same active objective instead of letting repeated replacement hide earlier work.

---

<a id="version-26"></a>
## Version 2.6: Aligned live task-list behavior to continuous execution mode

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.5 to v2.6.
- Updated `design/todo-standards.design.md` from v2.5 to v2.6.
- Added bounded guidance that when execution mode remains active and no real stop gate exists, the task list should support continued execution rather than milestone-only pause/report behavior.
- Preserved the durable-vs-live tracking split and current-phase-first task-list model.

### Summary
TODO standards now reinforce that live task lists support continued execution when the active path is already clear, instead of drifting into report-only pauses.

---

<a id="version-25"></a>
## Version 2.5: Linked active task lists explicitly to the current phase

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.4 to v2.5.
- Updated `design/todo-standards.design.md` from v2.4 to v2.5.
- Strengthened task-list behavior from merely preferred to expected for non-trivial work, especially when an active phase already exists.
- Added current-phase-first guidance so live task lists mirror the active phase before any future-wave planning is introduced.
- Added one-phase-many-tasks and future-phase-boundary guidance so task lists can represent several execution slices inside one phase without drifting into speculative next-phase work.

### Summary
TODO standards now treat the built-in task list as the current-phase-first live execution surface for non-trivial active work instead of leaving it as a loosely preferred optional aid.

---

<a id="version-24"></a>
## Version 2.4: Added live task-list execution tracking for non-trivial work

**Date:** 2026-04-10
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.3 to v2.4.
- Updated `design/todo-standards.design.md` from v2.3 to v2.4.
- Clarified the durable-vs-live tracking split so `TODO.md` remains the durable repository/project execution artifact while Claude Code's built-in task list becomes the live execution-tracking surface for non-trivial active work.
- Added explicit trigger guidance for when proactive task-list usage is expected.
- Added a live task-list update contract so task entries are created early, kept outcome-sized, and updated through pending / in_progress / completed state.
- Extended verification and quality metrics so stale or vague task-list behavior is now explicitly discouraged.

### Summary
TODO standards now distinguish durable `TODO.md` tracking from live built-in task tracking and make proactive task-list usage the expected execution surface for non-trivial active work.

---

<a id="version-23"></a>
## Version 2.3: Materialized TODO startup-establishment semantics and created first authority changelog

**Date:** 2026-03-28
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `changelog/todo-standards.changelog.md` as the first authoritative history file for the TODO standards chain.
- Updated `design/todo-standards.design.md` from v2.2 to v2.3.
- Updated runtime `todo-standards.md` from the prior header-only/stub state to a full active rule body at v2.3.
- Added a startup-establishment bridge so TODO posture must be resolved early through `artifact-initiation-control` when meaningful governed work requires tracking.
- Preserved TODO’s execution-only role, simplified structure, and TODO-last content synchronization order.

### Summary
Completed the TODO standards normalization so the chain now has full active runtime semantics, authoritative changelog history, and explicit early-establishment behavior when governed work needs tracking.

---

<a id="version-22"></a>
## Version 2.2: Existing simplified TODO standards baseline

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4b07-bb9d-a90a0e57b54e

### Changes
- Established the simplified TODO structure using `Completed`, `Tasks To Do`, and `History`.
- Defined pending-only discipline.
- Removed dashboard-style overhead from the active TODO model.
- Kept TODO as an execution-only layer updated after design/runtime/changelog synchronization.

### Summary
Established the active simplified TODO governance baseline later materialized into a fully tracked changelog authority.
