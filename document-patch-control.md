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
A patch is a governed before/during-execution change artifact showing **what will change**. It must let a reviewer identify the target artifact/location, current state, target state, and change type (`additive`, `replacement`, `deletion`, or `restructuring`).
A patch is not a retrospective summary, phase summary, rollout dashboard, prose-only recap, deletion authority, or generic plan with unclear before/after delta. Reviewability is the key distinction: a reader should not have to infer what artifact changes, where the change applies, or how current state maps to target state.
Allowed locations are `patch/<context>.patch.md` for active review, `patch/done/<context>.patch.md` for inactive completed history, or root `<context>.patch.md` when top-level placement is clearer. Filenames must be self-identifying and version-suffix-free; generic `patch.md` is not allowed.
`patch/done/` is inactive-by-default history, completed status is not junk/deletion authority, and live phased execution planning does not belong in `/patch`, `patch/done/`, or root `*.patch.md`. `phase-implementation-template.md` remains a reusable non-governed helper.
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
- metadata alignment proves review-surface integrity only; it does not make patch the version authority or move design/phase responsibilities into patch
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
Reviewable change items should avoid vague targets such as “update docs” or “clean up wording” unless the section, artifact, current state, target state, and change type are still explicit. Optional implementation order can explain sequencing, but it cannot replace the required before/after comparison.
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
Patch owns tactical before/after review: identity, metadata, target-design/history links, change representation, synchronization behavior, filename/location rules, completed patch history, and the boundary keeping live phase planning out of patch artifacts.
Phase owns live staged execution through `/phase`, `phase/SUMMARY.md`, and child phase detail files. Phase semantics, sequencing, design traceability, execution-step quality, patch-input synthesis, TODO/changelog coordination, handoffs, verification, rollback, and `SUMMARY.md` quality defer to `phase-implementation.md`.
`/patch` must not become the live phase-plan namespace, active phase summary/index, or per-phase execution file location. `phase-implementation.md` may synthesize patch inputs into live planning, but that creates no reverse-link requirement from patch/design to phase and does not move live planning into patch artifacts.
---
## Completed Patch History Surface
Active review scans start with active `patch/<context>.patch.md` and root `<context>.patch.md`. Consult `patch/done/` only for history, audit, rollback, provenance, or trace reconstruction; do not treat completed patch artifacts as active phase inputs, junk, or deletion-authorized by status alone. If completed patch history still matters to current review, reference it from the active patch/changelog/phase surface rather than making `patch/done/` the default active scan namespace.
---
## Compliance Checklist
- [ ] Patch path and filename use an allowed self-identifying, version-suffix-free location.
- [ ] Metadata is complete, session metadata is real, `Target Design` / `Full history` links resolve, and patch version aligns with patch changelog when applicable.
- [ ] Patch includes context, analysis, change items, verification, and rollback approach.
- [ ] Each concrete change item identifies target location, change type, before/current state, after/target state, and enough comparison detail for review.
- [ ] Non-code/conceptual patches explicitly say so and still provide structured before/after comparison.
- [ ] Patch remains outside TODO/changelog/phase authority, `patch/done/` stays inactive history, and root `phase-implementation-template.md` remains non-governed.
- [ ] Governance update order and related design/runtime/changelog/TODO/phase references are not obviously stale.
---
## Quality Metrics
| Metric | Target |
|---|---|
| Patch metadata, placement, links, and version alignment | 100% |
| Patch reviewability and target/change representation | 100% |
| Patch/done inactive-history and patch-vs-phase boundary | 100% |
| Active placeholder session markers, live phase files under patch, or broken history links | 0 |
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
