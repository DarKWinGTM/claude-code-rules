# Phase Implementation

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402 (2026-03-10)

---

## 1) Goal

Define one first-class rule chain for phased implementation planning so phase semantics are explicit, reusable, and easy to read while live governed execution plans still live in `patches/*.patch.md`.

The target state separates four concerns cleanly:
- `phase-implementation.md` defines phase-planning semantics
- `patches/*.patch.md` holds the live governed phase-plan instances
- `document-patch-control.md` governs patch metadata, reviewability, and lifecycle behavior
- `phase-implementation-template.md` remains a non-governed root helper for drafting and readability

---

## 2) Problem Statement

Before this chain, phased execution guidance lived only indirectly through `document-patch-control`, while the root helper still resembled a pseudo-governed document.

Observed failure modes:
- phase semantics and patch-governance metadata were blended together
- the helper template looked more authoritative than it should
- projects could misread phases as a fake repository-wide `Phase 1 → N` requirement
- plans could omit stable phase fields, handoff boundaries, verification gates, or rollback expectations
- plans often lacked explicit traceability back to the governing design details
- TODO and changelog coordination could be implied rather than planned explicitly inside the phase file
- review quality checks for patch artifacts could drift into phase-planning checks, or vice versa

This design creates one semantic authority for phase planning without replacing patches as the live governed execution artifacts.

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
- the user needs a live governed plan in `patches/*.patch.md`

### 3.2 Do not use phased planning when

Do not add phases when:
- the work is a single obvious edit or one-step fix
- the task is a tiny typo, wording cleanup, or low-risk isolated change
- a normal implementation plan or TODO checklist is sufficient
- the only reason for phases is visual symmetry or template compliance
- the plan would invent filler stages that do not change execution decisions

Phase planning is for execution clarity, not ceremony.

---

## 4) Core Phase Model

### 4.1 One semantic standard, many valid phase shapes

`phase-implementation` defines the semantic meaning of phase planning.

It does **not** require every project to use the same labels, count, or sequence. The active governed instance remains the patch document for that project.

### 4.2 Flexible order rules

The standard must explicitly allow:
- phases to be merged
- phases to be split
- phases to be skipped
- phases to be repeated
- phases to be reordered

These are first-class allowed behaviors, not exceptions.

### 4.3 Common patterns are suggestive only

Common patterns may be helpful, but they are examples rather than mandatory repository stages.

Typical examples:
- discovery / alignment
- design / decision lock
- implementation / change
- migration
- verification / test
- rollout / deploy
- cleanup / optimization

A project may use none, some, or renamed versions of these.

---

## 5) Required Phase Semantics

### 5.1 Phase-map expectations

When a plan uses more than one phase, it should expose the selected phase strategy clearly.

Recommended phase-map signals:
- phase identifier or name
- status
- objective
- design references
- dependencies or prerequisites
- outputs or handoff artifacts
- TODO companion signals when active execution tracking matters
- changelog impact when a phase is expected to create a synchronized or shipped history event

A compact phase map or table is recommended when it improves scanability.

### 5.2 Stable per-phase field set

Each chosen phase should define, or clearly map to, the same semantic field set:
- Status
- Design references
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

### 5.3 Design traceability rule

Every phase should make clear which design details it is implementing, validating, or synchronizing.

Good traceability signals:
- exact design file reference
- specific section heading or anchor
- short summary of the design contract being executed in that phase

Vague references such as "follow the design" are insufficient when the design contains multiple requirements.

---

## 6) Companion Tracking Model

Phased plans should not treat TODO and changelog as afterthoughts.

Required expectations:
- the phase file should show how active TODO work maps to the current phase
- the phase file should show what changelog entry or changelog impact is expected when the phase completes or when synchronization occurs
- TODO remains execution tracking only
- changelog remains history only
- the patch remains the live governed plan that explains how those companions relate to execution

The goal is visibility, not role confusion.

---

## 7) Cross-Phase Handoffs and Coordination

When multiple phases exist, the plan should make cross-phase relationships explicit.

Required coordination guidance:
- identify what later phases depend on
- identify what outputs must exist before handoff
- state what verification gate must pass before moving forward
- identify work that can proceed in parallel versus work that must wait
- preserve rollback or containment boundaries around phase transitions
- identify when TODO state or changelog state should change as part of phase completion

The plan should make it obvious how completion of one phase changes what becomes allowed next.

---

## 8) Verification and Rollback Boundaries

Phased planning must preserve both local and global safety.

Required boundary behavior:
- each phase should define phase-level verification
- each phase should define local rollback or containment notes
- the full plan must still define end-to-end verification
- the full plan must still define overall rollback or containment behavior
- passing one phase does not imply overall completion

`TODO.md` may track current actionable items derived from active phases, but it does not replace the phase definitions themselves.

---

## 9) Phase Validation Checklist Boundary

The `phase-implementation` checklist validates **phased execution-plan quality** only.

Validate here:
- phase necessity
- phase definition quality
- design traceability
- TODO/changelog companion coordination
- execution control quality

Do not validate here:
- patch metadata completeness
- patch filename/location compliance
- patch history-link integrity
- patch review-artifact governance requirements

Those remain the responsibility of `document-patch-control`.

---

## 10) Phase Validation Checklist

A strong phased plan should pass the following checks when phases are used:

### 10.1 Planning Appropriateness
- [ ] Phased planning is justified by real staged execution needs
- [ ] The plan does not invent filler phases for symmetry only
- [ ] Phase order reflects project reality rather than a fake global sequence

### 10.2 Phase Definition Quality
- [ ] The phase map is visible when more than one phase exists
- [ ] Each phase has a clear status
- [ ] Each phase has a clear objective
- [ ] Each phase has actionable execution points
- [ ] Each phase has explicit exit criteria when phase completion matters

### 10.3 Design Traceability
- [ ] Each phase cites the relevant design file or section
- [ ] Design references are specific enough to show what requirement is being executed
- [ ] No phase relies on a vague "follow the design" statement alone

### 10.4 Companion Coordination
- [ ] TODO coordination is explicit when execution tracking is relevant
- [ ] Changelog coordination is explicit when synchronization or release history is relevant
- [ ] TODO and changelog are treated as companion layers, not as replacements for the phase plan

### 10.5 Execution Control Quality
- [ ] Dependencies and handoffs are explicit when later phases rely on earlier outputs
- [ ] Verification expectations are explicit
- [ ] Rollback or containment notes exist where phase failure would matter
- [ ] The next possible phase or next execution path is clear

---

## 11) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| fake global `Phase 1 → N` requirement | forces artificial structure onto unrelated projects | choose phases according to project reality |
| helper template presented as authority | creates governance ambiguity | keep semantic authority in `phase-implementation.md` and live authority in the patch |
| TODO or changelog used as the main phase spec | loses stable phase semantics and handoff detail | keep TODO as execution tracking and changelog as history only |
| phases without design references | breaks traceability back to intended behavior | cite the design file and the exact relevant section |
| phase blocks without status or action points | makes execution tracking weak and hard to follow | show clear status plus an action checklist |
| phases without exit criteria | handoffs become ambiguous | define what must be true before progressing |
| verification only at the very end | hides phase-level failure boundaries | define verification gates inside each phase |
| phase checklist used to validate patch metadata or patch-link integrity | blurs patch and phase roles | keep patch-governance checks in `document-patch-control` |
| phases added only for symmetry | adds ceremony without decision value | keep the plan linear unless real staged execution exists |

---

## 12) Quality Metrics

| Metric | Target |
|--------|--------|
| Phase-use appropriateness | High |
| Flexible order support | 100% |
| Stable per-phase field coverage | High |
| Design traceability coverage | 100% when phases are used |
| TODO/changelog companion visibility | High |
| Cross-phase handoff clarity | High |
| Phase-level verification visibility | 100% when phases are used |
| Checklist boundary clarity vs patch-control | 100% |
| Fake global sequence requirements | 0 |
| Helper-authority confusion | 0 |

---

## 13) Integration

| Document | Relationship |
|----------|--------------|
| [../phase-implementation.md](../phase-implementation.md) | Runtime implementation of this design |
| [document-patch-control.design.md](document-patch-control.design.md) | Patch governance and metadata contract |
| [project-documentation-standards.design.md](project-documentation-standards.design.md) | Repository role model for rule, patch, helper, TODO, and changelog boundaries |
| [todo-standards.design.md](todo-standards.design.md) | Execution-tracking boundary |
| [../phase-implementation-template.md](../phase-implementation-template.md) | Non-governed root helper for authoring |

---

> Full history: [../changelog/phase-implementation.changelog.md](../changelog/phase-implementation.changelog.md)
