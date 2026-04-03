# Project Documentation Standards

> **Current Version:** 2.12
> **Design:** [design/project-documentation-standards.design.md](design/project-documentation-standards.design.md) v2.12
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)

---

## Rule Statement

**Core Principle: Use one deterministic documentation baseline across README, design, runtime rules, changelog, TODO, `/phase` planning artifacts, `/patch` artifacts, and non-governed helper/support artifacts, resolve required startup artifact posture before meaningful governed work drifts, make governed patch participation explicit in the live phase workspace when patch is in scope, and keep public onboarding/install guidance portable by default.**

---

## Core Requirements

### 1) Required Document Set

| Document | Required When | Purpose | Governing Rule |
|----------|---------------|---------|----------------|
| `README.md` | Always | Project overview and onboarding | Standard practice |
| `design/*.design.md` | Design/specification is required | Define target behavior/contract | `document-design-control` |
| `changelog/*.changelog.md` | Version traceability is required | Authoritative version history | `document-changelog-control` |
| `TODO.md` | Work tracking is required | Track execution state | `todo-standards` |
| `phase/SUMMARY.md` | Phased implementation work is required | Governed summary/index for live phase planning | `phase-implementation` |
| `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` | Multi-stage execution detail is required | Major/subphase execution detail | `phase-implementation` |
| `patch/<context>.patch.md` or root `<context>.patch.md` | Patch/review artifact is required | Governed patch/review artifact outside the live phase workspace | `document-patch-control` |
| `phase-implementation.md` | Phase semantics need to be standardized | First-class rule for phased planning behavior | Governed runtime rule |
| `phase-implementation-template.md` | Reusable phased authoring aid is needed at repository root | Readable root-level helper template for phased execution planning | Non-governed helper artifact |
| `support/**/*.md` or equivalent support path | Additional reference-only content is needed | Support/reference artifacts | Non-governed support layer |

### 2) UDVC-1 Integration

#### 2.1 Version Authority

- Changelog is the single version authority per governed chain
- Design/rule/phase/patch metadata must align with authoritative changelog state where applicable
- Root-level helper artifacts and support artifacts do not become chain authority unless intentionally normalized into a governed document chain

#### 2.2 Synchronization Order

For governance updates, apply in this order:
1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

#### 2.3 Session Integrity

- Active metadata must use real session identifiers
- Placeholder session values are not allowed in active metadata

### 3) Role Boundary for Phase Rule, `/phase`, `/patch`, and Helper Templates

- `phase-implementation.md` defines the semantic standard for phased execution planning
- `phase/SUMMARY.md` is the governed summary/index for live phased execution
- `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` are the governed per-phase execution files
- `patch/<context>.patch.md` or root `<context>.patch.md` is a governed patch/review artifact layer outside the live phase workspace
- Patch artifacts are self-identifying before/after change artifacts; they are not prose-only recaps or live phase summaries
- The canonical readable helper for this repository lives at root as `phase-implementation-template.md`
- Root-level helper templates are not governed chains and do not require their own rule/design/changelog triad
- Additional support materials may still live in `support/`
- phase may synthesize design and patch inputs as one-way source inputs into live execution planning when relevant
- design and patch artifacts are not required to point back to phase
- TODO tracks actionable work only; it does not become the primary place for phase definitions
- Changelog records shipped or synchronized changes only; it does not become the primary place for phase definitions
- Live phased execution must not be stored under patch artifacts
- `SUMMARY.md` should explicitly show how child phase files, TODO work, and changelog impact relate when that coordination matters

### 4) Startup Artifact Gate

Before meaningful governed work continues, startup artifact posture must be resolved through `artifact-initiation-control`.

That means each relevant startup artifact must be explicitly resolved as one of:
- use existing
- create now
- ask now
- not required

This startup gate happens before substantial drift.
It is separate from the later synchronization order in section 2.2.

### 5) Decision Model for Document Creation

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

### 6) Public Onboarding and Install Guidance

README and other onboarding/install docs should keep public guidance portable by default.

Required guidance:
- for cloneable or self-contained repositories, default to repo-root-relative source guidance when possible
- do not normalize workstation-specific absolute source paths or internal umbrella workspace roots as public install defaults
- distinguish source-side notation from destination/runtime notation when both appear
- use placeholders or explicit contract labels for destination/runtime paths
- exact local absolute paths may appear only when they are explicitly scoped as checked local facts, local workflow examples, or machine-scoped contracts
- if a command is intended to be run from the repo root, `./` or `<repo-root>` is preferred over one checked workstation path

### 7) Cross-Document Alignment Requirements

- Shared governed docs and templates should remain portable by default rather than embedding machine-specific environment assumptions
- Exact local values may appear only when they are explicitly being recorded as local observations or machine-scoped contracts
- Public onboarding/install docs should use portable source guidance and clearly labeled destination/runtime notation by default
- Portable-default and anti-hardcoding discipline should follow `portable-implementation-and-hardcoding-control.md`
- Source-versus-destination notation consistency should follow `document-consistency.md`
- Required document set must match project scope
- Full-history and parent-document links must resolve
- Active metadata across governed docs must not contain placeholder sessions
- `phase/SUMMARY.md` remains the governed summary/index when staged execution planning is needed
- Child phase files remain the governed execution detail layer for multi-phase work
- Patch artifacts remain outside the live phase namespace
- `phase-implementation.md` remains the semantic authority for phased execution behavior
- phased work with governed patch artifacts must show explicit patch linkage from `phase/SUMMARY.md` and relevant child phase files
- `artifact-initiation-control.md` remains the startup artifact-resolution owner
- Root-level helper artifacts and support artifacts must stay clearly outside governed authority semantics unless intentionally promoted into a governed chain

---

## Verification Checklist

- [ ] Required document set matches project scope
- [ ] Changelog exists for each governed chain
- [ ] Version references align across chain metadata
- [ ] Active session metadata has no placeholders
- [ ] Full-history links resolve
- [ ] Meaningful governed work resolves startup artifact posture before drift
- [ ] `phase-implementation.md` is used as the semantic phase rule when applicable
- [ ] Phased work uses `phase/SUMMARY.md`
- [ ] Multi-phase work uses child phase files under `phase/`
- [ ] Phased work with governed patch artifacts shows explicit patch linkage from `phase/SUMMARY.md` and relevant child phase files
- [ ] Patch artifacts use `patch/<context>.patch.md` or root `<context>.patch.md`
- [ ] Patch artifacts stay self-identifying and comparison-oriented
- [ ] Public onboarding/install guidance avoids workstation-specific absolute paths as public defaults
- [ ] Source-side guidance and destination/runtime guidance are clearly distinguished when both appear
- [ ] Exact local install examples are explicitly scoped when present
- [ ] `phase-implementation-template.md` remains a non-governed helper artifact

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Required document coverage | 100% |
| Version-reference correctness | 100% |
| Active metadata session integrity | 100% |
| Cross-link validity | 100% |
| Phase-rule role clarity | 100% |
| `SUMMARY.md` role clarity | 100% |
| Child-phase-file role clarity | 100% |
| Patch-role separation clarity | 100% |
| Patch placement clarity | 100% |
| Explicit phase-to-patch linkage coverage when patch is in scope | 100% |
| Startup artifact posture resolved before drift | 100% |
| Public onboarding/install portability | High |
| Workstation-specific absolute paths as public defaults | 0 critical cases |
| Source-vs-destination notation clarity | High |
| Root-helper placement clarity | 100% |
| TODO simplification compliance | 100% |

---

## Integration

| Rule | Relationship |
|------|-------------|
| [artifact-initiation-control.md](artifact-initiation-control.md) v1.0 | Startup artifact-resolution owner |
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority contract |
| [document-design-control.md](document-design-control.md) v1.8 | Design structure standards |
| [document-patch-control.md](document-patch-control.md) v2.4 | Patch-governance boundary and explicit before/after patch contract outside live phase planning |
| [phase-implementation.md](phase-implementation.md) v2.7 | Semantic standard for phased execution planning and one-way design/patch source synthesis |
| [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) v1.1 | Portable shared-artifact defaults and anti-hardcoding discipline |
| [document-consistency.md](document-consistency.md) v1.5 | Source-side and destination/runtime reference consistency |
| [todo-standards.md](todo-standards.md) v2.3 | TODO structure standards plus startup-establishment bridge |

---

> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
