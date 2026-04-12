# Goal-Set Review and Priority Balance

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-12)

---

## 1) Goal

Define one first-class rule chain that keeps the full active goal set visible during execution so the assistant does not become fixated on the current subtask and lose balance across the remaining primary goals.

---

## 2) Problem Statement

Observed failure modes:
- work on goal `A` deepens repeatedly while goals `B` and `C` receive little or no attention
- local cleanup or wording refinement expands even when the main structural picture is still under-developed
- summaries show lots of activity in one sub-area, but overall progress across the full goal set is weak
- the assistant behaves as if the current subtask is the whole mission instead of one component inside a larger objective set

The repository needs one explicit owner for continuous goal-set review and priority balance so current work stays proportional to the whole mission.

---

## 3) Core Principles

### 3.1 Goal-Set Visibility Principle
Primary goals should remain visible when several major goals are still open.

### 3.2 Priority-Balance Principle
Current focus should stay proportional to the total objective set rather than drifting into single-subtask obsession.

### 3.3 Structure-First Principle
Main structure, main pipeline, and core objective shape should generally come before micro-polish.

### 3.4 Goal-Review Principle
The system should review the full goal set periodically during execution, especially when repeated work slices stay in one area.

### 3.5 Anti-Fixation Principle
Local refinement should not be mistaken for mission-level progress.

### 3.6 Non-Reset Boundary
Goal review should be compact and forward-moving, not a full restart ritual.

---

## 4) Success Criteria

This chain succeeds when:
- the assistant no longer over-focuses on goal `A` while neglecting `B` and `C`
- structure-first execution remains visible during multi-goal work
- goal review helps rebalance attention without causing unnecessary pause or replay
- progress is measured against the whole objective set rather than only the current local task
