# TODO Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-23)

---

## 1) Goal

Define a simple TODO governance format that remains maintainable over time and aligned with UDVC-1 synchronization policy.

---

## 2) Scope

Applies to `TODO.md` documents used for project work tracking.

---

## 3) Required Structure

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

---

## 4) Task Format Rules

- Use checkbox format only: `- [ ]` and `- [x]`
- Keep tasks concise and actionable
- Categories are optional
- Do not require per-task timestamps
- Do not require priority labels

---

## 5) Governance Constraints

- Pending area must contain pending tasks only.
- Completed content belongs only in `Completed` and `History` areas.
- If deferred items exist, keep them as pending tasks with clear text labels (for example: `Deferred`), not dashboard counters.

---

## 6) Integration Contract

- TODO updates occur after design/runtime/changelog synchronization.
- TODO reflects execution state; changelog remains version authority for governed documents.

---

## 7) Quality Metrics

| Metric | Target |
|--------|--------|
| Structural compliance with standard sections | 100% |
| Pending-section contamination with completed tasks | 0 |
| Priority/deadline overhead artifacts | 0 |
| Readability and maintainability | High |

---

## 8) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Governs synchronization order |
| [../todo-standards.md](../todo-standards.md) | Runtime implementation |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Project-level doc governance |

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
