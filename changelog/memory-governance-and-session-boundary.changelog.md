# Changelog - Memory Governance and Session Boundary

> **Parent Document:** [../memory-governance-and-session-boundary.md](../memory-governance-and-session-boundary.md)
> **Current Version:** 1.5
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.5 | 2026-04-17 | **[Retired memsearch-specific naming in favor of generic optional external recall wording](#version-15)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 1.4 | 2026-04-17 | **[Reduced memory-governance memsearch wording to global optional-recall doctrine only](#version-14)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.3 | 2026-04-13 | **[Added optional-recall availability check and immediate fallback guidance](#version-13)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.2 | 2026-04-13 | **[Clarified how optional recall extensions should be used after stronger execution surfaces](#version-12)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.1 | 2026-04-13 | **[Added optional extension recall boundary for memsearch-style layers](#version-11)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.0 | 2026-04-09 | **[Created first-class memory-governance-and-session-boundary rule chain](#version-10)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Created a new design/runtime/changelog triad that governs memory role boundaries, root `MEMORY.md` index behavior, `global/path/archive` taxonomy, path-primary applicability, session provenance, canonical `SCOPE.md`, and archive lifecycle | |

---

<a id="version-15"></a>
## Version 1.5: Retired memsearch-specific naming in favor of generic optional external recall wording

**Date:** 2026-04-17
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `memory-governance-and-session-boundary.md` from v1.4 to v1.5.
- Updated `design/memory-governance-and-session-boundary.design.md` from v1.4 to v1.5.
- Replaced remaining memsearch-specific naming with generic optional external recall wording.
- Removed the last defer line that still pointed active memory-governance recall behavior at `shared-execution-coordination.md`.
- Preserved the fallback-safe, supplemental-only recall boundary without implying a Main RULES-managed custom-skill path.

### Summary
Memory-governance now describes optional external recall generically, without teaching memsearch-specific custom-skill doctrine inside Main RULES.

---

<a id="version-14"></a>
## Version 1.4: Reduced memory-governance memsearch wording to global optional-recall doctrine only

**Date:** 2026-04-17
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Removed shared-board-specific memsearch intake/fallback wording from `memory-governance-and-session-boundary.md`.
- Kept only the global optional-recall boundary where memsearch-style layers remain supplemental and subordinate to stronger checked execution evidence.
- Removed shared-board-specific memsearch semantics from Main RULES memory-governance active doctrine.

### Summary
Memory-governance now keeps only the global/general optional-recall doctrine, while shared-board-specific memsearch semantics move to the coordination package source rule.

---

<a id="version-13"></a>
## Version 1.3: Added optional-recall availability check and immediate fallback guidance

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `memory-governance-and-session-boundary.md` from v1.2 to v1.3.
- Updated `design/memory-governance-and-session-boundary.design.md` from v1.2 to v1.3.
- Added explicit guidance that receive-side optional recall should check extension availability instead of assuming plugin presence from prior sessions or prior machines.
- Added explicit guidance that unavailable or failed availability/probe steps should fall back immediately to native memory plus checked execution surfaces.

### Summary
Memory-governance now makes optional recall intake availability-first and immediate-fallback-aware without turning optional extensions into required infrastructure.

---

<a id="version-12"></a>
## Version 1.2: Clarified how optional recall extensions should be used after stronger execution surfaces

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `memory-governance-and-session-boundary.md` from v1.1 to v1.2.
- Updated `design/memory-governance-and-session-boundary.design.md` from v1.1 to v1.2.
- Added explicit guidance that optional recall extensions may accelerate recall after the relevant execution target is identified from stronger coordination surfaces.
- Added explicit guidance that optional recall output must not outrank checked task/phase/design/implementation evidence when those stronger surfaces already settle the active meaning.

### Summary
Memory-governance now explains how optional recall extensions such as memsearch should be used after stronger execution surfaces have already identified the relevant continuation target.

---

<a id="version-11"></a>
## Version 1.1: Added optional extension recall boundary for memsearch-style layers

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `memory-governance-and-session-boundary.md` from v1.0 to v1.1.
- Updated `design/memory-governance-and-session-boundary.design.md` from v1.0 to v1.1.
- Added an explicit optional-extension recall boundary so memsearch-like extension/plugin layers are treated as supplemental context bridges rather than required infrastructure or semantic truth.
- Added explicit deferral that shared-board-specific optional recall usage stays outside Main RULES scope.

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
