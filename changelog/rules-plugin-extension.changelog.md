# Changelog - RULES Plugin Extension

> **Parent Document:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Current Version:** 1.11
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.11 | 2026-04-13 | **[Corrected plugin topology so claude-code-rules is the skill plugin and rules-compact-extension remains the compact helper](#version-111)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.10 | 2026-04-13 | **[Added the session coordination bridge skill and renamed the plugin package to claude-code-rules](#version-110)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.9 | 2026-04-08 | **[Tightened compact review to reference-first directive form](#version-19)** | 4e792d4b-8876-439b-8c07-2c5d4b04af3a |
| 1.8 | 2026-04-08 | **[Turned SessionStart carry-forward into an active review trigger](#version-18)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.7 | 2026-04-07 | **[Added reviewRoot pointers to compact navigator messages](#version-17)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.6 | 2026-04-07 | **[Tightened SessionStart routing to exact session-id matching](#version-16)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.5 | 2026-04-07 | **[Added review-path navigator pointers to compact trigger messages](#version-15)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.4 | 2026-04-06 | **[Replaced singleton compact state with session-scoped carry-forward storage](#version-14)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.3 | 2026-04-06 | **[Added bounded SessionStart consumed-proof and separated visible/context outputs](#version-13)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.2 | 2026-04-06 | **[Replaced latest witness files with ephemeral compact handoff lifecycle](#version-12)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.1 | 2026-04-06 | **[Expanded plugin install and hook-behavior documentation](#version-11)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.0 | 2026-04-06 | **[Created design authority for the RULES plugin extension area](#version-10)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |

---

<a id="version-111"></a>
## Version 1.11: Corrected plugin topology so claude-code-rules is the skill plugin and rules-compact-extension remains the compact helper

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Corrected the plugin topology so `claude-code-rules` is now the session-coordination skill package only, while `rules-compact-extension` remains the active compact/context helper.
- Updated `plugin/README.md` and `design/rules-plugin-extension.design.md` so they no longer claim compact lifecycle hook ownership for `claude-code-rules`.
- Updated the RULES-side package metadata to v1.4.0 with skill-only wording.
- Updated install guidance so the intended user-facing install target is now `claude-code-rules@darkwingtm`, with package-local `@claude-code-rules` retained only for local development/testing.
- Preserved the compact-helper boundary explicitly so the new skill package does not overlap the active compact helper.

### Summary
The RULES plugin topology is now corrected: `claude-code-rules` is the session-coordination skill plugin, and `rules-compact-extension` remains the separate active compact helper.

---

## Version 1.10: Added the session coordination bridge skill and renamed the plugin package to claude-code-rules

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.8 to v1.10 so the optional plugin companion now explicitly includes one operator-facing session coordination support skill while keeping root RULES as semantic authority.
- Renamed the plugin package identity from `rules-compact-extension` to `claude-code-rules` and updated package metadata plus marketplace manifest to v1.3.1.
- Added `plugin/skills/session-coordination-bridge/` with `SKILL.md` plus focused support docs for overview, capability detection, coordination flow, request contract, and examples.
- Updated `plugin/README.md` so install/update flow now uses `claude-code-rules@claude-code-rules`, includes migration guidance for older `rules-compact-extension@darkwingtm` installs, and documents the new support skill.
- Updated compact visible runtime signal wording from `[rules-compact-extension]` to `[claude-code-rules]`.
- Updated compact session-state schema prefixes from `rules-compact-extension/*` to `claude-code-rules/*` so persisted runtime state matches the new plugin identity.

### Summary
The RULES plugin companion now exposes an operator-facing session coordination support skill under the `claude-code-rules` namespace and uses one coherent plugin identity across install flow, runtime signals, and persisted compact state.

---

## Version 1.9: Tightened compact review to reference-first directive form

**Date:** 2026-04-08
**Session:** 4e792d4b-8876-439b-8c07-2c5d4b04af3a

### Changes
- Tightened success-path `systemMessage` so it now says `review-required` explicitly instead of acting like a passive navigator only.
- Reduced success-path `hookSpecificOutput.additionalContext` to a bounded reference-first directive: instruction + review file pointers + objective status only.
- Removed direct injection of carried-forward objective/item summary text from `additionalContext` so compact resume does not drift into hidden context replay.
- Added `sessionstart-directive.json` as bounded directive proof for what review instruction was emitted.
- Extended the compact index so each session row can expose `hasDirective` in addition to `hasProof`.
- Updated source/bridge package metadata and docs to v1.2.6 so the installed runtime can pick up the reference-first refinement cleanly.

### Summary
The RULES compact plugin now keeps compact resume reference-first by emitting a clear `review-required` signal and file pointers without replaying old context text aggressively back into Claude.

---

## Version 1.8: Turned SessionStart carry-forward into an active review trigger

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Upgraded `sessionstart-compact-consume-handoff.sh` so success-path `hookSpecificOutput.additionalContext` now explicitly tells Claude to review stored session data before continuing.
- Success-path additionalContext now names the exact per-session review directory plus `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json`.
- Fallback additionalContext now points Claude to `index.json` and tells it to re-anchor from verified local context before continuing.
- Kept the visible compact navigator line through `systemMessage`, including `reviewRoot=` and `review=`.
- Updated source/bridge package metadata and docs to v1.2.5 so the installed runtime can pick up the active review-trigger refinement cleanly.
- Recorded the memsearch boundary honestly: this wave keeps memsearch as a later assist layer rather than an active runtime dependency.

### Summary
The RULES compact plugin now behaves like an active review trigger at compact resume by explicitly directing Claude to review the stored exact-session files before continuing, while preserving the short visible navigator line.

---

## Version 1.7: Added reviewRoot pointers to compact navigator messages

**Date:** 2026-04-07
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Extended the compact `systemMessage` navigator summary so it now shows both `reviewRoot=<compact-root>` and `review=<relative-target>`.
- Success-path trigger messages now expose the compact data root plus the per-session directory pointer together.
- Fallback trigger messages now expose the compact data root plus `review=index.json` together.
- Updated source/bridge package metadata and docs to v1.2.3 so the installed runtime can pick up the reviewRoot navigator refinement cleanly.

### Summary
The compact trigger message now points to stored review data more explicitly by showing both the compact root and the relative review target in the visible navigator line.

---

<a id="version-16"></a>
## Version 1.6: Tightened SessionStart routing to exact session-id matching

**Date:** 2026-04-07
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Tightened compact `SessionStart` routing so pending state is now eligible only when `sourceSessionId == session_id` from the compact resume event.
- Replaced the earlier "single pending session" consume rule with exact session-id matching.
- Updated success-path proof reasons to `exact_session_id_match`.
- Updated fallback wording so routing now fails closed on `no exact pending session match` rather than on generic pending-set ambiguity only.
- Updated source/bridge package metadata and docs to v1.2.2 so the installed runtime can pick up the exact-id routing refinement cleanly.

### Summary
The RULES compact plugin now treats the compact resume `session_id` as the deterministic routing key for SessionStart consumption, which keeps before/after compact handling aligned to the same session instead of relying on looser pending-set heuristics.

---

<a id="version-15"></a>
## Version 1.5: Added review-path navigator pointers to compact trigger messages

**Date:** 2026-04-07
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Upgraded the compact `systemMessage` into a stronger navigator summary that now includes a short `review=` pointer to the stored session-state location.
- Success-path trigger messages now point directly to `sessions/<source-session-id>/` for fast review of `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json`.
- Ambiguous fallback trigger messages now point to `index.json` so unresolved routing can be reviewed from one place.
- Updated source/bridge package metadata and README files to v1.2.1 so the installed runtime can pick up the navigator-pointer refinement cleanly.

### Summary
The compact trigger message now acts as a clearer navigator by pointing directly to the stored review location for the resolved session, or to `index.json` when routing is ambiguous.

---

<a id="version-14"></a>
## Version 1.4: Replaced singleton compact state with session-scoped carry-forward storage

**Date:** 2026-04-06
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Replaced singleton compact-state files with a session-scoped layout using `index.json` plus per-session directories.
- Added per-session `pending.json`, `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json` contracts.
- Changed `PreCompact` behavior so carry-forward extraction now uses bounded pre-compact source context keyed by `session_id`.
- Recorded the current bounded limitation that transcript-based objective extraction is still heuristic/noisy when recent transcript entries are dominated by tool/skill payload text, but now fails closed instead of injecting a guessed objective.
- Changed compact `SessionStart` behavior so injection now resolves exactly one source session and fails closed on ambiguity instead of consuming a singleton mixed state.
- Changed cleanup behavior so expired session directories are pruned and the live index is rewritten after cleanup.
- Kept the user-visible `systemMessage` path and upgraded it into a navigator-style compact-resume summary with a short review pointer, while preserving the Claude/model-visible `hookSpecificOutput.additionalContext` carry-forward/reminder path.
- Synchronized the same runtime model into the shared `rules-compact-extension@darkwingtm` bridge package.

### Summary
The RULES plugin companion now stores compact carry-forward state per source session instead of in singleton global files, which removes cross-session collision as the default active model and keeps injection bounded to the correct session when routing is unambiguous.

---

<a id="version-13"></a>
## Version 1.3: Added bounded SessionStart consumed-proof and separated visible/context outputs

**Date:** 2026-04-06
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Added `last-sessionstart-consumed.json` as a bounded 1-hour proof file so successful compact SessionStart execution can be verified without keeping long-lived compact history.
- Kept `active-handoff.json` as pending-only state and removed the need to leave the handoff file behind after successful consume.
- Added a `[rules-compact-extension]` prefix to the compact-resume `systemMessage` so UI proof is easier to distinguish from other plugins.
- Split SessionStart outputs by verified role: `systemMessage` for the user-visible compact-resume line and `hookSpecificOutput.additionalContext` for the re-anchor reminder.
- Updated package metadata/docs to v1.1.1, renamed the package-local marketplace to `darkwingtm`, and synchronized the proof-focused runtime/design/patch/phase/master-doc wording.

### Summary
The RULES plugin companion now leaves a bounded SessionStart proof file after successful compact resume and separates user-visible versus Claude-context hook outputs more cleanly, making real runtime verification easier without reverting to a witness-history model.

---

<a id="version-12"></a>
## Version 1.2: Replaced latest witness files with ephemeral compact handoff lifecycle

**Date:** 2026-04-06
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Replaced the active latest-only witness model with one ephemeral handoff file under `${CLAUDE_PLUGIN_DATA}/compact/active-handoff.json`.
- Changed `PreCompact` behavior from raw witness recording to short-lived handoff creation with 1-hour expiry.
- Changed compact `SessionStart` behavior so the plugin now consumes/deletes the handoff after successful use, still injects the re-anchor reminder, and writes one bounded `last-sessionstart-consumed.json` proof file.
- Added one short compact-resume signal through the user-visible `systemMessage` SessionStart hook output field and kept the docs honest about the lack of an officially documented dedicated SessionStart status-line field.
- Changed `PostCompact` behavior from witness recording to prune-only cleanup.
- Updated package/runtime docs so the plugin is now described as a short-lived handoff cache with bounded SessionStart proof instead of a compact witness/history store.

### Summary
The RULES plugin companion now uses a one-shot compact handoff lifecycle instead of persisting latest witness files, which keeps the package aligned with rules-first compact re-anchor behavior while reducing stale-state drift.

---

<a id="version-11"></a>
## Version 1.1: Expanded plugin install and hook-behavior documentation

**Date:** 2026-04-06
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `plugin/README.md` with step-by-step installation guidance from the package root.
- Added clearer explanation of how `SessionStart`, `PreCompact`, and `PostCompact` behave in the current first slice.
- Documented the expected witness files under `${CLAUDE_PLUGIN_DATA}/compact/`.
- Added explicit troubleshooting guidance for the duplicate `hooks/hooks.json` load failure and documented the correct package pattern.
- Extended `design/rules-plugin-extension.design.md` so the install/runtime contract now captures the same first-pass package behavior more explicitly.

### Summary
Expanded the RULES plugin companion docs so installation, runtime hook behavior, witness outputs, and the duplicate-hook-path pitfall are easier to understand before git push/update.

---

## Version 1.0: Created design authority for the RULES plugin extension area

**Date:** 2026-04-06
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/rules-plugin-extension.design.md` as the root design authority for the optional `plugin/` companion area.
- Defined `plugin/` as a support / extension package rather than a second rules authority.
- Recorded the package-local scaffold for `README.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `hooks/hooks.json`, and compact lifecycle scripts.
- Explicitly prohibited duplicate governance drift under `plugin/`.

### Summary
Created one root design document for the RULES plugin companion so hook-based compact handling can be packaged cleanly without weakening root RULES authority.
