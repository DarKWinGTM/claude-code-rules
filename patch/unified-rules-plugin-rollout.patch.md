# Unified Rules Plugin Rollout Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.13
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded rollout that re-unifies the Rules plugin under `<rules-root>/plugin`.

Why this change matters:
- the user wants the Rules plugin to be one unified Rules-owned package
- duplicate package paths under `TEMPLATE/PLUGIN` were creating topology confusion
- `rules-compact-extension` and `claude-code-rules` should no longer behave like two separately maintained package sources
- the public install path should remain `claude-code-rules@darkwingtm`

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../design/rules-plugin-extension.design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`
- `../changelog/rules-plugin-extension.changelog.md`
- `../plugin/README.md`
- `../plugin/.claude-plugin/plugin.json`
- `../plugin/.claude-plugin/marketplace.json`
- shared marketplace aggregate under `<plugin-marketplace-root>/.claude-plugin/marketplace.json`

Review concern:
- the unified plugin must keep both compact helper and coordination skill behavior without reintroducing authority drift
- the public install path through `@darkwingtm` must still work after removing duplicate maintained package copies

---

## 3) Change Items

### Change Item 1
- **Target location:** plugin ownership model
- **Change type:** replacement

**Before**
```text
The topology was split across two maintained package surfaces: one package for compact helper behavior and another for the coordination skill, which made the Rules plugin story confusing.
```

**After**
```text
The Rules plugin is unified again under `<rules-root>/plugin`, combining compact helper behavior and the session-coordination skill in one Rules-owned package.
```

### Change Item 2
- **Target location:** shared marketplace exposure
- **Change type:** replacement

**Before**
```text
The shared marketplace exposed separate package copies under `TEMPLATE/PLUGIN`, which created duplicate maintained package paths.
```

**After**
```text
The shared marketplace now exposes `claude-code-rules` as the public plugin id while pointing back to the unified Rules-owned package source.
```

### Change Item 3
- **Target location:** RULES plugin package surface
- **Change type:** additive + restructuring

**Before**
```text
The Rules plugin had been narrowed to skill-only, while compact helper behavior remained outside the Rules-owned plugin source.
```

**After**
```text
The Rules plugin again includes both the compact hook/helper surface and the `session-coordination-bridge` skill under one package.
```

---

## 4) Verification

- [x] `<rules-root>/plugin` is the unified Rules-owned package source
- [x] compact helper hooks/scripts are present again in the Rules plugin package
- [x] `session-coordination-bridge` remains present in the same package
- [x] public install target remains `claude-code-rules@darkwingtm`
- [x] duplicate maintained package copies are no longer required for the public install model
- [x] governance surfaces describe the unified model coherently

---

## 5) Rollback Approach

If the unified model proves incorrect:
- preserve the public install path and recorded history
- narrow docs first before reintroducing another split topology
- avoid restoring duplicate maintained package copies without an explicit new design decision
