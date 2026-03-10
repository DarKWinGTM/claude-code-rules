# Phase Implementation

> **Current Version:** 1.1
> **Design:** [design/phase-implementation.design.md](design/phase-implementation.design.md) v1.1
> **Session:** 468e053d-9953-496e-8e83-910e2ae67402
> **Full history:** [changelog/phase-implementation.changelog.md](changelog/phase-implementation.changelog.md)

---

## Rule Statement

**Core Principle: Use phased planning only when staged execution meaningfully improves clarity, and keep phase semantics explicit, traceable to design, and easy to execute without forcing a fake global sequence.**

This rule defines the semantic standard for phase planning. The live governed plan still belongs in `patches/*.patch.md`, while the root helper remains a non-governed drafting aid.

---

## Core Requirements

### 1) Purpose and Authority Boundary

`phase-implementation.md` defines:
- what phase planning is for
- when phased planning should and should not be used
- what semantic fields a phase should contain
- how design references should be mapped into each phase
- how cross-phase handoffs, verification, TODO coordination, changelog coordination, and rollback boundaries should be expressed

It does **not** replace:
- `patches/*.patch.md` as the live governed execution-plan artifact
- `document-patch-control.md` as the patch governance and metadata rule
- `TODO.md` as execution tracking
- `changelog/*.changelog.md` as history

### 2) When to Use Phase Planning

Use phased planning when one or more of these are true:
- work must happen in distinct stages with different entry and exit conditions
- rollout, migration, or verification gates matter between stages
- outputs from one stage are required by a later stage
- rollback or containment boundaries matter during execution
- the change spans multiple systems, files, or owners and benefits from staged coordination
- the project needs a governed patch that shows how design, TODO, and changelog move together during execution

### 3) When Not to Use Phase Planning

Do not force phases when:
- the work is a single obvious change
- a normal implementation plan or TODO checklist is enough
- the task is tiny and low-risk
- phases would only exist to satisfy template shape
- the plan would invent filler stages that add no execution meaning

### 4) Flexible Order Contract

When phase planning is used, phases may be:
- merged
- split
- skipped
- repeated
- reordered

These are normal allowed behaviors.
There is no repository-wide mandatory `Phase 1 → Phase N` sequence.

### 5) Stable Phase Field Contract

Each chosen phase should define, or clearly map to:
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

### 6) Design Traceability Contract

Each phase should make clear what part of the design it is executing.

Use explicit references such as:
- design file path or name
- section heading or anchor when available
- short note describing the exact design requirement being implemented, validated, or synchronized

A phase should never rely on a vague note like "follow the design" when the design contains multiple requirements.

### 7) Cross-Phase Coordination Contract

When multiple phases exist, make the following explicit when relevant:
- dependencies and handoffs between phases
- outputs required before later phases can start
- verification gates that must pass before progressing
- work that can proceed in parallel
- rollback or containment boundaries before the next phase starts
- when TODO state should be updated
- when changelog impact should be recorded

### 8) Verification and Rollback Contract

Phased planning must preserve both local and global safety:
- each phase should define phase-level verification
- each phase should define local rollback or containment notes
- the full plan must still define end-to-end verification
- the full plan must still define overall rollback or containment behavior

Passing one phase does not mean the full plan is complete.

### 9) Checklist Boundary Contract

The `phase-implementation` checklist validates **phased execution-plan quality** only.

Validate here:
- phase necessity
- phase definition quality
- design traceability
- TODO/changelog companion coordination
- execution control quality

Do not validate here:
- patch metadata completeness
- patch filename or path compliance
- patch history-link integrity
- patch review-artifact governance requirements

Those belong to `document-patch-control.md`.

---

## Phase Model

### 1) Phase semantics live here

This rule is the semantic authority for phase-planning behavior.

### 2) Live plan instances live in patches

When a project needs an authoritative phased execution plan, the actual governed instance belongs in `patches/*.patch.md`.

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
- the patch is the authoritative execution plan
- the phase should show what TODO items or TODO transitions matter now
- the phase should show what changelog event is expected later or upon completion

This preserves visibility without turning TODO or changelog into the primary phase-definition layer.

---

## Trigger Model

Apply this rule more strongly when one or more of these signals are present:

| Trigger | Typical Signal | Expected Shape |
|--------|-----------------|----------------|
| staged rollout | migration, deploy gate, cutover, reconciliation | explicit phases with handoffs and rollback boundaries |
| dependency chain | one stage produces outputs needed by another | phase map plus entry/exit criteria |
| multi-system change | docs, runtime, install targets, services, or teams move together | phase-level affected artifacts and verification |
| design-driven execution | different parts of the design must be implemented in sequence | explicit phase-to-design mapping |
| governance execution | governed repository change with synchronized artifacts | patch plan shows TODO and changelog coordination inside phase execution |
| risk containment | partial failure needs local rollback before proceeding | phase-level verification and rollback notes |

Do not trigger this rule just because a task is long. Trigger it when staged execution meaningfully changes how the work should be planned or controlled.

---

## Phase Validation Checklist

Use this checklist only when a plan actually uses phases.
It validates the quality of the phased execution plan itself.

### 1) Planning appropriateness
- [ ] Phased planning is justified by real staged execution needs
- [ ] The plan does not invent filler phases for symmetry only
- [ ] The chosen order reflects project reality rather than a fake global sequence

### 2) Phase definition quality
- [ ] A phase map is visible when more than one phase exists
- [ ] Each phase has a clear status
- [ ] Each phase has a clear objective
- [ ] Each phase has actionable execution points
- [ ] Each phase has explicit exit criteria when phase completion matters

### 3) Design traceability
- [ ] Each phase cites the relevant design file or section
- [ ] Design references are specific enough to show what requirement is being executed
- [ ] No phase relies on a vague "follow the design" statement alone

### 4) Companion coordination
- [ ] TODO coordination is explicit when execution tracking is relevant
- [ ] Changelog coordination is explicit when synchronization or release history is relevant
- [ ] TODO and changelog are treated as companion layers, not replacements for the phase plan

### 5) Execution control quality
- [ ] Dependencies and handoffs are explicit when later phases rely on earlier outputs
- [ ] Verification expectations are explicit
- [ ] Rollback or containment notes exist where phase failure would matter
- [ ] The next possible phase or next execution path is clear

---

## Good Patterns

### Pattern 1: Real staged migration with design mapping

```markdown
Phase Map

| Phase | Status | Objective | Design Reference | Depends On | Outputs |
|------|--------|-----------|------------------|------------|---------|
| P-A | Completed | Create new governed chain | `design/phase-implementation.design.md` sections 1-5 | none | rule/design/changelog baseline |
| P-B | In Progress | Realign related governance docs | `design/document-patch-control.design.md` section 8 | P-A | synchronized authority model |
| P-C | Pending | Install runtime copies | rollout section in master design | P-B | installed runtime files |
```

### Pattern 2: Per-phase action checklist with companion tracking

```markdown
### P-B: Realign related governance docs

**Status**
- In Progress

**Design references**
- `design/document-patch-control.design.md` section 8
- `design/project-documentation-standards.design.md` section 6

**Action points / execution checklist**
- [x] Refocus patch control to governance + metadata scope
- [ ] Update project-documentation standards role model
- [ ] Record synchronized rollout in master changelog

**TODO coordination**
- Active TODO item remains open until both governance chains are synchronized

**Changelog coordination**
- Add one release entry after runtime + design + changelog synchronization is complete
```

### Pattern 3: Linear plan instead of phases

```markdown
This change is a one-file wording fix.
A normal implementation checklist is enough, so phased planning is not used.
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| fake global `Phase 1 → N` requirement | creates unnecessary ceremony and distorts project reality | choose only the phases the project actually needs |
| helper template treated like a governed doc | causes authority confusion | keep authority in this rule and in the real patch instance |
| patch-control used as the only semantic authority | blends metadata governance with planning semantics | keep semantic authority here and governance authority in patch control |
| TODO used as the full phase spec | loses handoff and rollback meaning | keep TODO as execution tracking only |
| phases without design references | breaks traceability back to intended behavior | cite the relevant design sections |
| phases without status or action points | makes tracking weak and hard to execute | include status plus a clear checklist |
| phases without verification or exit criteria | makes progression ambiguous | define phase-level checks and completion gates |
| phase checklist used to validate patch metadata or patch-link integrity | blurs patch and phase roles | keep patch-governance checks in `document-patch-control` |
| phases added for formatting symmetry | adds noise without control value | use a linear plan if stages are not real |

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Appropriate use of phase planning | High |
| Explicit support for merge/split/skip/repeat/reorder | 100% |
| Stable per-phase field clarity | High |
| Design traceability coverage | 100% when phases are used |
| TODO/changelog companion visibility | High |
| Cross-phase handoff clarity | High |
| Phase-level verification visibility | 100% when phases are used |
| Checklist boundary clarity vs patch-control | 100% |
| Fake global sequence language | 0 |
| Helper-versus-authority confusion | 0 |

---

## Integration

Related rules:
- [document-patch-control.md](document-patch-control.md) - patch governance, metadata, lifecycle, and review-artifact contract
- [project-documentation-standards.md](project-documentation-standards.md) - repository role model for rules, patches, helpers, TODO, and changelog
- [todo-standards.md](todo-standards.md) - keeps TODO as execution tracking only
- [strict-file-hygiene.md](strict-file-hygiene.md) - avoids unneeded duplicate planning artifacts

---
