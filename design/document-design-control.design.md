# Document Design Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.2
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-21)

---

## 1) Goal (เป้าหมาย)

- สร้างมาตรฐานเดียวกันสำหรับ design documents ทั้งหมด
- ควบคุมคุณภาพและความสอดคล้องของ design documents
- ทำให้การทำงานร่วมกันระหว่าง design, changelog และ TODO เป็นไปอย่างง่าย
- รักษา Single Source of Truth principle

---

## 2) Scope (ขอบเขต)

### 2.1 Documents Covered

- Design documents (`.design.md`)
- Rules files created from design
- Changelog files
- TODO/task tracking

### 2.2 Standards Defined

- File naming conventions
- File location standards
- Document structure requirements
- Changelog integration patterns
- TODO tracking integration
- Cross-reference methods

---

## 3) Standards (มาตรฐาน)

### 3.1 File Naming Standards

| File Type | Format | Example |
|-----------|--------|---------|
| Design Document | `<name>.design.md` | `document-design-control.design.md` |
| Changelog File | `<name>.changelog.md` | `document-design-control.changelog.md` |
| Rules File | `<name>.md` | `document-design-control.md` |

### 3.2 Location Standards

```
./
├── design/
│   ├── <name>.design.md      ← Design documents
│   └── ...
├── changelog/
│   ├── changelog.md          ← Master changelog (optional)
│   └── <name>.changelog.md   ← Specific changelogs
├── <name>.md                 ← Rules files (from design)
└── README.md
```

### 3.3 Design Document Structure

**Required Sections:**

1. **Document Control** (Section 0) - MANDATORY
   - Parent Scope
   - Current Version
   - Session ID (real UUID)

2. **Goal** (Section 1)
   - Purpose statement

3. **Scope** (Section 2)
   - What is covered

4. **[Other Sections]** (Sections 3+)
   - Main content (FLEXIBLE - any structure)

5. **Changelog Link** (Last line) - MANDATORY
   - `> Full history: [<doc>.changelog.md](changelog/<doc>.changelog.md)`

**CRITICAL:**
- NO Version History table in design documents (per document-changelog-control.md v4.3)
- Design documents contain ONLY the link to changelog
- Content sections (Goal, Scope, etc.) are flexible and optional

### 3.4 Document Control Section Format

```markdown
## 0) Document Control

> **Parent Scope:** [Parent project/system]
> **Current Version:** X.Y
> **Session:** [UUID] (YYYY-MM-DD)
```

### 3.5 Version History (Unified) Format

**CRITICAL: Follows document-changelog-control.md v4.3**

**For Design Documents (Navigator format):**
```markdown
> Full history: [<doc>.changelog.md](changelog/<doc>.changelog.md)
```

**Key Points:**
- Design documents contain ONLY the link to changelog
- NO Version History table in design documents
- NO version entries in design documents
- This is called "Navigator" format per document-changelog-control.md

**For Changelog Files (Full format):**
```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[Headline](#L1)** | <UUID> |
| | | - Change 1 | |
| | | - Change 2 | |
| | | Summary: <One-line summary> | |

> Parent Document: [<doc>.design.md](../design/<doc>.design.md)
```

**Reference:** See [document-changelog-control.md](../document-changelog-control.md) for complete rules

---

## 4) Changelog Integration (การผนวกรวม Changelog)

> **Based on:** [document-changelog-control.md](../document-changelog-control.md) v4.3

### 4.1 Design Documents (Navigator Format)

**Design documents contain ONLY the link to changelog:**
```markdown
> Full history: [<doc>.changelog.md](changelog/<doc>.changelog.md)
```

**Key Rules:**
- NO Version History table in design documents
- NO version entries in design documents
- ONLY the link to changelog
- All version details go in changelog file

**Why?**
- Design documents are specifications (current state)
- Changelog files track history (all changes)
- Prevents duplication
- Single Source of Truth

### 4.2 Full Changelog Files

**When to create:**
- Design doc updates frequently
- Complex changes need detailed tracking
- Design doc has > 5 versions

**Format: Detailed Sections**
- Each version = separate section
- Full change details with bullet points
- Link back to design document

### 4.3 Linking Format

```markdown
# Design doc → Full changelog
> Full history: [<doc>.changelog.md](changelog/<doc>.changelog.md)

# Design doc → Specific version
**[Headline](<doc>.changelog.md#L42)**

# Full changelog → Design doc
> Parent Document: [<doc>.design.md](../design/<doc>.design.md)
```

---

## 5) TODO/Task Integration (การผนวก TODO)

### 5.1 TODO.md Format

**Organize by status:**
- ✅ Completed Tasks
- 🔄 In Progress
- 📋 Pending Tasks

**Checkbox format:**
```markdown
- [x] Completed task
- [ ] Pending task
```

### 5.2 Task Detail Format

```markdown
### [Category]
- [x] **Task name** - Brief description of what was done
- [ ] **Task name** - Description (Started: YYYY-MM-DD)
```

### 5.3 Design Document References

**In TODO.md:**
```markdown
### [Category]
- [ ] **Task for <design-name>.design.md** - Description
```

**In design document:**
```markdown
## Implementation Status

**Related Tasks:** See [TODO.md](../TODO.md)
```

---

## 6) Cross-reference Standards (มาตรฐานการอ้างอิง)

### 6.1 Link Formats

| Purpose | Format | Example |
|---------|--------|---------|
| Section link | `[file.md#section]` | `[design.md#requirements]` |
| Line number | `[file.md#Lxx]` | `[design.md#L42]` |
| Header link | `[file.md#<slug>]` | `[design.md#version-control]` |
| External | `[text](url)` | `[GitHub](https://github.com/...)` |

### 6.2 Cross-reference Verification

**Before committing:**
- Check all links are valid
- Update references when files move
- Use relative paths for internal links

---

## 7) Examples (ตัวอย่าง)

### 7.1 Complete Design Document

```markdown
# [Document Name]

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-20)

---

## 1) Goal

[Purpose]

---

## 2) Scope

[Coverage]

---

## 3) Requirements

[Details]

---

> Full history: [doc.changelog.md](changelog/doc.changelog.md)
```

**NOTE:**
- NO Version History table in design document
- ONLY the link to changelog
- Follows document-changelog-control.md v4.3 rules

### 7.2 Design with Changelog

**design/doc.design.md:**
```markdown
# [Document Name]

## 0) Document Control

> **Parent Scope:** [Project]
> **Current Version:** 2.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-20)

---

[Content sections...]

---

> Full history: [doc.changelog.md](changelog/doc.changelog.md)
```

**changelog/doc.changelog.md:**
```markdown
# Changelog - Doc

> **Parent:** [doc.design.md](../design/doc.design.md)

---

## Version History

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.0 | 2026-01-20 | **[Added Section 5](#L50)** | a77b77ae... |
| | | - Added Section 5: New features | |
| | | - Updated examples | |
| | | Summary: Enhanced with new features | |
| 1.0 | 2026-01-15 | **[Initial version](#L1)** | a77b77ae... |
| | | - Initial release | |
| | | Summary: Created design document | |

---

## Version 2.0: Added Section 5

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added Section 5: New features
- Updated examples

### Summary
Enhanced with new features
```

**Key Pattern:**
- design.md = ONLY the link (NO table)
- changelog.md = Version History (Unified) table + detailed sections

---

## 8) Quality Metrics (ตัวชี้วัด)

| Metric | Target | Notes |
|--------|--------|-------|
| Design file suffix | 100% `.design.md` | All in `./design/` |
| Document Control section | 100% present | Version + Session |
| Changelog link | 100% present | At design end (Navigator) |
| NO Version History table | 100% | Design docs only have link |
| Session ID accuracy | 100% real UUID | No placeholders |
| Cross-reference validity | 100% working | All links verify |
| Changelog file exists | When needed | Per document-changelog-control.md v4.3 |
| TODO tracking | Major tasks | In TODO.md |

---

## 9) Related Documents (เอกสารที่เกี่ยวข้อง)

| Document | Relationship | Purpose |
|----------|--------------|---------|
| **[document-changelog-control.md](../document-changelog-control.md)** | Related Reference | Defines Version History (Unified) format and design.md <> changelog.md relationship |
| [document-changelog-control.changelog.md](../changelog/document-changelog-control.changelog.md) | Example | Full changelog with detailed sections |
| [document-design-control.md](../document-design-control.md) | Rules implementation | Enforces these design standards |
| [../TODO.md](../TODO.md) | Task tracking | TODO/task tracking integration |

**NOTE:** This design.spec is based on and must comply with [document-changelog-control.md](../document-changelog-control.md) v4.3

---

> Full history: [document-design-control.changelog.md](changelog/document-design-control.changelog.md)
