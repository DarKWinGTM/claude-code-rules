# Document Changelog & Versions History Control

> **Current Version:** 4.6
> **Based on:** document-changelog-control.design.md v4.6
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

> **Full history:** [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)

---

## Rule Statement

**Core Principle: Govern documentation versions through one deterministic contract (UDVC-1).**

Normalize all governed documents to one consistent authority and synchronization model.

---

## UDVC-1 Core Requirements

### 1) Single Authority Per Document Chain

- Each governed chain (`rule/design/changelog`, and applicable patch chain) has one authoritative changelog.
- The authoritative changelog controls latest version state.
- Rule, design, and patch files reference this authority with `Full history` links.

### 2) Rule-Chain Triad Alignment (Mandatory)

For rule-governed chains, all values must match:

- Rule `Current Version`
- Rule `Design` reference version
- Design `Current Version`
- Changelog `Current Version`

### 3) Mandatory Metadata

#### Rule / Design / Patch docs
- `Current Version`
- `Session`
- `Full history` link

#### Changelog docs
- `Parent Document`
- `Current Version`
- `Session`

### 4) Session Integrity

- Active metadata uses real session IDs from current environment.
- Placeholder values are prohibited in active metadata (`<Session ID>`, `TBD`, `pending`, mock labels).
- `LEGACY-*` is allowed only for historical records where original session data is unavailable.

### 5) Pair Behavior (Design + Changelog)

When both files exist in one chain:

| File | MUST use | MUST NOT use |
|------|----------|--------------|
| `*.design.md` | Navigator link-only (`Full history`) | Embedded version table or detailed changelog sections |
| `*.changelog.md` | Detailed version sections + `Version History (Unified)` | Detailed-only or table-only format |

### 6) Canonical Anchor Policy

- Version-table links must use canonical `#version-xy` anchors.
- Do not use line-number anchors as version-navigation standard.

### 7) Execution Order (Non-Negotiable)

For synchronized governance updates:

1. design
2. runtime rule
3. changelog
4. TODO

Patch metadata synchronization follows the same cycle when affected.

---

## Format Standards

### A) Changelog Header (Authoritative)

```markdown
# Changelog - <Document>

> **Parent Document:** [../<doc>.md](../<doc>.md)
> **Current Version:** X.Y
> **Session:** <Real Session ID>
```

### B) Version Section + Unified Table

```markdown
## Version X.Y: <Headline>

**Date:** YYYY-MM-DD
**Session:** <Real Session ID>

### Changes
- ...

### Summary
...

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| X.Y | YYYY-MM-DD | **[<Headline>](#version-xy)** | <Real Session ID> |
| | | Summary: ... | |
```

### C) Design Navigator Footer

```markdown
> Full history: [../changelog/<doc>.changelog.md](../changelog/<doc>.changelog.md)
```

---

## Compliance Checklist

- [ ] Chain has one authoritative changelog
- [ ] Rule-chain triad versions are aligned
- [ ] Mandatory metadata fields are complete
- [ ] No placeholder sessions in active metadata
- [ ] Canonical `#version-xy` anchors are used for version links
- [ ] Pair behavior is respected
- [ ] Execution order was followed

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Triad alignment accuracy | 100% |
| Mandatory metadata completeness | 100% |
| Active placeholder session markers | 0 |
| Canonical anchor compliance | 100% |
| Broken full-history links | 0 |

---

## Enforcement Notes

- Changelog is the single version authority.
- Do not silently rewrite historical intent; add corrective entries when needed.
- Keep governance simple and deterministic; avoid mixed standards.

---

> **Full history:** [changelog/document-changelog-control.changelog.md](changelog/document-changelog-control.changelog.md)
