# Project Documentation Standards

> **Current Version:** 1.7
> **Based on:** [project-documentation-standards.design.md](design/project-documentation-standards.design.md) v1.7
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8
>
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)

---

## Rule Statement

**Core Principle: Use one deterministic documentation baseline across README, design, runtime rules, changelog, TODO, and patch documents.**

---

## Core Requirements

### 1) Required Document Set

| Document | Required When | Purpose | Governing Rule |
|----------|---------------|---------|----------------|
| `README.md` | Always | Project overview and onboarding | Standard practice |
| `design/*.design.md` | Design/specification is required | Define target behavior/contract | `document-design-control` |
| `changelog/*.changelog.md` | Version traceability is required | Authoritative version history | `document-changelog-control` |
| `TODO.md` | Work tracking is required | Track execution state | `todo-standards` |
| `patches/*.patch.md` | Transition/migration work is required | Tactical transition plan | `document-patch-control` |

### 2) UDVC-1 Integration

#### 2.1 Version Authority

- Changelog is the single version authority per governed chain
- Design/rule/patch metadata must align with authoritative changelog state

#### 2.2 Synchronization Order

For governance updates, apply in this order:

1. design
2. runtime rule
3. changelog
4. TODO

#### 2.3 Session Integrity

- Active metadata must use real session identifiers
- Placeholder session values are not allowed in active metadata

### 3) Decision Model for Document Creation

```text
Project start
  ↓
Create README
  ↓
Need design specification?
  → YES: create design doc(s)
  ↓
Need version traceability?
  → YES: create changelog doc(s)
  ↓
Need tracked execution items?
  → YES: create TODO.md
  ↓
Need migration/transition plan?
  → YES: create patch doc(s)
```

### 4) Cross-Document Alignment Requirements

- Required document set must match project scope
- Full-history and parent-document links must resolve
- Active metadata across governed docs must not contain placeholder sessions

---

## Verification Checklist

- [ ] Required document set matches project scope
- [ ] Changelog exists for each governed chain
- [ ] Version references align across chain metadata
- [ ] Active session metadata has no placeholders
- [ ] Full-history links resolve
- [ ] TODO follows simplified standard mode

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Required document coverage | 100% |
| Version-reference correctness | 100% |
| Active metadata session integrity | 100% |
| Cross-link validity | 100% |
| TODO simplification compliance | 100% |

---

## Integration

| Rule | Relationship |
|------|-------------|
| [document-changelog-control.md](document-changelog-control.md) v4.6 | Version authority contract |
| [document-design-control.md](document-design-control.md) v1.7 | Design structure standards |
| [todo-standards.md](todo-standards.md) v2.1 | TODO structure standards |
| [document-patch-control.md](document-patch-control.md) v1.2 | Patch structure standards |

---

> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
