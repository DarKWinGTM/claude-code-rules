# RULES Compact Extension Companion Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.2
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded Wave 018 refinement that replaces the plugin’s latest-only compact witness model with an ephemeral handoff lifecycle.

Why this change matters:
- the current latest-only witness files keep compact artifacts longer than needed
- stale witness state can preserve irrelevant compact carry-forward data
- the user wants compact support to behave like a short-lived handoff cache, not a history/audit store
- the repository already has the right root semantics from Wave 016, so this wave should refine plugin mechanics rather than reopen rule meaning

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../design/rules-plugin-extension.design.md`
- `../plugin/README.md`
- `../plugin/.claude-plugin/plugin.json`
- `../plugin/.claude-plugin/marketplace.json`
- `../plugin/hooks/hooks.json`
- `../plugin/scripts/compact-handoff-common.sh`
- `../plugin/scripts/precompact-create-handoff.sh`
- `../plugin/scripts/sessionstart-compact-consume-handoff.sh`
- `../plugin/scripts/postcompact-prune-handoff.sh`
- `../README.md`
- `../design/design.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- the plugin companion should stay support-only and hook-driven while removing the old witness/log posture cleanly
- the new runtime contract should use one ephemeral handoff file and opportunistic cleanup only
- docs must stay honest about official hook output support versus package-level compact-resume wording

---

## 3) Change Items

### Change Item 1
- **Target location:** plugin hook/runtime lifecycle under `plugin/hooks/` and `plugin/scripts/`
- **Change type:** replacement

**Before**
```text
PreCompact, PostCompact, and compact SessionStart each wrote a latest-only raw witness file:
- last-precompact.json
- last-postcompact.json
- last-sessionstart-compact.json
```

**After**
```text
The plugin uses one ephemeral handoff lifecycle with bounded SessionStart proof:
- PreCompact creates `${CLAUDE_PLUGIN_DATA}/compact/active-handoff.json`
- compact SessionStart consumes it once, injects the re-anchor reminder, emits one short compact-resume signal, deletes the handoff immediately after successful use, and writes `${CLAUDE_PLUGIN_DATA}/compact/last-sessionstart-consumed.json`
- PostCompact performs prune-only cleanup
```

### Change Item 2
- **Target location:** plugin runtime state contract in package docs/design
- **Change type:** replacement

**Before**
```text
The package was described as recording compact lifecycle witnesses for bounded local evidence.
```

**After**
```text
The package is described as a short-lived compact handoff cache that intentionally avoids history/audit behavior.
```

### Change Item 3
- **Target location:** compact-resume signaling guidance
- **Change type:** additive

**Before**
```text
The package documented only the re-anchor reminder via SessionStart hook behavior.
```

**After**
```text
The package now documents one short compact-resume signal through the user-visible `systemMessage` field while keeping the wording honest that official checked docs do not show a separate dedicated SessionStart status-line primitive.
```

### Change Item 4
- **Target location:** root rollout/index/history surfaces
- **Change type:** additive

**Before**
```text
Master governance surfaces ended at Wave 017 and still taught the plugin’s latest-witness model as the active package behavior.
```

**After**
```text
Master governance surfaces record Wave 018, the ephemeral handoff lifecycle, the prune-only PostCompact behavior, and the removal of the old latest-witness model from the active contract.
```

---

## 4) Verification

- [x] plugin hook/runtime surface now centers on one ephemeral `active-handoff.json` contract
- [x] `PreCompact` creates handoff state instead of recording a raw witness payload
- [x] compact `SessionStart` is designed to consume/delete the handoff after successful use and leave one bounded `last-sessionstart-consumed.json` proof file
- [x] `PostCompact` is prune-only and no longer records raw witness payloads
- [x] package docs now describe the plugin as a short-lived handoff cache instead of a witness/history store
- [x] docs are explicit that official checked hook docs do not document a separate dedicated SessionStart status-line field and now use user-visible `systemMessage` for the compact-resume line
- [x] no duplicate governance stack was created under `plugin/`

---

## 5) Rollback Approach

If the ephemeral handoff refinement proves too narrow or implementation details need adjustment:
- keep root RULES as the only semantic authority
- preserve the one-handoff cache model as the preferred boundary unless direct runtime evidence proves it insufficient
- adjust signal wording or helper logic without reintroducing latest-witness history by default
- preserve the recorded Wave 018 history rather than silently erasing the refinement evidence
