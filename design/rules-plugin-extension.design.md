# RULES Plugin Extension

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 1.30
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd (2026-04-16)

---

## 1) Goal

Define the reduced `plugin/` companion area for `<rules-root>` after the coordination runtime split, so RULES keeps semantic authority while `claude-session-coordination@darkwingtm` owns the active compact and coordination plugin runtime.

---

## 2) Current package model

The current package split is:
- `claude-code-rules@darkwingtm` = reduced Rules migration/reference package
- `claude-session-coordination@darkwingtm` = active compact + coordination runtime package

พูดง่าย ๆ:
- RULES = policy / semantics / governance
- claude-code-rules plugin = migration/reference shell on the Rules side
- claude-session-coordination plugin = active hooks / scripts / coordination runtime

This means `plugin/` under RULES is no longer the active runtime owner.
It remains a bounded support surface so users can still find the Rules-side package identity and migration path.

---

## 3) Boundary

### 3.1 What this reduced package is

`plugin/` is now a reduced support/extension area that may:
- preserve package identity for `claude-code-rules@darkwingtm`
- preserve migration/reference guidance for the former unified package line
- point users toward `claude-session-coordination@darkwingtm` when they need active plugin runtime behavior
- keep local-development install metadata for the reduced Rules-side package

### 3.2 What this reduced package is not

It is **not** meant to:
- replace root RULES authority
- own active compact lifecycle hooks/scripts
- own active shared-task coordination runtime
- act like a second semantic authority stack
- keep a second live runtime topology in parallel with `claude-session-coordination@darkwingtm`

---

## 4) Current reduced surface

The active reduced Rules-side package surface is:
- `plugin/README.md` = reduced install / usage / migration guide
- `plugin/.claude-plugin/plugin.json` = reduced package metadata
- `plugin/.claude-plugin/marketplace.json` = reduced local development marketplace manifest
- `plugin/hooks/hooks.json` = no active plugin hooks after cutover
- `plugin/scripts/*.sh` = retained source-side runtime/migration reference material only, not an active installed hook surface by default

Active runtime/package ownership now lives in:
- `<plugin-marketplace-root>/claude-session-coordination`
- install target: `claude-session-coordination@darkwingtm`

---

## 5) Install posture

### 5.1 Public install

Recommended public activation:
- `claude plugins marketplace add "<plugin-marketplace-root>" --scope user`
- `claude plugins install claude-code-rules@darkwingtm --scope user`
- `claude plugins install claude-session-coordination@darkwingtm --scope user`

Meaning:
- install `claude-code-rules@darkwingtm` when you want the Rules-side migration/reference package
- install `claude-session-coordination@darkwingtm` when you want the active compact/session-coordination runtime

### 5.2 Local development

Local development for the reduced Rules package remains:
- `claude plugins marketplace add ./ --scope local`
- `claude plugins install claude-code-rules@claude-code-rules --scope local`

Package-local `@claude-code-rules` remains development-only wording.
It is not the user-facing runtime package story.

---

## 6) Active authority split

Root RULES still owns:
- semantic coordination doctrine
- compact/post-compact semantics as a RULES concern
- design / changelog / TODO / phase / patch governance

`claude-session-coordination@darkwingtm` now owns:
- active compact lifecycle hook runtime
- session introduction runtime
- tmux request / report / reflection runtime helpers
- bounded shared-task `TaskCreated` validation in shared-task-list mode
- coordination skill/docs and related runtime surfaces

The reduced RULES plugin should therefore describe the split clearly instead of replaying the older unified package model as if it were still active truth.

---

## 7) Verification targets

This design is successful when:
- `plugin/README.md`, package metadata, and root README all describe the same reduced-package boundary
- `plugin/hooks/hooks.json` no longer presents the RULES package as an active runtime hook owner
- install guidance points readers to `claude-session-coordination@darkwingtm` for active runtime behavior
- root RULES docs still preserve semantic authority and do not collapse into plugin-first guidance
- older unified-package history remains preserved in changelog/phase/archive surfaces without being presented as current ownership

---

## 8) Integration

Related documents:
- `design/design.md`
- `shared-execution-coordination.md`
- `project-documentation-standards.md`
- `phase/SUMMARY.md`
- `plugin/README.md`

---

> Full history: [../changelog/rules-plugin-extension.changelog.md](../changelog/rules-plugin-extension.changelog.md)
