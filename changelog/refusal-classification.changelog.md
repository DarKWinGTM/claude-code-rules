# Changelog - Refusal Classification

> **Parent Document:** [../design/refusal-classification.design.md](../design/refusal-classification.design.md)
> **Current Version:** 1.3
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## Version 1.3: Aligned output requirements to WS-5 recovery schema fields

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `refusal-classification.md` from v1.2 to v1.3.
- Updated `design/refusal-classification.design.md` from v1.2 to v1.3.
- Replaced compact `next_step` output requirement with explicit recovery fields:
  - `what_can_be_done_now`
  - `how_to_proceed`
- Preserved deterministic decision-output and refusal-class mapping semantics.

### Summary
Synchronized refusal-classification runtime/design output contract to WS-5 explicit recovery-field schema.

---

## Version 1.2: Synchronized deterministic taxonomy to runtime v1.2

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/refusal-classification.design.md` from v1.1 to v1.2.
- Aligned taxonomy and output mapping wording with runtime `refusal-classification.md` v1.2.
- Normalized class trigger text to deterministic English-only language.
- Clarified escalation condition for unresolved non-hard block paths.

### Summary
Synchronized refusal taxonomy design and runtime behavior under deterministic v1.2 contract semantics.

---

## Version 1.1: Fixed integration links for design-only phase

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/refusal-classification.design.md` to v1.1.
- Replaced non-existent root-rule links in Integration section with existing `*.design.md` links.
- Clarified Integration heading to `Related design docs / active rules`.

### Summary
Removed broken cross-references and aligned integration links with design-phase artifacts.

---

## Version 1.0: Initial Refusal Taxonomy and Output Mapping

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created `design/refusal-classification.design.md` v1.0.
- Defined refusal classes: `HARD_BLOCK`, `SOFT_BLOCK`, `WORKFLOW_BLOCK`.
- Defined override policy per class (hard non-overridable; soft/workflow user-resolvable).
- Mapped decision outputs to refusal classes and execution behavior.
- Added classification triggers and deterministic output requirements.

### Summary
Established a clear refusal taxonomy and deterministic mapping to decision outputs for authorized adversarial workflows.

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.3 | 2026-02-22 | **[Aligned output requirements to WS-5 recovery schema fields](#version-13-aligned-output-requirements-to-ws-5-recovery-schema-fields)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Replaced `next_step` with explicit `what_can_be_done_now` and `how_to_proceed` fields | |
| 1.2 | 2026-02-22 | **[Synchronized deterministic taxonomy to runtime v1.2](#version-12-synchronized-deterministic-taxonomy-to-runtime-v12)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Aligned design taxonomy and runtime output mapping under deterministic language | |
| 1.1 | 2026-02-21 | **[Fixed integration links for design-only phase](#version-11-fixed-integration-links-for-design-only-phase)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Repointed integration links to existing design docs for non-materialized rule phase | |
| 1.0 | 2026-02-21 | **[Initial Refusal Taxonomy and Output Mapping](#version-10-initial-refusal-taxonomy-and-output-mapping)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Defined refusal classes, override policy, and decision-output mapping | |
