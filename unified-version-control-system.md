# Unified Version-Control System

> **Current Version:** 1.1
> **Based on:** [unified-version-control-system.design.md](design/unified-version-control-system.design.md) v1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8
>
> **Full history:** [changelog/unified-version-control-system.changelog.md](changelog/unified-version-control-system.changelog.md)

---

## Rule Statement

**Core Principle: One deterministic governance mechanism (UDVC-1) controls documentation versioning across design, runtime rules, changelog, TODO, and patch workflows.**

---

## Scope

Applies to:

- `design/*.design.md`
- `changelog/*.changelog.md`
- root runtime governance rules (`*.md`)
- `TODO.md`
- `patches/*.patch.md`

---

## Core Requirements

### 1) Single Mechanism

- UDVC-1 is the only version-governance mechanism.
- Do not introduce parallel governance systems.

### 2) Single Authority Per Chain

- Each governed chain has one authoritative changelog.
- Runtime/design/patch documents must link to that authority using `Full history`.

### 3) Rule-Chain Triad Alignment (Mandatory)

For rule-governed chains, these values must match:

- Rule `Current Version`
- Rule `Based on` design version
- Design `Current Version`
- Changelog `Current Version`

### 4) Mandatory Metadata

#### Rule / Design / Patch docs
- `Current Version`
- `Session`
- `Full history`

#### Changelog docs
- `Parent Document`
- `Current Version`
- `Session`

### 5) Canonical Anchor Policy

- Version navigation must use canonical `#version-xy` anchors.

### 6) Synchronization Order (Non-Negotiable)

1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

---

## Integration

- [document-changelog-control.md](document-changelog-control.md) v4.6
- [document-design-control.md](document-design-control.md) v1.7
- [document-patch-control.md](document-patch-control.md) v1.2
- [todo-standards.md](todo-standards.md) v2.1
- [project-documentation-standards.md](project-documentation-standards.md) v1.7

---

## Compliance Checklist

- [ ] Single mechanism enforced (UDVC-1 only)
- [ ] Single changelog authority per chain enforced
- [ ] Rule-chain triad alignment enforced
- [ ] Mandatory metadata complete across governed artifacts
- [ ] Canonical anchor policy enforced
- [ ] Synchronization order enforced

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Parallel governance mechanisms | 0 |
| Rule-chain triad mismatches | 0 |
| Missing mandatory metadata | 0 |
| Broken authority links | 0 |
| Non-canonical version anchors | 0 |

---

> **Full history:** [changelog/unified-version-control-system.changelog.md](changelog/unified-version-control-system.changelog.md)
