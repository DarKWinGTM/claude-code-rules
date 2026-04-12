# Phase 037-01 - Refine handoff request vs execution layer

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 037-01
> **Status:** Completed
> **Design References:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/handoff-request-vs-receiving-phase-boundary.patch.md](../patch/handoff-request-vs-receiving-phase-boundary.patch.md)

---

## Objective

Refine RULES so cross-session handoff tasks use request-layer naming and keep receiving-side phase ownership distinct.

## Why this phase exists

The current coordination owner already models lease and handoff, but handoff titles can still leak sender phase labels into receiving-side work, which creates phase-owner ambiguity. This phase closes that gap.

## Entry conditions / prerequisites

- `shared-execution-coordination` already exists as the first-class coordination owner
- the refinement remains bounded to handoff naming / remap semantics rather than opening another new owner chain
- the governed patch artifact for this wave is already established

## Action points / execution checklist

- [x] update `shared-execution-coordination` as the primary owner
- [x] update `todo-standards` as the task-board naming companion
- [x] update `phase-implementation` as the receiving-side phase companion
- [x] update `project-documentation-standards` as the repository-model companion
- [x] keep sender phase out of the default visible handoff title model
- [x] preserve source trace in handoff notes rather than default title prefixes

## Out of scope

- changing the underlying task-system UI
- forcing every task into one rigid naming format regardless of whether it is shared or session-specific
- activating `claude-peers-mcp`

## Affected artifacts

- `shared-execution-coordination.md`
- `todo-standards.md`
- `phase-implementation.md`
- `project-documentation-standards.md`
- touched design/changelog companions for those chains
- bounded patch and phase artifacts for wave `037`

## Verification

- [x] request-layer naming is distinct from execution-layer remap
- [x] receiving-side phase ownership is explicit
- [x] handoff notes are the preferred place for source trace when needed
- [x] touched companion owners reinforce the same boundary coherently

## Risks / rollback notes

- wording could become too rigid and block useful shorthand for obviously local tasks
- rollback should narrow the naming rule before removing the request-vs-execution distinction entirely
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `037-02` sync master docs and runtime install parity

## Exit criteria

- [x] sender phase leakage into default handoff titles is explicitly discouraged
- [x] receiver-side phase ownership is explicit enough to remove the main ambiguity
- [x] the refinement remains bounded to handoff naming/remap behavior
