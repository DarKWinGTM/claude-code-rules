# Document Design Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-20)

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

1. **Document Control** (Section 0)
   - Parent Scope
   - Current Version
   - Session ID

2. **Goal** (Section 1)
   - Purpose statement

3. **Scope** (Section 2)
   - What is covered

4. **[Other Sections]** (Sections 3+)
   - Main content

5. **References** (Optional)
   - Related documents

6. **Version History (Unified)** (Last section)
   - Navigator format (2-3 latest versions)

### 3.4 Document Control Section Format

```markdown
## 0) Document Control

> **Parent Scope:** [Parent project/system]
> **Current Version:** X.Y
> **Session:** [UUID] (YYYY-MM-DD)
```

### 3.5 Version History (Unified) Format

**For Design Documents (Navigator):**
```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[Headline](<doc>.changelog.md#L1)** | <UUID> |
| | | Summary: <One-line summary> | |

> Full history: [<doc>.changelog.md](changelog/<doc>.changelog.md)
```

---

## 4) Changelog Integration (การผนวกรวม Changelog)

### 4.1 Design Documents

**Use Navigator Format (2-3 latest versions):**
- Short entries with headline + summary
- Link to full changelog
- Line number links: `#Lxx`

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

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-01-20 | **Initial version** | a77b77ae... |
| | | Summary: Created design document | |

> Full history: [doc.changelog.md](changelog/doc.changelog.md)
```

### 7.2 Design with Changelog

**design/doc.design.md:**
```markdown
## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.0 | 2026-01-20 | **[Added Section 5](doc.changelog.md#L50)** | a77b77ae... |
| | | Summary: Enhanced with new features | |

> Full history: [doc.changelog.md](changelog/doc.changelog.md)
```

**changelog/doc.changelog.md:**
```markdown
# Changelog - Doc

> **Parent:** [doc.design.md](../design/doc.design.md)

## Version 2.0

**Date:** 2026-01-20
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Added Section 5: New features
- Updated examples

### Summary
Enhanced with new features
```

---

## 8) Quality Metrics (ตัวชี้วัด)

| Metric | Target | Notes |
|--------|--------|-------|
| Design file suffix | 100% `.design.md` | All in `./design/` |
| Document Control section | 100% present | Version + Session |
| Version History | 100% present | At design end |
| Session ID accuracy | 100% real UUID | No placeholders |
| Cross-reference validity | 100% working | All links verify |
| Changelog integration | As needed | Navigator or Full |
| TODO tracking | Major tasks | In TODO.md |

---

## 9) Related Documents (เอกสารที่เกี่ยวข้อง)

- [document-changelog-control.md](../document-changelog-control.md) - Version tracking
- [../changelog/document-changelog-control.changelog.md](../changelog/document-changelog-control.changelog.md) - Changelog example
- [../TODO.md](../TODO.md) - Task tracking
- [document-design-control.md](../document-design-control.md) - Rules implementation

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-01-20 | **Initial version** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | - Created design control standards for design documents | |
| | | - Defined file naming: `.design.md` suffix | |
| | | - Established location: `./design/` subdirectory | |
| | | - Specified Document Control section format | |
| | | - Created design structure standards | |
| | | - Integrated changelog system requirements | |
| | | - Added TODO/task tracking integration | |
| | | - Defined cross-reference standards | |
| | | Summary: Initial version with comprehensive design standards | |

> Full history: [document-design-control.changelog.md](changelog/document-design-control.changelog.md)
