# Unified Version-Control System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.2
> **Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2 (2026-03-08)

---

## 1) Goal

Define one controller-level governance view for UDVC-1 so the repository teaches a single deterministic model across runtime rules, design docs, changelogs, TODO, patches, and support artifacts.

---

## 2) Scope

Applies to:

- runtime governance rules
- `design/*.design.md`
- `changelog/*.changelog.md`
- `TODO.md`
- `patch/<context>.patch.md` or root `<context>.patch.md`
- repository-level role boundaries that prevent governed/support-layer confusion

---

## 3) Controller Contract

### 3.1 Single Mechanism

- UDVC-1 is the only version-governance mechanism.
- No parallel or competing governance model is allowed.

### 3.2 Single Authority Per Chain

- Each governed chain has one authoritative changelog.
- Runtime, design, and patch artifacts link to that authority through `Full history`.

### 3.3 Runtime Header Contract

Root runtime rules use this canonical metadata contract:

- `Current Version`
- `Design`
- `Session`
- `Full history`

`Design:` is the canonical label.
`Based on:` is retired in root runtime rule metadata.

### 3.4 Active-State Design Contract

- Design documents hold current active target-state guidance.
- Historical audit, rollout, and remediation detail lives in changelog files.

### 3.5 Layer Boundary Contract

- README is overview-only.
- TODO is execution-only.
- Support artifacts must not remain in ambiguous governed `.design.md` form unless intentionally normalized into a governed chain.

### 3.6 Synchronization Order

1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

---

## 4) Verification Checklist

- [ ] UDVC-1 is the only active governance mechanism
- [ ] Runtime rules use the canonical `Design` header label
- [ ] Active runtime headers include `Session`
- [ ] Design docs keep active guidance only
- [ ] README/TODO/support artifacts stay inside their proper role boundaries
- [ ] Synchronization order is enforced

---

## 5) Quality Metrics

| Metric | Target |
|--------|--------|
| Competing governance mechanisms | 0 |
| Mixed runtime header labels | 0 |
| Historical detail embedded in active design bodies | 0 critical cases |
| Ambiguous governed-looking support artifacts | 0 |
| Broken authority links | 0 |

---

## 6) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Chain authority and metadata contract |
| [document-design-control.design.md](document-design-control.design.md) | Active-state design-body contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role model |
| [todo-standards.design.md](todo-standards.design.md) | Execution-tracker boundary |

---

> Full history: [../changelog/unified-version-control-system.changelog.md](../changelog/unified-version-control-system.changelog.md)
