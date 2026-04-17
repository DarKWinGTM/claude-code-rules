# Changelog - RULES Plugin Extension

> **Parent Document:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Current Version:** 1.31
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.31 | 2026-04-17 | **[Reframed the former RULES plugin-extension chain as history after shell removal](#version-131)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.30 | 2026-04-16 | **[Reduced RULES plugin scope after coordination runtime split](#version-130)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.29 | 2026-04-16 | **[Added a bounded shared-task hook probe before the coordination split cutover](#version-129)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.28 | 2026-04-15 | **[Renamed and clarified the coordination concept as Shared Board Relay](#version-128)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.27 | 2026-04-15 | **[Added bounded retention helper for stale completed companion tasks](#version-127)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.26 | 2026-04-15 | **[Added anti-spam guard and request correlation hardening](#version-126)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.25 | 2026-04-15 | **[Added bounded workflow-acceptance proof from report plus board state](#version-125)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.24 | 2026-04-15 | **[Added richer request/held/blocked board automation](#version-124)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.23 | 2026-04-15 | **[Broadened bounded `board_ref` support with exact-subject anchors](#version-123)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.22 | 2026-04-15 | **[Standardized tmux bridge runtime onto Claude task-list identity](#version-122)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.21 | 2026-04-15 | **[Expanded plugin README with script-role and scope-boundary detail](#version-121)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.20 | 2026-04-15 | **[Added bounded anchored-task board reflection for tmux bridge records](#version-120)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.19 | 2026-04-14 | **[Added operator-facing dispatch wrapper for tmux requests](#version-119)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.18 | 2026-04-14 | **[Added report-back support for tmux requests](#version-118)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.17 | 2026-04-14 | **[Added minimal readiness gate for live tmux delivery](#version-117)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.16 | 2026-04-14 | **[Added board-anchored request wiring for tmux delivery](#version-116)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.15 | 2026-04-14 | **[Added minimal tmux transport adapter support](#version-115)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.14 | 2026-04-14 | **[Added group-local tmux bridge session introduction support](#version-114)** | 1b81d009-cf82-44a3-9739-cd3ea4af34dd |
| 1.13 | 2026-04-13 | **[Re-unified the Rules plugin under RULES/plugin](#version-113)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.12 | 2026-04-13 | **[Finalized topology-correction docs and portable install wording](#version-112)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
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

<a id="version-131"></a>
## Version 1.31: Reframed the former RULES plugin-extension chain as history after shell removal

**Date:** 2026-04-17
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Rewrote `design/rules-plugin-extension.design.md` so it now documents the former RULES plugin-extension line as historical context only.
- Removed current-state assumptions that `plugin/README.md`, local plugin metadata, hooks, or scripts still exist under `TEMPLATE/RULES/`.
- Clarified that active coordination runtime/package ownership now lives in `claude-session-coordination` while this chain remains only as historical design/changelog context.

### Summary
The former RULES plugin-extension chain is now preserved as history without implying that a local active plugin shell still exists under RULES.

---

<a id="version-130"></a>
## Version 1.30: Reduced RULES plugin scope after coordination runtime split

**Date:** 2026-04-16
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Reduced `plugin/hooks/hooks.json` to no active plugin hooks after the runtime ownership cutover.
- Rewrote `plugin/README.md` so the RULES package is now described as compact/runtime support only, with coordination runtime ownership moved to `claude-session-coordination@darkwingtm`.
- Updated RULES plugin manifests/metadata so they no longer describe the package as the active home of the coordination runtime.
- Preserved migration pointers so users can find the new coordination package without losing root RULES authority.

### Summary
The RULES plugin package is now reduced toward a migration/reference role, while active coordination runtime ownership is explicitly moved out to `claude-session-coordination@darkwingtm`.

---

<a id="version-129"></a>
## Version 1.29: Added a bounded shared-task hook probe before the coordination split cutover

**Date:** 2026-04-16
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Updated the active plugin hook surface at that time so `TaskCreated` was wired, while `TaskCompleted` stayed inactive before the later runtime ownership cutover.
- Updated `plugin/scripts/shared-task-hook-probe.sh` so it activates only when `CLAUDE_CODE_TASK_LIST_ID` is present, allows clearly open/shared task titles, and rejects malformed shared-board session-state titles with retryable `exit 2` feedback.
- Updated plugin/package/runtime docs so the feature was described as an active shared-task creation validator during the pre-cutover unified-package stage.
- Preserved the boundary that the validator does not mutate tasks, does not stop the whole session, and does not overclaim cross-session propagation.

### Summary
The RULES plugin history now records the bounded `TaskCreated` validator wave that landed before the later coordination split cutover, so the repo preserves that implementation history without treating the older unified package model as the current owner.

---

<a id="version-128"></a>
## Version 1.28: Renamed and clarified the coordination concept as Shared Board Relay

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Updated `README.md` at the repository root so the coordination concept is described more naturally as **Shared Board Relay** and linked readers to `plugin/README.md` for the full runtime/package explanation.
- Expanded `plugin/README.md` substantially so the concept, layers, core path, stronger proof path, cleanup path, runtime scripts, boundaries, and current limits are easier to understand in one place.
- Updated plugin metadata and design wording so the package description and operator-facing concept naming align more cleanly.

### Summary
The RULES plugin package now explains its coordination system under the clearer natural-language concept name **Shared Board Relay**, and both root/plugin README surfaces now make the bounded model easier to understand and review.

---

<a id="version-127"></a>
## Version 1.27: Added bounded retention helper for stale completed companion tasks

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added `plugin/scripts/tmux-bridge-retire-companions.sh` as a narrow retention helper for stale completed companion tasks.
- Added `plugin/skills/session-coordination-bridge/retention-notes.md` so the helper’s scope and boundaries are visible to operators.
- Updated the review checklist so retention reviews now explicitly verify that only eligible completed companion tasks are retired and anchored tasks remain untouched.
- Updated plugin README, patch, phase, TODO, and changelog surfaces so the retention helper is described consistently as a small cleanup/retention wave rather than a broader board engine.

### Summary
The RULES plugin companion now includes a bounded retention helper for stale completed companion tasks, helping the shared board stay cleaner without widening cleanup into aggressive or architecture-changing behavior.

---

<a id="version-126"></a>
## Version 1.26: Added anti-spam guard and request correlation hardening

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added `plugin/scripts/tmux-bridge-guard-send.sh` so equivalent still-open requests are blocked before the bridge can live-send the same intent repeatedly.
- Updated `plugin/scripts/tmux-bridge-create-request.sh` and `plugin/scripts/tmux-bridge-report-back.sh` so request state can be tracked strongly enough for duplicate-send guarding.
- Updated `plugin/scripts/tmux-bridge-send-request.sh` so the live tmux message now carries `request_id` for stronger later correlation.
- Updated `plugin/scripts/tmux-bridge-dispatch.sh` so dispatch now includes duplicate-send guarding, a short bounded capture delay, and clearer transport-only acknowledgment output.
- Updated plugin README and tmux protocol/request docs so the new anti-spam and correlation model is documented without implying callback-protocol behavior.

### Summary
The RULES plugin companion now has a bounded anti-spam and request-correlation hardening layer, reducing accidental resend risk while improving correlation and keeping tmux firmly in a transport-only role.

---

<a id="version-125"></a>
## Version 1.25: Added bounded workflow-acceptance proof from report plus board state

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added `plugin/scripts/tmux-bridge-evaluate-acceptance.sh` so the bridge can evaluate stronger workflow evidence from `report-back + reflected board state` instead of treating pane reach as acceptance.
- Updated `plugin/scripts/tmux-bridge-report-back.sh` so report-back output now includes the bounded acceptance evaluation result.
- Updated `plugin/scripts/tmux-bridge-dispatch.sh` so dispatch output explicitly marks transport-only state as non-acceptance.
- Updated plugin README and tmux protocol docs so stronger proof is now explained as report/board evidence while transport ack remains transport-only.

### Summary
The RULES plugin companion now provides a bounded workflow-acceptance proof layer that is stronger than tmux transport ack while still staying conservative and evidence-bounded.

---

<a id="version-124"></a>
## Version 1.24: Added richer request/held/blocked board automation

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Extended `plugin/scripts/tmux-bridge-sync-board.sh` so richer request-layer, held-owner, and blocked-owner companion tasks can now be created/updated in a bounded way from one request id.
- Kept the anchored task as the main board anchor while companion tasks now provide clearer request / held / blocked visibility.
- Added bounded lifecycle handling so superseded companion tasks are completed when later bridge states replace them.
- Updated plugin README, request contract, flow, protocol, examples, and design wording so the richer companion-task model is explained conservatively.

### Summary
The RULES plugin companion now provides richer board-visible request / held / blocked structure while keeping the anchored task as the main board anchor and preserving bounded same-task-list behavior.

---

<a id="version-123"></a>
## Version 1.23: Broadened bounded `board_ref` support with exact-subject anchors

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Extended `plugin/scripts/tmux-bridge-create-request.sh` so requests can preserve exact-subject anchor intent when `board_ref` uses `subject:<full task subject>`.
- Extended `plugin/scripts/tmux-bridge-sync-board.sh` so board reflection can resolve exact-subject anchors safely when there is one exact match.
- Added explicit fail-closed handling for exact-subject no-match and multi-match cases.
- Updated plugin README and protocol/support docs so the supported bounded anchor set now includes `task-<id>`, raw numeric id, and exact `subject:<full task subject>` matching.

### Summary
The RULES plugin companion now supports a broader but still bounded `board_ref` set, adding exact-subject anchors while preserving deterministic fail-closed behavior and avoiding fuzzy board discovery.

---

<a id="version-122"></a>
## Version 1.22: Standardized tmux bridge runtime onto Claude task-list identity

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Updated the tmux bridge runtime scripts so `CLAUDE_CODE_TASK_LIST_ID` becomes the upstream same-group basis instead of the older custom group variable.
- Added helper logic that derives the local board path internally from the task-list id when runtime board access still needs a filesystem path.
- Updated session introduction, request creation, same-group listing, readiness checks, send flow, and board-sync behavior to carry/use `task_list_id` as the primary shared-board identity.
- Updated plugin README and support docs so they describe `CLAUDE_CODE_TASK_LIST_ID` as the standard basis and treat local board paths as derived runtime detail.

### Summary
The RULES plugin companion now aligns its same-group runtime basis with Claude Code's standard task-list identity, keeping the bridge scoped to shared task lists while treating board paths as derived internal runtime state.

---

<a id="version-121"></a>
## Version 1.21: Expanded plugin README with script-role and scope-boundary detail

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Expanded `plugin/README.md` so the public runtime surface now names the tmux bridge helper scripts more explicitly instead of leaving them under a generic `scripts/*.sh` description.
- Added a plain-language explanation of how the `*.sh` scripts fit together across request creation, board reflection, readiness, live send, acknowledgement, and report-back.
- Added explicit current-limit guidance for broader `board_ref` support, richer request/held/blocked automation, and stronger workflow acceptance proof.
- Added explicit scope wording that current same-group coordination stays inside the shared task list / execution board group, with `CLAUDE_CODE_TASK_LIST_ID` now described as the standard upstream basis and the board path treated as a derived runtime value.

### Summary
The plugin README now explains the script layer and the group-boundary scope more directly, making the current tmux bridge easier to understand without changing the bounded runtime model.

---

<a id="version-120"></a>
## Version 1.20: Added bounded anchored-task board reflection for tmux bridge records

**Date:** 2026-04-15
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.14 to v1.15.
- Added `plugin/scripts/tmux-bridge-sync-board.sh` to reflect bridge-side request/report state into the existing anchored task when the anchor resolves safely.
- Extended `plugin/scripts/tmux-bridge-create-request.sh` with bounded board-sync metadata such as `target_session`, `group_path`, `request_title`, and optional `board_task_id`.
- Updated `plugin/scripts/tmux-bridge-report-back.sh` so report states normalize to the approved lifecycle set and immediately return the board-sync result after reflection is attempted.
- Updated `plugin/scripts/tmux-bridge-dispatch.sh` so dispatch now includes initial anchored-task board reflection for `requested` before live send handling continues.
- Updated protocol/support/package docs so this wave is described as bounded anchored-task reflection rather than hidden board replacement or broker behavior.

### Summary
The RULES plugin companion now includes a bounded anchored-task board-reflection step for tmux bridge records, making shared-board visibility stronger while keeping tmux transport and plugin state subordinate to the board as visible truth/history.

---

<a id="version-119"></a>
## Version 1.19: Added operator-facing dispatch wrapper for tmux requests

**Date:** 2026-04-14
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added `plugin/scripts/tmux-bridge-dispatch.sh` to compose request creation, readiness check, live send, and transport-level acknowledgement capture in one bounded flow.
- Updated protocol/support/package docs so the dispatch wrapper is described as workflow glue rather than board replacement or truth ownership.
- Verified the updated plugin package still validates and smoke-tested the dispatch wrapper path against a same-group tmux target.

### Summary
The RULES plugin companion now includes a single bounded dispatch wrapper for the tmux bridge model, which makes the live request workflow easier to operate while preserving the board as the visible truth/history layer.

---

<a id="version-118"></a>
## Version 1.18: Added report-back support for tmux requests

**Date:** 2026-04-14
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added `plugin/scripts/tmux-bridge-report-back.sh` to emit a machine-readable report-back record tied to an existing request.
- Extended `tmux-bridge-lib.sh` with report directory/path helpers.
- Updated request/protocol/flow/package/design docs so acceptance/progress/block/completion can now be staged in a structured report payload for later board sync.
- Verified the updated plugin package still validates and smoke-tested a report-back path using an existing request record.

### Summary
The RULES plugin companion now includes the first bounded report-back slice for the tmux bridge model, letting meaningful live requests produce a structured follow-up record without replacing the shared board as visible truth/history.

---

<a id="version-117"></a>
## Version 1.17: Added minimal readiness gate for live tmux delivery

**Date:** 2026-04-14
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added `plugin/scripts/tmux-bridge-check-readiness.sh` to evaluate same-group membership, tmux capability, input policy, and `ready_idle` state before live send.
- Updated `plugin/scripts/tmux-bridge-send-request.sh` so live delivery now consults the readiness gate and returns `board_only` instead of sending when the target is not clearly safe enough.
- Updated protocol/support/package docs to reflect that the default live path now prefers low-aggression fallback over transport eagerness.
- Verified the updated plugin package still validates and smoke-tested both `ready_idle` and `ready_busy` cases, confirming that the current gate sends only in the idle case and falls back in the busy case.

### Summary
The RULES plugin companion now includes the first bounded readiness gate for tmux delivery, ensuring that same-group live transport defaults back to board-only unless the target session is explicitly ready enough for low-aggression input.

---

<a id="version-116"></a>
## Version 1.16: Added board-anchored request wiring for tmux delivery

**Date:** 2026-04-14
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added `plugin/scripts/tmux-bridge-create-request.sh` to build a machine-readable board-anchored request record before live send.
- Extended `plugin/scripts/tmux-bridge-lib.sh` with request-record helper functions.
- Updated `plugin/scripts/tmux-bridge-send-request.sh` so live delivery now refuses requests without `board_ref`.
- Updated request/protocol/package docs so board anchoring is now an enforced transport precondition rather than documentation only.
- Smoke-tested the new board-anchored request creation plus live send/capture path.

### Summary
The RULES plugin companion now wires richer tmux delivery to an explicit shared coordination anchor before transport occurs, reducing the chance of hidden untracked live requests.

---

<a id="version-115"></a>
## Version 1.15: Added minimal tmux transport adapter support

**Date:** 2026-04-14
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Added `plugin/scripts/tmux-bridge-lib.sh` for shared tmux bridge path helpers.
- Added `plugin/scripts/tmux-bridge-list-sessions.sh` to list same-group session-introduction records.
- Added `plugin/scripts/tmux-bridge-send-request.sh` to deliver a structured request to a resolved tmux pane target.
- Added `plugin/scripts/tmux-bridge-capture-ack.sh` to capture pane output and report transport-level acknowledgement.
- Updated `tmux-bridge-protocol.md`, capability/support docs, and `plugin/README.md` so slice 2 transport behavior and its transport-only boundary are explicit.
- Verified the updated plugin package still validates and smoke-tested a send/capture path, which confirmed transport reach but also showed shell-level command conflict output, reinforcing that slice 2 proves transport acknowledgement more strongly than workflow acceptance.

### Summary
The RULES plugin companion now includes the first bounded tmux transport adapter slice for same-group live request delivery, while still keeping tmux in a transport-only role and leaving workflow acceptance/completion to shared coordination surfaces.

---

<a id="version-114"></a>
## Version 1.14: Added group-local tmux bridge session introduction support

**Date:** 2026-04-14
**Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.13 to v1.14.
- Updated `plugin/.claude-plugin/plugin.json` and `plugin/.claude-plugin/marketplace.json` from `1.5.0` to `1.6.0`.
- Added `plugin/scripts/session-group-introduce.sh` to emit a lightweight same-group session-introduction record for the tmux bridge model at session start.
- Extended `plugin/hooks/hooks.json` so `SessionStart` now also supports bounded session-introduction emission for `startup|resume|clear` without affecting the existing compact-only SessionStart path.
- Updated `plugin/README.md`, `plugin/skills/session-coordination-bridge/SKILL.md`, `request-contract.md`, `coordination-flow.md`, `examples.md`, and new `session-introduction.md` to reflect the group-local tmux bridge model.
- Validated the updated plugin manifest successfully and verified the new session-introduction script can write a same-group machine-readable session record with a non-tmux fallback readiness state.

### Summary
The RULES plugin companion now includes the first bounded runtime support for the tmux bridge design by emitting same-group session-introduction records at session start while keeping tmux transport and shared-board semantics clearly separated.

---

<a id="version-113"></a>
## Version 1.13: Re-unified the Rules plugin under RULES/plugin

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Re-unified the Rules plugin so compact helper hooks/scripts and the `session-coordination-bridge` skill now ship again from `<rules-root>/plugin`.
- Updated the RULES-side package metadata and local development marketplace metadata to `1.5.0`.
- Rewrote `plugin/README.md` to describe the unified package model instead of the split skill-only model.
- Updated the shared `darkwingtm` marketplace so `claude-code-rules` points at the unified Rules-owned package again.
- Removed duplicate maintained package copies from the shared marketplace workspace.

### Summary
The Rules plugin is unified again under `<rules-root>/plugin`, while the public install target remains `claude-code-rules@darkwingtm`.

---

<a id="version-112"></a>
## Version 1.12: Finalized topology-correction docs and portable install wording

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Tightened `plugin/README.md` into a skill-only package guide so it no longer carries stale compact-hook/state sections.
- Tightened `design/rules-plugin-extension.design.md` so public install wording is portable and the compact-helper boundary stays explicit.
- Updated RULES-side plugin package metadata and local-development marketplace metadata from `1.4.0` to `1.4.1`.
- Extended `phase/SUMMARY.md` review/coordination coverage for wave `042` and removed remaining topology-sync drift.

### Summary
The RULES plugin-extension chain now describes the corrected two-plugin topology cleanly, with portable install wording and no leftover compact-helper claims in the skill plugin package.

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

<a id="version-110"></a>
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
Historical note: this wave added an operator-facing session coordination support skill under the `claude-code-rules` namespace during the old plugin-extension stage. It is preserved as history only and does not imply a current usable skill path inside Main RULES.

---

<a id="version-19"></a>
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

<a id="version-18"></a>
## Version 1.8: Turned SessionStart carry-forward into an active review trigger

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.6 to v1.7.
- Updated `plugin/README.md` from v1.2.3 to v1.2.5.
- Updated `changelog/rules-plugin-extension.changelog.md` from v1.7 to v1.8.
- Upgraded compact `SessionStart` behavior so `hookSpecificOutput.additionalContext` now explicitly tells Claude to review stored session data before continuing.
- Success-path additionalContext now names the exact per-session review directory plus `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json`.
- Fallback additionalContext now points Claude to `index.json` and tells it to re-anchor from verified local context before continuing.
- Added `patch/compact-active-review-trigger-and-memsearch-assist-refinement.patch.md` plus `phase/phase-020-01-*` through `phase/phase-020-03-*` for the bounded Wave 020 rollout.
- Updated source and shared-bridge package metadata/docs to v1.2.5 so the installed runtime can pick up the active review-trigger refinement cleanly.
- Updated `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the Wave 020 review-trigger refinement is visible in master governance surfaces.

### Summary
The RULES compact plugin now behaves like an active review trigger at compact resume by explicitly directing Claude to review the stored exact-session files before continuing, while preserving the short visible navigator line.
