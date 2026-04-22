# TODO Standards

> **Current Version:** 2.17
> **Design:** [design/todo-standards.design.md](design/todo-standards.design.md) v2.17
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)

---

## Rule Statement

**Core Principle: Keep `TODO.md` as the durable execution-tracking layer, use Claude Code's built-in task list as the live execution-tracking surface for non-trivial active work, and resolve tracking posture early instead of treating it as retrospective cleanup.**

Multi-session shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES current doctrine.

---

## Core Contract

### 1) Durable-vs-Live Tracking Role
`TODO.md` is the durable/project execution-tracking artifact.
It is not a version-authority document.

Claude Code's built-in task list is the live execution-tracking surface for active non-trivial work.

Required guidance:
- use the built-in task list to show what is planned, in progress, and completed during active non-trivial work
- keep `TODO.md` for durable repository/project tracking when persistence/history is needed
- do not treat the built-in task list as a governed repository document
- do not treat `TODO.md` as a replacement for live task visibility during active non-trivial work

### 2) Startup Establishment Bridge
When meaningful governed work requires tracking, startup tracking posture must be resolved early through `artifact-initiation-control`.

That resolution may include:
- `TODO.md` posture (`use existing`, `create now`, `ask now`, `not required`)
- early initialization of the built-in task list when the work is non-trivial and live execution visibility materially helps

Durable TODO establishment at startup is different from later TODO content updates.

### 3) Required Structure

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

### 4) Pending-Only Discipline
- Pending areas contain pending tasks only.
- Completed content belongs only in `Completed` and `History`.
- Deferred work remains pending with clear text labels.

### 5) Live Task-List Trigger Model
Built-in task-list usage is expected by default when one or more are true:
- the work is non-trivial
- the work has 3 or more distinct steps
- the work spans multiple files or multiple execution stages
- the work is likely to continue across multiple execution slices
- the user would materially benefit from seeing pending / in_progress / completed state live
- an active phase already exists for the work
- the checked project/workstream context already shows a clearly phase-shaped or staged execution pattern even if the exact next phase file has not been opened yet

Do not skip the built-in task list in those cases unless there is a narrow justified reason.

Do not force built-in task-list overhead when:
- the task is trivial and isolated
- the work is a one-step lookup or one-step fix
- the task list would add more ceremony than clarity

### 5.1 Current-Phase-First but Phase-Context-Aware Task-List Rule
When an active phase already exists, the task list should mirror that current phase before proposing future-phase work.

If `/phase` exists and relevant governed phase context is already available, task creation must inspect that phase context before shaping the live task list.
Detached generic task shaping in the presence of relevant governed phase context should be treated as execution drift rather than as an acceptable fallback.

If the exact next phase file does not yet exist but the checked project/workstream context already makes the current phase family or staged execution lane clear, task-list creation should still align to that implied current phase/stage instead of falling back to detached generic standalone tasks.

If `/phase` already contains additional relevant planning context, task behavior should not stop at the currently open phase file alone. It should also consult bounded phase context that already exists in the governed phase workspace, such as:
- the current active phase
- the current phase family or staged execution lane
- the phase order and dependency structure visible in `phase/SUMMARY.md`
- already-authored `Next possible phases` in the relevant child phase files

Required guidance:
- create the built-in task list for the active phase rather than waiting for the user to ask explicitly
- when `/phase` exists and relevant governed phase context is available, inspect that phase context before shaping or extending the live task list
- default the task list to the current active phase before opening tasks for any later phase
- when no exact new phase file is open yet, but the current staged/phase family is already clear from checked context, create task entries that still reflect that phase-shaped execution structure
- when `/phase` already contains relevant next planned phase information, use that information to improve continuity, sequencing, and draft next-work visibility rather than ignoring it
- do not let the task list drift into next-wave planning while the current phase or clearly implied current stage still defines the active execution surface
- if the current phase is already complete, say that directly before creating any draft next-wave tasks
- already-authored future-phase context may inform discovery and draft planning, but it does not become active execution work until that phase is explicitly opened, selected, or otherwise made active by the governing phase context

### 5.2 One-Phase-Many-Tasks Rule
One phase may legitimately contain several live tasks.

Required guidance:
- allow multiple task entries inside the same phase when the phase contains several execution slices
- prefer task subjects that include the phase ID when a phase is active
- keep tasks as execution slices inside the phase rather than forcing one whole phase into one oversized task
- do not require every phase to have only one task

### 5.2.1 Same-Objective Retention Rule
Within the same active objective, reuse the current task list by default instead of replacing it with a fresh set.

Required guidance:
- append new real work to the current task list when it belongs to the same active objective
- keep already-completed tasks visible until the current objective is genuinely closed
- do not recreate the task list merely because a new slice, subtask, or cleanup pass was discovered inside the same active objective
- start a fresh task list only when the user opens a genuinely new objective, the prior objective is fully closed, or the user explicitly requests a reset

### 5.3 Future-Phase Task Boundary
Do not create task-list entries for a future phase as if they are active execution work unless that future phase has actually been opened or selected.

Required guidance:
- treat future-phase tasks as draft/proposal work only until the user selects or opens that later phase
- do not let a request to "show the task list" silently become permission to populate the task list with speculative future-wave tasks
- if `/phase` already records likely next phases, that information may still be surfaced as bounded planning context or draft next-work context
- if draft future-phase tasks are shown, make that draft status explicit
- do not let already-authored next planned phase information be ignored when it is relevant to understanding the current execution path, but do not silently upgrade it into active execution either

### 6) Live Task-List Update Contract
When the built-in task list is in use:
- create the task list early rather than after the work is already underway
- mark a task `in_progress` when real work on that slice begins
- mark a task `completed` as soon as that slice is actually done
- add new tasks when newly discovered work is real and non-trivial
- keep task entries outcome-sized rather than command-sized
- extend the current task list within the same active objective instead of replacing it with a fresh set
- keep completed tasks visible until the active objective is truly closed or explicitly reset
- when the checked project/workstream context is already phase-shaped, keep task creation aligned to the current active phase or clearly implied current stage/family even if the exact next phase file is still pending
- when `/phase` exists and relevant governed phase context is available, inspect that phase context before shaping new task entries or extending existing ones
- do not default task creation to detached generic standalone wording when stronger checked phase/stage context already exists
- when relevant governed phase context exists but task shaping does not follow it, treat that outcome as task-shaping drift rather than as an acceptable generic fallback
- task subjects and descriptions should follow the actual active session language pattern rather than defaulting to detached generic system wording
- if the session is primarily Thai, task wording should be Thai-led by default
- if the session naturally uses mixed Thai+English wording, task wording should follow that mix rather than being forced into one language
- this rule does not impose a fixed language ratio; it should follow the active session communication context and higher-priority runtime language preferences
- technical labels may remain in their technical form when forced translation would reduce clarity or make the wording read less naturally
- treat the task list as the first active source for discovering the next unfinished work within the same objective
- if the task list alone is insufficient, use the active phase, the current phase family, `phase/SUMMARY.md`, already-authored `Next possible phases` in the relevant phase files, `TODO.md`, and checked implementation state to discover the next unfinished slice before waiting for a restated user prompt
- keep the task list tied to the current active execution surface rather than using it mainly as a future-wave scratchpad
- when execution mode remains active and no real stop gate exists, let the task list support continued execution rather than milestone-only pause/report behavior
- do not let the task list drift into stale or vague bookkeeping

### 7) Simplicity Discipline
Do not require:
- dashboard counters
- priority grids
- per-task timestamps
- deadline fields
- execution telemetry blocks
- one task per command or tool call

---

## Synchronization Contract

When governance work changes governed artifacts, update in this order:
1. design
2. runtime rule
3. changelog
4. TODO

TODO content updates still happen last among the primary active layers.
That later sync order does not weaken the early startup-establishment rule or the expectation that live task tracking starts early when the work is non-trivial.

When `TODO.md` is required for the governed work, TODO synchronization is required companion work rather than optional bookkeeping.
That means:
- TODO may be updated later than design/runtime/changelog in the sync order
- but it should still be completed before the governed wave is treated as fully synchronized
- the built-in task list does not replace this durable TODO sync when the task actually requires repository-level tracked execution history

---

## Verification Checklist

- [ ] TODO keeps the required simplified structure
- [ ] Pending area contains pending tasks only
- [ ] Completed items are not mixed into pending sections
- [ ] No dashboard or priority overhead is present
- [ ] Tracking posture was resolved early when meaningful tracking was required
- [ ] Built-in task list was used proactively for non-trivial work when live execution visibility materially helped
- [ ] Task creation stayed aligned to active phase, clearly implied staged/phase context, and already-authored bounded phase-planning context from `/phase` when that context was already visible and relevant
- [ ] Task wording stayed aligned to the active session language/register instead of defaulting to detached generic wording
- [ ] Task entries remained outcome-sized rather than command-sized
- [ ] Required TODO synchronization was not downgraded into optional bookkeeping
- [ ] TODO content update occurred after design/runtime/changelog synchronization

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Structural compliance with required sections | 100% |
| Pending-section contamination with completed tasks | 0 |
| Dashboard-style overhead artifacts | 0 |
| Durable-vs-live tracking role clarity | 100% |
| Startup tracking posture resolved before drift when needed | 100% |
| Proactive task-list usage on non-trivial work | High |
| Current-phase-first task-list alignment | High when a phase is active |
| Future-phase task drift before explicit phase opening | 0 critical cases |
| Stale or vague live task lists during non-trivial work | Low |

---

## Integration

Related documents:
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup tracking posture resolution
- [document-changelog-control.md](document-changelog-control.md) - synchronization order and authority boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository role model and durable-vs-live tracking distinction

---

> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)
