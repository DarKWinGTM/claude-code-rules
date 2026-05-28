# Goal Internal Native Subagent Assistance Refinement Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [design/design.md](../design/design.md) v10.31
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the released `v10.31 / P123` wave.

It packages one bounded runtime + reference follow-up refinement so `/goal` may stay the only visible objective surface while still gaining conditional internal native subagent assistance for analysis, verification, testing, and bounded plan drafting when the selected governed goal remains non-trivial or route-heavy.

---

## Analysis

The released `v10.30 / P122` baseline already hardened the `/goal` ↔ `/plan` boundary and taught route-heavy selected goals to recommend `/plan` explicitly as the default next surface.

That structural separation is correct, but the user wants one more operational step without increasing visible command complexity. The remaining gap is that `/goal` can still lack enough help in turns where the route is non-trivial, the verification path is broad, or testing/analysis work would benefit from bounded separate context even though the user still wants to stay inside the existing `/goal` pattern.

The better posture is:
- `/goal` stays the objective contract
- `/plan` stays the route contract
- conditional internal native subagent assistance may help `/goal` with analysis, verification, testing, and bounded plan drafting when route complexity remains material
- that help stays internal helper behavior only and must not become a new public owner or completion proof shortcut

This update stays bounded. It does not add a new user-facing command, does not replace `/plan` as the route owner, does not weaken goal-gate closeout, and does not expand the runtime install set.

---

## Change Items

### 1) Goal-owned internal-helper refinement

- **Target artifact:** touched execution owner governing `/goal` behavior, next-surface logic, and worker-assisted continuation
- **Change type:** refinement
- **Current state:** `/goal` may recommend `/plan` when the remaining route is materially non-trivial, but the doctrine does not yet explicitly allow bounded internal native subagent help when the user still wants to stay inside the existing `/goal` surface
- **Target state:** `/goal` may conditionally use internal native subagent assistance for analysis, verification, testing, and bounded plan drafting while still preserving `/goal` objective ownership and `/plan` route ownership
- **Review point:** preserve the current `/goal` ↔ `/plan` boundary and do not let `/goal` become a mini-`/plan`

### 2) Worker-lane helper refinement

- **Target artifact:** touched worker-routing owner governing standalone subagent use, leader verification, and native execution behavior
- **Change type:** refinement
- **Current state:** worker-routing already defines subagent lane contracts and leader-owned verification, but it does not yet explicitly connect those rules to conditional internal-helper use inside governed `/goal` handling
- **Target state:** goal-assisted internal helper lanes are explicit, conditional, minimally scoped, and leader-verified; read-only remains the default where appropriate
- **Review point:** preserve worker findings as input, not proof, and avoid mandatory spawning for trivial work

### 3) Governed execution-surface refinement

- **Target artifact:** touched phase/TODO execution owner governing `/goal` sourcing, phase-backed lanes, and goal-to-plan boundaries
- **Change type:** refinement
- **Current state:** governed execution surfaces already preserve `/goal` objective ownership and `/plan` route ownership, but they do not yet state how bounded internal helper use may support `/goal` without becoming a new visible route surface
- **Target state:** governed execution surfaces allow internal helper use for selected non-trivial goals while keeping plan draft subordinate and `/plan` route ownership intact
- **Review point:** preserve direct continuation for simple goals and avoid new public-pattern drift

### 4) Visible wording refinement

- **Target artifact:** touched presentation/register/wording owners
- **Change type:** refinement
- **Current state:** wording keeps objective and route distinct, but it does not yet clearly express internal helper use, plan draft status, and leader-owned goal proof without risking visible orchestration sprawl
- **Target state:** visible output can expose plan draft and verification/testing route when needed while keeping internal helper behavior subordinate, compact, and evidence-shaped
- **Review point:** keep the wording concise, goal-first, and non-ceremonial rather than turning internal orchestration into the public surface

### 5) Reference-case update

- **Target artifact:** one existing case under `playground/cases/` or a directly related governed reference surface
- **Change type:** refinement
- **Current state:** current goal-related coverage shows candidate goals and `/goal` → `/plan` behavior, but it does not yet show goal-assisted internal helper planning/verification behavior clearly enough to inspect
- **Target state:** one updated case visibly shows the behavior delta from goal-only broad prose into bounded goal-assisted plan draft / verification help while preserving the objective-vs-route boundary
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about helper-vs-owner boundaries

### 6) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.30 / P122` as the current released baseline with no active wave open
- **Target state:** touched master surfaces open and later close `v10.31 / P123` consistently while preserving the 18-file runtime install scope, governed `/goal` sourcing doctrine, goal-to-plan boundary, and non-runtime playground boundary
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload

---

## Verification

Required checks before release closeout:
- touched owners preserve `/goal` as objective owner and `/plan` as route owner
- touched owners allow conditional internal native subagent assistance for analysis, verification, testing, and bounded plan drafting when selected governed goals remain non-trivial or route-heavy
- touched owners keep subagent help as internal helper behavior only rather than a new public owner pattern
- touched owners keep leader-owned synthesis/proof wording and goal-gate closeout instead of worker-output completion wording
- one related playground/reference case is updated with an inspectable behavior delta
- touched release/master surfaces align to `v10.31 / P123`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the updated playground/master surfaces after update
- GitHub release `v10.31` is created and verified before closeout wording claims release completion

---

## Implementation Status

P123 is completed.

The checked workflow gap was established, the bounded improvement direction was selected, and the phase/patch startup artifacts were opened. Touched runtime owner refinement, companion/changelog sync, reference-case update, runtime install-boundary proof, 18/18 parity/body-sufficiency verification, `git diff --check`, commit/push/default-branch verification, GitHub release verification, and final closeout alignment all completed.