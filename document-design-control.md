# Document Design Control

> **Current Version:** 1.3

## Rule Statement

**Core Principle: Design documents must follow consistent standards for structure, naming, and location**

This rule ensures all design documents (`*.design.md`) maintain uniform format, proper version tracking, and correct integration with changelog files.

**Based on:** [document-design-control.design.md](design/document-design-control.design.md) v1.2

**Related Reference:** [document-changelog-control.md](document-changelog-control.md) v4.3 - Defines Version History (Unified) format

---

## Core Requirements

### 1. File Naming Standards

**Required Format:**

| File Type | Format | Example | Correct ✅ | Incorrect ❌ |
|-----------|--------|---------|------------|--------------|
| Design Document | `<name>.design.md` | `anti-mockup.design.md` | `api-design.design.md` | `api-design-spec.md` |
| Changelog File | `<name>.changelog.md` | `anti-mockup.changelog.md` | `api-design.changelog.md` | `changelog-api-design.md` |
| Rules File | `<name>.md` | `anti-mockup.md` | `api-design.md` | `api-design-rule.md` |

**Key Points:**
- Design documents MUST use `.design.md` suffix
- Changelog files MUST use `.changelog.md` suffix
- Rules files use simple `.md` extension
- No version numbers in filenames (e.g., `-v2`, `-final`)

### 2. Location Standards

**Two patterns available - choose based on project complexity:**

---

#### Pattern 1: Simple Project (Single Design)

**Use when:** Project has only ONE design document and NO `./design/` or `./changelog/` subdirectories

```
./
├── README.md
├── design.md                 ← Design at ROOT (no suffix needed)
├── changelog.md              ← Changelog at ROOT
├── patch.md                  ← Other docs at ROOT
└── src/
```

**Rules for Pattern 1:**
- `design.md` at root (NO `.design.md` suffix needed)
- `changelog.md` at root
- NO subdirectories required
- Simpler structure for single-purpose projects

---

#### Pattern 2: Complex Project (Multiple Designs)

**Use when:** Project has multiple design documents OR uses `./design/` and `./changelog/` subdirectories

```
./
├── design/
│   └── <name>.design.md      ← Design documents here ONLY
├── changelog/
│   ├── changelog.md          ← Master changelog (optional)
│   └── <name>.changelog.md   ← Specific changelogs here
├── <name>.md                 ← Rules files at root
└── README.md
```

**Rules for Pattern 2:**
- ALL design documents go in `./design/` subdirectory
- ALL changelog files go in `./changelog/` subdirectory
- MUST use `.design.md` suffix for design files
- MUST use `.changelog.md` suffix for changelog files
- Rules files stay at project root

---

#### Decision Tree

```
How many design documents?
├─ ONE design only → Pattern 1 (Simple)
│   → design.md, changelog.md at ROOT
│   → NO subdirectories needed
│   → NO .design.md suffix needed
│
└─ MULTIPLE designs → Pattern 2 (Complex)
    → ./design/*.design.md
    → ./changelog/*.changelog.md
    → MUST use suffixes
```

**IMPORTANT: Never mix patterns**
- If using Pattern 2 (subdirectories exist), ALL design docs must be in `./design/`
- If using Pattern 1 (no subdirectories), keep everything at root

### 3. Document Control Section (MANDATORY)

**Every design document MUST have this section at the top:**

```markdown
## 0) Document Control

> **Parent Scope:** [Parent project/system name]
> **Current Version:** X.Y
> **Session:** [UUID] (YYYY-MM-DD)
```

**Field Requirements:**

| Field | Required | Format | Validation |
|-------|----------|--------|------------|
| Parent Scope | ✅ Yes | Project/system name | Must be meaningful |
| Current Version | ✅ Yes | X.Y format | Match changelog |
| Session ID | ✅ Yes | UUID (36 chars) | Real UUID, NO placeholders |

**Session ID Rules:**
- ✅ Valid: `a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7`
- ❌ Invalid: `<Session ID>`, `TBD`, `pending`, `xxx-xxx-xxx`

### 4. Design Document Structure (Comprehensive Rules)

**MANDATORY (Must Have):**

| Element | Requirement | Format |
|---------|-------------|--------|
| **Document Control Section** | Required at top | `## 0) Document Control` with Parent Scope, Version, Session |
| **Changelog Link** | Required at end | `> Full history: [changelog.md](changelog.md)` |
| **Session ID** | Must be real UUID | 36 characters, NO placeholders |
| **File Location** | Pattern 1: Root, Pattern 2: `./design/` | See Section 2 |
| **File Suffix** | Pattern 1: `.md`, Pattern 2: `.design.md` | See Section 2 |

**PROHIBITED (Must NOT Have):**

| Element | Why Prohibited | Correct Alternative |
|---------|----------------|---------------------|
| **Version History table** | Belongs in changelog only | Use changelog link instead |
| **Version numbers in filename** | Git tracks history | Use `name.design.md` only |
| **Placeholders** | Violates changelog rules | Use real UUID or omit |
| **Mixed formats** | Breaks consistency | Follow unified format |
| **Frames/boxes in diagrams** | Violates flow-diagram rule | Use text-based diagrams |

**ALLOWED (Flexible - Your Choice):**

| Element | When to Use | Notes |
|---------|-------------|-------|
| **Section numbering** | Any style | 0), 1., ##, or no numbers |
| **Section names** | Any meaningful names | Goal, Scope, Requirements, etc. |
| **Content sections** | As many as needed | Organize by your logic |
| **Language** | Thai, English, or mixed | Match team preference |
| **Code examples** | When helpful | Use markdown code blocks |
| **Diagrams** | When clarifying concepts | Follow flow-diagram-no-frame.md |

**DECISION TREE (What goes where?):**

```
Need to track versions?
  → YES: Version details go in changelog.md
  → NO: Design doc has link only

Need to show document hierarchy?
  → YES: Use Document Control section at top

Need to show specific change details?
  → YES: Put in changelog.md
  → NO: Design doc describes current state

Need to reference another design?
  → YES: Use markdown link format
  → [other.design.md](design/other.design.md)
```

**Example Structure (Minimal Required):**

```markdown
# [Document Name]

## 0) Document Control

> **Parent Scope:** [Project]
> **Current Version:** 1.0
> **Session:** [UUID] (YYYY-MM-DD)

---

[Your content sections - ANY structure you want]

---

> Full history: [file.changelog.md](changelog/file.changelog.md)
```

**Example Structure (Recommended):**

```markdown
# [Document Name]

## 0) Document Control

> **Parent Scope:** [Project]
> **Current Version:** 1.0
> **Session:** [UUID] (YYYY-MM-DD)

---

## Goal

[Purpose statement]

---

## Scope

[What is covered]

---

## [Any Other Sections]

[Your content]

---

> Full history: [file.changelog.md](changelog/file.changelog.md)
```

**IMPORTANT:**
- Design documents have ONLY the link to changelog (NO Version History table)
- Version History (Unified) table is ONLY in changelog.md file
- This follows document-changelog-control.md v4.3: Navigator format for design docs

### 5. Changelog Integration (Critical)

**For Design Documents (Navigator format):**

Design documents contain ONLY the link to changelog - NO version table:

```markdown
> Full history: [file.changelog.md](changelog/file.changelog.md)
```

**For Full Changelog Files:**

Changelog files contain the Version History (Unified) table:

```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[Headline](#Lxx)** | <UUID> |
| | | - Change 1 | |
| | | - Change 2 | |
| | | Summary: <One-line> | |

> Parent Document: [file.design.md](../design/file.design.md)
```

**Linking Format:**

```markdown
# Design doc → Full changelog
> Full history: [file.changelog.md](changelog/file.changelog.md)

# Design doc → Specific version
**[Headline](file.changelog.md#L42)**

# Full changelog → Design doc
> Parent Document: [file.design.md](../design/file.design.md)
```

### 6. Changelog Integration Rules

**When to create separate changelog file:**

| Condition | Create changelog? | Reason |
|-----------|-------------------|--------|
| Design doc has < 5 versions | ❌ No | Navigator in design doc is enough |
| Design doc updates frequently | ✅ Yes | Separate history before it gets too long |
| Complex changes need details | ✅ Yes | Need detailed change tracking |
| Design doc has > 5 versions | ✅ Yes | Navigator + Full changelog pattern |

**Mandatory Pattern (per document-changelog-control.md v4.3):**

When BOTH design.md AND changelog.md exist:
- design.md = ONLY link to changelog (NO table, NO entries)
- changelog.md = Full history (all versions, detailed sections)

### 7. Cross-reference Standards

**Link Formats:**

| Purpose | Format | Example |
|---------|--------|---------|
| Section link | `[file.md#section]` | `[design.md#requirements]` |
| Line number | `[file.md#Lxx]` | `[design.md#L42]` |
| Header slug | `[file.md#<slug>]` | `[design.md#version-control]` |
| External | `[text](url)` | `[GitHub](https://github.com/...)` |

**Verification Rules:**

- Check all links are valid before committing
- Use relative paths for internal links
- Update references when files move
- Test line number links after editing

---

## Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Pattern consistency | 100% | All docs follow same pattern (1 or 2) |
| Design file suffix | Pattern 2: `.design.md` | Check design files in `./design/` |
| Design location | Pattern 1: Root, Pattern 2: `./design/` | Per chosen pattern |
| Document Control section | 100% present | Verify version + session |
| Changelog link | 100% present | At design end (Navigator) |
| NO Version History table | 100% | Design docs only have link |
| Session ID accuracy | 100% real UUID | No placeholders |
| Changelog integration | Per document-changelog-control.md v4.3 | Navigator for design, Full for changelog |
| Cross-reference validity | 100% working | Test all links |

---

## Integration with Other Rules

### Related Reference

**Works together with:**
- **[document-changelog-control.md](document-changelog-control.md) v4.3**
  - Defines Version History (Unified) format
  - Establishes design.md <> changelog.md relationship
  - Specifies Navigator format for design documents

### Related Rules

| Rule | Relationship |
|------|-------------|
| **document-changelog-control.md** | Related - Defines Version History (Unified) format standard |
| **document-consistency.md** | Cross-reference validation |
| **strict-file-hygiene.md** | No duplicate/dummy design files |
| **flow-diagram-no-frame.md** | No frames/boxes in design diagrams |

### How They Work Together

```
document-changelog-control.md (v4.3)
  ↓ Defines Version History (Unified) format
  ↓ Specifies Navigator format: design.md = ONLY link

document-design-control.md (This rule)
  ↓ Defines design document structure
  ↓ Enforces .design.md naming/location
  ↓ Works with document-changelog-control.md format

document-consistency.md
  ↓ Validates cross-references work

strict-file-hygiene.md
  ↓ Prevents duplicate design files
```

---

## Compliance Checklist

Before creating a new design document:

**Step 1: Choose Pattern**
- [ ] Determine: Pattern 1 (Simple) or Pattern 2 (Complex)?
- [ ] Pattern 1: Single design → `design.md` at root
- [ ] Pattern 2: Multiple designs → `./design/*.design.md`

**Step 2: File Setup (depends on pattern)**

Pattern 1 (Simple):
- [ ] File named `design.md` (at root, no suffix)
- [ ] Changelog named `changelog.md` (at root)

Pattern 2 (Complex):
- [ ] File named `<name>.design.md` (correct suffix)
- [ ] Located in `./design/` directory
- [ ] Changelog in `./changelog/<name>.changelog.md`

**Step 3: Content Requirements (both patterns)**
- [ ] Has Document Control section (Section 0)
- [ ] Session ID is real UUID (36 characters, no placeholders)
- [ ] Version matches changelog (if exists)
- [ ] Has changelog link at end (ONLY link, NO Version History table)
- [ ] NO Version History table in design document
- [ ] All cross-references verified (test links)

---

## Examples

### ✅ Correct Design Document (Flexible Content)

```markdown
# API Gateway Design

## 0) Document Control

> **Parent Scope:** E-Commerce Platform Architecture
> **Current Version:** 1.2
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-21)

---

## 1) Goal

Design API gateway for rate limiting and authentication

---

## 2) Architecture

[Your content - ANY structure]

---

## 3) API Endpoints

[More content - ANY sections you want]

---

## 4) Security Considerations

[As many sections as needed]

---

> Full history: [api-gateway.changelog.md](changelog/api-gateway.changelog.md)
```

**Note:** Content sections (1, 2, 3, 4...) can be ANY structure you want. The rules are:
- ✅ MUST have Document Control at top
- ✅ MUST have changelog link at end
- ✅ NO Version History table
- Everything else is flexible!

**Corresponding changelog/api-gateway.changelog.md:**

```markdown
# Changelog - API Gateway Design

> **Parent Document:** [api-gateway.design.md](../design/api-gateway.design.md)

---

## Version History

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-01-21 | **[Added caching](#L45)** | a77b77ae... |
| | | - Added response caching layer | |
| | | - Configured TTL settings | |
| | | Summary: Added response caching layer | |
| 1.1 | 2026-01-15 | **[Initial release](#L1)** | a77b77ae... |
| | | - Basic gateway setup | |
| | | - Rate limiting rules | |
| | | Summary: Basic gateway setup | |

---

## Version 1.2: Added caching

**Date:** 2026-01-21
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added response caching layer
- Configured TTL settings

### Summary
Added response caching layer

---

## Version 1.1: Initial release

**Date:** 2026-01-15
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Basic gateway setup
- Rate limiting rules

### Summary
Basic gateway setup
```

### ❌ Incorrect Design Document

```markdown
# API Gateway Design v2  ← Wrong: version in name

## 1.0 Introduction  ← Wrong: no Document Control section

# Goal  ← Wrong: missing section numbering

Design API gateway

---

## Version History  ← WRONG: Design docs should NOT have this!

| Version | Date | Changes |
| 1.0 | 2026-01-21 | Added stuff |  ← WRONG: Not Version History (Unified) format

> Missing: link to changelog
```

---

## Version

| Version | Date | Notes |
|---------|------|-------|
| 1.3 | 2026-01-26 | Added Pattern 1 (Simple) for single-design projects |
| 1.2 | 2026-01-21 | Fixed terminology - "Primary Reference" → "Related Reference" |
| 1.1 | 2026-01-21 | Aligned with document-changelog-control.md v4.3 |
| 1.0 | 2026-01-21 | Initial version |

---

> Full history: [changelog/document-design-control.changelog.md](changelog/document-design-control.changelog.md)
