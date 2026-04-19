# TODO Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.17
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662 (2026-04-18)

---

## 1) Goal

Define a simple execution-tracking governance model that stays aligned with UDVC-1, preserves `TODO.md` as the durable/project tracking layer, uses Claude Code's built-in task list as the live execution surface for non-trivial active work, and resolves tracking posture early when meaningful governed work genuinely needs visibility.

---

## 2) Scope

Applies to the durable `TODO.md` layer plus Claude Code's built-in live task list when active non-trivial work needs execution visibility.

Multi-session shared-board, plugin, and external coordination/runtime mechanics are outside Main RULES scope.

---

## 3) Core Contract

### 3.1 Durable-vs-Live Tracking Role
`TODO.md` is the durable/project execution-tracking artifact.
It is not a version-authority document.

Claude Code's built-in task list is the live execution-tracking surface for active non-trivial work.

Required guidance:
- use the built-in task list to show what is planned, in progress, and completed during active non-trivial work
- keep `TODO.md` for durable repository/project tracking when persistence/history is needed
- do not treat the built-in task list as a governed repository document
- do not treat `TODO.md` as a replacement for live task visibility during active non-trivial work

### 3.2 Startup Establishment Rule
When meaningful governed work requires tracking, startup tracking posture must be resolved early through `artifact-initiation-control`.

That resolution may include:
- `TODO.md` posture (`use existing`, `create now`, `ask now`, `not required`)
- early initialization of the built-in task list when the work is non-trivial and live execution visibility materially helps

This rule distinguishes:
- early tracking establishment when visibility is needed
- later TODO content synchronization after design/runtime/changelog changes

Tracking should not be treated as retrospective backfill by default.

### 3.3 Required Structure

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

### 3.4 Pending-Only Discipline
- Pending areas contain pending tasks only.
- Completed content belongs only in `Completed` and `History`.
- Deferred work remains pending with clear text labels.

### 3.5 Live Task-List Trigger Model
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

### 3.5.1 Current-Phase-First Task-List Rule
When an active phase already exists, the task list should mirror that current phase before proposing future-phase work.

If the exact next phase file does not yet exist but the checked project/workstream context already makes the current phase family or staged execution lane clear, task-list creation should still align to that implied current phase/stage instead of falling back to detached generic standalone tasks.

Required guidance:
- create the built-in task list for the active phase rather than waiting for the user to ask explicitly
- default the task list to the current active phase before opening tasks for any later phase
- when no exact new phase file is open yet, but the current staged/phase family is already clear from checked context, create task entries that still reflect that phase-shaped execution structure
- do not let the task list drift into next-wave planning while the current phase or clearly implied current stage still defines the active execution surface
- if the current phase is already complete, say that directly before creating any draft next-wave tasks

### 3.5.2 One-Phase-Many-Tasks Rule
One phase may legitimately contain several live tasks.

Required guidance:
- allow multiple task entries inside the same phase when the phase contains several execution slices
- prefer task subjects that include the phase ID when a phase is active
- keep tasks as execution slices inside the phase rather than forcing one whole phase into one oversized task
- do not require every phase to have only one task

### 3.5.3 Future-Phase Task Boundary
Do not create task-list entries for a future phase as if they are active execution work unless that future phase has actually been opened or selected.

Required guidance:
- treat future-phase tasks as draft/proposal work only until the user selects or opens that later phase
- do not let a request to show the task list silently become permission to populate it with speculative future-wave tasks
- if draft future-phase tasks are shown, make that draft status explicit

### 3.6 Live Task-List Update Contract
When the built-in task list is in use:
- create the task list early rather than after the work is already underway
- mark a task `in_progress` when real work on that slice begins
- mark a task `completed` as soon as that slice is actually done
- add new tasks when newly discovered work is real and non-trivial
- keep task entries outcome-sized rather than command-sized
- when the checked project/workstream context is already phase-shaped, keep task creation aligned to the current active phase or clearly implied current stage/family even if the exact next phase file is still pending
- do not default task creation to detached generic standalone wording when stronger checked phase/stage context already exists
- task subjects and descriptions should align naturally with the active session language/register rather than defaulting to detached generic system wording
- this rule does not impose a fixed language ratio; it should follow the active session communication context and higher-priority runtime language preferences
- treat the task list as the first active source for discovering the next unfinished work within the same objective
- if the task list alone is insufficient, use the active phase, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state to discover the next unfinished slice before waiting for a restated user prompt
- keep the task list tied to the current active execution surface rather than using it mainly as a future-wave scratchpad
- do not let the task list drift into stale or vague bookkeeping

### 3.7 Simplicity Discipline
Do not require:
- dashboard counters
- priority grids
- per-task timestamps
- deadline fields
- execution telemetry blocks
- one task per command or tool call

---

## 4) Synchronization Contract

When governance work changes governed artifacts, update in this order:
1. design
2. runtime rule
3. changelog
4. TODO

TODO content updates still occur last among the primary active layers.
That later content-sync order does not weaken the early startup-establishment rule or the expectation that live task tracking starts early when the work is non-trivial.

When `TODO.md` is required for the governed work, TODO synchronization is required companion work rather than optional bookkeeping.
That means TODO may sync later in the order, but it still needs to be completed before the governed wave is treated as fully synchronized.

---

## 5) Verification Checklist

- [ ] TODO keeps the required simplified structure
- [ ] Pending area contains pending tasks only
- [ ] Completed items are not mixed into pending sections
- [ ] No dashboard or priority overhead is present
- [ ] Tracking posture is resolved early when meaningful tracking is required
- [ ] Built-in task list is used proactively for non-trivial work when live execution visibility materially helps
- [ ] Task creation stays aligned to active phase or clearly implied staged/phase context when that context is already visible
- [ ] Task wording stays aligned to the active session language/register instead of defaulting to detached generic wording
- [ ] Task entries remain outcome-sized rather than command-sized
- [ ] Required TODO synchronization is not downgraded into optional bookkeeping
- [ ] TODO content update occurs after design/runtime/changelog synchronization

---

## 6) Quality Metrics

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

## 7) Related Documents

| Document | Relationship |
|----------|--------------|
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup tracking posture resolution |
| [document-changelog-control.design.md](document-changelog-control.design.md) | Synchronization order and authority boundary |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role model and durable-vs-live tracking distinction |
| [../todo-standards.md](../todo-standards.md) | Runtime implementation |

---

> Full history: [../changelog/todo-standards.changelog.md](../changelog/todo-standards.changelog.md)
