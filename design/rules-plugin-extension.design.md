# RULES Plugin Extension

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.11
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-13)

---

## 1) Goal

Define the optional `plugin/` companion area for `<rules-root>` so one session-coordination support skill can be packaged cleanly without weakening root RULES authority or overlapping the real compact helper.

The target behavior is:
- root RULES remain the semantic owner for compact / post-compact behavior and cross-session coordination semantics
- `plugin/` remains an optional extension package that exposes one operator-facing support skill only
- compact lifecycle helper ownership remains with `rules-compact-extension`
- plugin implementation files live under `plugin/`
- root design / changelog / TODO / phase / patch artifacts remain the only governance stack

---

## 2) Problem Statement

The RULES repository now needs one bounded extension outcome in this slice:
- an optional operator-facing skill front door for session-coordination workflow that does not turn the plugin into a second authority stack and does not duplicate the already-active compact helper

Without an explicit model, the repository risks several failures:
- plugin-first drift, where the plugin starts to look like the new authority instead of an extension
- duplicate governance drift, where `plugin/` grows its own design/phase/changelog/TODO stack and competes with the root repository authority
- skill-front-door drift, where the support skill starts to masquerade as semantic truth instead of an operator bridge
- optional-tool assumption drift, where memsearch or peer signaling is treated like guaranteed infrastructure instead of optional capability
- compact-helper overlap drift, where the skill package duplicates the already-active `rules-compact-extension` helper role instead of staying narrowly focused

This design closes those gaps by keeping the package narrow, session-scoped, and bounded.

---

## 3) Active Extension Model

### 3.1 Boundary principle

`plugin/` is an optional support / extension area.
It is not a second rule layer.
It is not a replacement for `~/.claude/rules/`.
It is not a second governed workspace.

### 3.2 Package model

The package should follow the package-local plugin pattern already used under the shared plugin marketplace workspace `<plugin-marketplace-root>`.

Active package surface:
- `plugin/README.md` = package-local install / usage / boundary guide
- `plugin/.claude-plugin/plugin.json` = package metadata
- `plugin/.claude-plugin/marketplace.json` = package-local development marketplace manifest
- `plugin/skills/session-coordination-bridge/` = operator-facing support skill for session coordination workflow

Optional surfaces only when truly needed:
- additional `plugin/skills/` entries beyond the current coordination bridge
- `plugin/agents/` = companion runtime agent surface

### 3.3 Current active scope

The active slice stays bounded:
- `skills/session-coordination-bridge/` for operator-facing shared-board and optional-tool coordination guidance

This slice should not create a broad agent fleet, unrelated plugin capability surface, a second semantic coordination authority, or a duplicate compact-helper package.

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
- expose one operator-facing session coordination support skill under the plugin namespace
- provide bounded support docs for shared-board workflow, optional recall detection, request-vs-execution remap, and sync-back discipline

The plugin may not:
- redefine compact semantics independently of root rules
- replace root rules installation
- create a second design/changelog/phase/TODO authority tree under `plugin/`
- act like a compact witness or audit store
- act like the semantic owner of shared-board coordination behavior
- own compact lifecycle hooks or compact persistence state while `rules-compact-extension` remains the active helper

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

### 5.0 Path notation

- `<rules-root>` = the RULES repository root
- `<plugin-marketplace-root>` = the shared plugin marketplace root that contains the `darkwingtm` aggregate marketplace

### 5.1 Source-side path

Package-local install commands should run from:
- `<rules-root>/plugin`

### 5.2 Package-local install model

Preferred public activation:
- `claude plugins marketplace add "<plugin-marketplace-root>" --scope user`
- `claude plugins install claude-code-rules@darkwingtm --scope user`

Local development activation remains:
- `claude plugins marketplace add ./ --scope local`
- `claude plugins install claude-code-rules@claude-code-rules --scope local`

### 5.4 Detailed package-local install / runtime notes

The public install path should be documented from `<rules-root>/plugin`.

Required guidance:
- public install docs should show the shared `darkwingtm` marketplace path
- the intended user-facing installed identifier should be `claude-code-rules@darkwingtm`
- package-local `@claude-code-rules` docs should be framed as local development/testing only
- docs should explain that `rules-compact-extension@darkwingtm` remains the active compact helper
- docs should identify the operator-facing skill path under `skills/session-coordination-bridge/`
- docs should not claim that this package owns `SessionStart` / `PreCompact` / `PostCompact`

### 5.5 Current active skill mechanics

The current active mechanics are:
- `skills/session-coordination-bridge/` provides an operator-facing support surface for shared-board workflow, optional recall detection, request-vs-execution remap boundaries, and sync-back discipline
- memsearch remains a later assist-layer boundary rather than an active runtime dependency in this wave
- `claude-peers-mcp` remains an optional later signaling layer rather than an active package dependency in this wave
- compact helper behavior, compact runtime signals, and compact persistence layout remain with `rules-compact-extension`

### 5.6 Compact-helper boundary

Compact carry-forward state, routing rules, and persisted compact schema are intentionally out of this package.

That responsibility remains with:
- `rules-compact-extension`

This package should therefore not be treated as the owner of:
- compact state layout
- compact routing rules
- compact proof files
- compact witness/prune behavior

---

## 6) Verification Targets

The extension design is successful when:
- `plugin/` exists and matches the intended package-local scaffold
- root RULES docs continue to teach rules-first, plugin-second behavior
- no root docs imply plugin authority replaces root runtime rules
- public install guidance points users to `claude-code-rules@darkwingtm`
- plugin metadata and skill surface are coherent
- the coordination skill remains an operator bridge and does not masquerade as semantic truth
- compact-helper ownership stays visibly separate in `rules-compact-extension`
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
