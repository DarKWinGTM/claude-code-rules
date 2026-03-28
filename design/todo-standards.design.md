# TODO Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.3
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-03-28)

---

## 1) Goal

Define a simple TODO governance format that stays aligned with UDVC-1, preserves TODO as an execution-only layer, and resolves TODO presence early when meaningful governed work genuinely needs tracking.

---

## 2) Scope

Applies to `TODO.md` files used for project work tracking.

---

## 3) Core Contract

### 3.1 Execution-Only Role
`TODO.md` reflects execution state only.
It is not a version-authority document.

### 3.2 Startup Establishment Rule
When meaningful governed work requires tracking, startup TODO posture must be resolved early through `artifact-initiation-control` as one of:
- use existing
- create now
- ask now
- not required

This rule distinguishes:
- early TODO establishment when tracking is needed
- later TODO content synchronization after design/runtime/changelog changes

TODO should not be treated as retrospective backfill by default.

### 3.3 Required Structure

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

### 3.4 Pending-Only Discipline
- Pending areas contain pending tasks only.
- Completed content belongs only in `Completed` and `History`.
- Deferred work remains pending with clear text labels.

### 3.5 Simplicity Discipline
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

TODO content updates still occur last among the primary active layers.
That later content-sync order does not weaken the early startup-establishment rule.

---

## 5) Verification Checklist

- [ ] TODO keeps the required simplified structure
- [ ] Pending area contains pending tasks only
- [ ] Completed items are not mixed into pending sections
- [ ] No dashboard or priority overhead is present
- [ ] TODO startup posture is resolved early when meaningful tracking is required
- [ ] TODO content update occurs after design/runtime/changelog synchronization

---

## 6) Quality Metrics

| Metric | Target |
|--------|--------|
| Structural compliance with required sections | 100% |
| Pending-section contamination with completed tasks | 0 |
| Dashboard-style overhead artifacts | 0 |
| Execution-only role clarity | 100% |
| Startup TODO posture resolved before drift when needed | 100% |

---

## 7) Related Documents

| Document | Relationship |
|----------|--------------|
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup TODO posture resolution |
| [document-changelog-control.design.md](document-changelog-control.design.md) | Synchronization order and authority boundary |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role model |
| [../todo-standards.md](../todo-standards.md) | Runtime implementation |

---

> Full history: [../changelog/todo-standards.changelog.md](../changelog/todo-standards.changelog.md)
