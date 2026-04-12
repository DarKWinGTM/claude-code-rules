# Phase 036-02 - Integrate coordination companions and sync

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 036-02
> **Status:** Completed
> **Design References:** [../design/design.md](../design/design.md), [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md)
> **Patch References:** [../patch/shared-execution-coordination.patch.md](../patch/shared-execution-coordination.patch.md)

---

## Objective

Integrate bounded companion deferrals, sync master governance surfaces, reinstall touched runtime rules, and close the new coordination-owner wave.

## Why this phase exists

The new coordination owner only becomes operationally real when the touched companion chains defer correctly, the master surfaces record the new wave coherently, and the installed runtime copies reflect the touched rule set.

## Entry conditions / prerequisites

- `036-01` is complete and the new coordination owner triad already exists
- the bounded patch artifact for this wave already exists
- the active runtime rule count should increase from 39 to 40 after the new chain is added to master surfaces and install lists

## Action points / execution checklist

- [x] update touched companion rule chains with bounded deferrals
- [x] update touched companion designs/changelogs
- [x] update `design/design.md`
- [x] update `README.md`
- [x] update `TODO.md`
- [x] update `changelog/changelog.md`
- [x] update `phase/SUMMARY.md`
- [x] reinstall touched runtime rules into `~/.claude/rules/`
- [x] parity-check source/install alignment
- [x] complete postflight review before release

## Out of scope

- activating `claude-peers-mcp` in active RULES behavior
- making memsearch required for the framework to function
- replacing the existing narrow owners with the new coordination owner

## Affected artifacts

- touched runtime/design/changelog companions
- `design/design.md`
- `README.md`
- `TODO.md`
- `changelog/changelog.md`
- `phase/SUMMARY.md`
- installed runtime copies for the touched rules

## Verification

- [x] companion rules still keep their original narrow roles
- [x] companion rules defer coordination protocol details to the new owner coherently
- [x] master surfaces record wave `036` coherently
- [x] install lists now include the 40th active runtime rule
- [x] installed runtime files match source for the touched rules
- [x] postflight review confirms no blocker-level ownership regression

## Risks / rollback notes

- sync drift can survive even when the new owner is semantically correct
- ownership wording may become too broad if companion deferrals are not bounded carefully
- rollback should restore prior master/runtime state only if the wave itself is intentionally reverted

## Next possible phases

- none required once sync/parity/review/release are complete

## Exit criteria

- [x] repository-level governance reflects the new coordination owner coherently
- [x] runtime install parity is restored for all touched rules
- [x] the `036` phase family is visible and reviewable from `phase/SUMMARY.md`
