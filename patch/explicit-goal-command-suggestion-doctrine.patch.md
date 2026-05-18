# Explicit Goal-Command Suggestion Doctrine Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.15
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.15 / P107`.

It packages a command-shaping refinement so AI can propose concise, high-signal Claude Code `/goal` commands after summaries or next-step recommendations when a bounded successor objective is clear and the proof basis can be surfaced in transcript.

---

## Analysis

The released `v10.14 / P106` wave clarified active-doctrine precedence, but RULES still lacks explicit doctrine for the real `/goal` command.

The first issue is trigger ambiguity: AI has doctrine for next-goal recommendations, but it does not yet know when a supported next goal should be converted into a `/goal` suggestion versus handled through direct continuation.

The second issue is command-shape ambiguity: AI can easily overproduce `/goal` suggestions as long prose or mini-spec dumps instead of using a compact, evaluator-friendly format.

The third issue is sourcing ambiguity: AI needs an explicit rule that `/goal` suggestions come from checked Goal/Output/Gate/Verification surfaces and transcript-visible proof, not from vague intent alone.

---

## Change Items

### 1) `/goal` trigger and no-trigger doctrine

- **Target artifact:** `execution-and-goal-frame.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** RULES supports next-goal recommendations but does not explicitly define when the actual `/goal` command should be suggested.
- **Target state:** RULES explicitly allows `/goal` suggestions only when a bounded successor objective is clear, measurable, provable in transcript, and not better handled through direct continuation.
- **Review point:** preserve continuation-first behavior when safe continuation already exists.

### 2) Compact `/goal` output shape doctrine

- **Target artifact:** `explanation-and-presentation.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** RULES owns recommendation/closing shapes, but not a compact copy-pasteable `/goal` command format.
- **Target state:** RULES defines a compact `Suggested /goal:` shape using outcome, proof, scope, hard guardrails, and stop bound.
- **Review point:** keep `/goal` suggestions short, high-signal, and advisory.

### 3) `/goal` sourcing and wording doctrine

- **Target artifact:** `phase-todo-artifact.md`, `accurate-communication.md`, `communication-register.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** Goal/Output/Gate/Verification surfaces exist, but there is no explicit translation rule into `/goal`, and no explicit pruning/writing guard for command suggestions.
- **Target state:** RULES explicitly derives `/goal` suggestions from checked governed surfaces and constrains them with advisory wording, transcript-visible proof, and high-signal pruning.
- **Review point:** do not introduce fluff, hidden assumptions, or implied selected execution.

### 4) Companion chains and release surfaces

- **Target artifact:** touched owner design/changelog companions plus `README.md`, `design/design.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, P107 phase record, and this patch
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.14 / P106` as the current released wave with no active phase open.
- **Target state:** master surfaces identify `v10.15 / P107` as the active `/goal`-suggestion refinement wave until release verification passes.
- **Review point:** keep runtime install count at 18 and keep the `plugin/` tree observed-only and out of release scope.

---

## Verification

Required checks before release closeout:
- README Bash and PowerShell install arrays contain exactly the same 18 active runtime files.
- All 18 active source runtime files exist and have substantive bodies.
- Touched owner files keep resolvable design and changelog metadata links.
- Active doctrine explicitly states when `/goal` should be suggested and when it should not.
- Active doctrine explicitly defines a compact `/goal` shape based on outcome, proof, scope, hard guardrails, and stop bound.
- Active doctrine explicitly requires transcript-visible proof for `/goal` suggestions.
- Active doctrine explicitly derives `/goal` suggestions from checked Goal/Output/Gate/Verification surfaces.
- `/goal` suggestions remain advisory and high-signal.
- Current P106 chronology/adherence doctrine remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only README-listed active root runtime rules.
- Source/runtime parity and source/destination body sufficiency pass for 18/18 files.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- The untracked `plugin/` tree remains outside staged release scope.
- Git diff has no whitespace errors.
- GitHub release `v10.15` must be created and verified before closeout wording claims release completion.

---

## Implementation Status

P107 is active and not yet released.

Phase/patch startup is open from the released `v10.14 / P106` baseline. `/goal` trigger doctrine, output-shape doctrine, sourcing/writing doctrine, advisory/pruning guards, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, and pre-release master-surface sync are complete in source scope. Push, GitHub release creation, and closeout verification are still pending.

---

## Rollback Approach

If P107 is reversed after release, restore the prior `v10.14 / P106` source state through a governed rollback release while keeping the compact 18-rule runtime install scope unchanged unless an explicit rollback gate selects another install action.

Do not treat the untracked `plugin/` tree, runtime destination extras, or existing history/done/archive surfaces as cleanup targets during rollback.
