# Goal-to-Plan Bridge Doctrine Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active / In Progress
> **Target Design:** [design/design.md](../design/design.md) v10.29
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the planned `v10.29 / P121` wave.

It packages one bounded runtime + playground follow-up refinement so `/goal` keeps ownership of the objective layer, `/plan` keeps ownership of the route layer, and goal closeout returns to the goal gate instead of treating finished plan steps as sufficient proof by themselves.

---

## Analysis

The released `v10.28 / P120` baseline already hardened strategic correction posture, but the current doctrine still leaves one structural gap around `/goal` and `/plan`.

The remaining miss is not about whether `/goal` should exist; that part is already strong. The miss is that the doctrine still under-specifies how a selected goal should relate to planning. Without a sharper bridge, AI can either inflate `/goal` into a hidden route document or collapse `/plan` completion into premature goal completion.

The better posture is to keep the layers explicit:
- `/goal` owns objective, done condition, proof, and scope
- `/plan` owns route, sequencing, and task breakdown
- the bridge into `/plan` is evidence- and complexity-shaped, not universal
- closeout must prove the goal gate, not only the route progress

This update stays bounded. It does not make `/plan` mandatory for every goal, does not replace existing governed `/goal` sourcing doctrine, does not weaken direct continuation or candidate-goal behavior, and does not expand the runtime install set.

---

## Change Items

### 1) Objective-vs-route doctrine refinement

- **Target artifact:** touched execution owner governing goal framing and continuation
- **Change type:** refinement
- **Current state:** `/goal` successor suggestion doctrine exists, but selected-goal objective ownership and `/plan` route ownership are still under-specified
- **Target state:** `/goal` explicitly owns objective/done/proof/scope, while `/plan` explicitly owns route/sequence/task breakdown
- **Review point:** preserve the existing governed `/goal` bridge and do not let `/goal` become a mini-plan

### 2) Non-trivial goal-to-plan bridge refinement

- **Target artifact:** touched phase/TODO execution owner governing governed execution surfaces and `/goal` sourcing
- **Change type:** refinement
- **Current state:** governed `/goal` sourcing exists, but the rule does not yet explicitly teach when a selected governed goal should bridge into `/plan`
- **Target state:** non-trivial governed goals may bridge into `/plan` when scope, ambiguity, risk, or multi-step execution makes route selection material; trivial goals remain allowed to execute without a mandatory plan step
- **Review point:** preserve design-first sourcing and avoid forcing `/plan` into trivial or clearly direct continuation paths

### 3) Goal-gate closeout refinement

- **Target artifact:** touched communication/presentation owners governing visible wording and completion framing
- **Change type:** refinement
- **Current state:** advisory `/goal` wording and closeout wording exist, but they do not yet explicitly guard against treating completed plan steps as sufficient proof of goal completion
- **Target state:** wording should keep objective and route distinct, and closeout should explicitly return to the goal gate when that distinction matters
- **Review point:** preserve evidence-calibrated wording and avoid turning the rule into a ceremonial wording ritual

### 4) Playground case update

- **Target artifact:** one existing case under `playground/cases/`
- **Change type:** refinement
- **Current state:** current playground cases cover successor surfacing, language alignment, and evidence/portability boundaries, but they do not yet inspect the selected-goal objective-vs-plan-route failure mode directly enough
- **Target state:** one updated case visibly shows the behavior delta from goal-as-mini-plan or plan-equals-done drift into objective-first goal ownership plus non-trivial route bridging
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about the boundary between objective, route, and closeout proof

### 5) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.28 / P120` as the current released baseline with no active wave open
- **Target state:** touched master surfaces open and later close `v10.29 / P121` consistently while preserving the 18-file runtime install scope, governed `/goal` sourcing discipline, advisory `/goal` posture, and the non-runtime playground boundary
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload

---

## Verification

Required checks before release closeout:
- touched owners encode explicit objective-vs-route separation rather than leaving `/goal` and `/plan` as partially overlapping surfaces
- touched owners allow `/plan` bridging for non-trivial governed goals without turning it into a universal requirement
- touched owners make goal-gate verification the closeout owner rather than treating plan completion alone as sufficient proof
- one related playground case is updated with an inspectable behavior delta
- touched release/master surfaces align to `v10.29 / P121`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- remote default branch shows the updated playground/master surfaces after update
- GitHub release `v10.29` is created and verified before closeout wording claims release completion

---

## Implementation Status

P121 is active.

The checked structural gap is established, the bounded improvement direction is selected, and the phase/patch startup artifacts are opened. Owner refinement, companion/changelog sync, playground update, master-surface sync, runtime install-boundary proof, 18/18 parity/body-sufficiency verification, and `git diff --check` are now complete in checked scope. Commit/push/default-branch update, GitHub release verification, and final closeout alignment remain in progress.
