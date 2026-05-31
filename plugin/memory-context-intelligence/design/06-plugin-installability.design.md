# Design Shard 06 - Plugin installability

> **Parent Document:** [design.md](design.md)
> **Current Version:** 0.1.59
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-05-28)
> **Status:** Active installability and harness-surface target-state shard; phases 031-033 are retained as historical projection-family evidence only, phase 055 single-source authority cleanup completed in checked local scope, phase 034 harness-surface governance sync completed in checked local scope, phase 035 named slash-surface proof completed while the auto-flow blocker remains recorded in checked local scope, phase 036 analysis-only invocation design sync completed in checked local scope, phase 037 implementation planning completed, phase 038 analysis-surface runtime implementation completed in checked local scope, phases 039-041 completed the earlier plugin-skill naming correction family, phase 042 completed the earlier single public `/analysis` memsearch-backed operator-surface sync, phase 045 completed the registered analysis surface correction, phase 046 completed bare `/analysis` surface model selection, phase 047 completed the design-grounded current-session-first analysis review correction, phase 048 completed the memsearch-backed analysis retrieval correction, and phase 049 completed the analysis-surface output-contract correction

---

## Purpose

This shard defines the installability and governance contract for the `memory-context-intelligence` capsule after phase 016 checked-scope runtime readiness, after the phase 024 namespace correction, and after phase 055 removed the last active-authority drift from the earlier projection-family model.

Installability work remains separate from main RULES promotion. Phases 019-023 remain completed checked-local lifecycle evidence, but under the later selected namespace basis they are transitional rules-local / `@inline` proof rather than final target-namespace proof. Phases 025-027 remain valid historical checked evidence from the temporary/remapped darkwingtm state. Phases 031-033 remain valid historical installability/projection evidence from the now-removed `TEMPLATE/PLUGIN/memory-context-intelligence/` family. None of those waves represent current runtime truth anymore.

The target install ID remains the design subject for future proof work:

```text
memory-context-intelligence@darkwingtm
```

Current runtime truth after completed phase 055 single-source authority cleanup:

- active source authority remains `<repo-root>/plugin/memory-context-intelligence/`
- active runtime marketplace mapping remains `darkwingtm` -> root `TEMPLATE`
- the root `TEMPLATE` marketplace file includes `memory-context-intelligence` with supported in-base source `./RULES/plugin/memory-context-intelligence`
- `TEMPLATE/PLUGIN/memory-context-intelligence/` no longer exists in current runtime truth and is retained only as historical projection-family evidence from phases 031-033
- `claude plugin list --available --json` and current install state continue to expose `memory-context-intelligence@darkwingtm` under the active shared marketplace
- checked local install/details/enablement passed in normal and bare CLI views
- approved uninstall-only closeout from the older lifecycle proof remains historical evidence only while current checked-local state re-shows `memory-context-intelligence@darkwingtm` installed/enabled in local scope for `<workspace-root>`
- this transcript directly proves the implemented namespaced analysis surface `/memory-context-intelligence:analysis` from the RULES-owned package while the local `@darkwingtm` install is present
- retained historical cache/data from the lifecycle proof remains evidence and does not override the current active install state

## Harness-facing surface model

`memory-context-intelligence` is one plugin capability with three peer harness-facing entry surfaces:
- harness-native skill surface
- named slash-command surface
- plugin-managed auto-flow surface

These are peer entry shapes for one capability contract. They must not drift into separate products or separate semantic behaviors.

Current checked-local transcript evidence in this shard proves install/load visibility plus the current scoped runtime-chain implementation for analysis behavior in checked local scope. The packaged `intake → signals → present` chain now proves current-day/current-session narrowing with optional same-day lookback, and checked approved non-interactive local invocations of `/memory-context-intelligence:analysis` now return operator-facing output when local command approval is intentionally granted with `--permission-mode bypassPermissions`. Plain no-approval print-mode is not used as slash-output proof because this surface needs a local command run. `/memory-context-intelligence:analysis` still appears in checked slash-command registry output, and official Claude Code docs checked in scope state that plugin skills use the `plugin-name:skill-name` namespace when invoked as slash commands. This shard therefore treats `/memory-context-intelligence:analysis` as the checked plugin-owned surface and treats any future true bare `/analysis` command as a separate non-plugin harness-native owner surface rather than as a plugin-skill alias target. Earlier proof for `/memory-context-intelligence:memory-context-intelligence` remains historical pre-implementation evidence only. Plugin-managed auto-flow remains unproven: the installed package exposes no `hooks/hooks.json` or `monitors/monitors.json`, `claude plugin details` shows `Hooks (0)` and `MCP servers (0)`, and this transcript contains no autonomous auto-flow invocation event.

`bin/memory-context-intelligence` is an internal implementation adapter only. It may support development, testing, or internal runtime wiring, but it is not the primary post-install workflow for the user and it must not be treated as a peer harness-facing surface.

## Proof-separation boundary

The proof model for this capsule stays split:
- install/load proof: plugin is available, installed, enabled, and visible in runtime/plugin registry surfaces
- skill proof: harness-native skill surface is loaded or invoked in transcript-visible runtime evidence
- slash proof: named slash-command/chat invocation is shown separately
- auto-flow proof: plugin-managed automatic invocation path is shown separately
- internal adapter proof: `bin/**` behavior is implementation evidence only and does not by itself prove any harness-facing surface

## Implemented invocation surface boundary

Current checked runtime/proof now aligns to the implemented registered invocation:
- checked registered analysis slash surface: `/memory-context-intelligence:analysis`
- bare `/analysis` is not present in checked slash-command registry output and is not treated as proved current runtime behavior
- earlier proof for `/memory-context-intelligence:memory-context-intelligence` remains historical pre-implementation evidence only
- `/memory-context-intelligence:review` and `/memory-context-intelligence:packet` remain deferred until they have clearly distinct purposes
- the implemented first response for `analysis` is proposal-first topic suggestions with short why/impact wording, not package-map, internal pipeline, or development/progress-summary explanation by default
- if memsearch-backed analysis is blocked, the surface says so directly with the input reason
- if memsearch-backed analysis is dormant, the surface says so directly because the memsearch input is stale
- if no strong candidate is ready from checked memsearch scope yet, the surface says so directly with actionable insufficiency instead of filling the first response with workflow explanation or development/progress-summary narration
- recurring analysis-surface failures can surface as issue-first titles such as `Clarify analysis surface output contract for operator-facing results` instead of generic keyword-bag or plugin-harness wording
- deeper mechanism, matrix, packet, or rollout detail opens only after topic selection or explicit internal request
- green tests plus direct packaged `intake → signals → present` execution currently prove the scoped current-day/current-session analysis behavior, and checked approved non-interactive local slash runs now return operator-facing output when local command approval is intentionally granted with `--permission-mode bypassPermissions`
- plain no-approval print-mode still is not used as slash-output proof because this surface needs a local command run

Phase 045 closes the active operator-surface correction for this model. It still does not claim plugin-managed auto-flow proof, publication, external marketplace release, stable/broad production readiness, or main RULES promotion/mutation/merge.

## Source-home contract

The active runtime implementation source home remains:

```text
<repo-root>/plugin/memory-context-intelligence/
```

This source package stays the source authority for future design-selected darkwingtm proof work. It must not be treated as the active runtime marketplace root merely because the source package exists there.

The active runtime `darkwingtm` marketplace now points at the root `TEMPLATE` directory rather than at a `TEMPLATE/PLUGIN` marketplace root. That shared marketplace includes `memory-context-intelligence` as a supported in-base entry through source `./RULES/plugin/memory-context-intelligence`, which keeps one active source home and avoids a second projection tree.

Phase 029 selected the non-breaking bridge design, but phase 030 blocked that approach because Claude Code rejected the bridge source path outside the marketplace base. Phases 031-033 then formed the historical projection-family workaround/proof cycle. Phase 055 supersedes that active-authority model by keeping the root marketplace binding while removing the duplicate `TEMPLATE/PLUGIN/memory-context-intelligence/` tree from current truth.

## Historical transitional proof retained

### Phase 020 source-side bootstrap

Phase 020 created the source-side parent marketplace bootstrap surface at `<repo-root>/plugin/.claude-plugin/marketplace.json` and updated `.claude-plugin/plugin.json` author metadata to lowercase `darkwingtm`.

This remains valid source-side/bootstrap evidence. It is not current runtime marketplace proof because the active runtime `darkwingtm` marketplace is restored to `<template-plugin-root>`.

### Phase 021 session-only load proof

Phase 021 proved session-only inline availability from this source home by using `claude --bare --plugin-dir` and observing `memory-context-intelligence@inline` with `scope: "session"`, this source path as `installPath`, one skill, and four agents.

This remains valid session-scoped inline proof. It does not prove `memory-context-intelligence@darkwingtm`, persistence, reload behavior, uninstall behavior, marketplace publication, or main RULES promotion/merge.

### Phase 022 local persistent install proof

Phase 022 proved local-scope persistent CLI availability from `<workspace-root>` by installing `memory-context-intelligence@rules-local`. The checked output showed `rules-local` as a directory marketplace pointing at `<repo-root>/plugin`, while the then-existing `darkwingtm` marketplace pointed at `<template-plugin-root>`.

The observed install entry used `scope: "local"`, project path `<workspace-root>`, and cache install path `<user-claude-root>/plugins/cache/rules-local/memory-context-intelligence/0.9.0`. Bare plugin details showed `Source: memory-context-intelligence@rules-local`, one skill, and four agents.

This remains valid local persistent CLI install proof for the transitional `rules-local` namespace. It does not prove the selected target install ID `memory-context-intelligence@darkwingtm` under the restored shared `darkwingtm` marketplace.

### Phase 023 uninstall-only closeout

Phase 023 used the phase-022 normal plus bare CLI checks as the reload/new-process side and completed the approved uninstall-only proof:

```bash
claude plugin uninstall --scope local --keep-data "memory-context-intelligence@rules-local"
```

Post-uninstall checks showed the installed plugin absent from normal and bare plugin lists, details not found, local enablement cleared, `rules-local` retained, source package preserved, retained cache/data still present after `--keep-data`, and `/additional/` trial material preserved.

This remains valid checked-local lifecycle evidence for `memory-context-intelligence@rules-local`. It does not prove uninstall lifecycle behavior for `memory-context-intelligence@darkwingtm`.

## Target namespace proof gates

### Phase 024 namespace governance sync

Phase 024 was a docs-only correction wave. It clarified that:

- `memory-context-intelligence@darkwingtm` was the selected target install ID
- the active source home remained `<repo-root>/plugin/memory-context-intelligence/`
- phases 020-023 were completed transitional evidence, not final target-namespace closeout
- phases 025-027 would reprove session-only, persistent install, and uninstall lifecycle under the darkwingtm target namespace

Phase 024 did not perform runtime install/uninstall mutation.

### Phases 025-027 historical darkwingtm proof evidence

Phases 025-027 remain valid historical checked evidence from the temporary/remapped state where the effective local `darkwingtm` marketplace pointed at `<repo-root>/plugin`.

Historical evidence retained:

- phase 025 recorded the split proof under then-current Claude Code semantics: marketplace-qualified availability through `claude plugin list --available --json` and direct session-only disk load separately as `memory-context-intelligence@inline` with `scope: "session"`
- phase 026 recorded approved local-scope persistent install proof for `memory-context-intelligence@darkwingtm` from `<workspace-root>` while the effective `darkwingtm` mapping pointed at `<repo-root>/plugin`
- phase 027 recorded approved uninstall-only closeout for that local install and preserved source package, governed docs, cache/data retained by `--keep-data`, and `/additional/` material

Reclassification after marketplace restore and later supported reproof:

- the active runtime `darkwingtm` marketplace is restored to `<template-plugin-root>` and now includes `memory-context-intelligence` through supported in-base source `./memory-context-intelligence`
- phase 032 historically ended with approved uninstall-only closeout, but the current checked-local state in this transcript now re-shows `memory-context-intelligence@darkwingtm` installed/enabled in local scope and runtime-loaded through the namespaced skill surface
- retained cache from phase 026/027 and phase 032 lifecycle proof is evidence only and does not override the current active install state
- phases 025-027 remain historical evidence from the temporary/remapped state and must not be used to claim current proof basis; current checked-local installability under the restored shared marketplace is proven by phase 032 lifecycle evidence plus the current runtime-loaded/local-install proof re-shown by phase 033

### Phase 028 restored darkwingtm shared-marketplace governance sync

Phase 028 is completed by the v0.1.33 docs-only governance wave. It aligns active docs to the restored runtime mapping without mutating plugin install state, settings, marketplace registry, cache, source package runtime contents, or `/additional/` material.

Phase 028 explains why shared darkwingtm marketplace design is unresolved: adding `memory-context-intelligence` back under `darkwingtm` now affects the shared `<template-plugin-root>` marketplace and potentially other plugins, so a design decision is needed before any marketplace or install mutation.

### Phase 029 shared darkwingtm marketplace design resolution

Phase 029 is completed as docs-only design selection. It selects the smallest viable non-breaking shared-marketplace bridge design:

- keep active runtime marketplace `darkwingtm` mapped to `<template-plugin-root>`
- do not use `<repo-root>/plugin` as the active runtime marketplace root
- later, with explicit approval, add `memory-context-intelligence` as an extra entry inside `<template-plugin-root>/.claude-plugin/marketplace.json`
- the later shared-marketplace entry should use source `../RULES/plugin/memory-context-intelligence`
- keep `<template-plugin-root>/memory-context-intelligence/` as deprecated historical docs only, not the active plugin package

Rejected alternatives:

- remapping `darkwingtm` to `<repo-root>/plugin` is rejected because it breaks existing plugins that belong to the restored shared `TEMPLATE/PLUGIN` marketplace
- creating a second active `memory-context-intelligence` package under `<template-plugin-root>` is rejected because it would create source drift and duplicate truth; the active source authority remains `<repo-root>/plugin/memory-context-intelligence/`

Phase 029 does not mutate plugin install state, settings, marketplace registry, cache, source package runtime contents, installed plugins, or `/additional/` material.

### Phase 030 darkwingtm reproof after shared-marketplace resolution

Phase 030 is blocked, not completed. It attempted the phase-029 bridge design in the shared `darkwingtm` marketplace while preserving the marketplace mapping at `<template-plugin-root>`.

The blocker is exact and implementation-derived: adding `memory-context-intelligence` with source `../RULES/plugin/memory-context-intelligence` made it appear in the available list, but the install did not succeed because Claude Code rejected that source as unsupported / path traversal outside the marketplace base. Existing `@darkwingtm` plugins remained healthy in CLI outputs. Because of this, no final `memory-context-intelligence@darkwingtm` availability/install/uninstall proof exists under the shared-marketplace design.

### Historical phase 031 supported runtime package exposure design

Phase 031 is completed as docs-only historical design selection. It records the earlier supported runtime-facing package projection model that kept source authority at:

```text
RULES/plugin/memory-context-intelligence/
```

and selected the then-runtime-facing package path:

```text
TEMPLATE/PLUGIN/memory-context-intelligence/
```

That projection model is no longer current runtime truth after phase 055. It is retained here only as historical installability/provenance evidence for the earlier workaround family.

Selected phase-031 design:

- keep active runtime marketplace `darkwingtm` mapped to `<template-plugin-root>` / `TEMPLATE/PLUGIN`
- keep active source authority in `RULES/plugin/memory-context-intelligence/`
- later create or update `TEMPLATE/PLUGIN/memory-context-intelligence/` as the runtime-facing package projection
- govern projection drift through explicit sync/export rules, version alignment, and later reproof
- do not claim runtime availability/install/uninstall proof from the docs-only selection

Rejected alternatives:

- remapping `darkwingtm` to `RULES/plugin`, because the shared `darkwingtm` marketplace supports in-base sources under `TEMPLATE/PLUGIN` and other existing shared plugins belong there
- using the `../RULES/plugin/memory-context-intelligence` bridge entry, because phase 030 proved Claude Code rejects that outside-base source as unsupported / path traversal during install
- manually maintaining an independent package under `TEMPLATE/PLUGIN/memory-context-intelligence/`, because that creates duplicate truth and drift from the RULES plugin source authority

### Historical phase 032 supported runtime package implementation and reproof

Phase 032 is completed in checked local scope as historical projection-family evidence after explicit approval for the then-runtime-facing package mutation and lifecycle-proof scope.

Completed phase-032 gates:

- runtime-facing projection exists at `TEMPLATE/PLUGIN/memory-context-intelligence/`
- projection is traceable to source authority `RULES/plugin/memory-context-intelligence/`
- active `darkwingtm` marketplace uses supported in-base package path `./memory-context-intelligence`
- `memory-context-intelligence@darkwingtm` availability was observed under the active marketplace
- `claude plugin install --scope local "memory-context-intelligence@darkwingtm"` succeeded in checked local scope
- normal and bare plugin details/enablement both passed and showed one skill plus four agents under source `memory-context-intelligence@darkwingtm`
- approved uninstall-only closeout with `claude plugin uninstall --scope local --keep-data "memory-context-intelligence@darkwingtm"` succeeded
- post-uninstall normal registry/list output and bare details removed the active install while kept cache was orphan-marked as retained lifecycle evidence
- no new direct session-loaded `memory-context-intelligence@darkwingtm` identity proof is claimed by phase 032; direct disk loading remains the separate `memory-context-intelligence@inline` session-only boundary from the earlier split-proof model
- existing shared `@darkwingtm` plugins, retained historical evidence, source authority, and `/additional/` material remained preserved

## Local marketplace surface

The package-local source-side marketplace bootstrap surface remains:

```text
<repo-root>/plugin/.claude-plugin/marketplace.json
```

That surface is source-side evidence for this package, not the active runtime `darkwingtm` marketplace after restore. The active runtime `darkwingtm` marketplace is:

```text
<template-plugin-root>/.claude-plugin/marketplace.json
```

The active runtime marketplace now includes `memory-context-intelligence` through supported in-base source `./memory-context-intelligence`. The phase-029 bridge design was tried in phase 030 and is still retained only as blocked historical evidence because Claude Code rejects the outside-base bridge source as unsupported / path traversal. Current supported exposure through `darkwingtm` now uses the phase-031 selected runtime-facing projection model, completed by phase 032.

## Manifest and author identity

The user-selected author identity direction remains lowercase `darkwingtm`.

`.claude-plugin/plugin.json` author metadata using `darkwingtm` is valid manifest metadata, but author metadata alone is not proof that the package is loaded, available, installed, or enabled as `memory-context-intelligence@darkwingtm` under the restored shared marketplace.

## Relationship to phases 017-018

Installability phases 019-033 are separate from phases 017-018:

- phases 017-018 remain deferred main RULES promotion/merge phases
- phases 019-023 remain completed transitional installability evidence
- phase 024 completed namespace governance clarification only
- phases 025-027 remain completed historical checked evidence from the temporary/remapped state, not current runtime truth
- phase 028 completed docs-only governance correction for restored shared-marketplace state
- phase 029 completed docs-only shared darkwingtm marketplace bridge design selection
- phase 030 is blocked because the shared-marketplace bridge source was rejected as unsupported / path traversal during install
- phase 031 completed docs-only supported runtime package exposure design
- phase 032 completed supported runtime-facing package implementation and checked-local reproof
- phase 033 completed runtime-loaded proof plus broader correction closeout in checked local scope
- phase 034 completed docs-only harness-surface governance sync that classifies skill, slash, and plugin-managed auto flow as peer harness-facing surfaces while reclassifying `bin/memory-context-intelligence` as an internal implementation adapter only
- installability proof does not approve main RULES promotion
- persistent install proof and uninstall closeout did not mutate main RULES
- `/additional/` trial-stage behavior remains unchanged

## Phase-family contract

The installability and namespace proof family now reads:

- phase 019: completed planning and installability contract
- phase 020: completed source-side manifest and local marketplace bootstrap, now reclassified as transitional bootstrap evidence
- phase 021: completed session-only inline load proof, now reclassified as transitional `@inline` evidence
- phase 022: completed local-scope persistent install proof, now reclassified as transitional `rules-local` evidence
- phase 023: completed reload/new-process evidence reuse, approved uninstall-only proof, and install-doc closeout, now reclassified as transitional `rules-local` lifecycle evidence
- phase 024: completed namespace governance/design sync for the selected `darkwingtm` target namespace
- phase 025: completed historical darkwingtm session-only split proof from the temporary/remapped state
- phase 026: completed historical local-scope persistent install proof from the temporary/remapped state
- phase 027: completed historical uninstall-only lifecycle closeout from the temporary/remapped state
- phase 028: completed docs-only restored darkwingtm shared-marketplace governance sync
- phase 029: completed docs-only shared darkwingtm marketplace bridge design selection without runtime mutation
- phase 030: blocked shared-marketplace bridge implementation attempt because Claude Code rejected the outside-base bridge source as unsupported / path traversal during install
- phase 031: completed docs-only supported runtime package exposure design
- phase 032: completed supported runtime-facing package implementation and checked-local reproof
- phase 033: completed direct runtime-loaded proof and broader transcript-governed darkwingtm correction closeout in checked local scope

Together, phases 024-034 preserve the darkwingtm correction evidence, complete the supported current target-state path under the restored shared marketplace, and close the broader transcript-governed correction objective plus harness-surface governance sync in checked local scope. Phase 035 then adds named slash-command surface proof in checked local scope while keeping plugin-managed auto-flow proof unclaimed. Phase 036 then synchronizes the analysis-only invocation-design decision across governed docs while preserving current checked runtime truth for the existing slash surface. Publication, external marketplace release, broad/stable production readiness, main RULES promotion, main RULES mutation, and main RULES merge remain unclaimed.

## Boundaries preserved

Installability work must not:

- move the active runtime source authority away from `RULES/plugin/memory-context-intelligence/`
- treat `TEMPLATE/PLUGIN/memory-context-intelligence/` as an independent source of truth rather than a governed runtime-facing export/projection
- change `/additional/` trial-stage behavior
- claim direct `--plugin-dir` session-loaded identity should become `memory-context-intelligence@darkwingtm` instead of `memory-context-intelligence@inline`
- claim marketplace publication or public release without checked evidence
- claim session-only load as persistent install proof
- claim persistent install outside the checked namespace and scope
- treat phase 020 source-side manifest/bootstrap updates as session-only load proof or persistent install proof
- treat phase 021 session-only inline load proof as persistent install, publication, marketplace release, slash-command/chat invocation proof, or main RULES promotion/merge proof
- treat phase 022 local-scope persistent CLI install proof as current darkwingtm namespace proof, slash-command/chat invocation proof, publication proof, external marketplace release proof, stable/broad production readiness, or main RULES promotion/merge proof
- treat phase 023 uninstall closeout as current darkwingtm uninstall proof, publication, external marketplace release, slash-command/chat invocation proof, stable/broad production readiness, main RULES promotion, main RULES mutation, or main RULES merge proof
- treat phases 025-027 as current runtime truth after the shared `darkwingtm` marketplace was restored to `<template-plugin-root>`
- treat retained cache from old proof as active install state
- mutate plugin install state, settings, marketplace registry, cache, source package runtime contents, or `/additional/` material during phase 028 docs-only sync
- mutate plugin install state, settings, marketplace registry, cache, installed plugins, source package runtime contents, or `/additional/` material during phase 029 docs-only design selection
- treat the phase-030 blocked bridge attempt as completed availability/install/uninstall proof
- rely on unsupported `../RULES/plugin/memory-context-intelligence` path traversal from the shared marketplace after phase 030
- remap `darkwingtm` to `RULES/plugin`
- rely on the rejected `../RULES/plugin/memory-context-intelligence` bridge entry
- treat phase-032 checked-local lifecycle proof as publication, external marketplace release, slash-command/chat invocation proof, stable/broad production readiness, or main RULES promotion/mutation/merge proof
- remove retained `rules-local` evidence, source package, retained cache/data, or `/additional/` material without explicit action-and-scope confirmation
- promote, mutate, or merge main RULES

## Verification implications

Current package capability through phase 016 remains `usable in checked scope` only. Phases 020-023 remain valid checked-local evidence but are explicitly transitional namespace proof. Phase 024 verifies documentation/governance alignment only.

Phases 025-027 remain valid historical checked evidence from the temporary/remapped darkwingtm state. They no longer prove current darkwingtm installability after the runtime mapping was restored to `<template-plugin-root>` and the active marketplace was observed not to include `memory-context-intelligence`.

Phase 028 is docs-only verification-in-scope for governance alignment. It does not verify runtime installability, mutate runtime state, update marketplace files, or prove `memory-context-intelligence@darkwingtm` is currently available/installed/enabled.

Phase 029 is docs-only verification-in-scope for design selection. It selected the shared-marketplace bridge design but did not implement the marketplace entry, verify runtime installability, mutate runtime state, update marketplace files, or prove `memory-context-intelligence@darkwingtm` was currently available/installed/enabled.

Phase 030 is blocked implementation evidence, not completion proof. It showed that the shared-marketplace bridge entry using source `../RULES/plugin/memory-context-intelligence` is unsupported because Claude Code rejects it as path traversal outside the marketplace base during install.

Historical projection-family verification notes:

- phase 031 is documentation/design verification only for the removed projection model; it recorded the source/projection boundary, rejected alternatives, and the later phase-032 approval gate
- phase 032 is completed checked-local implementation/reproof evidence for that removed projection family only; it does not define current runtime truth after phase 055
- phase 033 completed the broader transcript-governed correction objective for that older family and remains useful provenance, but it no longer authorizes treating the removed `TEMPLATE/PLUGIN/memory-context-intelligence/` tree as current authority

Current truth after phase 055 is narrower: one active source home, one active root-TEMPLATE marketplace binding, preserved install identity `memory-context-intelligence@darkwingtm`, and no duplicate projection-tree authority. Publication, external marketplace release, slash-command/chat invocation proof, stable/broad production readiness, and main RULES promotion/mutation/merge remain unclaimed.

The installability family now verifies the named slash-command surface in checked local scope through phase 035 only. Phase 036 selects the next target public invocation design but does not verify that target as live runtime behavior yet. The family still does not verify live web access, external agent process spawning, plugin-managed auto-flow behavior, marketplace publication, external marketplace release, stable/broad production readiness, main RULES promotion, main RULES mutation, or main RULES merge.

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
