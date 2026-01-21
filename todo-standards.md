# TODO Standards

> **Current Version:** 2.0
> **Based on:** [todo-standards.design.md](design/todo-standards.design.md) v2.0
> **Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

> **Full history:** [changelog/changelog.md](changelog/changelog.md)

---

## Rule Statement

**Core Principle: Simple, maintainable TODO lists**

TODO.md should be simple and focused on actual work. Avoid complex systems that become stale and unmaintained.

---

## Core Requirements

### 1. Document Structure

Every TODO.md must have these sections:

```markdown
# [Project Name] - TODO

> **Session:** [Session ID]
> **Last Updated:** YYYY-MM-DD

---

## ✅ Completed
[Summary of completed work - what's done]

---

## 📋 Tasks To Do
### [Category Name]
- [ ] Task description

---

## 📜 History
| Date | Changes |
|------|---------|
```

### 2. Task Format

**Simple checkbox format:**
```markdown
- [ ] Task description here
```

**No timestamps required** (keep it simple)

### 3. Categories

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

## What Was Removed (v2.0 Simplification)

### Removed Items:
- ❌ Priority levels (P0, P1, P2, P3)
- ❌ Created/Started/Completed timestamps per task
- ❌ Status badges ([IN PROGRESS], [BLOCKED], etc.)
- ❌ Progress dashboard with metrics
- ❌ Task categorization by priority

### Why Removed:
- Complex TODO systems often become stale and unmaintained
- Simple lists are easier to keep current
- Priorities shift over time, making fixed labels inaccurate
- Deadlines are often arbitrary and missed
- Keep TODO.md focused on actual work, not overhead

---

## Compliance Checklist

When creating/updating TODO.md:

- [ ] Have Session ID in header
- [ ] Have Last Updated date
- [ ] Have Completed section (what's done)
- [ ] Have Tasks To Do section (what needs doing)
- [ ] Have History table (track changes)
- [ ] Use checkbox format `- [ ]` for tasks
- [ ] No priorities (P0-P3) - keep simple
- [ ] No deadlines - keep flexible

---

## Examples

### Example 1: Simple TODO

```markdown
# My Project - TODO

> **Session:** abc-123-def-456
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

> **Session:** abc-123-def-456

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

## Integration

### Related Rules
- [`document-design-control.md`](document-design-control.md) - Design document standards
- [`document-changelog-control.md`](document-changelog-control.md) - Changelog format (for History section)

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Simplicity | Maximum - focus on work |
| Maintainability | Easy to keep current |
| Flexibility | No artificial constraints |
| Completeness | All sections present |

---

> **Design:** [design/todo-standards.design.md](design/todo-standards.design.md) v2.0
> **Full history:** [changelog/changelog.md](changelog/changelog.md)
