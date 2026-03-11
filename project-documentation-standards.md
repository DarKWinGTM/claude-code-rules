# Project Documentation Standards

> **Current Version:** 2.3
> **Design:** [design/project-documentation-standards.design.md](design/project-documentation-standards.design.md) v2.3
> **Session:** 92fed037-8ba9-48a6-95c4-e1085f28bb32
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)

---

## Rule Statement

**Core Principle: Use one deterministic documentation baseline across README, design, runtime rules, changelog, TODO, `/phase` planning artifacts, `/patches` artifacts, and non-governed helper/support artifacts.**

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
| `phase/phase-010-<phase-name>.md` and peers | Multi-phase execution detail is required | Child per-phase execution detail | `phase-implementation` |
| `patches/*.patch.md` | Patch/review or transition artifact is required | Governed patch/review artifact outside the live phase workspace | `document-patch-control` |
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

### 3) Role Boundary for Phase Rule, `/phase`, `/patches`, and Helper Templates

- `phase-implementation.md` defines the semantic standard for phased execution planning
- `phase/SUMMARY.md` is the governed summary/index for live phased execution
- `phase/phase-010-<phase-name>.md` and peers are the governed per-phase execution files
- `patches/*.patch.md` is a governed patch/review artifact layer outside the live phase workspace
- The canonical readable helper for this repository lives at root as `phase-implementation-template.md`
- Root-level helper templates are not governed chains and do not require their own rule/design/changelog triad
- Additional support materials may still live in `support/`
- TODO tracks actionable work only; it does not become the primary place for phase definitions
- Changelog records shipped or synchronized changes only; it does not become the primary place for phase definitions
- Live phased execution must not be stored under `/patches`
- `SUMMARY.md` should explicitly show how child phase files, TODO work, and changelog impact relate when that coordination matters

Example boundary:
- `phase-implementation.md` is the rule/standard
- `phase-implementation-template.md` is a reusable helper
- `phase/SUMMARY.md` is the live governed summary/index for that project or change
- `phase/phase-010-<name>.md` is the live governed child phase detail
- `TODO.md` tracks current execution state derived from that structure
- `patches/*.patch.md` stays separate from the live phase workspace
- changelog records the synchronized or released result

### 4) Decision Model for Document Creation

```text
Project start
  ↓
Create README
  ↓
Need design specification?
  → YES: create design doc(s)
  ↓
Need version traceability?
  → YES: create changelog doc(s)
  ↓
Need tracked execution items?
  → YES: create TODO.md
  ↓
Need phased implementation planning?
  → YES: create `phase/SUMMARY.md`
  ↓
Does the governed plan have multiple live phases?
  → YES: create child phase files under `phase/`
  ↓
Need patch/review artifacts separate from the live phase workspace?
  → YES: create `patches/*.patch.md`
  ↓
Need standardized phase semantics?
  → YES: use `phase-implementation.md`
  ↓
Need the reusable root-level phase helper?
  → YES: use `phase-implementation-template.md`
  ↓
Need additional support/reference-only material?
  → YES: create support artifact outside governed design semantics
```

### 5) Cross-Document Alignment Requirements

- Required document set must match project scope
- Full-history and parent-document links must resolve
- Active metadata across governed docs must not contain placeholder sessions
- `phase/SUMMARY.md` remains the governed summary/index when staged execution planning is needed
- Child phase files remain the governed execution detail layer for multi-phase work
- `patches/*.patch.md` remains outside the live phase namespace
- `phase-implementation.md` remains the semantic authority for phased execution behavior
- Root-level helper artifacts and support artifacts must stay clearly outside governed authority semantics unless intentionally promoted into a governed chain

---

## Verification Checklist

- [ ] Required document set matches project scope
- [ ] Changelog exists for each governed chain
- [ ] Version references align across chain metadata
- [ ] Active session metadata has no placeholders
- [ ] Full-history links resolve
- [ ] TODO follows simplified standard mode
- [ ] `phase-implementation.md` is used as the semantic phase rule when applicable
- [ ] Phased work uses `phase/SUMMARY.md`
- [ ] Multi-phase work uses child phase files under `phase/`
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
| Root-helper placement clarity | 100% |
| TODO simplification compliance | 100% |

---

## Integration

| Rule | Relationship |
|------|-------------|
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority contract |
| [document-design-control.md](document-design-control.md) v1.8 | Design structure standards |
| [document-patch-control.md](document-patch-control.md) v1.9 | Patch-governance boundary outside live phase planning |
| [phase-implementation.md](phase-implementation.md) v1.3 | Semantic standard for phased execution planning |
| [todo-standards.md](todo-standards.md) v2.2 | TODO structure standards |

---

> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
