# Project Documentation Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.7
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-23)

---

## 1) Goal

Provide one deterministic, low-complexity documentation governance baseline across README, design, runtime rules, changelog, TODO, and patch documents.

---

## 2) Scope

Applies to new and existing projects that maintain governed documentation artifacts.

---

## 3) Required Document Set

| Document | Required When | Purpose | Governing Rule |
|----------|---------------|---------|----------------|
| `README.md` | Always | Project overview and onboarding | Standard practice |
| `design/*.design.md` | Design/specification needed | Define target behavior/contract | `document-design-control` |
| `changelog/*.changelog.md` | Version traceability required | Authoritative version history | `document-changelog-control` |
| `TODO.md` | Work tracking required | Track execution state | `todo-standards` |
| `patches/*.patch.md` | Transition/migration work required | Tactical transition plan | `document-patch-control` |

---

## 4) UDVC-1 Integration

### 4.1 Version Authority

- Changelog is the single version authority per chain.
- Design/rule/patch metadata must align with authoritative changelog state.

### 4.2 Synchronization Order

When applying governance updates:

1. design
2. runtime rule
3. changelog
4. TODO

### 4.3 Session Integrity

- Active metadata fields use real session identifiers.
- Placeholder session values are not allowed in active metadata.

---

## 5) Decision Model for Document Creation

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

---

## 6) Verification Checklist

- [ ] Required document set matches project scope
- [ ] Changelog exists for each governed chain
- [ ] Version references are aligned across chain metadata
- [ ] Active session metadata has no placeholders
- [ ] Full-history links resolve
- [ ] TODO follows simplified standard

---

## 7) Quality Metrics

| Metric | Target |
|--------|--------|
| Required document coverage | 100% |
| Version-reference correctness | 100% |
| Active metadata session integrity | 100% |
| Cross-link validity | 100% |
| TODO simplification compliance | 100% |

---

## 8) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Version authority contract |
| [document-design-control.design.md](document-design-control.design.md) | Design structure standards |
| [todo-standards.design.md](todo-standards.design.md) | TODO structure standards |
| [document-patch-control.design.md](document-patch-control.design.md) | Patch structure standards |

---

> Full history: [../changelog/project-documentation-standards.changelog.md](../changelog/project-documentation-standards.changelog.md)
