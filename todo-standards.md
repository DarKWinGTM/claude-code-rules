# TODO Standards
> **Current Version:** 2.21
> **Design:** [design/todo-standards.design.md](design/todo-standards.design.md) v2.21
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)
---
## Rule Statement
**Core Principle: Keep `TODO.md` as the durable execution-tracking layer, use Claude Code's built-in task list as the live execution-tracking surface for non-trivial active work, and resolve tracking posture early instead of treating it as retrospective cleanup.**
Multi-session shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES current doctrine.
---
## Core Contract
### 1) Durable vs live tracking
`TODO.md` is the durable repository/project execution-tracking artifact. It is not version authority and does not replace live task visibility. Claude Code's built-in task list is the live execution-tracking surface for active non-trivial work.

Guidance:
- use the built-in task list to show planned, in-progress, and completed slices during active non-trivial work
- keep `TODO.md` for durable tracking when persistence/history is needed
- do not treat the built-in task list as a governed repository document
- do not treat `TODO.md` as the primary live execution board during active non-trivial work

### 2) Startup establishment bridge
When meaningful governed work requires tracking, startup tracking posture must be resolved early through `artifact-initiation-control.md`. Resolution may include `TODO.md: use existing | create now | ask now | not required` and early built-in task-list initialization when work is non-trivial and live visibility helps. Durable TODO establishment at startup is different from later TODO content updates.

### 3) Required TODO structure
```markdown
# <Project Name> - TODO
> **Last Updated:** YYYY-MM-DD
---
## ✅ Completed
<summary or completed checklist>
---
## 📋 Tasks To Do
### <Optional Category>
- [ ] <task>
---
## 📜 History
| Date | Changes |
|------|---------|
```

### 4) Pending-only discipline
Pending areas contain pending tasks only. Completed content belongs only in `Completed` and `History`. Deferred work remains pending with clear text labels.
---
## Live Task-List Trigger Model
Built-in task-list usage is expected by default when work is non-trivial, has 3+ steps, spans multiple files/stages, may continue across slices, benefits from live pending/in_progress/completed visibility, has an active phase, or is clearly phase-shaped/staged even before the exact next phase file is opened.

Do not skip the built-in task list in those cases unless there is a narrow justified reason. Do not force task-list overhead for trivial isolated work, one-step lookup/fix work, or cases where the task list adds more ceremony than clarity.
---
## Phase-Context-Aware Task Rules
When active phase or staged context exists, the task list should mirror the current phase/stage before future-phase work. Inspect relevant `/phase` context before task shaping; detached generic wording is execution drift. If the exact next phase file is absent but checked context makes the phase family or staged lane clear, align to that implied current stage.

Bounded phase context may include current active phase, current phase family/staged lane, phase order/dependencies in `phase/SUMMARY.md`, and authored `Next possible phases` in relevant child files.

Guidance:
- create the built-in task list for active phase work rather than waiting for the user to ask
- default to current active phase before opening tasks for later phases
- task shaping may reveal that a phase file is needed, but it must not choose a new major phase silently; phase identity belongs to `phase-implementation.md` and its lineage gate
- use authored next-phase information for continuity and draft visibility, not silent activation
- do not let task-list continuation become implicit new-major creation when checked lineage points to an existing family or is unresolved
- do not let the task list drift into next-wave planning while the current phase/stage still defines active execution
- if the current phase is complete, say so before creating draft next-wave tasks
- future-phase tasks remain draft/proposal until the phase is opened, selected, or otherwise made active by governing phase context
- one phase may have several outcome-sized tasks; do not force a whole phase into one oversized task
- prefer task subjects that include the current phase ID when useful
---
## Live Task-List Update Contract
When the built-in task list is in use:
- create it early rather than after work is underway
- mark a task `in_progress` when real work on that slice begins
- mark a task `completed` as soon as that slice is actually done
- add new tasks when newly discovered work is real and non-trivial
- keep entries outcome-sized rather than command-sized
- extend the current task list within the same active objective instead of replacing it
- keep completed tasks visible until objective closure or explicit reset
- start fresh only for a genuinely new objective, true closure, or explicit user reset
- align task creation to current active phase or clearly implied stage/family when checked context is phase-shaped
- inspect `/phase` context before shaping tasks when relevant governed phase context exists
- task subjects/descriptions should follow the actual active session language/register; Thai-led or Thai/English mixed wording is acceptable when natural, and technical labels may remain technical
- use the task list first for next unfinished work; if insufficient, use active phase, current phase family, `phase/SUMMARY.md`, authored `Next possible phases`, `TODO.md`, and checked implementation state
- keep the task list tied to active execution, not stale bookkeeping or a future-wave scratchpad
- when execution mode remains active and no real stop gate exists, let the task list support continued execution rather than milestone-only pause/report behavior
---
## Simplicity Discipline
Do not require dashboard counters, priority grids, per-task timestamps, deadline fields, execution telemetry blocks, or one task per command/tool call.
---
## Synchronization Contract
When governance work changes governed artifacts, update in this order:
1. design
2. runtime rule
3. changelog
4. TODO

TODO content updates still happen last among primary active layers. That later order does not weaken early startup establishment or live task-list expectations. When `TODO.md` is required for governed work, TODO synchronization is required companion work; the built-in task list does not replace durable TODO sync when repository-level tracked history is required.
---
## Verification Checklist
- [ ] TODO keeps the required simplified structure
- [ ] Pending area contains pending tasks only
- [ ] Completed items are not mixed into pending sections
- [ ] No dashboard or priority overhead is present
- [ ] Tracking posture was resolved early when meaningful tracking was required
- [ ] Built-in task list was used proactively for non-trivial active work when live visibility helped
- [ ] Task creation aligned to active phase, implied staged context, and authored bounded phase context from `/phase`
- [ ] Task creation did not silently allocate a new major phase when phase lineage needed `phase-implementation.md` handling
- [ ] Task wording aligned to active session language/register
- [ ] Task entries remained outcome-sized
- [ ] Required TODO synchronization was not downgraded into optional bookkeeping
- [ ] TODO content update occurred after design/runtime/changelog synchronization
---
## Quality Metrics
| Metric | Target |
|---|---|
| Structural compliance with required sections | 100% |
| Pending-section contamination with completed tasks | 0 |
| Dashboard-style overhead artifacts | 0 |
| Durable-vs-live tracking role clarity | 100% |
| Startup tracking posture resolved before drift | 100% |
| Proactive task-list usage on non-trivial work | High |
| Current-phase-first task-list alignment | High when a phase is active |
| Task-list-driven new-major phase drift | 0 critical cases |
| Future-phase task drift before explicit phase opening | 0 critical cases |
| Stale or vague live task lists during non-trivial work | Low |
---
## Integration
Related documents:
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup tracking posture resolution
- [phase-implementation.md](phase-implementation.md) - phase identity and major-vs-subphase lineage selection when task shaping reveals phase work
- [document-changelog-control.md](document-changelog-control.md) - synchronization order and authority boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository role model and durable-vs-live tracking distinction
---
> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)
