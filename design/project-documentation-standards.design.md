# Project Documentation Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.1
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402 (2026-03-10)

---

## 1) Goal

Provide one deterministic, low-confusion repository model across README, runtime rules, design documents, changelog files, TODO trackers, patch documents, and support artifacts.

This model must preserve one authority system while clearly separating:
- `phase-implementation.md` as the first-class rule for phase semantics
- `patches/*.patch.md` as the live governed plan instances
- `phase-implementation-template.md` as the readable root-level helper
- `TODO.md` and changelog as required companions, but not as replacements for the phase plan itself

---

## 2) Scope

Applies to projects that keep governed documentation artifacts and support/reference materials in the same repository.

---

## 3) Repository Role Model

### 3.1 README Role

`README.md` is an overview/reference document.
It is not version authority for governed chains.
It should describe repository layout, usage, and workflow boundaries without overstating authority.

### 3.2 Runtime Rule Role

Root runtime rules are the active rule layer.
They use the canonical runtime header contract:
- `Current Version`
- `Design`
- `Session`
- `Full history`

### 3.3 Design Role

`design/*.design.md` documents hold active target-state guidance.
Historical detail lives in changelog files, not in active design bodies.

### 3.4 Changelog Role

Each governed chain uses one authoritative changelog.
Changelog files hold detailed history and latest chain version state.

### 3.5 TODO Role

`TODO.md` tracks execution state only.
It is not a version-authority document.

### 3.6 Patch Role

`patches/*.patch.md` is the governed execution-plan layer.
When phased execution planning is needed, the live project-specific plan belongs in the patch document.

### 3.7 Phase Rule Role

`phase-implementation.md` is the semantic rule for phased execution planning.
It defines:
- when phased planning should and should not be used
- flexible phase-order behavior
- stable per-phase fields
- design traceability expectations
- TODO/changelog companion expectations inside the phase plan
- cross-phase verification, handoff, and rollback expectations

### 3.8 Root Helper Role

`phase-implementation-template.md` is a non-governed root helper.
It exists for readability, drafting, and reuse.
It may be richer than a minimal example, but it must not present itself as a governed chain.

### 3.9 Support-Artifact Role

Other reference-only artifacts should live outside ambiguous governed `.design.md` semantics unless they are intentionally normalized as governed design docs.

---

## 4) Required Document Set

| Document | Required When | Purpose | Governance Role |
|----------|---------------|---------|-----------------|
| `README.md` | Always | Overview, onboarding, repository map | Overview only |
| `design/*.design.md` | Design/specification needed | Active target-state guidance | Governed design layer |
| `changelog/*.changelog.md` | Chain history needed | Authoritative version history | Governed authority layer |
| `TODO.md` | Work tracking needed | Execution tracking | Execution layer |
| `patches/*.patch.md` | Transition plan or phased execution plan needed | Tactical migration/transition plan and live governed execution plan | Governed patch layer |
| `phase-implementation.md` | Phase semantics need to be standardized | First-class rule for phased planning behavior | Governed runtime rule |
| `phase-implementation-template.md` | Reusable phased authoring aid needed at repository root | Readable root-level helper template | Non-governed helper artifact |
| `support/**/*.md` or equivalent support path | Reference-only content exists | Support/reference artifacts | Non-governed support layer |

---

## 5) UDVC-1 Integration

### 5.1 Single Authority Per Chain

- Changelog is the authority for each governed chain.
- Runtime, design, and patch metadata align to that chain authority.
- Root-level helper artifacts and support artifacts do not create parallel version authority.

### 5.2 Synchronization Order

1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

### 5.3 Session Integrity

- Active metadata uses real session identifiers.
- Placeholder session values are not allowed in active metadata.

---

## 6) Phase Planning Boundary

Required boundary rules:
- `phase-implementation.md` is the rule/standard for phase semantics
- `patches/*.patch.md` is the live governed phase-plan instance
- `phase-implementation-template.md` is the readable root helper for authoring
- TODO tracks actionable execution work only
- changelog records synchronized or shipped history only
- the patch should explicitly show how TODO and changelog companion work relates to the active phases

Example boundary:
- `phase-implementation.md` defines what a valid phase should contain
- `phase-implementation-template.md` offers a readable reusable structure
- `patches/<context>.patch.md` becomes the real governed plan for that project
- `TODO.md` tracks active execution slices derived from that plan
- `changelog/*.changelog.md` records the resulting synchronized or released changes

---

## 7) Decision Model for Document Creation

```text
Project start
  ↓
Create README overview
  ↓
Need governed target-state guidance?
  → YES: create design doc(s)
  ↓
Need authoritative chain history?
  → YES: create changelog doc(s)
  ↓
Need execution tracking?
  → YES: create TODO.md
  ↓
Need migration, transition, or phased implementation planning?
  → YES: create patch doc(s)
  ↓
Need standardized phase semantics?
  → YES: use `phase-implementation.md`
  ↓
Need a readable reusable root helper for authoring?
  → YES: use `phase-implementation-template.md`
  ↓
Need additional support/reference-only material?
  → YES: create support artifact outside governed design semantics
```

---

## 8) Verification Checklist

- [ ] README stays overview-only and does not overstate authority
- [ ] Runtime rules use the canonical `Design` header label
- [ ] Design docs contain active guidance only
- [ ] Changelog files remain chain authorities
- [ ] TODO remains execution-only
- [ ] `phase-implementation.md` is treated as the semantic phase-planning rule
- [ ] Patch docs remain the governed execution-plan layer
- [ ] Root-level helper artifacts do not masquerade as governed docs
- [ ] Support artifacts do not masquerade as governed design docs
- [ ] Active metadata uses real session IDs

---

## 9) Quality Metrics

| Metric | Target |
|--------|--------|
| README authority-boundary accuracy | 100% |
| Runtime header contract consistency | 100% |
| Active design-body cleanliness | 100% |
| Phase-rule role clarity | 100% |
| Patch-role clarity | 100% |
| Root-helper boundary clarity | 100% |
| Broken cross-layer links | 0 |

---

## 10) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Chain authority contract |
| [document-design-control.design.md](document-design-control.design.md) | Design-body and support-artifact boundary |
| [document-patch-control.design.md](document-patch-control.design.md) | Governed patch planning and metadata contract |
| [phase-implementation.design.md](phase-implementation.design.md) | First-class semantic standard for phase planning |
| [todo-standards.design.md](todo-standards.design.md) | Execution-tracker standard |
| [unified-version-control-system.design.md](unified-version-control-system.design.md) | Controller-level governance view |
| [../phase-implementation-template.md](../phase-implementation-template.md) | Non-governed root helper template |

---

> Full history: [../changelog/project-documentation-standards.changelog.md](../changelog/project-documentation-standards.changelog.md)
