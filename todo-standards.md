# TODO Standards

> **Current Version:** 2.3
> **Design:** [design/todo-standards.design.md](design/todo-standards.design.md) v2.3
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)

---

## Rule Statement

**Core Principle: Keep TODO as a simple execution-tracking layer, but resolve TODO presence early for meaningful governed work instead of treating TODO creation as retrospective cleanup.**

---

## Core Contract

### 1) Execution-Only Role
`TODO.md` reflects execution state only.
It is not a version-authority document.

### 2) Startup Establishment Bridge
When meaningful governed work requires tracking, startup TODO posture must be resolved early through `artifact-initiation-control` as one of:
- use existing
- create now
- ask now
- not required

TODO establishment at startup is different from TODO content updates later.

### 3) Required Structure

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

### 4) Pending-Only Discipline
- Pending areas contain pending tasks only.
- Completed content belongs only in `Completed` and `History`.
- Deferred work remains pending with clear text labels.

### 5) Simplicity Discipline
Do not require:
- dashboard counters
- priority grids
- per-task timestamps
- deadline fields
- execution telemetry blocks

---

## Synchronization Contract

When governance work changes governed artifacts, update in this order:
1. design
2. runtime rule
3. changelog
4. TODO

TODO content updates still happen last among the primary active layers.
That later sync order does not weaken the early startup-establishment rule.

---

## Verification Checklist

- [ ] TODO keeps the required simplified structure
- [ ] Pending area contains pending tasks only
- [ ] Completed items are not mixed into pending sections
- [ ] No dashboard or priority overhead is present
- [ ] TODO startup posture was resolved early when meaningful tracking was required
- [ ] TODO content update occurred after design/runtime/changelog synchronization

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Structural compliance with required sections | 100% |
| Pending-section contamination with completed tasks | 0 |
| Dashboard-style overhead artifacts | 0 |
| Execution-only role clarity | 100% |
| Startup TODO posture resolved before drift when needed | 100% |

---

## Integration

Related documents:
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup TODO posture resolution
- [document-changelog-control.md](document-changelog-control.md) - synchronization order and authority boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository role model

---

> **Full history:** [changelog/todo-standards.changelog.md](changelog/todo-standards.changelog.md)
