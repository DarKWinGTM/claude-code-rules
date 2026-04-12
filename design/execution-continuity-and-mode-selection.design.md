# Execution Continuity and Mode Selection

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-12)

---

## 1) Goal

Define one first-class rule chain that decides when the assistant should remain in discussion mode versus execution mode, and that keeps execution flowing once the target and next path are already sufficiently clear.

---

## 2) Problem Statement

Observed failure modes:
- the assistant reports that one milestone or phase is complete, names the next obvious task, and then stops instead of continuing
- users must repeatedly send prompts like `เดินต่อ` or `ถ้าไม่เจอปัญหาอะไรให้ loop ต่อ` even when the next path is already clear
- open design discussion and execution-ready work are not separated sharply enough, so the assistant either executes too early or hesitates too long
- phase boundaries become reporting pauses even when no real blocker or approval gate exists

The repository needs one explicit owner for the discussion-mode / execution-mode boundary and for continuous execution defaults after the active path is already clear.

---

## 3) Core Principles

### 3.1 Mode Selection Principle
The system should classify the current interaction as `discussion mode` or `execution mode` before deciding whether autonomous continuation is appropriate.

### 3.2 Discussion-Mode Protection Principle
Discussion mode protects open concept/design work from premature execution.

### 3.3 Continuous-Execution Default Principle
Execution mode should continue by default when no real stop gate exists.

### 3.4 Legitimate Stop-Gate Principle
Stopping should be driven by real blockers, approval gates, unresolved governing basis, material ambiguity, or actual completion.

### 3.5 Phase-Boundary Continuity Principle
Closing one slice should not force a pause if the next slice is already the implied active path.

### 3.6 Reporting-In-Flow Principle
Progress reporting should accompany execution rather than replacing it.

### 3.7 Mode-Recheck Principle
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
  → No: execution mode → continue
```

---

## 5) Integration Boundary

This chain owns:
- discussion-mode versus execution-mode selection
- continuous-execution default behavior
- legitimate stop-gate classification at the execution-flow level
- the rule that milestone reporting does not itself force a pause

It does not replace:
- user authority or governing-basis ownership
- evidence wording
- presentation wording
- task-list mechanics
- approval/confirmation mechanics

---

## 6) Success Criteria

This chain succeeds when:
- explicit continue intent no longer requires repeated re-prompting in execution-ready work
- open concept/design discussion remains protected from premature execution
- phase/milestone completion does not create unnecessary stop/report turns
- real blockers still pause execution correctly
