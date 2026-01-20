# Document Design Control

> **Current Version:** 1.0
> **Based on:** document-changelog-control.design.md v4.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

---

## Rule Statement

**Core Principle: Every design document must follow consistent standards with proper changelog integration and task traceability**

This rule ensures all design documents maintain:
- Consistent file naming and location
- Proper changelog integration following Version History (Unified) standards
- Clear task tracking and traceability
- Cross-referencing between design, changelog, and TODO

---

## Core Requirements

### 1. Design File Standards (Mandatory)

**Required Actions:**
- All design files MUST use `.design.md` suffix
- All design files MUST be located in `./design/` subdirectory
- Design files MUST have **Document Control** section at the top
- Design files MUST have **Version History (Unified)** section at the end
- Session IDs MUST be real values from environment (`<env>` tags)

### 2. Design Structure Standards

**Required Sections:**
1. **Document Control** - Version, Session, Parent Scope
2. **Table of Contents** - For documents > 50 lines
3. **Goal/Purpose** - Clear objective statement
4. **Scope** - What is covered
5. **Main Content** - Core design sections
6. **Examples** - Practical examples where applicable
7. **References** - Links to related documents
8. **Version History (Unified)** - At the end of file

### 3. Changelog Integration

**For Design Documents:**
- Use **Version History (Unified) Navigator** format (2-3 latest versions)
- Each entry = Headline + 1-line summary
- Include link to full changelog: `> Full history: [<doc>.changelog.md](changelog/<doc>.changelog.md)`

**When Full Changelog Exists:**
- Create separate `<doc>.changelog.md` file
- Full changelog uses **Detailed sections** format (all versions)
- Design doc links to full changelog with line numbers: `#Lxx`

### 4. TODO/Task Tracking Integration

**Required Actions:**
- Major design tasks MUST be tracked in TODO.md
- Use checkbox format: `[ ]` for pending, `[x]` for completed
- Organize by status: Completed, In Progress, Pending
- Reference design document in TODO entries
- Reference TODO entries in design document for traceability

**TODO Entry Format:**
```markdown
### [Category Name]
- [ ] Task description related to <design-name>.design.md
- [x] Completed task for <design-name>.design.md
```

### 5. Cross-reference Standards

**Required Actions:**
- Use `[<file>.md#<section>]` format for internal links
- Use `[<file>.md#L<line>]` format for line number links
- Update cross-references when files are restructured
- Verify all links are valid before committing

---

## Design File Standards

### File Naming Convention

| Type | Format | Example |
|------|--------|---------|
| Design Document | `<name>.design.md` | `document-changelog-control.design.md` |
| Changelog File | `<name>.changelog.md` | `document-changelog-control.changelog.md` |
| Rules File | `<name>.md` | `document-changelog-control.md` |

### Location Standards

```
./
├── design/
│   ├── <name>.design.md      ← Design documents
│   └── ...
├── changelog/
│   ├── changelog.md          ← Master changelog (if used)
│   ├── <name>.changelog.md   ← Specific changelogs
│   └── ...
├── <name>.md                 ← Rules files (from design)
└── README.md
```

### Document Control Section Format

```markdown
## 0) Document Control

> **Parent Scope:** [Parent project/system]
> **Current Version:** X.Y
> **Session:** [UUID] (YYYY-MM-DD)
```

---

## Version History (Unified) Format

### For Design Documents (Navigator - 2-3 versions)

```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[Headline](<doc>.changelog.md#L1)** | <UUID> |
| | | Summary: <One-line summary> | |
| X.X | YYYY-MM-DD | **[Headline](<doc>.changelog.md#L15)** | <UUID> |
| | | Summary: <One-line summary> | |

> Full history: [<doc>.changelog.md](changelog/<doc>.changelog.md)
```

### Entry Format

```markdown
| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 4.0 | 2026-01-20 | **[Added Feature X](doc.changelog.md#L42)** | a77b77ae... |
| | | - Added Section 5: New functionality | |
| | | - Updated examples | |
| | | Summary: Implemented feature X for better Y | |
```

---

## Changelog Integration Examples

### Example 1: Design Document with Full Changelog

**design.md (Navigator):**
```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 4.0 | 2026-01-20 | **[Document Design Control](document-design-control.changelog.md#L1)** | a77b77ae... |
| | | Summary: Initial version with design standards | |

> Full history: [document-design-control.changelog.md](changelog/document-design-control.changelog.md)
```

**changelog/document-design-control.changelog.md (Full):**
```markdown
# Changelog - Document Design Control

> **Parent Document:** [document-design-control.design.md](../design/document-design-control.design.md)
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

---

## Version 1.0: Initial Version

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Created initial design control standards
- Defined file naming conventions
- Established changelog integration rules
- Added TODO/task tracking integration
- Specified cross-reference standards

### Summary
Initial version with comprehensive design standards

### Links
- Design: [document-design-control.design.md#version-10](../design/document-design-control.design.md)
```

### Example 2: Design Document without Full Changelog

**design.md (Self-contained):**
```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-01-20 | **Initial design** | a77b77ae... |
| | | - Created basic structure | |
| | | - Added core requirements | |
| | | Summary: First version | |
```

---

## TODO/Task Tracking Integration

### TODO.md Organization

```markdown
# TODO

---

## ✅ Completed Tasks

### Design System
- [x] Create document-changelog-control v4.0
- [x] Define design vs product file distinction
- [x] Establish Single Source of Truth principle

### Documentation
- [x] Update README.md v1.2.0
- [x] Translate TODO.md to English

---

## 🔄 In Progress

### [Category]
- [ ] Task description for <design-name>.design.md
- [ ] Another task related to <design-name>.design.md

---

## 📋 Pending Tasks

### [Category]
- [ ] Future task for <design-name>.design.md
- [ ] Create image for img/<design-name>.png

---

> **Session**: <UUID>
> **Last Updated**: YYYY-MM-DD
```

### Referencing TODO in Design Documents

**In design.md:**
```markdown
## Implementation Status

**Current Status:** See [TODO.md](../TODO.md) for task tracking

**Related Tasks:**
- Task 1: Create initial design structure
- Task 2: Define standards
- Task 3: Create examples
```

---

## Cross-reference Standards

### Link Format Guidelines

| Purpose | Format | Example |
|---------|--------|---------|
| Section link | `[file.md#section]` | `[design.md#requirements]` |
| Line number link | `[file.md#Lxx]` | `[design.md#L42]` |
| Header link | `[file.md#<slug>]` | `[design.md#version-control]` |
| External link | `[text](url)` | `[GitHub](https://github.com/...)` |

### Cross-reference Verification

**Before Committing:**
```bash
# Find all markdown links
grep -r '\[.*\]('*.md

# Find all broken links (requires tool)
# Or use markdown linter
```

---

## Quality Metrics

| Metric | Target | Notes |
|--------|--------|-------|
| **Design file suffix** | 100% `.design.md` | All design files must use correct suffix |
| **Location compliance** | 100% in `./design/` | No design files in root |
| **Document Control section** | 100% present | Must have version and session |
| **Version History** | 100% present | Must have at design end |
| **Session ID accuracy** | 100% real UUID | No placeholders or mock data |
| **Cross-reference validity** | 100% working | All links must verify |
| **TODO integration** | Required for major tasks | Tracked in TODO.md |

---

## Compliance Checklist

### Before Creating Design Document

- [ ] File named `<name>.design.md`
- [ ] Located in `./design/` directory
- [ ] Document Control section at top
- [ ] Table of Contents (if > 50 lines)
- [ ] Clear purpose and scope
- [ ] Version History (Unified) at end
- [ ] Session ID from `<env>` tags

### Before Creating Changelog

- [ ] File named `<name>.changelog.md`
- [ ] Located in `./changelog/` directory
- [ ] Parent document link at top
- [ ] Detailed sections for each version
- [ ] Session ID from `<env>` tags
- [ ] Link back to design document

### Before Updating TODO.md

- [ ] Use checkbox format `[ ]` / `[x]`
- [ ] Organized by status (Completed, In Progress, Pending)
- [ ] Clear task descriptions
- [ ] Reference design documents
- [ ] Session ID and date at bottom

---

## Reserved Terms

| Term | Usage | Notes |
|------|-------|-------|
| `.design.md` | Design document suffix | For design specifications only |
| `.changelog.md` | Changelog file suffix | For version history only |
| `Version History (Unified)` | Standard format | Use exact phrase |
| `Document Control` | Header section | First section in design files |
| `Navigator` | Short version history | 2-3 latest versions |

---

## Examples

### Complete Design Document Structure

```markdown
# [Document Name]

## 0) Document Control

> **Parent Scope:** [Project/System]
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-20)

---

## 1) Goal

[Purpose statement]

---

## 2) Scope

[What is covered]

---

## 3) Requirements

[Detailed requirements]

---

## 4) Examples

[Code examples]

---

## 5) References

- [Related document 1](../doc1.md)
- [Related document 2](../doc2.md)

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-01-20 | **Initial version** | a77b77ae... |
| | | Summary: Created design document | |

> Full history: [doc.changelog.md](changelog/doc.changelog.md)
```

---

## Related Documents

- [document-changelog-control.md](document-changelog-control.md) - Changelog version control
- [strict-file-hygiene.md](strict-file-hygiene.md) - File creation standards
- [TODO.md](TODO.md) - Task tracking

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-01-20 | **Initial version** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Created design control standards | |
| | | - Integrated changelog system requirements | |
| | | - Added TODO/task tracking integration | |
| | | - Defined cross-reference standards | |
| | | Summary: Initial version with comprehensive design standards | |

> Full history: [document-design-control.changelog.md](changelog/document-design-control.changelog.md)
