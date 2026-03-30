# Project Documentation Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.9
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-03-28)

---

## 1) Goal

Provide one deterministic, low-confusion repository model across README, runtime rules, design documents, changelog files, TODO trackers, phase-planning artifacts, patch documents, and support artifacts.

This model must preserve one authority system while clearly separating:
- `phase-implementation.md` as the first-class rule for phase semantics
- `phase/SUMMARY.md` as the governed summary/index for the active phase plan
- `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` as governed execution files
- `patch/<context>.patch.md` or root `<context>.patch.md` as patch-governance artifacts outside the live phase workspace
- `phase-implementation-template.md` as the readable root-level helper
- `TODO.md` and changelog as required companions, but not as replacements for the phase plan itself
- `artifact-initiation-control.md` as the startup-governance owner that resolves artifact posture before meaningful work drifts

---

## 2) Scope

Applies to projects that keep governed documentation artifacts and support/reference materials in the same repository.

---

## 3) Repository Role Model

### 3.1 README Role
`README.md` is an overview/reference document.
It is not version authority for governed chains.

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

### 3.7 Phase Execution-File Role
The active phase identity model uses:
- major phase files: `phase/phase-NNN-<phase-name>.md`
- subphase files: `phase/phase-NNN-NN-<subphase-name>.md`

### 3.8 Patch Role
`patch/<context>.patch.md` or root `<context>.patch.md` is a governed patch/review artifact layer.
It is not the live phase-plan namespace.
A patch is a self-identifying before/after artifact whose job is to show what will change.

### 3.9 Startup Artifact-Initiation Role
`artifact-initiation-control.md` is the semantic owner of startup artifact posture.
It decides whether design, changelog, TODO, phase, and patch should be reused, created now, asked about now, or marked not required before meaningful work drifts.

### 3.10 Phase Rule Role
`phase-implementation.md` is the semantic rule for phased execution planning.
It owns phase semantics after `/phase` is required.

### 3.11 Root Helper Role
`phase-implementation-template.md` is a non-governed root helper.
It exists for readability, drafting, and reuse.

---

## 4) Required Document Set

| Document | Required When | Purpose | Governance Role |
|----------|---------------|---------|-----------------|
| `README.md` | Always | Overview, onboarding, repository map | Overview only |
| `design/*.design.md` | Design/specification needed | Active target-state guidance | Governed design layer |
| `changelog/*.changelog.md` | Chain history needed | Authoritative version history | Governed authority layer |
| `TODO.md` | Work tracking needed | Execution tracking | Execution layer |
| `phase/SUMMARY.md` | Phased execution planning is required | Governed summary/index for live phase planning | Governed phase summary layer |
| `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` | Multi-stage execution detail exists | Major/subphase execution detail | Governed phase-detail layer |
| `patch/<context>.patch.md` or root `<context>.patch.md` | Patch/review artifact is required | Governed patch/review artifact outside the live phase workspace | Governed patch layer |
| `artifact-initiation-control.md` | Startup artifact posture must be standardized | First-class startup-governance behavior | Governed runtime rule |
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

## 6) Startup Artifact Gate

Before meaningful governed work continues, startup artifact posture must be resolved through `artifact-initiation-control`.

Required startup artifact states:
- use existing
- create now
- ask now
- not required

This startup gate happens before substantial drift.
It is distinct from the later synchronization order under UDVC-1.

---

## 7) Decision Model for Document Creation

```text
Meaningful governed work begins
  ↓
Resolve startup artifact posture through artifact-initiation-control
  ↓
Need design specification?
  → YES: use existing / create now / ask now
  ↓
Need version traceability?
  → YES: use existing / create now / ask now
  ↓
Need tracked execution items?
  → YES: use existing / create now / ask now
  ↓
Need phased implementation planning?
  → YES: establish `phase/SUMMARY.md` and child phase files now or ask now
  ↓
Need patch/review artifacts separate from the live phase workspace?
  → YES: use existing / create now / ask now
        - use `patch/<context>.patch.md` as the default shared patch path
        - use root `<context>.patch.md` when direct top-level placement is clearer
  ↓
After startup posture is resolved
  → continue with substantive planning / implementation
```

When phased work also uses governed patch artifacts, the phase workspace should declare that linkage explicitly in `phase/SUMMARY.md` and the relevant child phase files instead of leaving patch participation implicit.


---

## 8) Verification Checklist

- [ ] Required document set matches project scope
- [ ] Changelog exists for each governed chain
- [ ] Version references align across chain metadata
- [ ] Active session metadata has no placeholders
- [ ] Full-history links resolve
- [ ] Meaningful governed work resolves startup artifact posture before drift
- [ ] `phase-implementation.md` is treated as the semantic phase-planning rule
- [ ] Phased work uses `phase/SUMMARY.md`
- [ ] Multi-stage execution uses canonical `NNN` / `NNN-NN` phase files under `phase/`
- [ ] Phased work with governed patch artifacts shows explicit patch linkage from `phase/SUMMARY.md` and relevant child phase files
- [ ] Patch artifacts use `patch/<context>.patch.md` or root `<context>.patch.md`
- [ ] Patch artifacts stay self-identifying and comparison-oriented
- [ ] Root-level helper artifacts do not masquerade as governed docs

---

## 9) Quality Metrics

| Metric | Target |
|--------|--------|
| Required document coverage | 100% |
| Version-reference correctness | 100% |
| Active metadata session integrity | 100% |
| Cross-link validity | 100% |
| Phase-rule role clarity | 100% |
| `SUMMARY.md` role clarity | 100% |
| Phase-file role clarity | 100% |
| Patch-role separation clarity | 100% |
| Patch placement clarity | 100% |
| Explicit phase-to-patch linkage coverage when patch is in scope | 100% |
| Startup artifact posture resolved before drift | 100% |
| Root-helper placement clarity | 100% |
| TODO simplification compliance | 100% |

---

## 10) Integration

| Rule | Relationship |
|------|-------------|
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup artifact-resolution owner |
| [document-changelog-control.md](../document-changelog-control.md) | Version authority contract |
| [document-design-control.md](../document-design-control.md) | Design structure standards |
| [document-patch-control.md](../document-patch-control.md) | Patch-governance boundary and explicit before/after patch contract outside live phase planning |
| [phase-implementation.md](../phase-implementation.md) | Semantic standard for phased execution planning and one-way design/patch source synthesis |
| [todo-standards.md](../todo-standards.md) | TODO structure standards plus startup-establishment bridge |

---

> Full history: [../changelog/project-documentation-standards.changelog.md](../changelog/project-documentation-standards.changelog.md)
