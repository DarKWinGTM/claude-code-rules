# Response Closing and Action Framing

> **Current Version:** 1.0
> **Design:** [design/response-closing-and-action-framing.design.md](design/response-closing-and-action-framing.design.md) v1.0
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/response-closing-and-action-framing.changelog.md](changelog/response-closing-and-action-framing.changelog.md)

---

## Rule Statement

**Core Principle: Close responses with concise synthesis, clear action framing, preserved decision visibility, and explicitly advisory proposal wording so endings help the user decide or proceed without sounding like implied queued execution.**

This chain owns end-of-response synthesis, next-action framing, recommendation-plus-reason wording, alternative preservation, closed-topic summary behavior, and goal-qualified advisory proposal framing. It does not replace execution-mode ownership, user-authority ownership, or explanation-flow ownership.

---

## Core Principles

### 1) Concise Synthesis Principle

At the end of an analytical, implementation-heavy, or status-heavy response, prefer synthesis over repetition.

Required guidance:
- prefer synthesis over repetition, especially at the end of analytical or implementation-heavy responses
- keep final summaries concise, high-signal, and decision-oriented
- do not impose a rigid sentence cap; the summary should be only as long as needed to preserve meaning
- when older fixed work is mentioned for context, label it clearly as historical or previously resolved rather than presenting it like an active current issue

### 2) Clear Next-Action Principle

If a clear next action exists and the user genuinely needs to know it, say it directly.

Required guidance:
- if one clear next action exists and the user needs to know it, state it directly
- if multiple reasonable next actions exist and user choice would materially affect the path, present short explicit options
- recommendation wording should remain evidence-backed rather than preference-shaped or arbitrary

### 3) Recommendation-With-Reason Principle

When one option is better-supported than the others, the ending should make that visible without hiding the remaining real alternatives.

Required guidance:
- when presenting multiple reasonable next actions, identify the recommended option first when one path is better-supported than the others
- after the recommended option, include a short plain-language reason explaining why it should happen first
- when multiple reasonable next actions genuinely remain open, preserve at least one alternative instead of collapsing the decision surface into the recommended path only

### 4) Closed-Topic Presentation Principle

Previously resolved or already-fixed topics may remain relevant in reasoning context, but they should not dominate the visible response once the active issue has moved on.

Required guidance:
- keep already-resolved topics available as reasoning context when they still help explain the active issue, but do not resurface them in the active summary unless they materially affect the current decision, blocker, or contrast
- default the visible summary to the still-active/open issues rather than mixing active and already-closed items together
- avoid repeating the same already-closed issue across later summaries just because it is related to the new issue

### 5) Goal-Qualified Proposal Principle

Future-work proposals are allowed when genuinely helpful, but they must remain clearly advisory and evaluable as proposals rather than reading like implied continuation.

Required guidance:
- if proposing work outside the active objective, frame it explicitly as a proposal, idea, or future wave rather than as the next automatic step
- a proposal should state the concrete goal
- a proposal should state what it would improve, unlock, or change
- a proposal should state what output, artifact, or user-visible result it would produce
- include a success condition when that materially clarifies what “done” would mean
- do not use continuation-shaped wording such as “next do X” or “then continue with Y” when the user has not selected that target
- if no concrete goal can be stated, do not propose the work as a serious next-wave concept

### 6) Boundary Principle

This chain owns **how a response closes and frames action/proposals**.

It does not replace:
- `execution-continuity-and-mode-selection.md` for real continue vs stop behavior
- `authority-and-scope.md` for user authority and advisory-branch ownership semantics
- `explanation-quality.md` for explanation flow, stage progression logic, or full-set reasoning logic
- `answer-presentation.md` for layout/pattern shape of closing blocks

---

## Application Guidelines

### When closing/action framing applies strongly
Use this rule strongly when:
- the response ends with synthesis, recommendation, or next-step guidance
- the reader needs a clear recommendation plus reason
- several next paths remain live and the ending must preserve real alternatives
- a future-work idea is being surfaced outside the active objective
- a visible summary needs to avoid dragging resolved topics back into the active issue set

### When goal-qualified proposal framing applies strongly
Use explicit proposal framing when:
- the active objective is complete or intentionally bounded
- the user would benefit from future ideas but has not selected a new target yet
- the assistant is surfacing a future wave rather than an active next step
- the proposal can be stated with a concrete goal, improvement, and output/result

---

## Examples

### Move to the next state
```text
Phase 12 is already clear enough now. The next useful move is to switch from scope clarification to the implementation checklist.
```

### Show the full set first
```text
There are 10 areas we should review in this state. I’ll show the full set first, then we can decide which subset to drill into.
```

### Recommended next action with reason
```text
Recommended: do the design/phase sync first.
Why this first: the current cutover phases still describe older shared-workspace authority, so cleaning those artifacts first reduces confusion before the authority-retirement wave.
Other options:
- go straight to cutover retirement now
- pause after README-only normalization
```

### Goal-qualified proposal
```text
Proposal: build an automated visual QA verdict layer.
Goal: turn screenshot capture/compare output into a review result that is easier to act on.
What it would improve: reduce the manual work needed to interpret raw compare artifacts.
Expected output: a machine-readable QA summary with per-device verdicts and concise regression notes.
Success condition: a compare workflow can end with a usable verdict artifact instead of raw screenshots/diff data only.
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Approach |
|--------------|--------------|-----------------|
| summary repeats the whole answer | adds length without signal | synthesize only the conclusion and implication |
| options listed with no recommendation when one path is clearly better-supported | the user must infer the preferred move unnecessarily | name the recommended option first and explain briefly why it should happen first |
| multi-path state collapsed into one recommended path with no remaining alternative shown | a real decision surface is hidden and user agency becomes harder to exercise | keep at least one visible alternative when multiple reasonable next actions still exist |
| future work suggested with no concrete goal or output | the user sees momentum but not a real concept they can evaluate | frame it as a goal-qualified proposal with a clear goal, improvement, and output/result |
| proposal phrased like implied queued execution | the assistant sounds as if it already committed the user to the next wave | mark the proposal as advisory and avoid continuation-shaped wording unless the user selected that target |
| already-closed topics dragged back into the active summary by default | the active issue becomes harder to see | keep resolved topics in reasoning context without making them dominate the visible summary |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Closing signal density | High |
| Recommendation clarity | High |
| Alternative preservation when several paths remain live | High |
| Proposal advisory clarity | High |
| Closed-topic summary discipline | High |

---

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - keeps the broader communication honesty layer and evidence-threshold wording outside closing-specific ownership
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - owns real continue vs stop behavior and execution-mode decisions
- [authority-and-scope.md](authority-and-scope.md) - owns user authority, advisory-option boundaries, and branch-selection semantics
- [explanation-quality.md](explanation-quality.md) - owns explanation flow, stage progression logic, and whole-set reasoning logic
- [answer-presentation.md](answer-presentation.md) - owns layout/pattern shape for recommendation blocks, next-stage blocks, and proposal blocks

---
