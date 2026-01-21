# TODO Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-21)
> **Design:** [../design.md](../design.md) v1.4

---

## 1) Goal (เป้าหมาย)

สร้างมาตรฐานเดียวกันสำหรับ TODO.md ที่ง่าย และใช้งานได้จริง

---

## 2) Scope (ขอบเขต)

### 2.1 Documents Covered

- TODO.md หลักของ project
- TODO สำหรับ sub-projects หรือ modules

### 2.2 Standards Defined

- โครงสร้างเอกสารแบบง่าย
- Task format และ checkbox
- Completed / Tasks To Do แยกส่วน
- History tracking อย่างง่าย

---

## 3) Standards (มาตรฐาน)

### 3.1 Document Structure (โครงสร้างเอกสาร)

```markdown
# [Project Name] - TODO

> **Last Updated:** YYYY-MM-DD

---

## ✅ Completed

[Summary of completed work - what's done]

---

## 📋 Tasks To Do

### [Category Name]

- [ ] Task description
- [ ] Another task

---

## 📜 History

| Date | Changes |
|------|---------|
| YYYY-MM-DD | Description |
```

### 3.2 Task Format (รูปแบบ Task)

**Simple checkbox format:**
```markdown
- [ ] Task description here
```

**No timestamps required** (keep it simple)

### 3.3 Categories (หมวดหมู่)

**Optional categories** - Use only if helpful:

```markdown
### Documentation
- [ ] Create user guide
- [ ] Update API docs

### Features
- [ ] Add new authentication
- [ ] Implement caching
```

**No priorities** (P0, P1, P2, P3) - keep simple

**No deadlines** - tasks get done when they get done

---

## 4) Examples (ตัวอย่าง)

### Example 1: Simple TODO

```markdown
# My Project - TODO

> **Last Updated:** 2026-01-21

---

## ✅ Completed

- Project setup
- Database schema designed

---

## 📋 Tasks To Do

### Features
- [ ] User authentication
- [ ] Data export functionality
- [ ] Admin dashboard

### Bug Fixes
- [ ] Fix login redirect issue
- [ ] Resolve memory leak

---

## 📜 History

| Date | Changes |
|------|---------|
| 2026-01-21 | Initial TODO |
```

### Example 2: Minimal TODO

```markdown
# TODO

---

## 📋 Tasks To Do

- [ ] Review PR #42
- [ ] Update dependencies
- [ ] Write unit tests

---

## 📜 History

| Date | Changes |
|------|---------|
| 2026-01-21 | Created TODO |
```

---

## 5) Compliance Checklist (checklist ความสอดคล้อง)

เมื่อสร้าง/อัปเดต TODO.md:

- [ ] มี Last Updated date
- [ ] มี Completed section (สิ่งที่ทำเสร็จ)
- [ ] มี Tasks To Do section (สิ่งที่ต้องทำ)
- [ ] มี History table (track การเปลี่ยนแปลง)
- [ ] ใช้ checkbox format `- [ ]` สำหรับ tasks
- [ ] ไม่มี priorities (P0-P3) - keep simple
- [ ] ไม่มี deadlines - keep flexible

---

## 6) Integration (การเชื่อมโยงงาน)

### Related Rules

- [`document-design-control.md`](../document-design-control.md) - Design document standards
- [`document-changelog-control.md`](../document-changelog-control.md) - Changelog format (for History section)

---

## 7) Notes (บันทึก)

### Key Changes from v1.0

**Removed (Simplification):**
- ❌ Priority levels (P0, P1, P2, P3)
- ❌ Created/Started/Completed timestamps per task
- ❌ Status badges ([IN PROGRESS], [BLOCKED], etc.)
- ❌ Progress dashboard with metrics
- ❌ Task categorization by priority

**Added (Simplicity):**
- ✅ Simple "Completed" summary
- ✅ Optional categories for organization
- ✅ Flexible task list without complexity
- ✅ Focus on what needs to get done

**Rationale:**
- Complex TODO systems often become stale and unmaintained
- Simple lists are easier to keep current
- Priorities shift over time, making fixed P0-P3 labels inaccurate
- Deadlines are often arbitrary and missed
- Keep TODO.md focused on actual work, not overhead

---

> **Design:** [../design.md](../design.md) v1.4
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
