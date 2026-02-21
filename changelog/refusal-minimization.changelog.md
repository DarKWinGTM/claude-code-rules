# Changelog - Refusal Minimization

> **Parent Document:** [../design/refusal-minimization.design.md](../design/refusal-minimization.design.md)
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## Version 1.0: Initial Design for False Refusal Minimization

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created `design/refusal-minimization.design.md` v1.0
- Defined principle: minimize unnecessary refusal while preserving hard boundaries
- Standardized decision-output orientation (`ALLOW_EXECUTE`, `ALLOW_CONSTRAINED`, `NEED_CONTEXT`, `REFUSE_WITH_PATH`)
- Added false-refusal patterns and replacement behaviors
- Added safety invariants and quality metrics

### Summary
Introduced design baseline for reducing false refusals in authorized pentest workflows without weakening hard safety controls

---

## Version 1.1: Fixed integration links for design-only phase

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/refusal-minimization.design.md` to v1.1
- Replaced non-existent root-rule links in Integration section with existing `*.design.md` links
- Preserved existing link to active rule `authority-and-scope.md`
- Clarified Integration heading to `Related design docs / active rules`

### Summary
Eliminated broken integration links while keeping design-phase scope (no root rule materialization)

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-02-21 | **[Fixed integration links for design-only phase](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Repointed integration links to existing design docs and removed root-rule dependency in design phase | |
| 1.0 | 2026-02-21 | **[Initial Design for False Refusal Minimization](#version-10)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Design baseline for false-refusal minimization with hard-boundary preservation | |
