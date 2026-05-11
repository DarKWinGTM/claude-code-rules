# Changelog - Governed Document Rollover Control

> **Parent Document:** [../governed-document-rollover-control.md](../governed-document-rollover-control.md)
> **Current Version:** 1.2
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Version History (Unified)

<a id="version-12"></a>
## Version 1.2: Added automatic rollover repair planning for God documents

**Date:** 2026-05-11
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Added automatic rollover repair planning for God-document pressure in active TODO and phase entrypoints.
- Required immediate rollover when clear or visible repair planning when broader classification is needed.
- Preserved the no-deletion boundary and parent/history/done reference requirements.

### Summary
Added automatic rollover repair planning for God documents for P092 / v10.00.

---

## Version 1.1: Added God-document repair routing through rollover surfaces

- Added P091 governed document God-file prevention and repair semantics for this owner chain.
- Preserved role-specific authority boundaries while adding the correct split, shard, rollover, or redistribution route.


| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-05-11 | **[Added automatic rollover repair planning for God documents](#version-12)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 1.0 | 2026-05-08 | **[Created daily-first governance rollover owner](#version-10)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Created the first-class active runtime owner for daily-first TODO and phase-summary rollover, active entrypoint preservation, history/done reference integrity, existing oversized file migration, and no-deletion-by-rollover boundaries. | |

---

<a id="version-10"></a>
## Version 1.0: Created daily-first governance rollover owner

**Date:** 2026-05-08
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Created `governed-document-rollover-control.md` as a new active runtime rule.
- Created `design/governed-document-rollover-control.design.md` as the target-state design companion.
- Defined daily-first rollover for `TODO.md` and `phase/SUMMARY.md` using `todo/history/`, `todo/done/`, `phase/history/`, and `phase/done/` as referenced inactive history/detail surfaces.
- Added soft and hard size/thrash triggers for active governance entrypoints.
- Required existing oversized files to be preserved, classified, compacted into active indexes, and linked to reachable history/done shards instead of ignored.
- Preserved the boundary that rollover is not deletion authority and runtime installs target only active root rule files.

### Summary
Governed document rollover now has one active owner: main TODO and phase summary files remain current navigation roots, daily/history/done shards keep accumulated detail reachable, and oversized existing files are migrated without deleting governed meaning.

---
