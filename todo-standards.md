# TODO Standards

> **Current Version:** 2.4
> **Design:** [design/todo-standards.design.md](design/todo-standards.design.md) v2.4
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)

---

## Rule Statement

**Core Principle: Keep `TODO.md` as the durable execution-tracking layer, use Claude Code's built-in task list as the live execution-tracking surface for non-trivial active work, and resolve tracking posture early instead of treating it as retrospective cleanup.**

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
Prefer proactive built-in task-list usage when one or more are true:
- the work is non-trivial
- the work has 3 or more distinct steps
- the work spans multiple files or multiple execution stages
- the work is likely to continue across multiple execution slices
- the user would materially benefit from seeing pending / in_progress / completed state live

Do not force built-in task-list overhead when:
- the task is trivial and isolated
- the work is a one-step lookup or one-step fix
- the task list would add more ceremony than clarity

### 6) Live Task-List Update Contract
When the built-in task list is in use:
- create the task list early rather than after the work is already underway
- mark a task `in_progress` when real work on that slice begins
- mark a task `completed` as soon as that slice is actually done
- add new tasks when newly discovered work is real and non-trivial
- keep task entries outcome-sized rather than command-sized
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
| Stale or vague live task lists during non-trivial work | Low |

---

## Integration

Related documents:
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup tracking posture resolution
- [document-changelog-control.md](document-changelog-control.md) - synchronization order and authority boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository role model and durable-vs-live tracking distinction

---

> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)
