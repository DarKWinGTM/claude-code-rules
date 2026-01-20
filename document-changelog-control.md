# Document Changelog & Versions History Control

> **Current Version:** 4.0
> **Based on:** document-changelog-control.design.md v4.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

---

## Rule Statement

**Core Principle: Every document must have traceable version history with real session IDs**

This rule ensures all documentation maintains proper version control using the **Version History (Unified)** format. It prevents confusion between detailed changelogs and summary version tables, establishes a single format for all document types, and enforces the use of real session IDs (no mock data) for traceability.

---

## Core Requirements

### 1. Version History Format (Mandatory)

**Required Actions:**
- Every document MUST have a **Version History (Unified)** section
- Use the same format for both changelog files and design documents
- Session IDs MUST be real values from the environment (`<env>` tags)
- Date format: `YYYY-MM-DD`

### 2. Session ID Integrity

**Required Actions:**
- Session ID MUST be extracted from `<env>` tags in the current session
- Format: UUID (36 characters) or `SXXXX` format
- NEVER use placeholder values like `<Session ID>`, `TBD`, or mock data
- For legacy entries: Use `LEGACY-XXX` format (sequential)

**Session ID Location:**
```xml
<env>
Session ID: a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7
Time: [timestamp]
</env>
```

### 3. History Preservation

**Required Actions:**
- NEVER delete or truncate existing Version History entries
- Preserve all historical entries when updating documents
- If correcting old history: Create a new entry documenting the correction
- All entries MUST have Date and Session ID

### 4. design.md <> changelog.md Relationship (Mandatory)

> **Critical Rule:** When BOTH `design.md` AND `changelog.md` exist in the same project

**Mandatory Format Enforcement:**

| File | MUST use | MUST NOT use |
|------|----------|--------------|
| **changelog.md** (main) | Full Changelog (Detailed sections) | Version History (Unified) table |
| **design.md** | Version History (Unified) Navigator | Full Changelog sections |

**Key Principle:**
- ✅ **BOTH files MUST exist together** - design.md and changelog.md must both be present
- ✅ **design.md** = Version History (Unified) Navigator (short, 2-3 latest versions)
- ✅ **changelog.md** = Full Changelog (Detailed sections with all versions)

---

### What is "Navigator"?

**Version History (Unified) Navigator** means:
- ✅ Version History table with **ONLY 2-3 latest versions**
- ✅ Each entry = **Headline + 1-line summary** (no bullet points)
- ✅ Has **link to Full Changelog**: `> Full history: [changelog.md](changelog.md)`
- ❌ NOT the full Version History (with all versions)

---

### Complete Example (Both Files Together)

#### design.md - at the end of file

```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 3.9 | 2026-01-20 | **[Added design.md <> changelog.md Relationship Rule](changelog.md#L863)** | a77b77ae... |
| | | Summary: Enforced clear separation between design (navigator) and changelog (full) | |
| 3.8 | 2026-01-20 | **[Clarified changelog.md Location Patterns](changelog.md#L820)** | a77b77ae... |
| | | Summary: Fixed AI confusion about master changelog location | |
| 3.7 | 2026-01-20 | **[Standardized on Line Number Links](changelog.md#L750)** | a77b77ae... |
| | | Summary: Line Number format for precise changelog navigation | |

> Full history: [changelog.md](changelog.md)
```

#### changelog.md - separate file

```markdown
# Changelog - Main

> **Parent Document:** [design.md](design.md)
> **Current Version:** 3.9
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

---

## Version 3.9: Added design.md <> changelog.md Relationship Rule

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added Section 5.2.1: Mandatory design.md <> changelog.md relationship
- changelog.md MUST be Full Changelog (not Version History table)
- design.md MUST be Version History (Unified) Navigator
- Applies to all patterns (Simple/Mixed) when both files exist
- Added mechanism diagram and linking examples

### Summary
Enforced clear separation between design (navigator) and changelog (full)

### Links
- Design: [design.md#version-39](design.md#version-39)

---

## Version 3.8: Clarified changelog.md Location Patterns

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added location pattern to Reserved Terms: root vs changelog/ subdirectory
- Pattern 1: changelog.md at root IS the master changelog
- Pattern 2: changelog/changelog.md IS the master changelog (not root)
- Updated Decision Tree with master changelog location for each pattern
- Added WARNING about duplicate changelog.md files

### Summary
Fixed AI confusion about which changelog.md is the master

### Links
- Design: [design.md#version-38](design.md#version-38)
```

---

### Comparison: Correct vs Incorrect

| File | ✅ Correct (Navigator + Full) | ❌ Incorrect (Full everywhere) |
|------|-------------------------------|------------------------------|
| **design.md** | Has Version History table with 2-3 entries + link | No Version History or has full version |
| **changelog.md** | Has Detailed sections with all versions | None or has only Version History table |

---

**Applies to ALL patterns:**

| Pattern | design.md | changelog.md |
|---------|-----------|--------------|
| **1 (Simple)** | `./design.md` (Navigator - 2-3 versions) | `./changelog.md` (Full - all versions) |
| **2 (Mixed)** | `./design/*.design.md` (Navigator - 2-3 versions) | `./changelog/changelog.md` (Full - all versions) |

---

**PROHIBITED:**
- ❌ Creating changelog.md with only Version History (Unified) table (when design.md exists)
- ❌ Creating design.md with Full Changelog sections (must be Navigator only)
- ❌ Having only ONE file (must have BOTH design.md AND changelog.md)

### 5. Changelog Linking

**Required Actions:**
- If a separate changelog file exists: Link to it from the main document
- Use format: `> Full history: [changelog.<doc>.md](changelog/changelog/<doc>.md)`
- The link MUST be included in the Version History section

---

## Format Standards

### Universal Format: Version History (Unified)

**Use for all documents** - whether changelog master files or design docs

```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **<Headline>** | <Session UUID or ID> |
| | | - <Change 1> | |
| | | - <Change 2> | |
| | | Summary: <One-line summary> | |
| X.X | YYYY-MM-DD | **<Headline>** | <Session UUID or ID> |
| | | - <Change 1> | |
| | | Summary: <One-line summary> | |

> Full history: [changelog.<doc>.md](changelog/changelog.<doc>.md)
```

### Location Strategy

| Document Type | Version History Location |
|--------------|------------------------|
| **Changelog files** | Entire file is Version History |
| **Design documents** | Section at the end of the file |
| **General documents** | Section at the end of the file |

---

## Version Classification

| Type | Description | Example |
|------|-------------|---------|
| **Major** (X.0) | Breaking changes, structural modifications | Rewriting entire format |
| **Minor** (X.Y) | New features, significant content additions | Adding new sections |
| **Patch** (X.Y.Z) | Typos, clarifications, minor fixes | Fixing grammar |

---

## Reserved Terms & Protected Keywords

### Reserved File Names (Master Files)

| Reserved Term | Location Pattern | Do NOT use for |
|--------------|-----------------|---------------|
| `changelog.md` | Root level only (`./changelog.md`) | Other changelog files, or if using Pattern 2 |
| `changelog/changelog.md` | Inside `./changelog/` directory | Other changelog files |
| `design.md` | Root level only (`./design.md`) | Other design files |

### Reserved File Suffixes

| Reserved Suffix | Meaning | Do NOT use for |
|----------------|-----------|---------------|
| `.design.md` | Design document | Non-design files |
| `.changelog.md` | Changelog file | Non-changelog files |

### Reserved Section Names

| Reserved Term | Correct format | Do NOT use instead |
|--------------|----------------|------------------|
| `Version History (Unified)` | Section header | `Changelog`, `Change Log`, `History` |

### Reserved Table Columns

| Column Name | Do NOT use instead |
|-------------|-------------------|
| `Version` | `Ver`, `Rev`, `V` |
| `Date` | `Time`, `Updated`, `When` |
| `Changes` | `Description`, `What`, `Notes` |
| `Session ID` | `ID`, `Session`, `UUID` |

---

## File Organization Patterns

### Pattern 1: Simple Project (no ./changelog/ and ./design/)

```
./
├── README.md
├── design.md                 ← Version History at end (if present)
├── changelog.md              ← Master changelog at ROOT
└── src/
```

**Use when:** Project has neither `./changelog/` nor `./design/`
**Note:** `changelog.md` at root level IS the master changelog

### Pattern 2: Mixed (has both design and changelog) - **Most Complete**

```
./
├── design/
│   ├── anti-mockup.design.md   ← Version History at end
│   └── safe-file-reading.design.md
├── changelog/
│   ├── changelog.md         ← Master changelog (INSIDE changelog/)
│   └── video.changelog.md    ← Specific changelog
└── src/
```

**Use when:** Project has both design docs and specific changelogs
**Note:** `chelog/changelog.md` (not root `changelog.md`) IS the master changelog

### Decision Tree

```
Has ./changelog/ or ./design/?
├─ Yes → ✅ Use Pattern 2 (Mixed - ideal/complete)
│         → Master changelog = changelog/changelog.md
└─ No  → Use Pattern 1 (Simple - root level only)
         → Master changelog = changelog.md at root
```

**IMPORTANT: Never have BOTH**
- `./changelog.md` (root) AND `./changelog/changelog.md` ← This is DUPLICATE/CONFUSED

---

## Naming Rules

### Changelog File Naming

**Recommended format**: `<doc>.changelog.md`

**Examples:**
- `anti-mockup.changelog.md`
- `document-changelog-control.changelog.md`
- `safe-file-reading.changelog.md`

### Location Options

| Location | Format | Use when |
|-----------|--------|----------|
| `design/changelog/<doc>.changelog.md` | With subdir | Design docs with many changelogs |
| `changelog/<doc>.changelog.md` | Root subdir | Project with centralized changelog |

---

## When to Create Full Changelog

| Situation | Create .changelog.md? | Reason |
|-----------|----------------------|--------|
| Design doc has few versions (< 5) | ❌ No need | Version History in single file is enough |
| Design doc updates frequently | ✅ Yes | Separate history before it gets too long |
| Design doc has complex changes | ✅ Yes | Need detailed change tracking |

---

## Detail Level Guidelines

### Brief Entry (For Design Doc)

Use for Version History in design documents (showing 2-3 latest versions)

```markdown
| X.Y | YYYY-MM-DD | **<Short Headline>** | <Session ID> |
| | | Summary: <One-line summary> | |
```

### Detailed Entry (For Full Changelog)

Use for Full changelog files (`<doc>.changelog.md`) - showing all versions

```markdown
## Version X.Y: <Headline>

**Date:** YYYY-MM-DD
**Session:** <Session ID>

### Changes
- <Change 1 - detailed description>
- <Change 2 - detailed description>

### Summary
<One-line summary>
```

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Version History Presence | 100% (all documents must have one) |
| Session ID Accuracy | 100% No Mock (real values only) |
| Date Completeness | 100% (all entries must have Date) |
| History Preservation | 100% (never delete old entries) |
| Changelog Linking | Required when separate changelog exists |
| Naming Format | Recommended: `<doc>.changelog.md` |

---

## Compliance Levels

### Minimum Compliance (Mandatory)

Every document MUST have at least one of:
1. **Version History (Unified)** table in the document
2. Link to a separate changelog file

### Recommended Compliance

For documents with frequent updates:
1. Create separate `<doc>.changelog.md` file
2. Include Version History (Unified) in main document (2-3 latest versions)
3. Link from main document to full changelog

---

## Enforcement Notes

- **Single Source of Truth**: If master changelog exists, use as single reference
- **Cross-reference check**: All links `changelog.<doc>.md` must reference existing files
- **No duplicated history**: Do NOT copy full history across multiple files
- **Git handles history**: Let Git track history, NOT suffixes in filenames

