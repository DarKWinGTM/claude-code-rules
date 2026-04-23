# Document Patch Control

## 0) Document Control

> **Parent Scope:** Project Documentation Standards
> **Current Version:** 2.5
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-08)

---

## 1) Goal

Standardize governed patch-document behavior under the same UDVC-1 metadata and version-trace contract used by other governed document chains, while making the patch concept explicit: a patch exists to show the exact intended before/after change surface for review.

This chain must keep live phased execution planning in `/phase`, not in patch artifacts.

---

## 2) Scope

Applies to:
- `patch/<context>.patch.md`
- root-level `<context>.patch.md`
- patch lifecycle documentation
- patch metadata traceability and history references
- governed patch execution/review artifacts that are not the live `/phase` plan workspace
- patch documents describing code, configuration, schema, query, command, policy-text, or structured document changes

The root helper `phase-implementation-template.md` may help authors draft a plan, but it is not itself a governed chain.

---

## 3) Patch Meaning and Location

### 3.1 Patch definition
A patch is a governed change artifact whose purpose is to show **what will be changed** clearly enough for review before or during controlled execution.

A valid patch must make it easy for a reviewer to answer:
- what artifact changes
- where it changes
- what exists now
- what it should become after the change
- whether the change is additive, replacement, deletion, or restructuring

The chain must explicitly reject these misreadings:
- patch as retrospective summary
- patch as phase summary/index
- patch as prose-only recap with no explicit change surface
- patch as generic plan text that leaves before/after state implicit
- patch as the default startup artifact for greenfield / baseline-formation work when no stable before-state exists yet

A patch normally assumes an identifiable current/before surface.
For greenfield startup, first-time scaffolding, baseline formation, or first-pass terminology/contract establishment, patch is usually not the default governing artifact unless the user explicitly asks for it or a real pre-existing review surface already exists.

### 3.2 Allowed locations
Governed patch files must use a self-identifying `<context>.patch.md` filename and may live in one of these places:
- shared patch directory: `patch/<context>.patch.md`
- repository root: `<context>.patch.md`

Required location rules:
- `patch/` is the default shared patch directory for this repository
- root-level placement is allowed when the patch should live directly at repository top level
- generic `patch.md` is not allowed
- version suffixes in patch filenames are not allowed

### 3.3 `/phase` separation
Live phased execution planning does not belong in `/patch` or in root-level patch files.

The dedicated live phase-plan workspace is:

```text
phase/
  SUMMARY.md
  phase-001-<phase-name>.md
  phase-001-01-<subphase-name>.md
```

### 3.4 Helper placement
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
1. Context
2. Analysis
3. Change items
4. Verification
5. Rollback approach

Optional implementation order is allowed when sequencing matters, but it does not replace the required change items.

### 5.1 Change-item requirement
For each concrete change item, the patch must show:
- target artifact or stable target location
- change type (`additive`, `replacement`, `deletion`, or `restructuring`)
- current/before state
- target/after state
- enough comparison detail for a reviewer to understand the exact change surface

### 5.2 Preferred comparison forms
Use one or more of these forms when applicable:
- before/after snippets
- current/target comparison tables
- unified diff style blocks
- patch hunk sections with explicit target file/path and relevant anchors
- clearly scoped command/config replacement blocks

The rule is semantic, not tied to one markdown shape. The comparison must be concrete enough for review.

### 5.3 Target-location requirement
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

### 5.4 Non-code patch allowance
Not every patch is a code diff.
When a patch is conceptual, governance-only, or architecture-only, it may use structured before/after comparison without code snippets.

In that case the patch must say clearly that:
- it is a non-code patch or non-snippet patch
- the change surface is conceptual / governance / structural
- concrete runtime edits are intentionally out of scope for that patch

### 5.5 Patch specificity principle
A patch should be specific enough that a reviewer can answer:
- what artifact changes
- where it changes
- what the current state is
- what the proposed state is
- how the before/after comparison maps to the intended modification

If the reviewer cannot answer those questions, the patch is under-specified.

### 5.6 External-requirement basis rule
When a change is materially constrained by external documentation, API specifications, provider references, or comparable external implementation authorities, the patch should make the implementation-relevant basis visible clearly enough that a reviewer can tell why the change surface exists.

Required guidance:
- patch should point to the normalized design truth when design already owns the extracted external requirement
- patch may summarize the change-driving external requirement, but it should not replace design as the target-state truth layer
- when external requirements materially determine request parameters, authentication behavior, callback handling, acceptance criteria, field semantics, or comparable integration constraints, the patch context/analysis should make that basis legible enough for review
- do not rely on transient doc-reading memory alone to explain a later change-driving external constraint in review

---

## 6) Patch-versus-Phase Boundary

### 6.1 Patch role
Patch artifacts exist to hold governed change/review information outside live phase planning.

They remain appropriate for:
- tactical change artifacts
- governed review artifacts
- patch-specific transition analysis
- reviewable current→target documentation that is outside the live phase workspace

They are not appropriate for:
- retrospective summary documents
- general progress recaps
- the active phase summary/index
- live per-phase execution files

### 6.2 Phase role
`/phase` owns live phased execution planning.
It contains:
- `phase/SUMMARY.md` as the governed summary/index
- `phase/phase-001-*.md` and peers as child phase-detail files

### 6.3 Prohibited blending
The following are not allowed:
- using `/patch` as the live phase-plan namespace
- storing the active phase summary/index in a patch file instead of `phase/SUMMARY.md`
- storing live per-phase execution files in patch artifacts

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
- patch usage inside phase does not move live execution planning into patch artifacts

### 6.5 What this chain owns
`document-patch-control` owns:
- patch metadata rules
- patch filename and location rules
- the definition of patch as a before/after change artifact
- patch lifecycle and synchronization behavior
- patch checklist expectations for governed review/change artifacts
- patch change-representation and reviewability expectations
- the boundary that keeps live phased execution out of patch artifacts

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
- patch change-representation quality
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
- [ ] Patch path uses an allowed location model (`patch/<context>.patch.md` or root `<context>.patch.md`)
- [ ] Patch filename is self-identifying and uses `<context>.patch.md`
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
- [ ] Patch includes context, analysis, change items, verification, and rollback approach
- [ ] A reviewer can identify what is changing and why this patch exists
- [ ] A reviewer can identify the intended target design or target state
- [ ] The patch remains readable as a governed change/review artifact because live phase detail is kept outside patch artifacts

### 4) Change Representation
- [ ] Patch identifies the target artifact or stable target location for each concrete change item
- [ ] Patch shows before/current state and after/target state in a comparison-friendly form for each structured change item
- [ ] Patch makes clear whether each change is additive, replacement, deletion, or restructuring
- [ ] If exact code/snippet comparison is intentionally not present, the patch explicitly declares itself non-code/conceptual and still provides structured before/after comparison
- [ ] A reviewer can understand how the change would be applied without having to guess the change surface

### 5) Synchronization Behavior
- [ ] Governance update order remains consistent when the patch participates in synchronized work
- [ ] Related design, runtime, changelog, TODO, and `/phase` references are not obviously stale
- [ ] Patch history references remain valid after synchronization
- [ ] The patch remains self-identifying outside its directory context

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Patch metadata completeness | 100% |
| Patch placement clarity | 100% |
| Patch concept clarity | 100% |
| Active placeholder session markers | 0 |
| Patch ↔ changelog version alignment | 100% |
| Patch ↔ target design reference validity | 100% |
| Patch-role clarity | 100% |
| Patch change-representation clarity | 100% |
| Patch target-location clarity | 100% |
| Patch-versus-phase namespace separation clarity | 100% |
| Patch-governance checklist boundary clarity vs phase-implementation | 100% |
| Live phased execution files under patch artifacts | 0 |
| Broken patch history links | 0 |

---

## Integration

| Rule | Relationship |
|------|-------------|
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority contract |
| [project-documentation-standards.md](project-documentation-standards.md) v2.8 | Project-level documentation role model |
| [phase-implementation.md](phase-implementation.md) v2.5 | Semantic authority for phased execution planning |
| [todo-standards.md](todo-standards.md) v2.2 | TODO structure standards |

---

> Full history: [../changelog/document-patch-control.changelog.md](../changelog/document-patch-control.changelog.md)
