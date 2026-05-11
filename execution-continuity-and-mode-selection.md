# Execution Continuity and Mode Selection
> **Current Version:** 1.17
> **Design:** [design/execution-continuity-and-mode-selection.design.md](design/execution-continuity-and-mode-selection.design.md) v1.17
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/execution-continuity-and-mode-selection.changelog.md](changelog/execution-continuity-and-mode-selection.changelog.md)
---
## Rule Statement
**Core Principle: Distinguish discussion mode from execution mode, re-check user intent when the decision surface changes, and once work is execution-ready, continue by default by discovering the next unfinished slice from compact active execution surfaces while triggering rollover maintenance when oversized active governance entrypoints block safe continuation, keeping current goal state clear enough to recommend supported next goals only at true completion boundaries.**
This rule owns mode selection, the stop/continue boundary, goal-state continuity during execution, and the completion-to-roadmap/next-goal bridge. It does not replace startup governance, user authority, safety gates, evidence wording, native worker routing, phase roadmap semantics, goal-set owner semantics, or shared-board/plugin coordination ownership.
---
## Core Contract
### Mode selection and discussion protection
Classify the interaction before autonomous continuation.
- `discussion mode`: concept shaping, design exploration, unresolved architecture choice, behavior/RULES analysis, and open option comparison
- `execution mode`: explicit goal with sufficiently defined scope/path/order

Do not infer execution mode merely because the topic is technical or pasted evidence includes project paths. Do not stay in discussion mode once target and path are clear enough. Discussion mode is not permission to implement: stay there while behavior, structure, governing basis, or materially different paths remain live.

### Intent recheck before project exploration
When the user provides technical evidence, logs, snippets, paths, or another session's output, re-check whether the active request is about behavior/governance or the project itself.
- if the user asks about AI behavior, RULES behavior, or workflow compliance, treat pasted technical material as evidence for that question first
- do not start project file reading, search, or implementation merely because evidence contains paths or code snippets
- project exploration is appropriate only when requested for project facts/implementation/review, or when a bounded verification need is stated and aligned with the active question
- if the user corrects scope back to AI/RULES behavior, drop the project path and continue in the corrected scope

### Startup gate first
Execution readiness does not bypass `artifact-initiation-control.md`. Resolve materially pending design/changelog/TODO/phase/patch or live-task posture first, then keep work moving once the active slice is resolved enough. Startup resolution is an early gate, not a repeated ritual. If the active execution surfaces themselves are oversized enough to cause failed reads or autocompact thrash, resolve rollover/compaction posture before broad continuation so the current-state entrypoint remains usable.

### Continuous execution
When execution mode is active, startup posture is resolved enough, and no real stop gate exists, continue the active objective.
- continue when the next step is implied by the current goal, phase, task list, TODO, or checked implementation state
- keep the current goal, expected output, and completion gate clear enough to prevent drift when work is non-trivial
- when implementation is complete but material verification/debug/TestKit evidence remains pending, continue into the proportionate verification slice when safe
- do not end a turn only to report a milestone if safe continuation exists
- do not pause to expose an obvious task when the assistant can do it directly
- status may clarify changes/completion/blockers, but reporting alone must not become the stop reason

### God artifact continuation

Detected touched-scope God artifact pressure is active continuation work when governed execution is already underway.

Required guidance:
- continue into safe local repair when the split is clear and low-risk
- create or extend a visible repair slice when the repair is broad but belongs to the active objective
- route phase-shaped repair through phase lineage before opening a new major phase
- route reviewable before/after repair through patch posture when needed
- stop only for real ambiguity, approval-sensitive scope, destructive action, missing authority, or completed objective with no selected repair path

Reporting that God pressure exists is not a legitimate stop by itself when repair or planning is already clear.

### Goal-state continuity and completion-to-next-goal bridge
During non-trivial execution, use the goal/output/gate frame as navigation when it prevents drift or improves verification. The frame may stay internal when the path is obvious, and it must not become a stop ritual between already selected safe slices.

When the active objective is actually complete, use checked execution surfaces to decide whether a next-goal recommendation is useful.
- if a selected, unblocked current or next goal exists in the same active objective or phase chain, continue rather than converting it into a proposal
- if meaningful successor work is implied by design, phase roadmap, TODO, or checked implementation state but is not selected/opened, recommend it as an advisory next goal with why it is supported, expected output, and gate
- if successor goal state is ambiguous, approval-sensitive, destructive, or materially divergent, ask a narrow basis/approval question instead of guessing
- if no meaningful successor goal is visible in checked scope, say no next phase/wave/goal is currently selected or opened

This bridge is a closeout behavior, not a mid-execution stop ritual. It must not block phase 1 → 2 → 3 style continuation when those phases or goals are already selected, safe, and unblocked.
---
## Active Next-Work Discovery
When execution mode remains active, inspect execution surfaces instead of waiting for a repeated prompt.
- use the current task list first when it clearly expresses the objective
- if task list is insufficient, inspect active phase, compact `phase/SUMMARY.md`, compact `TODO.md`, and checked implementation state
- follow `todo/history/`, `todo/done/`, `phase/history/`, or `phase/done/` references only when active entrypoints point there for needed history/detail
- prefer unfinished work in the same objective/phase family before opening a fresh objective
- when the current objective is complete, treat design, phase roadmap, TODO, task list, and checked implementation state as roadmap-discovery surfaces for a supported next-goal recommendation
- treat design, phase, TODO, task list, and checked implementation state as execution-discovery surfaces once execution mode is active
- shared-board, plugin, and external coordination/runtime mechanics remain outside Main RULES doctrine
- oversized active governance files are maintenance triggers, not normal execution surfaces to repeatedly absorb

Phase-shaped next work must not become a new major phase by momentum. If it may belong to an existing family, apply `phase-implementation.md` major-vs-subphase lineage handling before choosing current phase update, existing-family subphase, new major, or ask-now posture. Continuation-created or continuation-extended task entries for phase-backed work must preserve visible phase linkage in the subject or description instead of becoming generic next-work tasks.
---
## Capture Before Continue
Continuous execution must not outrun required knowledge capture or required active-entrypoint compaction. If external docs/specs/provider references produce implementation-critical knowledge, normalize the extracted truth into the governed artifact before later multi-step execution depends on it. Prefer governed design for implementation truth, use phase/patch for execution consequences when in scope, and do not rely on transient reading memory when compact/handoff could remove context.
---
## Worker Routing Before Broad Continuation
Continuous execution must not turn the next broad slice into default leader-session raw absorption.
- when implied work is broad, noisy, context-heavy, multi-surface, high-output, or naturally parallel, apply `native-worker-agent-routing-and-context-control.md` before broad direct reading/searching/testing/log review
- when implied work is broad external research, design-improvement research, source comparison, or recommendation research, apply the native research orchestration gate before leader raw WebSearch/source absorption
- apply intent-first worker routing before project exploration when the next slice could be behavior/RULES analysis rather than project work
- prefer standalone subagent / worker-lane handling for broad independent read/search/audit/review work before considering Agent Team workflow
- if worker routing selects a standalone subagent, multiple subagents, or Agent Team lane, dispatch or assign that lane before the leader absorbs raw broad evidence
- if the leader handles broad worker-fit work directly, state the narrow reason rather than treating execution momentum as authorization
- trivial, low-output, tightly sequential, or exact interactive-control work may still continue directly
---
## Legitimate Stop Gates
Stop only for missing evidence/input/access, real technical blocker, approval-sensitive/destructive/external action, unresolved governing basis that changes the answer, new path-changing ambiguity, or active objective completion with no selected safe continuation. Active objective completion may still require a supported next-goal recommendation before the response ends when checked surfaces show meaningful unselected successor work.

Completing one slice is not a stop by itself. Implementation complete but material verification pending is not active objective completion unless verification is blocked, not applicable with reason, approval-sensitive, or already satisfied by the evidence held. Continue into the next slice when it is already the implied active path; treat related follow-up as a lineage checkpoint rather than automatic new-major boundary; do not turn every phase boundary into a handoff-style report; do not auto-promote draft-only, future-only, or unselected phases/goals; and when the whole active objective is complete, convert meaningful unselected successor work into a supported next-goal recommendation rather than silence.

Re-check mode when the user changes scope, corrects intent, provides evidence from another session, or shifts between behavior analysis and project execution. Move back to discussion mode only for real new ambiguity, design work, behavior/RULES analysis, or user direction. Do not let habit, ceremony, or milestone reporting reset execution mode.
---
## Trigger Model
| Trigger | Required behavior |
|---|---|
| explicit continue intent | preserve execution mode unless real stop gate exists |
| pasted logs/paths/snippets from another session | classify intent before project exploration |
| AI/RULES behavior question | stay discussion/governance unless project inspection is explicitly requested |
| unresolved startup gate | resolve startup posture before execution drift |
| oversized active governance entrypoint | compact/roll over current-state file before broad continuation |
| clear active phase/task path | continue rather than stop on narration |
| discoverable unfinished work | inspect execution surfaces and continue if safe |
| implementation completed but material verification remains | continue into the proportionate verification slice when safe, or state the blocker/not-applicable reason |
| phase-shaped follow-up | apply phase lineage handling before opening a new major phase and preserve visible phase linkage in created/extended task entries |
| active objective complete with meaningful unselected successor work | recommend the supported next goal with why, output, and gate without blocking selected safe continuation |
| broad/noisy next slice | apply worker routing before broad leader-session absorption |
| broad research/design-improvement next slice | decompose into research lanes or state a narrow direct-handling reason before leader raw websearch/source absorption |
| milestone-only pause drift | continue after reporting when safe |
| open concept/design/behavior work | stay in discussion mode |
| unresolved governing basis | ask for basis selection before deep execution |
| approval-sensitive step | stop for confirmation under stronger rule |
---
## Anti-Patterns
Avoid report-then-stop drift, phase-closure pause ritual, completion-without-roadmap when checked successor work is meaningful, unsupported next-goal recommendations, goal-framing pauses between selected safe slices, roadmap recommendations that block selected safe continuation, startup-gate bypass, oversized active-entrypoint bypass, execution inside open design/behavior discussion, project exploration from pasted paths alone, discussion inertia after the path is clear, user-choice theater for obvious safe continuation, waiting despite clear execution surfaces, stopping at edit-only implementation when material verification remains safe, new-major allocation by momentum, phase-shaped continuation tasks that hide their phase context, skipped worker routing, continuing into broad research as leader raw websearch by momentum, and treating teammate/Agent Team restriction as an all-subagent ban.
---
## Quality Metrics
| Metric | Target |
|---|---|
| Correct discussion-vs-execution classification | High |
| Intent recheck before project exploration | High |
| Unnecessary milestone-only pauses | Low |
| Continuous execution after clear next step | High |
| Completion-to-next-goal recommendation after actual objective completion | High when meaningful successor work exists and is not already selected for continuation |
| Continuation into material verification after implementation | High when safe and not blocked |
| Worker-routing gate respected before broad continuation | High |
| Research orchestration gate respected before broad research continuation | High |
| Visible phase linkage preserved during phase-shaped continuation | High |
| Execution during unresolved design/behavior discussion | 0 critical cases |
| Stop-gate correctness | High |
---
## Integration
Related rules:
- [development-verification-and-debug-strategy.md](development-verification-and-debug-strategy.md) - owns the proportionate verification/debug/TestKit strategy that execution continuity continues into when implementation is done but evidence remains pending
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - owns intent-first worker routing, subagent-first scale gating, research-lane orchestration, and leader-context control before broad leader-session absorption
- [authority-and-scope.md](authority-and-scope.md) - user authority and governing-basis ownership
- [accurate-communication.md](accurate-communication.md) - progress/blocker/completion wording
- [todo-standards.md](todo-standards.md) - live task list as execution surface
- [goal-set-review-and-priority-balance.md](goal-set-review-and-priority-balance.md) - goal-first working frame, goal hierarchy, triggered visibility, and next-goal recommendation boundaries
- [phase-implementation.md](phase-implementation.md) - active phase/task linkage, roadmap/phase-matrix semantics, phase-visible continuation tasks, and next-phase recommendation basis
- [functional-intent-verification.md](functional-intent-verification.md) - approval-sensitive gates
- [governed-document-rollover-control.md](governed-document-rollover-control.md) - daily-first rollover when active governance entrypoints are too large for safe continuation
---
