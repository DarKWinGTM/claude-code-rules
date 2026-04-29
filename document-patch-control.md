# Document Patch Control
> **Current Version:** 2.7
> **Design:** [design/document-patch-control.design.md](design/document-patch-control.design.md) v2.7
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)
---
## Rule Statement
**Core Principle: Patch documents are governed patch/review artifacts outside the live `/phase` workspace, a patch means a self-identifying before/after change artifact clear enough for review, and completed patch artifacts may move to inactive `patch/done/` history without becoming junk or active inputs by default.**
Patch docs are governed patch artifacts. Changelog remains version authority; TODO remains execution tracking.
---
## Patch Meaning and Location
A patch is a governed change artifact showing **what will change** before or during reviewable execution.
A valid patch must let a reviewer answer:
- what artifact changes
- where it changes
- what exists now
- what it should become after the change
- whether the change is additive, replacement, deletion, or restructuring
A patch is **not** a retrospective summary, phase summary, rollout dashboard, prose-only recap, or generic plan with unclear before/after delta.
Allowed governed patch locations:
- active patch artifact: `patch/<context>.patch.md`
- inactive completed patch history: `patch/done/<context>.patch.md`
- root `<context>.patch.md`
Required guidance:
- filename must be self-identifying and version-suffix-free
- `patch/` is the default shared patch directory for active patch/review artifacts
- `patch/done/` is inactive-by-default completed patch history
- root placement is allowed when top-level placement is clearer
- generic `patch.md` is **not allowed**
- live phased execution planning does not belong in `/patch`, `patch/done/`, or root `*.patch.md`
- completed status does not make a patch artifact junk and does not authorize deletion
- `phase-implementation-template.md` at RULES root is a reusable non-governed helper; discoverability does not make it authority
---
## Metadata and Alignment
Patch metadata must include `Current Version`, `Session`, `Status`, `Target Design`, and `Full history` link.
Patch changelog metadata must include `Parent Document`, `Current Version`, and `Session`.
Integrity requirements:
- active patch metadata must use real session IDs; placeholders are not allowed
- `LEGACY-*` is allowed only for historical records when original session data is unavailable
- patch `Current Version` must align with patch changelog `Current Version`
- `Target Design` must resolve to an existing design document/version
- patch metadata synchronization follows governance order with final patch sync when affected
---
## Patch Structure and Reviewability
Every governed patch must include:
1. Context
2. Analysis
3. Change items
4. Verification
5. Rollback approach
Optional implementation order is allowed when sequencing matters, but it does not replace required change items.
Each concrete change item must show:
- target artifact or stable target location
- change type: `additive`, `replacement`, `deletion`, or `restructuring`
- current/before state
- target/after state
- enough comparison detail for review
Preferred comparison forms: before/after snippets, current/target tables, unified diff blocks, patch hunk sections with target path and anchors, or scoped command/config replacement blocks.
Acceptable target locators include file path, section heading, function/class/query name, config key path, route/endpoint name, command block label, or schema object/table/column reference. If line numbers are unstable, use the most precise stable locator.
Non-code or governance-only patches may omit code snippets **only if** they explicitly say the patch is non-code/non-snippet, the change surface is conceptual/governance/structural, and concrete runtime edits are intentionally out of scope.
A patch is under-specified when a reviewer cannot identify what changes, where it changes, current state, proposed state, and how before/after comparison maps to the intended modification.
---
## External-Requirement Basis
When a change is constrained by external docs, API specs, provider references, or comparable implementation authorities, the patch should make the implementation-relevant basis visible enough for review.
Required guidance:
- point to normalized design truth when design already owns the extracted requirement
- patch may summarize the change-driving external requirement but must not replace design as target-state truth
- if external requirements determine request parameters, authentication, callbacks, acceptance criteria, field semantics, or integration constraints, make that basis legible in context/analysis
- do not rely on transient doc-reading memory alone for later review passes
---
## Patch vs Phase Authority Split
Patch role:
- tactical change artifact
- governed review artifact
- patch-specific transition analysis
- reviewable current→target documentation outside live phase workspace
- inactive completed patch history under `patch/done/` when history/audit/rollback/trace may be needed
Patch is not retrospective summary, general progress recap, active phase summary/index, live per-phase execution file, or deletion authority.
Phase role:
- `/phase` is the live phased execution workspace
- `phase/SUMMARY.md` is the governed summary/index
- `phase/phase-NNN-*.md` and subphase peers are child phase-detail files
Prohibited blending:
- using `/patch` as the live phase-plan namespace
- storing the active phase summary/index in a patch file
- storing live per-phase execution files in patch artifacts
If phased execution exists, phase semantics defer to `phase-implementation.md`: use conditions, required structure, stable fields, design references, patch-input synthesis, status/action points, TODO/changelog coordination, handoffs, verification, and rollback.
`phase-implementation.md` may synthesize patch inputs into live phase planning. This creates no reverse-link requirement from patch/design to phase and does not move live planning into patch artifacts.
`document-patch-control.md` owns patch governance, metadata, before/after representation, filename/location rules, completed patch history semantics, and the boundary keeping live phase planning out of patch artifacts. It does **not** own full phase-planning semantics.
---
## Completed Patch History Surface
`patch/done/` is inactive-by-default completed patch history.
Required guidance:
- active review scans start with active `patch/<context>.patch.md` and root `<context>.patch.md` surfaces
- consult `patch/done/` only for history, audit, rollback, provenance, or trace reconstruction
- do not treat completed patch artifacts as active phase inputs by default
- do not treat files in `patch/done/` as junk or deletion-authorized by completed status alone
---
## Patch Checklist Boundary
Validate here: patch identity/metadata, target-design and history links, structure/reviewability, change representation, synchronization behavior, and patch-versus-phase namespace separation.
Do not validate here: phase necessity, phase sequencing quality, per-phase design traceability, per-phase execution-step quality, or `SUMMARY.md` content quality. Those belong to `phase-implementation.md`.
---
## Compliance Checklist
- [ ] Patch path uses `patch/<context>.patch.md`, `patch/done/<context>.patch.md`, or root `<context>.patch.md`
- [ ] Patch filename is self-identifying and version-suffix-free
- [ ] Patch metadata fields are complete and session metadata is real
- [ ] `Target Design` and `Full history` links resolve
- [ ] Patch version aligns with patch changelog when applicable
- [ ] Patch remains identifiable as a governed patch artifact
- [ ] `patch/done/` artifacts remain inactive-by-default history, not junk or deletion authority
- [ ] Patch does not act like TODO, changelog, phase summary, or phase detail authority
- [ ] Root `phase-implementation-template.md` remains non-governed
- [ ] Patch includes context, analysis, change items, verification, and rollback approach
- [ ] Each concrete change item identifies target location, change type, before/current state, and after/target state
- [ ] Non-code/conceptual patches explicitly say so and still provide structured before/after comparison
- [ ] A reviewer can understand the change surface without guessing
- [ ] Governance update order remains consistent when patch participates
- [ ] Related design, runtime, changelog, TODO, and `/phase` references are not obviously stale
- [ ] Patch history references remain valid and patch remains self-identifying outside its directory context
---
## Quality Metrics
| Metric | Target |
|---|---|
| Patch metadata completeness and placement clarity | 100% |
| `patch/done/` inactive-history boundary clarity | 100% |
| Active placeholder session markers | 0 |
| Patch ↔ changelog version and target-design alignment | 100% |
| Patch role, change representation, target location, and phase namespace separation | 100% |
| Patch-governance checklist boundary vs phase-implementation | 100% |
| Live phased execution files under patch artifacts | 0 |
| Broken patch history links | 0 |
---
## Integration
| Document | Relationship |
|---|---|
| [document-changelog-control.md](document-changelog-control.md) v4.8 | Version authority, metadata, and completed changelog history contract |
| [project-documentation-standards.md](project-documentation-standards.md) v2.31 | Project document governance, role boundaries, and completed-surface model |
| [phase-implementation.md](phase-implementation.md) v2.25 | Semantic authority for phased execution planning and `phase/done/` boundary |
| [todo-standards.md](todo-standards.md) v2.17 | Execution tracking alignment |
| [phase-implementation-template.md](phase-implementation-template.md) | Non-governed root helper |
---
> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)
