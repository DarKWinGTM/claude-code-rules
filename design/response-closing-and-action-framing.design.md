# Response Closing and Action Framing Design

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-07)

---

## Current Target-State Refinement

This design now makes supported next-goal recommendations a first-class closeout shape, not only next-phase or next-wave recommendations. At true completion, the ending may name a recommended next phase, wave, or goal with a short evidence-backed reason, expected output, and completion gate.

The recommendation remains advisory unless user direction or governed execution surfaces select it. It must not interrupt selected safe continuation, and it must not invent future work when checked design/TODO/phase/roadmap/implementation evidence does not support a successor.

---

## 1) Goal

Define one first-class rule chain that owns how responses end: concise synthesis, clear next-action wording, recommendation-with-reason framing, alternative preservation, phase-backed delivery/impact closeout synthesis, roadmap-aware next recommendations and supported next-goal recommendations at true completion boundaries, optional deep-dive offers, closed-topic summary handling, and advisory proposal framing.

This chain should make endings easier to act on and make phase-backed closeouts show what the phase delivered, what improved, why it matters, and what meaningful next phase/wave/goal is recommended when checked roadmap surfaces support one, without replacing execution-mode ownership, authority ownership, evidence wording, phase roadmap ownership, or explanation-flow ownership.

---

## 2) Problem Statement

Observed failure modes:
- endings repeat prior detail instead of synthesizing the decision and implication
- the user must infer the preferred next move because several options are listed with no recommendation
- a real decision surface is hidden because one recommended option collapses all alternatives
- future-work ideas read like queued continuation instead of advisory proposals
- phase closeouts list checked files, task IDs, and audit status without explaining the delivered feature/improvement or practical impact
- true objective completion can end with no useful next recommendation even when phase/design/TODO surfaces show meaningful successor work
- easy-first answers can omit a compact path for deeper explanation even when the user may want detail after the short version
- already-closed topics keep returning in active summaries and blur the current issue

The repository needs one explicit owner for closing/action/proposal framing and phase-backed delivery/impact closeout synthesis so these ending behaviors stop being scattered across broader communication rules.

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

### 3.5 Phase-Backed Closeout Principle
When closing phase-backed work, the ending should state the delivered work, feature/improvement, user/system impact, verification basis, and next phase state when relevant before or alongside audit/checklist status.

### 3.6 Roadmap-Aware Completion Principle
When active work is genuinely complete and checked roadmap, design, TODO, phase, or implementation surfaces show meaningful unselected successor work, the ending should recommend the next phase, wave, or goal with why it is supported, expected output, and gate. This recommendation must not block selected safe continuation.

### 3.7 Goal-Qualified Proposal Principle
Future-work ideas outside the active objective should remain clearly advisory and specific enough to evaluate as proposals.

### 3.8 Optional Deep-Dive Offer Principle
When the default answer is intentionally easy-first and compact but a deeper explanation may help, the ending may include one short offer naming the specific topic to expand.

### 3.9 Boundary Principle
This chain owns **end-of-response action/proposal framing and phase-backed closeout synthesis** only.
It should not replace:
- execution-mode decision ownership
- user-authority/branch-choice ownership
- evidence-strength wording ownership
- explanation-flow ownership
- closing-block layout ownership
- phase roadmap/phase-matrix ownership

---

## 4) Application Model

Use this chain when:
- the response ends with synthesis, recommendation, or next-step guidance
- multiple next paths remain live and the user needs a visible preferred path plus alternatives
- a future-wave idea is being proposed outside the active objective
- a completed governed or phase-backed objective has meaningful unselected successor work visible in checked surfaces
- an easy-first answer should offer a specific optional deeper explanation path
- phase-backed work is being closed and the user needs to see what changed in practical terms
- resolved topics risk dominating the active summary

---

## 5) Examples

- "Recommended: do the design/phase sync first. Why this first: ... Other options: ..."
- "What this phase delivered: closeout reporting now explains the feature/improvement and impact before audit detail."
- "Proposal: build an automated visual QA verdict layer. Goal: ... Improvement: ... Output: ... Success condition: ..."
- "Recommended next: start P056 docs frontend implementation. Goal: render the locked OpenAPI contract through the docs UI. Output: React/Vite/Scalar package path. Gate: package/build scope selected."
- "ถ้าต้องการ ผมสามารถอธิบายละเอียดเพิ่มเรื่อง roadmap decision logic ต่อได้."
- "Phase 12 is already clear enough now. The next useful move is to switch from scope clarification to the implementation checklist."
- "There are 10 areas we should review in this state. I’ll show the full set first, then we can decide which subset to drill into."

---

## 6) Anti-Patterns

- summary repeats the whole answer
- recommendation omitted when one option is clearly better-supported
- alternatives hidden after recommendation
- future-wave idea phrased like implied queued execution
- objective completion with meaningful checked successor work but no recommendation
- next recommendation used as a blocker for already selected safe continuation
- optional deep-dive offer expanded into a full second explanation before the user selects it
- phase-backed closeout reduced to file/task/audit status only
- already-closed topics brought back into active summary by default

---

## 7) Success Criteria

This chain succeeds when:
- endings are shorter and more actionable without losing decision value
- recommendation-plus-reason behavior is explicit and consistent
- alternative paths remain visible when they still matter
- future-work ideas are clearly advisory
- true completion includes roadmap-aware next-phase/wave/goal recommendations when checked successor work is meaningful
- optional deep-dive offers give a specific path to more detail without bloating the first answer
- phase closeouts explain delivered feature/improvement and impact before audit-only detail
- resolved topics stop dominating active summaries by default

---

## 8) Integration

| Rule | Relationship |
|------|--------------|
| [../accurate-communication.md](../accurate-communication.md) | Keeps broader communication honesty and evidence-threshold wording outside closing-specific ownership |
| [execution-continuity-and-mode-selection.design.md](execution-continuity-and-mode-selection.design.md) | Owns real continue vs stop behavior and completion-to-roadmap bridge |
| [phase-implementation.design.md](phase-implementation.design.md) | Owns roadmap/phase-matrix semantics and next-phase states |
| [authority-and-scope.design.md](authority-and-scope.design.md) | Owns user authority and advisory-branch semantics |
| [explanation-quality.design.md](explanation-quality.design.md) | Owns explanation flow, easy-first depth, and stage/full-set reasoning logic |
| [answer-presentation.design.md](answer-presentation.design.md) | Owns layout/pattern shape of recommendation/next-stage/proposal/deep-dive blocks |

---

> Full history: [../changelog/response-closing-and-action-framing.changelog.md](../changelog/response-closing-and-action-framing.changelog.md)
