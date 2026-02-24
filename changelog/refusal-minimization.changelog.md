# Changelog - Refusal Minimization

> **Parent Document:** [../design/refusal-minimization.design.md](../design/refusal-minimization.design.md)
> **Current Version:** 1.4
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## Version 1.4: Consolidated compact non-ALLOW schema fields for WS-5

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `refusal-minimization.md` from v1.3 to v1.4.
- Updated `design/refusal-minimization.design.md` from v1.3 to v1.4.
- Standardized non-`ALLOW_EXECUTE` output schema to explicit five fields:
  - `decision_output`
  - `refusal_class`
  - `reason`
  - `what_can_be_done_now`
  - `how_to_proceed`
- Removed compact `next_step` style from WS-5 non-ALLOW contract path.

### Summary
Aligned refusal-minimization runtime/design outputs to WS-5 compact deterministic five-field non-ALLOW schema.

---

## Version 1.3: Hardened deterministic refusal-class output contract to runtime v1.3

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `refusal-minimization.md` from v1.2 to v1.3.
- Updated `design/refusal-minimization.design.md` from v1.2 to v1.3.
- Removed optional refusal-class wording from runtime Output Standard.
- Enforced explicit refusal-class requirement (`SOFT_BLOCK`, `WORKFLOW_BLOCK`, or `HARD_BLOCK`) for all non-`ALLOW_EXECUTE` outcomes.

### Summary
Strengthened WS-1 deterministic mapping by eliminating refusal-class ambiguity in runtime/design output contracts.

---

## Version 1.2: Synchronized deterministic contract to runtime v1.2

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/refusal-minimization.design.md` from v1.1 to v1.2.
- Aligned design decision semantics with runtime `refusal-minimization.md` v1.2.
- Normalized wording to deterministic English-only contract language.
- Clarified mapping triggers for `NEED_CONTEXT`, `ALLOW_CONSTRAINED`, and `REFUSE_WITH_PATH`.

### Summary
Synchronized design and runtime behavior for refusal minimization under a deterministic v1.2 contract.

---

## Version 1.1: Fixed integration links for design-only phase

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/refusal-minimization.design.md` to v1.1.
- Replaced non-existent root-rule links in Integration section with existing `*.design.md` links.
- Preserved existing link to active rule `authority-and-scope.md`.
- Clarified Integration heading to `Related design docs / active rules`.

### Summary
Eliminated broken integration links while keeping design-phase scope (no root-rule materialization).

---

## Version 1.0: Initial Design for False Refusal Minimization

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created `design/refusal-minimization.design.md` v1.0.
- Defined principle: minimize unnecessary refusal while preserving hard boundaries.
- Standardized decision-output orientation (`ALLOW_EXECUTE`, `ALLOW_CONSTRAINED`, `NEED_CONTEXT`, `REFUSE_WITH_PATH`).
- Added false-refusal patterns and replacement behaviors.
- Added safety invariants and quality metrics.

### Summary
Introduced design baseline for reducing false refusals in authorized pentest workflows without weakening hard safety controls.

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.4 | 2026-02-22 | **[Consolidated compact non-ALLOW schema fields for WS-5](#version-14-consolidated-compact-non-allow-schema-fields-for-ws-5)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Standardized five explicit fields for all non-ALLOW outputs across runtime/design contract text | |
| 1.3 | 2026-02-22 | **[Hardened deterministic refusal-class output contract to runtime v1.3](#version-13-hardened-deterministic-refusal-class-output-contract-to-runtime-v13)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Removed optional-class ambiguity and enforced explicit refusal class for all non-ALLOW_EXECUTE outputs | |
| 1.2 | 2026-02-22 | **[Synchronized deterministic contract to runtime v1.2](#version-12-synchronized-deterministic-contract-to-runtime-v12)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Synced design contract and runtime behavior for deterministic refusal minimization | |
| 1.1 | 2026-02-21 | **[Fixed integration links for design-only phase](#version-11-fixed-integration-links-for-design-only-phase)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Repointed integration links to existing design docs and removed root-rule dependency in design phase | |
| 1.0 | 2026-02-21 | **[Initial Design for False Refusal Minimization](#version-10-initial-design-for-false-refusal-minimization)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Design baseline for false-refusal minimization with hard-boundary preservation | |
