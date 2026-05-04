# Phase Implementation

> **Current Version:** 2.26
> **Design:** [design/phase-implementation.design.md](design/phase-implementation.design.md) v2.26
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/phase-implementation.changelog.md](changelog/phase-implementation.changelog.md)

---

## Rule Statement

**Core Principle: Use phased planning only when staged execution improves clarity, synthesize sufficiently clear governed design into live phase execution order, maintain an active `/phase` workspace with mandatory `SUMMARY.md` and deterministic `NNN` / `NNN-NN` IDs, choose major versus subphase identity through lineage-first criteria, keep completed phase detail in inactive `phase/done/` history, resolve phase posture early through startup governance, and declare governed patch participation when patch is in scope.**

This rule owns phase-execution semantics. `phase/SUMMARY.md` is the governed summary/index; active child files hold phase-local execution detail; `phase/done/` is inactive completed history; design remains target-state authority; patch remains governed before/after review authority. Shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES doctrine.

---

## Authority Boundary

`phase-implementation.md` defines when to use phases, `/phase` structure, phase ID grammar, lineage selection, child-phase field expectations, design/patch-to-phase synthesis, TODO/changelog coordination, verification, rollback, and closeout behavior. It does not replace `phase/SUMMARY.md`, child phase files, design docs, patch docs, `TODO.md`, changelogs, or startup governance.

---

## When to Use Phase Planning

Use phases for meaningful stages, gated rollout/migration/verification, rollback or containment boundaries, dependencies between stages, multi-system/multi-owner coordination, or a need to show how design/TODO/changelog move together. Do not force phases for a single obvious low-risk change, a normal checklist, or filler stages with no execution meaning.

If staged work is clear, `artifact-initiation-control.md` must resolve phase posture as `use existing`, `create now`, or `ask now` before substantial drift. If the exact next phase file is absent but the phase family/stage is clear, live task shaping should still follow that implied current phase provisionally. Retrospective phase creation is repair, not the preferred path.

Resolving phase posture does not automatically open a new major phase. When a phase file must be created or selected, run the lineage gate below first.

---

## Phase Workspace Contract

### Identity grammar
- major phase: `NNN`
- subphase: `NNN-NN`
- `NNN` = top-level execution phase or grouped rollout stage
- `NNN-NN` = child execution slice inside major phase `NNN`
- hierarchy is expressed by the hyphen suffix, not prose alone
- zero-padded lexical ordering is preferred; phases may split, merge, skip, repeat, or reorder when reality requires it; subphases are optional

### Major-vs-subphase lineage gate
Before opening a new major phase, inspect checked phase lineage and choose the smallest truthful identity:
- update the current active phase when work remains inside the same active execution slice
- create a new `NNN-NN` subphase when work continues an existing major phase family
- create a new `NNN` major phase only for a new top-level rollout family
- ask or record the governing basis when multiple phase families plausibly fit and checked evidence does not settle lineage

Subphase-fit signals:
- same user-facing objective, policy domain, rule owner chain, design target, patch surface, or rollback boundary
- follow-up that refines, repairs, verifies, installs, releases, documents, or synchronizes the same governed target
- dependency on prior phase output or a clear link from `Next possible phases`, closeout notes, `TODO.md`, changelog, or `phase/SUMMARY.md`
- completed parent/sibling history still defines the same rollout family

Major-phase-fit signals:
- new first-class rule or policy domain
- materially different user-facing objective, governing basis, design target, or rollback/containment boundary
- independent rollout that does not need an existing family to be understandable or reviewable
- nesting under an existing family would overload or mislead that family
- explicit user direction to start a new phase family

Completed status does not break lineage, and new concern wording does not justify a new major phase by itself. Do not force subphases for unrelated work; if no real lineage exists, open a new major phase. Subphase use is criteria-based, not automatic nesting: the checked evidence must show shared objective, owner chain, target state, patch surface, dependency, or rollback meaning. If lineage is real but ambiguous or overloaded, preserve the relationship in `phase/SUMMARY.md` or the child phase record and choose the clearer identity.

### Required files and history
When phased planning is used:
- `phase/SUMMARY.md` is mandatory
- active executable files live under `phase/`
- valid active paths are `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md`
- completed phase-detail history may live under `phase/done/` with the same filename grammar
- live phased execution files inside patch artifacts are **not allowed**

`phase/done/` is inactive-by-default completed phase history. Active scans start with `phase/SUMMARY.md` and active child files in `phase/`; consult `phase/done/` only for history, audit, rollback, provenance, or trace reconstruction. Completed files are not junk or deletion-authorized by completed status, and `phase/done/` must not replace the live phase namespace.

---

## Source-Input Synthesis

`/phase` is a live execution synthesis layer, not source of truth. It may consume normalized design target-state truth and governed patch review input one-way: phase executes design/patch consequences, but design/patch need not point back to phase and phase does not become design or patch authority.

### Design-to-phase synthesis
When governed design is sufficiently clear for staged execution, `/phase` should derive or update execution order from design truth instead of waiting for retrospective planning. Split target state into outcome-sized phases by dependency, risk, rollout boundary, and verification gate; create or update `phase/SUMMARY.md` and current child phase files when posture resolves to `create now` or `use existing`; initialize or extend current-phase live tasks for non-trivial work; then continue phase-by-phase unless a real stop gate exists. Ask only when design ambiguity, materially different rollout choices, missing access, destructive/high-impact action, or approval-sensitive scope changes the phase plan.

### Patch linkage
When phased work uses a governed patch artifact:
- `phase/SUMMARY.md` must name the governing patch artifact(s) or explicitly state `none`
- each child phase using patch-derived work must include `Patch References`, or explicit `none`
- `none` is valid only when patch is truly not required, not when unresolved

When external docs/specs/provider references materially constrain execution, phase should point to normalized design truth so later slices do not depend on transient reading memory after compact or handoff.

---

## Phase File Responsibilities

`phase/SUMMARY.md` keeps the global execution picture: context, target state, risk, constraints, dependencies, phase map/index, active child references, lineage context, needed `phase/done/` pointers, design/patch source inputs, governing patch references, cross-phase handoffs, TODO/changelog coordination, end-to-end verification, and rollback/containment behavior.

Each executable child phase should define or map to:
- Summary File, Phase ID, Status
- design references
- patch references or explicit `none`
- objective and why the phase exists
- implementation-relevant doc/spec constraints when material
- entry conditions/prerequisites
- action checklist and out-of-scope boundaries
- affected artifacts
- TODO and changelog coordination
- verification, exit criteria, and closeout summary
- risks/rollback notes
- next possible phases

---

## Live Task-List Linkage Contract

When a phase is active and work is non-trivial, the built-in task list should mirror current phase execution slices.

Guidance:
- inspect relevant `/phase` context before shaping/extending tasks; detached generic wording is execution drift
- default tasks to the current active phase before future phases
- if the exact next phase file is absent but phase family/stage is clear, align tasks to that implied structure
- do not let task-list shaping silently allocate a new major phase; use the lineage gate when a phase file is needed
- one phase may have many outcome-sized tasks; current phase ID in task subjects is useful when it improves clarity
- extend the current task list for the same objective/phase family instead of recreating it
- task wording should follow the active session language/register; technical labels may remain technical when clearer
- use current phase, phase family, `phase/SUMMARY.md`, `TODO.md`, authored `Next possible phases`, and checked implementation state as bounded execution-discovery surfaces
- authored future-phase context may inform continuity and draft visibility but is not active execution until opened/selected/made active
- if the current phase is complete and the next phase is the implied active path, say the current phase is complete before continuing

---

## Verification, Closeout, and Rollback Contract

Each child phase should define phase-level verification, closeout expectations, and local rollback/containment notes. `phase/SUMMARY.md` still owns end-to-end verification and overall rollback/containment behavior. Patch artifacts must remain outside the live phase-plan namespace.

Phase-backed closeout should report practical delivery, not only files/tasks/audit status: delivered feature/capability/behavior/governance improvement or verification gate; user/system impact; evidence-strength-aligned verification basis; and next phase state when relevant (`not started`, `draft/planned`, `selected`, `active`, or `none opened`). Keep closeout concise and do not force it onto trivial non-phase work.

---

## Verification Checklist

- [ ] `NNN` / `NNN-NN` grammar, required active paths, and `phase/SUMMARY.md` are used
- [ ] major-vs-subphase selection checks lineage before any new major phase
- [ ] startup governance establishes or asks about `/phase` before staged/governed drift
- [ ] `phase/done/` remains inactive history, never junk/deletion authority or live namespace
- [ ] sufficiently clear governed design synthesizes into phase summary, current child files, and current-phase live tasks without replacing design authority
- [ ] patch-derived phase work shows explicit patch linkage and patch artifacts stay outside live phase workspace
- [ ] child phases include required source references, execution fields, verification, rollback/risks, and closeout
- [ ] closeout reports delivery, feature/improvement, impact, evidence-strength-aligned verification basis, and next phase state when relevant
- [ ] task creation aligns to active/implied phase context while authored future-phase context remains non-active until opened/selected

---

## Integration

Related rules:
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup phase posture
- [document-patch-control.md](document-patch-control.md) - patch governance boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository document model
- [todo-standards.md](todo-standards.md) - TODO and live task coordination
