# Goal-Set Review and Priority Balance

> **Current Version:** 1.0
> **Design:** [design/goal-set-review-and-priority-balance.design.md](design/goal-set-review-and-priority-balance.design.md) v1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/goal-set-review-and-priority-balance.changelog.md](changelog/goal-set-review-and-priority-balance.changelog.md)

---

## Rule Statement

**Core Principle: Keep the full active goal set visible during execution so the current subtask does not crowd out remaining primary goals or collapse the system into micro-detail obsession.**

This rule owns continuous goal-set review and priority balance. It is not a reset ritual; it checks whether current work still serves the active objective set.

---

## Core Contract

When active work spans several primary goals, keep sibling goals visible enough that one subtask does not silently become the whole mission. Current focus must stay proportional: do not deepen one area merely because more detail is possible, and shift when progressing a neglected sibling goal has higher value.

Prefer main structure before subordinate polish unless a stronger blocker or user directive says otherwise. Establish the major structure, pipeline, skeleton, or governing shape first; treat micro-cleanup as secondary while core structure remains under-developed; do not let detail refinement substitute for unresolved architecture or pipeline work.

Review the active goal set when work stays in one area for several slices, micro-fixes accumulate, summaries repeatedly mention only one subgoal, several major goals remain open, or the user says the work is getting too granular. If the current subtask no longer serves the main objective set strongly enough, rebalance toward neglected primary goals.

Goal review should stay compact and decision-oriented. Anti-fixation remains mandatory: do not replay the whole project state, stop execution unnecessarily, or let local progress masquerade as mission-wide progress.

---

## Trigger Model

| Trigger | Required behavior |
|---|---|
| single-goal overfocus | review whether sibling goals are neglected |
| micro-cleanup drift | rebalance toward structure-first work |
| user says work is too granular | perform goal review immediately |
| summaries mention only one area repeatedly | restore the full goal set in the decision frame |
| several major goals remain open | keep current focus proportional to the whole set |

---

## Anti-Patterns to Avoid

| Anti-pattern | Better behavior |
|---|---|
| A-only fixation | review the full goal set and rebalance |
| detail-first drift | return to structure-first progression |
| false progress by local refinement | measure progress against the full goal set |
| goal review as conversation restart | keep review compact and forward-moving |

---

## Quality Metrics

| Metric | Target |
|---|---|
| Full active goal-set visibility | High |
| Single-subtask fixation incidents | Low |
| Structure-first priority balance | High |
| Micro-detail drift before core structure is clear | Low |
| Goal review usefulness | High |

---

## Integration

Related rules:
- [tactical-strategic-programming.md](tactical-strategic-programming.md) - structure-first and strategic target framing
- [phase-implementation.md](phase-implementation.md) - active phase execution surface
- [explanation-quality.md](explanation-quality.md) - visible explanation of goal review
- [answer-presentation.md](answer-presentation.md) - compact goal-review layout
- [authority-and-scope.md](authority-and-scope.md) - user authority over the active objective set
