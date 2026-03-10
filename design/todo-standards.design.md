# TODO Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.2
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2 (2026-03-08)

---

## 1) Goal

Define a simple TODO governance format that stays aligned with UDVC-1 and does not reintroduce dashboard-style noise or version-authority confusion.

---

## 2) Scope

Applies to `TODO.md` files used for project work tracking.

---

## 3) Core Contract

### 3.1 Execution-Only Role

`TODO.md` reflects execution state only.
It is not a version-authority document.

### 3.2 Required Structure

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

### 3.3 Pending-Only Discipline

- Pending areas contain pending tasks only.
- Completed content belongs only in `Completed` and `History`.
- Deferred work remains pending with clear text labels.

### 3.4 Simplicity Discipline

Do not require:

- dashboard counters
- priority grids
- per-task timestamps
- deadline fields
- execution telemetry blocks

---

## 4) Synchronization Contract

When governance work changes governed artifacts, update in this order:

1. design
2. runtime rule
3. changelog
4. TODO

TODO is updated last among the primary active layers.

---

## 5) Verification Checklist

- [ ] TODO keeps the required simplified structure
- [ ] Pending area contains pending tasks only
- [ ] Completed items are not mixed into pending sections
- [ ] No dashboard or priority overhead is present
- [ ] TODO update occurred after design/runtime/changelog synchronization

---

## 6) Quality Metrics

| Metric | Target |
|--------|--------|
| Structural compliance with required sections | 100% |
| Pending-section contamination with completed tasks | 0 |
| Dashboard-style overhead artifacts | 0 |
| Execution-only role clarity | 100% |

---

## 7) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Synchronization order and authority boundary |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role model |
| [../todo-standards.md](../todo-standards.md) | Runtime implementation |

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
