# Phase 039-02 - Sync universal task ownership surfaces

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 039-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/universal-session-owned-task-title-grammar.patch.md](../patch/universal-session-owned-task-title-grammar.patch.md)

---

## Objective

Synchronize the master RULES surfaces and installed runtime copies after the universal session-owned task title grammar refinement.

## Why this phase exists

The ownership-grammar refinement only becomes operationally real when the inventories, README, TODO, changelog, phase summary, and installed runtime copies all reflect the same universal visible-ownership model.

## Entry conditions / prerequisites

- `039-01` is complete and the touched owner chains are already updated
- the bounded patch artifact for this wave already exists
- the active runtime rule count should remain unchanged at 40

## Action points / execution checklist

- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `changelog/changelog.md`
- [x] update `TODO.md`
- [x] update `phase/SUMMARY.md`
- [x] reinstall touched runtime rules into `~/.claude/rules/`
- [x] parity-check source/install alignment
- [x] complete postflight review before release

## Out of scope

- changing runtime rule count
- changing task-list internals or UI behavior
- activating `claude-peers-mcp`
- creating another new owner chain

## Affected artifacts

- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for the touched rules

## Verification

- [x] master surfaces record wave `039` coherently
- [x] touched rule descriptions show universal visible session ownership and state-specific task-title grammar clearly
- [x] installed runtime files match source for the touched rules
- [x] postflight review confirms the refinement remains bounded to the current owner set

## Risks / rollback notes

- sync drift can survive even when the semantic wording is correct
- rollback should restore prior master/runtime state only if the wave itself is intentionally reverted
- preserve wave history instead of silently erasing the refinement wave

## Next possible phases

- none required once sync/parity/review/release are complete

## Exit criteria

- [x] repository-level governance reflects the universal task-ownership refinement coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `039` phase family is visible and reviewable from `phase/SUMMARY.md`
