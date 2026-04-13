# Project Documentation Standards

> **Current Version:** 2.23
> **Design:** [design/project-documentation-standards.design.md](design/project-documentation-standards.design.md) v2.23
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)

---

## Rule Statement

**Core Principle: Use one deterministic documentation baseline across README, design, runtime rules, changelog, TODO, `/phase` planning artifacts, `/patch` artifacts, and non-governed helper/support or extension-package artifacts, resolve required startup artifact posture before meaningful governed work drifts, make governed patch participation explicit in the live phase workspace when patch is in scope, and keep public onboarding/install guidance portable by default.**

---

## Core Requirements

### 1) Required Document Set

| Document | Required When | Purpose | Governing Rule |
|----------|---------------|---------|----------------|
| `README.md` | Always | Project overview and onboarding | Standard practice |
| `design/*.design.md` | Design/specification is required | Define target behavior/contract | `document-design-control` |
| `changelog/*.changelog.md` | Version traceability is required | Authoritative version history | `document-changelog-control` |
| `TODO.md` | Work tracking is required | Durable repository/project execution tracking | `todo-standards` |
| `phase/SUMMARY.md` | Phased implementation work is required | Governed summary/index for live phase planning | `phase-implementation` |
| `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` | Multi-stage execution detail is required | Major/subphase execution detail | `phase-implementation` |
| `patch/<context>.patch.md` or root `<context>.patch.md` | Patch/review artifact is required | Governed patch/review artifact outside the live phase workspace | `document-patch-control` |
| `phase-implementation.md` | Phase semantics need to be standardized | First-class rule for phased planning behavior | Governed runtime rule |
| `phase-implementation-template.md` | Reusable phased authoring aid is needed at repository root | Readable root-level helper template for phased execution planning | Non-governed helper artifact |
| `support/**/*.md`, `plugin/**`, or equivalent support/extension path | Additional reference-only content or optional extension-package content is needed | Support/reference or extension-package artifacts | Non-governed support / extension layer |

### 2) UDVC-1 Integration

#### 2.1 Version Authority

- Changelog is the single version authority per governed chain
- Design/rule/phase/patch metadata must align with authoritative changelog state where applicable
- Root-level helper artifacts, support artifacts, and optional extension-package artifacts do not become chain authority unless intentionally normalized into a governed document chain

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
- Additional support materials or optional extension packages may still live in `support/` or `plugin/`
- package-local plugin assets may use a package scaffold such as `README.md`, `.claude-plugin/`, `hooks/`, `scripts/`, optional `skills/`, and optional `agents/`
- those package-local assets remain implementation/support surfaces, not root governance authority
- when package-local skills, agents, scripts, or docs are intended to remain reusable source artifacts, they should stay portable by default rather than embedding workstation-specific absolute paths as if those were shared contracts
- design and patch artifacts are not required to point back to phase
- Claude Code's built-in task list is the live in-session execution surface for active non-trivial work
- `TODO.md` remains the durable repository/project execution-tracking document; it does not become the primary place for phase definitions and does not replace live task-list visibility during active work
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
Need live execution visibility for non-trivial active work?
  → YES: initialize the built-in task list early
  ↓
Need phased implementation planning?
  → YES: establish `phase/SUMMARY.md` and child phase files now or ask now
  ↓
Need patch/review artifacts separate from the live phase workspace?
  → YES: only when a real existing governed surface needs separate before/after review packaging, or the user explicitly requests patch packaging
        - use existing / create now / ask now
        - use `patch/<context>.patch.md` as the default shared patch path
        - use root `<context>.patch.md` when direct top-level placement is clearer
  → For greenfield startup / baseline formation by itself: default to `patch: not required`
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
- Package-local support/extension source artifacts such as `plugin/**`, optional `skills/`, optional `agents/`, and reusable support scripts should also remain portable by default when they are acting as maintained source artifacts rather than ephemeral local test output
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
- built-in task-list usage remains a live execution surface rather than becoming a governed repository document type
- within the same active objective, the live task-list surface should normally be reused and extended rather than replaced, while durable history still belongs in TODO/phase/changelog surfaces
- design, phase, TODO, task-list, and checked implementation state may all act as execution-discovery surfaces once work is already in execution mode
- execution-continuity and goal-review owners may shape how active work keeps moving and how the full objective set stays visible, while tasks, phases, and docs remain the execution surfaces rather than the owner of that behavior
- visible session ownership should remain a default task-list standard for session-owned work rather than a convention that only turns on when several sessions happen to share one task-list path
- shared-board multi-session coordination semantics such as session lease, handoff, retention/aging, anti-overclear behavior, optional-extension support, and session-state title grammar should defer to `shared-execution-coordination.md` rather than being reinvented ad hoc across task/phase/doc layers
- request-layer titles such as `For <session-short-id> owner: ...` should remain distinct from held-owner and blocked-owner title forms so board readers can identify session state consistently across usage modes
- shared board request-layer naming should remain distinct from receiving-side execution-layer phase structure so sender phase labels do not become the default visible title for accepted receiving-side work
- Root-level helper artifacts, support artifacts, and optional extension-package artifacts must stay clearly outside governed authority semantics unless intentionally promoted into a governed chain

---

## Verification Checklist

- [ ] Required document set matches project scope
- [ ] Changelog exists for each governed chain
- [ ] Version references align across chain metadata
- [ ] Active session metadata has no placeholders
- [ ] Full-history links resolve
- [ ] Meaningful governed work resolves startup artifact posture before drift
- [ ] Built-in task-list usage is treated as the live execution surface for non-trivial active work rather than as a governed document artifact
- [ ] `phase-implementation.md` is used as the semantic phase rule when applicable
- [ ] Phased work uses `phase/SUMMARY.md`
- [ ] Multi-phase work uses child phase files under `phase/`
- [ ] Phased work with governed patch artifacts shows explicit patch linkage from `phase/SUMMARY.md` and relevant child phase files
- [ ] Patch artifacts use `patch/<context>.patch.md` or root `<context>.patch.md` when patch is actually required
- [ ] Greenfield startup / baseline formation does not create patch by default unless a real existing before/after review surface or explicit user request justifies it
- [ ] Patch artifacts stay self-identifying and comparison-oriented
- [ ] Public onboarding/install guidance avoids workstation-specific absolute paths as public defaults
- [ ] Package-local support/extension source artifacts do not bake workstation-specific absolute paths into reusable source content by default
- [ ] Source-side guidance and destination/runtime guidance are clearly distinguished when both appear
- [ ] Exact local install examples are explicitly scoped when present
- [ ] Root-level helper artifacts remain non-governed
- [ ] Support or extension-package artifacts such as `plugin/**` do not masquerade as a second governance stack

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
| [artifact-initiation-control.md](artifact-initiation-control.md) v1.4 | Startup artifact-resolution owner |
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority contract |
| [document-design-control.md](document-design-control.md) v1.8 | Design structure standards |
| [document-patch-control.md](document-patch-control.md) v2.5 | Patch-governance boundary and explicit before/after patch contract outside live phase planning |
| [phase-implementation.md](phase-implementation.md) v2.14 | Semantic standard for phased execution planning and one-way design/patch source synthesis |
| [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) v1.2 | Portable shared-artifact defaults and anti-hardcoding discipline |
| [document-consistency.md](document-consistency.md) v1.6 | Source-side and destination/runtime reference consistency |
| [todo-standards.md](todo-standards.md) v2.12 | TODO structure standards plus startup-establishment bridge |
| [shared-execution-coordination.md](shared-execution-coordination.md) v1.3 | Shared-board multi-session coordination semantics, default session-state title grammar, visible session identity, lifecycle/retention behavior, request-layer naming, and receiving-side phase ownership boundary |

---

> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
