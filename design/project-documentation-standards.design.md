# Project Documentation Standards

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.25
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd (2026-04-17)

---

## 1) Goal

Provide one deterministic, low-confusion repository model across README, runtime rules, design documents, changelog files, TODO trackers, phase-planning artifacts, patch documents, and support or extension-package artifacts.

Shared governed docs and templates should remain portable by default rather than embedding machine-specific environment assumptions as if they were universal repository truth.

Public onboarding/install docs should also stay portable by default so cloneable or self-contained repositories do not teach one workstation's absolute path or an internal umbrella workspace root as the default way to install or use the project.

This model must preserve one authority system while clearly separating:
- `phase-implementation.md` as the first-class rule for phase semantics
- `phase/SUMMARY.md` as the governed summary/index for the active phase plan
- `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` as governed execution files
- `patch/<context>.patch.md` or root `<context>.patch.md` as patch-governance artifacts outside the live phase workspace
- `phase-implementation-template.md` as the readable root-level helper
- Claude Code's built-in task list as the live in-session execution surface for non-trivial work
- `TODO.md` and changelog as required durable companions, but not as replacements for the phase plan itself
- design, phase, TODO, task-list, and checked implementation state as execution-discovery surfaces once execution mode is already active
- `artifact-initiation-control.md` as the startup-governance owner that resolves artifact posture before meaningful work drifts
- `portable-implementation-and-hardcoding-control.md` as the semantic owner of portable-default and anti-hardcoding behavior
- `document-consistency.md` as the supporting owner for source-side versus destination/runtime notation consistency
- `plugin/` as an optional extension-package area whose implementation assets stay subordinate to the root governance stack
- package-local support assets such as optional `skills/`, optional `agents/`, scripts, and plugin-owned docs remaining portable by default when they are maintained as reusable source artifacts
- shared-board multi-session coordination semantics, including shared-board-specific memsearch handling, staying outside Main RULES scope rather than being redefined ad hoc in the repository role model
- visible session ownership remaining a default task-list standard for session-owned work rather than a convention that only turns on when several sessions share one task-list path
- request-layer naming remaining distinct from receiving-side execution-layer phase structure so sender phase labels do not become the default visible handoff title

---

## 2) Scope

Applies to projects that keep governed documentation artifacts and support/reference materials in the same repository.

This includes:
- repository role boundaries across README, design, changelog, TODO, phase, and patch artifacts
- startup artifact posture before meaningful governed work
- public onboarding/install guidance in README or adjacent install docs
- source-side versus destination/runtime notation clarity when install docs name both

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
`TODO.md` tracks durable repository/project execution state only.
It is not a version-authority document.

Claude Code's built-in task list is the live in-session execution surface for active non-trivial work.
It does not replace `TODO.md`, and `TODO.md` does not replace live task visibility during active work.
Visible session ownership should remain a default board-facing standard for session-owned task-list work whether the current task list is being used by one session or several.

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
It is not the default startup artifact for greenfield / baseline-formation work when no stable before-state exists yet.

### 3.9 Startup Artifact-Initiation Role
`artifact-initiation-control.md` is the semantic owner of startup artifact posture.
It decides whether design, changelog, TODO, phase, and patch should be reused, created now, asked about now, or marked not required before meaningful work drifts.

### 3.10 Phase Rule Role
`phase-implementation.md` is the semantic rule for phased execution planning.
It owns phase semantics after `/phase` is required.

### 3.11 Root Helper Role
`phase-implementation-template.md` is a non-governed root helper.
It exists for readability, drafting, and reuse.

### 3.12 Extension-Package Role
`plugin/**` may exist as an optional extension-package area.
It may contain package-local implementation assets such as:
- `README.md`
- `.claude-plugin/`
- `hooks/`
- `scripts/`
- optional `skills/`
- optional `agents/`

Those package-local assets remain support/implementation surfaces.
They do not create a second design/changelog/phase/TODO authority stack under `plugin/`.

---

## 4) Required Document Set

| Document | Required When | Purpose | Governance Role |
|----------|---------------|---------|-----------------|
| `README.md` | Always | Overview, onboarding, repository map | Overview only |
| `design/*.design.md` | Design/specification needed | Active target-state guidance | Governed design layer |
| `changelog/*.changelog.md` | Chain history needed | Authoritative version history | Governed authority layer |
| `TODO.md` | Work tracking needed | Durable repository/project execution tracking | Execution layer |
| `phase/SUMMARY.md` | Phased execution planning is required | Governed summary/index for live phase planning | Governed phase summary layer |
| `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` | Multi-stage execution detail exists | Major/subphase execution detail | Governed phase-detail layer |
| `patch/<context>.patch.md` or root `<context>.patch.md` | A separate before/after review artifact for an existing governed surface is required | Governed patch/review artifact outside the live phase workspace | Governed patch layer |
| `artifact-initiation-control.md` | Startup artifact posture must be standardized | First-class startup-governance behavior | Governed runtime rule |
| `phase-implementation.md` | Phase semantics need to be standardized | First-class rule for phased planning behavior | Governed runtime rule |
| `phase-implementation-template.md` | Reusable phased authoring aid is needed at repository root | Readable root-level helper template | Non-governed helper artifact |
| `support/**/*.md`, `plugin/**`, or equivalent support/extension path | Reference-only content or optional extension-package content exists | Support/reference or extension-package artifacts | Non-governed support / extension layer |

---

## 5) UDVC-1 Integration

### 5.1 Single Authority Per Chain
- Changelog is the authority for each governed chain.
- Runtime, design, phase, and patch metadata align to that chain authority where applicable.
- Root-level helper artifacts, support artifacts, and optional extension-package artifacts do not create parallel version authority.

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

When phased work also uses governed patch artifacts, the phase workspace should declare that linkage explicitly in `phase/SUMMARY.md` and the relevant child phase files instead of leaving patch participation implicit.

---

## 8) Public Onboarding and Install Guidance

### 8.1 Portable public default
For cloneable or self-contained repositories, public onboarding/install docs should default to repo-root-relative or otherwise portable source guidance.

### 8.2 Workstation-literal failure mode
One workstation absolute path or an internal umbrella workspace root should not be taught as the public default install source path.

### 8.3 Source-vs-destination notation split
If onboarding/install docs mention both where the artifact comes from and where it installs or runs, those two roles should stay visually and semantically distinct.

Preferred examples:
- source-side: `<repo-root>`, `./`
- destination/runtime-side: `<install-root>`, `<user-runtime-rules>`, `<user-runtime-skills>`, `<user-runtime-agents>`

### 8.4 Local-example exception
Exact local absolute paths are allowed only when they are explicitly framed as:
- checked local facts
- local workflow examples
- machine-scoped runtime contracts

This design delegates broader anti-hardcoding semantics to `portable-implementation-and-hardcoding-control.md` and notation consistency enforcement to `document-consistency.md`.

---

## 9) Verification Checklist

- [ ] Required document set matches project scope
- [ ] Changelog exists for each governed chain
- [ ] Version references align across chain metadata
- [ ] Active session metadata has no placeholders
- [ ] Full-history links resolve
- [ ] Meaningful governed work resolves startup artifact posture before drift
- [ ] Built-in task-list usage is treated as the live execution surface for non-trivial active work rather than as a governed document artifact
- [ ] `phase-implementation.md` is treated as the semantic phase-planning rule
- [ ] Phased work uses `phase/SUMMARY.md`
- [ ] Multi-stage execution uses canonical `NNN` / `NNN-NN` phase files under `phase/`
- [ ] Phased work with governed patch artifacts shows explicit patch linkage from `phase/SUMMARY.md` and relevant child phase files
- [ ] Patch artifacts use `patch/<context>.patch.md` or root `<context>.patch.md`
- [ ] Patch artifacts stay self-identifying and comparison-oriented
- [ ] Public onboarding/install docs avoid workstation-specific absolute paths as public defaults
- [ ] Source-side and destination/runtime notation are clearly distinguished when both appear
- [ ] Exact local install examples are explicitly scoped
- [ ] Root-level helper artifacts do not masquerade as governed docs

---

## 10) Quality Metrics

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
| Live task-vs-durable TODO distinction clarity | High |
| Execution-discovery surface clarity during active execution | High |
| Public onboarding/install portability | High |
| Workstation-specific absolute paths as public defaults | 0 critical cases |
| Source-vs-destination notation clarity | High |
| Root-helper placement clarity | 100% |
| TODO simplification compliance | 100% |

---

## 11) Integration

| Rule | Relationship |
|------|-------------|
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup artifact-resolution owner and early live task-tracking bridge |
| [document-changelog-control.md](../document-changelog-control.md) | Version authority contract |
| [document-design-control.md](../document-design-control.md) | Design structure standards |
| [document-patch-control.md](../document-patch-control.md) | Patch-governance boundary and explicit before/after patch contract outside live phase planning |
| [phase-implementation.md](../phase-implementation.md) | Semantic standard for phased execution planning and one-way design/patch source synthesis |
| [portable-implementation-and-hardcoding-control.md](../portable-implementation-and-hardcoding-control.md) | Portable shared-artifact defaults and anti-hardcoding discipline |
| [document-consistency.md](../document-consistency.md) | Source-side and destination/runtime reference consistency |
| [todo-standards.md](../todo-standards.md) | Durable TODO structure standards plus live task-list execution tracking and default visible session ownership for session-owned work |
| [shared-execution-coordination.md](../shared-execution-coordination.md) | Shared-board coordination semantics, default session-state title grammar, visible session identity, lifecycle/retention behavior, request-layer naming, and receiving-side phase ownership boundary |

---

> Full history: [../changelog/project-documentation-standards.changelog.md](../changelog/project-documentation-standards.changelog.md)
