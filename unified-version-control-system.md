# Unified Version-Control System

> **Current Version:** 1.3
> **Design:** [design/unified-version-control-system.design.md](design/unified-version-control-system.design.md) v1.3
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/unified-version-control-system.changelog.md](changelog/unified-version-control-system.changelog.md)

---

## Rule Statement

**Core Principle: Use one deterministic version-governance controller for governed RULES chains, and require each active runtime rule to materialize its own runtime behavior body instead of relying on design metadata or changelog claims as a substitute.**

This rule owns UDVC-1 controller-level version governance, rule-chain sufficiency, root runtime header standards, active runtime body sufficiency, and design/runtime/changelog authority separation.

---

## Core Contract

### 1) Single governance mechanism

UDVC-1 is the only version-governance mechanism for governed RULES chains.

Required guidance:
- do not introduce parallel version authorities
- keep each governed chain aligned through runtime, design, and changelog surfaces
- use changelog as version/history authority, design as active target-state authority, and root runtime rule as active behavior contract

### 2) Single authority per chain role

Each governed chain has distinct roles:

| Surface | Role |
|---|---|
| root runtime rule | active behavior contract loaded by runtime |
| `design/*.design.md` | active target-state, rationale, and design authority |
| `changelog/*.changelog.md` | current version and version history authority |
| `TODO.md` | durable execution tracking |
| `phase/` | live staged execution |
| `patch/` | before/after review artifact |

Required guidance:
- design cannot replace the runtime body for an active installed rule
- changelog claims do not prove runtime behavior exists when the root body is missing
- README install arrays define the source-owned active runtime set but do not widen scope to design/changelog/TODO/phase/patch files

### 3) Runtime header contract

Root active runtime rules use canonical metadata:

- `Current Version`
- `Design`
- `Session`
- `Full history`

`Design:` is the canonical design reference label. `Based on:` is retired in active root runtime metadata.

### 4) Active runtime body sufficiency

A README-listed active runtime rule is invalid if it is metadata-only.

Minimum body requirements:
- a substantive rule statement or equivalent behavior contract
- operational guidance that can affect runtime behavior
- relevant boundaries, triggers, anti-patterns, verification, or integration guidance
- enough body content to distinguish active runtime behavior from a design pointer

Required guidance:
- source/runtime parity must include body sufficiency, not only hash equality
- a root runtime file with only title/version/design/session metadata cannot satisfy active runtime install claims
- body sufficiency should be checked before claiming no-drift, runtime parity, release readiness, or active rule install success

### 5) Synchronization order

Default governed sync order:
1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync when affected

This order does not allow runtime body omission. If design changes a runtime rule’s active behavior, the root runtime file must materialize the behavior before the changelog claims runtime sync complete.

---

## Validation Model

For each README-listed active runtime file:

```text
Active runtime file listed
  ↓
File exists at source root?
  → NO: install set invalid
  → YES: continue
  ↓
Canonical metadata includes Current Version, Design, Session, Full history?
  → NO: metadata invalid
  → YES: continue
  ↓
Substantive runtime body exists after metadata?
  → NO: metadata-only stub; runtime install invalid
  → YES: continue
  ↓
Runtime/design/changelog versions align?
  → NO: chain sync invalid
  → YES: eligible for runtime parity/install claim
```

---

## Anti-Patterns

Avoid:
- active runtime root files that only point to design
- treating design bodies as installed runtime behavior
- changelog entries that say runtime updated while the root runtime body is empty
- parity checks that compare hashes but ignore semantic body sufficiency
- mixed `Based on` and `Design` labels in active root metadata
- README install scope drifting into design/changelog/TODO/phase/patch surfaces

Better behavior: materialize runtime behavior in the root rule, keep design as target-state authority, keep changelog as history authority, and verify both parity and body sufficiency before release claims.

---

## Verification Checklist

- [ ] UDVC-1 remains the only active version-governance mechanism.
- [ ] Root runtime metadata uses `Design`, not `Based on`.
- [ ] Active runtime metadata includes `Current Version`, `Design`, `Session`, and `Full history`.
- [ ] Every README-listed active runtime file has a substantive body.
- [ ] Design files are not used as substitutes for root runtime behavior.
- [ ] Changelog claims align with actual runtime body state.
- [ ] Source/runtime parity checks include body-sufficiency validation.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Competing governance mechanisms | 0 |
| Metadata-only active runtime files | 0 |
| Mixed active runtime header labels | 0 |
| Runtime/design/changelog version drift | 0 critical cases |
| Parity claims without body sufficiency | 0 critical cases |
| Broken authority links | 0 |

---

## Integration

Related rules:
- [project-documentation-standards.md](project-documentation-standards.md) - repository document roles and runtime install scope
- [document-design-control.md](document-design-control.md) - design active-state target truth and design/body boundary
- [document-changelog-control.md](document-changelog-control.md) - changelog version authority
- [document-consistency.md](document-consistency.md) - cross-reference, version, source/runtime, and no-drift checks
- [todo-standards.md](todo-standards.md) - durable execution tracking after governed sync
- [document-patch-control.md](document-patch-control.md) - patch review artifacts and final metadata sync

---

> **Full history:** [changelog/unified-version-control-system.changelog.md](changelog/unified-version-control-system.changelog.md)
