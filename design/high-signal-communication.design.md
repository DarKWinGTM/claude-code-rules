# High Signal Communication

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-11)

---

## 1) Goal

Create a standalone experimental rule that can be evaluated separately from the active communication-owner set.

The purpose is to test whether a small set of supplementary high-signal filters improves response usefulness without damaging:
- natural tone
- easy-to-follow explanation
- useful options
- existing active owner boundaries

---

## 2) Why This Stays Separate

The active RULES system already has owners for:
- communication wording
- explanation flow
- presentation shape
- natural professional tone

So this experiment should not duplicate those owners.

It should remain separate because:
- the effect is not yet certain
- the user wants to observe behavior before merging anything into the active rule graph
- a separate rule is easier to revise or discard without destabilizing working rules

---

## 3) Allowed Experimental Scope

This experiment may add only supplementary mechanisms that are not already owned directly by the active rules.

Initial allowed scope:
- extra-content admission filtering
- post-draft pruning of repeated or low-value material
- bounded expansion control after the core answer is already clear

Out of scope:
- tone ownership
- main-point-first ownership
- plain-language-first explanation ownership
- option/recommendation ownership
- phase/progress explanation ownership

---

## 4) Experimental Mechanisms

### 4.1 Extra-Content Admission Gate
A sentence or block should stay only if it earns its place by improving understanding, actionability, or correctness.

### 4.2 Post-Draft Pruning Pass
After drafting, repeated or low-value parts should be pruned before final output.

### 4.3 Expansion Budget Gate
After the core answer is clear, extra elaboration should be bounded rather than growing by habit.

---

## 5) Evaluation Questions

The experiment is useful only if it improves responses without flattening them.

Check whether responses become:
- more direct
- less repetitive
- less ceremonious
- less likely to over-expand
- still natural
- still understandable
- still willing to offer useful next moves when genuinely needed

Failure signals:
- answers become too dry or machine-like
- answers stop offering helpful options even when useful
- answers become too compressed to understand
- the experiment starts duplicating existing owner behavior

---

## 6) Merge Boundary

Do not merge this into the active rules unless testing shows a clear positive effect and the extracted pieces can be assigned cleanly to the correct existing owners.
