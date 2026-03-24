# Phase Implementation

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.2
> **Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c (2026-03-17)

---

## 1) Goal

Define one first-class rule chain for phased implementation planning so phased work uses a dedicated `/phase` workspace with a mandatory `SUMMARY.md` file and separate per-phase files, while treating phase as the live execution synthesis layer that may pull from design target-state inputs and relevant patch/review inputs without storing live phase plans under `/patches`.

The target state separates these concerns clearly:
- `phase-implementation.md` defines phase-planning semantics and one-way source-input synthesis
- `phase/SUMMARY.md` is the governed summary/index for the active phased execution plan
- `phase/phase-010-<phase-name>.md` is the default child phase-file pattern
- `design/*.design.md` remains target-state authority
- `patches/*.patch.md` remains governed patch/review/change-surface authority outside the live phase-plan namespace
- `phase-implementation-template.md` remains a non-governed root helper for drafting and readability

---

## 2) Problem Statement

The previous patch-based phase model still tied live phased execution too closely to `/patches`, even when the actual need was a dedicated phase workspace.

Observed failure modes:
- phased execution and patch governance remained conceptually entangled
- the live phase plan could still be framed as part of patch artifacts instead of a dedicated phase area
- a separate summary/index file was not mandatory
- phase-local execution detail could still be mixed into the wrong namespace
- operators had no single required `SUMMARY.md` control surface for the active phase workspace
- repository role boundaries became harder to explain because phase planning looked like a subtype of patch planning
- the model was strong for design-driven extraction, but it did not clearly define how patch-derived work should be pulled into live phased execution
- phase planning lacked an explicit one-way synthesis rule, so design/patch inputs and live execution orchestration could still be read as mutually coupled

The repository needs a rule that makes `/phase` first-class, requires `SUMMARY.md`, and lets live phased execution synthesize relevant design and patch inputs without collapsing those source layers into one another.

---

## 3) Scope and Use Boundary

This chain applies when work benefits from explicit staged execution rather than a single linear implementation block.

### 3.1 Use phased planning when

Use phases when one or more of these conditions exist:
- the work has multiple execution stages with different entry and exit conditions
- migration, rollout, or verification gates must happen in sequence
- outputs from one stage are required by a later stage
- rollback or containment boundaries matter between stages
- multiple systems, documents, services, or owners participate in the same change
- the user needs a governed plan that shows how design, TODO, and changelog move together during execution

### 3.2 Do not use phased planning when

Do not add phases when:
- the work is a single obvious edit or one-step fix
- the task is a tiny typo, wording cleanup, or low-risk isolated change
- a normal implementation plan or TODO checklist is sufficient
- the only reason for phases is visual symmetry or template compliance
- the plan would invent filler stages that do not change execution decisions

Phase planning is for execution clarity, not ceremony.

### 3.3 Mandatory `/phase` structure

When phased planning is used, the repository must use a dedicated `/phase` workspace.

Required structure:

```text
phase/
  SUMMARY.md
  phase-001-<phase-name>.md
  phase-002-<phase-name>.md
  phase-003-<phase-name>.md
```

`SUMMARY.md` is mandatory.
Live phased execution files must not be stored under `/patches`.

### 3.4 Source-input synthesis boundary

`/phase` is the live execution synthesis layer, not a new source-of-truth layer.

It may consume:
- `design/*.design.md` as target-state inputs
- `patches/*.patch.md` as optional governed change/review inputs when patch-derived work matters

This direction is one-way:
- phase artifacts may cite and synthesize design and patch inputs
- design and patch artifacts are not required to point back to phase
- using patch input does not move live execution planning into `/patches`
- using design input does not turn phase into target-state authority

---

## 4) Summary-and-Child Phase Model

### 4.1 `phase/SUMMARY.md` role

`phase/SUMMARY.md` is the governed summary/index file for the active phased execution plan.

It should keep:
- overall context and target state
- analysis of risk, constraints, and dependencies
- a phase map or phase index
- references to child phase files
- summary-level source inputs from design and patch artifacts when relevant
- cross-phase handoffs and dependency rules
- overall TODO/changelog coordination when the concern is global
- end-to-end verification requirements
- overall rollback or containment behavior
- an overview flow diagram for the full phase set

### 4.2 Child phase-file role

Each child phase file owns the execution detail for exactly one phase.

A child phase file should keep:
- phase identity and status
- summary-file reference
- design references specific to that phase
- optional patch references specific to that phase when patch-derived work exists
- phase objective and rationale
- prerequisites and entry conditions
- action points and execution checklist
- out-of-scope boundary
- affected artifacts
- phase-local TODO/changelog coordination
- verification evidence and exit criteria
- risks, rollback notes, and next possible phases

### 4.3 Canonical default path pattern

The default phased layout is:

```text
phase/
  SUMMARY.md
  phase-001-<phase-name>.md
  phase-002-<phase-name>.md
  phase-003-<phase-name>.md
```

Zero-padded contiguous numbering (`001`, `002`, `003`) is preferred so phase order stays human-readable and naturally sequential.

### 4.4 `/patches` boundary

`/patches` is not the live phase-plan namespace.
When phased execution is used, live phase planning belongs in `/phase`.

---

## 5) Required Phase Semantics

### 5.1 Summary-file expectations

`phase/SUMMARY.md` should expose the selected phase strategy clearly.

Recommended summary signals:
- phase identifier or name
- status
- child file path
- objective
- design reference
- patch reference when patch-derived work exists
- dependencies or prerequisites
- outputs or handoff artifacts
- TODO companion signals when active execution tracking matters
- changelog impact when a phase is expected to create synchronized or shipped history

A compact phase map or table is recommended when it improves scanability.

### 5.1.1 Summary source-input extraction table rule

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

### 5.1.2 Summary flow-diagram rule

`phase/SUMMARY.md` should include a small overview flow diagram for the whole phase set.

The summary diagram should show, as applicable:
- the relevant design source, patch source, or current-state baseline
- the major phase sequence or branching path
- what major capability, workflow, or governed state each phase changes
- the final target state produced by the combined phased execution

This diagram exists to improve review speed and make the full phase story visible before reviewers open the child phase files.
It must follow `flow-diagram-no-frame.md`.

### 5.1.3 Summary review-aggregate rule

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

### 5.2 Stable child phase-file field set

Each child phase file should define, or clearly map to, this semantic field set:
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

Fields may be marked not applicable when truly unnecessary, but they should not disappear in a way that hides execution meaning.

### 5.3 Source traceability rule

Every child phase file should make clear which source details it is implementing, validating, or synchronizing.

Required source-input behavior:
- design references remain the primary target-state traceability input when relevant
- patch references may be added when patch-derived work materially affects the phase
- phase may synthesize both source types in the same child file when that improves execution clarity
- source references remain one-way inputs into phase rather than back-link obligations on design or patch documents

Good traceability signals:
- exact design file reference
- specific design section heading or anchor
- exact patch file reference when patch-derived work exists
- patch section heading, anchor, or change block locator when relevant
- short summary of the source contract being executed in that phase

Vague references such as "follow the design" are insufficient when the design contains multiple requirements.

### 5.4 Design-to-phase extraction rule

Every child phase file should explicitly show what was **pulled from the design** and transformed into phase execution work.

Required extraction signals:
- the source design section or requirement
- the behavior, contract, workflow, component, or governance rule derived from that source
- what this phase is enhancing, extending, migrating, validating, or replacing
- the target execution artifact or operational outcome expected from that design input

A reviewer should be able to see the design-to-execution mapping without inferring it from scattered notes.

### 5.5 Patch-to-phase extraction rule

When patch-derived work exists, each child phase file should also show what was **pulled from the patch** and transformed into phase execution work.

Required extraction signals:
- the source patch file and the relevant section, anchor, or change-surface locator
- the patch-defined change, review constraint, migration step, or implementation surface being operationalized in the phase
- what this phase is applying, validating, sequencing, or rolling out from that patch input
- the target execution artifact or operational outcome expected from that patch input

This patch-to-phase mapping exists alongside the design-to-phase mapping.
It does not replace design traceability, and it does not turn the patch into the source of truth for the overall target state.

### 5.6 Review flow-diagram rule

Every child phase file should include a small review-oriented flow diagram.

The diagram should show, as applicable:
- the source design element, source patch element, or current-state component
- the phase action applied in this phase
- the resulting target component, workflow, or operational state
- the dependency or handoff into the next state when relevant

This diagram exists to improve review speed and clarity.
It must follow `flow-diagram-no-frame.md`:
- no boxes
- no frames
- arrows and indentation only

### 5.7 Reviewer-checklist block rule

Every child phase file should include a small reviewer-oriented checklist block.

The reviewer checklist should make it easy to confirm:
- the cited design source is correct for this phase when design input is used
- the cited patch source is correct for this phase when patch input is used
- the derived execution work is justified by the cited source inputs
- the source → phase action → target outcome flow is clear
- the phase boundary is correct and the work belongs in this phase
- dependencies and handoffs are explicit enough for safe progression
- verification evidence is sufficient for review or sign-off

This block exists for review readiness and should remain distinct from the execution checklist.

### 5.8 Standard review-outcome vocabulary rule

Every child phase file should use one standardized review-outcome vocabulary.

#### Sign-off status values
Use these values for the sign-off decision field:
- `Pending Review`
- `Needs Revision`
- `Approved`
- `Approved With Follow-up`
- `Not Required`

#### Reviewer severity values
Use these values when review issues must be categorized:
- `Blocking`
- `Non-Blocking`
- `Follow-Up`
- `None`

#### Reviewer disposition values
Use these values when the reviewer records the disposition of findings:
- `Must Fix Before Approval`
- `May Proceed With Follow-Up`
- `Approved As-Is`
- `No Review Required`

These values should align so review outcomes are easy to compare across phases and easy to read during approval.

---

## 6) Companion Tracking Model

Phased plans should not treat TODO and changelog as afterthoughts.

### 6.1 Summary-level coordination

`phase/SUMMARY.md` should show:
- global TODO coordination when multiple phases affect the same execution slice
- global changelog coordination when one synchronized history event depends on multiple phases
- the checkpoint rules for when companion artifacts are allowed to change

### 6.2 Child-level coordination

Each child phase file should show:
- what TODO work is active for that phase
- what TODO transition happens when the phase exits
- what changelog impact should be recorded later when the phase completes or when synchronized rollout closes

TODO remains execution tracking only.
Changelog remains history only.
`phase/SUMMARY.md` plus the child phase files remain the live phase plan.

---

## 7) Cross-Phase Handoffs and Coordination

When multiple phases exist, the plan should make cross-phase relationships explicit.

Required coordination guidance:
- identify what later phases depend on
- identify what outputs must exist before handoff
- identify what source inputs are design-derived, patch-derived, or synthesized from both when that distinction affects sequencing
- state what verification gate must pass before moving forward
- identify work that can proceed in parallel versus work that must wait
- preserve rollback or containment boundaries around phase transitions
- identify when TODO state or changelog state should change as part of phase completion

The plan should make it obvious how completion of one phase changes what becomes allowed next.

---

## 8) Verification and Rollback Boundaries

Phased planning must preserve both local and global safety.

Required boundary behavior:
- each child phase file defines phase-level verification
- each child phase file defines local rollback or containment notes
- `phase/SUMMARY.md` defines end-to-end verification
- `phase/SUMMARY.md` defines overall rollback or containment behavior
- passing one phase does not imply overall completion

`TODO.md` may track current actionable items derived from active phases, but it does not replace the summary file or child phase definitions themselves.

---

## 9) Phase Validation Checklist Boundary

The `phase-implementation` checklist validates **phased execution-plan quality** only.

Validate here:
- phase necessity
- summary-versus-child structure quality
- source-input traceability across design and patch inputs when applicable
- TODO/changelog companion coordination
- execution control quality

Do not validate here:
- patch metadata completeness
- patch filename/location compliance
- patch history-link integrity
- patch review-artifact governance requirements

Those remain outside this rule and belong to patch governance when patch docs exist.

---

## 10) Phase Validation Checklist

A strong phased plan should pass the following checks when phases are used.

### 10.1 Planning Appropriateness
- [ ] Phased planning is justified by real staged execution needs
- [ ] The plan does not invent filler phases for symmetry only
- [ ] Phase order reflects project reality rather than a fake global sequence

### 10.2 Summary/Child Structure Quality
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

### 10.3 Source Traceability
- [ ] Each child phase file cites the relevant design file or section when design input exists
- [ ] Each child phase file cites the relevant patch file or section when patch-derived work exists
- [ ] Source references are specific enough to show what requirement or change surface is being executed
- [ ] No child phase file relies on a vague "follow the design" statement alone
- [ ] Each child phase explicitly maps design source → derived execution work when design input exists
- [ ] Each child phase explicitly maps patch source → derived execution work when patch-derived work exists
- [ ] Each child phase makes clear what part is being enhanced, developed, migrated, validated, applied, or replaced
- [ ] Each child phase includes a review-oriented flow diagram showing source → phase action → target outcome
- [ ] Each child phase includes a reviewer checklist block for source correctness, flow clarity, boundary correctness, dependency clarity, and evidence readiness
- [ ] Each child phase uses standardized sign-off status values and aligned severity/disposition fields when review outcomes are recorded

### 10.4 Companion Coordination
- [ ] Summary-level TODO/changelog coordination is explicit when global coordination matters
- [ ] Child-level TODO/changelog coordination is explicit when phase-local execution tracking matters
- [ ] TODO and changelog are treated as companion layers, not as replacements for the plan

### 10.5 Execution Control Quality
- [ ] Dependencies and handoffs are explicit when later phases rely on earlier outputs
- [ ] Phase-level verification expectations are explicit in child files
- [ ] Phase-level rollback or containment notes exist where failure boundaries matter
- [ ] End-to-end verification and overall rollback remain explicit in `SUMMARY.md`
- [ ] The next possible phase or next execution path is clear

---

## 11) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| fake global `Phase 1 → N` requirement | forces artificial structure onto unrelated projects | choose phases according to project reality |
| no `SUMMARY.md` file | removes the required high-signal control surface | always create `phase/SUMMARY.md` when phased planning is used |
| storing live phase plans under `/patches` | keeps phase planning entangled with patch governance | keep live phased execution under `/phase/` |
| putting all phase-local detail only in `SUMMARY.md` | makes the summary heavy and hard to operate | keep global control in `SUMMARY.md` and per-phase detail in child files |
| child phase files without design references when design input exists | breaks traceability back to intended behavior | cite the design file and the exact relevant section |
| child phase files using patch-derived work without patch references | hides the governed change surface being operationalized | cite the relevant patch file and precise section or change locator |
| child phase blocks without status or action points | makes execution tracking weak and hard to follow | show clear status plus an action checklist |
| verification only at the very end | hides phase-level failure boundaries | define verification gates inside each child phase file and keep end-to-end checks in `SUMMARY.md` |
| phases added only for symmetry | adds ceremony without decision value | keep the plan linear unless real staged execution exists |

---

## 12) Completion Boundary and Stop Rule

### 12.1 Definition of Done

Treat the phase-planning model as complete when all of the following are true:
- `/phase` is the live namespace
- `phase/SUMMARY.md` contains the required summary-level structures
- child phase files contain the required design, review, and execution structures
- review outcome vocabulary is standardized across child phases
- rule/design/changelog/template/TODO synchronization is complete

### 12.2 Stop rule after completion

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

## 13) Quality Metrics

| Metric | Target |
|--------|--------|
| Phase-use appropriateness | High |
| `/phase` workspace compliance | 100% |
| `SUMMARY.md` presence when phased planning is used | 100% |
| Stable per-phase field coverage | High |
| Design traceability coverage | 100% when design input is used |
| Patch traceability coverage | 100% when patch-derived work is used |
| One-way source-input boundary clarity | 100% |
| TODO/changelog companion visibility | High |
| Cross-phase handoff clarity | High |
| Phase-level verification visibility | 100% when phases are used |
| Checklist boundary clarity vs patch-control | 100% |
| Live phased execution files under `/patches` | 0 |
| Helper-authority confusion | 0 |
| Unrequested post-completion capability expansion | 0 |

---

## 14) Integration

| Document | Relationship |
|----------|--------------|
| [../phase-implementation.md](../phase-implementation.md) | Runtime implementation of this design |
| [document-patch-control.design.md](document-patch-control.design.md) | Patch governance boundary outside `/phase` and one-way synthesis clarification for patch inputs |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role model for `/phase`, helper, TODO, changelog, and one-way design/patch source synthesis |
| [todo-standards.design.md](todo-standards.design.md) | Execution-tracking boundary |
| [../phase-implementation-template.md](../phase-implementation-template.md) | Non-governed root helper for authoring |

---

> Full history: [../changelog/phase-implementation.changelog.md](../changelog/phase-implementation.changelog.md)
