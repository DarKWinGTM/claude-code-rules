# RULES Plugin Extension Companion Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.0
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded rollout that adds an optional `plugin/` companion area to the RULES repository.

Why this change matters:
- the RULES system now needs a reusable hook package for compact lifecycle reinforcement
- plugin packaging should strengthen RULES behavior without becoming a replacement for root rules authority
- the repository already has strong root governance patterns, so the plugin companion needs a clean support-layer model rather than a duplicate governance stack

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../design/rules-plugin-extension.design.md`
- `../project-documentation-standards.md`
- `../design/project-documentation-standards.design.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../plugin/README.md`
- `../plugin/.claude-plugin/plugin.json`
- `../plugin/.claude-plugin/marketplace.json`
- `../plugin/hooks/hooks.json`

Review concern:
- the plugin companion should follow the proven `TEMPLATE/PLUGIN` package pattern while staying visibly subordinate to root RULES authority
- `plugin/` should not grow its own design/changelog/phase/TODO stack

---

## 3) Change Items

### Change Item 1
- **Target location:** new root design/changelog surface for the plugin companion
- **Change type:** additive

**Before**
```text
The RULES repository had no explicit design authority for an optional plugin companion area.
```

**After**
```text
The repository now has a dedicated root design/changelog pair for the RULES plugin extension area so the package boundary is explicit without creating a new runtime rule chain.
```

### Change Item 2
- **Target location:** repository role model and support-layer definition
- **Change type:** additive

**Before**
```text
The root role model recognized helper/support materials generally, but it did not yet define `plugin/**` as an optional support / extension package area.
```

**After**
```text
The root role model now places `plugin/**` under the support / extension layer and keeps root runtime rules as the semantic authority.
```

### Change Item 3
- **Target location:** `plugin/` package scaffold
- **Change type:** additive

**Before**
```text
The repository had no `plugin/` package for compact lifecycle reinforcement.
```

**After**
```text
The repository now has a package-local plugin scaffold under `plugin/` with package README, `.claude-plugin` metadata, `hooks/hooks.json`, and compact lifecycle scripts.
```

### Change Item 4
- **Target location:** root README and package README install/usage guidance
- **Change type:** additive

**Before**
```text
The root README taught rules installation only and did not yet explain the optional compact hook companion package in enough operational detail.
```

**After**
```text
The root README and package README now teach a rules-first install path plus a clearly optional plugin companion path, including step-by-step package-root install commands, compact hook flow, witness-file expectations, and duplicate-hook-path troubleshooting.
```

### Change Item 5
- **Target location:** master changelog/TODO/phase surfaces
- **Change type:** additive

**Before**
```text
Master governance surfaces did not yet record the plugin companion rollout family.
```

**After**
```text
Master governance surfaces now record the plugin extension wave, its patch/phase artifacts, the support-layer boundary for `plugin/**`, and the later documentation refinement that makes the package install/hook mechanics easier to follow.
```

---

## 4) Verification

- [x] root design/changelog authority exists for the plugin extension area
- [x] `plugin/**` is modeled as support / extension-only rather than a new authority layer
- [x] `plugin/README.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `hooks/hooks.json`, and compact lifecycle scripts exist
- [x] plugin docs explain package-root install/update flow, hook behavior, witness outputs, and duplicate-hook-path troubleshooting
- [x] plugin docs do not claim to replace `~/.claude/rules/`
- [x] root README, TODO, changelog, and phase surfaces record the plugin companion rollout coherently
- [x] no duplicate governance stack was created under `plugin/`

---

## 5) Rollback Approach

If the companion package model proves too broad:
- keep root RULES as the only semantic authority
- narrow the plugin to the smallest useful compact hook surface
- preserve the recorded history of the plugin companion rollout rather than silently removing the evidence trail
- do not revert to a plugin-first framing that weakens the rules-first authority model
