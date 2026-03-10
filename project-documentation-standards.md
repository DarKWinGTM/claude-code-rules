# Project Documentation Standards

> **Current Version:** 2.1
> **Design:** [design/project-documentation-standards.design.md](design/project-documentation-standards.design.md) v2.1
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)

---

## Rule Statement

**Core Principle: Use one deterministic documentation baseline across README, design, runtime rules, changelog, TODO, patch documents, and non-governed helper/support artifacts.**

---

## Core Requirements

### 1) Required Document Set

| Document | Required When | Purpose | Governing Rule |
|----------|---------------|---------|----------------|
| `README.md` | Always | Project overview and onboarding | Standard practice |
| `design/*.design.md` | Design/specification is required | Define target behavior/contract | `document-design-control` |
| `changelog/*.changelog.md` | Version traceability is required | Authoritative version history | `document-changelog-control` |
| `TODO.md` | Work tracking is required | Track execution state | `todo-standards` |
| `patches/*.patch.md` | Transition/migration or phased implementation work is required | Tactical transition plan and live governed execution plan | `document-patch-control` |
| `phase-implementation.md` | Phase semantics need to be standardized | First-class rule for phased planning behavior | Governed runtime rule |
| `phase-implementation-template.md` | Reusable phased authoring aid is needed at repository root | Readable root-level helper template for phased execution planning | Non-governed helper artifact |
| `support/**/*.md` or equivalent support path | Additional reference-only content is needed | Support/reference artifacts | Non-governed support layer |

### 2) UDVC-1 Integration

#### 2.1 Version Authority

- Changelog is the single version authority per governed chain
- Design/rule/patch metadata must align with authoritative changelog state
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

### 3) Role Boundary for Phase Rule, Patch Plans, and Helper Templates

- `phase-implementation.md` defines the semantic standard for phased execution planning
- Real governed phase-plan instances live in `patches/*.patch.md`
- The canonical readable helper for this repository lives at root as `phase-implementation-template.md`
- Root-level helper templates are not governed chains and do not require their own rule/design/changelog triad
- Additional support materials may still live in `support/`
- TODO tracks actionable work only; it does not become the primary place for phase definitions
- Changelog records shipped or synchronized changes only; it does not become the primary place for phase definitions
- Phase plans should explicitly show how TODO work and changelog impact relate to each phase when that coordination matters

Example boundary:
- `phase-implementation.md` is the rule/standard
- `phase-implementation-template.md` is a reusable helper
- `patches/<context>.patch.md` is the live governed plan for that project or change
- `TODO.md` tracks current execution state derived from that plan
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
Need migration, transition, or phased implementation planning?
  → YES: create patch doc(s)
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
- Patch docs remain the governed execution-plan layer when staged execution planning is needed
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
- [ ] Patch docs own live phased execution plans when phase planning is used
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
| Patch-plan role clarity | 100% |
| Root-helper placement clarity | 100% |
| TODO simplification compliance | 100% |

---

## Integration

| Rule | Relationship |
|------|-------------|
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority contract |
| [document-design-control.md](document-design-control.md) v1.8 | Design structure standards |
| [document-patch-control.md](document-patch-control.md) v1.6 | Patch structure standards and governed execution-plan role |
| [phase-implementation.md](phase-implementation.md) v1.0 | Semantic standard for phased execution planning |
| [todo-standards.md](todo-standards.md) v2.2 | TODO structure standards |

---

> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
