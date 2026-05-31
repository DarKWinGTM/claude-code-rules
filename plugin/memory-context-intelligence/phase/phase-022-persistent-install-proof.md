# Phase 022 - Persistent install proof

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

022

## Status

Completed

## Historical reclassification note

Under the later selected namespace basis, this phase remains Completed and valid as checked local-scope persistent CLI evidence, but it is transitional. It proves `memory-context-intelligence@rules-local`, not the selected target install ID `memory-context-intelligence@darkwingtm`.

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Prove the plugin remains available through the approved local-scope persistent install path without moving the source home, overriding the existing `darkwingtm` marketplace, or promoting main RULES.

## Why this phase exists

Persistent install proof is stronger than session-only load proof. The approved safer path renamed the source-side RULES marketplace to `rules-local` so the install ID is `memory-context-intelligence@rules-local` and does not collide with the existing local `darkwingtm` marketplace that points at `<template-plugin-root>`.

## Goal

Establish checked local-scope persistent install behavior for `memory-context-intelligence@rules-local`.

## Output

Completed output:

- source-side parent marketplace renamed to `rules-local`
- local-scope marketplace registration added from `<repo-root>/plugin`
- local-scope plugin install completed as `memory-context-intelligence@rules-local`
- bare CLI plugin listing/details proved the installed plugin is visible without `--plugin-dir`
- observed local settings/cache surfaces recorded for phase 023 uninstall/rollback verification
- closeout docs distinguish local persistent install proof from publication, external marketplace release, slash-command/chat invocation proof, stable/broad production readiness, or main RULES promotion/merge

## Gate

Completed in checked local scope when these commands succeeded from `<workspace-root>`:

```bash
claude plugin marketplace add --scope local "<repo-root>/plugin"
claude plugin install --scope local "memory-context-intelligence@rules-local"
claude plugin marketplace list --json
claude plugin list --json
claude --bare plugin list --json
claude --bare plugin details "memory-context-intelligence@rules-local"
```

## Owner

Runtime install verification owner. User approval for phase 022 local-scope runtime mutation was already supplied before execution.

## Files and runtime surfaces observed

Source-side governed mutation:

- `<repo-root>/plugin/.claude-plugin/marketplace.json` now uses marketplace name `rules-local`, owner metadata `darkwingtm`, and plugin source `./memory-context-intelligence`.

Observed local runtime/settings surfaces after install:

- `<workspace-root>/.claude/settings.local.json` changed from size `86565`, sha256 `f930198fc33b21eaa84686238c950137a57ce742059e40e6e75565292804f665` to size `86774`, sha256 `4739c15249315f7c063c5644d8a85fee7aa1036a4e984d5cd3afb507f5cb9bbd`; relevant keys include `enabledPlugins.memory-context-intelligence@rules-local = true` and `extraKnownMarketplaces.rules-local.source.path = <repo-root>/plugin`.
- `<workspace-root>/.claude/settings.json` remained unchanged at size `115`, sha256 `2d7752b7244abfc78e451e4bcddcf077985a28bb97f197e03d547feacbf10430`.
- `<user-claude-root>/settings.json` remained unchanged at size `8328`, sha256 `034ad5f5f27c43e619b6ab26a54cffe1bd86c065ee22f23b1a23ffc8594ce8e8`.
- `<user-claude-root>/plugins/cache/rules-local/memory-context-intelligence/0.9.0` exists as the Claude plugin cache copy for the local-scope install; a post-install snapshot found `102` files there.
- `<user-claude-root>/plugins/marketplaces/rules-local` was not created; `claude plugin marketplace list --json` reports `rules-local` as a directory source whose install location is `<repo-root>/plugin`.
- `<workspace-root>/.claude/plugins` remained missing.

## Verification

Verification route: `smoke_check` for local-scope persistent install proof.

Relevant observed output shape:

- `claude plugin marketplace add --scope local ...` returned `Successfully added marketplace: rules-local (declared in local settings)`.
- `claude plugin install --scope local "memory-context-intelligence@rules-local"` returned `Successfully installed plugin: memory-context-intelligence@rules-local (scope: local)`.
- `claude plugin marketplace list --json` included `rules-local` with `source: "directory"`, `path: "<repo-root>/plugin"`, and `installLocation: "<repo-root>/plugin"`; it also still showed the existing `darkwingtm` marketplace pointing at `<template-plugin-root>`.
- `claude plugin list --json` and `claude --bare plugin list --json` included `memory-context-intelligence@rules-local` with `version: "0.9.0"`, `scope: "local"`, `enabled: true`, `installPath: "<user-claude-root>/plugins/cache/rules-local/memory-context-intelligence/0.9.0"`, and `projectPath: "<workspace-root>"`.
- `claude --bare plugin details "memory-context-intelligence@rules-local"` showed `Source: memory-context-intelligence@rules-local`, skill inventory `memory-context-intelligence`, and agent inventory `source-trust-reviewer`, `synthesis-lead`, `trace-scout`, and `research-scout`.

This proves local-scope persistent CLI availability in the checked project path without `--plugin-dir`. It does not prove slash-command/chat invocation behavior, uninstall/rollback behavior, external marketplace publication, stable/broad production readiness, main RULES promotion, main RULES mutation, or main RULES merge.

## Risks

- persistent local settings now contain `enabledPlugins.memory-context-intelligence@rules-local`
- uninstall/rollback proof is still required in phase 023
- installed cache output lives under `<user-claude-root>/plugins/cache/rules-local/`, even though the install scope reported by Claude is local to `<workspace-root>`
- source-side marketplace name must remain `rules-local` to avoid colliding with the existing `darkwingtm` marketplace
- documentation must keep author metadata `darkwingtm` separate from marketplace name `rules-local`

## Rollback notes

Phase 023 remains the first uninstall/rollback/reload closeout gate. It must verify removal or rollback of the local-scope installed state, including the relevant `settings.local.json` entries and cached installed plugin state, without deleting the source package or `/additional/` trial-stage material unless separately confirmed.
