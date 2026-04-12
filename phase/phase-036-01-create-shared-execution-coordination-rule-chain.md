# Phase 036-01 - Create shared execution coordination rule chain

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 036-01
> **Status:** Completed
> **Design References:** [../design/shared-execution-coordination.design.md](../design/shared-execution-coordination.design.md)
> **Patch References:** [../patch/shared-execution-coordination.patch.md](../patch/shared-execution-coordination.patch.md)

---

## Objective

Create one first-class RULES owner for shared multi-session execution coordination.

## Why this phase exists

The current RULES already contain useful task-list, phase, execution-continuity, repository-model, and memory-governance pieces, but the shared coordination protocol itself is still scattered. This phase creates one explicit owner without destroying the existing narrower owners.

## Entry conditions / prerequisites

- same-objective task-list continuity already exists
- next-work discovery from execution surfaces already exists
- the new work should stay bounded to coordination ownership rather than replacing existing tracking/phase/memory owners
- the governed patch artifact for this wave is already established

## Action points / execution checklist

- [x] create `shared-execution-coordination.md`
- [x] create `design/shared-execution-coordination.design.md`
- [x] create `changelog/shared-execution-coordination.changelog.md`
- [x] define shared-board vs semantic-truth boundary
- [x] define session lease / handoff / retention / aging / anti-overclear semantics
- [x] define optional memsearch support and future-optional `claude-peers-mcp` boundary

## Out of scope

- activating `claude-peers-mcp` as a current required runtime dependency
- replacing the existing task / phase / execution / memory owners
- changing undocumented internal task-system capabilities

## Affected artifacts

- `shared-execution-coordination.md`
- `design/shared-execution-coordination.design.md`
- `changelog/shared-execution-coordination.changelog.md`
- bounded patch and phase artifacts for wave `036`

## Verification

- [x] the new chain exists as a full governed triad
- [x] shared-board semantics are explicit
- [x] session lease / handoff semantics are explicit
- [x] retention / aging / anti-overclear semantics are explicit
- [x] memsearch is modeled as optional support, not required infrastructure
- [x] `claude-peers-mcp` remains future-optional only

## Risks / rollback notes

- the new chain could become too broad and swallow narrower owners if not kept bounded
- rollback should narrow ownership before removing the chain entirely
- preserve the bounded wave history instead of silently erasing it

## Next possible phases

- `036-02` integrate companion coordination deferrals and sync master/runtime surfaces

## Exit criteria

- [x] one first-class coordination owner exists
- [x] the owner remains bounded rather than super-rule shaped
- [x] optional memsearch / future-optional peer-messaging boundaries are explicit
