# Phase Implementation

> **Current Version:** 2.33
> **Design:** [design/phase-implementation.design.md](design/phase-implementation.design.md) v2.33
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/phase-implementation.changelog.md](changelog/phase-implementation.changelog.md)

---

## Rule Statement

**Core Principle: Use phased planning only when staged execution improves clarity, synthesize sufficiently clear governed design into live phase execution order and a bounded goal/output/gate-aware roadmap or phase matrix, maintain an active `/phase` workspace with mandatory compact `SUMMARY.md` and deterministic `NNN` / `NNN-NN` IDs, choose major versus subphase identity through lineage-first criteria that keep subphases tied to bounded execution gates while allowing umbrella-phase escape when a family becomes misleading or saturated, visibly link non-trivial phase-backed live tasks to active or implied phase context, move accumulated daily phase movement into referenced `phase/history/` shards, keep completed phase detail in inactive `phase/done/` history, resolve phase posture early through startup governance, and declare governed patch participation when patch is in scope.**

This rule owns phase-execution semantics. `phase/SUMMARY.md` is the compact governed summary/index; active child files hold phase-local execution detail; `phase/history/` holds referenced daily phase movement; `phase/done/` is inactive completed history; design remains target-state authority; patch remains governed before/after review authority. Shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES doctrine.

---

## Authority Boundary

`phase-implementation.md` defines when to use phases, `/phase` structure, phase ID grammar, lineage selection, child-phase field expectations, design/patch-to-phase synthesis, roadmap/phase-matrix expectations, phase-level goal/output/gate semantics, TODO/changelog coordination, verification, rollback, and closeout behavior. It does not replace `phase/SUMMARY.md`, child phase files, design docs, patch docs, `TODO.md`, changelogs, goal-set ownership, or startup governance.

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
- create a new `NNN-NN` subphase when work continues the same bounded execution gate inside an existing major family
- create a new `NNN` major phase when work forms a distinct top-level rollout family, capability boundary, output, verification gate, release boundary, or rollback boundary
- ask or record the governing basis when multiple phase families plausibly fit and checked evidence does not settle lineage

Lineage is evidence, not a prison. A subphase must preserve the parent family's bounded goal/output/gate meaning; same product area, broad domain, owner chain, historical label, or old phase family is not sufficient by itself.

Subphase-fit signals:
- same bounded execution gate, target output, verification gate, dependency chain, or rollback boundary
- same governed target where the follow-up refines, repairs, verifies, installs, releases, documents, or synchronizes that target without changing the top-level capability boundary
- dependency on prior phase output or a clear link from `Next possible phases`, closeout notes, `TODO.md`, changelog, or `phase/SUMMARY.md` that preserves the same goal/output/gate
- completed parent/sibling history still defines the same bounded rollout family rather than only the same broad program area

Major-phase-fit and umbrella-escape signals:
- new first-class rule, policy domain, feature capability, or rollout family
- materially different user-facing objective, governing basis, design target, output, verification gate, release boundary, or rollback/containment boundary
- independent rollout that does not need an existing phase family to be understandable or reviewable
- the parent label has become a program bucket rather than a bounded execution slice
- many sibling subphases no longer share one clear gate, output, or closeout meaning
- readers cannot tell why the work remains inside the old family without reading historical context
- nesting under an existing family would overload or mislead that family
- explicit user direction to start a new phase family

Completed status does not break lineage, and new concern wording does not justify a new major phase by itself. Do not force subphases for unrelated work; if no real lineage exists, open a new major phase. Do not force old-family subphases when the work has a separate output/gate/release/rollback meaning or the old family is saturated. If lineage is real but ambiguous or overloaded, preserve the relationship in `phase/SUMMARY.md` or the child phase record and choose the clearer identity, including a new major phase when that prevents umbrella drift.

### God Phase prevention

A God Phase is a phase file that tries to execute several independent phases at once. It is not defined by length alone; it is defined by mixed execution responsibilities.

God Phase signals include:
- multiple primary goals that can complete independently
- multiple expected outputs that do not share one bounded gate
- unrelated verification gates, rollback boundaries, or capability streams
- phase content that is really a roadmap, changelog, TODO list, patch review, and execution file combined
- readers cannot tell what must be true for this phase alone to close

Required repair posture:
- if the work still has one bounded goal/output/gate, restructure the phase file in place
- if the work shares the same parent rollout gate, split into `NNN-NN` subphases
- if the work has a distinct capability, release, verification, output, or rollback boundary, open a new major phase
- keep `phase/SUMMARY.md` as the compact map and move accumulated history/completed detail to `phase/history` or `phase/done`
- do not use phase splitting as deletion authority for old content

### Required files and history
When phased planning is used:
- `phase/SUMMARY.md` is mandatory
- active executable files live under `phase/`
- valid active paths are `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md`
- daily phase movement may live under `phase/history/YYYY-MM-DD*.md` and must link back to `phase/SUMMARY.md`
- completed phase-detail history may live under `phase/done/` with the same filename grammar
- live phased execution files inside patch artifacts are **not allowed**

`phase/history/` is referenced daily movement history and `phase/done/` is inactive-by-default completed phase history. Active scans start with compact `phase/SUMMARY.md` and active child files in `phase/`; consult `phase/history/` or `phase/done/` only through active references or for history, audit, rollback, provenance, or trace reconstruction. History files are not junk or deletion-authorized by rollover/completed status, and history/done shards must not replace the live phase namespace.

---

## Source-Input Synthesis

`/phase` is a live execution synthesis layer, not source of truth. It may consume normalized design target-state truth and governed patch review input one-way: phase executes design/patch consequences, but design/patch need not point back to phase and phase does not become design or patch authority.

### Design-to-phase synthesis
When governed design is sufficiently clear for staged execution, `/phase` should derive or update execution order from design truth instead of waiting for retrospective planning. Split target state into outcome-sized phases by dependency, risk, rollout boundary, expected output, and verification gate; create or update `phase/SUMMARY.md` and current child phase files when posture resolves to `create now` or `use existing`; initialize or extend current-phase live tasks for non-trivial work; then continue phase-by-phase unless a real stop gate exists. Ask only when design ambiguity, materially different rollout choices, missing access, destructive/high-impact action, or approval-sensitive scope changes the phase plan.

### Roadmap and next-phase synthesis
When a governed objective has enough design/TODO/phase/implementation evidence to forecast more than the current slice, `phase/SUMMARY.md` should carry a bounded roadmap or phase matrix instead of only the currently open phase. The roadmap should identify meaningful candidate phases, their goal, expected output, completion gate, dependencies, deliverables, and status such as `active`, `selected`, `implied-unblocked`, `proposal`, `blocked`, `needs-approval`, or `none opened`. Roadmap entries are planning context, not automatic execution authority: selected and unblocked follow-up can continue; implied but unselected work should be recommended as a goal-qualified proposal; ambiguous, approval-sensitive, or materially divergent work should trigger a narrow question.

After a phase-backed objective closes, inspect the checked roadmap and goal surfaces before ending the closeout. If future work is meaningful, name the best-supported next phase, wave, or goal with why it is supported, expected output, and gate; if no next phase/goal is selected or meaningful, state that directly. Do not let this recommendation interrupt safe continuous execution through already selected phases, and do not auto-promote draft or proposal-only entries into active phases.

### Patch linkage
When phased work uses a governed patch artifact:
- `phase/SUMMARY.md` must name the governing patch artifact(s) or explicitly state `none`
- each child phase using patch-derived work must include `Patch References`, or explicit `none`
- `none` is valid only when patch is truly not required, not when unresolved

When external docs/specs/provider references materially constrain execution, phase should point to normalized design truth so later slices do not depend on transient reading memory after compact or handoff.

---

## Phase File Responsibilities

`phase/SUMMARY.md` keeps the compact global execution picture: context, target state, risk, constraints, dependencies, goal/output/gate-aware roadmap or phase matrix, phase map/index, active child references, lineage context, needed `phase/history/` and `phase/done/` pointers, design/patch source inputs, governing patch references, cross-phase handoffs, TODO/changelog coordination, end-to-end verification, next-phase or next-goal recommendation basis, and rollback/containment behavior.

Each executable child phase should define or map to:
- Summary File, Phase ID, Status
- design references
- patch references or explicit `none`
- objective and why the phase exists
- expected output or user/system-visible result when material
- completion gate or verification gate when material
- implementation-relevant doc/spec constraints when material
- entry conditions/prerequisites
- action checklist and out-of-scope boundaries
- affected artifacts
- TODO and changelog coordination
- Development Verification / TestKit Coverage or equivalent when coding verification materially affects exit criteria
- verification, exit criteria, and closeout summary
- risks/rollback notes
- next possible phases or roadmap/next-goal recommendation, including why/goal/output/gate when future work is meaningful

---

## Live Task-List Linkage Contract

When a phase is active or clearly implied and work is non-trivial, the built-in task list should mirror current phase execution slices and visibly expose the active or implied phase context.

Guidance:
- inspect relevant `/phase` context before shaping/extending tasks; detached generic wording is execution drift
- default tasks to the current active phase before future phases
- if the exact next phase file is absent but phase family/stage is clear, align tasks to that implied structure
- do not let task-list shaping silently allocate a new major phase; use the lineage gate when a phase file is needed
- one phase may have many outcome-sized tasks; each non-trivial phase-backed task should show phase ID, phase name, phase family, or clearly implied stage context in the subject or description, and may carry expected output or gate meaning when that prevents command-only drift
- prefer compact subject linkage such as `P<phase-id>` when no stronger title grammar or shared-board rule blocks it
- when another title grammar makes subject linkage awkward, put `phase_ref`, phase file path, phase name, or equivalent visible linkage in the description instead
- hidden internal phase alignment alone is insufficient for non-trivial phase-backed live tasks
- if a phase-backed task is created or extended without visible phase linkage, update it immediately rather than leaving it as a generic live-tracking item
- extend the current task list for the same objective/phase family instead of recreating it
- task wording should follow the active session language/register; technical labels may remain technical when clearer
- use current phase, phase family, `phase/SUMMARY.md`, `TODO.md`, authored `Next possible phases`, and checked implementation state as bounded execution-discovery surfaces
- authored future-phase context may inform continuity and draft visibility but is not active execution until opened/selected/made active
- if the current phase is complete and the next phase is the implied active path, say the current phase is complete before continuing

---

## Verification, Closeout, and Rollback Contract

Each child phase should define phase-level verification, closeout expectations, and local rollback/containment notes. `phase/SUMMARY.md` still owns end-to-end verification and overall rollback/containment behavior. Patch artifacts must remain outside the live phase-plan namespace.

For phase-backed coding work, child phases should show `Development Verification / TestKit Coverage` or equivalent when verification materially affects exit criteria. Verification depth, debug signal selection, and TestKit/scenario decisions defer to `development-verification-and-debug-strategy.md`.

Phase-backed closeout should report practical delivery, not only files/tasks/audit status: delivered feature/capability/behavior/governance improvement or verification gate; user/system impact; evidence-strength-aligned verification basis; and next phase state when relevant (`not started`, `draft/planned`, `selected`, `active`, `implied-unblocked`, `proposal`, `blocked`, `needs-approval`, or `none opened`). When checked roadmap or goal surfaces show meaningful successor work and continuous execution is not already safely proceeding, closeout should include a compact next-phase/wave/goal recommendation with why it is supported, expected output, and gate. Keep closeout concise and do not force it onto trivial non-phase work.

---

## Verification Checklist
- [ ] God Phase signals were checked, and independent goals/outputs/gates/rollback boundaries were split instead of hidden inside one phase file.

- [ ] `NNN` / `NNN-NN` grammar, required active paths, and `phase/SUMMARY.md` are used
- [ ] major-vs-subphase selection checks lineage before any new major phase
- [ ] subphase selection preserves a bounded goal/output/gate rather than relying only on broad same-domain or historical-family signals
- [ ] phase saturation and umbrella-escape signals are considered before keeping distinct work inside an old major family
- [ ] startup governance establishes or asks about `/phase` before staged/governed drift
- [ ] `phase/history/` and `phase/done/` remain referenced/inactive history, never junk/deletion authority or live namespace
- [ ] sufficiently clear governed design synthesizes into compact phase summary, bounded goal/output/gate-aware roadmap or phase matrix, current child files, and current-phase live tasks without replacing design authority
- [ ] roadmap entries distinguish selected/active work from proposal, blocked, needs-approval, or none-opened states without auto-promoting future work
- [ ] meaningful roadmap or phase-matrix entries expose goal, expected output, and completion gate when that improves execution or closeout
- [ ] patch-derived phase work shows explicit patch linkage and patch artifacts stay outside live phase workspace
- [ ] oversized phase summaries are compacted into current indexes with reachable `phase/history/` and `phase/done/` references instead of retaining duplicate historical detail.
- [ ] child phases include required source references, execution fields, verification, rollback/risks, and closeout
- [ ] phase-backed coding work includes Development Verification / TestKit Coverage or equivalent when material
- [ ] closeout reports delivery, feature/improvement, impact, evidence-strength-aligned verification basis, next phase state, and supported next-phase/wave/goal recommendation when meaningful
- [ ] task creation visibly links to active/implied phase context while authored future-phase context remains non-active until opened/selected

---

## Integration

Related rules:
- [development-verification-and-debug-strategy.md](development-verification-and-debug-strategy.md) - owns phase-backed coding verification strategy, debug signal selection, and TestKit/scenario decisions when material
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup phase posture
- [document-patch-control.md](document-patch-control.md) - patch governance boundary
- [project-documentation-standards.md](project-documentation-standards.md) - repository document model
- [governed-document-rollover-control.md](governed-document-rollover-control.md) - daily-first `phase/SUMMARY.md` / `phase/history/` / `phase/done/` rollover owner
- [todo-standards.md](todo-standards.md) - TODO and live task coordination
- [goal-set-review-and-priority-balance.md](goal-set-review-and-priority-balance.md) - goal-first working frame, goal hierarchy, and next-goal recommendation boundaries
