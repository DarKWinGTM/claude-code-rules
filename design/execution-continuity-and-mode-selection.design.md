# Execution Continuity and Mode Selection

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.8
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-03)

---

## 1) Goal

Define one first-class rule chain that decides when the assistant should remain in discussion mode versus execution mode, keeps execution flowing by default once the active path is genuinely execution-ready, does not let execution continuity bypass startup artifact governance, and does not let broad continuation bypass native worker routing.

---

## 2) Problem Statement

Observed failure modes:
- the assistant reports that one milestone or phase is complete, names the next obvious task, and then stops instead of continuing
- users must repeatedly send prompts like `เดินต่อ` or `ถ้าไม่เจอปัญหาอะไรให้ loop ต่อ` even when the next path is already clear
- execution-ready work may still stall because the assistant waits for the user to restate the next unfinished slice even though phase/TODO/task/design/checked implementation surfaces already reveal it
- open design discussion and execution-ready work are not separated sharply enough, so the assistant either executes too early or hesitates too long
- phase boundaries become reporting pauses even when no real blocker or approval gate exists
- execution-continuity wording can be overread as permission to keep moving even when startup artifact posture is still unresolved for meaningful governed work
- execution momentum can push the leader session into broad raw search/read/log/test absorption without first applying worker routing

The repository needs one explicit owner for the discussion-mode / execution-mode boundary and for continuous execution defaults after the active path is already clear.

---

## 3) Core Principles

### 3.1 Mode Selection Principle
The system should classify the current interaction as `discussion mode` or `execution mode` before deciding whether autonomous continuation is appropriate.

### 3.2 Discussion-Mode Protection Principle
Discussion mode protects open concept/design work from premature execution.

### 3.3 Startup-Gate-First Principle
Execution readiness should not be treated as permission to bypass unresolved startup artifact posture.

### 3.4 Continuous-Execution Default Principle
Execution mode should continue by default when no real stop gate exists and startup posture is already resolved enough for the active governed slice.

### 3.5 Active Next-Work Discovery Principle
Execution mode should actively inspect the current execution surfaces to discover the next unfinished slice when the task list alone does not already make it obvious.

### 3.6 Capture-Before-Continue Boundary
Execution continuity should not outrun required knowledge capture when external docs/specs/provider references have just produced implementation-critical knowledge that later governed execution still depends on.

### 3.7 Worker-Routing-Before-Broad-Continue Principle
Execution continuity should not make broad, noisy, context-heavy, high-output, multi-surface, or naturally parallel next work default to leader-session raw absorption. Those slices should pass through `native-worker-agent-routing-and-context-control.md` unless direct handling has a narrow reason.

### 3.8 Legitimate Stop-Gate Principle
Stopping should be driven by real blockers, approval gates, unresolved governing basis, material ambiguity, actual completion, or a required knowledge-capture gate.

### 3.9 Phase-Boundary Continuity Principle
Closing one slice should not force a pause if the next slice is already the implied active path.

### 3.10 Reporting-In-Flow Principle
Progress reporting should accompany execution rather than replacing it.

### 3.11 Mode-Recheck Principle
The system should re-check mode when the decision surface materially changes, but not let ceremony or milestone narration reset execution mode by default.

---

## 4) Decision Model

```text
Current interaction
  ↓
Is the user still shaping concept/design/choice?
  → Yes: discussion mode
  → No: continue
  ↓
Are goal, scope, and next execution order sufficiently clear?
  → No: discussion mode / clarification
  → Yes: continue
  ↓
Is a real stop gate active?
  → Yes: stop for blocker/approval/basis/ambiguity/completion
  → No: continue
  ↓
Is the next slice broad/noisy/context-heavy/multi-surface/high-output/parallelizable?
  → Yes: apply native worker routing, then continue on selected path
  → No: execution mode → continue directly
```

---

## 5) Integration Boundary

This chain owns:
- discussion-mode versus execution-mode selection
- continuous-execution default behavior
- active next-work discovery from current execution surfaces once execution mode is already active
- legitimate stop-gate classification at the execution-flow level
- the rule that milestone reporting does not itself force a pause

It does not replace:
- startup artifact governance
- user authority or governing-basis ownership
- evidence wording
- presentation wording
- task-list mechanics
- approval/confirmation mechanics
- native worker routing and leader-context control, which defer to `native-worker-agent-routing-and-context-control.md`
- shared-board, plugin, and external coordination/runtime mechanics, including any discontinued custom recall/skill paths, which stay outside Main RULES scope

---

## 6) Success Criteria

This chain succeeds when:
- explicit continue intent no longer requires repeated re-prompting in execution-ready work
- execution-ready work can discover the next unfinished slice from task/phase/TODO/design/checked-state surfaces when that path is already visible
- open concept/design discussion remains protected from premature execution
- phase/milestone completion does not create unnecessary stop/report turns
- broad or high-output continuation applies worker routing before leader raw absorption
- real blockers still pause execution correctly
