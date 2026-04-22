# Phase 070-01 - Refine task language pattern

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 070-01
> **Status:** Completed
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Design References:** [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/task-language-pattern-refinement.patch.md](../patch/task-language-pattern-refinement.patch.md)

---

## Objective

Refine the existing owner set so Task List wording follows the actual active session language pattern more explicitly.

## Why this phase exists

The current RULES doctrine already says task wording should align with the active session language/register, but that wording is still loose enough that detached generic phrasing can slip back in.
This wave closes that gap without turning the rule into a rigid monolingual policy:
- Thai-led sessions should produce Thai-led task wording by default
- naturally mixed Thai+English sessions should keep that mix
- technical labels should stay in technical form when forced translation would reduce clarity
- the rule should follow the real session language pattern, not an artificial ratio or forced translation policy

## Action points / execution checklist

- [x] refine `todo-standards` so task wording follows the actual active session language pattern more explicitly
- [x] refine `phase-implementation` so phase-linked task wording follows the same actual active session language pattern
- [x] keep naturally mixed Thai+English wording allowed instead of forcing one language
- [x] keep technical labels in technical form when forced translation would reduce clarity
- [x] synchronize master/history surfaces for the bounded wave

## Verification

- [x] active Task List wording guidance now follows the actual active session language pattern more explicitly
- [x] Thai-led session usage now maps to Thai-led task wording by default
- [x] naturally mixed Thai+English wording remains allowed when that matches the real session pattern
- [x] technical labels may remain untranslated when that reads more naturally
- [x] touched master/history surfaces record the wave coherently

## Exit criteria

- [x] the owner set now expresses actual-session-language-pattern task wording without inventing a new doctrine chain
- [x] task wording no longer depends on a vague `align naturally` phrasing alone when the session pattern is already clear
