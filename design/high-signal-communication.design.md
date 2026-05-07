# High Signal Communication

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-07)

---

## Current Target-State Refinement

This design now protects useful goal/output/gate framing and supported next-goal recommendations from over-pruning. High-signal filtering should remove surplus wording, but it must not remove content that prevents non-trivial goal drift, clarifies expected output or completion gate, or gives a supported next-goal recommendation at true completion.

Goal framing remains proportional: the pruning pass should also remove rigid or repeated goal blocks when they do not directly improve understanding, decision, verification, continuation, or closeout.

---

## 1) Goal

Define a bounded high-signal communication rule that tightens response quality by removing low-value extra content and repeated wording without displacing existing communication, explanation, presentation, goal-aware framing, roadmap/next-goal recommendation, or optional deep-dive-offer owners.

The purpose is to improve signal density while preserving:
- natural tone
- easy-to-follow explanation
- useful options when they are still needed
- useful goal/output/gate framing and roadmap-aware next-goal recommendations when checked completion surfaces support them
- optional deeper-detail offers when an easy-first answer should stay compact but expandable
- the existing active owner boundaries

---

## 2) Role Boundary

The active RULES system already has owners for:
- communication wording
- explanation flow
- presentation shape
- natural professional tone
- roadmap-aware completion recommendations
- optional deep-dive offers

So this rule should remain supplementary rather than turning into a replacement owner.

It exists to add a narrow response-tightening layer where excess wording, repetition, or unnecessary expansion is the real problem.

---

## 3) Allowed Scope

This rule may add only supplementary mechanisms that do not override the existing active owners.

Allowed scope:
- extra-content admission filtering
- repetition pruning after the main answer is already present
- protection against over-pruning content that an active owner still requires

Out of scope:
- tone ownership
- main-point-first ownership
- plain-language-first explanation ownership
- option/recommendation ownership
- roadmap-aware completion and next-goal recommendation ownership
- optional deep-dive-offer ownership
- phase/progress explanation ownership

---

## 4) Supplementary Mechanisms

### 4.1 Extra-Content Admission Gate
Keep a sentence, list, example, option, roadmap recommendation, optional deep-dive offer, or next-step block only when it directly answers the user, prevents likely misunderstanding, changes the next action/decision, reports a real checked result, is supported by checked successor-work evidence, or is still required by an active owner.

### 4.2 Repetition Pruning Pass
Before final output, remove repeated restatement, repeated conclusion wording, and duplicated next-step phrasing when one clear synthesis already covers the same meaning. This pass removes repetition only; it must not strip a goal-qualified roadmap recommendation after true completion or a useful one-line optional deep-dive offer.

---

## 5) Protection Boundary

This rule must not:
- reduce an answer below the level needed for understanding
- strip content that an existing active owner still requires
- prune roadmap-aware next recommendations when checked completion surfaces make them materially useful
- prune optional deep-dive offers when an easy-first answer should remain compact but expandable
- turn into a blanket pressure toward ultra-short answers
- replace the current owner graph

If there is a conflict about whether content is still required, the existing active owner wins.

---

## 6) Evaluation Questions

This rule is useful only if it improves signal density without making answers harder to use.

Check whether responses become:
- less repetitive
- less fluffy
- still natural
- still understandable

Failure signals:
- answers become too dry or machine-like
- answers become too compressed to understand
- useful explanation or next-step content gets removed
- roadmap-aware recommendations disappear after true completion despite checked successor work
- optional deep-dive offers expand into a second full answer instead of staying compact
- the rule starts duplicating existing owner behavior

---

## 7) Status

- status: active
- install status: part of the active runtime rule set
- refinement posture: may continue to evolve as a bounded supplementary rule without requiring standalone experimental framing