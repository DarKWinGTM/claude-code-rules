# Claude Code Rules Plugin Companion

> **Current Version:** 1.5.0

A unified plugin companion for `<rules-root>` that combines the compact/context helper and the session coordination support skill in one Rules-owned package.

---

## Purpose

This package exists to keep the RULES plugin surface unified.

It is meant to:
- reinforce RULES compact/post-compact behavior through supported Claude Code hooks
- create one short-lived session-scoped compact handoff before compaction
- extract bounded pre-compact session context as the real carry-forward source
- emit review-required compact-resume signals and bounded re-anchor context on resume
- expose `/claude-code-rules:session-coordination-bridge` as an operator-facing support skill for cross-session coordination workflow

It is **not** meant to:
- replace root RULES authority
- install or manage `~/.claude/rules/`
- act like a second governance stack
- replace the shared task board, phase, TODO, or checked implementation state as coordination truth
- turn optional recall or peer signaling into required infrastructure

---

## Path notation

- `<rules-root>` = the RULES repository root
- `<plugin-root>` = `<rules-root>/plugin`
- `<plugin-marketplace-root>` = the shared plugin marketplace root that contains the `darkwingtm` aggregate marketplace
- `<plugin-data>` = `${CLAUDE_PLUGIN_DATA}` persistent plugin data directory

---

## Installation and activation

### Recommended public install

```bash
claude plugins marketplace add "<plugin-marketplace-root>" --scope user
claude plugins install claude-code-rules@darkwingtm --scope user
```

### Local development install

```bash
cd <plugin-root>
claude plugins marketplace add ./ --scope local
claude plugins install claude-code-rules@claude-code-rules --scope local
```

### Update

Public update:

```bash
claude plugins update claude-code-rules@darkwingtm --scope user
```

Local development update:

```bash
claude plugins update claude-code-rules@claude-code-rules --scope local
```

### Migration note

If an older `rules-compact-extension@darkwingtm` install is still active, migrate to the unified package:

```bash
claude plugins uninstall rules-compact-extension@darkwingtm --scope user
claude plugins install claude-code-rules@darkwingtm --scope user
```

---

## Verification

Check installed state:

```bash
claude plugins list --json
```

Optional interactive checks:
- `/reload-plugins`
- `/claude-code-rules:session-coordination-bridge`
- `/hooks`

What you should see:
- `claude-code-rules@darkwingtm` enabled for the public install path
- compact lifecycle hooks visible through the plugin hook surface
- the skill `/claude-code-rules:session-coordination-bridge` available

---

## Runtime contract

### Public runtime surface
- `hooks/hooks.json` = compact lifecycle hook configuration
- `scripts/compact-handoff-common.sh` = shared session-state path builders, TTL, extraction, and prune logic
- `scripts/precompact-create-handoff.sh` = creates session-scoped pending/context/carry-forward state before compaction
- `scripts/sessionstart-compact-consume-handoff.sh` = resolves exactly one source session, injects only that session’s carry-forward payload, emits one short compact-resume signal, and records session-scoped proof
- `scripts/postcompact-prune-handoff.sh` = opportunistically prunes stale/orphaned session state
- `skills/session-coordination-bridge/SKILL.md` = operator-facing support skill for shared-board and optional-tool coordination workflow
- `skills/session-coordination-bridge/*.md` = focused support docs for coordination model, capability detection, flow, request contract, and examples

### Current behavior
- this package owns the compact helper again
- this package also exposes the `session-coordination-bridge` skill
- compact behavior and coordination skill now ship from the same Rules-owned plugin source
- the intended user-facing install path is `claude-code-rules@darkwingtm`
- the package-local `claude-code-rules@claude-code-rules` path is for local development/testing only

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
      sessionstart-directive.json
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

### Current compact behavior
- `PreCompact` creates or refreshes per-session state under `${CLAUDE_PLUGIN_DATA}/compact/sessions/<source-session-id>/`
- `SessionStart` with matcher `compact` reads only `index.json`, requires exact `session_id` match against one pending source session, emits a navigator-style compact-resume summary through `systemMessage`, injects a bounded reference-first review directive through `hookSpecificOutput.additionalContext`, and records proof/directive files
- `PostCompact` is prune-only and rewrites the live index after cleanup
- current carry-forward extraction stays conservative and fails closed when objective extraction is too noisy

### Coordination skill behavior
- `skills/session-coordination-bridge/` provides an operator-facing support surface for shared-board coordination workflow, optional recall detection, request-vs-execution remap, and sync-back discipline
- task list remains the coordination board
- phase/TODO/design/code remain semantic truth
- memsearch remains optional recall support
- `claude-peers-mcp` remains optional live signaling

### Current structure

| Path | Role |
|------|------|
| `.claude-plugin/plugin.json` | package metadata |
| `.claude-plugin/marketplace.json` | package-local development marketplace manifest |
| `hooks/hooks.json` | compact lifecycle hook configuration |
| `scripts/*.sh` | compact lifecycle helper scripts |
| `skills/session-coordination-bridge/` | operator-facing session coordination support skill |
| `README.md` | package-local install and boundary guide |

---

## Important boundary

The semantic authority remains at `<rules-root>`:
- root runtime rules define compact/post-compact semantics
- root runtime rules define coordination semantics and the meaning of the shared execution model
- this plugin reinforces those semantics through compact hooks plus one support skill front door
