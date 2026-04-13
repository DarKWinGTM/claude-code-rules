# Claude Code Rules Plugin Companion

> **Current Version:** 1.4.0

An optional plugin companion for `<rules-root>` that exposes the session coordination support skill while leaving compact lifecycle hooks to `rules-compact-extension`.

---

## Purpose

This package exists to expose one optional support job cleanly.

It is meant to:
- expose `/claude-code-rules:session-coordination-bridge` as an operator-facing support skill for cross-session coordination workflow
- help operators use the shared board, phase/TODO/design/code, memory, optional recall, and optional peer signaling together safely
- stay small enough that the compact-helper role remains owned separately by `rules-compact-extension`

It is **not** meant to:
- replace root RULES authority
- install or manage `~/.claude/rules/`
- act like a second governance stack
- own compact lifecycle hooks
- own compact persistence state
- replace the shared task board, phase, TODO, or checked implementation state as coordination truth

---

## Path notation

- `<rules-root>` = the RULES repository root
- `<plugin-root>` = `<rules-root>/plugin`
- `<plugin-marketplace-root>` = the shared plugin marketplace root that contains the `darkwingtm` aggregate marketplace

---

## Installation and activation

### Recommended public install

Install through the shared `darkwingtm` marketplace:

```bash
claude plugins marketplace add "<plugin-marketplace-root>" --scope user
claude plugins install claude-code-rules@darkwingtm --scope user
```

### Local development install

Use this only when testing directly from the RULES repo source:

```bash
cd <plugin-root>
claude plugins marketplace add ./ --scope local
claude plugins install claude-code-rules@claude-code-rules --scope local
```

### Update

Public install update:

```bash
claude plugins update claude-code-rules@darkwingtm --scope user
```

Local development update:

```bash
claude plugins update claude-code-rules@claude-code-rules --scope local
```

### Important boundary

- `claude-code-rules@darkwingtm` = session-coordination skill plugin
- `rules-compact-extension@darkwingtm` = compact/context helper
- do **not** uninstall `rules-compact-extension` just to install `claude-code-rules`

---

## Verification

Check installed state:

```bash
claude plugins list --json
```

Optional interactive checks:
- `/reload-plugins`
- `/claude-code-rules:session-coordination-bridge`
- `/hooks` to confirm compact hooks still come from `rules-compact-extension`

What you should see:
- `claude-code-rules@darkwingtm` enabled for the public install path
- `rules-compact-extension@darkwingtm` still enabled if you use compact helper behavior
- the skill `/claude-code-rules:session-coordination-bridge` available

---

## Runtime contract

### Public runtime surface
- `skills/session-coordination-bridge/SKILL.md` = operator-facing support skill for shared-board and optional-tool coordination workflow
- `skills/session-coordination-bridge/*.md` = focused support docs for coordination model, capability detection, flow, request contract, and examples
- `.claude-plugin/plugin.json` = skill-plugin metadata
- `.claude-plugin/marketplace.json` = local development marketplace metadata for the skill package

### Current behavior
- this package exposes the `session-coordination-bridge` skill only
- it does not own compact hooks, compact runtime signals, compact state, or compact proof files
- compact helper behavior remains in `rules-compact-extension@darkwingtm`
- the intended user-facing install path is `claude-code-rules@darkwingtm`
- the package-local `@claude-code-rules` path is for local development/testing only

### Current structure

| Path | Role |
|------|------|
| `.claude-plugin/plugin.json` | package metadata |
| `.claude-plugin/marketplace.json` | package-local development marketplace manifest |
| `skills/session-coordination-bridge/` | operator-facing session coordination support skill |
| `README.md` | package-local install and boundary guide |

---

## Relationship to compact helper

Compact lifecycle behavior is intentionally out of this package.

That responsibility remains with:
- `rules-compact-extension@darkwingtm`

พูดง่าย ๆ คือ package นี้ดูแล skill ด้าน session coordination ส่วน compact helper ยังอยู่อีก plugin หนึ่ง ไม่ได้รวมอยู่ที่นี่แล้ว

---

## Boundary reminder

The semantic authority remains at `<rules-root>`:
- root runtime rules define coordination semantics and the meaning of the shared execution model
- this plugin only provides an operator-facing coordination skill surface
- compact helper behavior is intentionally owned by `rules-compact-extension`, not by this plugin
