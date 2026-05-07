# Goal-Set Review and Priority Balance

> **Current Version:** 1.1
> **Design:** [design/goal-set-review-and-priority-balance.design.md](design/goal-set-review-and-priority-balance.design.md) v1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/goal-set-review-and-priority-balance.changelog.md](changelog/goal-set-review-and-priority-balance.changelog.md)

---

## Rule Statement

**Core Principle: Keep the full active goal set visible and use goal-first working frames for non-trivial work so execution stays outcome-shaped without turning goal wording into a rigid visible ritual.**

This rule owns continuous goal-set review, priority balance, goal-first working frames, goal/output/gate semantics, goal hierarchy, triggered goal visibility, anti-fixation, anti-ritual boundaries, and evidence-grounded next-goal recommendations. It is not a reset ritual; it checks whether current work still serves the active objective set.

---

## Core Contract

### 1) Goal-set visibility and priority balance

When active work spans several primary goals, keep sibling goals visible enough that one subtask does not silently become the whole mission. Current focus must stay proportional: do not deepen one area merely because more detail is possible, and shift when progressing a neglected sibling goal has higher value.

Prefer main structure before subordinate polish unless a stronger blocker or user directive says otherwise. Establish the major structure, pipeline, skeleton, or governing shape first; treat micro-cleanup as secondary while core structure remains under-developed; do not let detail refinement substitute for unresolved architecture or pipeline work.

Review the active goal set when work stays in one area for several slices, micro-fixes accumulate, summaries repeatedly mention only one subgoal, several major goals remain open, or the user says the work is getting too granular. If the current subtask no longer serves the main objective set strongly enough, rebalance toward neglected primary goals.

### 2) Goal-first working frame

For non-trivial work, establish a working frame when it prevents drift, improves verification, or helps closeout:
- **Goal:** what outcome the work is trying to reach
- **Output:** what artifact, behavior, decision, or verified state should exist
- **Gate:** what proves the current goal is complete enough or ready to move forward

This frame may stay internal when the answer is simple or the active path is obvious. Make it visible only when the user would benefit from orientation, the work spans several steps/files/phases, verification depends on the target outcome, or closeout needs a supported next-goal recommendation.

### 3) Goal hierarchy

Use goal hierarchy to avoid confusing broad strategy with the current slice:
- `strategic goal`: broad system direction or long-term target
- `current goal`: active objective being executed now
- `execution goal`: concrete work slice currently being performed
- `verification goal`: evidence or gate that proves completion
- `next goal`: supported successor objective after true closeout

Do not promote a next goal into selected execution merely because it is recommended. User selection, checked roadmap authority, or selected safe continuation must still govern execution.

### 4) Triggered visibility and anti-ritual boundary

Goal framing is navigation, not ceremony. It should guide work, not create a mandatory visible block in every response.

Required guidance:
- do not force `Goal / Output / Gate` blocks into trivial answers, one-step lookups, or obvious safe continuation
- do not stop between already selected safe phases only to restate the goal
- do not use goal framing as a substitute for real design, phase, TODO, implementation, or verification evidence
- keep visible goal framing compact and decision-oriented when used
- preserve selected safe continuation as first-class behavior

### 5) Evidence-grounded next-goal recommendation

At true closeout, recommend a next goal only when checked design, phase, TODO, roadmap, or implementation evidence supports meaningful successor work. A useful next-goal recommendation names why this goal is supported, expected output, and completion gate. If the evidence is ambiguous or approval-sensitive, ask narrowly. If no supported next goal is visible, do not invent one.

---

## Trigger Model

| Trigger | Required behavior |
|---|---|
| non-trivial work begins | establish goal/output/gate when it prevents drift or improves verification |
| multi-step, multi-file, or phase-backed work | keep current goal, expected output, and completion gate clear enough to guide execution |
| single-goal overfocus | review whether sibling goals are neglected |
| micro-cleanup drift | rebalance toward structure-first work |
| user says work is too granular | perform goal review immediately |
| summaries mention only one area repeatedly | restore the full goal set in the decision frame |
| several major goals remain open | keep current focus proportional to the whole set |
| objective is truly complete | recommend only a supported next goal, or say none is selected/opened in checked scope |

---

## Anti-Patterns to Avoid

| Anti-pattern | Better behavior |
|---|---|
| A-only fixation | review the full goal set and rebalance |
| detail-first drift | return to structure-first progression |
| false progress by local refinement | measure progress against the full goal set |
| goal review as conversation restart | keep review compact and forward-moving |
| mandatory goal block in every simple answer | use visible goal framing only when it adds orientation or verification value |
| goal-setting pause between selected safe phases | continue selected work and keep the goal frame as navigation |
| unsupported next goal | recommend only from checked roadmap/goal evidence or report none visible |
| next-goal proposal treated as selected execution | keep it advisory until user or governed surfaces select it |

---

## Verification Checklist

- [ ] Non-trivial work has a current goal, expected output, and completion gate when that improves execution quality.
- [ ] Visible goal framing is triggered and proportional, not a rigid template.
- [ ] Goal hierarchy separates strategic/current/execution/verification/next goals.
- [ ] Selected safe continuation is not blocked by goal wording.
- [ ] Next-goal recommendations are grounded in checked design/TODO/phase/implementation evidence.
- [ ] Goal-set review still prevents single-subtask fixation and micro-detail drift.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Full active goal-set visibility | High |
| Goal/output/gate usefulness for non-trivial work | High |
| Single-subtask fixation incidents | Low |
| Structure-first priority balance | High |
| Micro-detail drift before core structure is clear | Low |
| Rigid visible goal-template incidents | Low |
| Unsupported next-goal recommendations | 0 critical cases |
| Goal review usefulness | High |

---

## Integration

Related rules:
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - selected continuation, goal-state continuity, and completion-to-roadmap stop/continue behavior
- [response-closing-and-action-framing.md](response-closing-and-action-framing.md) - supported next-goal recommendation shape at closeout
- [phase-implementation.md](phase-implementation.md) - active phase execution surface and phase roadmap goal/output/gate semantics
- [todo-standards.md](todo-standards.md) - live task entries as outcome/goal-shaped execution slices
- [tactical-strategic-programming.md](tactical-strategic-programming.md) - structure-first and strategic target framing
- [explanation-quality.md](explanation-quality.md) - easy-to-understand, proportional visible explanation of goal framing
- [answer-presentation.md](answer-presentation.md) - compact goal-aware presentation patterns
- [authority-and-scope.md](authority-and-scope.md) - user authority over the active objective set and advisory future goals
