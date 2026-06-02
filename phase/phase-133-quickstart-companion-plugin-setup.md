# P133 — Quick Start Companion-Plugin Setup

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P133
> **Status:** Completed / Released
> **Target Release:** v10.41
> **Design References:**
> - [../design/design.md](../design/design.md) v10.35
> **Patch References:** [../patch/quickstart-companion-plugin-setup.patch.md](../patch/quickstart-companion-plugin-setup.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Promote the new root README Quick Start companion-plugin setup guidance into a bounded successor release wave.

---

## Why This Phase Exists

P132 made the two companion plugins discoverable and improved their plugin-local READMEs, but the root README Quick Start still behaved like a runtime-rules-only entry path.

P133 exists to close that gap without broadening the work into plugin code or runtime-rule payload changes:
- runtime rules still install into `.claude/rules/`
- companion plugins still install separately from the local marketplace
- Quick Start now tells operators how to add the marketplace, install both companion plugins, reload them, and begin the intended first-use flow

---

## Expected Output

- root `README.md` carries a Quick Start companion-plugin setup block directly after the runtime-rule install notes
- the Quick Start setup block keeps plugin installation separate from the active `.claude/rules/` runtime payload
- the block points operators to install `governed-docs` and `memory-context-intelligence` from the local marketplace
- the block preserves `memory-context-intelligence` first use as `/memory-context-intelligence:init` followed by `/memory-context-intelligence:analysis`
- touched README/TODO/phase/patch/changelog surfaces align to `v10.41 / P133`
- `git diff --check`, branch/default-branch verification, and GitHub release verification all pass before closeout claims release completion

---

## Action Checklist

- [x] Keep the existing root README Quick Start companion-plugin setup block as the source change for this wave.
- [x] Update root README release framing to the successor wave.
- [x] Sync TODO current release and completed-wave history.
- [x] Sync `phase/SUMMARY.md` and create a dedicated P133 phase file.
- [x] Create a dedicated patch record for the Quick Start companion-plugin setup wave.
- [x] Sync master changelog and add a v10.41 detail shard.
- [x] Publish the selected scope safely without bundling unrelated dirty repo state.
- [x] Verify the pushed commit and GitHub release `v10.41`.

---

## Out of Scope

- changing plugin runtime behavior or command contracts
- changing the active 18-rule runtime install payload
- reopening P132 as if the Quick Start setup block had already shipped there
- rewriting plugin-local design/phase/changelog/TODO families beyond what this selected release surface needs
- bundling unrelated dirty repo state into this wave

---

## Completion Gate

- the root README Quick Start now includes the companion-plugin setup path
- plugin/runtime boundaries remain explicit and correct
- `memory-context-intelligence` first-use flow remains `/memory-context-intelligence:init` then `/memory-context-intelligence:analysis`
- touched README/TODO/phase/patch/changelog surfaces align to `v10.41 / P133`
- `git diff --check` passes
- the selected scope is committed, pushed, tagged, and release-verified

---

## Current Status

P133 is completed.

Current checked progress:
- the root README now exposes the companion-plugin setup path as part of Quick Start follow-through rather than leaving installation guidance only in later plugin documentation
- the new Quick Start block still keeps plugin loading separate from the active runtime-rule payload
- touched README/TODO/phase/patch/changelog surfaces are aligned to `v10.41 / P133`
- the selected documentation/release-sync scope was published through a clean isolated release path rather than the dirty local working tree
- `git diff --check`, push/update to `master`, GitHub release verification, and final closeout alignment all passed
