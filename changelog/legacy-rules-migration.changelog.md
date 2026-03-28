# Changelog - Legacy Rules Migration

> **Parent Document:** [../patch/legacy-rules-migration.patch.md](../patch/legacy-rules-migration.patch.md)
> **Current Version:** 1.3
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.3 | 2026-03-28 | **[Rewrote the migration patch as a structured non-code before/after artifact](#version-13)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | Summary: Renamed the active patch location to `patch/` and normalized this historical governance patch so it now compares legacy versus standardized document-state changes directly instead of reading like a prose migration checklist | |
| 1.2 | 2026-02-01 | **[Fixed Navigator Format Compliance](#version-12)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Truncated Version History in design docs to 2-3 latest versions (Navigator standard) | |
| | | - Fixed document-changelog-control.design.md and project-documentation-standards.design.md | |
| | | Summary: Enforced Navigator format on design documents | |
| 1.1 | 2026-02-01 | **[Completion of Migration](#version-11)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Completed migration of all 12 legacy rules | |
| 1.0 | 2026-02-01 | **[Initial Plan](#version-10)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Plan to migrate 12 legacy rules to standard template | |

---

<a id="version-13"></a>
## Version 1.3: Rewrote the migration patch as a structured non-code before/after artifact

**Date:** 2026-03-28
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Moved the patch from `patches/legacy-rules-migration.patch.md` to `patch/legacy-rules-migration.patch.md`.
- Reclassified the patch explicitly as a non-code / governance patch.
- Replaced phase-checklist-style patch prose with structured change items.
- Added before/after comparison blocks for:
  - legacy runtime header state
  - design-file history handling
  - changelog-authority introduction
  - migration-control wording itself
- Preserved the patch as a historical example while normalizing it to the active patch-governance model.

### Summary
Normalized the legacy migration patch so it now demonstrates the corrected patch concept even for governance work: explicit current→target comparison rather than prose-only migration planning.

---

<a id="version-12"></a>
## Version 1.2: Fixed Navigator Format Compliance

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Enforced Navigator format on all design documents (removed full history tables)
- Truncated `design/document-changelog-control.design.md` to latest 3 versions
- Updated `design/project-documentation-standards.design.md` to Navigator format
- Verified `design/document-design-control.design.md` compliance
- Ensured all full history is preserved in corresponding changelog files

### Summary
Enforced Navigator format (brief history) on design documents to prevent duplication

---

<a id="version-11"></a>
## Version 1.1: Completion of Migration

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Completed Phase 1: Created changelogs for all 12 rules
- Completed Phase 2: Updated all 12 design documents to standard format
- Completed Phase 3: Updated all 12 rule files to standard header/footer
- Completed Phase 4: Verified compliance and links
- Updated `strict-file-hygiene.design.md` with missing content

### Summary
Completed migration of all 12 legacy rules to standard template

---

<a id="version-10"></a>
## Version 1.0: Initial Plan

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Created migration plan for 12 legacy rules
- Defined 3 phases: Preparation, Design Doc Standardization, Rule File Standardization
- Target design: design.md v1.5 standard templates

### Summary
Plan to migrate 12 legacy rules to standard template
