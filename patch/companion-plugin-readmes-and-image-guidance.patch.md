# Companion Plugin READMEs and Image Guidance Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/design.md](../design/design.md) v10.35
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P132 wave.

It packages one bounded documentation/presentation refinement so the two local companion plugins are easier to discover and understand: each plugin gets its requested plugin-local image asset plus a stronger README, and the root RULES README gains a concise section that tells readers those plugins exist and what they help with.

---

## Analysis

Before this wave, the repo had two real companion plugins but a weak discovery path:
- the plugin-local image files were not present in plugin-local `img/` folders
- the plugin READMEs were useful but still too text-heavy at the top and lacked a visual entrypoint
- the root README did not clearly explain that RULES also ships companion plugins beside the active runtime rules

The better posture is:
- keep plugin assets local to each plugin
- keep plugin READMEs visually easier to enter
- make the root README acknowledge the plugins without collapsing into full plugin manuals
- preserve the boundary that plugins are installed separately from the 18 active runtime rules

This wave is intentionally documentation/presentation-only. It does not change plugin command behavior or semantic doctrine ownership.

---

## Change Items

### 1) Plugin-local image asset placement

- **Target artifacts:** `plugin/governed-docs/img/GOD.png`, `plugin/memory-context-intelligence/img/MCI.png`
- **Change type:** additive
- **Current state:** requested root image files existed, but the plugin-local image folders/files did not
- **Target state:** each plugin owns its referenced image asset under its own `img/` directory
- **Review point:** no cross-plugin or root-only image reference remains necessary for the README visuals

### 2) governed-docs README refinement

- **Target artifact:** `plugin/governed-docs/README.md`
- **Change type:** refinement
- **Current state:** the README already documented command/install behavior but lacked a stronger visual/top-level operator orientation
- **Target state:** the README includes the requested image plus clearer at-a-glance, workflow, and support-boundary guidance
- **Review point:** README remains accurate to current checked plugin behavior and does not overclaim semantic authority

### 3) memory-context-intelligence README refinement

- **Target artifact:** `plugin/memory-context-intelligence/README.md`
- **Change type:** refinement
- **Current state:** the README already documented install/init/analysis boundaries but lacked a stronger visual/top-level operator orientation
- **Target state:** the README includes the requested image plus clearer at-a-glance, first-use workflow, and boundary guidance
- **Review point:** README remains aligned to checked public surfaces `/memory-context-intelligence:init` and `/memory-context-intelligence:analysis`

### 4) Root README companion-plugin mention

- **Target artifact:** `README.md`
- **Change type:** refinement
- **Current state:** the root README mentioned plugin/ mostly as an excluded or preserved tree, not as discoverable companion tools
- **Target state:** the root README includes a concise `Companion Plugins` section and TOC entry explaining the two plugins and what they help with
- **Review point:** the root README preserves the boundary that plugins are installed separately and are not part of the active 18-rule runtime payload

### 5) Release-surface sync

- **Target artifact:** touched README/TODO/phase/patch/changelog surfaces
- **Change type:** release synchronization
- **Current state:** latest released baseline was `v10.39 / P131`
- **Target state:** touched release surfaces consistently open and close `v10.40 / P132`
- **Review point:** release wording remains evidence-calibrated and tied to the selected publish path

---

## Verification

Required checks before release closeout:
- both requested plugin-local image files exist at the selected paths
- both plugin READMEs reference their plugin-local image correctly
- the governed-docs README remains aligned to checked current command/install/index behavior
- the memory-context-intelligence README remains aligned to checked current init/analysis/config behavior
- the root README names both plugins clearly and preserves the runtime/plugin boundary
- touched README/TODO/phase/patch/changelog surfaces align to `v10.40 / P132`
- `git diff --check` passes
- the selected scope is committed, pushed, tagged, and GitHub release verification passes

---

## Implementation Status

P132 is completed.

The two plugin-local image assets were added, both plugin READMEs were expanded with clearer visual/operator guidance, the root README now acknowledges the companion plugins clearly, the touched release surfaces were synchronized, and the selected scope was published through a clean release path with push/tag/release verification.
