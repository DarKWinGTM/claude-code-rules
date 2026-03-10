# Document Patch Control

> **Current Version:** 1.7
> **Design:** [design/document-patch-control.design.md](design/document-patch-control.design.md) v1.7
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402
> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)

---

## Rule Statement

**Core Principle: Patch documents are the governed execution-plan layer, while `phase-implementation.md` defines phase semantics and the root template remains a non-governed helper.**

Patch docs remain the canonical place for migration and implementation transition planning. Changelog remains the version authority, and TODO remains execution-only tracking.

---

## Core Requirements

### 1) Naming and Location

- Patch filename format: `<context>.patch.md`
- Recommended location: `patches/`
- Do not use version suffixes in filenames
- The canonical reusable phase-planning helper for this repository is `phase-implementation-template.md` at the RULES root
- Root-level placement improves discoverability but does not make the helper authoritative

### 2) Mandatory Metadata

Each patch document must include:
- `Current Version`
- `Session`
- `Status`
- `Target Design`
- `Full history` link

Each patch changelog must include:
- `Parent Document`
- `Current Version`
- `Session`

### 3) Patch Content Structure

Patch documents must include, at minimum:
1. Context (current vs target)
2. Analysis (risk and dependencies)
3. Implementation plan
4. Verification criteria
5. Rollback approach

The implementation plan may be linear or phase-based depending on project reality.

### 4) Phase-Planning Authority Split

When phased execution is used:
- `patches/*.patch.md` remains the live governed execution-plan artifact
- `phase-implementation.md` defines phase semantics
- `phase-implementation-template.md` may assist authoring as a non-governed helper

`document-patch-control.md` owns patch governance and metadata.
It does **not** own the full semantic definition of phase planning.

### 5) Phase-Based Patch Expectation

If a patch uses phases, it should follow `phase-implementation.md` for:
- when phase planning should be used versus not used
- flexible order behavior
- stable phase fields
- design references per phase
- status and action-point expectations
- TODO coordination and changelog coordination
- cross-phase handoffs
- verification and rollback boundaries

### 6) Session Integrity

- Active patch metadata must use real session IDs
- Placeholder markers are not allowed in active metadata
- `LEGACY-*` is allowed only for historical records when original session data is unavailable

### 7) Version Alignment

- Patch `Current Version` must align with patch changelog `Current Version`
- `Target Design` reference must resolve to an existing design document/version
- Patch metadata synchronization follows governance order with final patch sync when affected

### 8) Patch Checklist Boundary

The `document-patch-control` checklist validates **governed patch quality** only.

Validate here:
- patch identity and metadata
- target-design and history-link integrity
- patch structure and reviewability
- synchronization behavior

Do not validate here:
- phase necessity
- phase sequencing quality
- per-phase design-traceability and execution quality
- per-phase execution-step quality

Those belong to `phase-implementation.md` when phases are used.

---

## Compliance Checklist

Use this checklist to validate the patch as a governed artifact.

### 1) Identity and Metadata
- [ ] Filename uses `.patch.md` format
- [ ] Patch metadata fields are complete
- [ ] Session metadata is real (no placeholders)
- [ ] `Target Design` reference resolves correctly
- [ ] `Full history` links resolve correctly

### 2) Patch Authority Integrity
- [ ] Patch version aligns with patch changelog version when applicable
- [ ] Patch remains the governed execution-plan instance when phased planning is used
- [ ] `phase-implementation.md` is referenced for phase semantics when applicable
- [ ] Root-level `phase-implementation-template.md` remains non-governed
- [ ] The patch does not act like TODO authority or changelog authority

### 3) Structure and Reviewability
- [ ] Patch includes context, analysis, implementation plan, verification criteria, and rollback approach
- [ ] A reviewer can identify what is changing and why this patch exists
- [ ] A reviewer can identify the intended target design or target state
- [ ] The patch remains readable as a governed change/review artifact even when it includes phases

### 4) Synchronization Behavior
- [ ] Governance update order remains consistent when the patch participates in synchronized work
- [ ] Related design, runtime, changelog, and TODO references are not obviously stale
- [ ] Patch history references remain valid after synchronization

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Patch metadata completeness | 100% |
| Active placeholder session markers | 0 |
| Patch ↔ changelog version alignment | 100% |
| Patch ↔ target design reference validity | 100% |
| Patch-role clarity | 100% |
| Patch-governance checklist boundary clarity vs phase-implementation | 100% |
| Phase semantic duplication in patch-control | 0 |
| Broken patch history links | 0 |

---

## Integration

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority and metadata contract |
| [project-documentation-standards.md](project-documentation-standards.md) v2.1 | Project-level document governance and role boundary model |
| [phase-implementation.md](phase-implementation.md) v1.1 | Semantic authority for phased execution planning |
| [todo-standards.md](todo-standards.md) v2.2 | Execution tracking alignment |
| [phase-implementation-template.md](phase-implementation-template.md) | Non-governed root helper for authoring |

---

> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)
