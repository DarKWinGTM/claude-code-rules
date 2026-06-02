# Quick Start Companion-Plugin Setup Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Complete / Released
> **Target Design:** [../design/design.md](../design/design.md) v10.35
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for the P133 wave.

It packages one bounded documentation/release-sync refinement so the root RULES Quick Start no longer stops at runtime-rule installation only: operators now get a compact companion-plugin setup path for `governed-docs` and `memory-context-intelligence` immediately after the runtime install notes, while plugin/runtime boundaries remain explicit.

---

## Analysis

Before this wave:
- the root README already introduced the two companion plugins in a later section
- plugin-local READMEs already carried fuller install/use guidance
- the new Quick Start setup block existed as a source-only change, but the release/tracker surfaces still described only the earlier P132 discovery wave

The better posture is:
- keep the Quick Start follow-up compact
- expose the companion-plugin install path earlier
- preserve the boundary that plugins install separately from `.claude/rules`
- record the change as its own successor doc-only wave instead of reopening P132 retroactively

This wave is intentionally documentation/release-sync-only. It does not change plugin behavior, runtime rule scope, or marketplace semantics.

---

## Change Items

### 1) Root README Quick Start companion-plugin setup

- **Target artifact:** `README.md`
- **Change type:** refinement
- **Current state:** Quick Start explained runtime-rule installation, while plugin setup lived only in later documentation
- **Target state:** Quick Start now includes a compact companion-plugin setup block with marketplace add, install, reload, boundary, and first-use guidance
- **Review point:** the README must keep plugin installation separate from the active `.claude/rules/` payload and must not overclaim plugin/runtime behavior changes

### 2) Successor-wave tracking alignment

- **Target artifacts:** `TODO.md`, `phase/SUMMARY.md`, `phase/phase-133-quickstart-companion-plugin-setup.md`
- **Change type:** release synchronization
- **Current state:** active tracking surfaces still closed only P132 / `v10.40`
- **Target state:** tracking surfaces now close the Quick Start setup refinement as `P133 / v10.41`
- **Review point:** wording must keep the wave doc-only and must not imply plugin code/runtime payload changes

### 3) Release-history alignment

- **Target artifacts:** `changelog/changelog.md`, `changelog/changelog/v10.41-released-quickstart-companion-plugin-setup.changelog.md`
- **Change type:** release synchronization
- **Current state:** the latest released baseline recorded only the P132 discovery/docs wave
- **Target state:** changelog parent and detail shard now record the Quick Start setup follow-up as the next released wave
- **Review point:** version selection must match checked remote/default-branch reality before release wording is finalized

### 4) Patch-path clarity

- **Target artifact:** `patch/quickstart-companion-plugin-setup.patch.md`
- **Change type:** additive governance artifact
- **Current state:** there was no dedicated patch artifact for the Quick Start setup successor wave
- **Target state:** the wave has its own before/after review artifact instead of stretching the P132 patch beyond its original scope
- **Review point:** patch scope stays narrow and release-sync-focused

---

## Verification

Required checks before release closeout:
- the root README Quick Start includes the new companion-plugin setup block
- the block preserves the plugin/runtime boundary
- the block preserves `memory-context-intelligence` first use as `/memory-context-intelligence:init` then `/memory-context-intelligence:analysis`
- touched README/TODO/phase/patch/changelog surfaces align to `v10.41 / P133`
- `git diff --check` passes
- the selected scope is committed, pushed, tagged, and GitHub release verification passes

---

## Implementation Status

P133 is completed.

The root README now exposes companion-plugin setup in the Quick Start path, the touched release/tracker surfaces were synchronized to the successor wave, the plugin/runtime boundary stayed intact, and the selected scope was published through a clean release path with push/tag/release verification.
