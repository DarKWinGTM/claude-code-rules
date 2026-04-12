# Phase Implementation

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 2.11
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-12)

---

## 1) Goal

Define one deterministic semantic model for phased execution planning so the RULES repository uses one stable `/phase` structure and establishes `/phase` early when startup artifact governance already shows phased work is required.

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
- summary-level design and patch source inputs when relevant
- TODO/changelog companion coordination when the concern is global
- end-to-end verification requirements
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
- Exit criteria
- Risks / rollback notes
- Next possible phases

### 6.1 Live Task-List Linkage Contract
When a phase is active and the work is non-trivial, the built-in task list should mirror the current phase's execution slices.

Required guidance:
- use the current active phase as the default source for live task-list entries
- allow one phase to contain multiple task-list entries when the execution checklist has several real slices
- prefer task subjects that include the current phase ID when that improves clarity
- treat the current phase and `phase/SUMMARY.md` as execution-discovery surfaces when the task list alone is not enough to reveal the next unfinished slice
- use checked implementation state alongside the phase workspace when that combination clarifies the next unfinished work more accurately
- do not jump ahead into future-phase task creation while the current phase still defines the active execution surface, unless the user explicitly opens that next phase
- if the current phase is already complete, say so directly before opening any draft future-phase tasks

---

## 7) Verification Checklist

- [ ] `phase-implementation` explicitly defines `NNN` and `NNN-NN`
- [ ] startup artifact governance establishes or asks about `/phase` before drift when phase is required
- [ ] active examples do not mix sparse `010/020/030` with the new contract
- [ ] symbolic IDs are not used as active canonical phase identifiers
- [ ] `/phase` examples show a valid major/subphase model
- [ ] `SUMMARY.md` guidance makes grouping visible when subphases exist
- [ ] patch artifacts remain outside the live phase workspace

---

## 8) Quality Metrics

| Metric | Target |
|--------|--------|
| Appropriate use of phase planning | High |
| `/phase` workspace compliance | 100% |
| `SUMMARY.md` presence when phased planning is used | 100% |
| Current-phase-first task-list linkage when a phase is active | High |
| Startup phase posture resolved before drift when phase is required | 100% |
| Live phased execution files under patch artifacts | 0 |

---

## 9) Integration

| Rule | Relationship |
|------|--------------|
| [artifact-initiation-control.md](../artifact-initiation-control.md) | Startup owner for establishing or asking about `/phase` |
| [document-patch-control.md](../document-patch-control.md) | Patch-governance boundary outside live phase planning |
| [project-documentation-standards.md](../project-documentation-standards.md) | Repository role model and startup artifact gate |
| [todo-standards.md](../todo-standards.md) | TODO coordination and early-establishment bridge |

---

> Full history: [../changelog/phase-implementation.changelog.md](../changelog/phase-implementation.changelog.md)
