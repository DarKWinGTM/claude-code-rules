# Goal-Set Review and Priority Balance

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-07)

---

## Current Target-State Refinement

This design now treats goal awareness as an execution navigation layer rather than a rigid visible template. For non-trivial work, the active behavior should establish the current goal, expected output, and completion gate when that prevents drift, improves verification, or supports a closeout recommendation.

The goal hierarchy is strategic goal → current goal → execution goal → verification goal → next goal. Visible goal framing is triggered only when it improves orientation, multi-step execution, verification, or true-closeout clarity. At true completion, next-goal recommendations must be grounded in checked design, phase, TODO, roadmap, or implementation evidence; unsupported future work stays unclaimed.

---

## 1) Goal

Define one first-class rule chain that keeps the full active goal set visible and establishes proportional goal-first working frames for non-trivial work so execution stays outcome-shaped without becoming a rigid visible ritual.

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
