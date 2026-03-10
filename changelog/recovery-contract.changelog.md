# Changelog - Recovery Contract

> **Parent Document:** [../recovery-contract.md](../recovery-contract.md)
> **Current Version:** 1.5
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.5 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-15)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical runtime header metadata and aligned the recovery-contract chain to the cleanup-wave version state | |
| 1.4 | 2026-02-22 | **[Aligned response pattern keys to deterministic WS-5 schema](#version-14)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Synchronized recovery-contract runtime/design response pattern to WS-5 deterministic snake_case output schema keys | |
| 1.3 | 2026-02-22 | **[Synchronized constrained/blocked/refused contract language to runtime v1.3](#version-13)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Unified constrained/blocked/refused terminology across runtime, design, and changelog contract language for deterministic WS-1 behavior | |
| 1.2 | 2026-02-22 | **[Synchronized blocked-response schema to runtime v1.2](#version-12)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Synchronized recovery-contract design and runtime behavior to a shared v1.2 blocked/constrained response schema | |
| 1.1 | 2026-02-21 | **[Fixed integration links for design-only phase](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Fixed cross-reference validity for recovery-contract design without introducing root rule files | |
| 1.0 | 2026-02-21 | **[Initial Blocked-Response Recovery Contract](#version-10)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Established the initial deterministic recovery contract for blocked outcomes | |

---

<a id="version-15"></a>
## Version 1.5: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `recovery-contract.md` from v1.4 to v1.5.
- Updated `design/recovery-contract.design.md` from v1.4 to v1.5.
- Added canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing recovery-contract behavioral contract.

### Summary
Normalized the recovery-contract chain to the canonical cleanup-wave runtime header format while preserving substantive recovery behavior.

---

## Version 1.4: Aligned response pattern keys to deterministic WS-5 schema

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `recovery-contract.md` from v1.3 to v1.4.
- Updated `design/recovery-contract.design.md` from v1.3 to v1.4.
- Replaced mixed-case response pattern labels with deterministic snake_case keys:
  - `decision_output`
  - `refusal_class`
  - `reason`
  - `what_can_be_done_now`
  - `how_to_proceed`
- Preserved constrained/blocked/refused contract-field semantics while normalizing output key format.

### Summary
Synchronized recovery-contract runtime/design response pattern to WS-5 deterministic snake_case output schema keys.

---

## Version 1.3: Synchronized constrained/blocked/refused contract language to runtime v1.3

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `recovery-contract.md` from v1.2 to v1.3.
- Updated `design/recovery-contract.design.md` from v1.2 to v1.3.
- Replaced blocked-only wording with constrained/blocked/refused wording in the runtime rule statement and mandatory fields.
- Updated quality metric scope to include constrained and refused outputs, not only blocked outputs.

### Summary
Unified constrained/blocked/refused terminology across runtime, design, and changelog contract language for deterministic WS-1 behavior.

---

## Version 1.2: Synchronized blocked-response schema to runtime v1.2

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/recovery-contract.design.md` from v1.1 to v1.2.
- Expanded contract applicability to include `ALLOW_CONSTRAINED` alongside blocked outcomes.
- Aligned response schema and class-specific requirements with runtime `recovery-contract.md` v1.2.
- Normalized wording to deterministic English-only language.

### Summary
Synchronized recovery-contract design and runtime behavior to a shared v1.2 blocked/constrained response schema.

---

## Version 1.1: Fixed integration links for design-only phase

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/recovery-contract.design.md` to v1.1.
- Replaced non-existent root-rule links in Integration section with existing `*.design.md` links.
- Preserved existing link to active rule `authority-and-scope.md`.
- Clarified Integration heading to `Related design docs / active rules`.

### Summary
Fixed cross-reference validity for recovery-contract design without introducing root rule files.

---

## Version 1.0: Initial Blocked-Response Recovery Contract

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created `design/recovery-contract.design.md` v1.0.
- Established an initial deterministic recovery contract for blocked outcomes.

### Summary
Established the initial deterministic recovery contract for blocked outcomes.
