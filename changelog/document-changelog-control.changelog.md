# Changelog - Document Changelog Control

> **Parent Document:** [../document-changelog-control.md](../document-changelog-control.md)
> **Current Version:** 4.4
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

---

<a id="version-44"></a>
## Version 4.4: Introduced OR Compliance and Explicit Pair Behavior

**Date:** 2026-02-21
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Synchronized changelog policy with `design/document-changelog-control.design.md` v4.4
- Clarified **traceable version path** rule as OR compliance:
  - (A) local `Version History (Unified)` table, OR
  - (B) authoritative changelog link (`> Full history: ...`)
- Made pair behavior explicit when design/changelog documents coexist:
  - `design.md` / `*.design.md` = Navigator link-only
  - `changelog.md` / `*.changelog.md` = Detailed sections (UPPER) + Unified table (LOWER)
- Normalized malformed legacy v4.1 block into proper changelog section structure while preserving historical intent

### Summary
Added v4.4 governance update for OR compliance and strict design/changelog pair separation

### Links
- Design: [../design/document-changelog-control.design.md](../design/document-changelog-control.design.md)

---

<a id="version-43"></a>
## Version 4.3: Clarify changelog.md MUST have BOTH detailed sections and Unified table

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Clarified changelog format as two mandatory parts:
  - UPPER: Detailed version sections
  - LOWER: `Version History (Unified)` summary table
- Updated examples and format comparison to enforce BOTH parts
- Reinforced that rules files use changelog links rather than embedded full history tables

### Summary
Established two-part changelog format (detailed sections + unified summary table)

### Links
- Design: [../design/document-changelog-control.design.md](../design/document-changelog-control.design.md)

---

<a id="version-42"></a>
## Version 4.2: Clarify changelog.md can include "Version History" header

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Clarified that a `## Version History` section header is allowed in changelog files
- Clarified distinction between section header and summary table usage
- Refined examples to reduce confusion between header naming and data format

### Summary
Clarified header naming versus data format in changelog files

### Links
- Design: [../design/document-changelog-control.design.md](../design/document-changelog-control.design.md)

---

<a id="version-41"></a>
## Version 4.1: Clarify design.md Navigator behavior (link-only)

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Clarified design documents should act as Navigator (link to full changelog)
- Emphasized design documents are specification documents, not full changelog containers
- Added explanation to prevent duplicate version history across design/changelog pairs

### Summary
Clarified design docs should provide navigation link, not duplicated full history tables

### Links
- Design: [../design/document-changelog-control.design.md](../design/document-changelog-control.design.md)

---

<a id="version-40"></a>
## Version 4.0: Design vs Product distinction and Single Source of Truth

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Introduced structured version-control model across rules/design/changelog documents
- Established Single Source of Truth concept for version authority
- Defined foundational integration behavior for changelog governance

### Summary
Established baseline architecture for documentation version governance

### Links
- Design: [../design/document-changelog-control.design.md](../design/document-changelog-control.design.md)

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 4.4 | 2026-02-21 | **[Introduced OR Compliance and Explicit Pair Behavior](#version-44)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | Summary: Added OR compliance and strict design/changelog pair separation | |
| 4.3 | 2026-01-20 | **[Clarify changelog.md MUST have BOTH detailed sections and Unified table](#version-43)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Established two-part changelog format | |
| 4.2 | 2026-01-20 | **[Clarify changelog.md can include "Version History" header](#version-42)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Clarified header naming versus table format | |
| 4.1 | 2026-01-20 | **[Clarify design.md Navigator behavior (link-only)](#version-41)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Clarified design docs as navigator link-only | |
| 4.0 | 2026-01-20 | **[Design vs Product distinction and Single Source of Truth](#version-40)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Established baseline governance architecture | |
