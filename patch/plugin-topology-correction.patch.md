# Plugin Topology Correction Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.12
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded correction wave that fixes the plugin topology after the earlier session-coordination skill rollout overlapped the real compact helper.

Why this change matters:
- `rules-compact-extension` is an active compact/context helper package, not dead baggage
- the earlier `claude-code-rules` plugin rollout accidentally duplicated the compact-helper role instead of staying skill-only
- the user-facing install path should be `claude-code-rules@darkwingtm`
- the shared `darkwingtm` marketplace should keep both plugins visible with distinct responsibilities

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
- shared compact helper package under `<plugin-marketplace-root>/rules-compact-extension`

Review concern:
- the correction must remove overlap without breaking the active compact helper
- RULES repo docs must stop claiming that `claude-code-rules` owns compact helper behavior
- the shared marketplace install path must resolve correctly after the split

---

## 3) Change Items

### Change Item 1
- **Target location:** plugin ownership model
- **Change type:** replacement

**Before**
```text
`claude-code-rules` was described as both the compact-helper plugin and the session-coordination skill plugin.
```

**After**
```text
`claude-code-rules` is now the session-coordination skill plugin only, while `rules-compact-extension` remains the active compact/context helper.
```

### Change Item 2
- **Target location:** public install topology
- **Change type:** replacement

**Before**
```text
The RULES plugin docs centered the package-local install path `claude-code-rules@claude-code-rules` as if it were the main user-facing target.
```

**After**
```text
The docs now treat `claude-code-rules@darkwingtm` as the public install target and keep `@claude-code-rules` only as a local development/testing path.
```

### Change Item 3
- **Target location:** support-layer boundary docs
- **Change type:** replacement

**Before**
```text
The plugin design and README still described compact lifecycle hooks, compact runtime state, and compact routing behavior as part of `claude-code-rules`.
```

**After**
```text
The plugin design and README now describe `claude-code-rules` as the coordination-skill plugin only and explicitly leave compact-helper ownership to `rules-compact-extension`.
```

---

## 4) Verification

- [x] `rules-compact-extension` remains the active compact helper
- [x] `claude-code-rules` is described as the skill plugin only
- [x] the shared `darkwingtm` marketplace is restored
- [x] the plugin family resolves again through `@darkwingtm`
- [x] docs now point users to `claude-code-rules@darkwingtm` as the intended public install path
- [x] package-local `@claude-code-rules` remains clearly bounded as local development/testing only
- [x] the final portable install-wording cleanup is reflected in the active target design version

---

## 5) Rollback Approach

If this topology correction proves incomplete:
- preserve `rules-compact-extension` as the compact helper
- preserve the shared marketplace restoration
- further narrow the RULES skill-plugin docs before changing the plugin family again
- do not reintroduce compact-helper overlap into `claude-code-rules`
