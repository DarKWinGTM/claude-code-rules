# Phase Implementation

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.35
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-31)

---

## P092 Target-State Refinement: Automatic God Phase Handling

Phase governance now treats God Phase detection as an immediate lineage and repair-planning event.

The target state is restructure, subphase split, new major phase, or narrow ambiguity question before phase closeout claims.

---

## Current Target-State Refinement

This design now tightens major-vs-subphase selection so lineage remains evidence rather than a permanent container. A subphase should continue the same bounded goal/output/gate, while a new major phase is appropriate when the work has its own capability, output, verification gate, release boundary, rollback boundary, or when an existing family has become a misleading umbrella.

Roadmap and phase-matrix entries remain goal/output/gate-aware. Meaningful candidate phases should expose the goal they pursue, the expected output or user/system-visible result, the completion or verification gate, dependencies, deliverables, and status. Phase-backed closeout may recommend a supported next phase, wave, or goal after true completion, but only from checked roadmap, design, TODO, phase, or implementation evidence. Proposal/draft entries stay non-active until selected or opened.

---

### Daily Phase History Target

`phase/SUMMARY.md` remains the compact phase roadmap/index. Daily movement and rollover notes may live in `phase/history/YYYY-MM-DD*.md`, and completed phase detail may live in `phase/done/`; active summary content links to those surfaces instead of retaining duplicate historical detail.

## P091 Target-State Refinement: God Phase Prevention

A phase file should represent one bounded execution slice.

When a phase carries independent goals, outputs, verification gates, rollback boundaries, or capability streams, it should not remain one overloaded file.

Repair it by restructuring, splitting into a fitting subphase, or opening a new major phase according to lineage and umbrella-escape rules.

## 1) Goal

Define one deterministic semantic model for phased execution planning so the RULES repository uses one stable active `/phase` structure, may move completed phase detail into `phase/done/` as inactive history, establishes `/phase` early when startup artifact governance already shows phased work is required, synthesizes sufficiently clear governed design into phase execution order and a bounded goal/output/gate-aware roadmap or phase matrix, selects major phases versus subphases through lineage-first criteria with bounded-phase and umbrella-escape safeguards, visibly links non-trivial phase-backed live tasks to active or implied phase context, records material Development Verification / TestKit Coverage for phase-backed coding work, and closes phase-backed work with practical delivery/impact plus meaningful next-phase, wave, or goal recommendation behavior rather than audit-only status.

Multi-session shared-board, plugin, and external coordination/runtime mechanics are outside Main RULES scope.

---

## 2) Scope and Use Boundary

This chain applies when work benefits from explicit staged execution rather than a single linear implementation block.

### 2.1 Use phased planning when
Use phases when one or more of these are true:
- work has multiple execution stages with different entry and exit conditions
- rollout, migration, or verification gates matter between stages
- outputs from one stage are required by a later stage
- rollback or containment boundaries matter during execution
- multiple systems, files, or owners participate in the same change
- the user needs a governed plan that shows how design, TODO, and changelog move together during execution

When those signals make phased work clearly implied rather than merely optional, default phase posture should be treated as `use existing`, `create now`, or `ask now` through startup governance rather than being left implicit until later backfill.
When that staged/phase-shaped context is already clear, live task-list creation should also follow that execution structure provisionally rather than waiting for the exact next phase file to exist first.

### 2.2 Do not use phased planning when
Do not add phases when:
- the work is a single obvious change
- the task is tiny and low-risk
- a normal implementation plan or TODO checklist is enough
- phases would exist only to satisfy template shape
- the plan would invent filler stages that add no execution meaning

### 2.3 Startup establishment bridge
When `artifact-initiation-control` determines phase posture is:
- use existing
- create now
- ask now

that phase posture must be resolved before substantial work drifts.

The preferred path is early phase establishment, not retrospective phase backfill.
When staged or governed execution is already clearly implied by the checked work shape, phase establishment should not be treated as an optional afterthought.

When governed design is sufficiently clear for staged execution, phase should actively derive or update execution order from that normalized design truth. The phase workspace should split design target state into outcome-sized phases by dependency, risk, rollout boundary, expected output, and verification gate; create or update `phase/SUMMARY.md`, a bounded goal/output/gate-aware roadmap or phase matrix, and current child phase files; initialize or extend live tasks for the current phase when non-trivial work begins; and proceed phase-by-phase unless a real stop gate exists. This synthesis remains one-way: phase executes design and does not replace design as target-state authority. Roadmap entries guide continuity and recommendation, but only selected/opened and safe work becomes active execution.

---

## 3) Phase Identity Model

### 3.1 Canonical ID grammar
The active identity model is:
- major phase ID: `NNN`
- subphase ID: `NNN-NN`
- nested child phase ID: `NNN-NN-NN`
- observed alphanumeric forms such as `NNN-NNa` are legacy-only unless a later doctrine explicitly normalizes them
- deeper hybrid forms such as `NNN-NN-NNb` are not forward-valid grammar

### 3.2 Semantic meaning
- `NNN` identifies a top-level execution phase or grouped rollout stage
- `NNN-NN` identifies a child execution slice inside major phase `NNN`
- `NNN-NN-NN` identifies a nested child execution slice inside subphase `NNN-NN` when the work still belongs to the same bounded rollout gate
- hierarchy is expressed by the hyphenated numeric suffix, not by implication or prose alone

### 3.3 Lineage-first phase selection
Before opening a new major phase, the phase owner should inspect checked phase lineage and decide whether the work is better represented as:
- an update to the current active phase
- a new subphase under an existing major family
- a new major phase / rollout family
- an unresolved lineage choice that needs user or evidence clarification

The decision is principle-based rather than subphase-first or major-first. The goal is to preserve real execution lineage without hiding genuinely new rollout families inside an overloaded old phase or trapping distinct work inside a saturated umbrella phase.

### 3.4 Bounded subphase-fit criteria
A new `NNN-NN` subphase is usually a better fit when the work continues the same bounded execution gate inside the same rollout family by refining, repairing, verifying, documenting, installing, releasing, or synchronizing the same governed target without changing the top-level capability boundary.

Strong child-phase signals include:
- same bounded goal/output/gate, verification gate, dependency chain, or rollback boundary
- same governed target where the follow-up keeps the same top-level capability boundary
- direct follow-up from an authored `Next possible phases`, closeout note, TODO item, or phase summary relationship that preserves the same gate meaning
- dependency on a prior phase's output or a need to preserve visible lineage for review
- completed parent or sibling phases whose history still defines the same bounded rollout family rather than only the same broad program area
- current active major phase still needs a bounded child execution slice, making `NNN-NN` the next truthful form
- current active subphase still needs a bounded child execution slice inside that same gate family, making `NNN-NN-NN` the next truthful form

Same product area, broad policy domain, rule owner chain, historical phase label, or project umbrella is supporting evidence only. It is not enough by itself when the new work has a distinct output, verification gate, release boundary, or rollback boundary.

### 3.5 Major-phase-fit and umbrella-escape criteria
A new `NNN` major phase is usually a better fit when the work starts a new top-level rollout family or when an old family would become misleading if extended again.

Strong major-phase and umbrella-escape signals include:
- new first-class rule, policy domain, feature capability, or rollout family
- materially different user-facing objective, governing basis, design target, output, verification gate, release boundary, or rollback boundary
- independent rollout that does not depend on an existing phase family for reviewability
- an existing major family would become misleading, saturated, or overloaded if the new work were nested under it
- many sibling subphases no longer share one clear gate, output, or closeout meaning
- readers cannot tell why the work remains inside the old family without reading historical context
- explicit user direction to start a new program or separate phase family

### 3.6 Ambiguity and no-forced-subphase boundary
Completed status does not automatically break lineage, and new concern wording does not automatically justify a new major phase. Lineage is evidence, not a prison.

If multiple existing phase families plausibly fit and checked lineage does not clearly choose one, the phase owner should preserve uncertainty and ask or record the selected basis instead of inventing a relationship. If no real lineage exists, opening a new major phase is correct. If lineage exists but the old family would become unclear, saturated, or overloaded, a new major phase may still be correct with a visible relation note.

### 3.7 Anti-confusion rules
The active model must not allow these ambiguities:
- `002` must not be used to imply “child of `001`”
- symbolic labels such as `P1/P2/P3` must not replace canonical IDs in active phase semantics
- active normative surfaces must not mix older sparse numbering with the current `NNN` / `NNN-NN` contract
- flat-only examples must not be presented as if they were the only canonical model

---

## 4) `/phase` Workspace Model

### 4.1 Mandatory summary
When phased planning is used, the repository must use:
- `phase/SUMMARY.md`

### 4.2 Canonical file patterns
The active path patterns are:
- major-phase file: `phase/phase-NNN-<phase-name>.md`
- subphase file: `phase/phase-NNN-NN-<subphase-name>.md`
- nested child-phase file: `phase/phase-NNN-NN-NN-<child-phase-name>.md`

Observed alphanumeric forms such as `phase/phase-NNN-NNa-<phase-name>.md` remain legacy-only unless a later doctrine explicitly normalizes them.

Completed phase-detail files may be retained under `phase/done/` using the same phase filename grammar when they are no longer part of the active execution scan surface.

### 4.2.1 Completed phase history surface
`phase/done/` is inactive-by-default phase history.

Required guidance:
- active execution scans start with `phase/SUMMARY.md` and active child phase files in `phase/`
- completed phase files in `phase/done/` are consulted only for history, audit, rollback, provenance, or trace reconstruction
- moving a phase file to `phase/done/` does not make it junk and does not authorize deletion
- `phase/done/` must not become the live phase workspace or a replacement for `phase/SUMMARY.md`

### 4.3 Patch-artifact boundary
Live phased execution files must not be stored under patch artifacts.
Patch artifacts remain outside the live phase-plan namespace.

---

## 5) Summary-and-Child Model

### 5.1 `phase/SUMMARY.md` role
`phase/SUMMARY.md` should keep the global execution picture, including:
- overall context and target state
- risk, constraints, and dependency framing
- major-phase grouping and phase-family lineage when multiple major phases or related subphases exist
- references to live major/subphase files
- references to completed `phase/done/` files only when history/audit/rollback/trace continuity requires them
- summary-level design and patch source inputs when relevant
- TODO/changelog companion coordination when the concern is global
- end-to-end verification requirements
- Development Verification / TestKit Coverage expectations when phase-backed coding verification materially affects exit criteria
- phase closeout expectations for delivered work, feature/improvement, impact, verification basis, next phase state, and goal-qualified next recommendation when meaningful
- goal/output/gate-aware roadmap or phase-matrix entries with status such as active, selected, implied-unblocked, proposal, blocked, needs-approval, or none opened
- overall rollback or containment behavior

### 5.2 Child phase role
Each executable phase file should own one bounded execution slice and make its design/patch inputs reviewable enough for safe progression.

When governed patch artifacts are in scope, the live phase workspace must declare that linkage explicitly rather than leaving patch participation implicit.

---

## 6) Child Phase Field Contract

Each executable child phase file should define or clearly map to:
- Summary File
- Phase ID
- Status
- Design references
- Patch references when patch-derived work exists
- Objective
- Why this phase exists
- Entry conditions / prerequisites
- Action points
- Out of scope
- Affected artifacts
- TODO coordination
- Changelog coordination
- Development Verification / TestKit Coverage when coding verification materially affects exit criteria
- Verification / evidence
- Closeout summary: delivered work, feature/improvement, user/system impact, verification basis, and next phase state when relevant
- Exit criteria
- Risks / rollback notes
- Next possible phases or roadmap recommendation with goal/output/gate when future work is meaningful

### 6.1 Live Task-List Linkage Contract
When a phase is active or clearly implied and the work is non-trivial, the built-in task list should mirror the current phase's execution slices and visibly expose the active or implied phase context.

If `/phase` exists and relevant governed phase context is already available, task creation must inspect that phase context before shaping the live task list.
Task shaping that ignores relevant governed phase context and falls back to detached generic wording or structure should be treated as execution drift rather than as an acceptable default path.

If the exact next phase file does not yet exist, but the checked project/workstream context already makes the current staged or phase family clear, task creation should still follow that implied phase structure provisionally instead of reverting to detached generic standalone task shaping.

Visible linkage may live in the subject or description. The preferred compact form is a subject token such as `P<phase-id>` when no stronger title grammar blocks it. When another title grammar makes subject linkage awkward, use `phase_ref`, phase file path, phase name, phase family, or equivalent description linkage. Hidden internal alignment is not enough for non-trivial phase-backed live tasks.

If `/phase` already contains additional authored planning context, task behavior should use a bounded phase-context hierarchy rather than relying only on the currently open phase file.
That hierarchy is:
1. current active phase
2. current phase family or staged execution lane
3. already-authored bounded next-phase context from `phase/SUMMARY.md`, phase ordering/dependency structure, and the relevant child files' `Next possible phases`

Required guidance:
- when `/phase` exists and relevant governed phase context is available, inspect that phase context before shaping or extending the live task list
- use the current active phase as the default source for live task-list entries
- allow one phase to contain multiple task-list entries when the execution checklist has several real slices
- ensure each non-trivial phase-backed live task visibly carries phase ID, phase name, phase family, or clearly implied stage context in the subject or description
- prefer compact subject linkage such as `P<phase-id>` when no stronger title grammar applies
- use `phase_ref` or equivalent description linkage when subject linkage would conflict with another title grammar
- update any created or extended phase-backed task immediately if it lacks visible phase linkage
- task wording created from phase-linked work should still follow the actual active session language pattern rather than reverting to detached generic phrasing
- if the session is primarily Thai, phase-linked task wording should be Thai-led by default
- if the session naturally uses mixed Thai+English wording, phase-linked task wording should follow that mix rather than being forced into one language
- technical labels may remain in their technical form when forced translation would reduce clarity or make the wording read less naturally
- treat the current phase, the current phase family, and `phase/SUMMARY.md` as execution-discovery surfaces when the next unfinished slice is not fully obvious from the task list alone
- use already-authored `Next possible phases` as bounded planning input when they help clarify continuity, sequencing, or draft next-work visibility
- use checked implementation state alongside the phase workspace when phase text and current repo state together reveal the next unfinished work more clearly than either one alone
- do not jump ahead into future-phase task creation while the current phase or clearly implied current staged context still defines the active execution surface, unless the user explicitly opens that next phase
- when relevant governed phase context exists but task shaping does not follow it, treat that outcome as task-shaping drift rather than as an acceptable generic fallback
- already-authored future-phase context may inform continuity, sequencing, and draft next-work discovery, but it does not become active execution work until that phase is explicitly opened, selected, or otherwise made active by the governing phase context
- if the current phase is already complete, say so directly before opening any draft future-phase tasks

---

## 7) Verification, Closeout, and Rollback Model

Each child phase should define phase-level verification, closeout summary expectations, and local rollback/containment notes. `phase/SUMMARY.md` should keep end-to-end verification and overall rollback or containment behavior visible.

Phase-backed closeout should report what the phase delivered in practical terms before or alongside governance/audit status:
- delivered feature, capability, behavior, governance improvement, or verification gate
- user/system impact or why the change matters
- verification basis at the evidence strength actually checked
- next phase state when relevant: not started, draft/planned, selected, active, implied-unblocked, proposal, blocked, needs-approval, or none opened
- recommended next phase/wave/goal with goal, expected output, and gate when checked roadmap surfaces show meaningful unselected successor work

This shape should remain concise, should not block safe continuation through already selected phases, and should not be forced onto trivial non-phase work.

---

## 8) Verification Checklist

- [ ] `phase-implementation` explicitly defines `NNN`, `NNN-NN`, and `NNN-NN-NN` as forward-valid numeric forms
- [ ] observed alphanumeric forms are classified explicitly as legacy-only or normalized by selected doctrine rather than left ambiguous
- [ ] deeper hybrid forms such as `NNN-NN-NNb` are not silently treated as forward-valid grammar
- [ ] phase identity selection checks lineage before opening a new major phase
- [ ] child-phase use preserves bounded goal/output/gate meaning rather than relying only on same-domain or historical-family evidence
- [ ] umbrella-escape signals are checked when an old major family would become saturated, misleading, or overloaded
- [ ] subphase use remains criteria-based rather than forced by default
- [ ] startup artifact governance establishes or asks about `/phase` before drift when phase is required
- [ ] staged/governed work that clearly implies phase usage is not left without explicit phase posture until late backfill
- [ ] task creation can still align to clearly implied staged/phase context even before the exact next phase file exists
- [ ] non-trivial phase-backed live tasks visibly expose phase ID/name/family/stage context in subject or description
- [ ] sufficiently clear governed design can be synthesized into phase execution order and bounded roadmap/phase matrix without replacing design authority
- [ ] roadmap entries distinguish selected/active work from proposal, blocked, needs-approval, and none-opened states without auto-promotion
- [ ] active examples do not mix sparse `010/020/030` with the new contract
- [ ] symbolic IDs are not used as active canonical phase identifiers
- [ ] `/phase` examples show a valid major/subphase/nested-child model
- [ ] `SUMMARY.md` guidance makes grouping visible when subphases exist
- [ ] active phase scans start with `phase/SUMMARY.md` and active child files before `phase/done/`
- [ ] `phase/done/` is inactive-by-default history, not junk or deletion authority
- [ ] patch artifacts remain outside the live phase workspace
- [ ] phase-backed coding work includes Development Verification / TestKit Coverage or equivalent when verification materially affects exit criteria
- [ ] phase-backed closeout reports delivered work, feature/improvement, impact, verification basis, next phase state, and next-phase recommendation when meaningful

---

## 9) Quality Metrics

| Metric | Target |
|--------|--------|
| Appropriate use of phase planning | High |
| Major-vs-subphase lineage selection quality | High |
| Bounded subphase fit and same-domain-is-not-enough discipline | High |
| New-major bias for related follow-up work | Low |
| Umbrella-phase drift from saturated major families | Low |
| Forced subphase use for unrelated rollout families | Low |
| `/phase` workspace compliance | 100% |
| `SUMMARY.md` presence when phased planning is used | 100% |
| Current-phase-first task-list linkage when a phase is active | High |
| Visible phase linkage in non-trivial phase-backed live tasks | High |
| Startup phase posture resolved before drift when phase is required | 100% |
| Live phased execution files under patch artifacts | 0 |
| Active phase scan bloat from completed phase history | Low |
| Phase closeout delivery/impact clarity | High |
| Roadmap-aware next-phase recommendation after true completion | High when meaningful successor work exists |
| Development Verification / TestKit Coverage visibility in material coding phases | High |

---

## 10) Integration

| Rule | Relationship |
|------|--------------|
| [development-verification-and-debug-strategy.design.md](development-verification-and-debug-strategy.design.md) | Owns coding-time verification strategy, debug signal selection, testing depth, and TestKit/scenario decisions that phase files record when material |
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup owner for establishing or asking about `/phase` |
| [document-patch-control.md](../document-patch-control.md) | Patch-governance boundary outside live phase planning |
| [project-documentation-standards.md](../project-documentation-standards.md) | Repository role model and startup artifact gate |
| [todo-standards.md](../todo-standards.md) | TODO coordination and early-establishment bridge |
| [response-closing-and-action-framing.md](../response-closing-and-action-framing.md) | User-facing roadmap-aware next recommendation and phase-backed closeout framing |

---

> Full history: [../changelog/phase-implementation.changelog.md](../changelog/phase-implementation.changelog.md)
