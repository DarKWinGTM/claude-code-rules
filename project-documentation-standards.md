# Project Documentation Standards
> **Current Version:** 2.32
> **Design:** [design/project-documentation-standards.design.md](design/project-documentation-standards.design.md) v2.32
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
---
## Rule Statement
**Core Principle: Use one deterministic documentation baseline across README, design, runtime rules, changelog, TODO, `/phase`, `/patch`, completed history surfaces, and non-governed helper/support or extension-package artifacts; resolve startup posture before governed work drifts; declare patch participation in live phase when patch is in scope; keep public onboarding/install guidance portable.**
---
## Required Document Set
| Document | Required when | Purpose | Owner |
|---|---|---|---|
| `README.md` | always | overview/onboarding | standard practice |
| `design/*.design.md` | design/spec required | active target behavior/contract | `document-design-control` |
| `changelog/*.changelog.md` | version trace required | active version authority, current index, and navigation | `document-changelog-control` |
| `changelog/done/*.changelog.md` | completed/older history should leave active scans | inactive history for audit/rollback/provenance/trace | `document-changelog-control` |
| `TODO.md` | tracking required | durable execution tracking | `todo-standards` |
| `phase/SUMMARY.md` | phased work required | live phase summary/index | `phase-implementation` |
| `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md` | multi-stage detail required | active execution detail | `phase-implementation` |
| `phase/done/phase-NNN-*.md`, `phase/done/phase-NNN-NN-*.md` | completed phase detail retained outside active scans | inactive completed phase history | `phase-implementation` |
| `patch/<context>.patch.md` or root `<context>.patch.md` | patch/review required | active review artifact outside phase | `document-patch-control` |
| `patch/done/<context>.patch.md` | completed patch artifact retained outside active scans | inactive completed patch history | `document-patch-control` |
| `phase-implementation-template.md` | reusable authoring aid needed | readable helper | non-governed helper |
| `support/**/*.md`, `plugin/**`, equivalent | optional reference/extension needed | support/extension content | non-governed support |
---
## Authority and Sync
- Changelog is the single version authority per governed chain.
- Design/rule/phase/patch metadata align with authoritative changelog state where applicable.
- Root helpers, support artifacts, and extension-package assets do not become chain authority unless intentionally normalized into a governed chain.
- Governance update order: design → runtime rule → changelog → TODO → patch metadata final sync when affected.
- Active metadata must use real session identifiers; placeholders are not allowed in active metadata.
---
## Role Boundaries
- `phase-implementation.md` defines phase-planning semantics, including major-vs-subphase lineage selection.
- `phase/SUMMARY.md` is the governed live phase summary/index and should preserve phase-family lineage when that context affects future phase identity decisions.
- `phase/phase-NNN-*.md` and `phase/phase-NNN-NN-*.md` are governed active phase detail files.
- `phase/done/` is inactive-by-default completed phase history.
- Patch artifacts are self-identifying before/after review artifacts outside live phase planning, not recaps or phase summaries.
- `patch/done/` is inactive-by-default completed patch history.
- Active changelogs remain version authority; `changelog/done/` may hold inactive completed/older detailed history.
- `design/` remains active blueprint/target-state authority and does not use a default `design/done/` pattern.
- `phase-implementation-template.md` is a non-governed root helper.
- Support/package assets may include docs, scripts, hooks, optional skills/agents, or plugin scaffolds, but stay implementation/support surfaces, not root governance authority.
- Reusable support/package assets should stay portable and avoid workstation absolute paths unless explicitly machine-scoped.
- Design and patch artifacts need not point back to phase.
- Claude Code's built-in task list is live in-session tracking; `TODO.md` is durable tracking and does not replace live visibility or define phases.
- Runtime installs target the current project/source-owned active runtime rule files only; design, changelog, TODO, phase, patch, support, helper, and extension-package surfaces are not runtime-rule install targets unless a later explicit gate says otherwise.
- Shared runtime destinations may contain other project/plugin-owned runtime rules that remain out of scope unless their owner/project is explicitly selected or verified.
- Changelog records shipped/synchronized changes; it is not phase-definition storage.
- Live phase execution must not be stored under patch artifacts.
---
## Completed Documentation Surface Governance
Completed documentation surfaces reduce active scan bloat without deleting governed history.
Allowed completed-history surfaces:
- `phase/done/` for completed phase execution detail
- `patch/done/` for completed patch/review artifacts
- `changelog/done/` for older or completed detailed version history
Not a default completed-history surface:
- `design/done/`, because design is active blueprint and target-state authority
Required guidance:
- current-state scans start with active design, active changelog, `phase/SUMMARY.md`, active phase files, active patch files, `TODO.md`, and checked implementation state
- open `done/` surfaces only for history, audit, rollback, provenance, or trace reconstruction
- files in `done/` are not junk and completed status is not deletion authorization
- active surfaces must preserve enough pointer/index context for completed history to be found when needed
- broad scans should avoid `done/` and archive surfaces unless the task explicitly needs historical evidence
---
## Startup Artifact Gate
Before meaningful governed work continues, `artifact-initiation-control` must resolve each relevant artifact as `use existing`, `create now`, `ask now`, or `not required`; this is earlier than later sync order.
Required governed surfaces remain companions, not optional aids:
- design = target-state authority for material behavior/contract/policy changes
- changelog = governed version/history authority
- `TODO.md` = durable execution-tracking companion when tracked work is required
- `/phase` = staged-execution companion when phased work is required
- `/patch` = before/after review companion when patch is in scope
- built-in task list = live execution surface, not a replacement for required governed artifacts
When a checked repo/workstream is phased or staged, live task creation should align to that execution model. Current phase, phase family, order/dependencies, authored next phases, and checked lineage may guide bounded discovery and draft visibility, but unopened future phases do not become active automatically. Creating or selecting a phase file should defer to `phase-implementation.md` for current phase versus subphase versus new-major selection.
---
## New or Unclear File Classification
When a newly encountered file appears during governed work and its role is unclear, keep it unresolved rather than collapsing uncertainty into cleanup/disposal logic.
A destination/runtime file outside the current source-owned active runtime install set is not unmanaged project junk merely because it is co-located in a shared runtime destination.
Required guidance:
- check master surfaces and relevant governed owner chains first
- resolve owner/project scope before classifying destination/runtime files outside the current source-owned install set
- keep git state and runtime co-location as observed local evidence only
- avoid disposal conclusions unless stronger semantic authority and stronger deletion authorization both exist
Minimum active lookup set when applicable: `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, relevant active `phase/`, and relevant active `patch/`; consult `phase/done/`, `patch/done/`, or `changelog/done/` only when history/audit/rollback/provenance/trace context is needed.
`not required` does not mean `safe to remove` without stronger authority and destructive-execution permission.
---
## Document Creation Model
```text
Meaningful governed work begins
  ↓
Resolve startup posture
  ↓
Need design? use existing / create now / ask now
Need version trace? use existing / create now / ask now
Need durable tracking? use existing / create now / ask now
Need live non-trivial visibility? initialize built-in task list early
Need phased planning? establish phase/SUMMARY.md + lineage-selected child files now or ask now
Need patch/review? use patch/<context>.patch.md only for real before/after surface or explicit request
Greenfield baseline alone: patch not required by default
  ↓
Continue substantive work after posture is resolved
```
---
## Public Onboarding and Install Guidance
README/onboarding/install docs stay portable by default.
Required guidance:
- prefer repo-root-relative source guidance for cloneable/self-contained repos
- do not present workstation absolute paths or internal umbrella roots as public defaults
- distinguish source-side notation from destination/runtime notation
- use placeholders or contract labels for destination/runtime paths
- when naming runtime install scope, identify the current project/source-owned active runtime rule set rather than the whole shared destination directory
- exact local paths may appear only as checked local facts, local examples, or machine-scoped contracts
- for repo-root commands, prefer `./` or `<repo-root>` over a workstation path
---
## Cross-Document Alignment
- Shared governed docs/templates stay portable by default.
- Support/extension source artifacts avoid workstation defaults in reusable content.
- Exact local values appear only as local observations or machine-scoped contracts.
- Public onboarding uses portable source guidance and labeled destination/runtime notation.
- Portable defaults defer to `portable-implementation-and-hardcoding-control.md`; source/destination consistency defers to `document-consistency.md`.
- Required document set matches project scope; full-history/parent links resolve; active metadata has no placeholder sessions.
- `phase/SUMMARY.md` + child phase files remain the governed phase workspace when staged planning is required.
- `phase/SUMMARY.md` should preserve enough phase-family lineage to support later major-vs-subphase decisions.
- Patch artifacts stay outside live phase namespace and phased work with governed patches shows phase-to-patch linkage.
- Built-in task list is live tracking, not a governed repository document.
- Live task list does not downgrade required design/changelog/TODO/phase/patch surfaces.
- Within one active objective, normally reuse/extend the live task list rather than replacing it.
- Design, phase, TODO, task list, and checked implementation state may guide execution discovery once work is in execution mode.
- `/phase` may contribute current and authored next structure; unopened future phases remain bounded planning input until explicitly active.
- Shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES scope.
- Root helpers, support artifacts, and optional extension packages remain outside governed authority unless intentionally promoted.
---
## Verification Checklist
- [ ] Required document set matches scope
- [ ] Changelog/version references align where applicable
- [ ] Active session metadata has no placeholders
- [ ] Full-history and parent links resolve
- [ ] Startup posture is resolved before drift
- [ ] Required governed surfaces remain companions, not optional aids
- [ ] Unclear files are checked against master surfaces before junk/disposal classification
- [ ] Built-in task list remains live execution surface, not governed document artifact
- [ ] Phased work uses `phase/SUMMARY.md` and active child files when required
- [ ] Phase records preserve enough phase-family lineage for future major-vs-subphase decisions
- [ ] Phase file creation/selection defers to `phase-implementation.md` instead of defaulting to a new major phase
- [ ] Completed phase, patch, and changelog history uses `phase/done/`, `patch/done/`, and `changelog/done/` only as inactive-by-default history
- [ ] No default `design/done/` pattern is introduced for governed blueprint docs
- [ ] Phased work with governed patches shows explicit patch linkage
- [ ] Patch artifacts use allowed self-identifying paths and stay comparison-oriented outside live phase planning
- [ ] Greenfield baseline does not create patch by default unless justified
- [ ] Public onboarding avoids workstation paths as public defaults
- [ ] Support/extension source avoids workstation reusable defaults
- [ ] Source-side and destination/runtime guidance are distinct
- [ ] Runtime install scope is limited to current project/source-owned active runtime rule files in shared destinations
- [ ] Other project/plugin-owned runtime destination files are not classified, managed, or deleted by repository documentation wording alone
- [ ] Root helpers remain non-governed
- [ ] Support/extension packages do not masquerade as a second governance stack
---
## Quality Metrics
| Metric | Target |
|---|---|
| Required document coverage and version-reference correctness | 100% |
| Active metadata integrity and cross-link validity | 100% |
| Phase/summary/child-phase/patch role clarity | 100% |
| Phase lineage preservation for future phase identity decisions | High |
| Completed-history inactive-surface boundary clarity | 100% |
| Explicit phase-to-patch linkage when patch is in scope | 100% |
| Startup artifact posture before drift | 100% |
| Public onboarding/install portability | high |
| Workstation paths as public defaults | 0 critical cases |
| Source-vs-destination clarity, shared-destination owner boundary, and TODO simplification | high / 100% |
---
## Integration
| Rule | Relationship |
|---|---|
| [artifact-initiation-control.md](artifact-initiation-control.md) v1.7 | startup artifact-resolution owner |
| [document-changelog-control.md](document-changelog-control.md) v4.8 | version authority and `changelog/done/` completed history boundary |
| [document-design-control.md](document-design-control.md) v1.10 | design structure and no-default-`design/done/` boundary |
| [document-patch-control.md](document-patch-control.md) v2.7 | patch boundary, before/after contract, and `patch/done/` completed history boundary |
| [phase-implementation.md](phase-implementation.md) v2.26 | phased execution semantics, major-vs-subphase lineage selection, and `phase/done/` completed history boundary |
| [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) v1.2 | portable shared-artifact defaults |
| [document-consistency.md](document-consistency.md) v1.8 | source/destination and source-owned/shared-destination reference consistency |
| [todo-standards.md](todo-standards.md) v2.17 | TODO structure and startup bridge |
| [design/rules-plugin-extension.design.md](design/rules-plugin-extension.design.md) | historical plugin-extension boundary; active plugin/runtime coordination is not Main RULES doctrine |
---
> **Full history:** [changelog/project-documentation-standards.changelog.md](changelog/project-documentation-standards.changelog.md)
