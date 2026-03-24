# Phase Implementation

> **Current Version:** 2.2
> **Design:** [design/phase-implementation.design.md](design/phase-implementation.design.md) v2.2
> **Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c
> **Full history:** [changelog/phase-implementation.changelog.md](changelog/phase-implementation.changelog.md)

---

## Rule Statement

**Core Principle: Use phased planning only when staged execution meaningfully improves clarity, and require phased work to use a dedicated `/phase` workspace with mandatory `SUMMARY.md` plus separate child per-phase files, while allowing phase to act as the live execution synthesis layer for relevant design and patch inputs rather than storing live phase plans under `/patches`.**

This rule defines the semantic standard for phase planning. The governed summary/index lives in `/phase/SUMMARY.md`, per-phase execution detail lives in `/phase/phase-001-*.md`, design remains target-state authority, patch remains governed change/review authority, and the root helper remains a non-governed drafting aid.

---

## Core Requirements

### 1) Purpose and Authority Boundary

`phase-implementation.md` defines:
- what phase planning is for
- when phased planning should and should not be used
- what `/phase` structure should look like
- what semantic fields a child phase file should contain
- how design references should be mapped into each phase
- how optional patch references may also be mapped into each phase when patch-derived work matters
- how cross-phase handoffs, verification, TODO coordination, changelog coordination, and rollback boundaries should be expressed
- how live phase planning may synthesize one-way source inputs from design and relevant patch artifacts without becoming a source-of-truth layer

It does **not** replace:
- `phase/SUMMARY.md` as the governed summary/index for the active phased execution plan
- child phase files as the governed phase-local execution detail
- `design/*.design.md` as target-state authority
- `patches/*.patch.md` as governed patch/review authority
- `TODO.md` as execution tracking
- `changelog/*.changelog.md` as history

### 2) When to Use Phase Planning

Use phased planning when one or more of these are true:
- work must happen in distinct stages with different entry and exit conditions
- rollout, migration, or verification gates matter between stages
- outputs from one stage are required by a later stage
- rollback or containment boundaries matter during execution
- the change spans multiple systems, files, or owners and benefits from staged coordination
- the project needs a governed plan that shows how design, TODO, and changelog move together during execution

### 3) When Not to Use Phase Planning

Do not force phases when:
- the work is a single obvious change
- a normal implementation plan or TODO checklist is enough
- the task is tiny and low-risk
- phases would only exist to satisfy template shape
- the plan would invent filler stages that add no execution meaning

### 4) Mandatory `/phase` File Model

When phased planning is used, the repository must use:
- `phase/SUMMARY.md`
- one separate child file per live phase

The default layout is:

```text
phase/
  SUMMARY.md
  phase-001-<phase-name>.md
  phase-002-<phase-name>.md
  phase-003-<phase-name>.md
```

Zero-padded contiguous numbering (`001`, `002`, `003`) is preferred so phase order stays human-readable and naturally sequential.

`SUMMARY.md` is mandatory.
Live phased execution files under `/patches` are **not allowed**.

### 4.1) Source-input synthesis boundary

`/phase` is the live execution synthesis layer, not a new source-of-truth layer.

Phase planning may consume:
- `design/*.design.md` as target-state inputs
- `patches/*.patch.md` as optional governed change/review inputs when patch-derived work matters

This direction is one-way:
- phase artifacts may cite and synthesize design and patch inputs
- design and patch artifacts are not required to point back to phase
- using patch input does not move live execution planning into `/patches`
- using design input does not turn phase into target-state authority

### 5) Flexible Order Contract

When phase planning is used, phases may be:
- merged
- split
- skipped
- repeated
- reordered

These are normal allowed behaviors.
There is no repository-wide mandatory `Phase 1 → Phase N` sequence.

### 6) `SUMMARY.md` Responsibilities

`phase/SUMMARY.md` should keep the global execution picture, including:
- overall context and target state
- analysis of risk, constraints, and dependencies
- a phase map or phase index
- references to child phase files
- summary-level source inputs from design and patch artifacts when relevant
- cross-phase handoffs and dependency rules
- overall TODO/changelog coordination when the concern is global
- end-to-end verification requirements
- overall rollback or containment behavior

`SUMMARY.md` should not become the place where all child phase detail is duplicated in full.

### 7) Summary Source-Input Extraction Table Requirement

`phase/SUMMARY.md` should include a source-input extraction summary table for the whole phase set.

The table should let a reviewer quickly see:
- which design source or section feeds which phase
- which patch source, if any, also feeds that phase
- what execution work is derived from those source inputs
- what target outcome each phase is expected to produce
- which phase file owns that execution detail

Recommended columns:
- Phase
- Phase File
- Design Source
- Patch Source
- Derived Execution Work
- Target Outcome

### 8) Summary Flow-Diagram Requirement

`phase/SUMMARY.md` should include a small overview flow diagram for the full phase set.

The summary diagram should show, as applicable:
- the relevant design source, patch source, or current-state baseline
- the major phase sequence or branching path
- what major capability, workflow, or governed state each phase changes
- the final target state produced by the combined phased execution

The goal is to let a reviewer understand the full phase story quickly before reading each child phase file.

The diagram must follow `flow-diagram-no-frame.md`:
- no boxes
- no frames
- no rectangle ASCII art
- use arrows / indentation only

### 8.1) Summary Review-Aggregate Requirement

`phase/SUMMARY.md` should include a review summary table for the whole phase set.

The review summary should let a reviewer or approver quickly see, per phase:
- sign-off status
- reviewer severity
- reviewer disposition
- current blocker or follow-up state

Recommended columns:
- Phase
- Phase File
- Sign-Off Status
- Reviewer Severity
- Reviewer Disposition
- Blocker / Follow-Up State

### 9) Stable Child Phase Field Contract

Each child phase file should define, or clearly map to:
- Summary File reference
- Phase ID / phase name
- Status
- Design references
- Patch references (optional when patch-derived work exists)
- Objective
- Why this phase exists
- Entry conditions / prerequisites
- Action points / execution checklist
- Out of scope
- Affected artifacts
- TODO coordination
- Changelog coordination
- Verification
- Exit criteria
- Risks / rollback notes
- Next possible phases

Equivalent headings are acceptable if the meaning stays explicit.

### 10) Source Traceability Contract

Each child phase file should make clear what source details it is executing.

Required source-input behavior:
- design references remain the primary target-state traceability input when relevant
- patch references may be added when patch-derived work materially affects the phase
- phase may synthesize both source types in the same child file when that improves execution clarity
- source references remain one-way inputs into phase rather than back-link obligations on design or patch documents

Use explicit references such as:
- design file path or name
- design section heading or anchor when available
- patch file path or name when patch-derived work exists
- patch section heading, anchor, or change-surface locator when relevant
- short note describing the exact source requirement or change surface being implemented, validated, or synchronized

A child phase file should never rely on a vague note like "follow the design" when the design contains multiple requirements.

### 11) Design-to-Phase Extraction Contract

Each child phase file should explicitly show **what is being pulled from the design into executable phase work**.

Required extraction signals:
- the specific design source section or requirement
- what behavior, contract, component, workflow, or governance rule is being derived from that source
- what this phase is enhancing, extending, migrating, validating, or replacing
- what target execution artifact or operational outcome is expected from that design input

This extraction mapping should be reviewable enough that a reviewer can answer:
- what design source was used
- what execution work was derived from it
- why that derived work belongs in this phase instead of another phase

### 11.1) Patch-to-Phase Extraction Contract

When patch-derived work exists, each child phase file should also show **what is being pulled from the patch into executable phase work**.

Required extraction signals:
- the source patch file and the relevant section, anchor, or change-surface locator
- the patch-defined change, review constraint, migration step, or implementation surface being operationalized in the phase
- what this phase is applying, validating, sequencing, or rolling out from that patch input
- what target execution artifact or operational outcome is expected from that patch input

This patch-to-phase mapping exists alongside the design-to-phase mapping.
It does not replace design traceability, and it does not turn the patch into the source of truth for the overall target state.

### 12) Flow-Diagram Requirement for Review

Each child phase file should include a small text flow diagram that explains the phase at review level.

The diagram should show, as applicable:
- what source design element, source patch element, or current-state component the phase starts from
- what enhancement, migration, implementation, validation, or rollout action occurs in this phase
- what target component, workflow, or operational state the phase produces or modifies
- what dependency or handoff connects this phase to the next relevant state

Use the diagram to make review faster, not decorative.
The diagram must follow `flow-diagram-no-frame.md`:
- no boxes
- no frames
- no rectangle ASCII art
- use arrows / indentation only

### 12.1) Reviewer Checklist Block Requirement

Each child phase file should include a small reviewer-oriented checklist block.

The reviewer checklist should make it easy to confirm:
- the cited design source is correct for this phase when design input is used
- the cited patch source is correct for this phase when patch input is used
- the derived execution work is justified by the cited source inputs
- the source → phase action → target outcome flow is clear
- the phase boundary is correct and the work belongs in this phase
- dependencies and handoffs are explicit enough for safe progression
- verification evidence is sufficient for review or sign-off

This block is for review readiness, not for replacing the execution checklist.

### 12.2) Review Outcome Contract

Each child phase file should use one standardized review outcome vocabulary.

#### Sign-off status vocabulary
Use these values for the sign-off decision field:
- `Pending Review`
- `Needs Revision`
- `Approved`
- `Approved With Follow-up`
- `Not Required`

#### Reviewer severity field
Use these values for reviewer issue severity when relevant:
- `Blocking`
- `Non-Blocking`
- `Follow-Up`
- `None`

#### Reviewer disposition field
Use these values for reviewer disposition when relevant:
- `Must Fix Before Approval`
- `May Proceed With Follow-Up`
- `Approved As-Is`
- `No Review Required`

The sign-off status, severity, and disposition should align so a reviewer can quickly understand whether work is blocked, approved, or approved with follow-up obligations.

### 13) Companion Tracking Model

When phased work exists:
- `phase/SUMMARY.md` should show global TODO and changelog coordination when multiple phases contribute to one execution milestone
- each child phase file should show what TODO work and changelog impact apply to that phase
- TODO remains execution tracking only
- changelog remains history only
- `SUMMARY.md` plus child phase files remain the live plan that explains how those companions relate to execution

### 14) Cross-Phase Coordination Contract

When multiple phases exist, make the following explicit when relevant:
- dependencies and handoffs between phases
- outputs required before later phases can start
- what source inputs are design-derived, patch-derived, or synthesized from both when that distinction affects sequencing
- verification gates that must pass before progressing
- work that can proceed in parallel
- rollback or containment boundaries before the next phase starts
- when TODO state should be updated
- when changelog impact should be recorded

### 15) Verification and Rollback Contract

Phased planning must preserve both local and global safety:
- each child phase file should define phase-level verification
- each child phase file should define local rollback or containment notes
- `phase/SUMMARY.md` must still define end-to-end verification
- `phase/SUMMARY.md` must still define overall rollback or containment behavior

Passing one phase does not mean the full plan is complete.

### 16) `/patches` Boundary

`/patches` is not the live phase-plan namespace.
If patch documents exist, they remain patch artifacts and must not be used as the location for live phased execution planning.

### 17) Checklist Boundary Contract

The `phase-implementation` checklist validates **phased execution-plan quality** only.

Validate here:
- phase necessity
- summary-versus-child structure quality
- source-input traceability across design and patch inputs when applicable
- TODO/changelog companion coordination
- execution control quality

Do not validate here:
- patch metadata completeness
- patch filename or path compliance
- patch history-link integrity
- patch review-artifact governance requirements

Those belong outside this rule and remain patch-governance concerns when patch docs exist.

---

## Phase Model

### 1) Phase semantics live here

This rule is the semantic authority for phase-planning behavior.

### 2) Live plan instances live in `/phase`

When a project needs an authoritative phased execution plan, the governed instance belongs in:
- `phase/SUMMARY.md` as the summary/index file
- `phase/phase-010-<phase-name>.md` and peers as child per-phase files

### 3) Helper guidance lives in the root template

`phase-implementation-template.md` is a reusable helper for drafting and readability.
It is not a governed chain and must not masquerade as one.

### 4) Common phase patterns are optional

Examples only:
- discovery / alignment
- design / decision lock
- implementation / change
- migration
- verification / test
- rollout / deploy
- cleanup / optimization

Use these only when they match project reality.

### 5) Companion tracking stays explicit

A good phase plan makes companion artifacts visible:
- `SUMMARY.md` is the authoritative execution summary/index
- the child phase file shows what TODO items or TODO transitions matter for that phase
- the child phase file shows what changelog event is expected later or upon completion

This preserves visibility without turning TODO or changelog into the primary phase-definition layer.

---

## Trigger Model

Apply this rule more strongly when one or more of these signals are present:

| Trigger | Typical Signal | Expected Shape |
|--------|-----------------|----------------|
| staged rollout | migration, deploy gate, cutover, reconciliation | `/phase/SUMMARY.md` plus explicit child phase files with handoffs and rollback boundaries |
| dependency chain | one stage produces outputs needed by another | summary phase map plus child phase entry/exit criteria |
| multi-system change | docs, runtime, install targets, services, or teams move together | phase-level affected artifacts and verification in child files |
| design-driven execution | different parts of the design must be implemented in sequence | explicit child phase-to-design mapping |
| governance execution | governed repository change with synchronized artifacts | summary shows global coordination, child files show phase-local detail |
| risk containment | partial failure needs local rollback before proceeding | child phase verification and rollback notes plus summary-level global rollback |

Do not trigger this rule just because a task is long. Trigger it when staged execution meaningfully changes how the work should be planned or controlled.

---

## Phase Validation Checklist

Use this checklist only when a plan actually uses phases.
It validates the quality of the phased execution plan itself.

### 1) Planning appropriateness
- [ ] Phased planning is justified by real staged execution needs
- [ ] The plan does not invent filler phases for symmetry only
- [ ] The chosen order reflects project reality rather than a fake global sequence

### 2) Summary/child structure quality
- [ ] The repository uses `/phase/` for live phased execution
- [ ] `phase/SUMMARY.md` exists and acts as the governing summary/index
- [ ] `SUMMARY.md` includes a source-input extraction summary table for the whole phase set
- [ ] `SUMMARY.md` can show design and patch inputs separately when both matter
- [ ] `SUMMARY.md` includes an overview flow diagram for the full phase set
- [ ] `SUMMARY.md` includes a review summary table for the whole phase set
- [ ] Each live phase has its own child phase file
- [ ] `SUMMARY.md` exposes a readable phase map or phase index
- [ ] Child files own phase-local execution detail
- [ ] Live phase planning is not stored under `/patches`

### 3) Source traceability
- [ ] Each child phase file cites the relevant design file or section when design input exists
- [ ] Each child phase file cites the relevant patch file or section when patch-derived work exists
- [ ] Source references are specific enough to show what requirement or change surface is being executed
- [ ] No child phase file relies on a vague "follow the design" statement alone
- [ ] Each child phase file explicitly maps what execution work was derived from the cited design source when design input exists
- [ ] Each child phase file explicitly maps what execution work was derived from the cited patch source when patch-derived work exists
- [ ] Each child phase file makes clear what existing part is being enhanced, developed, migrated, validated, applied, or replaced
- [ ] Each child phase file includes a review-friendly flow diagram showing source → phase action → target outcome
- [ ] Each child phase file includes a reviewer checklist block for source correctness, flow clarity, boundary correctness, dependency clarity, and evidence readiness
- [ ] Each child phase file uses standardized sign-off status values and aligned severity/disposition fields when review outcomes are recorded

### 4) Companion coordination
- [ ] Summary-level TODO/changelog coordination is explicit when global coordination matters
- [ ] Child-level TODO/changelog coordination is explicit when execution tracking is relevant
- [ ] TODO and changelog are treated as companion layers, not replacements for the phase plan

### 5) Execution control quality
- [ ] Dependencies and handoffs are explicit when later phases rely on earlier outputs
- [ ] Phase-level verification expectations are explicit in child files
- [ ] Rollback or containment notes exist where phase failure would matter
- [ ] End-to-end verification and overall rollback remain explicit in `SUMMARY.md`
- [ ] The next possible phase or next execution path is clear

---

## Good Patterns

### Pattern 1: Summary plus per-phase child files

```text
phase/
  SUMMARY.md
  phase-010-create-rule.md
  phase-020-realign-docs.md
  phase-030-verify-rollout.md
```

### Pattern 2: `SUMMARY.md` holds global control only

```markdown
## Phase map

| Phase | Status | File | Objective | Depends On |
|------|--------|------|-----------|------------|
| P1 | Completed | `phase/phase-010-<name>.md` | <objective> | none |
| P2 | In Progress | `phase/phase-020-<name>.md` | <objective> | P1 |
```

### Pattern 3: Child file shows design extraction and flow

```markdown
## Design extraction
- Source design: `design/example.design.md` → section 4.2 "Request validation"
- Derived execution work: implement validation middleware and verification gate
- Enhancement path: current route-level validation → centralized middleware validation
- Target outcome: shared validation layer before handler execution

## Flow diagram

Current request path
  → route-local validation
  → phase action: extract + centralize validation middleware
  → target request path with shared validation gate
```

### Pattern 4: Child file owns phase-local checklist

```markdown
## Action points
- [x] Update design chain
- [ ] Update runtime chain
- [ ] Record changelog synchronization

## Verification
- runtime/design/changelog versions align
- references resolve
```

### Pattern 5: Linear plan instead of phases

```markdown
This change is a one-file wording fix.
A normal implementation checklist is enough, so phased planning is not used.
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| fake global `Phase 1 → N` requirement | creates unnecessary ceremony and distorts project reality | choose only the phases the project actually needs |
| no `SUMMARY.md` file | removes the required control surface for the phase workspace | always create `phase/SUMMARY.md` when phased planning is used |
| storing live phase plans under `/patches` | keeps phase planning entangled with patch governance | keep live phased execution under `/phase/` |
| putting all phase-local detail only in `SUMMARY.md` | makes the summary heavy and hard to operate | keep global control in `SUMMARY.md` and per-phase detail in child files |
| child phase files without design references when design input exists | breaks traceability back to intended behavior | cite the relevant design sections |
| child phase files using patch-derived work without patch references | hides the governed change surface being operationalized | cite the relevant patch file and precise section or change locator |
| child phase files without status or action points | makes tracking weak and hard to execute | include status plus a clear checklist |
| verification only at the very end | hides phase-level failure boundaries | define verification gates in child files and keep end-to-end checks in `SUMMARY.md` |
| phases added for formatting symmetry | adds noise without control value | use a linear plan if stages are not real |

---

## Completion Boundary and Stop Rule

### Definition of Done

Treat the phase-planning model as complete when all of the following are true:
- `/phase` is the live namespace
- `phase/SUMMARY.md` contains the required summary-level structures
- child phase files contain the required design, review, and execution structures
- review outcome vocabulary is standardized across child phases
- rule/design/changelog/template/TODO synchronization is complete

### Stop rule after completion

After the model reaches the definition of done above:
- do not keep adding new mandatory capability blocks by default
- do not keep expanding the model unless the user explicitly requests a new capability
- further changes should be limited to:
  - bug fixes
  - wording clarifications
  - inconsistency corrections
  - broken reference/version repairs
  - explicit user-requested scope changes

This stop rule exists to prevent endless governance expansion after the phase-planning model is already operationally complete.

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Appropriate use of phase planning | High |
| `/phase` workspace compliance | 100% |
| `SUMMARY.md` presence when phased planning is used | 100% |
| Stable per-phase field clarity | High |
| Design traceability coverage | 100% when design input is used |
| Patch traceability coverage | 100% when patch-derived work is used |
| One-way source-input boundary clarity | 100% |
| TODO/changelog companion visibility | High |
| Cross-phase handoff clarity | High |
| Phase-level verification visibility | 100% when phases are used |
| Checklist boundary clarity vs patch-control | 100% |
| Live phased execution files under `/patches` | 0 |
| Helper-versus-authority confusion | 0 |
| Unrequested post-completion capability expansion | 0 |

---

## Integration

Related rules:
- [document-patch-control.md](document-patch-control.md) - patch governance boundary outside live phase planning and one-way synthesis clarification for patch inputs
- [project-documentation-standards.md](project-documentation-standards.md) - repository role model for `/phase`, helper, TODO, changelog, and one-way design/patch source synthesis
- [todo-standards.md](todo-standards.md) - keeps TODO as execution tracking only
- [strict-file-hygiene.md](strict-file-hygiene.md) - avoids unneeded duplicate planning artifacts

---
