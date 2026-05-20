# End-to-End Language-Aligned Goal Surface Refinement Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** In progress
> **Target Design:** [design/design.md](../design/design.md) v10.24
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.24 / P116`.

It packages a focused runtime + playground refinement so dominant-session-language behavior controls the full visible goal surface rather than only the promoted command body.

---

## Analysis

The runtime doctrine released in `v10.22 / P114` already says candidate goals and promoted `/goal` wording should follow the dominant session language, and `v10.23 / P115` made that doctrine inspectable as one governed non-runtime playground family.

The remaining gap is surface-level consistency: some output templates, slot labels, and wrapper examples still encode English-first wording such as `Suggested /goal:` or `Done when`, which can still produce English-shell + Thai-content output even when the user's working language is Thai-first.

This update stays narrow. It does not reopen the governed-work-only `/goal` bridge, does not turn advisory `/goal` into selected execution, and does not expand the runtime install set. It refines the language surface, adds one new playground case family, and syncs the directly affected governing/master surfaces.

---

## Change Items

### 1) Runtime owner language-surface refinement

- **Target artifact:** touched runtime owners for `/goal`, candidate-goal, and closing/recap presentation doctrine
- **Change type:** refinement
- **Current state:** runtime owners describe dominant-session-language behavior, but some surface templates/examples still leave English wrapper labels in place.
- **Target state:** runtime owners make the end-to-end language surface explicit across wrapper labels, candidate-goal headings, promoted `/goal`, and recap/closing lines while preserving exact-literal boundaries.
- **Review point:** keep `/goal` advisory, keep exact literals exact when needed, and preserve governed-work-only boundaries.

### 2) New playground case family

- **Target artifact:** `playground/cases/case-16-end-to-end-language-aligned-goal-surface.md`
- **Change type:** additive
- **Current state:** the playground family has no dedicated case for wrapper-label language alignment across candidate goals, promoted `/goal`, and recap lines.
- **Target state:** the playground family includes one dedicated case showing that end-to-end language-surface behavior operationally.
- **Review point:** keep the case non-runtime, evidence-calibrated, and explicit about `rule-enforced fact`, `observed case`, and `virtual variant` separation.

### 3) Playground index update

- **Target artifact:** `playground/README.md`
- **Change type:** additive
- **Current state:** the scenario-family index stops at case 15.
- **Target state:** the index includes case 16 and keeps the playground as a pointer-level governed family entrypoint.
- **Review point:** do not turn the playground README into a broad scenario dump.

### 4) Release-surface and design sync

- **Target artifact:** touched README/design/changelog/TODO/phase/patch surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces identify `v10.23 / P115` as the current released baseline.
- **Target state:** master surfaces open and later close `v10.24 / P116` consistently while preserving advisory `/goal`, the 18-file runtime install scope, and the non-runtime playground boundary.
- **Review point:** keep runtime install scope at 18 and make no claim that `playground/` entered the install payload.

---

## Verification

Required checks before release closeout:
- touched runtime owners encode end-to-end dominant-session-language behavior without forcing translation of exact literals
- `playground/cases/case-16-end-to-end-language-aligned-goal-surface.md` exists
- `playground/README.md` indexes the new case family
- touched release/master surfaces align to `v10.24 / P116`
- `playground/` remains outside the runtime install payload
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- GitHub release `v10.24` is created and verified before closeout wording claims release completion

---

## Implementation Status

P116 is in progress.

The runtime doctrine gaps are identified in checked source scope and startup surfaces are being opened; owner/companion/changelog sync, playground case creation, runtime install-boundary proof, parity/body-sufficiency verification, commit/push, GitHub release verification, and final closeout alignment remain pending.
