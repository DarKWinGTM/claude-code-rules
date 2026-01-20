# Changelog - Document Changelog Control

> **Parent Document:** [../document-changelog-control.md](../document-changelog-control.md)
> **Current Version:** 4.3
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

---

## Version History

---

## Version 4.3: Clarify changelog.md MUST have BOTH: detailed sections + Version History Unified table

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- User clarified: changelog.md format has UPPER part (detailed sections) + LOWER part (summary table)
- Updated format table: changelog.md = Detailed sections (UPPER) + Version History Unified table (LOWER)
- Updated comparison table to reflect correct format
- Updated example to show BOTH parts of changelog.md
- Added link to changelog at end of rules files (NOT Version History section)
- Rules files rely on Git for history, NOT Version History sections

### Summary
changelog.md has BOTH detailed sections AND Version History Unified table

### Links
- Design: [../design/document-changelog-control.design.md#version-43](../design/document-changelog-control.design.md)

---

## Version 4.2: Clarify changelog.md CAN have "## Version History" header

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Clarified distinction: "## Version History" HEADER is allowed, summary TABLE is not
- Updated format table: changelog.md may optionally have "## Version History" header
- changelog.md MUST NOT use summary table format (Version | Date | Changes | Session ID)
- Updated example to show changelog.md with "## Version History" header + detailed sections
- Fixed confusion: HEADER ≠ TABLE format

### Summary
changelog.md can have "## Version History" section header, but not the summary table

### Links
- Design: [../design/document-changelog-control.design.md#version-42](../design/document-changelog-control.design.md)

---

## Version 4.1: Clarify design.md format - ONLY link, NO table

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7
| | | - Added ⚠️ CRITICAL section emphasizing design.md should NOT have Version History table | |
| | | - Updated example to show design.md with ONLY the Full history link | |
| | | - Clarified design.md is a specification document, not a changelog | |
| | | - Added \"Why This Design?\" explanation for Single Source of Truth | |
| | | - design.md now provides only navigation link to full changelog | |
| | | Summary: Made it crystal clear that design.md has NO version table, only link | |
| 4.0 | 2026-01-20 | **Design vs Product file distinction, Single Source of Truth, Lessons Learned** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | (Full changelog entries for v4.0) | |
| | | Summary: Established clear separation between design files and rules/changelogs | |

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 4.3 | 2026-01-20 | **[Clarify changelog.md MUST have BOTH: detailed sections + Version History Unified table](#version-43)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: changelog.md has BOTH detailed sections AND Version History Unified table | |
| 4.2 | 2026-01-20 | **[Clarify changelog.md CAN have "## Version History" header](#version-42)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: changelog.md can have "## Version History" section header, but not the summary table | |
| 4.1 | 2026-01-20 | **[Clarify design.md format - ONLY link, NO table](#version-41)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Made it crystal clear that design.md has NO version table, only link | |
| 4.0 | 2026-01-20 | **[Design vs Product file distinction, Single Source of Truth, Lessons Learned](#version-40)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Established clear separation between design files and rules/changelogs | |
