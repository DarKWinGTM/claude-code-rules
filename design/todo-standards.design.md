# TODO Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.26
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-07)

---

## Current Target-State Refinement

This design now requires non-trivial live task entries to stay outcome/goal-shaped rather than command-only when goal, expected output, or completion gate meaning prevents drift. The task list should still remain lightweight; goal/output/gate details belong in the subject or description only when they improve execution clarity.

This applies especially to phase-backed or staged work, where tasks should expose phase context and the intended output/gate without turning every command or trivial lookup into a bulky template.

---

### 3.4 Daily-First Rollover Surfaces

`TODO.md` remains the current durable state file, not a growing archive. When active-scan bloat appears, old movement/detail is preserved in `todo/history/YYYY-MM-DD*.md` and `todo/done/<task-or-wave>.md`, while the main TODO restarts as a compact index with active tasks and explicit history/done references.

## 1) Goal

Define a simple execution-tracking governance model that stays aligned with UDVC-1, preserves `TODO.md` as the durable/project tracking layer, uses Claude Code's built-in task list as the live execution surface for non-trivial active work, keeps non-trivial entries outcome/goal-shaped rather than command-only, keeps material coding verification slices visible when implementation and verification are distinct outcomes, visibly links phase-backed live task entries to active or implied phase context, resolves tracking posture early when meaningful governed work genuinely needs visibility, and prevents non-material live tracking friction from collapsing bounded worker routing.

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
- implementation and verification are distinct material outcomes in non-trivial coding work
- an active phase already exists for the work
- the checked project/workstream context already shows a clearly phase-shaped or staged execution pattern even if the exact next phase file has not been opened yet

Do not skip the built-in task list in those cases unless there is a narrow justified reason.

Do not force built-in task-list overhead when:
- the task is trivial and isolated
- the work is a one-step lookup or one-step fix
- the task list would add more ceremony than clarity

### 3.5.1 Current-Phase-First but Phase-Context-Aware Task-List Rule
When an active phase already exists, the task list should mirror that current phase before proposing future-phase work.

If `/phase` exists and relevant governed phase context is already available, task creation must inspect that phase context before shaping the live task list.
Detached generic task shaping in the presence of relevant governed phase context should be treated as execution drift rather than as an acceptable fallback.

If the exact next phase file does not yet exist but the checked project/workstream context already makes the current phase family or staged execution lane clear, task-list creation should still align to that implied current phase/stage instead of falling back to detached generic standalone tasks.

Task-list shaping may reveal that a phase file is needed, but it should not silently decide that the file must be a new major phase. Current phase update, existing-family subphase, new major, or ask-now lineage handling belongs to `phase-implementation.md`.

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
- do not let task-list shaping become implicit new-major phase creation when phase lineage points to an existing family or is unresolved
- when `/phase` already contains relevant next planned phase information, use that information to improve continuity, sequencing, and draft next-work visibility rather than ignoring it
- do not let the task list drift into next-wave planning while the current phase or clearly implied current stage still defines the active execution surface
- if the current phase is already complete, say that directly before creating any draft next-wave tasks
- already-authored future-phase context may inform discovery and draft planning, but it does not become active execution work until that phase is explicitly opened, selected, or otherwise made active by the governing phase context

### 3.5.2 One-Phase-Many-Tasks Rule
One phase may legitimately contain several live tasks, and each non-trivial phase-backed task should carry visible phase context.

Required guidance:
- allow multiple task entries inside the same phase when the phase contains several execution slices
- visibly expose phase ID, phase name, phase family, or implied-stage context in each phase-backed task subject or description
- prefer compact subject linkage such as `P<phase-id>` when no stronger title grammar applies
- use `phase_ref` or equivalent description linkage when subject linkage would conflict with another title grammar
- keep tasks as execution slices inside the phase rather than forcing one whole phase into one oversized task
- do not require every phase to have only one task

### 3.5.3 Future-Phase Task Boundary
Do not create task-list entries for a future phase as if they are active execution work unless that future phase has actually been opened or selected.

Required guidance:
- treat future-phase tasks as draft/proposal work only until the user selects or opens that later phase
- do not let a request to show the task list silently become permission to populate it with speculative future-wave tasks
- if `/phase` already records likely next phases, that information may still be surfaced as bounded planning context or draft next-work context
- if draft future-phase tasks are shown, make that draft status explicit
- do not let already-authored next planned phase information be ignored when it is relevant to understanding the current execution path, but do not silently upgrade it into active execution either

### 3.6 Live Task-List Update Contract
When the built-in task list is in use:
- create the task list early rather than after the work is already underway
- mark a task `in_progress` when real work on that slice begins
- mark a task `completed` as soon as that slice is actually done
- preserve or add a visible verification slice when non-trivial coding implementation is done but targeted verification remains material
- add new tasks when newly discovered work is real and non-trivial
- keep task entries outcome-sized rather than command-sized, and include expected output or completion gate meaning when material
- when the checked project/workstream context is already phase-shaped, keep task creation aligned to the current active phase or clearly implied current stage/family even if the exact next phase file is still pending
- if task shaping shows a new phase file is needed, defer current phase vs subphase vs new-major selection to `phase-implementation.md`
- when `/phase` exists and relevant governed phase context is available, inspect that phase context before shaping new task entries or extending existing ones
- do not default task creation to detached generic standalone wording when stronger checked phase/stage context already exists
- when relevant governed phase context exists but task shaping does not follow it, treat that outcome as task-shaping drift rather than as an acceptable generic fallback
- after creating or extending a phase-backed task, verify that the subject or description visibly exposes the phase context and update it immediately when missing
- task subjects and descriptions should follow the actual active session language pattern rather than defaulting to detached generic system wording
- if the session is primarily Thai, task wording should be Thai-led by default
- if the session naturally uses mixed Thai+English wording, task wording should follow that mix rather than being forced into one language
- technical labels may remain in their technical form when forced translation would reduce clarity or make the wording read less naturally
- this rule does not impose a fixed language ratio; it should follow the active session communication context and higher-priority runtime language preferences
- treat the task list as the first active source for discovering the next unfinished work within the same objective
- if the task list alone is insufficient, use the active phase, the current phase family, `phase/SUMMARY.md`, already-authored `Next possible phases` in the relevant phase files, `TODO.md`, and checked implementation state to discover the next unfinished slice before waiting for a restated user prompt
- keep the task list tied to the current active execution surface rather than using it mainly as a future-wave scratchpad
- do not let the task list drift into stale or vague bookkeeping
- if live task-list creation or update fails during bounded worker dispatch, classify whether tracking is material; repair material tracking before sync/completion claims, but do not collapse a non-material standalone research lane into leader raw absorption merely because live tracking had friction
- keep plugin/shared-board exact title grammar outside Main RULES while still requiring phase/task visibility at this generic layer

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
- [ ] Non-trivial coding work preserves a visible verification slice when implementation and verification are distinct material outcomes
- [ ] Task creation stays aligned to active phase or clearly implied staged/phase context when that context is already visible
- [ ] Phase-backed or clearly phase-shaped task entries visibly expose phase context in subject or description
- [ ] Task creation does not silently allocate a new major phase when `phase-implementation.md` lineage handling is needed
- [ ] Task wording stays aligned to the active session language/register instead of defaulting to detached generic wording
- [ ] Task entries remain outcome-sized rather than command-sized and include output/gate meaning when material
- [ ] Required TODO synchronization is not downgraded into optional bookkeeping
- [ ] Live tracking friction is repaired when material and bounded/reported when non-material to standalone worker routing
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
| Visible verification slices for non-trivial coding work | High when implementation and verification are distinct material outcomes |
| Current-phase-first task-list alignment | High when a phase is active |
| Visible phase linkage for phase-backed task entries | High |
| Task-list-driven new-major phase drift | 0 critical cases |
| Future-phase task drift before explicit phase opening | 0 critical cases |
| Stale or vague live task lists during non-trivial work | Low |
| Non-material tracking friction derailing worker routing | 0 critical cases |

---

## 7) Related Documents

| Document | Relationship |
|----------|--------------|
| [development-verification-and-debug-strategy.design.md](development-verification-and-debug-strategy.design.md) | Owns coding-time verification strategy; this design keeps material verification work visible in live task tracking |
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup tracking posture resolution |
| [phase-implementation.md](../phase-implementation.md) | Phase identity and major-vs-subphase lineage selection when task shaping reveals phase work |
| [document-changelog-control.design.md](document-changelog-control.design.md) | Synchronization order and authority boundary |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role model and durable-vs-live tracking distinction |
| [../todo-standards.md](../todo-standards.md) | Runtime implementation |

---

> Full history: [../changelog/todo-standards.changelog.md](../changelog/todo-standards.changelog.md)
