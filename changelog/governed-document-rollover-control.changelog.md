# Changelog - Governed Document Rollover Control

> **Parent Document:** [../governed-document-rollover-control.md](../governed-document-rollover-control.md)
> **Current Version:** 1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
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
