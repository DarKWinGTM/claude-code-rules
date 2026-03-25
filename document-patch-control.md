# Document Patch Control

> **Current Version:** 2.2
> **Design:** [design/document-patch-control.design.md](design/document-patch-control.design.md) v2.2
> **Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c
> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)

---

## Rule Statement

**Core Principle: Patch documents are governed patch/review artifacts outside the live `/phase` workspace, and when they describe concrete changes they must show the change surface clearly enough for review through explicit target locations and comparison-friendly current-vs-target representation.**

Patch docs remain the canonical place for governed patch artifacts. Changelog remains the version authority, and TODO remains execution-only tracking.

---

## Core Requirements

### 1) Naming and Location

#### 1.1 Patch naming
Patch naming should distinguish between **filename-authoritative naming** and **path-authoritative naming**.

**Filename-authoritative naming**
- Use `<context>.patch.md` when the filename itself needs to carry the stable identifying context
- Typical cases:
  - the file may be reviewed outside its parent directory context
  - multiple patch artifacts may coexist in the same directory
  - search/discovery ergonomics materially benefit from a self-identifying filename
- Examples:
  - `patches/issue-276.patch.md`
  - `patches/runtime-routing-hardening.patch.md`

**Path-authoritative naming**
- Use `patch.md` when the parent workspace path already provides the stable unique context and only one patch artifact of that role exists in the directory
- Typical cases:
  - issue-local workspaces such as `issue/276/`
  - feature-local workspaces such as `feature/tool-routing/`
  - migration-local workspaces where the directory itself is the namespace
- Examples:
  - `issue/276/patch.md`
  - `feature/tool-routing/patch.md`

**Anti-redundancy principle**
- Avoid repeating the same context in both parent path and filename unless the repetition provides a real portability, review, or search benefit

Additional naming rules:
- Recommended shared patch directory remains `patches/`
- Do not use version suffixes in filenames
- If generic `patch.md` naming is used, the parent path should clearly act as the namespace

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

### 3.1 Change-Representation Requirement
A governed patch must be reviewable as an actual intended change, not only as prose.

When the patch concerns code, configuration, commands, queries, schemas, structured documents, or other concrete structured text changes, the patch must show the change surface in a comparison-friendly way.

At minimum, a reviewer should be able to see:
- what artifact or location is affected
- what currently exists there
- what is intended to replace, augment, remove, or restructure it

### 3.2 Preferred Comparison Forms
Use one or more of these forms when applicable:
- before/after snippets
- current/target comparison tables
- unified diff style blocks
- patch hunk sections with explicit target file/path and anchors
- clearly scoped command/config replacement blocks

The rule is semantic rather than tied to one markdown layout. The comparison just needs to be concrete enough for review.

### 3.3 Target-Location Requirement
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

### 3.4 Non-Code Patch Allowance
Not every patch is a code diff.
When a patch is conceptual, governance-only, or architecture-only, it may omit code snippets **only if** it says so explicitly and still provides structured current-state vs target-state comparison.

In that case the patch must say clearly that:
- it is a non-code patch or non-snippet patch
- the change surface is conceptual / governance / structural
- concrete runtime edits are intentionally out of scope for that patch

### 3.5 Patch Specificity Principle
A patch should be specific enough that a reviewer can answer:
- what artifact changes
- where it changes
- what the current state is
- what the proposed state is
- whether the patch is additive, replacement, deletion, or restructuring

If those questions cannot be answered from the patch, the patch is under-specified.

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
- patch usage inside phase does not move live execution planning into `/patches`

#### 4.5 What this chain owns
`document-patch-control.md` owns patch governance and metadata.
It also owns the boundary that keeps live phased execution out of `/patches`.
It also owns the requirement that governed patch docs represent the intended change concretely enough for review.

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
- [ ] Filename uses `.patch.md` format
- [ ] Chosen naming mode is justified (`<context>.patch.md` when filename must carry context, `patch.md` when parent path is the namespace)
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

### 4) Change Representation
- [ ] Patch identifies the target artifact or stable target location for each concrete change item
- [ ] Patch shows current state vs proposed state in a comparison-friendly form when the patch concerns structured text/code/config changes
- [ ] Patch makes clear whether each change is additive, replacement, deletion, or restructuring
- [ ] If exact code/snippet comparison is intentionally not present, the patch explicitly declares itself non-code/conceptual and still provides structured current-state vs target-state comparison
- [ ] A reviewer can understand how the change would be applied without having to guess the change surface

### 5) Synchronization Behavior
- [ ] Governance update order remains consistent when the patch participates in synchronized work
- [ ] Related design, runtime, changelog, TODO, and `/phase` references are not obviously stale
- [ ] Patch history references remain valid after synchronization
- [ ] Redundant path + filename repetition is avoided unless it has a clear portability or review benefit

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Patch metadata completeness | 100% |
| Patch naming-mode clarity | 100% |
| Active placeholder session markers | 0 |
| Patch ↔ changelog version alignment | 100% |
| Patch ↔ target design reference validity | 100% |
| Patch-role clarity | 100% |
| Patch change-representation clarity | 100% |
| Patch target-location clarity | 100% |
| Patch-versus-phase namespace separation clarity | 100% |
| Patch-governance checklist boundary clarity vs phase-implementation | 100% |
| Live phased execution files under `/patches` | 0 |
| Broken patch history links | 0 |

---

## Integration

| Document | Relationship |
|----------|--------------|
| [document-changelog-control.md](document-changelog-control.md) v4.7 | Version authority and metadata contract |
| [project-documentation-standards.md](project-documentation-standards.md) v2.4 | Project-level document governance and role boundary model |
| [phase-implementation.md](phase-implementation.md) v2.1 | Semantic authority for phased execution planning |
| [todo-standards.md](todo-standards.md) v2.2 | Execution tracking alignment |
| [phase-implementation-template.md](phase-implementation-template.md) | Non-governed root helper for authoring |

---

> **Full history:** [changelog/document-patch-control.changelog.md](changelog/document-patch-control.changelog.md)
