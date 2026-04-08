# RULES Compact Session-Scoped Carry-Forward State Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.4
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded Wave 019 refinement that replaces singleton compact plugin state with session-scoped storage and selected carry-forward extraction.

Why this change matters:
- singleton compact files can collide across multiple sessions
- one mixed file per kind does not scale safely when several sessions compact close together
- the user wants pre-compact context to stay per-session and selected, not merged into one large blob
- the plugin should inject only the current compacted session’s own selected carry-forward content and fail closed on ambiguity

---

## 2) Analysis

Risk level: Medium

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
- shared runtime bridge under `../../PLUGIN/rules-compact-extension/`

Review concern:
- session-scoped storage must prevent cross-session mix-up without creating giant aggregate payload files
- carry-forward extraction should remain bounded and conservative
- the maintained `rules-compact-extension@darkwingtm` runtime path must stay coherent with the RULES source package

---

## 3) Change Items

### Change Item 1
- **Target location:** compact state layout under `${CLAUDE_PLUGIN_DATA}/compact/`
- **Change type:** replacement

**Before**
```text
Compact state used singleton files such as:
- active-handoff.json
- last-sessionstart-consumed.json
```

**After**
```text
Compact state uses a small live index plus per-session directories:
- index.json
- sessions/<source-session-id>/pending.json
- sessions/<source-session-id>/precompact-context.json
- sessions/<source-session-id>/carry-forward-selected.json
- sessions/<source-session-id>/sessionstart-proof.json
```

### Change Item 2
- **Target location:** carry-forward source model
- **Change type:** replacement

**Before**
```text
The plugin used singleton handoff/proof files and injected only a generic reminder.
```

**After**
```text
The plugin extracts bounded pre-compact session context per source session, derives selected carry-forward payload per source session, and injects only that session’s selected data when routing is unambiguous.
```

### Change Item 3
- **Target location:** SessionStart routing behavior
- **Change type:** replacement

**Before**
```text
Any fresh singleton handoff could be consumed by the next compact SessionStart path.
```

**After**
```text
SessionStart reads only the live index, resolves exactly one pending source session, injects only that session’s selected carry-forward data, and fails closed on ambiguity.
```

### Change Item 4
- **Target location:** cleanup model
- **Change type:** replacement

**Before**
```text
Cleanup removed singleton pending/proof files and legacy leftovers.
```

**After**
```text
Cleanup prunes expired per-session directories, removes malformed local state without corrupting unrelated sessions, and rewrites a small live index.
```

---

## 4) Verification

- [x] singleton compact-state files are no longer the active model
- [x] one compact cycle creates session-scoped pending/context/carry-forward/proof files plus a small index
- [x] SessionStart injects only one resolved session’s selected carry-forward content
- [x] ambiguous multi-session routing fails closed and does not merge sessions
- [x] the shared `@darkwingtm` runtime bridge stays aligned with the RULES source package

---

## 5) Rollback Approach

If the session-scoped model proves too heavy or brittle:
- keep root RULES as the only semantic authority
- preserve the principle of session-scoped storage and fail-closed routing
- narrow extraction fields or file count before falling back to any singleton mixed-state model
- preserve the Wave 019 history rather than silently erasing the architectural refinement
