# Document Patch Control

> **Current Version:** 1.9
> **Design:** [design/document-patch-control.design.md](design/document-patch-control.design.md) v1.9
> **Session:** 92fed037-8ba9-48a6-95c4-e1085f28bb32
> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)

---

## Rule Statement

**Core Principle: Patch documents are governed patch/review artifacts, while live phased execution must use a dedicated `/phase` workspace with `SUMMARY.md` and separate child per-phase files.**

Patch docs remain the canonical place for governed patch artifacts. Changelog remains the version authority, and TODO remains execution-only tracking.

---

## Core Requirements

### 1) Naming and Location

#### 1.1 Patch naming
- Patch filename format: `<context>.patch.md`
- Recommended location: `patches/`
- Do not use version suffixes in filenames

#### 1.2 `/phase` separation
Live phased execution planning does not belong in `/patches`.
The dedicated live phase-plan workspace is:

```text
phase/
  SUMMARY.md
  phase-010-<phase-name>.md
  phase-020-<phase-name>.md
```

#### 1.3 Helper placement
- The canonical reusable phase-planning helper for this repository is `phase-implementation-template.md` at the RULES root
- Root-level placement improves discoverability but does not make the helper authoritative

### 2) Mandatory Metadata

#### 2.1 Patch metadata
Each patch document must include:
- `Current Version`
- `Session`
- `Status`
- `Target Design`
- `Full history` link

#### 2.2 Patch changelog metadata
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

Patch documents may reference phased execution work, but the live phase summary/index and per-phase execution detail must remain in `/phase`.

### 4) Patch-versus-Phase Authority Split

#### 4.1 Patch role
When patch documents are used, they remain governed patch/review artifacts.

They remain appropriate for:
- tactical migration or review plans
- governed change artifacts
- transition analysis tied to patch governance
- metadata-governed execution/review documents that are not the live phase workspace

#### 4.2 Phase role
The live phased execution workspace is `/phase`.

It contains:
- `phase/SUMMARY.md` as the governed summary/index
- `phase/phase-010-*.md` and peers as child phase-detail files

#### 4.3 Prohibited blending
The following are not allowed:
- using `/patches` as the live phase-plan namespace
- storing the active phase summary/index in a patch file instead of `phase/SUMMARY.md`
- storing live per-phase execution files under `/patches`

#### 4.4 Semantic authority
If phased execution exists, it should follow `phase-implementation.md` for:
- when phase planning should be used versus not used
- the required `/phase` structure
- stable phase fields
- design references per phase
- status and action-point expectations
- TODO coordination and changelog coordination
- cross-phase handoffs
- verification and rollback boundaries

#### 4.5 What this chain owns
`document-patch-control.md` owns patch governance and metadata.
It also owns the boundary that keeps live phased execution out of `/patches`.

It does **not** own the full semantic definition of phase planning.

### 5) Session Integrity

- Active patch metadata must use real session IDs
- Placeholder markers are not allowed in active metadata
- `LEGACY-*` is allowed only for historical records when original session data is unavailable

### 6) Version Alignment

- Patch `Current Version` must align with patch changelog `Current Version`
- `Target Design` reference must resolve to an existing design document/version
- Patch metadata synchronization follows governance order with final patch sync when affected

### 7) Patch Checklist Boundary

The `document-patch-control` checklist validates **governed patch quality** only.

Validate here:
- patch identity and metadata
- target-design and history-link integrity
- patch structure and reviewability
- synchronization behavior
- patch-versus-phase namespace separation

Do not validate here:
- phase necessity
- phase sequencing quality
- per-phase design-traceability and execution quality
- per-phase execution-step quality
- `SUMMARY.md` content quality

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
- [ ] Patch remains identifiable as a governed patch artifact
- [ ] `phase-implementation.md` is referenced for phase semantics when applicable
- [ ] Root-level `phase-implementation-template.md` remains non-governed
- [ ] The patch does not act like TODO authority or changelog authority
- [ ] The patch does not masquerade as the live `/phase` summary/index or per-phase detail layer

### 3) Structure and Reviewability
- [ ] Patch includes context, analysis, implementation plan, verification criteria, and rollback approach
- [ ] A reviewer can identify what is changing and why this patch exists
- [ ] A reviewer can identify the intended target design or target state
- [ ] The patch remains readable as a governed change/review artifact because live phase detail is kept outside `/patches`

### 4) Synchronization Behavior
- [ ] Governance update order remains consistent when the patch participates in synchronized work
- [ ] Related design, runtime, changelog, TODO, and `/phase` references are not obviously stale
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
| Patch-versus-phase namespace separation clarity | 100% |
| Patch-governance checklist boundary clarity vs phase-implementation | 100% |
| Live phased execution files under `/patches` | 0 |
| Broken patch history links | 0 |

---

## Integration

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority and metadata contract |
| [project-documentation-standards.md](project-documentation-standards.md) v2.3 | Project-level document governance and role boundary model |
| [phase-implementation.md](phase-implementation.md) v1.3 | Semantic authority for phased execution planning |
| [todo-standards.md](todo-standards.md) v2.2 | Execution tracking alignment |
| [phase-implementation-template.md](phase-implementation-template.md) | Non-governed root helper for authoring |

---

> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)
