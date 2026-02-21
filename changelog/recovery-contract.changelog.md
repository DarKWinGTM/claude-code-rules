# Changelog - Recovery Contract

> **Parent Document:** [../design/recovery-contract.design.md](../design/recovery-contract.design.md)
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

## Version 1.0: Initial Blocked-Response Recovery Contract

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Created `design/recovery-contract.design.md` v1.0
- Standardized mandatory contract fields for blocked outcomes:
  - Reason
  - What can be done now
  - How to proceed
- Added class-specific requirements for HARD/SOFT/WORKFLOW blocks
- Added output pattern and quality metrics to eliminate dead-end refusals

### Summary
Created a standard recovery contract so blocked responses always provide actionable next steps

---

## Version 1.1: Fixed integration links for design-only phase

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `design/recovery-contract.design.md` to v1.1
- Replaced non-existent root-rule links in Integration section with existing `*.design.md` links
- Preserved existing link to active rule `authority-and-scope.md`
- Clarified Integration heading to `Related design docs / active rules`

### Summary
Fixed cross-reference validity for recovery-contract design without introducing root rule files

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-02-21 | **[Fixed integration links for design-only phase](#version-11)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Repointed integration links to design artifacts while preserving active-rule references | |
| 1.0 | 2026-02-21 | **[Initial Blocked-Response Recovery Contract](#version-10)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Introduced mandatory recovery structure for all blocked decisions | |
