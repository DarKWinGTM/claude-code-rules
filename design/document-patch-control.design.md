# Document Patch Control

## 0) Document Control

> **Parent Scope:** Project Documentation Standards
> **Current Version:** 2.2
> **Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c (2026-03-15)

---

## 1) Goal

Standardize patch-document governance under the same UDVC-1 metadata and version-trace contract used by other governed document chains, while making the boundary explicit that live phased execution planning belongs in `/phase`, not in `/patches`.

When phased execution planning is used, semantic phase behavior should come from `phase-implementation.md`, while this chain keeps `/patches` limited to governed patch/review artifacts outside the live phase-plan namespace.

This chain also defines what makes a patch **reviewable as a patch** rather than a vague plan: a governed patch should let a reviewer see what artifact is changing, where it changes, what the current state is, what the target state is, and how the change is intended to be applied.

---

## 2) Scope

Applies to:
- `patches/*.patch.md`
- patch lifecycle documentation
- patch metadata traceability and history references
- governed patch execution/review artifacts that are not the live `/phase` plan workspace
- patch documents describing code, configuration, schema, query, command, policy-text, or structured document changes

The root helper `phase-implementation-template.md` may help authors draft a plan, but it is not itself a governed chain.

---

## 3) Naming and Location

### 3.1 Patch naming

Patch naming should distinguish between **filename-authoritative naming** and **path-authoritative naming**.

#### Filename-authoritative naming
Use `<context>.patch.md` when the filename itself needs to carry the stable identifying context.

Typical cases:
- the file may be reviewed outside its parent directory context
- multiple patch artifacts may coexist in the same directory
- search/discovery ergonomics materially benefit from a self-identifying filename

Examples:
- `patches/issue-276.patch.md`
- `patches/runtime-routing-hardening.patch.md`

#### Path-authoritative naming
Use `patch.md` when the parent workspace path already provides the stable unique context and only one patch artifact of that role exists in the directory.

Typical cases:
- issue-local workspaces such as `issue/276/`
- feature-local workspaces such as `feature/tool-routing/`
- migration-local workspaces where the directory itself is the namespace

Examples:
- `issue/276/patch.md`
- `feature/tool-routing/patch.md`

#### Anti-redundancy principle
Avoid repeating the same context in both parent path and filename unless the repetition provides a real portability, review, or search benefit.

Additional naming rules:
- Preferred shared patch directory remains `patches/`
- Do not use version suffixes in filenames
- If generic `patch.md` naming is used, the parent path should clearly act as the namespace

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

### 5.1 Change-Representation Requirement
A governed patch must be reviewable as an actual intended change, not only as prose.

When the patch concerns code, configuration, command, query, schema, or other structured text changes, the patch should include a concrete change representation that lets a reviewer compare current state to target state.

Required review signals:
- target artifact or target location
- what currently exists there
- what is intended to replace, augment, or remove it
- enough comparison detail for a reviewer to understand the exact change surface

### 5.2 Preferred Comparison Forms
Use one or more of these forms when applicable:
- before/after snippets
- current/target comparison tables
- unified diff style blocks
- patch hunk sections with explicit target file/path and relevant anchors
- clearly scoped command/config replacement blocks

The rule is semantic, not tied to one markdown shape. The comparison must be concrete enough for review.

### 5.3 Target-Location Requirement
For each concrete change item, the patch should identify where the change applies.

Examples:
- file path
- section heading or anchor
- function/class/query name
- config key path
- route/endpoint name
- command block label
- schema object/table/column reference

If exact line numbers are not stable or not yet known, the patch should still use the most precise stable locator available.

### 5.4 Non-Code Patch Allowance
Not every patch is a code diff.
When a patch is conceptual, governance-only, or architecture-only, it may use structured current-state vs target-state comparison without code snippets.

In that case the patch must say clearly that:
- it is a non-code patch or non-snippet patch
- the change surface is conceptual / governance / structural
- concrete runtime edits are intentionally out of scope for that patch

A non-code patch must still provide comparison-friendly current-state vs target-state detail.

### 5.5 Patch Specificity Principle
A patch should be specific enough that a reviewer can answer:
- what artifact changes
- where it changes
- what the current state is
- what the proposed state is
- whether the patch is additive, replacement, deletion, or restructuring

If the reviewer cannot answer those questions, the patch is under-specified.

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
- optional patch-input synthesis inside the live phase plan when patch-derived work matters
- status and action-point expectations
- TODO/changelog coordination inside the plan
- cross-phase handoffs
- verification and rollback boundaries

### 6.4.1 One-way synthesis clarification
`phase-implementation.md` may synthesize governed patch inputs into live phased execution planning when relevant.

This does not create a reverse-link requirement:
- patch documents may remain complete patch artifacts without pointing back to phase
- design documents may remain target-state artifacts without pointing back to phase
- patch usage inside phase does not move live execution planning into `/patches`

### 6.5 What this chain owns
`document-patch-control` owns:
- patch metadata rules
- patch filename and location rules
- patch lifecycle and synchronization behavior
- patch checklist expectations for governed review/change artifacts
- patch change-representation and reviewability expectations
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
- change-representation quality
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
- [ ] Chosen naming mode is justified (`<context>.patch.md` when filename must carry context, `patch.md` when parent path is the namespace)
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

### 9.4 Change Representation
- [ ] Patch identifies the target artifact or stable target location for each concrete change item
- [ ] Patch shows current state vs proposed state in a comparison-friendly form when the patch concerns structured text/code/config changes
- [ ] Patch makes clear whether each change is additive, replacement, deletion, or restructuring
- [ ] If exact code/snippet comparison is intentionally not present, the patch explicitly declares itself non-code/conceptual and still provides structured current-state vs target-state comparison
- [ ] A reviewer can understand how the change would be applied without having to guess the change surface

### 9.5 Synchronization Behavior
- [ ] Governance update order remains consistent when the patch participates in synchronized work
- [ ] Related design, runtime, changelog, TODO, and `/phase` references are not obviously stale
- [ ] Patch history references remain valid after synchronization
- [ ] Redundant path + filename repetition is avoided unless it has a clear portability or review benefit

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
| Patch naming-mode clarity | 100% |
| Patch-role clarity | 100% |
| Patch change-representation clarity | 100% |
| Patch target-location clarity | 100% |
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
