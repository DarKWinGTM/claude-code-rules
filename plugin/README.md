# Claude Code Rules Plugin Companion

> **Current Version:** 1.8.6

A reduced Rules-owned plugin package for `<rules-root>`.

This package no longer owns the active compact/session-coordination runtime.
That ownership now lives in:
- `claude-session-coordination@darkwingtm`

---

## Purpose

This package exists to keep a minimal Rules-side package surface during and after the coordination fork.

It is meant to:
- preserve migration/reference guidance for the former unified RULES plugin surface
- point users toward the active coordination package when plugin runtime behavior is needed
- avoid re-expanding active runtime/package ownership back into RULES by accident

It is **not** meant to:
- replace root RULES authority
- own the active Shared Board Relay runtime
- own active compact lifecycle hooks/scripts
- replace the shared task board, phase, TODO, or checked implementation state as coordination truth

---

## Package split

Current package model:
- `claude-code-rules@darkwingtm` = reduced Rules migration/reference package
- `claude-session-coordination@darkwingtm` = active compact + coordination runtime package

พูดง่าย ๆ:
- RULES = policy / semantics / governance
- claude-session-coordination = plugin runtime / hooks / scripts / coordination skill

---

## Installation

### Recommended public install

```bash
claude plugins marketplace add "<plugin-marketplace-root>" --scope user
claude plugins install claude-code-rules@darkwingtm --scope user
claude plugins install claude-session-coordination@darkwingtm --scope user
```

If you only need the Rules-side migration/reference package, `claude-code-rules@darkwingtm` is enough.
If you need the active plugin runtime, install `claude-session-coordination@darkwingtm`.

### Local development install

```bash
cd <plugin-root>
claude plugins marketplace add ./ --scope local
claude plugins install claude-code-rules@claude-code-rules --scope local
```

### Update

```bash
claude plugins update claude-code-rules@darkwingtm --scope user
claude plugins update claude-session-coordination@darkwingtm --scope user
```

---

## What this reduced package still means

This package is now mainly for:
- migration/reference continuity
- reduced package identity in the shared marketplace
- pointing readers back to root RULES authority and forward to the coordination package

For the active runtime surface, read:
- `TEMPLATE/PLUGIN/claude-session-coordination/README.md`

---

## Boundary reminder

The semantic authority remains at `<rules-root>`:
- root runtime rules define compact/post-compact semantics
- root runtime rules define shared execution coordination semantics
- plugin runtime behavior is now owned by `claude-session-coordination@darkwingtm`

This reduced package should not be treated as the active owner of hooks, scripts, or skills that were moved out.
