# Document Patch Control

## 0) Document Control

> **Parent Scope:** Project Documentation Standards
> **Current Version:** 1.7
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402 (2026-03-10)

---

## 1) Goal

Standardize patch-document governance under the same UDVC-1 metadata and version-trace contract used by other governed document chains, while keeping patch docs as the live governed execution-plan artifacts.

When phased execution planning is used inside a patch, semantic phase behavior should come from `phase-implementation.md` rather than being redefined here.

---

## 2) Scope

Applies to:
- `patches/*.patch.md`
- patch lifecycle documentation
- patch metadata traceability and history references
- governed execution-plan instances, whether linear or phase-based

The root helper `phase-implementation-template.md` may help authors draft a plan, but it is not itself a governed chain.

---

## 3) Naming and Location

- Patch document filename: `<context>.patch.md`
- Preferred location: `patches/`
- Do not use version suffixes in filenames
- The canonical reusable helper for this repository is the root-level `phase-implementation-template.md`
- Root-level helper placement improves discoverability, but helper placement does not change chain authority

---

## 4) Mandatory Metadata

Each patch document must include:
- `Current Version`
- `Session`
- `Status`
- `Target Design`
- `Full history` link

Patch changelog files must include:
- `Parent Document`
- `Current Version`
- `Session`

---

## 5) Patch Structure Baseline

Every governed patch document must include, at minimum:
1. Context (current state vs target state)
2. Analysis (risk, constraints, dependencies)
3. Implementation plan
4. Verification
5. Rollback approach

The implementation-plan section may be linear for simple work or phase-based for staged work.

---

## 6) Phase-Planning Boundary

### 6.1 Live instance role

If a project needs a phased execution plan, the live governed instance belongs in the patch document.

### 6.2 Semantic authority

If a patch uses phases, the patch should follow `phase-implementation.md` for:
- when phase planning is appropriate
- flexible phase ordering
- stable per-phase fields
- design traceability
- status and action-point expectations
- TODO and changelog coordination inside the plan
- cross-phase handoffs
- verification and rollback boundaries

### 6.3 What this chain owns

`document-patch-control` owns:
- patch metadata rules
- patch filename and location rules
- patch lifecycle and synchronization behavior
- patch role as the governed execution-plan layer
- patch checklist expectations for governed review/change artifacts

It does **not** serve as the primary semantic authority for phase behavior.

---

## 7) Version and Session Integrity

- Patch active metadata must not contain placeholder sessions.
- If patch version is updated, corresponding changelog metadata must be synchronized.
- Target design version references must be resolvable and current.

---

## 8) Patch Checklist Boundary

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

Those remain the responsibility of `phase-implementation` when phase planning is used.

---

## 9) Patch Governance Checklist

Use this checklist to validate the patch as a governed artifact.

### 9.1 Identity and Metadata
- [ ] Patch filename uses `.patch.md`
- [ ] Patch metadata fields are complete
- [ ] Session metadata is real and not placeholder-based
- [ ] `Target Design` resolves to an existing design document or agreed target reference
- [ ] `Full history` link resolves correctly

### 9.2 Patch Authority Integrity
- [ ] Patch version aligns with its patch changelog version when a patch changelog exists
- [ ] Patch remains identifiable as the governed execution-plan artifact
- [ ] Patch does not rely on the helper template as an authority source
- [ ] Patch does not drift into acting like changelog or TODO authority

### 9.3 Structure and Reviewability
- [ ] Patch includes context, analysis, implementation plan, verification, and rollback coverage
- [ ] A reviewer can identify what is changing and why this patch exists
- [ ] A reviewer can identify the intended target design or target state
- [ ] The patch remains readable as a change/review artifact even when it includes phases

### 9.4 Synchronization Behavior
- [ ] Governance update order remains consistent when the patch participates in synchronized work
- [ ] Related design, runtime, changelog, and TODO references are not obviously stale
- [ ] Patch history references remain valid after synchronization

---

## 10) Integration Contract

- Design defines the target state.
- Patch defines the governed transition process and, when needed, the live phase-plan instance.
- `phase-implementation.md` defines phase semantics.
- Changelog records shipped or synchronized history.
- TODO tracks actionable execution items only.
- `phase-implementation-template.md` is a non-governed helper that may assist authoring but never replaces the patch as the authority instance.

Update order remains:
1. design
2. runtime
3. changelog
4. TODO
5. patch metadata final sync (if affected)

---

## 11) Quality Metrics

| Metric | Target |
|--------|--------|
| Patch metadata completeness | 100% |
| Active placeholder session markers in patch docs | 0 |
| Patch ↔ design version reference validity | 100% |
| Patch-role clarity | 100% |
| Patch-governance checklist boundary clarity vs phase-implementation | 100% |
| Phase semantic duplication in patch-control | 0 |
| Patch history link validity | 100% |

---

## 12) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | UDVC-1 version authority contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository-level document and helper role model |
| [phase-implementation.design.md](phase-implementation.design.md) | Semantic authority for phased execution planning |
| [../document-patch-control.md](../document-patch-control.md) | Runtime implementation |
| [../phase-implementation-template.md](../phase-implementation-template.md) | Non-governed root helper for authoring |

---

> Full history: [../changelog/document-patch-control.changelog.md](../changelog/document-patch-control.changelog.md)
