# RULES Plugin Extension

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.10
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-13)

---

## 1) Goal

Define the optional `plugin/` companion area for `/home/node/workplace/AWCLOUD/TEMPLATE/RULES` so compact lifecycle hooks and an optional session-coordination support skill can be packaged cleanly without weakening root RULES authority.

The target behavior is:
- root RULES remain the semantic owner for compact / post-compact behavior and cross-session coordination semantics
- `plugin/` remains an optional extension package that reinforces those semantics through supported Claude Code hook mechanics plus one operator-facing support skill
- plugin implementation files live under `plugin/`
- root design / changelog / TODO / phase / patch artifacts remain the only governance stack

---

## 2) Problem Statement

The RULES repository now needs three things at once:
- stronger post-compact behavior in the root rule owners
- a reusable hook package that can reinforce that behavior in runtime
- an optional operator-facing skill front door for session-coordination workflow that does not turn the plugin into a second authority stack

Without an explicit model, the repository risks several failures:
- plugin-first drift, where the plugin starts to look like the new authority instead of an extension
- duplicate governance drift, where `plugin/` grows its own design/phase/changelog/TODO stack and competes with the root repository authority
- skill-front-door drift, where the support skill starts to masquerade as semantic truth instead of an operator bridge
- optional-tool assumption drift, where memsearch or peer signaling is treated like guaranteed infrastructure instead of optional capability
- singleton-state drift, where one compact file or one proof file quietly mixes several sessions together
- file-bloat drift, where carrying too much context into one file becomes the new hidden failure mode

This design closes those gaps by keeping the package narrow, session-scoped, and bounded.

---

## 3) Active Extension Model

### 3.1 Boundary principle

`plugin/` is an optional support / extension area.
It is not a second rule layer.
It is not a replacement for `~/.claude/rules/`.
It is not a second governed workspace.

### 3.2 Package model

The package should follow the package-local plugin pattern already used under `/home/node/workplace/AWCLOUD/TEMPLATE/PLUGIN/`.

Active package surface:
- `plugin/README.md` = package-local install / usage / boundary guide
- `plugin/.claude-plugin/plugin.json` = package metadata
- `plugin/.claude-plugin/marketplace.json` = package-local marketplace manifest
- `plugin/hooks/hooks.json` = plugin hook configuration
- `plugin/scripts/*.sh` = compact lifecycle scripts called by the plugin hooks
- `plugin/skills/session-coordination-bridge/` = operator-facing support skill for session coordination workflow

Optional surfaces only when truly needed:
- additional `plugin/skills/` entries beyond the current coordination bridge
- `plugin/agents/` = companion runtime agent surface

### 3.3 Current active scope

The active slice stays bounded:
- `SessionStart` with matcher `compact` for post-compact re-anchor injection plus one short compact-resume signal
- `PreCompact` for session-scoped handoff/context extraction
- `PostCompact` for prune-only cleanup
- `skills/session-coordination-bridge/` for operator-facing shared-board and optional-tool coordination guidance

This slice should not create a broad agent fleet, unrelated plugin capability surface, or a second semantic coordination authority.

---

## 4) Authority and Non-Goals

### 4.1 Root authority remains here

Root RULES authority remains in:
- root runtime rules
- `design/*.design.md`
- `changelog/*.changelog.md`
- `TODO.md`
- `phase/`
- `patch/`

### 4.2 Plugin role

The plugin may:
- reinforce compact/post-compact behavior through supported hooks
- inject bounded post-compact reminder context where Claude Code supports it
- emit one short compact-resume signal through the user-visible `systemMessage` SessionStart hook output field
- keep per-session compact state in `${CLAUDE_PLUGIN_DATA}`
- keep bounded SessionStart proof files so real compact-resume execution can be verified without turning the package into a history store
- expose one operator-facing session coordination support skill under the plugin namespace
- prune expired, malformed, consumed, or legacy compact-state leftovers opportunistically

The plugin may not:
- redefine compact semantics independently of root rules
- replace root rules installation
- create a second design/changelog/phase/TODO authority tree under `plugin/`
- act like a compact witness or audit store
- act like the semantic owner of shared-board coordination behavior
- merge multiple sessions’ carry-forward content into one giant active file

### 4.3 Non-goals

This extension design does not aim to:
- convert the RULES system into a plugin-first architecture
- create a new runtime rule chain for plugin packaging itself
- make managed-policy assumptions that plugin hooks always run
- bundle unrelated agents/skills just because the package format allows them
- preserve raw compact payload history as part of the active runtime contract
- store a full transcript copy per session in plugin state

---

## 5) Install and Runtime Posture

### 5.1 Source-side path

Package-local install commands should run from:
- `<repo-root>/plugin`

### 5.2 Package-local install model

Preferred package-local activation:
- `claude plugins marketplace add ./ --scope local`
- `claude plugins install claude-code-rules@claude-code-rules --scope local`

### 5.4 Detailed package-local install / runtime notes

The public install path should be documented from `<repo-root>/plugin`.

Required guidance:
- package-local install commands should show `claude plugins marketplace add ./ --scope local`
- install commands should use the explicit installed identifier form `claude-code-rules@claude-code-rules`
- docs should explain the migration path from the older `rules-compact-extension@darkwingtm` install when relevant
- docs should explain that `hooks/hooks.json` is auto-discovered by Claude Code when the plugin is enabled
- docs should explain that `plugin.json` must not duplicate that same default hook path under a `hooks` field unless additional non-default hook files are being layered in
- docs should show the practical runtime behavior of `SessionStart` / `PreCompact` / `PostCompact`
- docs should identify the active session-scoped compact state layout
- docs should identify the operator-facing skill path under `skills/session-coordination-bridge/`
- docs should explain that the package no longer uses singleton `last-*.json` witness files as the active contract

### 5.5 Current active hook and skill mechanics

The current active mechanics are:
- `PreCompact` prunes stale state and creates/refreshes one session-scoped compact state directory keyed by source `session_id`
- `SessionStart` with matcher `compact` emits one short navigator-style compact-resume summary through `systemMessage`, now explicitly marked as `review-required`, including `reviewRoot=` plus `review=` pointers into stored session state
- success-path `hookSpecificOutput.additionalContext` stays reference-first and bounded: one short review-required instruction, the exact review directory plus `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json`, one short objective-status line, and one short discipline reminder against replay-based continuation
- fallback SessionStart behavior remains fail-closed, marks review as required, points Claude to `index.json`, and re-anchors from verified local context when exact session routing does not resolve
- `PostCompact` is prune-only and no longer records raw witness payloads
- `skills/session-coordination-bridge/` provides an operator-facing support surface for shared-board workflow, optional recall detection, request-vs-execution remap boundaries, and sync-back discipline
- pending state and proof state both expire after 1 hour and are pruned opportunistically by later hook runs
- memsearch remains a later assist-layer boundary rather than an active runtime dependency in this wave
- `claude-peers-mcp` remains an optional later signaling layer rather than an active package dependency in this wave

The active layout under `${CLAUDE_PLUGIN_DATA}/compact/` is:

```text
index.json
sessions/
  <source-session-id>/
    pending.json
    precompact-context.json
    carry-forward-selected.json
    sessionstart-proof.json
    sessionstart-directive.json
```

### 5.6 Carry-forward data model

The plugin should treat pre-compact source state as the real source of carry-forward selection.

That means:
- `precompact-context.json` is the bounded extracted source-of-truth file
- `carry-forward-selected.json` is the derived selected injection payload
- `index.json` is routing/cleanup metadata only
- `sessionstart-proof.json` is proof-only
- `sessionstart-directive.json` is bounded directive proof for what review instruction was emitted at SessionStart

Do not store:
- one giant all-session JSON blob
- full transcript copies inside plugin state
- raw compact summary as the primary source of carry-forward truth

Current bounded limitation:
- transcript extraction may still be noisy when the latest user-visible transcript entries are dominated by tool/skill payload text rather than a clean natural-language objective
- in that case the plugin now fails closed on objective extraction and keeps a `needsRecheck` marker instead of injecting a guessed objective

### 5.7 SessionStart routing rule

The plugin should route conservatively:
1. read only `index.json`
2. require exact `session_id` equality between the compact `SessionStart` event and one pending source session
3. if that exact match exists, inject only that session’s `carry-forward-selected.json`
4. if no exact match exists, inject only a bounded reference-first review directive pointing to `index.json` and record a non-success proof state
5. never merge multiple sessions together
6. do not use `additionalContext` as a hidden context-restore channel; keep it instruction + locator + bounded status only

The strongest currently verified key is:
- `session_id`

Transcript location is derivable from that key as:
- `/home/node/.claude/projects/-home-node-workplace-AWCLOUD-CLAUDE/<session-id>.jsonl`

---

## 6) Verification Targets

The extension design is successful when:
- `plugin/` exists and matches the intended package-local scaffold
- root RULES docs continue to teach rules-first, plugin-second behavior
- no root docs imply plugin authority replaces root runtime rules
- plugin README install/use guidance is expressed from `<repo-root>/plugin`
- plugin metadata, skill surface, and hook config are coherent
- the active runtime contract uses a small live index plus per-session compact state directories rather than singleton mixed files
- SessionStart emits a bounded reference-first review directive for only one resolved session and does not replay old context text aggressively
- ambiguous multi-session routing fails closed instead of guessing
- the coordination skill remains an operator bridge and does not masquerade as semantic truth
- plugin files stay implementation-only while root docs remain governance-only

---

## 7) Integration

Related documents:
- `design/design.md`
- `project-documentation-standards.md`
- `accurate-communication.md`
- `authority-and-scope.md`
- `evidence-grounded-burden-of-proof.md`
- `explanation-quality.md`
- `answer-presentation.md`

---

> Full history: [../changelog/rules-plugin-extension.changelog.md](../changelog/rules-plugin-extension.changelog.md)
