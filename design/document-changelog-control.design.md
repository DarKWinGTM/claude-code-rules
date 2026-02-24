# Document Changelog & Versions History Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 4.6
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-23)

---

## 1) Goal

Define one deterministic documentation-version contract (UDVC-1) across rule, design, changelog, TODO, and patch layers.

---

## 2) UDVC-1 (Unified Documentation Version Contract)

### 2.1 Single Authority Per Document Chain

- Each governed document chain has one authoritative changelog file.
- The authoritative changelog controls latest version state.
- Runtime and design documents reference this authority via `Full history` links.

### 2.2 Triad Alignment (Rule Chains)

For rule-governed chains:

- `Rule Current Version`
- `Rule referenced Design version`
- `Design Current Version`
- `Changelog Current Version`

must be equal.

### 2.3 Session Integrity

- Active metadata must use a real session identifier from the active environment.
- Placeholder values are not allowed in active metadata fields.
- `LEGACY-*` markers are allowed only for historical entries where original session data is unavailable.

---

## 3) Mandatory Metadata Contract

### 3.1 Rule / Design / Patch Documents

Required header fields:

- `Current Version`
- `Session`
- `Full history` link

### 3.2 Changelog Documents

Required header fields:

- `Parent Document`
- `Current Version`
- `Session`

### 3.3 Pair Behavior

When a design/changelog pair exists:

- Design document: navigator behavior only (no local version table)
- Changelog document: detailed version sections + `Version History (Unified)` table

---

## 4) Canonical Anchor Policy

Version table links must use only:

- `#version-xy` style anchors

Do not use line-number anchors for version navigation examples.

---

## 5) Execution Order Contract

When synchronizing governed documentation, update in this fixed order:

1. design
2. runtime rule
3. changelog
4. TODO

Patch updates follow the same synchronization cycle after policy alignment.

---

## 6) Compliance Checklist

- [ ] Chain has one authoritative changelog
- [ ] Rule-chain triad versions are equal
- [ ] Required metadata headers are complete
- [ ] Active metadata has no placeholders
- [ ] Version links use canonical `#version-xy` style
- [ ] Design/changelog pair behavior is respected
- [ ] Updates followed required execution order

---

## 7) Quality Metrics

| Metric | Target |
|--------|--------|
| Triad alignment accuracy | 100% |
| Metadata completeness | 100% |
| Active placeholder session markers | 0 |
| Canonical anchor compliance | 100% |
| Cross-file synchronization drift | 0 unresolved |

---

## 8) Related Documents

| Document | Relationship |
|----------|--------------|
| [../document-changelog-control.md](../document-changelog-control.md) | Runtime implementation |
| [document-design-control.design.md](document-design-control.design.md) | Design-format contract |
| [document-patch-control.design.md](document-patch-control.design.md) | Patch metadata alignment |
| [todo-standards.design.md](todo-standards.design.md) | TODO governance format |

---

> Full history: [../changelog/document-changelog-control.changelog.md](../changelog/document-changelog-control.changelog.md)
