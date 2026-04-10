# Memory Governance and Session Boundary Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** In Progress
> **Target Design:** [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md) v1.0
> **Target Rule:** [../memory-governance-and-session-boundary.md](../memory-governance-and-session-boundary.md)
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/memory-governance-and-session-boundary.changelog.md](../changelog/memory-governance-and-session-boundary.changelog.md)

---

## 1) Context

This patch captures the introduction of a first-class rule chain for memory governance and session-boundary behavior.

Why this change matters:
- the repository already has compact/post-compact caution and a RULES-first-over-memory boundary, but memory governance itself is still distributed and implicit
- the user wants RULES to define how memory works before any actual `/memory` reorganization happens
- the current memory model needs one semantic owner for root `MEMORY.md`, path-vs-session applicability, `global/path/archive` separation, and archive lifecycle

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../authority-and-scope.md`
- `../accurate-communication.md`
- `../evidence-grounded-burden-of-proof.md`
- `../answer-presentation.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the new chain should define memory applicability and organization clearly without re-owning adjacent communication/evidence/layout concerns
- the first wave should define the contract without prematurely migrating actual live memory files under `~/.claude/projects/.../memory/`

---

## 3) Change Items

### Change Item 1
- **Target location:** RULES runtime inventory
- **Change type:** additive

**Before**
```text
Memory governance behavior is distributed across authority, communication, burden-of-proof, and compact/post-compact refinements, but no first-class chain owns memory applicability, `MEMORY.md`, path-scoped memory, session provenance, or archive semantics directly.
```

**After**
```text
A dedicated first-class rule chain owns memory governance and session-boundary behavior, including root `MEMORY.md` index behavior, `global/path/archive` taxonomy, path-primary applicability, session-provenance-only semantics, canonical `SCOPE.md`, and archive lifecycle.
```

### Change Item 2
- **Target location:** memory applicability model
- **Change type:** additive

**Before**
```text
Current adjacent rules imply that stale carried-forward detail must be rechecked, but they do not yet define what makes a memory applicable to later work or how path-scoped memory differs from session provenance.
```

**After**
```text
The new chain defines:
- path as the primary applicability key
- session IDs as provenance only
- default path matching / specificity behavior
- archive as inactive-by-default memory
- root `MEMORY.md` as an active index only
```

### Change Item 3
- **Target location:** first governance wave scope boundary
- **Change type:** additive

**Before**
```text
No governed boundary exists yet between defining the memory contract and physically reorganizing live project memory files.
```

**After**
```text
The first wave explicitly defines governance only. Actual migration/reorganization of live `/memory` contents is deferred to a later wave after the contract exists.
```

### Change Item 4
- **Target location:** adjacent-chain integration
- **Change type:** additive

**Before**
```text
Adjacent chains already constrain memory-related wording and authority edges, but they do not defer a dedicated memory-governance workflow to one owner.
```

**After**
```text
Adjacent chains retain their own authority while the new chain becomes the semantic owner of memory applicability and memory organization behavior.
```

---

## 4) Verification

- [ ] Confirm the design/runtime/changelog triad exists for the new chain
- [ ] Confirm the rule defines root `MEMORY.md` as an active index only
- [ ] Confirm the rule defines `global/`, `path/`, and `archive/`
- [ ] Confirm the rule makes path the primary applicability key and session IDs provenance only
- [ ] Confirm the rule requires canonical `SCOPE.md` for path scopes
- [ ] Confirm the rule keeps archive inactive by default
- [ ] Confirm adjacent chains retain their own authority boundaries
- [ ] Confirm the patch remains readable as a before/after governance artifact

---

## 5) Rollback Approach

If the chain proves redundant or over-scoped:
- narrow the chain to memory applicability and root index behavior only
- preserve the triad and patch history rather than silently deleting the ownership experiment
- revert any adjacent-chain integration wording that overstates the new chain’s scope
- do not revert to a state where actual memory reorganization happens without one explicit governing contract for memory scope and lifecycle
