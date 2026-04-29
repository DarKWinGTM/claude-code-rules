# Response Closing and Action Framing

> **Current Version:** 1.1
> **Design:** [design/response-closing-and-action-framing.design.md](design/response-closing-and-action-framing.design.md) v1.1
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/response-closing-and-action-framing.changelog.md](changelog/response-closing-and-action-framing.changelog.md)

---

## Rule Statement

**Core Principle: Close responses with concise synthesis, clear action framing, preserved decision visibility, phase-backed delivery/impact closeouts, and explicitly advisory proposal wording.**

This chain owns end-of-response synthesis, next-action framing, recommendation-with-reason wording, alternative preservation, phase-backed closeout synthesis, closed-topic summary behavior, and goal-qualified advisory proposal framing. It does not replace execution-mode, user-authority, explanation-flow, evidence wording, or layout ownership.

---

## Core Principles

### 1) Concise Synthesis Principle

At the end of an analytical, implementation-heavy, or status-heavy response, prefer synthesis over repetition.

Required guidance:
- keep final summaries concise, high-signal, and decision-oriented
- do not impose a rigid sentence cap; use only enough wording to preserve meaning
- when older fixed work is mentioned, label it as historical or previously resolved instead of active

### 2) Clear Next-Action Principle

If a clear next action exists and the user genuinely needs to know it, state it directly.

Required guidance:
- present options only when user choice materially affects the path
- keep recommendation wording evidence-backed, not arbitrary
- do not invent extra options when the active objective can safely continue

### 3) Recommendation-With-Reason Principle

When one option is better-supported, name it first and add one short reason.

Required guidance:
- use `Recommended` / `Why this first` wording when it improves clarity
- preserve at least one real alternative when multiple reasonable next actions remain open
- do not collapse a real decision surface into one path without saying so

### 4) Closed-Topic Presentation Principle

Previously resolved topics may support reasoning, but they should not dominate the visible ending once the active issue has moved on.

Required guidance:
- summarize still-active or decision-relevant issues first
- mention resolved topics only when they materially affect the current blocker, contrast, or decision
- avoid repeating already-closed items across later summaries by inertia

### 5) Phase-Backed Closeout Principle

When closing phase-backed work, explain what the phase delivered before or alongside audit/checklist status.

Required guidance:
- state what the phase developed, improved, enabled, or locked
- name the feature, capability, behavior, or governance improvement that changed
- explain the user/system impact in practical terms
- state the verification basis at the evidence strength actually checked
- state next phase state when relevant: not started, draft/planned, selected, active, or no next phase opened
- keep the closeout compact; do not force this shape onto trivial non-phase completions

### 6) Goal-Qualified Proposal Principle

Future-work ideas must stay clearly advisory unless the user selects them.

A useful proposal states:
- concrete goal
- expected improvement or change
- expected output or user-visible result
- success condition when it clarifies what done means

Required guidance:
- label future work as a `Proposal`, `Idea`, or `Future wave`
- avoid continuation-shaped wording such as `next do X` when the user has not selected that target
- do not present a proposal if no concrete goal or output can be stated

### 7) Boundary Principle

This chain owns how a response closes and frames action/proposals. It does not replace:
- `execution-continuity-and-mode-selection.md` for real continue-vs-stop behavior
- `authority-and-scope.md` for user authority and advisory-option boundaries
- `accurate-communication.md` for evidence-strength and verification-state wording
- `explanation-quality.md` for explanation flow, stage progression, and full-set logic
- `answer-presentation.md` for layout/pattern shape

---

## Preferred Shapes

Phase-backed closeout:

```text
What this phase delivered
- <plain-language delivery statement>
Feature / Improvement
- <feature, capability, behavior, or governance improvement>
Impact
- <user/system impact>
Verification
- <checked evidence; avoid stronger wording than verified>
Next phase state
- <not started | draft/planned | selected | active | none opened>
```

Recommendation:

```text
Recommended: do the design/phase sync first.
Why this first: the current phase records still describe older authority, so syncing them reduces confusion before execution.
Other options:
- go straight to implementation now
- pause after the current source-only update
```

Advisory proposal:

```text
Proposal: build an automated visual QA verdict layer.
Goal: turn screenshot compare output into an easier review result.
Improvement: reduce manual interpretation of raw screenshots/diffs.
Output: a machine-readable QA summary with concise regression notes.
Success condition: compare runs end with a usable verdict artifact.
```

---

## Anti-Patterns to Avoid

| Anti-pattern | Better approach |
|---|---|
| summary repeats the whole answer | synthesize conclusion and implication only |
| options listed with no recommendation when one path is clearly stronger | name the recommendation and why first |
| real multi-path state hidden behind one recommendation | preserve a visible alternative |
| future work with no concrete goal/output | do not present it as a serious proposal |
| proposal phrased like queued execution | mark it advisory until selected |
| phase closeout lists only files/tasks/audit status | state delivered feature/improvement, impact, verification, and next phase state |
| already-closed topics dominate the active summary | keep resolved items in context only |

---

## Quality Metrics

| Metric | Target |
|---|---|
| Closing signal density | High |
| Recommendation clarity | High |
| Alternative preservation when paths remain live | High |
| Proposal advisory clarity | High |
| Phase-backed delivery/impact closeout clarity | High |
| Closed-topic summary discipline | High |

---

## Integration

Related rules:
- [accurate-communication.md](accurate-communication.md) - broader evidence-threshold wording
- [execution-continuity-and-mode-selection.md](execution-continuity-and-mode-selection.md) - real continue-vs-stop behavior
- [authority-and-scope.md](authority-and-scope.md) - user authority and advisory-option semantics
- [explanation-quality.md](explanation-quality.md) - explanation flow and stage/full-set logic
- [answer-presentation.md](answer-presentation.md) - layout patterns for recommendations and proposals

---
