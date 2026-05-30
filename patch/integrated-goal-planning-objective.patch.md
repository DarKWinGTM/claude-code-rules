# Integrated Goal-with-Planning Objective Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.33
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the released `v10.33 / P125` wave.

It packages one bounded runtime + reference follow-up refinement so `/goal` and planning work as one integrated surface for governed non-trivial or route-heavy requests: assistant may automatically use internal planning / plan-mode-style support when necessary before final goal emission, while the visible output remains one goal-centric surface and `/plan` remains overflow or explicitly requested route handling only.

---

## Analysis

The unreleased P124 predecessor already moved the system toward pre-goal plan-backed goal authoring. That direction is still useful, but the wording and presentation can still make `/goal` and `/plan` feel like two neighboring outputs: one goal block, one plan block, or a goal followed by a plan handoff.

The better posture is:
- `/goal` stays the objective contract
- internal planning may run automatically when route complexity makes the goal unsafe or vague
- route notes, plan basis, verification route hints, or plan references may appear only as subordinate support inside or adjacent to the goal-centric surface
- `/plan` stays available only when overflow route detail or explicit standalone planning is truly needed
- simple goals still keep the direct `/goal` path
- helper or planning support stays internal/subordinate only and must not become completion proof

This update stays bounded. It does not add a new user-facing command, does not make planning mandatory for every goal, does not replace `/plan` as a route artifact when it is genuinely needed, does not let plan files become objective authority, does not weaken goal-gate closeout, and does not expand the runtime install set.

---

## Change Items

### 1) Integrated goal-with-planning refinement

- **Target artifact:** touched execution owner governing advisory `/goal` construction, route-heavy handling, and selected-goal follow-through
- **Change type:** refinement
- **Current state:** route-heavy governed `/goal` requests may use pre-goal planning support, but the doctrine still leaves room for `/goal` and `/plan` to read like neighboring or staged public outputs
- **Target state:** governed non-trivial or route-heavy `/goal` requests may automatically use internal planning support when necessary, then emit one goal-centric visible surface with subordinate route context while keeping `/plan` for overflow or explicit standalone planning only
- **Review point:** preserve `/goal` objective ownership and do not let the integrated support turn `/goal` into a mini-`/plan`

### 2) Worker-lane integrated support refinement

- **Target artifact:** touched worker-routing owner governing standalone subagent use, leader verification, and native execution behavior
- **Change type:** refinement
- **Current state:** worker-routing already defines goal-owned helper lanes and pre-goal planning help, but it still frames that help as a distinct planning stage more than as integrated goal authoring support
- **Target state:** analysis, route drafting, verification ordering, testing, and optional plan-file reference synthesis are explicit as integrated goal-authoring help; helper outputs remain subordinate, leader-normalized, and non-proof
- **Review point:** preserve worker findings as input, not proof, and avoid mandatory spawning for trivial work

### 3) Governed execution-surface refinement

- **Target artifact:** touched phase/TODO execution owner governing `/goal` sourcing, phase-backed lanes, and goal-to-plan boundaries
- **Change type:** refinement
- **Current state:** governed execution surfaces allow conditional plan-backed goal authoring, but still explicitly teach `/plan` as the normal next surface for route-heavy selected goals
- **Target state:** governed execution surfaces teach one integrated goal-with-planning surface first; `/plan` becomes overflow or explicitly requested route handling only after the selected goal exists and standalone route detail is genuinely needed
- **Review point:** preserve direct continuation for simple goals and avoid new public-pattern drift

### 4) Visible wording refinement

- **Target artifact:** touched presentation/register owners
- **Change type:** refinement
- **Current state:** wording keeps objective and route distinct, but still reads naturally as one `/goal` output plus a neighboring `/plan` recommendation or support block
- **Target state:** visible output presents one goal-centric block, with any planning help clearly subordinate, compact, and non-competing; `/plan` is never phrased as a second equal recommendation in the same moment
- **Review point:** keep the wording concise, goal-first, and non-ceremonial rather than turning internal planning into a public second surface

### 5) Reference-case update

- **Target artifact:** one existing case under `playground/cases/` or a directly related governed reference surface
- **Change type:** refinement
- **Current state:** current goal-related coverage shows candidate goals plus helper/planning support, but still leaves room for the sequence to read as goal first, plan second
- **Target state:** one updated case visibly shows candidate goals leading into one advisory `/goal` with integrated planning support and no separate `/plan` block unless overflow route detail is genuinely needed
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about helper-vs-owner boundaries

### 6) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.32 / P124` as the active target, while latest released baseline remains `v10.31 / P123`
- **Target state:** touched master surfaces open and later close `v10.33 / P125` consistently, preserve the 18-file runtime install scope, teach the integrated goal-with-planning target model, keep `/plan` out of ordinary paired output, and preserve the non-runtime playground boundary
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload

---

## Verification

Required checks before release closeout:
- touched owners preserve `/goal` as objective owner while integrated planning support stays subordinate route context only
- touched owners allow automatic internal planning / plan-mode-style support only when route complexity truly requires it
- touched owners keep simple-goal `/goal` emission direct instead of forcing planning for every goal
- touched owners no longer teach `/plan` as the ordinary paired next-step surface for route-heavy goal requests
- touched owners keep `/plan` and any plan file as overflow or explicitly requested route artifacts only
- one related playground/reference case is updated with an inspectable integrated-goal-with-planning behavior delta
- touched release/master surfaces align to `v10.33 / P125`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the updated playground/master surfaces after update
- GitHub release `v10.33` is created and verified before closeout wording claims release completion

---

## Implementation Status

P125 is completed.

The checked workflow gap was established, the bounded improvement direction was selected, and the phase/patch startup artifacts were opened. Touched runtime owner refinement, companion/changelog sync, reference-case update, runtime install-boundary proof, 18/18 parity/body-sufficiency verification, `git diff --check`, commit/push/default-branch verification, GitHub release verification, and final closeout alignment all completed.
