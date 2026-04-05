# RULES Compact Extension

> **Current Version:** 1.0.1

An optional hook-based plugin companion for `/home/node/workplace/AWCLOUD/TEMPLATE/RULES` that reinforces post-compact re-anchor behavior.

---

## Purpose

This package exists to help Claude Code handle `/compact` more consistently.

It is meant to:
- record compact lifecycle events
- add a short post-compact reminder at `SessionStart` when the session resumes from `compact`
- reinforce the RULES contract that compacted carry-forward state must re-anchor to the active objective before continuing

It is **not** meant to:
- replace root RULES authority
- install or manage `~/.claude/rules/`
- act like a second governance stack

---

## Path notation

- `<rules-root>` = the RULES repository root
- `<plugin-root>` = `<rules-root>/plugin`
- `<plugin-data>` = `${CLAUDE_PLUGIN_DATA}` persistent plugin data directory

---

## Installation and activation

Run from `<plugin-root>`.

### Recommended first-time install

```bash
cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin
claude plugins marketplace add ./ --scope local
claude plugins install rules-compact-extension@rules-compact-extension --scope local
```

Detailed meaning:
1. `cd .../plugin` moves to the package root so the local marketplace manifest resolves correctly.
2. `claude plugins marketplace add ./ --scope local` adds the package-local marketplace declared by `.claude-plugin/marketplace.json`.
3. `claude plugins install rules-compact-extension@rules-compact-extension --scope local` installs the plugin from that package-local marketplace into local scope.

### Reload and verification

Optional reload:

```bash
/reload-plugins
```

Check installed state:

```bash
claude plugins list
```

Practical verification after reload:
- confirm `rules-compact-extension@rules-compact-extension` is `enabled`
- inspect `/hooks` if you want to confirm the compact lifecycle hooks are visible from the plugin source
- trigger `/compact` later to observe the re-anchor behavior in practice

### Update an installed plugin

Use the installed identifier shape:

```bash
claude plugins update rules-compact-extension@rules-compact-extension --scope local
```

Why this exact shape matters:
- Claude Code tracks installed plugins by `plugin@marketplace`
- the explicit installed identifier avoids ambiguity when updating
- this package already validated that the local installed identity is `rules-compact-extension@rules-compact-extension`

---

## Runtime contract

### Public runtime surface
- `hooks/hooks.json` = plugin hook configuration
- `scripts/sessionstart-compact-reanchor.sh` = injects post-compact reminder context at `SessionStart` with matcher `compact`
- `scripts/precompact-record.sh` = records `PreCompact` input into `<plugin-data>/compact/`
- `scripts/postcompact-record.sh` = records `PostCompact` input into `<plugin-data>/compact/`

### Current behavior
- `SessionStart` with matcher `compact` adds one short post-compact reminder to Claude context
- `PreCompact` records raw event input for bounded local evidence
- `PostCompact` records raw event input for bounded local evidence

### How the hook flow works

1. **Before compact**
   - `PreCompact` runs `scripts/precompact-record.sh`
   - the raw hook input is stored under `${CLAUDE_PLUGIN_DATA}/compact/last-precompact.json`

2. **After compact resumes**
   - `SessionStart` with matcher `compact` runs `scripts/sessionstart-compact-reanchor.sh`
   - that script emits `additionalContext` so Claude sees a short re-anchor reminder in the new compacted session

3. **After compact completes**
   - `PostCompact` runs `scripts/postcompact-record.sh`
   - the raw hook input is stored under `${CLAUDE_PLUGIN_DATA}/compact/last-postcompact.json`

พูดง่าย ๆ คือ plugin นี้ไม่ได้ “คิดแทน rules” แต่คอยเตือน Claude ตอน session กลับมาหลัง compact และเก็บ compact-event witness ไว้สำหรับตรวจย้อนหลัง

### Important boundary
The semantic authority remains at `<rules-root>`:
- root runtime rules define what post-compact re-anchor means
- this plugin only reinforces that behavior through supported Claude Code hook mechanics

---

## Current structure

| Path | Role |
|------|------|
| `.claude-plugin/plugin.json` | package metadata |
| `.claude-plugin/marketplace.json` | package-local marketplace manifest |
| `hooks/hooks.json` | plugin hook configuration |
| `scripts/*.sh` | compact lifecycle hook scripts |
| `README.md` | package-local install and boundary guide |

---

## Hook and policy notes

- plugin hooks merge with user/project hooks when the plugin is enabled
- managed policy may still block plugin hooks
- this package uses `hooks/hooks.json` for the public plugin hook surface
- it does not depend on a package-local `.claude/settings.json` in this first slice
- `hooks/hooks.json` is auto-discovered by Claude Code when the plugin is enabled
- because of that, `plugin.json` must **not** also point `hooks` at `./hooks/hooks.json`
- `plugin.json` should reference hook paths only when you need additional non-default hook files beyond the standard `hooks/hooks.json`

### Troubleshooting

#### Duplicate hook load error
If you see an error like:

```text
Duplicate hooks file detected: ./hooks/hooks.json ... The standard hooks/hooks.json is loaded automatically
```

that means the package declared the same hook file twice.

Correct package pattern:
- keep `hooks/hooks.json` at the package root
- do **not** duplicate it in `.claude-plugin/plugin.json`

#### Plugin installed but effect not visible yet
- run `/reload-plugins`
- run `claude plugins list`
- inspect `/hooks` if you want to see whether compact hook entries are visible
- remember that this package does most of its user-visible work only when the session resumes from `compact`

---

## What persists

If `${CLAUDE_PLUGIN_DATA}` is available, this package stores compact-event witness files under:

```text
${CLAUDE_PLUGIN_DATA}/compact/
```

Expected files include:
- `last-precompact.json`
- `last-postcompact.json`
- `last-sessionstart-compact.json`

Those files are runtime evidence only, not governance authority.
