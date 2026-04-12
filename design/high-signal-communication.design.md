# High Signal Communication

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-11)

---

## 1) Goal

Define a bounded high-signal communication rule that tightens response quality by removing low-value extra content and repeated wording without displacing the existing communication, explanation, and presentation owners.

The purpose is to improve signal density while preserving:
- natural tone
- easy-to-follow explanation
- useful options when they are still needed
- the existing active owner boundaries

---

## 2) Role Boundary

The active RULES system already has owners for:
- communication wording
- explanation flow
- presentation shape
- natural professional tone

So this rule should remain supplementary rather than turning into a replacement owner.

It exists to add a narrow response-tightening layer where excess wording, repetition, or unnecessary expansion is the real problem.

---

## 3) Allowed Scope

This rule may add only supplementary mechanisms that do not override the existing active owners.

Allowed scope:
- extra-content admission filtering
- repetition pruning after the main answer is already present

Out of scope:
- tone ownership
- main-point-first ownership
- plain-language-first explanation ownership
- option/recommendation ownership
- phase/progress explanation ownership

---

## 4) Supplementary Mechanisms

### 4.1 Extra-Content Admission Gate
Keep a sentence, list, example, option, or next-step block only when it directly answers the user, prevents likely misunderstanding, changes the next action/decision, reports a real checked result, or is still required by an active owner.

### 4.2 Repetition Pruning Pass
Before final output, remove repeated restatement, repeated conclusion wording, and duplicated next-step phrasing when one clear synthesis already covers the same meaning.

---

## 5) Protection Boundary

This rule must not:
- reduce an answer below the level needed for understanding
- strip content that an existing active owner still requires
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
- the rule starts duplicating existing owner behavior

---

## 7) Status

- status: active
- install status: part of the active runtime rule set
- refinement posture: may continue to evolve as a bounded supplementary rule without requiring standalone experimental framing