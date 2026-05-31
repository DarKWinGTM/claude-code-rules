# Phase 023 - Reload, uninstall, and install documentation closeout

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

023

## Status

Completed

## Historical reclassification note

Under the later selected namespace basis, this phase remains Completed and valid as checked local reload/new-process and uninstall-only lifecycle evidence, but it is transitional. It closes the `memory-context-intelligence@rules-local` lifecycle, not the selected target install ID `memory-context-intelligence@darkwingtm`.

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Close the installability family by using the existing phase-022 normal plus bare CLI checks as the reload/new-process proof side, then proving approved uninstall-only behavior for `memory-context-intelligence@rules-local` without removing the retained `rules-local` marketplace registration, source package, or `/additional/` trial-stage material.

## Why this phase exists

Phase 022 proved local-scope persistent CLI availability for `memory-context-intelligence@rules-local`, but the installability family needed a lifecycle closeout showing what remains available after uninstall and which surfaces are intentionally retained. The user explicitly approved uninstall-only proof and did not approve marketplace removal, source package deletion, `/additional/` removal, or reinstall.

## Goal

Finish the phase-019 through phase-023 installability lifecycle with checked reload/new-process evidence, uninstall-only evidence, and synchronized install documentation.

## Output

Completed output:

- reload/new-process side is covered by the phase-022 normal plus bare CLI checks that showed `memory-context-intelligence@rules-local` available without `--plugin-dir` after local-scope install
- approved uninstall-only command completed from `<workspace-root>`
- post-uninstall CLI checks show the plugin is absent from normal and bare installed-plugin lists
- post-uninstall details check fails with `Plugin "memory-context-intelligence@rules-local" not found.`
- `rules-local` marketplace registration remains intentionally retained and still points at `<repo-root>/plugin`
- source package remains preserved at `<repo-root>/plugin/memory-context-intelligence/`
- phase-015 additional-stage material remains preserved at `<user-runtime-rules>/additional/memory-context-intelligence/`
- local install enablement is removed from `<workspace-root>/.claude/settings.local.json`; `enabledPlugins` is now `{}` and the file no longer contains `memory-context-intelligence`
- global installed plugin registry `<user-claude-root>/plugins/installed_plugins.json` no longer contains `memory-context-intelligence`
- cache/data path `<user-claude-root>/plugins/cache/rules-local/memory-context-intelligence` remains present with child `0.9.0` after `--keep-data`; this is retained cache/data, not an installed/enabled plugin-list entry
- install lifecycle docs distinguish ready-to-install checked local scope from publication, external marketplace release, slash-command/chat invocation proof, stable/broad production readiness, or main RULES promotion/merge

## Gate

Completed in checked local scope when the approved uninstall-only command succeeded and post-uninstall checks proved that the local installed plugin entry is absent while the `rules-local` marketplace registration, source package, and `/additional/` trial-stage material remain preserved.

## Owner

Install lifecycle closeout owner. User approval was explicitly limited to uninstall-only proof and did not authorize marketplace removal, source package deletion, `/additional/` deletion, main RULES promotion/merge, or reinstall.

## Commands and evidence

All commands below were run from `<workspace-root>` unless otherwise noted.

### Reload/new-process side reused from phase 022

Phase 022 already recorded normal and bare CLI checks without `--plugin-dir`:

```bash
claude plugin list --json
claude --bare plugin list --json
claude --bare plugin details "memory-context-intelligence@rules-local"
```

Those checks showed `memory-context-intelligence@rules-local` with `scope: "local"`, `enabled: true`, project path `<workspace-root>`, cache install path `<user-claude-root>/plugins/cache/rules-local/memory-context-intelligence/0.9.0`, and details inventory containing one skill plus four agents. This is the reload/new-process evidence reused for phase 023. It is CLI install visibility proof only; it is not slash-command/chat invocation proof.

### Approved uninstall-only command

```bash
claude plugin uninstall --scope local --keep-data "memory-context-intelligence@rules-local"
```

Observed output:

```text
✔ Successfully uninstalled plugin: memory-context-intelligence (scope: local)
```

### Post-uninstall CLI checks

```bash
claude plugin marketplace list --json
```

Observed result: `rules-local` remains listed with `source: "directory"`, `path: "<repo-root>/plugin"`, and `installLocation: "<repo-root>/plugin"`.

```bash
claude plugin list --json
claude --bare plugin list --json
```

Observed result: both installed-plugin lists no longer include `memory-context-intelligence@rules-local`.

```bash
claude --bare plugin details "memory-context-intelligence@rules-local"
```

Observed result:

```text
Exit code 1
Plugin "memory-context-intelligence@rules-local" not found. Run `claude plugin list` to see installed plugins, or pass --plugin-dir <path> to load one from disk.
```

### Post-uninstall local state checks

- `<workspace-root>/.claude/settings.local.json` exists with size `86719`, sha256 `593fd282bf3509c2db0e1f4a290a9a1040dcce54f362ea05695480d4ba156500`, `enabledPlugins: {}`, `extraKnownMarketplaces.rules-local.source.path = <repo-root>/plugin`, and no `memory-context-intelligence` string.
- `<workspace-root>/.claude/plugins` remains absent.
- `<user-claude-root>/plugins/installed_plugins.json` exists with size `6133`, sha256 `769a7a67164a5182f925a56efad8e745a7a581a2482d13ca5d23eba3ba727b9e`, and no `memory-context-intelligence` string.
- `<user-claude-root>/plugins/cache/rules-local/memory-context-intelligence` still exists after `--keep-data`; checked children show `0.9.0`, with `103` files and `14` directories under the retained cache/data path.
- `<repo-root>/plugin/memory-context-intelligence/` still exists.
- `<user-runtime-rules>/additional/memory-context-intelligence/phase-015-live-bounded-additional-stage-trial.md` still exists.

## Verification

Verification route: `smoke_check` for the approved uninstall-only lifecycle closeout.

The checked evidence proves local CLI uninstall-only behavior for the previously installed `memory-context-intelligence@rules-local` entry. It also proves the retained `rules-local` marketplace registration keeps the package ready to install again in checked local scope because the marketplace source still points at the preserved source package.

It does not prove publication, external marketplace release, slash-command/chat invocation behavior, stable/broad production readiness, main RULES promotion, main RULES mutation, main RULES merge, or reinstall after uninstall.

## Risks

- `--keep-data` left the cache/data path present; docs must not phrase the retained cache directory as an installed/enabled plugin entry.
- `rules-local` remains intentionally registered; docs must not imply marketplace removal or full local-state purge.
- source package and `/additional/` material remain preserved and must not be treated as cleanup targets.
- installability family closure remains checked-scope local lifecycle proof, not publication or promotion readiness.

## Rollback notes

No reinstall was performed in phase 023. If future work needs the plugin installed again, use the retained `rules-local` marketplace registration and preserved source package under a separately selected install action. Do not delete the source package, retained cache/data path, `rules-local` marketplace registration, or `/additional/` trial-stage material without explicit action-and-scope confirmation.
