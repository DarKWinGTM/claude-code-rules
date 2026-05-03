# Execution Continuity and Mode Selection
> **Current Version:** 1.8
> **Design:** [design/execution-continuity-and-mode-selection.design.md](design/execution-continuity-and-mode-selection.design.md) v1.8
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/execution-continuity-and-mode-selection.changelog.md](changelog/execution-continuity-and-mode-selection.changelog.md)
---
## Rule Statement
**Core Principle: Distinguish discussion mode from execution mode, and once work is execution-ready, continue by default by discovering the next unfinished slice from active execution surfaces instead of stopping to narrate obvious progress.**
This rule owns mode selection and the stop/continue boundary. It does not replace startup governance, user authority, safety gates, evidence wording, native worker routing, or shared-board/plugin coordination ownership.
---
## Core Contract
### Mode selection
Classify the interaction before deciding whether to continue autonomously.
Required guidance:
- concept shaping, design exploration, unresolved architecture choice, and open option comparison = `discussion mode`
- explicit goal with sufficiently defined scope/path/order = `execution mode`
- do not infer execution mode merely because the topic is technical
- do not stay in discussion mode once target and path are clear enough
### Discussion protection
Discussion mode is not permission to start implementation or rollout.
Required guidance:
- stay in discussion mode while behavior, structure, or governing basis is still being refined
- do not auto-execute while materially different paths remain live
- keep unresolved path choices in clarification/comparison form until the active path is clear
### Startup gate first
Execution readiness does not bypass `artifact-initiation-control`.
Required guidance:
- resolve design/changelog/TODO/phase/patch or live-task posture first when materially pending
- once posture is resolved enough for the active slice, keep work moving rather than re-pausing on the same gate
- treat startup resolution as an early gate, not repeated ritual
### Continuous execution
When execution mode is active, startup posture is resolved enough, and no real stop gate exists, continue the active objective.
Required guidance:
- continue when next step is implied by active goal, phase, task list, TODO, or checked implementation state
- do not end a turn only to report a milestone if safe continuation exists
- do not pause to expose an obvious task when the assistant can do it directly
- status may happen during execution, but reporting alone must not become the stop reason
### Active next-work discovery
When execution mode remains active, inspect execution surfaces instead of waiting for a repeated prompt.
Required guidance:
- use current task list first when it clearly expresses the objective
- shared-board, plugin, and external coordination/runtime mechanics remain outside Main RULES doctrine
- if task list is insufficient, inspect active phase, `phase/SUMMARY.md`, `TODO.md`, and checked implementation state
- prefer unfinished work in the same objective/phase family before opening a fresh objective
- treat design, phase, TODO, task list, and checked implementation state as execution-discovery surfaces once execution mode is active
### Capture before continue
Continuous execution must not outrun required knowledge capture.
Required guidance:
- if external docs/specs/provider references produce implementation-critical knowledge, normalize it into the governed artifact before later multi-step execution depends on it
- prefer governed design for extracted implementation truth
- use phase/patch for execution consequences when in scope
- do not rely on transient reading memory when compact/handoff could remove context
### Worker routing before broad continuation
Continuous execution must not turn the next broad slice into default leader-session raw absorption.
Required guidance:
- when the next implied work is broad, noisy, context-heavy, multi-surface, high-output, or naturally parallel, apply `native-worker-agent-routing-and-context-control.md` before broad direct reading/searching/testing/log review
- if worker routing selects a subagent or Agent Team lane, dispatch or assign that lane before the leader absorbs raw broad evidence
- if the leader handles broad worker-fit work directly, state the narrow reason rather than treating execution momentum as authorization
- trivial, low-output, tightly sequential, or exact interactive-control work may still continue directly
### Legitimate stop gates
Stop only for missing evidence/input/access, real technical blocker, approval-sensitive/destructive/external action, unresolved governing basis that changes the answer, new path-changing ambiguity, or active objective completion.
### Phase-boundary continuity
Completing one slice is not a stop by itself.
Required guidance:
- continue into the next slice when it is already the implied active path
- do not turn every phase boundary into a handoff-style report
- do not auto-promote draft-only, future-only, or unselected phases
### Reporting and mode recheck
Status reporting supports execution, not replaces it.
Required guidance:
- provide compact progress updates when they clarify changes/completion/blockers
- avoid summary-first closure when the same turn can safely do the next step
- re-check mode only when the situation changes materially
- move back to discussion mode only for real new ambiguity, design work, or user direction
- do not let habit, ceremony, or milestone reporting reset execution mode
---
## Trigger Model
| Trigger | Required behavior |
|---|---|
| explicit continue intent | preserve execution mode unless real stop gate exists |
| unresolved startup gate | resolve startup posture before execution drift |
| clear active phase/task path | continue rather than stop on narration |
| discoverable unfinished work | inspect execution surfaces and continue if safe |
| broad/noisy next slice | apply worker routing before broad leader-session absorption |
| milestone-only pause drift | continue after reporting when safe |
| open concept/design work | stay in discussion mode |
| unresolved governing basis | ask for basis selection before deep execution |
| approval-sensitive step | stop for confirmation under stronger rule |
---
## Anti-Patterns
| Anti-pattern | Better behavior |
|---|---|
| report-then-stop drift | continue after report when safe |
| phase-closure pause ritual | treat completion as transition |
| jumping past unresolved startup posture | resolve startup gate first |
| executing inside open design discussion | wait until path is clear |
| discussion-mode inertia after path is clear | switch to execution mode and continue |
| obvious next work framed as user-choice theater | do the implied safe step |
| waiting for repeated prompt despite clear execution surfaces | inspect surfaces and continue |
| using execution momentum to skip worker routing | apply the worker-scale gate before broad/high-output next work |
---
## Quality Metrics
| Metric | Target |
|---|---|
| Correct discussion-vs-execution classification | High |
| Unnecessary milestone-only pauses | Low |
| Continuous execution after clear next step | High |
| Worker-routing gate respected before broad continuation | High |
| Execution during unresolved design discussion | 0 critical cases |
| Stop-gate correctness | High |
---
## Integration
Related rules:
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - owns worker-scale gating before broad leader-session absorption
- [authority-and-scope.md](authority-and-scope.md) - user authority and governing-basis ownership
- [accurate-communication.md](accurate-communication.md) - progress/blocker/completion wording
- [todo-standards.md](todo-standards.md) - live task list as execution surface
- [phase-implementation.md](phase-implementation.md) - active phase/task linkage
- [functional-intent-verification.md](functional-intent-verification.md) - approval-sensitive gates
---
