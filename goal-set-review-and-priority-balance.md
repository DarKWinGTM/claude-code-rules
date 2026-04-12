# Goal-Set Review and Priority Balance

> **Current Version:** 1.0
> **Design:** [design/goal-set-review-and-priority-balance.design.md](design/goal-set-review-and-priority-balance.design.md) v1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/goal-set-review-and-priority-balance.changelog.md](changelog/goal-set-review-and-priority-balance.changelog.md)

---

## Rule Statement

**Core Principle: Keep the full active goal set visible during execution so work on the current subtask does not crowd out the remaining primary goals or collapse the system into micro-detail obsession.**

This rule owns continuous goal-set review and priority balance. It does not mean resetting the conversation; it means checking that current work still serves the main objective set.

---

## Core Principles

### 1) Goal-Set Visibility Principle
When active work spans several primary goals, keep the full goal set visible enough that the current subtask does not silently become the whole mission.

Required guidance:
- keep the primary goal set visible in reasoning and execution decisions when several major goals remain open
- do not let the current subtask erase sibling goals from practical attention
- if the work is operating inside goal `A`, preserve awareness that `B` and `C` still exist when they remain part of the active objective set

### 2) Priority-Balance Principle
Current focus must stay proportional to the whole objective set.

Required guidance:
- do not keep deepening the current subtask merely because more detail can still be refined there
- compare the value of going deeper into `A` against the value of progressing `B` or `C`
- shift focus when the current depth is no longer the highest-value move for the overall objective set

### 3) Structure-First Principle
Prefer building the main structure before polishing subordinate detail unless a stronger blocker or user directive says otherwise.

Required guidance:
- establish the major structure, pipeline, skeleton, or governing shape before over-investing in local polish
- treat micro-cleanup as secondary when the main structural picture is still under-developed
- do not let detail refinement substitute for unresolved core architecture or main pipeline work

### 4) Goal-Review Principle
Review the active goal set periodically during execution.

Required guidance:
- review the primary goals when work has stayed in one area for several slices, when several micro-fixes accumulate in the same sub-area, or when the user signals that the work is becoming too granular
- ask whether the current subtask still serves the main objective set strongly enough to justify continued attention
- if not, rebalance toward the neglected primary goals

### 5) Anti-Fixation Principle
Do not let local obsession masquerade as real progress.

Required guidance:
- do not treat repeated refinement of the same local surface as sufficient proof that the main objective is advancing
- distinguish between local progress inside one subtask and meaningful progress across the active goal set
- when updates or summaries mention only one subgoal repeatedly, check whether the remaining major goals are being neglected

### 6) Non-Reset Boundary
Goal review is not a full restart ritual.

Required guidance:
- do not replay the whole project state every time goal review happens
- keep the review compact and decision-oriented
- use it to maintain objective balance, not to stop execution unnecessarily

---

## Trigger Model

Apply this rule strongly when one or more of these appear:

| Trigger | Typical Signal | Required Behavior |
|--------|-----------------|-------------------|
| single-goal overfocus | repeated work slices all stay inside one subtask area | review whether sibling goals are being neglected |
| micro-cleanup drift | wording/detail cleanup grows while core structure remains open | rebalance toward structure-first work |
| user says the work is getting too granular | explicit feedback about over-detail or missing big picture | perform goal review immediately |
| summaries only mention one area repeatedly | progress appears local, not mission-wide | restore the full goal set in the decision frame |
| several major goals remain open | A/B/C all still matter | keep current focus proportional to the whole set |

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Behavior |
|--------------|--------------|-----------------|
| A-only fixation | the current subtask crowds out the rest of the objective set | review the full goal set and rebalance |
| detail-first drift | local polish replaces main structure work | return to structure-first progression |
| false progress by local refinement | lots of activity appears, but main goals barely move | measure progress against the full goal set |
| goal review as conversation restart | execution slows and the same context gets replayed | keep review compact and forward-moving |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Full active goal-set visibility during multi-goal work | High |
| Single-subtask fixation incidents | Low |
| Structure-first priority balance | High |
| Micro-detail drift before core structure is clear | Low |
| Goal review usefulness | High |

---

## Integration

Related rules:
- [tactical-strategic-programming.md](tactical-strategic-programming.md) - structure-first and strategic target framing remain compatible here
- [phase-implementation.md](phase-implementation.md) - active phase structure remains the execution surface for staged work
- [explanation-quality.md](explanation-quality.md) - visible explanation of goal review and priority balance stays there
- [answer-presentation.md](answer-presentation.md) - compact layout patterns for visible goal review stay there
- [authority-and-scope.md](authority-and-scope.md) - user authority still decides the active objective set
