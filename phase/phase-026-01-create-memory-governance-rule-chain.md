# Phase 026-01 - Create memory governance rule chain

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 026-01
> **Status:** In Progress
> **Design References:** [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md)
> **Patch References:** [../patch/memory-governance-and-session-boundary.patch.md](../patch/memory-governance-and-session-boundary.patch.md)

---

## Objective

Create the first-class rule chain that owns memory governance and session-boundary behavior.

## Why this phase exists

The current RULES stack already has useful compact/post-compact and RULES-first-over-memory guardrails, but it does not yet have one semantic owner for memory applicability, root `MEMORY.md`, path-scoped memory, session provenance, and archive lifecycle. This phase closes that ownership gap before any actual `/memory` migration happens.

## Entry conditions / prerequisites

- the user explicitly wants RULES to define memory behavior before reorganizing real memory files
- the first wave remains governance-only and does not yet migrate live memory contents
- existing compact/post-compact and RULES-first-over-memory waves remain precedent inputs rather than edit targets

## Action points / execution checklist

- [x] create `design/memory-governance-and-session-boundary.design.md`
- [x] create runtime `memory-governance-and-session-boundary.md`
- [x] create `changelog/memory-governance-and-session-boundary.changelog.md`
- [x] create `patch/memory-governance-and-session-boundary.patch.md`
- [x] keep the new chain bounded to memory governance and session-boundary semantics
- [x] keep actual live-memory migration out of this phase

## Out of scope

- modifying live memory files under `~/.claude/projects/.../memory/`
- rewriting the current live `MEMORY.md`
- creating real `global/`, `path/`, or `archive/` directories in the live memory root
- creating live `SCOPE.md` files in the current memory directory

## Affected artifacts

- `design/memory-governance-and-session-boundary.design.md`
- `memory-governance-and-session-boundary.md`
- `changelog/memory-governance-and-session-boundary.changelog.md`
- `patch/memory-governance-and-session-boundary.patch.md`

## TODO coordination

- do not claim actual memory reorganization yet
- record this wave as governance-definition work only after sync is complete

## Changelog coordination

- add per-chain changelog authority for the new chain
- add one repository-level master changelog entry after integration and sync complete

## Verification

- [x] new design file exists
- [x] runtime rule exists
- [x] changelog authority exists
- [x] patch artifact exists
- [x] chain scope is distinct from authority, communication, burden-of-proof, and presentation owners
- [x] the phase remains governance-only and does not yet migrate live memory contents

## Risks / rollback notes

- the new chain could over-scope if it restates wording/evidence/layout ownership already held elsewhere
- rollback should narrow the chain rather than silently erasing the governance history
- preserve the bounded wave history even if later migration design changes

## Next possible phases

- `026-02` integrate companion owners narrowly
- `026-03` sync master docs and runtime install parity
- `026-04` run postflight memory-governance audit

## Exit criteria

- [x] one first-class chain now owns memory governance and session-boundary semantics
- [x] the implementation remains a bounded governance wave rather than an immediate live-memory migration
- [x] the patch/design/runtime/changelog triad is coherent
