# RULES Plugin Extension

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.1
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e (2026-04-06)

---

## 1) Goal

Define the optional `plugin/` companion area for `/home/node/workplace/AWCLOUD/TEMPLATE/RULES` so hook-based compact handling can be packaged cleanly without weakening root RULES authority.

The target behavior is:
- root RULES remain the semantic owner for compact / post-compact behavior
- `plugin/` remains an optional extension package that reinforces those semantics through supported Claude Code hook mechanics
- plugin implementation files live under `plugin/`
- root design / changelog / TODO / phase / patch artifacts remain the only governance stack

---

## 2) Problem Statement

The RULES repository now needs two things at once:
- stronger post-compact behavior in the root rule owners
- a reusable hook package that can reinforce that behavior in runtime

Without an explicit model, the repository risks two opposite failures:
- plugin-first drift, where the plugin starts to look like the new authority instead of an extension
- duplicate governance drift, where `plugin/` grows its own design/phase/changelog/TODO stack and competes with the root repository authority

This design closes that gap by making the plugin package explicit while keeping its authority boundaries narrow.

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

Optional surfaces only when truly needed:
- `plugin/skills/` = operator-facing helper front door
- `plugin/agents/` = companion runtime agent surface

### 3.3 Current first-pass scope

The first slice should stay hook-first and narrow:
- `SessionStart` with matcher `compact` for post-compact re-anchor context injection
- `PreCompact` for compact-event witness recording
- `PostCompact` for compact-event witness recording

This first slice should not create a broad agent fleet or unrelated plugin capability surface.

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
- record compact lifecycle witness files into `${CLAUDE_PLUGIN_DATA}`

The plugin may not:
- redefine compact semantics independently of root rules
- replace root rules installation
- create a second design/changelog/phase/TODO authority tree under `plugin/`

### 4.3 Non-goals

This first extension design does not aim to:
- convert the RULES system into a plugin-first architecture
- create a new runtime rule chain for plugin packaging itself
- make managed-policy assumptions that plugin hooks always run
- bundle unrelated agents/skills just because the package format allows them

---

## 5) Install and Runtime Posture

### 5.1 Source-side path

Package-local install commands should run from:
- `<repo-root>/plugin`

### 5.2 Package-local install model

Preferred package-local activation:
- `claude plugins marketplace add ./ --scope local`
- `claude plugins install rules-compact-extension@rules-compact-extension --scope local`

### 5.4 Detailed package-local install / runtime notes

The public install path should be documented from `<repo-root>/plugin`.

Required guidance:
- package-local install commands should show `claude plugins marketplace add ./ --scope local`
- install commands should use the explicit installed identifier form `rules-compact-extension@rules-compact-extension`
- docs should explain that `hooks/hooks.json` is auto-discovered by Claude Code when the plugin is enabled
- docs should explain that `plugin.json` must not duplicate that same default hook path under a `hooks` field unless additional non-default hook files are being layered in
- docs should show the practical runtime behavior of `SessionStart` / `PreCompact` / `PostCompact`
- docs should identify the expected witness files under `${CLAUDE_PLUGIN_DATA}/compact/`

### 5.5 Current first-pass hook mechanics

The current first-pass mechanics are:
- `SessionStart` with matcher `compact` injects a short post-compact re-anchor reminder into the resumed session
- `PreCompact` records the raw event payload to `${CLAUDE_PLUGIN_DATA}/compact/last-precompact.json`
- `PostCompact` records the raw event payload to `${CLAUDE_PLUGIN_DATA}/compact/last-postcompact.json`

This keeps the package small and directly aligned with the compact lifecycle instead of widening into unrelated automation.

## 6) Verification Targets

The extension design is successful when:
- `plugin/` exists and matches the intended package-local scaffold
- root RULES docs continue to teach rules-first, plugin-second behavior
- no root docs imply plugin authority replaces root runtime rules
- plugin README install/use guidance is expressed from `<repo-root>/plugin`
- plugin metadata and hook config are coherent
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
