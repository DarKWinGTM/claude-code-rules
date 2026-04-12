# Phase 038-01 - Refine shared-board visibility, retention, and memsearch

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 038-01
> **Status:** Completed
> **Design References:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md)
> **Patch References:** [../patch/shared-board-visibility-retention-and-memsearch-refinement.patch.md](../patch/shared-board-visibility-retention-and-memsearch-refinement.patch.md)

---

## Objective

Refine the remaining visibility, lifecycle, retention, and optional memsearch operating details of the shared execution coordination model.

## Why this phase exists

The core coordination framework already exists, but several practical operating details still needed to become explicit: how session-held work should be visible on the board, how the handoff lifecycle should be described, how retention should vary by task class/state, and how optional memsearch should be used without becoming authority.

## Entry conditions / prerequisites

- `shared-execution-coordination` already exists as the first-class coordination owner
- handoff request vs receiving-phase boundary already exists
- the refinement remains bounded to visibility/lifecycle/retention/memsearch details rather than opening another new owner chain

## Action points / execution checklist

- [x] update `shared-execution-coordination` with visible session identity guidance
- [x] update `shared-execution-coordination` with explicit handoff lifecycle states
- [x] update `shared-execution-coordination` with a clearer retention matrix principle
- [x] update `shared-execution-coordination` with deeper optional memsearch operating guidance
- [x] update `todo-standards` as the task-board visibility companion
- [x] update `memory-governance-and-session-boundary` as the optional recall companion

## Out of scope

- activating `claude-peers-mcp`
- changing runtime rule count
- replacing the existing coordination owner with a new owner chain

## Affected artifacts

- `shared-execution-coordination.md`
- `todo-standards.md`
- `memory-governance-and-session-boundary.md`
- touched design/changelog companions for those chains
- bounded patch and phase artifacts for wave `038`

## Verification

- [x] session-held work visibility is clearer
- [x] handoff lifecycle states are more explicit
- [x] retention depends more explicitly on task class/state
- [x] memsearch remains optional and supplemental
- [x] the refinement stayed inside the existing coordination/memory/task-board owner set

## Risks / rollback notes

- wording could become too ceremonial if it over-specifies visible naming beyond what the board can realistically maintain
- rollback should narrow operating detail before removing it entirely
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `038-02` sync master docs and runtime install parity

## Exit criteria

- [x] shared-board operating detail is materially clearer than before
- [x] optional memsearch use is clearer without becoming mandatory
- [x] the refinement remains bounded to the existing owner set
