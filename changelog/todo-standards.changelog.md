# Changelog - TODO Standards

> **Parent Document:** [../todo-standards.md](../todo-standards.md)
> **Current Version:** 2.17
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.17 | 2026-04-18 | **[Aligned task-list creation more strongly to phase-shaped context and session language](#version-217)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.16 | 2026-04-18 | **[Made required TODO sync explicit as companion work](#version-216)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.15 | 2026-04-17 | **[Retired stale shared-execution deferral in TODO standards](#version-215)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.14 | 2026-04-17 | **[Reduced TODO memsearch wording to shared-board defer only](#version-214)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 2.13 | 2026-04-17 | **[Reduced TODO standards to global task-list doctrine only](#version-213)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 2.12 | 2026-04-13 | **[Made visible session ownership a default task-list standard for session-owned work](#version-212)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.11 | 2026-04-13 | **[Made session-held task visibility more explicit in live task updates](#version-211)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
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

<a id="version-217"></a>
## Version 2.17: Aligned task-list creation more strongly to phase-shaped context and session language

**Date:** 2026-04-18
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `todo-standards.md` from v2.16 to v2.17.
- Updated `design/todo-standards.design.md` from v2.16 to v2.17.
- Added trigger and creation guidance so task-list creation aligns not only to an already-active exact phase, but also to clearly phase-shaped or staged project/workstream context.
- Added wording that task subjects and descriptions should align naturally with the active session language/register rather than defaulting to detached generic wording.
- Added verification coverage for both phase-shaped task creation alignment and session-language-aligned task wording.

### Summary
TODO standards now says more clearly that live task creation should follow the current phase structure when visible, the clearly implied stage/family when not yet formalized, and the current session language when wording the task itself.

---

<a id="version-216"></a>
## Version 2.16: Made required TODO sync explicit as companion work

**Date:** 2026-04-18
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `todo-standards.md` from v2.15 to v2.16.
- Updated `design/todo-standards.design.md` from v2.15 to v2.16.
- Clarified that when `TODO.md` is required for governed work, TODO synchronization is required companion work rather than optional bookkeeping.
- Added verification coverage so required TODO sync is checked explicitly instead of being left implicit behind the live task-list surface.
- Preserved the TODO-last synchronization order while tightening the rule that the later sync still has to happen before the governed wave is treated as fully synchronized.

### Summary
TODO standards now states more directly that durable TODO sync remains required companion work when the governed change actually needs `TODO.md`.

---

<a id="version-215"></a>
## Version 2.15: Retired stale shared-execution deferral in TODO standards

**Date:** 2026-04-17
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `todo-standards.md` from v2.14 to v2.15.
- Replaced the old defer line that still pointed to `shared-execution-coordination.md` with explicit wording that shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES current doctrine.
- Kept TODO standards focused on durable-vs-live tracking roles and the generic task-list update contract.

### Summary
TODO standards no longer point to a stale in-repo coordination owner and now state the out-of-scope boundary directly.

---

<a id="version-214"></a>
## Version 2.14: Reduced TODO memsearch wording to shared-board defer only

**Date:** 2026-04-17
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Replaced the old optional memsearch support wording with a narrower boundary line so shared-board-specific memsearch handling no longer remains in Main RULES active doctrine.
- Kept TODO standards focused on the global live-task-list trigger model, same-objective retention, and generic update contract.

### Summary
TODO standards now keep no active memsearch doctrine of their own beyond a narrow shared-board/out-of-scope boundary.

---

<a id="version-213"></a>
## Version 2.13: Reduced TODO standards to global task-list doctrine only

**Date:** 2026-04-17
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Reduced `todo-standards.md` so shared-board-specific session grammar, request/held/blocked title specifics, and receiving-side remap semantics now defer to `claude-session-coordination`.
- Preserved the global live-task-list trigger model, startup bridge, same-objective retention, and generic live update contract inside RULES.

### Summary
TODO standards now keep only the global task-list doctrine, while shared-task-list-path naming and remap semantics move to the plugin-owned coordination rule source.

---

<a id="version-212"></a>
## Version 2.12: Made visible session ownership a default task-list standard for session-owned work

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.11 to v2.12.
- Updated `design/todo-standards.design.md` from v2.11 to v2.12.
- Added explicit guidance that visible session ownership is a default board-facing standard for session-owned work even when the current task list is not shared across several sessions.
- Added explicit held-owner and blocked-on-session title forms while preserving request/handoff naming for request-layer work.

### Summary
TODO standards now treat visible session ownership as a general task-list standard instead of a mode-specific convention, while keeping request, held, and blocked states distinct.

---

<a id="version-211"></a>
## Version 2.11: Made session-held task visibility more explicit in live task updates

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards.md` from v2.10 to v2.11.
- Updated `design/todo-standards.design.md` from v2.10 to v2.11.
- Added explicit guidance that session-held, handoff, and blocked-on-session tasks should identify the relevant session visibly enough for fast scanability.
- Preserved request-style handoff naming and receiving-side remap behavior.

### Summary
TODO standards now make session-held work easier to identify in the live task board instead of leaving that visibility too implicit.

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
- Added explicit deferral that multi-session shared-board semantics stay outside Main RULES scope.
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
