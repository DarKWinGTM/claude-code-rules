# Changelog - Memory Governance and Session Boundary

> **Parent Document:** [../memory-governance-and-session-boundary.md](../memory-governance-and-session-boundary.md)
> **Current Version:** 1.1
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-04-13 | **[Added optional extension recall boundary for memsearch-style layers](#version-11)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.0 | 2026-04-09 | **[Created first-class memory-governance-and-session-boundary rule chain](#version-10)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Created a new design/runtime/changelog triad that governs memory role boundaries, root `MEMORY.md` index behavior, `global/path/archive` taxonomy, path-primary applicability, session provenance, canonical `SCOPE.md`, and archive lifecycle | |

---

<a id="version-11"></a>
## Version 1.1: Added optional extension recall boundary for memsearch-style layers

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `memory-governance-and-session-boundary.md` from v1.0 to v1.1.
- Updated `design/memory-governance-and-session-boundary.design.md` from v1.0 to v1.1.
- Added an explicit optional-extension recall boundary so memsearch-like extension/plugin layers are treated as supplemental context bridges rather than required infrastructure or semantic truth.
- Added explicit deferral that coordination ownership for optional recall-layer usage lives in `shared-execution-coordination.md`.

### Summary
Memory-governance now keeps native memory authority boundaries explicit while modeling memsearch-style recall layers as optional supplemental context bridges rather than required core behavior.

---

<a id="version-10"></a>
## Version 1.0: Created first-class memory-governance-and-session-boundary rule chain

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Created `design/memory-governance-and-session-boundary.design.md` as the active target-state design for memory governance and session-boundary behavior.
- Created runtime `memory-governance-and-session-boundary.md` as a first-class rule defining:
  - memory role boundary relative to RULES, user instruction, and checked evidence
  - root `MEMORY.md` as an active index only
  - active memory taxonomy using `global/`, `path/`, and `archive/`
  - path as the primary applicability key
  - session IDs as provenance only
  - canonical `SCOPE.md` for path scopes
  - path matching and specificity rules
  - freshness / recheck behavior for memory-derived context
  - archive-inactive lifecycle semantics
- Positioned the chain as the semantic owner of memory applicability and memory organization behavior while keeping adjacent authority boundaries intact for:
  - `authority-and-scope.md`
  - `accurate-communication.md`
  - `evidence-grounded-burden-of-proof.md`
  - `answer-presentation.md`
- Explicitly kept actual live-memory migration out of the first governance wave so the repository defines the contract before reorganizing `/memory` contents.

### Summary
Created a first-class `memory-governance-and-session-boundary` rule chain so memory structure, path-vs-session applicability, root `MEMORY.md` behavior, and archive semantics now have one durable semantic authority instead of remaining scattered across compact/post-compact and authority-adjacent rules.
