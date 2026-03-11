# Document Patch Control

## 0) Document Control

> **Parent Scope:** Project Documentation Standards
> **Current Version:** 1.9
> **Session:** 92fed037-8ba9-48a6-95c4-e1085f28bb32 (2026-03-11)

---

## 1) Goal

Standardize patch-document governance under the same UDVC-1 metadata and version-trace contract used by other governed document chains, while making the boundary explicit that live phased execution planning belongs in `/phase`, not in `/patches`.

When phased execution planning is used, semantic phase behavior should come from `phase-implementation.md`, while this chain keeps `/patches` limited to patch-document governance outside the live phase-plan namespace.

---

## 2) Scope

Applies to:
- `patches/*.patch.md`
- patch lifecycle documentation
- patch metadata traceability and history references
- governed patch execution/review artifacts that are not the live `/phase` plan workspace

The root helper `phase-implementation-template.md` may help authors draft a plan, but it is not itself a governed chain.

---

## 3) Naming and Location

### 3.1 Patch naming

- Patch document filename: `<context>.patch.md`
- Preferred location: `patches/`
- Do not use version suffixes in filenames

### 3.2 `/phase` separation

Live phased execution planning does not belong in `/patches`.
The dedicated live phase-plan workspace is:

```text
phase/
  SUMMARY.md
  phase-010-<phase-name>.md
  phase-020-<phase-name>.md
```

### 3.3 Helper placement

- The canonical reusable helper for this repository is the root-level `phase-implementation-template.md`
- Root-level helper placement improves discoverability, but helper placement does not change chain authority

---

## 4) Mandatory Metadata

### 4.1 Patch metadata

Each patch document must include:
- `Current Version`
- `Session`
- `Status`
- `Target Design`
- `Full history` link

### 4.2 Patch changelog metadata

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

Patch documents may reference phased execution work, but the live phase summary/index and per-phase execution detail must remain in `/phase`.

---

## 6) Patch-versus-Phase Boundary

### 6.1 Patch role

`/patches` owns governed patch artifacts.
It remains appropriate for:
- tactical migration/review plans
- governed change artifacts
- patch-specific transition analysis
- metadata-governed execution/review documents that are not the live phase workspace

### 6.2 Phase role

`/phase` owns live phased execution planning.
It contains:
- `phase/SUMMARY.md` as the governed summary/index
- `phase/phase-010-*.md` and peers as child phase-detail files

### 6.3 Prohibited blending

The following are not allowed:
- using `/patches` as the live phase-plan namespace
- storing the active phase summary/index in a patch file instead of `phase/SUMMARY.md`
- storing live per-phase execution files under `/patches`

### 6.4 Semantic authority

If phased execution exists, it should follow `phase-implementation.md` for:
- when phase planning is appropriate
- the required `/phase` structure
- stable per-phase fields
- design traceability
- status and action-point expectations
- TODO/changelog coordination inside the plan
- cross-phase handoffs
- verification and rollback boundaries

### 6.5 What this chain owns

`document-patch-control` owns:
- patch metadata rules
- patch filename and location rules
- patch lifecycle and synchronization behavior
- patch checklist expectations for governed review/change artifacts
- the boundary that keeps live phased execution out of `/patches`

It does **not** serve as the primary semantic authority for phased execution behavior.

---

## 7) Version and Session Integrity

- Patch active metadata must not contain placeholder sessions.
- If patch version is updated, corresponding patch changelog metadata must be synchronized.
- Target design version references must be resolvable and current.

---

## 8) Patch Checklist Boundary

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
- per-phase design-traceability quality
- per-phase execution-step quality
- `SUMMARY.md` content quality

Those remain the responsibility of `phase-implementation` when phased planning is used.

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
- [ ] Patch remains identifiable as a governed patch artifact
- [ ] The patch does not rely on the helper template as an authority source
- [ ] The patch does not drift into acting like changelog or TODO authority
- [ ] The patch does not masquerade as the live `/phase` summary/index or phase-detail layer

### 9.3 Structure and Reviewability
- [ ] Patch includes context, analysis, implementation plan, verification, and rollback coverage
- [ ] A reviewer can identify what is changing and why this patch exists
- [ ] A reviewer can identify the intended target design or target state
- [ ] The patch remains readable as a change/review artifact because live phase detail is kept outside `/patches`

### 9.4 Synchronization Behavior
- [ ] Governance update order remains consistent when the patch participates in synchronized work
- [ ] Related design, runtime, changelog, TODO, and `/phase` references are not obviously stale
- [ ] Patch history references remain valid after synchronization

---

## 10) Integration Contract

- Design defines the target state.
- Patch defines governed patch/review behavior outside the live phase workspace.
- `/phase` defines the live phased execution workspace.
- `phase-implementation.md` defines phase semantics.
- Changelog records shipped or synchronized history.
- TODO tracks actionable execution items only.
- `phase-implementation-template.md` is a non-governed helper that may assist authoring but never replaces the live `/phase` workspace.

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
| Patch-role clarity | 100% |
| Patch-versus-phase namespace separation clarity | 100% |
| Active placeholder session markers in patch docs | 0 |
| Patch ↔ design version reference validity | 100% |
| Patch-governance checklist boundary clarity vs phase-implementation | 100% |
| Live phased execution files under `/patches` | 0 |
| Patch history link validity | 100% |

---

## 12) Related Documents

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.design.md](document-changelog-control.design.md) | UDVC-1 version authority contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository-level document and helper role model |
| [phase-implementation.design.md](phase-implementation.design.md) | Semantic authority for phased execution under `/phase` |
| [../document-patch-control.md](../document-patch-control.md) | Runtime implementation |
| [../phase-implementation-template.md](../phase-implementation-template.md) | Non-governed root helper for authoring |

---

> Full history: [../changelog/document-patch-control.changelog.md](../changelog/document-patch-control.changelog.md)
