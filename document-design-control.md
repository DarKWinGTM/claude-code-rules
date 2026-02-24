# Document Design Control

> **Current Version:** 1.7
> **Based on:** [document-design-control.design.md](design/document-design-control.design.md) v1.7
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8
>
> **Full history:** [changelog/document-design-control.changelog.md](changelog/document-design-control.changelog.md)

---

## Rule Statement

**Core Principle: Design documents must use one deterministic structure aligned with UDVC-1 governance.**

Design files are navigator documents. Authoritative version state is controlled by changelog files.

---

## Core Requirements

### 1) Naming and Location

- Design documents use `<name>.design.md`
- Design documents live in `design/`
- Authoritative changelog files live in `changelog/<name>.changelog.md`

### 2) Mandatory Metadata (Design Docs)

Each design document must include:

- `Parent Scope`
- `Current Version`
- `Session` (real session ID)
- `Full history` link

### 3) Pair Behavior (Design + Changelog)

When both files exist for one chain:

| File | MUST use | MUST NOT use |
|------|----------|--------------|
| `*.design.md` | Navigator link-only (`Full history`) | Embedded version table or detailed changelog sections |
| `*.changelog.md` | Detailed version sections + `Version History (Unified)` | Detailed-only or table-only format |

### 4) Rule-Chain Triad Alignment (Mandatory)

For rule-governed chains, these values must match:

- Rule `Current Version`
- Rule `Based on` design version
- Design `Current Version`
- Changelog `Current Version`

### 5) Canonical Anchor Policy

- Version-navigation links must use canonical `#version-xy` anchors
- Line-number anchors (`#Lxx`) must not be used as version-navigation standard

### 6) Synchronization Order (Non-Negotiable)

For governance updates:

1. design
2. runtime rule
3. changelog
4. TODO

---

## Required Design Template

```markdown
# <Document Name>

## 0) Document Control

> **Parent Scope:** <scope>
> **Current Version:** X.Y
> **Session:** <real-session-id> (YYYY-MM-DD)

---

<design content>

---

> Full history: [../changelog/<name>.changelog.md](../changelog/<name>.changelog.md)
```

---

## Compliance Checklist

- [ ] File uses `*.design.md` naming and `design/` location
- [ ] Required metadata fields are complete
- [ ] Session value is real (no placeholder)
- [ ] Design file is navigator-only when paired with changelog
- [ ] Triad versions are aligned across rule/design/changelog
- [ ] Version links use canonical `#version-xy` anchors
- [ ] Update order followed `design → runtime → changelog → TODO`

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Design metadata completeness | 100% |
| Navigator compliance in paired docs | 100% |
| Triad version alignment | 100% |
| Canonical anchor compliance | 100% |
| Broken design/changelog links | 0 |

---

## Integration

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.md](document-changelog-control.md) v4.6 | Version authority and anchor policy |
| [document-consistency.md](document-consistency.md) | Cross-reference verification model |
| [project-documentation-standards.md](project-documentation-standards.md) | Project-level governance integration |

---

> **Full history:** [changelog/document-design-control.changelog.md](changelog/document-design-control.changelog.md)
