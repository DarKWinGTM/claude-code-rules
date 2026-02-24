# Unified Version-Control System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8 (2026-02-24)

---

## 1) Goal

Define one non-duplicated controller rule for documentation version governance across design, changelog, TODO, and patch workflows.

This controller does not introduce a second mechanism. It centralizes and enforces the existing UDVC-1 contract.

---

## 2) Scope

Applies to:

- `design/*.design.md`
- `changelog/*.changelog.md`
- `TODO.md`
- `patches/*.patch.md`
- related runtime governance rules

---

## 3) Core Governance Contract

### 3.1 Single Mechanism

- UDVC-1 is the only version-governance mechanism.
- No parallel or competing version-control model is allowed.

### 3.2 Single Authority Per Chain

- Each governed chain has one authoritative changelog.
- Runtime/design/patch documents must link to that authority with `Full history`.

### 3.3 Alignment Rules

For rule-governed chains, these values must match:

- Rule `Current Version`
- Rule `Design` reference version
- Design `Current Version`
- Changelog `Current Version`

### 3.4 Mandatory Metadata

- Rule / Design / Patch: `Current Version`, `Session`, `Full history`
- Changelog: `Parent Document`, `Current Version`, `Session`

### 3.5 Canonical Version Anchors

- Version navigation uses canonical `#version-xy` anchors only.

### 3.6 Execution Order

1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

---

## 4) Relationship With Existing Governance Rules

| Rule | Relationship |
|------|--------------|
| `document-changelog-control.md` | Core UDVC-1 authority and metadata contract |
| `document-design-control.md` | Design-structure and navigator behavior |
| `document-patch-control.md` | Patch metadata and patch-chain authority consistency |
| `todo-standards.md` | TODO execution-tracking mode and synchronization order |
| `project-documentation-standards.md` | Project-level adoption and compliance framing |

---

## 5) Rollout Plan (Design-First)

### Phase A (Completed)

- Create design + changelog chain for `unified-version-control-system`.
- Register rollout in master design/changelog.
- Add pending TODO items for runtime materialization.

### Phase B (Completed)

- Created runtime `unified-version-control-system.md`.
- Repointed related governance references to active unified-controller state in master docs.
- Re-ran consistency closure updates and completed TODO rollout task.

---

## 6) Compliance Checklist

- [ ] Single mechanism (UDVC-1) explicitly declared
- [ ] No competing governance mechanism introduced
- [ ] Single-authority-per-chain model applied
- [ ] Triad alignment enforced for rule chains
- [ ] Mandatory metadata completeness enforced
- [ ] Canonical anchor policy enforced
- [ ] Synchronization order enforced

---

## 7) Quality Metrics

| Metric | Target |
|--------|--------|
| Parallel governance mechanisms | 0 |
| Triad alignment mismatches | 0 |
| Missing mandatory metadata | 0 |
| Broken `Full history` links | 0 |
| Non-canonical version anchor usage | 0 |

---

> Full history: [../changelog/unified-version-control-system.changelog.md](../changelog/unified-version-control-system.changelog.md)
