# Phase 066-01 - Refine task list phase context and session language

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 066-01
> **Status:** Completed
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Design References:** [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/task-list-phase-context-and-session-language-refinement.patch.md](../patch/task-list-phase-context-and-session-language-refinement.patch.md)

---

## Objective

Refine the existing owner set so Task List creation aligns more strongly to Phase structure and follows the active session language/register more naturally.

## Why this phase exists

The current RULES already support current-phase-first behavior when an active phase exists, but still leave two practical gaps:
- task creation can become too generic when the work is clearly phase-shaped even before the exact next phase file exists
- task wording can drift into detached generic phrasing instead of following the current session language context

## Action points / execution checklist

- [x] refine `todo-standards` so task creation aligns to active phase or clearly implied staged/phase context
- [x] refine `todo-standards` so task wording aligns with active session language/register
- [x] refine `phase-implementation` so phase-linked task creation can follow clearly implied staged context before the exact next phase file exists
- [x] refine `phase-implementation` so phase-linked task wording still follows session language naturally
- [x] refine `project-documentation-standards` so the repo model reinforces phase-shaped task creation
- [x] synchronize master/history surfaces for the bounded wave

## Verification

- [x] task-list rules now recognize clearly implied staged/phase context instead of depending only on an already-open exact phase file
- [x] active-phase-first behavior still remains intact when an active phase already exists
- [x] task wording now has an explicit session-language alignment rule
- [x] touched master/history surfaces record the wave coherently

## Exit criteria

- [x] the owner set now expresses stronger phase-related task creation without inventing a new doctrine chain
- [x] session-language task wording is explicit without widening the owner set into a separate coordination doctrine
