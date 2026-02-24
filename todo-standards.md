# TODO Standards

> **Current Version:** 2.1
> **Based on:** [todo-standards.design.md](design/todo-standards.design.md) v2.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8
>
> **Full history:** [changelog/changelog.md](changelog/changelog.md)

---

## Rule Statement

**Core Principle: Keep TODO simple, maintainable, and synchronized after governance updates.**

TODO reflects execution state, not version authority.

---

## Core Requirements

### 1) Required Structure

Every `TODO.md` must use this structure:

```markdown
# <Project Name> - TODO

> **Last Updated:** YYYY-MM-DD

---

## ✅ Completed
<summary or completed checklist>

---

## 📋 Tasks To Do
### <Optional Category>
- [ ] <task>

---

## 📜 History
| Date | Changes |
|------|---------|
```

### 2) Task Format

- Use checkbox format only: `- [ ]` and `- [x]`
- Keep tasks concise and actionable
- Categories are optional

### 3) Governance Constraints

- Pending area must contain pending tasks only
- Completed content belongs only in `Completed` and `History`
- If deferred items exist, keep them as pending tasks with clear labels (for example: `Deferred`)

### 4) Simplicity Contract

The following are not part of TODO standard mode:

- Priority levels (P0/P1/P2/P3)
- Dashboard counters/metrics blocks
- Per-task timestamps
- Deadline fields

### 5) Integration Contract

- TODO updates occur after design/runtime/changelog synchronization
- Changelog remains version authority for governed document chains
- TODO tracks execution state only

### 6) Synchronization Order

1. design
2. runtime rule
3. changelog
4. TODO

---

## Compliance Checklist

- [ ] Required TODO sections are present
- [ ] Task list uses checkbox format
- [ ] Pending section has pending tasks only
- [ ] Completed items are not mixed into pending section
- [ ] No dashboard/priority/deadline overhead artifacts
- [ ] TODO updated after design/runtime/changelog sync

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Structural compliance with required sections | 100% |
| Pending-section contamination with completed tasks | 0 |
| Priority/deadline/dashboard overhead artifacts | 0 |
| Readability and maintainability | High |

---

## Integration

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.md](document-changelog-control.md) v4.6 | Synchronization order and authority model |
| [project-documentation-standards.md](project-documentation-standards.md) v1.7 | Project-level doc governance |

---

> **Design:** [design/todo-standards.design.md](design/todo-standards.design.md) v2.1
> **Full history:** [changelog/changelog.md](changelog/changelog.md)
