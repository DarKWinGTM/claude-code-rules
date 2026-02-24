# Document Design Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.7
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-23)

---

## 1) Goal

Define one consistent structure for design documents that is fully compatible with UDVC-1 governance.

---

## 2) Scope

Applies to:

- `design/*.design.md`
- design-to-changelog pair behavior
- cross-reference style used by design governance docs

---

## 3) Core Standards

### 3.1 Naming and Location

- Design documents use `<name>.design.md`
- Design documents are stored under `design/`
- Their authoritative changelog is under `changelog/<name>.changelog.md`

### 3.2 Mandatory Header Metadata

Each design document must include:

- `Parent Scope`
- `Current Version`
- `Session` (real value)

### 3.3 Navigator Rule

When a paired changelog exists, design documents must:

- include only a `Full history` link for version history navigation
- not embed local version-history tables
- not embed detailed changelog sections

### 3.4 Version Alignment Rule

For rule-governed chains, design version must align with:

- runtime rule current version
- runtime rule design reference version
- changelog current version

---

## 4) Reference and Anchor Policy

### 4.1 Canonical Version Anchors

Version-navigation examples in governance documents must use:

- `#version-xy`

Line-number anchors must not be used as the primary version-navigation standard.

### 4.2 Internal Link Requirements

- Use resolvable relative paths
- Keep design → changelog and changelog → design references consistent

---

## 5) Required Design Template

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

## 6) Quality Metrics

| Metric | Target |
|--------|--------|
| Design metadata completeness | 100% |
| Navigator compliance in paired docs | 100% |
| Triad version alignment | 100% |
| Broken design/changelog links | 0 |
| Mixed version-anchor style in governance docs | 0 |

---

## 7) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | UDVC-1 authority contract |
| [../document-design-control.md](../document-design-control.md) | Runtime implementation |
| [document-consistency.design.md](document-consistency.design.md) | Verification trigger alignment |

---

> Full history: [../changelog/document-design-control.changelog.md](../changelog/document-design-control.changelog.md)
