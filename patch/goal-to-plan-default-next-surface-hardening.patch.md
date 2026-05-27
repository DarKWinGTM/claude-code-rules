# Goal-to-Plan Default Next-Surface Hardening Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.30
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the planned `v10.30 / P122` wave.

It packages one bounded runtime + playground follow-up refinement so selected governed goals not only preserve a bridge into `/plan` when needed, but explicitly recommend `/plan` as the default next surface when route complexity is still materially non-trivial.

---

## Analysis

The released `v10.29 / P121` baseline already hardened the objective-vs-route boundary: `/goal` owns outcome/proof/scope and `/plan` owns route/sequence/task breakdown. That structural separation is correct, but the user wants one more behavioral step.

The remaining gap is practical rather than conceptual. AI can still acknowledge that planning would help while continuing to answer in broad prose instead of explicitly recommending `/plan` as the next working surface. That leaves the cooperation between the two commands weaker than intended.

The better posture is:
- `/goal` stays the objective contract
- `/plan` stays the route contract
- when the selected governed goal is still route-heavy, AI should explicitly recommend `/plan` next
- the recommendation should explain why planning is now the correct next surface without turning plan into a mandatory step for trivial work

This update stays bounded. It does not make `/plan` universal, does not replace candidate-goal doctrine, does not weaken direct continuation, and does not expand the runtime install set.

---

## Change Items

### 1) Explicit `/plan` next-surface recommendation refinement

- **Target artifact:** touched execution owner governing goal framing and next-surface selection
- **Change type:** refinement
- **Current state:** selected governed goals may bridge into `/plan`, but the doctrine does not yet explicitly prefer `/plan` as the default next surface when route complexity remains material
- **Target state:** when the selected governed goal is still route-heavy, AI should explicitly recommend `/plan` rather than leaving the route in generic prose
- **Review point:** preserve direct continuation for simple/bounded goals and avoid turning planning into a universal ritual

### 2) Governed execution-surface recommendation refinement

- **Target artifact:** touched phase/TODO execution owner governing execution surfaces and goal-to-plan handoff
- **Change type:** refinement
- **Current state:** execution surfaces preserve the bridge, but they do not yet make the `/plan` recommendation explicit enough as the default next surface
- **Target state:** goal-linked phase/task/TODO surfaces should make planning the explicit next step when route complexity is materially non-trivial
- **Review point:** preserve goal ownership and do not let route detail blur back into goal text

### 3) Visible recommendation wording refinement

- **Target artifact:** touched presentation/register/wording owners
- **Change type:** refinement
- **Current state:** wording keeps objective and route distinct, but still allows broad prose follow-up where an explicit `/plan` recommendation would be clearer
- **Target state:** visible output should say why `/plan` is next, what it should cover, and why that does not replace the selected goal
- **Review point:** keep the wording concise, advisory, and evidence-shaped rather than ceremonial

### 4) Playground case update

- **Target artifact:** one existing case under `playground/cases/`
- **Change type:** refinement
- **Current state:** current playground coverage shows candidate goals and the goal-to-plan boundary, but it does not yet show the delta from broad prose follow-up into explicit `/plan` recommendation clearly enough
- **Target state:** one updated case visibly shows that a selected governed goal should now recommend `/plan` as the next surface when route complexity remains material
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about objective-vs-route ownership

### 5) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.29 / P121` as the current released baseline with no active wave open
- **Target state:** touched master surfaces open and later close `v10.30 / P122` consistently while preserving the 18-file runtime install scope, governed `/goal` sourcing doctrine, advisory goal posture, and the non-runtime playground boundary
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload

---

## Verification

Required checks before release closeout:
- touched owners explicitly recommend `/plan` as the default next surface when a selected governed goal remains route-heavy
- touched owners preserve `/goal` as objective owner and `/plan` as route owner
- touched owners preserve goal-gate closeout instead of route-completion closeout
- one related playground case is updated with an inspectable behavior delta
- touched release/master surfaces align to `v10.30 / P122`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the updated playground/master surfaces after update
- GitHub release `v10.30` is created and verified before closeout wording claims release completion

---

## Implementation Status

P122 is active.

The checked cooperation gap is established, the bounded improvement direction is selected, and the phase/patch startup artifacts are opened. Owner refinement, companion/changelog sync, playground update, master-surface sync, runtime install-boundary proof, 18/18 parity/body-sufficiency verification, and `git diff --check` are now complete in checked scope. Commit/push/default-branch update, GitHub release verification, and final closeout alignment remain in progress.
