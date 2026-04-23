# Document Patch Control

> **Current Version:** 2.5
> **Design:** [design/document-patch-control.design.md](design/document-patch-control.design.md) v2.5
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)

---

## Rule Statement

**Core Principle: Patch documents are governed patch/review artifacts outside the live `/phase` workspace, and a patch means a self-identifying before/after change artifact that shows the exact intended modification surface clearly enough for review.**

Patch docs remain the canonical place for governed patch artifacts. Changelog remains the version authority, and TODO remains execution-only tracking.

---

## Core Requirements

### 1) Patch Meaning and Location

#### 1.1 What a patch means
A patch is a governed change artifact whose job is to show **what will change** before or during reviewable execution.

A valid patch must make it easy for a reviewer to answer:
- what artifact changes
- where it changes
- what exists now
- what it should become after the change
- whether the change is additive, replacement, deletion, or restructuring

A patch is **not**:
- a retrospective summary of what already happened
- a phase summary or rollout dashboard
- a prose-only recap with no explicit change surface
- a generic plan that leaves the reviewer guessing the actual before/after delta

#### 1.2 Allowed patch locations
Governed patch files must use a self-identifying `<context>.patch.md` filename and may live in one of these places:
- shared patch directory: `patch/<context>.patch.md`
- repository root: `<context>.patch.md`

Additional rules:
- `patch/` is the default shared patch directory for this repository
- root-level placement is allowed when the patch should live directly at repository top level
- generic `patch.md` is **not allowed**
- do not use version suffixes in patch filenames

#### 1.3 `/phase` separation
Live phased execution planning does not belong in `/patch` or in root-level `*.patch.md` files.
The dedicated live phase-plan workspace is:

```text
phase/
  SUMMARY.md
  phase-001-<phase-name>.md
  phase-001-01-<subphase-name>.md
```

#### 1.4 Helper placement
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

### 3) Patch Structure Baseline

Every governed patch document must include, at minimum:
1. Context
2. Analysis
3. Change items
4. Verification
5. Rollback approach

Optional implementation order is allowed when sequencing matters, but it does not replace the required change items.

### 3.1 Change-item requirement
For each concrete change item, the patch must show:
- target artifact or stable target location
- change type (`additive`, `replacement`, `deletion`, or `restructuring`)
- current/before state
- target/after state
- enough comparison detail for a reviewer to understand the exact change surface

### 3.2 Preferred comparison forms
Use one or more of these forms when applicable:
- before/after snippets
- current/target comparison tables
- unified diff style blocks
- patch hunk sections with explicit target file/path and anchors
- clearly scoped command/config replacement blocks

The rule is semantic rather than tied to one markdown layout. The comparison must be concrete enough for review.

### 3.3 Target-location requirement
For each concrete change item, the patch should identify a stable target location.

Acceptable locators include:
- file path
- section heading or anchor
- function/class/query name
- config key path
- route/endpoint name
- command block label
- schema object/table/column reference

If exact line numbers are unstable or not yet known, use the most precise stable locator available.

### 3.4 Non-code patch allowance
Not every patch is a code diff.
When a patch is conceptual, governance-only, or architecture-only, it may omit code snippets **only if** it says so explicitly and still provides structured before/after comparison.

In that case the patch must say clearly that:
- it is a non-code patch or non-snippet patch
- the change surface is conceptual / governance / structural
- concrete runtime edits are intentionally out of scope for that patch

### 3.5 Patch specificity principle
A patch should be specific enough that a reviewer can answer:
- what artifact changes
- where it changes
- what the current state is
- what the proposed state is
- how the before/after comparison maps to the intended modification

If those questions cannot be answered from the patch, the patch is under-specified.

### 3.6 External-requirement basis rule
When a change is materially constrained by external documentation, API specifications, provider references, or comparable external implementation authorities, the patch should make the implementation-relevant basis visible clearly enough that a reviewer can tell why the change surface exists.

Required guidance:
- patch should point to the normalized design truth when design already owns the extracted external requirement
- patch may summarize the change-driving external requirement, but it should not replace design as the target-state truth layer
- when external requirements materially determine request parameters, authentication behavior, callback handling, acceptance criteria, field semantics, or comparable integration constraints, the patch context/analysis should make that basis legible enough for review
- do not rely on transient doc-reading memory alone to explain a change-driving external constraint in later review passes

### 4) Patch-versus-Phase Authority Split

#### 4.1 Patch role
When patch documents are used, they remain governed patch/review artifacts.

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

#### 4.2 Phase role
The live phased execution workspace is `/phase`.

It contains:
- `phase/SUMMARY.md` as the governed summary/index
- `phase/phase-001-*.md` and peers as child phase-detail files

#### 4.3 Prohibited blending
The following are not allowed:
- using `/patch` as the live phase-plan namespace
- storing the active phase summary/index in a patch file instead of `phase/SUMMARY.md`
- storing live per-phase execution files in patch artifacts

#### 4.4 Semantic authority
If phased execution exists, it should follow `phase-implementation.md` for:
- when phase planning should be used versus not used
- the required `/phase` structure
- stable phase fields
- design references per phase
- optional patch-input synthesis inside the live phase plan when patch-derived work matters
- status and action-point expectations
- TODO coordination and changelog coordination
- cross-phase handoffs
- verification and rollback boundaries

#### 4.4.1 One-way synthesis clarification
`phase-implementation.md` may synthesize governed patch inputs into live phased execution planning when relevant.

This does not create a reverse-link requirement:
- patch documents may remain complete patch artifacts without pointing back to phase
- design documents may remain target-state artifacts without pointing back to phase
- patch usage inside phase does not move live execution planning into patch artifacts

#### 4.5 What this chain owns
`document-patch-control.md` owns patch governance and metadata.
It also owns:
- the definition of patch as a before/after change artifact
- the patch filename and location rules
- the requirement that governed patch docs represent intended change surfaces concretely enough for review
- the boundary that keeps live phased execution out of patch artifacts

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

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority and metadata contract |
| [project-documentation-standards.md](project-documentation-standards.md) v2.14 | Project-level document governance and role boundary model |
| [phase-implementation.md](phase-implementation.md) v2.7 | Semantic authority for phased execution planning |
| [todo-standards.md](todo-standards.md) v2.3 | Execution tracking alignment |
| [phase-implementation-template.md](phase-implementation-template.md) | Non-governed root helper for authoring |

---

> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)
