# Session Coordination Bridge Skill Rollout Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.10
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded rollout that extends the optional RULES plugin companion with an operator-facing session coordination support skill.

Why this change matters:
- the current plugin companion already packages compact lifecycle reinforcement cleanly, but it has no skill front door for session-coordination workflow
- the user wants the coordination support surface to belong to `claude-code-rules`, not to a separate peer plugin
- optional tooling such as memsearch and `claude-peers-mcp` should stay optional and availability-checked rather than silently assumed
- the support skill should help operators use the shared board, memory, optional recall, and optional peer signaling together without turning the plugin into a second semantic authority stack

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../design/rules-plugin-extension.design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../changelog/changelog.md`
- `../plugin/README.md`
- `../plugin/.claude-plugin/plugin.json`
- `../plugin/.claude-plugin/marketplace.json`
- `../plugin/skills/session-coordination-bridge/SKILL.md`

Review concern:
- the new skill should stay an operator bridge only and must not masquerade as the semantic owner of shared execution coordination
- plugin naming, install flow, and migration wording must stay coherent after renaming the plugin package from the older compact-only identity to `claude-code-rules`

---

## 3) Change Items

### Change Item 1
- **Target location:** plugin package identity and install path
- **Change type:** replacement

**Before**
```text
The plugin package was published and installed as `rules-compact-extension@darkwingtm`, which matched the compact-hook-only package identity but did not align with the broader claude-code-rules skill direction.
```

**After**
```text
The plugin package is now published and installed as `claude-code-rules@claude-code-rules`, with migration guidance for older `rules-compact-extension@darkwingtm` installs.
```

### Change Item 2
- **Target location:** plugin support surface
- **Change type:** additive

**Before**
```text
The plugin companion exposed compact lifecycle hooks only and had no skill front door for session coordination workflow.
```

**After**
```text
The plugin companion now exposes `skills/session-coordination-bridge/` as an operator-facing support skill for shared-board coordination, optional recall detection, request-vs-execution remap, and sync-back discipline.
```

### Change Item 3
- **Target location:** plugin design and README boundary docs
- **Change type:** additive

**Before**
```text
The plugin extension design recognized optional `plugin/skills/` in principle, but it did not yet define one active coordination skill or explain how that support layer should stay subordinate to root RULES authority.
```

**After**
```text
The plugin extension design and plugin README now define one active `session-coordination-bridge` support skill, explain its bounded role, and keep semantic truth in root RULES plus checked execution surfaces.
```

### Change Item 4
- **Target location:** compact runtime signal identity
- **Change type:** replacement

**Before**
```text
The compact hook runtime still identified itself in the visible navigator line as `[rules-compact-extension]`.
```

**After**
```text
The compact hook runtime now identifies itself as `[claude-code-rules]`, keeping the visible runtime signal aligned with the new plugin identity.
```

---

## 4) Verification

- [x] plugin metadata now uses `claude-code-rules` coherently
- [x] plugin README install/update flow uses `claude-code-rules@claude-code-rules`
- [x] migration guidance for older `rules-compact-extension@darkwingtm` installs is present
- [x] `skills/session-coordination-bridge/` exists and is operator-facing rather than authority-shifting
- [x] compact hook runtime signal now uses `[claude-code-rules]`
- [x] master design/README/TODO/changelog/phase surfaces record the skill rollout coherently
- [x] final release/update path is documented and verified

---

## 5) Rollback Approach

If the skill rollout proves too broad:
- keep the root RULES authority model unchanged
- narrow the skill content before removing the support surface entirely
- preserve the plugin rename and skill rollout history rather than silently erasing the recorded wave
- do not fall back into a plugin-first framing that makes the support package look like semantic truth
