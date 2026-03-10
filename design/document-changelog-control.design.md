# Document Changelog & Versions History Control

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 4.7
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2 (2026-03-08)

---

## 1) Goal

Define one deterministic documentation-version contract (UDVC-1) across runtime rules, design documents, changelog files, TODO trackers, and patch artifacts.

---

## 2) Scope

Applies to governed documentation artifacts in this repository:

- root runtime rules (`*.md`, excluding overview-only/support documents)
- `design/*.design.md`
- `changelog/*.changelog.md`
- `TODO.md`
- `patches/*.patch.md`

---

## 3) UDVC-1 Core Contract

### 3.1 Single Authority Per Chain

- Each governed chain has one authoritative changelog.
- The authoritative changelog controls latest version state for that chain.
- Runtime, design, and patch artifacts reference that authority through `Full history` links.

### 3.2 Rule-Chain Alignment

For rule-governed chains, these values must match:

- runtime rule `Current Version`
- runtime rule `Design` reference version
- design `Current Version`
- changelog `Current Version`

### 3.3 Session Integrity

- Active metadata uses real session identifiers from the active environment.
- Placeholder values are not allowed in active metadata.
- `LEGACY-*` markers are allowed only for preserved historical records where the original active session is unavailable.

---

## 4) Mandatory Metadata Contract

### 4.1 Runtime Rule Header Contract

Root runtime rules use this canonical header contract:

- `Current Version`
- `Design`
- `Session`
- `Full history`

`Design:` is the only allowed label for root runtime design references.
`Based on:` is retired for root runtime rule metadata.

### 4.2 Design / Patch Metadata

Required active metadata:

- `Current Version`
- `Session`
- `Full history`

### 4.3 Changelog Metadata

Required active metadata:

- `Parent Document`
- `Current Version`
- `Session`

---

## 5) Pair Behavior

When a design/changelog pair exists for one governed chain:

| File | MUST use | MUST NOT use |
|------|----------|--------------|
| `*.design.md` | Active-state design body + `Full history` navigation | Embedded version tables, detailed changelog sections, historical rollout logs |
| `*.changelog.md` | Detailed version sections + `Version History (Unified)` | Table-only history or design-state guidance |

Historical detail belongs in changelog files, not in the active design body.

---

## 6) Canonical Anchor Policy

- Version-table links use canonical `#version-xy` anchors.
- Line-number anchors are not the version-navigation standard.

---

## 7) Execution Order Contract

When synchronizing governed documentation:

1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

---

## 8) Required Patterns

### 8.1 Runtime Rule Header

```markdown
# <Rule Name>

> **Current Version:** X.Y
> **Design:** [design/<rule>.design.md](design/<rule>.design.md) vX.Y
> **Session:** <real-session-id>
> **Full history:** [changelog/<rule>.changelog.md](changelog/<rule>.changelog.md)
```

### 8.2 Changelog Header

```markdown
# Changelog - <Document>

> **Parent Document:** [../<doc>.md](../<doc>.md)
> **Current Version:** X.Y
> **Session:** <real-session-id>
```

### 8.3 Design Footer

```markdown
> Full history: [../changelog/<doc>.changelog.md](../changelog/<doc>.changelog.md)
```

---

## 9) Verification Checklist

- [ ] Each governed chain has one authoritative changelog
- [ ] Runtime-rule header uses `Design`, not `Based on`
- [ ] Active runtime headers include `Session`
- [ ] Rule/design/changelog versions are aligned for governed rule chains
- [ ] Design files keep active guidance only
- [ ] Changelog files hold historical detail
- [ ] Version links use canonical `#version-xy` anchors
- [ ] Synchronization order was followed

---

## 10) Quality Metrics

| Metric | Target |
|--------|--------|
| Rule-chain alignment accuracy | 100% |
| Runtime header contract consistency | 100% |
| Active placeholder session markers | 0 |
| Historical detail left in active design bodies | 0 critical cases |
| Broken `Full history` links | 0 |

---

## 11) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-design-control.design.md](document-design-control.design.md) | Active-state design-body contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository-wide document-role boundary model |
| [todo-standards.design.md](todo-standards.design.md) | Execution-tracker boundary |
| [unified-version-control-system.design.md](unified-version-control-system.design.md) | UDVC-1 controller view |

---

> Full history: [../changelog/document-changelog-control.changelog.md](../changelog/document-changelog-control.changelog.md)
