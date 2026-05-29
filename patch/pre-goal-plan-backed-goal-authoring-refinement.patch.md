# Pre-goal Plan-backed Goal Authoring Refinement Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.32
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the planned `v10.32 / P124` wave.

It packages one bounded runtime + reference follow-up refinement so advisory `/goal` creation for governed non-trivial or route-heavy work may conditionally run an internal pre-goal planning pass before final goal emission, with optional native subagent help for analysis, route drafting, verification ordering, and plan-file reference synthesis when that route basis materially improves the emitted goal.

---

## Analysis

The released `v10.31 / P123` baseline already hardened the selected-goal boundary so `/goal` can keep objective ownership while conditional internal helper output supports analysis, verification, testing, and bounded plan drafting inside selected governed work.

That structural separation is still correct, but the user wants one step earlier in the workflow. The remaining gap is that governed `/goal` authoring itself can still happen before enough route synthesis exists, then only later bridge into `/plan` or helper output. The user wants the internal planning work to happen before the command is emitted, so the surfaced `/goal` already reflects a better route basis without turning `/plan` or a plan file into the objective owner.

The better posture is:
- `/goal` stays the objective contract
- `/plan` stays the route contract
- a conditional internal pre-goal planning pass may synthesize route basis before advisory `/goal` emission when route complexity remains material
- optional plan file output stays a route artifact and reference surface only
- simple goals still keep the direct `/goal` path
- that help stays internal planning behavior only and must not become a new public owner or completion proof shortcut

This update stays bounded. It does not add a new user-facing command, does not replace `/plan` as the route owner, does not force pre-planning for every goal, does not let plan files become objective authority, does not weaken goal-gate closeout, and does not expand the runtime install set.

---

## Change Items

### 1) Goal-owned pre-goal planning-pass refinement

- **Target artifact:** touched execution owner governing advisory `/goal` construction, next-surface logic, and worker-assisted continuation
- **Change type:** refinement
- **Current state:** selected governed goals may already receive conditional internal helper output after the goal is selected, but the doctrine does not yet explicitly allow route synthesis before the advisory `/goal` is emitted
- **Target state:** governed non-trivial or route-heavy `/goal` creation may conditionally use an internal pre-goal planning pass so the emitted `/goal` is already shaped by route analysis while still preserving `/goal` objective ownership and `/plan` route ownership
- **Review point:** preserve the `/goal` ↔ `/plan` boundary and do not let pre-goal planning pass make `/goal` a mini-`/plan`

### 2) Worker-lane pre-goal helper refinement

- **Target artifact:** touched worker-routing owner governing standalone subagent use, leader verification, and native execution behavior
- **Change type:** refinement
- **Current state:** worker-routing already defines goal-owned helper lanes after selection, but it does not yet explicitly connect those rules to conditional pre-goal planning-pass support before advisory `/goal` emission
- **Target state:** pre-goal helper lanes for analysis, route drafting, verification ordering, and optional plan-file reference synthesis are explicit, conditional, minimally scoped, and leader-normalized; read-only remains the default where appropriate
- **Review point:** preserve worker findings as input, not proof, and avoid mandatory spawning for trivial work

### 3) Governed execution-surface refinement

- **Target artifact:** touched phase/TODO execution owner governing `/goal` sourcing, phase-backed lanes, and goal-to-plan boundaries
- **Change type:** refinement
- **Current state:** governed execution surfaces already preserve `/goal` objective ownership and `/plan` route ownership after a goal is selected, but they do not yet state how conditional planning-pass output may shape the emitted `/goal` before selection without making the plan file a new visible owner
- **Target state:** governed execution surfaces allow conditional plan-backed goal authoring with optional plan-file references while keeping `/goal` as the objective contract, `/plan` as the route owner, and plan file behavior reference-only
- **Review point:** preserve direct continuation for simple goals and avoid new public-pattern drift

### 4) Visible wording refinement

- **Target artifact:** touched presentation/register/wording owners
- **Change type:** refinement
- **Current state:** wording keeps objective and route distinct after the selected goal exists, but it does not yet clearly express pre-goal planning pass, plan reference status, and leader-owned goal proof without risking visible orchestration sprawl
- **Target state:** visible output can expose plan-backed goal authoring, compact plan reference, and route basis when needed while keeping internal planning behavior subordinate, compact, and evidence-shaped
- **Review point:** keep the wording concise, goal-first, and non-ceremonial rather than turning internal planning into the public surface

### 5) Reference-case update

- **Target artifact:** one existing case under `playground/cases/` or a directly related governed reference surface
- **Change type:** refinement
- **Current state:** current goal-related coverage shows candidate goals plus selected-goal helper support, but it does not yet show the pre-goal planning-pass behavior clearly enough to inspect
- **Target state:** one updated case visibly shows the behavior delta from immediate `/goal` emission into conditional plan-backed goal authoring with optional plan reference while preserving the objective-vs-route boundary
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about helper-vs-owner boundaries

### 6) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.31 / P123` as the current released baseline with no active wave open
- **Target state:** touched master surfaces open and later close `v10.32 / P124` consistently while preserving the 18-file runtime install scope, governed `/goal` sourcing doctrine, goal-to-plan boundary, plan-file reference-only boundary, and non-runtime playground boundary
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload

---

## Verification

Required checks before release closeout:
- touched owners preserve `/goal` as objective owner while `/plan` and any plan file remain route artifacts only
- touched owners allow a conditional internal pre-goal planning pass for analysis, route drafting, verification ordering, and optional plan-file reference synthesis when governed work remains non-trivial or route-heavy
- touched owners keep simple-goal `/goal` emission direct instead of forcing pre-planning for every goal
- touched owners keep helper/planning support as internal subordinate behavior only rather than a new public owner pattern
- touched owners keep leader-owned normalization/synthesis/proof wording and goal-gate closeout instead of helper-output or plan-file completion wording
- one related playground/reference case is updated with an inspectable behavior delta
- touched release/master surfaces align to `v10.32 / P124`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the updated playground/master surfaces after update
- GitHub release `v10.32` is created and verified before closeout wording claims release completion

---

## Implementation Status

P124 is active.

The checked workflow gap and the bounded improvement direction are established, and the phase/patch startup artifacts are opened. Touched runtime owner refinement, companion/changelog sync, reference-case update, runtime install-boundary proof, 18/18 parity/body-sufficiency verification, `git diff --check`, commit/push/default-branch verification, GitHub release verification, and final closeout alignment remain in progress.
