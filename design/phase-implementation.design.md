# Phase Implementation

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.25
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-04-29)

---

## 1) Goal

Define one deterministic semantic model for phased execution planning so the RULES repository uses one stable active `/phase` structure, may move completed phase detail into `phase/done/` as inactive history, establishes `/phase` early when startup artifact governance already shows phased work is required, synthesizes sufficiently clear governed design into phase execution order, and closes phase-backed work with practical delivery/impact reporting rather than audit-only status.

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

When governed design is sufficiently clear for staged execution, phase should actively derive or update execution order from that normalized design truth. The phase workspace should split design target state into outcome-sized phases by dependency, risk, rollout boundary, and verification gate; create or update `phase/SUMMARY.md` and current child phase files; initialize or extend live tasks for the current phase when non-trivial work begins; and proceed phase-by-phase unless a real stop gate exists. This synthesis remains one-way: phase executes design and does not replace design as target-state authority.

---

## 3) Phase Identity Model

### 3.1 Canonical ID grammar
The active identity model is:
- major phase ID: `NNN`
- subphase ID: `NNN-NN`

### 3.2 Semantic meaning
- `NNN` identifies a top-level execution phase or grouped rollout stage
- `NNN-NN` identifies a child execution slice inside major phase `NNN`
- hierarchy is expressed by the hyphenated suffix, not by implication or prose alone

### 3.3 Anti-confusion rules
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
- major-phase grouping when multiple major phases exist
- references to live major/subphase files
- references to completed `phase/done/` files only when history/audit/rollback/trace continuity requires them
- summary-level design and patch source inputs when relevant
- TODO/changelog companion coordination when the concern is global
- end-to-end verification requirements
- phase closeout expectations for delivered work, feature/improvement, impact, verification basis, and next phase state when relevant
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
- Verification / evidence
- Closeout summary: delivered work, feature/improvement, user/system impact, verification basis, and next phase state when relevant
- Exit criteria
- Risks / rollback notes
- Next possible phases

### 6.1 Live Task-List Linkage Contract
When a phase is active and the work is non-trivial, the built-in task list should mirror the current phase's execution slices.

If `/phase` exists and relevant governed phase context is already available, task creation must inspect that phase context before shaping the live task list.
Task shaping that ignores relevant governed phase context and falls back to detached generic wording or structure should be treated as execution drift rather than as an acceptable default path.

If the exact next phase file does not yet exist, but the checked project/workstream context already makes the current staged or phase family clear, task creation should still follow that implied phase structure provisionally instead of reverting to detached generic standalone task shaping.

If `/phase` already contains additional authored planning context, task behavior should use a bounded phase-context hierarchy rather than relying only on the currently open phase file.
That hierarchy is:
1. current active phase
2. current phase family or staged execution lane
3. already-authored bounded next-phase context from `phase/SUMMARY.md`, phase ordering/dependency structure, and the relevant child files' `Next possible phases`

Required guidance:
- when `/phase` exists and relevant governed phase context is available, inspect that phase context before shaping or extending the live task list
- use the current active phase as the default source for live task-list entries
- allow one phase to contain multiple task-list entries when the execution checklist has several real slices
- prefer task subjects that include the current phase ID when that improves clarity
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
- next phase state when relevant: not started, draft/planned, selected, active, or none opened

This shape should remain concise and should not be forced onto trivial non-phase work.

---

## 8) Verification Checklist

- [ ] `phase-implementation` explicitly defines `NNN` and `NNN-NN`
- [ ] startup artifact governance establishes or asks about `/phase` before drift when phase is required
- [ ] staged/governed work that clearly implies phase usage is not left without explicit phase posture until late backfill
- [ ] task creation can still align to clearly implied staged/phase context even before the exact next phase file exists
- [ ] sufficiently clear governed design can be synthesized into phase execution order without replacing design authority
- [ ] active examples do not mix sparse `010/020/030` with the new contract
- [ ] symbolic IDs are not used as active canonical phase identifiers
- [ ] `/phase` examples show a valid major/subphase model
- [ ] `SUMMARY.md` guidance makes grouping visible when subphases exist
- [ ] active phase scans start with `phase/SUMMARY.md` and active child files before `phase/done/`
- [ ] `phase/done/` is inactive-by-default history, not junk or deletion authority
- [ ] patch artifacts remain outside the live phase workspace
- [ ] phase-backed closeout reports delivered work, feature/improvement, impact, verification basis, and next phase state when relevant

---

## 9) Quality Metrics

| Metric | Target |
|--------|--------|
| Appropriate use of phase planning | High |
| `/phase` workspace compliance | 100% |
| `SUMMARY.md` presence when phased planning is used | 100% |
| Current-phase-first task-list linkage when a phase is active | High |
| Startup phase posture resolved before drift when phase is required | 100% |
| Live phased execution files under patch artifacts | 0 |
| Active phase scan bloat from completed phase history | Low |
| Phase closeout delivery/impact clarity | High |

---

## 10) Integration

| Rule | Relationship |
|------|--------------|
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup owner for establishing or asking about `/phase` |
| [document-patch-control.md](../document-patch-control.md) | Patch-governance boundary outside live phase planning |
| [project-documentation-standards.md](../project-documentation-standards.md) | Repository role model and startup artifact gate |
| [todo-standards.md](../todo-standards.md) | TODO coordination and early-establishment bridge |

---

> Full history: [../changelog/phase-implementation.changelog.md](../changelog/phase-implementation.changelog.md)
