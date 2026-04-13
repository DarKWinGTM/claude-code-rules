# Phase 039-01 - Refine universal session-owned task title grammar

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 039-01
> **Status:** Completed
> **Design References:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/universal-session-owned-task-title-grammar.patch.md](../patch/universal-session-owned-task-title-grammar.patch.md)

---

## Objective

Refine RULES so visible session ownership becomes the default board-facing standard for session-owned task-list work, while keeping request, held, and blocked states semantically distinct.

## Why this phase exists

The current coordination model already improved visible session identity for shared execution boards, but the user identified a remaining gap: the ownership grammar still reads too much like a special multi-session mode instead of a generally useful standard. This phase closes that gap without collapsing all states into one ambiguous title form.

## Entry conditions / prerequisites

- `shared-execution-coordination` already exists as the first-class coordination owner
- visible session identity, lifecycle, and retention semantics already exist from wave `038`
- the refinement remains bounded to universal visible ownership and session-state title grammar rather than opening another new owner chain

## Action points / execution checklist

- [x] update `shared-execution-coordination` as the primary ownership/grammar owner
- [x] update `todo-standards` as the live task-board companion
- [x] update `phase-implementation` as the phase-linked execution companion
- [x] update `project-documentation-standards` as the repository-model companion
- [x] keep request-layer, held-owner, and blocked-owner task-title forms semantically distinct
- [x] make visible session ownership standard regardless of whether the task list is currently shared by one session or several

## Out of scope

- changing Claude Code task-list internals or UI behavior
- forcing one exact string such as `For <session-id> owner:` across every task state
- creating another first-class owner chain
- activating `claude-peers-mcp`

## Affected artifacts

- `shared-execution-coordination.md`
- `todo-standards.md`
- `phase-implementation.md`
- `project-documentation-standards.md`
- touched design/changelog companions for those chains
- bounded patch and phase artifacts for wave `039`

## Verification

- [x] visible session ownership is now expressed as a default board-facing standard for session-owned work
- [x] request, held, and blocked title forms remain semantically distinct
- [x] request-layer naming remains distinct from receiving-side execution-layer phase structure
- [x] phase-linked execution work now prefers held-owner forms once the task is already locally owned
- [x] the refinement stayed inside the existing coordination/task-board/phase/repository-model owner set

## Risks / rollback notes

- wording could become too rigid if it over-prescribes exact title shapes beyond what the board can maintain comfortably
- rollback should narrow title-form prescriptions before weakening universal visible ownership itself
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `039-02` sync master docs and runtime install parity

## Exit criteria

- [x] visible session ownership is standard enough to apply across usage modes
- [x] request vs held vs blocked state meaning remains readable from the title grammar
- [x] the refinement remains bounded to the current owner set
