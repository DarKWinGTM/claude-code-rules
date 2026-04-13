# RULES Plugin Extension

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.13
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-13)

---

## 1) Goal

Define the optional `plugin/` companion area for `<rules-root>` so the RULES plugin remains one unified Rules-owned package that combines compact lifecycle reinforcement and the session-coordination support skill without weakening root RULES authority.

The target behavior is:
- root RULES remain the semantic owner for compact / post-compact behavior and cross-session coordination semantics
- `plugin/` remains the single canonical source for the Rules plugin package
- the unified plugin package exposes both:
  - compact lifecycle hooks
  - one operator-facing session coordination support skill
- the public install target is `claude-code-rules@darkwingtm`
- duplicate maintained package copies under the shared marketplace workspace are no longer the intended model

---

## 2) Problem Statement

The RULES plugin surface must solve two jobs together:
- reinforce compact/post-compact behavior in runtime
- provide a bounded operator-facing coordination skill

Without an explicit unified model, the system risks:
- plugin-first drift, where the plugin starts to look like authority instead of extension
- duplicate-source drift, where the same plugin is maintained in several places
- compact-helper split drift, where hook behavior and coordination skill behavior live in different package sources and confuse installation or ownership
- marketplace confusion, where users cannot tell which plugin id is the real Rules plugin

This design closes those gaps by keeping one canonical Rules-owned plugin source while still exposing the package through the shared `darkwingtm` marketplace.

---

## 3) Active Extension Model

### 3.1 Boundary principle

`plugin/` is an optional support / extension area.
It is not a second rule layer.
It is not a replacement for `~/.claude/rules/`.
It is not a second governed workspace.

### 3.2 Package model

The unified Rules plugin package lives at:
- `<rules-root>/plugin`

Active package surface:
- `plugin/README.md` = package-local install / usage / boundary guide
- `plugin/.claude-plugin/plugin.json` = package metadata
- `plugin/.claude-plugin/marketplace.json` = package-local development marketplace manifest
- `plugin/hooks/hooks.json` = compact lifecycle hook configuration
- `plugin/scripts/*.sh` = compact lifecycle scripts called by the plugin hooks
- `plugin/skills/session-coordination-bridge/` = operator-facing support skill for session coordination workflow

Optional surfaces only when truly needed:
- additional `plugin/skills/` entries beyond the current coordination bridge
- `plugin/agents/` = companion runtime agent surface

### 3.3 Current active scope

The active slice is intentionally unified but bounded:
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

The unified plugin may:
- reinforce compact/post-compact behavior through supported hooks
- inject bounded post-compact reminder context where Claude Code supports it
- emit one short compact-resume signal through the user-visible `systemMessage` SessionStart hook output field
- keep per-session compact state in `${CLAUDE_PLUGIN_DATA}`
- keep bounded SessionStart proof files so real compact-resume execution can be verified without turning the package into a history store
- expose one operator-facing session coordination support skill under the plugin namespace
- prune expired, malformed, consumed, or legacy compact-state leftovers opportunistically

The unified plugin may not:
- redefine compact semantics independently of root rules
- replace root rules installation
- create a second design/changelog/phase/TODO authority tree under `plugin/`
- act like a compact witness or audit store
- act like the semantic owner of shared-board coordination behavior
- merge many sessions’ carry-forward content into one giant active file

### 4.3 Non-goals

This extension design does not aim to:
- convert the RULES system into a plugin-first architecture
- create a new runtime rule chain for plugin packaging itself
- make managed-policy assumptions that plugin hooks always run
- bundle unrelated agents/skills just because the package format allows them
- preserve raw compact payload history as part of the active runtime contract
- store a full transcript copy per session in plugin state
- maintain duplicate package copies as co-equal sources of truth

---

## 5) Install and Runtime Posture

### 5.0 Path notation

- `<rules-root>` = the RULES repository root
- `<plugin-marketplace-root>` = the shared plugin marketplace root that contains the `darkwingtm` aggregate marketplace

### 5.1 Canonical source path

The canonical plugin source is:
- `<rules-root>/plugin`

### 5.2 Public install model

Preferred public activation:
- `claude plugins marketplace add "<plugin-marketplace-root>" --scope user`
- `claude plugins install claude-code-rules@darkwingtm --scope user`

The shared marketplace may expose the plugin by pointing its `claude-code-rules` entry back to `<rules-root>/plugin`.

### 5.3 Local development model

Local development activation remains:
- `claude plugins marketplace add ./ --scope local`
- `claude plugins install claude-code-rules@claude-code-rules --scope local`

### 5.4 Detailed package-local install / runtime notes

Required guidance:
- public install docs should show the shared `darkwingtm` marketplace path through `<plugin-marketplace-root>`
- the intended user-facing installed identifier should be `claude-code-rules@darkwingtm`
- package-local `@claude-code-rules` docs should be framed as local development/testing only
- docs should identify the operator-facing skill path under `skills/session-coordination-bridge/`
- docs should show the practical runtime behavior of `SessionStart` / `PreCompact` / `PostCompact`
- docs should identify the active session-scoped compact state layout
- docs should explain that the package no longer uses singleton `last-*.json` witness files as the active contract
- docs should not imply a second maintained package source is needed for the same plugin

### 5.5 Current active mechanics

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

### 5.7 SessionStart routing rule

The plugin should route conservatively:
1. read only `index.json`
2. require exact `session_id` equality between the compact `SessionStart` event and one pending source session
3. if that exact match exists, inject only that session’s `carry-forward-selected.json`
4. if no exact match exists, inject only a bounded reference-first review directive pointing to `index.json` and record a non-success proof state
5. never merge multiple sessions together
6. do not use `additionalContext` as a hidden context-restore channel; keep it instruction + locator + bounded status only

---

## 6) Verification Targets

The extension design is successful when:
- `plugin/` exists and matches the intended package-local scaffold
- root RULES docs continue to teach rules-first, plugin-second behavior
- no root docs imply plugin authority replaces root runtime rules
- public install guidance points users to `claude-code-rules@darkwingtm`
- the package-local install path remains clearly development-only
- plugin metadata, hook surface, skill surface, and docs are coherent together
- the coordination skill remains an operator bridge and does not masquerade as semantic truth
- the active runtime contract uses a small live index plus per-session compact state directories rather than singleton mixed files
- SessionStart emits a bounded reference-first review directive for only one resolved session and does not replay old context text aggressively
- ambiguous multi-session routing fails closed instead of guessing
- duplicate maintained package copies are not required for the public install model
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
