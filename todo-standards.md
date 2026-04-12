# TODO Standards

> **Current Version:** 2.11
> **Design:** [design/todo-standards.design.md](design/todo-standards.design.md) v2.11
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)

---

## Rule Statement

**Core Principle: Keep `TODO.md` as the durable execution-tracking layer, use Claude Code's built-in task list as the live execution-tracking surface for non-trivial active work, and resolve tracking posture early instead of treating it as retrospective cleanup.**

Multi-session shared-board coordination semantics such as session lease, handoff, retention/aging, anti-overclear behavior, and optional memsearch support defer to `shared-execution-coordination.md`.

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

Do not skip the built-in task list in those cases unless there is a narrow justified reason.

Do not force built-in task-list overhead when:
- the task is trivial and isolated
- the work is a one-step lookup or one-step fix
- the task list would add more ceremony than clarity

### 5.1 Current-Phase-First Task-List Rule
When an active phase already exists, the task list should mirror that current phase before proposing future-phase work.

Required guidance:
- create the built-in task list for the active phase rather than waiting for the user to ask explicitly
- default the task list to the current active phase before opening tasks for any later phase
- do not let the task list drift into next-wave planning while the current phase still defines the active execution surface
- if the current phase is already complete, say that directly before creating any draft next-wave tasks

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
- if draft future-phase tasks are shown, make that draft status explicit

### 6) Live Task-List Update Contract
When the built-in task list is in use:
- create the task list early rather than after the work is already underway
- mark a task `in_progress` when real work on that slice begins
- mark a task `completed` as soon as that slice is actually done
- add new tasks when newly discovered work is real and non-trivial
- keep task entries outcome-sized rather than command-sized
- extend the current task list within the same active objective instead of replacing it with a fresh set
- keep completed tasks visible until the active objective is truly closed or explicitly reset
- treat the task list as the first active source for discovering the next unfinished work within the same objective
- if the task list alone is insufficient, use the active phase, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state to discover the next unfinished slice before waiting for a restated user prompt
- session-held, handoff, and blocked-on-session tasks should identify the relevant session visibly enough for fast scanability rather than hiding that meaning only in long description text
- cross-session request tasks should use request/handoff naming rather than carrying the sender's phase as the default visible title label
- if accepted work later needs phase/objective tracking, the receiving session should remap it into its own execution structure
- source trace should remain in description/handoff notes rather than default title prefixes when that distinction matters
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

---

## Verification Checklist

- [ ] TODO keeps the required simplified structure
- [ ] Pending area contains pending tasks only
- [ ] Completed items are not mixed into pending sections
- [ ] No dashboard or priority overhead is present
- [ ] Tracking posture was resolved early when meaningful tracking was required
- [ ] Built-in task list was used proactively for non-trivial work when live execution visibility materially helped
- [ ] Task entries remained outcome-sized rather than command-sized
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
