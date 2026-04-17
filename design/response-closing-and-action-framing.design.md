# Response Closing and Action Framing Design

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662 (2026-04-17)

---

## 1) Goal

Define one first-class rule chain that owns how responses end: concise synthesis, clear next-action wording, recommendation-with-reason framing, alternative preservation, closed-topic summary handling, and advisory goal-qualified proposal framing.

This chain should make endings easier to act on without replacing execution-mode ownership, authority ownership, or explanation-flow ownership.

---

## 2) Problem Statement

Observed failure modes:
- endings repeat prior detail instead of synthesizing the decision and implication
- the user must infer the preferred next move because several options are listed with no recommendation
- a real decision surface is hidden because one recommended option collapses all alternatives
- future-work ideas read like queued continuation instead of advisory proposals
- already-closed topics keep returning in active summaries and blur the current issue

The repository needs one explicit owner for closing/action/proposal framing so these ending behaviors stop being scattered across broader communication rules.

---

## 3) Core Principles

### 3.1 Concise Synthesis Principle
The ending should synthesize rather than repeat.

### 3.2 Clear Next-Action Principle
If a clear next action exists and the user genuinely needs it, the ending should say it directly.

### 3.3 Recommendation-With-Reason Principle
When one option is better-supported than the others, the response should make that visible without hiding the remaining live alternatives.

### 3.4 Closed-Topic Presentation Principle
Resolved topics may remain in reasoning context, but should not dominate the visible summary once the active issue has moved on.

### 3.5 Goal-Qualified Proposal Principle
Future-work ideas outside the active objective should remain clearly advisory and specific enough to evaluate as proposals.

### 3.6 Boundary Principle
This chain owns **end-of-response action/proposal framing** only.
It should not replace:
- execution-mode decision ownership
- user-authority/branch-choice ownership
- explanation-flow ownership
- closing-block layout ownership

---

## 4) Application Model

Use this chain when:
- the response ends with synthesis, recommendation, or next-step guidance
- multiple next paths remain live and the user needs a visible preferred path plus alternatives
- a future-wave idea is being proposed outside the active objective
- resolved topics risk dominating the active summary

---

## 5) Examples

- "Recommended: do the design/phase sync first. Why this first: ... Other options: ..."
- "Proposal: build an automated visual QA verdict layer. Goal: ... Improvement: ... Output: ... Success condition: ..."
- "Phase 12 is already clear enough now. The next useful move is to switch from scope clarification to the implementation checklist."
- "There are 10 areas we should review in this state. I’ll show the full set first, then we can decide which subset to drill into."

---

## 6) Anti-Patterns

- summary repeats the whole answer
- recommendation omitted when one option is clearly better-supported
- alternatives hidden after recommendation
- future-wave idea phrased like implied queued execution
- already-closed topics brought back into active summary by default

---

## 7) Success Criteria

This chain succeeds when:
- endings are shorter and more actionable without losing decision value
- recommendation-plus-reason behavior is explicit and consistent
- alternative paths remain visible when they still matter
- future-work ideas are clearly advisory
- resolved topics stop dominating active summaries by default

---

## 8) Integration

| Rule | Relationship |
|------|--------------|
| [../accurate-communication.md](../accurate-communication.md) | Keeps broader communication honesty and evidence-threshold wording outside closing-specific ownership |
| [execution-continuity-and-mode-selection.design.md](execution-continuity-and-mode-selection.design.md) | Owns real continue vs stop behavior |
| [authority-and-scope.design.md](authority-and-scope.design.md) | Owns user authority and advisory-branch semantics |
| [explanation-quality.design.md](explanation-quality.design.md) | Owns explanation flow and stage/full-set reasoning logic |
| [answer-presentation.design.md](answer-presentation.design.md) | Owns layout/pattern shape of recommendation/next-stage/proposal blocks |

---

> Full history: [../changelog/response-closing-and-action-framing.changelog.md](../changelog/response-closing-and-action-framing.changelog.md)
