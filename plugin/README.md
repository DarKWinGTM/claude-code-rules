# RULES Compact Extension

> **Current Version:** 1.2.6

An optional hook-based plugin companion for `/home/node/workplace/AWCLOUD/TEMPLATE/RULES` that reinforces post-compact re-anchor behavior.

---

## Purpose

This package exists to help Claude Code handle `/compact` more consistently.

It is meant to:
- create one short-lived session-scoped compact handoff before compaction
- extract bounded pre-compact session context as the real carry-forward source
- keep extraction conservative when transcript structure is noisy, rather than pretending objective extraction is perfect
- derive one selected carry-forward payload per source session instead of storing one mixed global blob
- add a short post-compact reminder when the session resumes from `compact`
- emit one short compact-resume signal when that session’s own handoff is applied
- keep one short-lived per-session SessionStart proof file so real compact-resume execution can be verified without turning the package into a history store
- reinforce the RULES contract that compacted carry-forward state must re-anchor to the active objective before continuing

It is **not** meant to:
- replace root RULES authority
- install or manage `~/.claude/rules/`
- act like a second governance stack
- act like a history or audit store for compact payloads
- merge many sessions into one large carry-forward file

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
claude plugins install rules-compact-extension@darkwingtm --scope local
```

Detailed meaning:
1. `cd .../plugin` moves to the package root so the local marketplace manifest resolves correctly.
2. `claude plugins marketplace add ./ --scope local` adds the package-local marketplace declared by `.claude-plugin/marketplace.json`.
3. `claude plugins install rules-compact-extension@darkwingtm --scope local` installs the plugin from that package-local marketplace into local scope.

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
- confirm `rules-compact-extension@darkwingtm` is `enabled`
- inspect `/hooks` if you want to confirm the compact lifecycle hooks are visible from the plugin source
- trigger `/compact` later to observe the session-scoped handoff lifecycle in practice

### Update an installed plugin

Use the installed identifier shape:

```bash
claude plugins update rules-compact-extension@darkwingtm --scope local
```

Why this exact shape matters:
- Claude Code tracks installed plugins by `plugin@marketplace`
- the explicit installed identifier avoids ambiguity when updating
- this package now uses the shared `darkwingtm` marketplace as the maintained runtime label

---

## Runtime contract

### Public runtime surface
- `hooks/hooks.json` = plugin hook configuration
- `scripts/compact-handoff-common.sh` = shared session-state path builders, TTL, extraction, and prune logic
- `scripts/precompact-create-handoff.sh` = creates session-scoped pending/context/carry-forward state before compaction
- `scripts/sessionstart-compact-consume-handoff.sh` = resolves exactly one source session, injects only that session’s carry-forward payload, emits one short compact-resume signal, and records session-scoped proof
- `scripts/postcompact-prune-handoff.sh` = opportunistically prunes stale/orphaned session state

### Active state layout

```text
${CLAUDE_PLUGIN_DATA}/compact/
  index.json
  sessions/
    <source-session-id>/
      pending.json
      precompact-context.json
      carry-forward-selected.json
      sessionstart-proof.json
```

### What each file means
- `index.json`
  - small live routing/cleanup metadata only
  - one entry per live/recent source session
  - no large carry-forward text payloads
- `pending.json`
  - pending-only marker that this source session is waiting for a compact resume
- `precompact-context.json`
  - bounded extracted source context from before compact
- `carry-forward-selected.json`
  - selected carry-forward payload ready for SessionStart injection
- `sessionstart-proof.json`
  - proof-only file for what SessionStart did for that source session
- `sessionstart-directive.json`
  - bounded proof file for the emitted review-required directive and review targets

### Current behavior
- `PreCompact` creates or refreshes per-session state under `${CLAUDE_PLUGIN_DATA}/compact/sessions/<source-session-id>/`
- `SessionStart` with matcher `compact` reads only `index.json`, requires exact `session_id` match against one pending source session, emits a navigator-style compact-resume summary through `systemMessage` with explicit `review-required` wording plus `reviewRoot=` and `review=` pointers, injects a bounded reference-first review directive through `hookSpecificOutput.additionalContext`, names the exact per-session review directory plus `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json`, deletes `pending.json` after successful consume, and writes both `sessionstart-proof.json` and `sessionstart-directive.json`
- current carry-forward extraction is conservative and transcript-heuristic-based, and now fails closed when recent transcript entries are dominated by tool/skill payload text instead of injecting a guessed objective
- `PostCompact` is prune-only and rewrites the live index after cleanup

### How the hook flow works

1. **Before compact**
   - `PreCompact` runs `scripts/precompact-create-handoff.sh`
   - the plugin prunes stale compact state first
   - the plugin creates:
     - `pending.json`
     - `precompact-context.json`
     - `carry-forward-selected.json`
   - state is keyed by `source-session-id`
   - pending state expires after 1 hour if never consumed

2. **After compact resumes**
   - `SessionStart` with matcher `compact` runs `scripts/sessionstart-compact-consume-handoff.sh`
   - if the compact `SessionStart` event matches exactly one pending source session by `session_id`, the script:
     - emits one short navigator-style compact-resume summary through `systemMessage`, explicitly marked `review-required`, including session id, objective/carry/recheck status, `reviewRoot=<compact-root>`, and `review=sessions/<source-session-id>/`
     - injects a bounded reference-first review directive through `hookSpecificOutput.additionalContext`
     - names the exact review directory and the files `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json`
     - limits the injected context to instruction + file pointers + objective status only
     - removes `pending.json`
     - writes `sessionstart-proof.json`
     - writes `sessionstart-directive.json`
     - rewrites `index.json`
   - if routing is ambiguous, the script fails closed:
     - it emits a conservative fallback navigator line through `systemMessage`, explicitly marked `review-required`, including `reviewRoot=<compact-root>` and `review=index.json`
     - it injects a bounded reference-first review directive that points Claude to `index.json` and tells it to re-anchor from verified local context before continuing
     - it writes `sessionstart-directive.json`
     - it does not merge multiple sessions together

3. **After compact completes**
   - `PostCompact` runs `scripts/postcompact-prune-handoff.sh`
   - this is prune-only behavior now, not witness recording
   - expired session directories are removed and the index is rewritten

พูดง่าย ๆ คือ plugin นี้ไม่ได้เอา context ของทุก session มารวมกัน และไม่ได้เก็บ giant JSON ก้อนเดียว แต่แยก state ต่อ source session แล้วค่อย inject เฉพาะ session ที่ match กันจริง ถ้าแยกไม่ได้ก็ไม่เดาและไม่ merge ให้

### Important boundary
The semantic authority remains at `<rules-root>`:
- root runtime rules define what post-compact re-anchor means
- this plugin only reinforces that behavior through supported Claude Code hook mechanics
- the plugin now behaves as a bounded, session-scoped carry-forward cache rather than a compact witness/audit store

---

## Current structure

| Path | Role |
|------|------|
| `.claude-plugin/plugin.json` | package metadata |
| `.claude-plugin/marketplace.json` | package-local marketplace manifest |
| `hooks/hooks.json` | plugin hook configuration |
| `scripts/compact-handoff-common.sh` | shared session-state helper |
| `scripts/*.sh` | compact lifecycle hook scripts |
| `README.md` | package-local install and boundary guide |

---

## Hook and policy notes

- plugin hooks merge with user/project hooks when the plugin is enabled
- managed policy may still block plugin hooks
- this package uses `hooks/hooks.json` for the public plugin hook surface
- it does not depend on a package-local `.claude/settings.json` in this slice
- `hooks/hooks.json` is auto-discovered by Claude Code when the plugin is enabled
- because of that, `plugin.json` must **not** also point `hooks` at `./hooks/hooks.json`
- `plugin.json` should reference hook paths only when you need additional non-default hook files beyond the standard `hooks/hooks.json`

### Compact-resume signal note
Current checked official hook docs verify:
- `hookSpecificOutput.additionalContext` for `SessionStart` as Claude/model context
- `systemMessage` as a warning message shown to the user
- plain stdout text being added as context for Claude

The checked docs do **not** document a separate dedicated `SessionStart` hook status-line field.

So this package carries the compact-resume line through `systemMessage` for the user-visible signal and uses `hookSpecificOutput.additionalContext` as a bounded reference-first review-trigger channel for Claude/model context, naming the exact stored review files before continuation without replaying old context aggressively.

### Ambiguous-session safety note
When more than one pending source session exists, the plugin should fail closed rather than inject a guessed carry-forward payload.

That means:
- no multi-session merge
- no “latest wins” overwrite policy for injection
- no guessed session selection when exact routing is unclear

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

If `${CLAUDE_PLUGIN_DATA}` is available, this package uses:

```text
${CLAUDE_PLUGIN_DATA}/compact/index.json
${CLAUDE_PLUGIN_DATA}/compact/sessions/<source-session-id>/pending.json
${CLAUDE_PLUGIN_DATA}/compact/sessions/<source-session-id>/precompact-context.json
${CLAUDE_PLUGIN_DATA}/compact/sessions/<source-session-id>/carry-forward-selected.json
${CLAUDE_PLUGIN_DATA}/compact/sessions/<source-session-id>/sessionstart-proof.json
```

These files are:
- short-lived
- pruned opportunistically if expired or malformed
- separated per source session rather than merged together globally
- limited to routing metadata, bounded extracted context, selected carry-forward payload, and proof-only state

Expected active-state contract:
- one source session gets one directory under `sessions/`
- `pending.json` exists only while that source session is waiting for consume
- `sessionstart-proof.json` exists briefly after SessionStart handling
- expired session directories are removed rather than left behind forever
- legacy singleton files such as `active-handoff.json`, `last-sessionstart-consumed.json`, `last-precompact.json`, `last-postcompact.json`, and `last-sessionstart-compact.json` are treated as old-state leftovers and pruned

These files are bounded runtime state only, not governance authority.
