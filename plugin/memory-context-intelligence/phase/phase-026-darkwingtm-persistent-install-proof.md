# Phase 026 - darkwingtm persistent install proof

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

026

## Status

Completed / Historical evidence

## Historical Reclassification

Phase 026 remains valid historical checked evidence from the temporary/remapped `darkwingtm` state where the effective marketplace mapping pointed at `<repo-root>/plugin`. After the runtime marketplace mapping was restored to `darkwingtm` -> `<template-plugin-root>`, this phase no longer represents current installed/enabled state for `memory-context-intelligence@darkwingtm`.

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Reprove local-scope persistent install availability under the selected target install ID `memory-context-intelligence@darkwingtm`.

## Why this phase exists

Phase 022 proved persistent CLI availability only as `memory-context-intelligence@rules-local`. The user selected `darkwingtm` as the target marketplace namespace after that proof, and phase 025 completed the session split proof for the selected namespace. Phase 026 therefore rechecks persistent local install under the selected target ID before uninstall lifecycle closeout.

## Approval and execution boundary

The user explicitly approved local-scope persistent install proof for this phase.

Executed boundary:

- local scope only
- no uninstall in this phase
- no main RULES promotion/merge phase work
- no `/additional/` behavior change
- no slash-command/chat invocation proof claim
- no publication, external marketplace release, stable/broad production readiness, or main RULES promotion/merge claim

## Goal

Establish whether `memory-context-intelligence@darkwingtm` can be installed persistently from the effective local `darkwingtm` marketplace mapping without moving source truth or expanding into uninstall lifecycle work.

## Output

Phase 026 produced checked local persistent-install evidence for `memory-context-intelligence@darkwingtm` from `<workspace-root>`.

Exact install command:

```bash
claude plugin install --scope local "memory-context-intelligence@darkwingtm"
```

Observed install output:

```text
Installing plugin "memory-context-intelligence@darkwingtm"...✔ Successfully installed plugin: memory-context-intelligence@darkwingtm (scope: local)
```

## Checked CLI evidence

### Effective marketplace mapping

Command:

```bash
claude plugin marketplace list --json
```

Checked output includes:

```text
name: darkwingtm
source: directory
path: <repo-root>/plugin
installLocation: <repo-root>/plugin
```

### Normal CLI list

Command:

```bash
claude plugin list --json
```

Checked output includes:

```text
id: memory-context-intelligence@darkwingtm
version: 0.9.0
scope: local
enabled: true
installPath: <user-claude-root>/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0
installedAt: 2026-05-19T01:12:34.926Z
lastUpdated: 2026-05-19T01:12:34.926Z
projectPath: <workspace-root>
```

### Bare CLI list

Command:

```bash
claude --bare plugin list --json
```

Checked output includes the same installed plugin entry:

```text
id: memory-context-intelligence@darkwingtm
version: 0.9.0
scope: local
enabled: true
installPath: <user-claude-root>/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0
installedAt: 2026-05-19T01:12:34.926Z
lastUpdated: 2026-05-19T01:12:34.926Z
projectPath: <workspace-root>
```

### Bare CLI details

Command:

```bash
claude --bare plugin details "memory-context-intelligence@darkwingtm"
```

Checked output includes:

```text
memory-context-intelligence 0.9.0
Source: memory-context-intelligence@darkwingtm
Skills (1)  memory-context-intelligence
Agents (4)  source-trust-reviewer, synthesis-lead, trace-scout, research-scout
Hooks (0)
MCP servers (0)
Always-on: ~400 tok added to every session
```

## Runtime/config/cache surfaces observed

Checked local settings surface:

```text
<workspace-root>/.claude/settings.local.json
```

Observed entries:

```text
enabledPlugins.memory-context-intelligence@darkwingtm = true
extraKnownMarketplaces.darkwingtm.source.source = directory
extraKnownMarketplaces.darkwingtm.source.path = <repo-root>/plugin
extraKnownMarketplaces.darkwingtm.installLocation = <repo-root>/plugin
```

Checked user marketplace registry surface:

```text
<user-claude-root>/plugins/known_marketplaces.json
```

Observed `darkwingtm` entry:

```text
source.source = directory
source.path = <repo-root>/plugin
installLocation = <repo-root>/plugin
lastUpdated = 2026-05-19T00:00:00.000Z
```

Checked installed-plugin registry surface:

```text
<user-claude-root>/plugins/installed_plugins.json
```

Observed `memory-context-intelligence@darkwingtm` entry:

```text
scope = local
installPath = <user-claude-root>/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0
version = 0.9.0
installedAt = 2026-05-19T01:12:34.926Z
lastUpdated = 2026-05-19T01:12:34.926Z
gitCommitSha = 67d86e93778c580e324776608c7a9a7900d6920b
projectPath = <workspace-root>
```

Checked cache install surface:

```text
<user-claude-root>/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0
```

Observed cache contents include:

```text
.claude-plugin/
agents/
bin/
changelog/
design/
lib/
patch/
phase/
skills/
tests/
README.md
```

Checked cached plugin manifest:

```text
<user-claude-root>/plugins/cache/darkwingtm/memory-context-intelligence/0.9.0/.claude-plugin/plugin.json
```

Observed manifest identity:

```text
name = memory-context-intelligence
version = 0.9.0
author.name = darkwingtm
author.url = https://github.com/darkwingtm
```

Checked source-side marketplace surface:

```text
<repo-root>/plugin/.claude-plugin/marketplace.json
```

Observed source entry:

```text
name = darkwingtm
plugins[0].name = memory-context-intelligence
plugins[0].source = ./memory-context-intelligence
```

## Observed side effect outside phase repair scope

Normal and bare plugin list output now also show marketplace mismatch errors for existing installed `@darkwingtm` plugins that are not present in the current `<repo-root>/plugin` marketplace root:

```text
claude-session-coordination@darkwingtm: Plugin claude-session-coordination not found in marketplace darkwingtm
frontend-design-pattern-navigator@darkwingtm: Plugin frontend-design-pattern-navigator not found in marketplace darkwingtm
general-expert@darkwingtm: Plugin general-expert not found in marketplace darkwingtm
multi-hat-system@darkwingtm: Plugin multi-hat-system not found in marketplace darkwingtm
supervisor-audit-agent-system@darkwingtm: Plugin supervisor-audit-agent-system not found in marketplace darkwingtm
webview-screenshort@darkwingtm: Plugin webview-screenshort not found in marketplace darkwingtm
```

This phase records the side effect only. It does not expand scope to repair existing installed `@darkwingtm` plugins, shared marketplace normalization, or user-scope installed plugin state.

## Gate

Completed in checked local scope.

The local-scope persistent install proof for `memory-context-intelligence@darkwingtm` is supported by successful install output, normal CLI list evidence, bare CLI list evidence, bare CLI details evidence, and checked local settings/registry/cache surfaces.

## Verification

Verification route: `smoke_check`.

Ran:

```bash
claude plugin install --scope local "memory-context-intelligence@darkwingtm"
claude plugin list --json
claude --bare plugin list --json
claude --bare plugin details "memory-context-intelligence@darkwingtm"
claude plugin marketplace list --json
```

Result: passed in checked local scope for persistent install visibility and details of `memory-context-intelligence@darkwingtm`.

Covers:

- local-scope install command success
- normal CLI installed-plugin visibility
- bare CLI installed-plugin visibility without `--plugin-dir`
- bare CLI details source identity and component inventory
- project-local enablement and marketplace mapping evidence
- user installed-plugin registry and cache install path evidence

Does not cover:

- uninstall lifecycle behavior for `memory-context-intelligence@darkwingtm`
- slash-command/chat invocation behavior
- publication or external marketplace release
- stable/broad production readiness
- main RULES promotion, mutation, or merge
- repair of existing installed `@darkwingtm` plugin marketplace mismatch errors

## Rollback notes

No uninstall is performed in phase 026. Phase 027 is the first darkwingtm uninstall lifecycle closeout gate and remains approval-sensitive because it will mutate the installed local plugin state if selected.

Preserve the source package, governed docs, project-local settings evidence, installed-plugin registry evidence, cache evidence, and `/additional/` trial material unless the user explicitly confirms broader cleanup or deletion.
