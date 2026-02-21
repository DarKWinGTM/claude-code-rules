# Changelog - Refusal Classification

> **Parent Document:** [../design/refusal-classification.design.md](../design/refusal-classification.design.md)
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## Version 1.0: Initial Refusal Taxonomy and Output Mapping

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created `design/refusal-classification.design.md` v1.0
- Defined refusal classes: `HARD_BLOCK`, `SOFT_BLOCK`, `WORKFLOW_BLOCK`
- Defined override policy per class (hard non-overridable; soft/workflow user-resolvable)
- Mapped decision outputs to refusal classes and execution behavior
- Added classification triggers and deterministic output requirements

### Summary
Established a clear refusal taxonomy and deterministic mapping to decision outputs for authorized adversarial workflows

---

## Version 1.1: Fixed integration links for design-only phase

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/refusal-classification.design.md` to v1.1
- Replaced non-existent root-rule links in Integration section with existing `*.design.md` links
- Clarified Integration heading to `Related design docs / active rules`

### Summary
Removed broken cross-references and aligned integration links with design-phase artifacts

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-02-21 | **[Fixed integration links for design-only phase](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Repointed integration links to existing design docs for non-materialized rule phase | |
| 1.0 | 2026-02-21 | **[Initial Refusal Taxonomy and Output Mapping](#version-10)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Defined refusal classes, override policy, and decision-output mapping | |
