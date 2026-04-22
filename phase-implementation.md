# Phase Implementation

> **Current Version:** 2.19
> **Design:** [design/phase-implementation.design.md](design/phase-implementation.design.md) v2.19
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/phase-implementation.changelog.md](changelog/phase-implementation.changelog.md)

---

## Rule Statement

**Core Principle: Use phased planning only when staged execution meaningfully improves clarity, require phased work to use a dedicated `/phase` workspace with mandatory `SUMMARY.md` plus deterministic major/subphase IDs, establish `/phase` early when startup artifact governance already shows phased work is required, and declare governed patch participation explicitly when patch is in scope.**

This rule defines the semantic standard for phase planning. The governed summary/index lives in `/phase/SUMMARY.md`, executable phase detail lives in `/phase/phase-NNN-*.md` or `/phase/phase-NNN-NN-*.md`, design remains target-state authority, patch remains governed change/review authority as explicit before/after change artifacts, and the root helper remains a non-governed drafting aid.

Multi-session shared-board, plugin, and external coordination/runtime mechanics stay outside Main RULES current doctrine.

---

## Core Requirements

### 1) Purpose and Authority Boundary

`phase-implementation.md` defines:
- what phase planning is for
- when phased planning should and should not be used
- what `/phase` structure should look like
- the active phase-identity grammar
- what semantic fields a child phase file should contain
- how design references should be mapped into each phase
- how governed patch references should be mapped into each phase when patch-derived work matters
- how cross-phase handoffs, verification, TODO coordination, changelog coordination, and rollback boundaries should be expressed
- how live phase planning may synthesize one-way source inputs from design and relevant patch artifacts without becoming a source-of-truth layer

It does **not** replace:
- `phase/SUMMARY.md` as the governed summary/index for the active phased execution plan
- child phase files as the governed phase-local execution detail
- `design/*.design.md` as target-state authority
- `patch/<context>.patch.md` or root `<context>.patch.md` as governed patch/review authority
- `TODO.md` as execution tracking
- `changelog/*.changelog.md` as history
- `artifact-initiation-control.md` as the startup owner that decides whether `/phase` must be established now

### 2) When to Use Phase Planning

Use phased planning when one or more of these are true:
- work must happen in distinct stages with different entry and exit conditions
- rollout, migration, or verification gates matter between stages
- outputs from one stage are required by a later stage
- rollback or containment boundaries matter during execution
- the change spans multiple systems, files, or owners and benefits from staged coordination
- the project needs a governed plan that shows how design, TODO, and changelog move together during execution

When those signals make phased work clearly implied rather than merely optional, default phase posture should be treated as `use existing`, `create now`, or `ask now` through startup governance rather than being left implicit until later backfill.
When that staged/phase-shaped context is already clear, live task-list creation should also follow that execution structure provisionally rather than waiting for the exact next phase file to exist first.

### 3) Startup Bridge for Phase Establishment

If `artifact-initiation-control` resolves phase posture as:
- use existing
- create now
- ask now

then phase posture must be handled before substantial work drifts.

Required guidance:
- if phase is clearly required, establish `/phase` early rather than backfilling it later
- when staged or governed execution is already clearly implied by the checked work shape, do not treat phase establishment as an optional afterthought
- if phase need is still ambiguous, ask immediately before detailed work continues
- retrospective phase creation is a repair path, not the preferred operating path

### 4) When Not to Use Phase Planning

Do not force phases when:
- the work is a single obvious change
- a normal implementation plan or TODO checklist is enough
- the task is tiny and low-risk
- phases would only exist to satisfy template shape
- the plan would invent filler stages that add no execution meaning

### 5) Phase Identity Model

#### 5.1 Canonical ID grammar
The active identity model is:
- major phase ID: `NNN`
- subphase ID: `NNN-NN`

#### 5.2 Semantic meaning
- `NNN` identifies a top-level execution phase or grouped rollout stage
- `NNN-NN` identifies a child execution slice inside major phase `NNN`
- hierarchy is expressed by the hyphenated suffix, not by implication or prose alone

#### 5.3 Numbering behavior
- zero-padded lexical ordering remains preferred
- major phases may be merged, split, skipped, repeated, or reordered when project reality requires it
- subphases may exist only where execution meaning justifies them
- subphases are optional, not mandatory for every major phase

### 6) Mandatory `/phase` File Model

When phased planning is used, the repository must use:
- `phase/SUMMARY.md`
- executable phase files under `phase/`

The active path patterns are:
- major-phase file: `phase/phase-NNN-<phase-name>.md`
- subphase file: `phase/phase-NNN-NN-<subphase-name>.md`

`SUMMARY.md` is mandatory.
Live phased execution files inside patch artifacts are **not allowed**.

### 7) Source-input synthesis boundary
`/phase` is the live execution synthesis layer, not a new source-of-truth layer.

Phase planning may consume:
- `design/*.design.md` as target-state inputs
- `patch/<context>.patch.md` or root `<context>.patch.md` as governed change/review inputs when patch-derived work matters

This direction is one-way:
- phase artifacts may cite and synthesize design and patch inputs
- design and patch artifacts are not required to point back to phase
- using patch input does not move live execution planning into patch artifacts
- using design input does not turn phase into target-state authority

### 7.1 Explicit phase-to-patch linkage rule

When phased work uses a governed patch artifact, the live phase workspace must declare that linkage explicitly.

Required guidance:
- `phase/SUMMARY.md` must name the governing patch artifact(s) for the relevant phase, or explicitly state that no governed patch artifact is available yet
- each child phase file that uses patch-derived work must include a `Patch References` field naming the applicable patch artifact(s), or explicit `none`
- use `none` only when patch is truly not required for that phase, not as a placeholder for an unresolved decision
- this requirement does not create a reverse-link requirement from patch back to phase, though projects may still add such links if helpful

### 8) `SUMMARY.md` Responsibilities
`phase/SUMMARY.md` should keep the global execution picture, including:
- overall context and target state
- analysis of risk, constraints, and dependencies
- a phase map or phase index
- references to live major/subphase files
- summary-level source inputs from design and patch artifacts when relevant
- explicit governing patch artifact references for phases where patch is in scope, or explicit `none` when patch is genuinely not required
- cross-phase handoffs and dependency rules
- overall TODO/changelog coordination when the concern is global
- end-to-end verification requirements
- overall rollback or containment behavior

### 9) Stable Child Phase Field Contract
Each executable child phase file should define, or clearly map to:
- Summary File reference
- Phase ID
- Status
- Design references
- Patch references (required when patch-derived work exists; otherwise explicit `none`)
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

### 9.1 Live Task-List Linkage Contract
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
- when repeated slices still belong to the same active objective/phase family, extend the current task-list surface instead of recreating it
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
- if the current phase is already complete and the next phase is already the implied active path, phase-boundary continuity may continue directly instead of turning completion into a report-only stop
- if the current phase is already complete, say so directly before opening any draft future-phase tasks

### 10) Verification and Rollback Contract
Phased planning must preserve both local and global safety:
- each executable child phase file should define phase-level verification
- each executable child phase file should define local rollback or containment notes
- `phase/SUMMARY.md` must still define end-to-end verification
- `phase/SUMMARY.md` must still define overall rollback or containment behavior

### 11) Patch-artifact boundary
Patch artifacts are not the live phase-plan namespace.
If patch documents exist, they remain patch artifacts and must not be used as the location for live phased execution planning.

---

## Verification Checklist

- [ ] `phase-implementation` explicitly defines `NNN` and `NNN-NN`
- [ ] startup artifact governance establishes or asks about `/phase` before drift when phase is required
- [ ] staged/governed work that clearly implies phase usage is not left without explicit phase posture until late backfill
- [ ] task creation can still align to clearly implied staged/phase context even before the exact next phase file exists
- [ ] already-authored next-phase context can inform continuity and draft next-work discovery without being silently promoted into active execution
- [ ] active examples do not mix sparse `010/020/030` with the new contract
- [ ] symbolic IDs such as `P1/P2/P3` are not used as active canonical phase identifiers
- [ ] `/phase` examples show either a valid major-phase file, a valid subphase file, or both
- [ ] `SUMMARY.md` guidance makes parent-child grouping visible when subphases exist
- [ ] child phase-file guidance uses canonical IDs in dependencies and examples
- [ ] phased work with governed patch artifacts shows explicit patch linkage in `phase/SUMMARY.md` and relevant child phase files
- [ ] patch artifacts remain outside the live phase workspace

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Appropriate use of phase planning | High |
| `/phase` workspace compliance | 100% |
| `SUMMARY.md` presence when phased planning is used | 100% |
| Design traceability coverage | 100% when design input is used |
| Patch traceability coverage | 100% when patch-derived work is used |
| Explicit phase-to-patch linkage coverage | 100% when patch is in scope |
| Current-phase-first task-list linkage when a phase is active | High |
| Startup phase posture resolved before drift when phase is required | 100% |
| Live phased execution files inside patch artifacts | 0 |

---

## Integration

Related rules:
- [artifact-initiation-control.md](artifact-initiation-control.md) - startup owner for establishing or asking about `/phase`
- [document-patch-control.md](document-patch-control.md) - patch governance boundary outside live phase planning
- [project-documentation-standards.md](project-documentation-standards.md) - repository role model and startup artifact gate
- [todo-standards.md](todo-standards.md) - TODO coordination and early establishment bridge

---

> **Full history:** [changelog/phase-implementation.changelog.md](changelog/phase-implementation.changelog.md)
