# TODO Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 (2026-01-21)
> **Design:** [../design.md](../design.md) v1.4

---

## 1) Goal (goal)

Create a common standard for easy, usable TODO.md.

---

## 2) Scope

### 2.1 Documents Covered

- TODO.md main project
- TODO for sub-projects or modules

### 2.2 Standards Defined

- Simple document structure
- Task format and checkbox
- Completed / Tasks To Do separated
- History tracking easily

---

## 3) Standards

### 3.1 Document Structure

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

### 3.2 Task Format

**Simple checkbox format:**
```markdown
- [ ] Task description here
```

**No timestamps required** (keep it simple)

### 3.3 Categories (categories)

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

## 4) Examples

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

## 5) Compliance Checklist (checklist compliance)

When creating/updating TODO.md:

- [ ] has Last Updated date
- [ ] There is a Completed section (things that have been completed)
- [ ] There is a Tasks To Do section (things that need to be done)
- [ ] There is a History table (track changes)
- [ ] Use checkbox format `- [ ]` for tasks.
- [ ] No priorities (P0-P3) - keep simple
- [ ] No deadlines - keep flexible

---

## 6) Integration (linking tasks)

### Related Rules

- [`document-design-control.md`](../document-design-control.md) - Design document standards
- [`document-changelog-control.md`](../document-changelog-control.md) - Changelog format (for History section)

---

## 7) Notes

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
