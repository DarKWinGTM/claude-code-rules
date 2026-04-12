# Phase 038-02 - Sync shared-board operating-detail surfaces

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 038-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md)
> **Patch References:** [../patch/shared-board-visibility-retention-and-memsearch-refinement.patch.md](../patch/shared-board-visibility-retention-and-memsearch-refinement.patch.md)

---

## Objective

Synchronize master RULES surfaces and installed runtime copies after the shared-board operating-detail refinement.

## Why this phase exists

The operating-detail refinement only becomes operationally real when the inventories, README, TODO, changelog, phase summary, and installed runtime copies all reflect the same improved session-visible / lifecycle / retention / optional-memsearch model.

## Entry conditions / prerequisites

- `038-01` is complete and the touched owner chains are already updated
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

- activating `claude-peers-mcp`
- changing runtime rule count
- creating another new owner chain

## Affected artifacts

- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for the touched rules

## Verification

- [x] master surfaces record wave `038` coherently
- [x] touched rule descriptions show clearer session-held visibility, lifecycle, retention, and optional memsearch guidance
- [x] installed runtime files match source for the touched rules
- [x] postflight review confirms the refinement remains bounded to the current owner set

## Risks / rollback notes

- sync drift can survive even when semantic wording is correct
- rollback should restore prior master/runtime state only if the wave itself is intentionally reverted
- preserve wave history instead of silently erasing the refinement wave

## Next possible phases

- none required once sync/parity/review/release are complete

## Exit criteria

- [x] repository-level governance reflects the operating-detail refinement coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `038` phase family is visible and reviewable from `phase/SUMMARY.md`
