# Project Documentation Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.5
> **Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c (2026-03-15)

---

## 1) Goal

Provide one deterministic, low-confusion repository model across README, runtime rules, design documents, changelog files, TODO trackers, phase-planning artifacts, patch documents, and support artifacts.

This model must preserve one authority system while clearly separating:
- `phase-implementation.md` as the first-class rule for phase semantics
- `phase/SUMMARY.md` as the governed summary/index for the active phase plan
- `phase/phase-001-<phase-name>.md` and peers as the governed child phase-detail layer
- `patches/*.patch.md` as patch-governance artifacts outside the live phase workspace
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

### 3.6 Phase Summary Role

`phase/SUMMARY.md` is the governed summary/index for live phased execution planning.
It is the required top-level control surface when phased planning is used.

### 3.7 Child Phase-File Role

`phase/phase-001-<phase-name>.md` and peers are the governed child per-phase execution files.
Each child file owns the execution detail for one phase while staying subordinate to `SUMMARY.md`.

### 3.8 Patch Role

`patches/*.patch.md` is a governed patch/review artifact layer.
It is not the live phase-plan namespace.

### 3.8.1 Directory-as-namespace naming guidance

When a workspace directory already provides the stable unique context, prefer role-based filenames rather than repeating the same context in every filename.

Preferred examples in namespaced workspaces:
- `issue/276/design.md`
- `issue/276/changelog.md`
- `issue/276/patch.md`
- `issue/276/TODO.md`

Use context-bearing filenames when one or more of these are true:
- the file must remain self-identifying outside its directory context
- multiple same-role artifacts may coexist in one directory
- search, review, or portability needs materially benefit from repeating the context in the filename

Examples:
- `patches/issue-276.patch.md`
- `patches/runtime-routing-hardening.patch.md`

The goal is low-confusion naming, not mandatory generic filenames.

### 3.9 Phase Rule Role

`phase-implementation.md` is the semantic rule for phased execution planning.
It defines:
- when phased planning should and should not be used
- the required `/phase` structure
- flexible phase-order behavior
- stable child phase-file fields
- design traceability expectations
- TODO/changelog companion expectations inside the plan
- cross-phase verification, handoff, and rollback expectations

### 3.10 Root Helper Role

`phase-implementation-template.md` is a non-governed root helper.
It exists for readability, drafting, and reuse.
It may be richer than a minimal example, but it must not present itself as a governed chain.

### 3.11 Support-Artifact Role

Other reference-only artifacts should live outside ambiguous governed `.design.md` semantics unless they are intentionally normalized as governed design docs.

---

## 4) Required Document Set

| Document | Required When | Purpose | Governance Role |
|----------|---------------|---------|-----------------|
| `README.md` | Always | Overview, onboarding, repository map | Overview only |
| `design/*.design.md` | Design/specification needed | Active target-state guidance | Governed design layer |
| `changelog/*.changelog.md` | Chain history needed | Authoritative version history | Governed authority layer |
| `TODO.md` | Work tracking needed | Execution tracking | Execution layer |
| `phase/SUMMARY.md` | Phased execution planning is required | Governed summary/index for live phase planning | Governed phase summary layer |
| `phase/phase-001-<phase-name>.md` and peers | Multi-phase execution detail exists | Child per-phase execution detail | Governed phase-detail layer |
| `patches/*.patch.md` | Patch/review or transition artifact is required | Governed patch/review artifact outside the live phase workspace | Governed patch layer |
| `phase-implementation.md` | Phase semantics need to be standardized | First-class rule for phased planning behavior | Governed runtime rule |
| `phase-implementation-template.md` | Reusable phased authoring aid is needed at repository root | Readable root-level helper template | Non-governed helper artifact |
| `support/**/*.md` or equivalent support path | Reference-only content exists | Support/reference artifacts | Non-governed support layer |

---

## 5) UDVC-1 Integration

### 5.1 Single Authority Per Chain

- Changelog is the authority for each governed chain.
- Runtime, design, phase, and patch metadata align to that chain authority where applicable.
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
- `phase/SUMMARY.md` is the governed summary/index for live phased execution
- `phase/phase-001-<phase-name>.md` and peers are the governed child phase-detail files
- `patches/*.patch.md` is outside the live phase-plan namespace
- `phase-implementation-template.md` is the readable root helper for authoring
- phase may synthesize design and patch inputs as one-way source inputs into live execution planning when relevant
- design and patch artifacts are not required to point back to phase
- TODO tracks actionable execution work only
- changelog records synchronized or shipped history only
- `SUMMARY.md` should explicitly show how child phase files, TODO work, and changelog companion work relate to the active execution state

Example boundary:
- `phase-implementation.md` defines what a valid phase should contain and may synthesize relevant design/patch inputs into execution planning
- `phase-implementation-template.md` offers a readable reusable structure
- `phase/SUMMARY.md` becomes the real governed summary/index for that project
- `phase/phase-001-<name>.md` becomes the child execution detail for a specific phase
- `TODO.md` tracks active execution state derived from that structure
- `patches/*.patch.md` remains separate from the live phase workspace and does not need to point back to phase
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
Need phased implementation planning?
  → YES: create `phase/SUMMARY.md`
  ↓
Does the governed plan have multiple live phases?
  → YES: create child phase files under `phase/`
  ↓
Need patch/review artifacts separate from the live phase workspace?
  → YES: create a governed patch artifact
        - use `patches/<context>.patch.md` when filename context must travel with the file
        - use `<namespace>/patch.md` when the parent workspace already acts as the namespace
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
- [ ] Phased work uses `phase/SUMMARY.md`
- [ ] Multi-phase work uses child phase files under `phase/`
- [ ] Patch docs remain outside the live phase workspace
- [ ] Namespaced workspaces may use role-based filenames when the parent path already supplies stable context
- [ ] Redundant path + filename repetition is avoided unless it has a clear portability, coexistence, or search benefit
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
| `SUMMARY.md` role clarity | 100% |
| Child-phase-file role clarity | 100% |
| Patch-role separation clarity | 100% |
| Namespaced-workspace naming clarity | 100% |
| Root-helper boundary clarity | 100% |
| Broken cross-layer links | 0 |

---

## 10) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | Chain authority contract |
| [document-design-control.design.md](document-design-control.design.md) | Design-body and support-artifact boundary |
| [document-patch-control.design.md](document-patch-control.design.md) | Governed patch boundary outside the live phase workspace |
| [phase-implementation.design.md](phase-implementation.design.md) | First-class semantic standard for phase planning |
| [todo-standards.design.md](todo-standards.design.md) | Execution-tracker standard |
| [unified-version-control-system.design.md](unified-version-control-system.design.md) | Controller-level governance view |
| [../phase-implementation-template.md](../phase-implementation-template.md) | Non-governed root helper template |

---

> Full history: [../changelog/project-documentation-standards.changelog.md](../changelog/project-documentation-standards.changelog.md)
