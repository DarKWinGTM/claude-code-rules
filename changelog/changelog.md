# Master Changelog - Claude Code Rules

> **Project:** Claude Code Rules System
> **Current Version:** 9.28
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 9.28 | 2026-04-13 | **[Corrected plugin topology so claude-code-rules is the skill plugin and rules-compact-extension remains the compact helper](#version-928)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.27 | 2026-04-13 | **[Added the session coordination bridge skill to the optional plugin companion](#version-927)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.26 | 2026-04-13 | **[Added memsearch availability detection and fallback intake guidance](#version-926)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.25 | 2026-04-13 | **[Standardized visible session ownership for session-owned task work](#version-925)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.24 | 2026-04-13 | **[Refined shared-board visibility, lifecycle, retention, and optional memsearch guidance](#version-924)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.23 | 2026-04-13 | **[Separated handoff request naming from receiving-side phase ownership](#version-923)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.22 | 2026-04-13 | **[Created shared execution coordination as a first-class rule chain](#version-922)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.21 | 2026-04-12 | **[Added next-work discovery from execution surfaces](#version-921)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.20 | 2026-04-12 | **[Added same-objective task-list continuity and retention](#version-920)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.19 | 2026-04-12 | **[Added first-class execution continuity and goal-set review owners](#version-919)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.18 | 2026-04-12 | **[Promoted high-signal communication into the active runtime rule set](#version-918)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.17 | 2026-04-12 | **[Improved README Quick Start install scripts for Bash and PowerShell](#version-917)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.16 | 2026-04-12 | **[Added AI-assisted install prompts to the README](#version-916)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.15 | 2026-04-11 | **[Added easy-to-picture concise phase/progress explanation guidance](#version-915)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.14 | 2026-04-11 | **[Linked live task-list behavior explicitly to the current active phase](#version-914)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.13 | 2026-04-11 | **[Cleaned stale custom-table detail out of active rules after suspension](#version-913)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.12 | 2026-04-11 | **[Suspended the custom table-format experiment from the active RULES system](#version-912)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.11 | 2026-04-11 | **[Hardened no-box enforcement with character-level checks and send-time self-check](#version-911)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.10 | 2026-04-11 | **[Made the no-boxed-table rule explicit for ordinary assistant answers](#version-910)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.9 | 2026-04-11 | **[Created a first-class table owner and centralized ordinary answer-table semantics](#version-99)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.7 | 2026-04-10 | **[Corrected the default table style to the selected light plain aligned no-frame form](#version-97)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.6 | 2026-04-10 | **[Made task-list-first tracking explicit for non-trivial work across tracking/startup/documentation owners](#version-96)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.5 | 2026-04-09 | **[Created first-class memory-governance rule chain and synchronized memory-boundary companions](#version-95)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.4 | 2026-04-09 | **[Standardized compact markdown tables and list-first alternatives for lighter answer formatting](#version-94)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.3 | 2026-04-09 | **[Added purpose-first communication framing across wording, explanation, presentation, and style owners](#version-93)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.2 | 2026-04-09 | **[Kept user-declared RULES-first issues out of memory-first fixes and hardened portable support artifacts](#version-92)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.1 | 2026-04-08 | **[Preferred direct human-readable wording over metaphor-heavy internal shorthand](#version-91)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 9.0 | 2026-04-08 | **[Added closed-topic presentation guidance and narrowed startup patch posture](#version-90)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 8.9 | 2026-04-08 | **[Narrowed startup patch posture for greenfield baseline formation](#version-89)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 8.8 | 2026-04-08 | **[Tightened compact review to reference-first directive form](#version-88)** | 4e792d4b-8876-439b-8c07-2c5d4b04af3a |
| 8.7 | 2026-04-08 | **[Turned compact SessionStart into an active review trigger](#version-87)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 8.6 | 2026-04-07 | **[Added reviewRoot pointers to compact navigator messages](#version-86)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 8.5 | 2026-04-07 | **[Tightened compact SessionStart to exact session-id routing](#version-85)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 8.4 | 2026-04-07 | **[Added navigator review pointers to compact trigger messages](#version-84)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 8.3 | 2026-04-06 | **[Replaced singleton compact files with session-scoped carry-forward state](#version-83)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 8.2 | 2026-04-06 | **[Replaced compact witness files with an ephemeral handoff lifecycle](#version-82)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 8.1 | 2026-04-06 | **[Added compact/post-compact re-anchor governance and an optional plugin companion extension](#version-81)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 8.0 | 2026-04-05 | **[Added governing-basis clarification before deep branch analysis](#version-80)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.9 | 2026-04-04 | **[Added team-agent dedup and stale-presence boundaries](#version-79)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.8 | 2026-04-04 | **[Added goal-qualified proposal boundaries across the communication-owner set](#version-78)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.7 | 2026-04-04 | **[Added identifier-explanation guidance across the communication-owner trio](#version-77)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.6 | 2026-04-03 | **[Added recommendation-plus-reason guidance for multi-option next steps](#version-76)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.5 | 2026-04-03 | **[Refined public install portability and source-vs-destination notation across hardcoding-governance owners](#version-75)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.4 | 2026-04-03 | **[Opened continuation-priority refinement across communication-owner chains](#version-74)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.3 | 2026-04-02 | **[Deepened portability-rule integration across adjacent chains](#version-73)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.2 | 2026-04-02 | **[Created first-class portable-implementation-and-hardcoding-control rule chain and synchronized hardcoding governance](#version-72)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.1 | 2026-03-31 | **[Created first-class custom-agent-selection-priority rule chain and synchronized agent-selection governance](#version-71)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.0 | 2026-03-31 | **[Created first-class external-verification-and-source-trust rule chain and synchronized source-trust governance](#version-70)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 6.9 | 2026-03-30 | **[Hardened explicit phase-to-patch linkage in phased work](#version-69)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 6.8 | 2026-03-28 | **[Created startup artifact-initiation governance and synchronized the repository to artifact-first work startup](#version-68)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 6.7 | 2026-03-28 | **[Corrected the repository-wide patch model to explicit before/after artifacts in `patch/` or at root](#version-67)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 6.5 | 2026-03-27 | **[Created natural-professional-communication rule chain and synchronized communication-owner refinements](#version-65)** | a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2 |
| 6.4 | 2026-03-17 | **[Changed default phase numbering to 001/002/003 across phase-implementation governance](#version-64)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| 6.3 | 2026-03-17 | **[Created first-class tactical-strategic-programming rule chain and synchronized master governance](#version-63)** | 77d0802a-fd64-4023-a66d-88c165ccca12 |

---

<a id="version-928"></a>
## Version 9.28: Corrected plugin topology so claude-code-rules is the skill plugin and rules-compact-extension remains the compact helper

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Corrected the plugin topology so `rules-compact-extension@darkwingtm` remains the active compact/context helper while `claude-code-rules` becomes the session-coordination skill plugin only.
- Updated `design/rules-plugin-extension.design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so they no longer describe `claude-code-rules` as the compact helper.
- Updated the RULES-side package metadata to v1.4.0 with skill-only wording.
- Restored the shared `darkwingtm` marketplace and reinstalled the plugin family so `frontend-design-pattern-navigator`, `general-expert`, `multi-hat-system`, `supervisor-audit-agent-system`, `webview-screenshort`, and `rules-compact-extension` all resolve again.
- Mirrored the RULES skill plugin into the shared marketplace source so the intended user-facing install path is now `claude-code-rules@darkwingtm`.

### Summary
The RULES plugin rollout is now topology-correct: compact helper behavior stays in `rules-compact-extension`, while `claude-code-rules` becomes the separate session-coordination skill plugin exposed through `@darkwingtm`.

---

## Version 9.27: Added the session coordination bridge skill to the optional plugin companion

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.8 to v1.10 so the optional plugin companion now includes one operator-facing session coordination support skill while keeping root RULES as semantic authority.
- Updated `changelog/rules-plugin-extension.changelog.md` to v1.10 for the plugin companion skill rollout.
- Renamed the plugin package identity from `rules-compact-extension` to `claude-code-rules` and updated `plugin/.claude-plugin/plugin.json` plus `plugin/.claude-plugin/marketplace.json` to v1.3.1.
- Added `plugin/skills/session-coordination-bridge/` with `SKILL.md` plus focused support docs for overview, capability detection, coordination flow, request contract, and examples.
- Updated `plugin/README.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the optional extension layer now documents both compact lifecycle hooks and the new support skill, including migration guidance for older `rules-compact-extension@darkwingtm` installs.
- Updated compact visible runtime signal wording and persisted compact-state schema prefixes from `rules-compact-extension/*` to `claude-code-rules/*` so runtime behavior stays aligned with the new plugin identity.
- Added bounded `patch/session-coordination-bridge-skill-rollout.patch.md` plus `phase-041-01` and `phase-041-02` artifacts for the skill rollout wave.

### Summary
The optional RULES plugin companion now exposes `claude-code-rules:session-coordination-bridge` as a bounded support skill and uses one coherent `claude-code-rules` plugin identity across install flow, runtime signals, and persisted compact state.

---

## Version 9.26: Added memsearch availability detection and fallback intake guidance

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `shared-execution-coordination` from v1.3 to v1.4 so receive-side continuation now checks memsearch availability before relying on the optional recall extension.
- Updated `memory-governance-and-session-boundary` from v1.2 to v1.3 so optional recall availability is now checked explicitly and falls back immediately when absent or probe fails.
- Added bounded `patch/memsearch-availability-detection-and-fallback-intake.patch.md` plus `phase-040-01` and `phase-040-02` artifacts.
- Updated master design/README/TODO/phase surfaces while keeping the active runtime rule count unchanged at 40.

### Summary
The RULES repository now makes optional recall intake availability-first and immediate-fallback-aware, so missing memsearch does not have to block receive-side task continuation.

---

<a id="version-925"></a>
## Version 9.25: Standardized visible session ownership for session-owned task work

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `shared-execution-coordination` from v1.2 to v1.3 so visible session ownership is now the default board-facing standard for session-owned work and request / held / blocked title forms remain distinct.
- Updated `todo-standards` from v2.11 to v2.12 so task-list guidance now treats visible session ownership as a general standard rather than a shared-path-only convention.
- Updated `phase-implementation` from v2.13 to v2.14 so phase-linked execution slices now prefer held-owner title forms once the work is already locally owned.
- Updated `project-documentation-standards` from v2.22 to v2.23 so the repository model now treats visible session ownership as a default task-list standard and defers session-state title grammar to the coordination owner.
- Added bounded `patch/universal-session-owned-task-title-grammar.patch.md` plus `phase-039-01` and `phase-039-02` artifacts.
- Updated master design/README/TODO/phase surfaces while keeping the active runtime rule count unchanged at 40.

### Summary
The RULES repository now treats visible session ownership as a default task-list standard for session-owned work across usage modes, while preserving distinct request, held, and blocked title forms.

---

<a id="version-924"></a>
## Version 9.24: Refined shared-board visibility, lifecycle, retention, and optional memsearch guidance

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `shared-execution-coordination` from v1.1 to v1.2 so session-held work is more visibly distinguishable, handoff lifecycle states are more explicit, retention depends more clearly on task class/state, and optional memsearch use is explained after stronger execution surfaces identify the continuation target.
- Updated `todo-standards` from v2.10 to v2.11 so session-held, handoff, and blocked-on-session tasks now have clearer visible-session guidance in the live task board.
- Updated `memory-governance-and-session-boundary` from v1.1 to v1.2 so optional recall extensions are now explicitly positioned after stronger checked execution surfaces rather than beside or above them.
- Added bounded `patch/shared-board-visibility-retention-and-memsearch-refinement.patch.md` plus `phase-038-01` and `phase-038-02` artifacts.
- Updated master design/README/TODO/phase surfaces while keeping the active runtime rule count unchanged at 40.

### Summary
The RULES repository now gives shared execution boards clearer visible session identity, more explicit handoff lifecycle and retention behavior, and a more concrete optional memsearch operating model without making optional tooling authoritative or required.

---

<a id="version-923"></a>
## Version 9.23: Separated handoff request naming from receiving-side phase ownership

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `shared-execution-coordination` from v1.0 to v1.1 so cross-session request naming is now explicitly separated from receiving-side execution phase ownership.
- Updated `todo-standards` from v2.9 to v2.10 so cross-session request tasks now favor request/handoff naming over sender-phase title leakage.
- Updated `phase-implementation` from v2.12 to v2.13 so accepted cross-session work is now explicitly remapped by the receiving session into its own phase/objective structure when needed.
- Updated `project-documentation-standards` from v2.20 to v2.21 so the repository model now distinguishes shared-board request naming from receiving-side execution phase structure.
- Added bounded `patch/handoff-request-vs-receiving-phase-boundary.patch.md` plus `phase-037-01` and `phase-037-02` artifacts.
- Updated master design/README/TODO/phase surfaces while keeping the active runtime rule count unchanged at 40.

### Summary
The RULES repository now keeps cross-session handoff naming request-oriented and leaves execution-phase ownership with the receiving session, which reduces phase-owner ambiguity on shared task boards.

---

<a id="version-922"></a>
## Version 9.22: Created shared execution coordination as a first-class rule chain

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Created `shared-execution-coordination` as a new first-class runtime/design/changelog chain for multi-session shared execution boards, session lease/handoff behavior, continuity-first retention, anti-overclear policy, optional memsearch support, and future-optional peer-messaging boundaries.
- Updated `todo-standards`, `phase-implementation`, `execution-continuity-and-mode-selection`, `project-documentation-standards`, `memory-governance-and-session-boundary`, and `authority-and-scope` with bounded deferrals to the new coordination owner.
- Updated master design/README/TODO/phase surfaces and expanded the active runtime install set from 39 to 40 rules.
- Preserved the existing phase, tracking, memory, and execution-continuity owners rather than replacing them with one super-rule.

### Summary
The RULES repository now has one explicit coordination owner for multi-session shared execution boards, while the existing task, phase, memory, and execution owners keep their narrower roles.

---

<a id="version-921"></a>
## Version 9.21: Added next-work discovery from execution surfaces

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `execution-continuity-and-mode-selection` from v1.0 to v1.1 so execution continuity now includes active next-work discovery from execution surfaces.
- Updated `todo-standards` from v2.7 to v2.8 so the task list is now explicitly the first next-work discovery surface with bounded fallback to active phase / `phase/SUMMARY.md` / `TODO.md` / checked implementation state.
- Updated `phase-implementation` from v2.10 to v2.11 so the active phase workspace now acts as a bounded discovery surface when the task list alone is insufficient.
- Updated `project-documentation-standards` from v2.18 to v2.19 so the repository model now explicitly recognizes execution-discovery surfaces during active execution.
- Added bounded `patch/next-work-discovery-from-execution-surfaces.patch.md` plus `phase-035-01` and `phase-035-02` artifacts.
- Updated master design/README/TODO/changelog/phase surfaces and kept the active runtime rule count unchanged at 39.

### Summary
The RULES repository now lets execution-ready work discover the next unfinished slice from the active execution surfaces instead of waiting for the user to restate it.

---

<a id="version-920"></a>
## Version 9.20: Added same-objective task-list continuity and retention

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards`, `phase-implementation`, `artifact-initiation-control`, and `project-documentation-standards` so the built-in task list is reused within the same active objective instead of being repeatedly replaced.
- Added explicit same-objective reuse/append behavior, completed-task visibility until closure, and objective-boundary reset language.
- Added bounded `phase-034` plus `patch/task-list-continuity-and-objective-boundary-retention.patch.md` artifacts for the refinement wave.
- Bundled the already-open `accurate-communication.md` micro-compression maintenance so the installed runtime copy is now below the 40.0k warning threshold.

### Summary
The RULES repository now keeps one live task-list surface per active objective instead of repeatedly replacing it, while still allowing a fresh list when a truly new objective begins.

---

<a id="version-919"></a>
## Version 9.19: Added first-class execution continuity and goal-set review owners

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Created `execution-continuity-and-mode-selection` as a first-class runtime/design/changelog chain for discussion-vs-execution mode selection, continuous-execution defaults, legitimate stop gates, and phase-boundary continuity.
- Created `goal-set-review-and-priority-balance` as a first-class runtime/design/changelog chain for continuous goal-set review, structure-first priority balance, and protection against single-subtask fixation.
- Updated bounded companion rules so continuity and goal-review semantics now defer to the new owners without expanding `accurate-communication.md`.
- Updated master design/README/TODO/phase surfaces and expanded the active runtime install set from 37 to 39 rules.

### Summary
The RULES repository now has explicit owners for continuous execution and full-goal-set review, so active work can keep moving without losing discussion protection or neglecting sibling goals.

---

<a id="version-918"></a>
## Version 9.18: Promoted high-signal communication into the active runtime rule set

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `high-signal-communication` from v1.0 to v1.1 and aligned its design/changelog chain so it no longer reads like a standalone experiment.
- Added `high-signal-communication.md` to the active runtime inventory and README install set, increasing the active runtime count from 36 to 37.
- Added bounded patch/phase artifacts for the promotion wave and synchronized master design/README/TODO/phase surfaces to the new active status.
- Closed metadata drift by aligning touched runtime/design headers with already-authoritative changelog versions for `todo-standards`, `phase-implementation`, and `artifact-initiation-control`.

### Summary
The RULES repository now treats high-signal communication as an active bounded supplementary runtime rule, and the related source/master metadata is synchronized around that status.

---

<a id="version-917"></a>
## Version 9.17: Improved README Quick Start install scripts for Bash and PowerShell

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Replaced the old Quick Start install block with cleaner Bash and PowerShell scripts.
- Removed centered presentation around the Quick Start code block so the install commands read more naturally.
- Kept the same active 36-rule runtime install set while making the script structure easier to reuse and edit.
- Added a dedicated Windows PowerShell install path alongside the Bash install path for Linux/macOS users.
- Updated `TODO.md` and the master changelog to record the Quick Start install-script refinement.

### Summary
The README now gives cleaner install scripts for both Bash and PowerShell so Quick Start is easier to follow across Linux/macOS and Windows.

---

<a id="version-916"></a>
## Version 9.16: Added AI-assisted install prompts to the README

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `README.md` with ready-to-send AI install/adaptation prompts for Claude Code, Codex CLI, and Gemini CLI.
- Kept the prompts aligned to the active-vs-non-active rule boundary so AI installers are told to ignore `suspend/`, `support/`, `plugin/`, `design/`, `changelog/`, `phase/`, `patch/`, and `TODO.md` for runtime installation unless reference is explicitly needed.
- Added a short chooser block so users can quickly tell when to use the Claude Code prompt versus the Codex CLI or Gemini CLI adaptation prompts.
- Updated `TODO.md` and the master changelog to record the README install-prompt refinement.

### Summary
The README now includes copy-ready prompts users can paste into Claude Code, Codex CLI, or Gemini CLI to install or adapt the active rule set directly from this repository.

---

<a id="version-915"></a>
## Version 9.15: Added easy-to-picture concise phase/progress explanation guidance

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `explanation-quality` so phase/progress/next-step explanations now explicitly favor easy-to-picture plain-language framing before deeper mechanism detail.
- Updated `accurate-communication` so phase/progress communication now emphasizes short human-readable framing that helps the reader understand what the phase is doing and why it matters before the denser execution/result detail appears.
- Updated `answer-presentation` so phase-heavy explanations now have stronger support for concise easy-to-picture grouped presentation without becoming overlong.
- Synchronized the touched design/changelog chains plus master design/README/changelog surfaces and installed runtime copies for the explanation-style refinement.

### Summary
The RULES repository now pushes phase/progress explanations toward a shorter, easier-to-picture explanation style that helps the user see what the work is doing before the denser governance detail begins.

---

<a id="version-914"></a>
## Version 9.14: Linked live task-list behavior explicitly to the current active phase

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards` from v2.4 to v2.5 so built-in task-list usage is now expected by default for non-trivial active work, especially when an active phase already exists.
- Updated `phase-implementation` from v2.7 to v2.8 so active phases now expect a built-in task list that mirrors the current phase execution slices instead of drifting into future-phase planning.
- Updated `artifact-initiation-control` from v1.2 to v1.3 so phase-backed live task tracking is now treated as expected startup behavior rather than optional.
- Updated the touched design/changelog chains plus master design/README/changelog surfaces so current-phase-first live task tracking is explicit across the governance stack.

### Summary
The RULES repository now links live task-list behavior directly to the current active phase so execution visibility starts earlier and stays tied to the work that is actually in progress.

---

<a id="version-913"></a>
## Version 9.13: Cleaned stale custom-table detail out of active rules after suspension

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `answer-presentation` from v1.19 to v1.20 and `explanation-quality` from v2.13 to v2.14 so stale custom-table owner detail is no longer carried inside active rule text.
- Updated the two touched design companions to remove stale dependency wording and custom-format owner residue.
- Rewrote the retained `table-format-and-usage` file/design pair as suspended reference material only, so the preserved file no longer reads like an active owner.
- Moved `table-format-and-usage.md` out of the root active rule area into `suspend/table-format-and-usage.md`.
- Synchronized master docs/history/runtime state so the suspended custom-table experiment is no longer referenced as active behavior from the current rule layer.

### Summary
The active RULES system now keeps general table support without carrying stale custom-table detail forward, while the suspended experiment remains preserved separately for later redesign.

---

<a id="version-912"></a>
## Version 9.12: Suspended the custom table-format experiment from the active RULES system

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Removed active dependency on `table-format-and-usage.md` from `answer-presentation` and `explanation-quality`.
- Restored general support for using tables when they genuinely help explanation or comparison, without enforcing the suspended custom table-format doctrine.
- Removed `table-format-and-usage.md` from the active README install set and restored the active runtime inventory count from 37 to 36.
- Reframed `table-format-and-usage.md` itself as a retained-but-suspended future design candidate instead of an active enforcement owner.
- Updated the touched design/changelog/master/TODO/phase surfaces and runtime install state so the custom table-format experiment is preserved in-repo but no longer active in the RULES system.

### Summary
The custom table-format experiment is now preserved for later redesign, but it has been removed from the active RULES enforcement path while general support for using tables when helpful remains intact.

---

<a id="version-911"></a>
## Version 9.11: Hardened no-box enforcement with character-level checks and send-time self-check

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `table-format-and-usage` from v1.1 to v1.2 so generic table requests still require the canonical no-frame format and box-drawing frame characters are treated as non-compliant in ordinary assistant answers.
- Added a send-time visible-shape self-check requirement so framed table output should be rewritten before send instead of being mislabeled as plain no-frame.
- Added `phase/phase-029-03-harden-no-box-enforcement.md` for the bounded hardening slice.
- Updated the central design/changelog chain, master design inventory, README wording, TODO tracking, and runtime install copy to reflect the stronger enforcement posture.
- Deliberately kept user-driven real-world validation outside this implementation slice, per the user's instruction.

### Summary
The RULES repository now hardens no-box enforcement by checking visible framed characters directly and by requiring a final visible-shape self-check before ordinary assistant tables are sent.

---

<a id="version-910"></a>
## Version 9.10: Made the no-boxed-table rule explicit for ordinary assistant answers

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `table-format-and-usage` from v1.0 to v1.1 so ordinary assistant answers now explicitly forbid boxed, full-frame, and Unicode box-drawing tables.
- Clarified inside the central table owner that the canonical no-frame style may still use `|` separators and `-` separator lines, so the prohibition is about frame weight rather than pipe characters.
- Updated the central table-owner design, per-chain changelog, master design inventory, README wording, and runtime install copy to reflect the stricter no-box contract.
- Deliberately skipped behavioral test prompting in this wave because the user wants to validate real-world table behavior themselves rather than through direct style-prompted test commands.

### Summary
The RULES repository now makes the no-box contract explicit for ordinary assistant answers while preserving the selected plain aligned no-frame format as the required default.

---

<a id="version-99"></a>
## Version 9.9: Created a first-class table owner and centralized ordinary answer-table semantics

**Date:** 2026-04-11
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Created the new first-class `table-format-and-usage` chain from v1.0 design/runtime/changelog so ordinary answer-table usage, default style, list-versus-table boundary, bounded markdown-table exceptions, and table anti-pattern semantics now have one semantic owner.
- Updated `answer-presentation` from v1.18 to v1.19 so broader layout/scanability ownership remains there while ordinary answer-table doctrine now defers to `table-format-and-usage`.
- Updated `explanation-quality` from v2.12 to v2.13 so explanation-flow ownership remains there while explanation-side table semantics now defer to `table-format-and-usage`.
- Added `patch/table-format-and-usage-centralization.patch.md` plus `phase/phase-029-01-*` and `phase/phase-029-02-*` for the bounded ownership-transfer wave.
- Synchronized the touched design/changelog chains, master-governance surfaces, and runtime install set for the centralized table-owner wave.

### Summary
The RULES repository now gives ordinary answer-table semantics one first-class owner, so table behavior is clearer, more enforceable, and less likely to drift across adjacent chains.

---

<a id="version-97"></a>
## Version 9.7: Corrected the default table style to the selected light plain aligned no-frame form

**Date:** 2026-04-10
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `answer-presentation` from v1.17 to v1.18 so the previous compact markdown pipe-table default is replaced with the selected light plain aligned no-frame style.
- Updated `explanation-quality` from v2.11 to v2.12 so explanation-side comparison-table guidance now aligns to the same selected default style.
- Added `patch/plain-aligned-no-frame-table-style-refinement.patch.md` plus `phase/phase-028-01-*` and `phase/phase-028-02-*` for the bounded refinement wave.
- Narrowed the overreaching remembered comparison-table preference so it no longer acts like the owner of table style and instead defers to the active RULES contract.
- Synchronized the touched design/changelog chains, master-governance surfaces, and runtime install set for the table-style correction wave.

### Summary
The RULES repository now keeps tables available when useful, but the default ordinary answer-table style is explicitly the selected light plain aligned no-frame form instead of a generic compact pipe-table default.

---

<a id="version-96"></a>
## Version 9.6: Made task-list-first tracking explicit for non-trivial work across tracking/startup/documentation owners

**Date:** 2026-04-10
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `todo-standards` from v2.3 to v2.4 so Claude Code's built-in task list is now explicitly the live execution-tracking surface for non-trivial active work, while `TODO.md` remains the durable repository/project execution-tracking artifact.
- Updated `artifact-initiation-control` from v1.1 to v1.2 so startup posture now includes early live task-list initialization when non-trivial tracked work would materially benefit from visible pending / in_progress / completed state.
- Updated `project-documentation-standards` from v2.15 to v2.16 so the repository role model now explicitly distinguishes live built-in task tracking from durable `TODO.md` governance without turning the task list into a governed document artifact.
- Added `patch/task-list-first-execution-tracking.patch.md` plus `phase/phase-027-01-*` and `phase/phase-027-02-*` for the bounded refinement wave.
- Synchronized the touched design/changelog chains, master-governance surfaces, and runtime install set for the task-list-first refinement wave.

### Summary
The RULES repository now makes built-in task tracking explicit for non-trivial active work, so execution state is more visible while durable repository tracking remains in `TODO.md`.

---

<a id="version-95"></a>
## Version 9.5: Created first-class memory-governance rule chain and synchronized memory-boundary companions

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Created the new first-class `memory-governance-and-session-boundary` chain from v1.0 design/runtime/changelog so memory governance and session-boundary behavior now have one semantic owner.
- Updated `authority-and-scope` from v2.0 to v2.1 so memory applicability now defers to the new chain and non-matching path-scoped remembered context cannot override the current repo/objective.
- Updated `accurate-communication` from v2.13 to v2.14 so remembered path-scoped context is now disclosed explicitly instead of being phrased like freshly verified repo truth.
- Updated `evidence-grounded-burden-of-proof` from v1.2 to v1.3 so applicable path-scoped remembered context is now a distinct evidence/claim state rather than being conflated with current observed local fact.
- Updated `answer-presentation` from v1.16 to v1.17 so remembered path-scoped context can now be shown through a compact memory-status block rather than blending visually into current-state facts.
- Added `patch/memory-governance-and-session-boundary.patch.md` plus `phase/phase-026-01-*` through `phase/phase-026-04-*` for the bounded governance wave.
- Synchronized the touched design/changelog chains, master-governance surfaces, and runtime install set for the new memory-governance owner wave.

### Summary
The RULES repository now defines memory governance before live memory migration, keeps root `MEMORY.md` index-only, makes path the primary applicability key, keeps session IDs as provenance only, and integrates that contract into adjacent authority, communication, burden-of-proof, and presentation owners.

---

<a id="version-94"></a>
## Version 9.4: Standardized compact markdown tables and list-first alternatives for lighter answer formatting

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `answer-presentation` from v1.15 to v1.16 so compact markdown tables are now the default table form when a table is genuinely useful, full-frame ASCII/boxed tables are no longer the ordinary default, and list-first alternatives for sequence/simple status are explicit.
- Updated `explanation-quality` from v2.10 to v2.11 so explanation flow now explicitly prefers compact markdown tables only when they add real comparison value and prefers lists/bullets for sequence and simple status content.
- Added `patch/compact-markdown-table-default-and-minimal-table-usage.patch.md` plus `phase/phase-025-01-*` and `phase/phase-025-02-*` for the bounded refinement wave.
- Synchronized the touched design/changelog chains, master-governance surfaces, reinstalled the touched runtime rules into `~/.claude/rules/`, and verified runtime-copy parity for the new bounded refinement wave.

### Summary
The RULES repository now standardizes lighter compact markdown tables and makes list-first alternatives explicit, so ordinary answer formatting stays more economical and less box-heavy.

---

<a id="version-93"></a>
## Version 9.3: Added purpose-first communication framing across wording, explanation, presentation, and style owners

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `accurate-communication` from v2.12 to v2.13 so diagnosis, test, recommendation, proposal, and implementation-update answers now open with one direct sentence saying what the message is doing when that orientation materially helps the reader.
- Updated `explanation-quality` from v2.9 to v2.10 so operational explanations now use a purpose-first explanation step before deeper mechanism detail expands.
- Updated `answer-presentation` from v1.14 to v1.15 so operational answers now have a compact purpose-first framing layout pattern and snapshot examples that expose the purpose earlier.
- Updated `natural-professional-communication` from v1.1 to v1.2 so sounding natural and professional now explicitly includes purpose-before-detail wording for operational answers.
- Synchronized the touched design/changelog chains, updated the master-governance surfaces, reinstalled the touched runtime rules into `~/.claude/rules/`, and verified runtime-copy parity for the new bounded refinement wave.

### Summary
The RULES repository now makes operational answers state their purpose earlier, so the user can understand what is being tested, diagnosed, recommended, or proposed before the supporting detail unfolds.

---

<a id="version-92"></a>
## Version 9.2: Kept user-declared RULES-first issues out of memory-first fixes and hardened portable support artifacts

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `authority-and-scope` from v1.9 to v2.0 so user-declared RULES-first issues now stay on the RULES path instead of drifting into memory-first convenience.
- Updated `portable-implementation-and-hardcoding-control` from v1.1 to v1.2 so reusable support/package source artifacts such as plugin-owned docs, scripts, skills, and agents are now explicitly portable-by-default.
- Updated `project-documentation-standards` from v2.14 to v2.15 so package-local support assets are now explicitly governed as portable source artifacts when maintained for reuse.
- Updated `document-consistency` from v1.5 to v1.6 so local execution paths are now explicitly kept distinct from reusable source-artifact references.
- Added `patch/rules-first-over-memory-and-portable-support-artifacts.patch.md` plus `phase/phase-023-01-*` and `phase/phase-023-02-*` for the bounded refinement wave.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md`, then reinstalled the touched runtime rules into `~/.claude/rules/`.

### Summary
The RULES repository now keeps user-declared RULES-first issues on the RULES path and treats reusable support/package source artifacts as portable-by-default instead of letting memory-first fixes or workstation paths substitute for the real governance contract.

---

<a id="version-91"></a>
## Version 9.1: Preferred direct human-readable wording over metaphor-heavy internal shorthand

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `accurate-communication` from v2.11 to v2.12 so direct human-readable action/result wording is now preferred over metaphor-heavy internal shorthand.
- Updated `explanation-quality` from v2.8 to v2.9 so architecture-first or metaphor-heavy wording is translated into direct human-readable action/result language before deeper explanation depends on it.
- Updated `natural-professional-communication` from v1.0 to v1.1 so abstract system language is no longer treated as automatically professional when the reader still has to decode the practical meaning.
- Updated `answer-presentation` from v1.13 to v1.14 so abstract internal phrasing can be paired with a short gloss or direct implication near the term when it still appears.
- Added `patch/direct-human-readable-wording-over-metaphor-heavy-shorthand.patch.md` plus `phase/phase-022-01-*` and `phase/phase-022-02-*` for the bounded refinement wave.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md`, then reinstalled the touched runtime rules into `~/.claude/rules/`.

### Summary
The RULES repository now prefers direct human-readable wording over metaphor-heavy internal shorthand when a plain action/result statement would make the practical meaning clearer immediately.

---

<a id="version-90"></a>
## Version 9.0: Added closed-topic presentation guidance and narrowed startup patch posture

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `accurate-communication.md` from v2.10 to v2.11 and `design/accurate-communication.design.md` from v2.10 to v2.11 so resolved topics may remain available as reasoning context without being repeated in active summaries by default.
- Updated `artifact-initiation-control` from v1.0 to v1.1 so patch is non-default during greenfield / baseline-formation startup unless a real existing review surface or explicit user request exists.
- Updated `project-documentation-standards` from v2.13 to v2.14 so repository startup decisioning now treats patch as conditional on an existing governed surface rather than a default startup peer.
- Updated `document-patch-control` from v2.4 to v2.5 so patch explicitly assumes an identifiable current/before surface and rejects patch as the default startup artifact for baseline formation.
- Updated `design/design.md`, `README.md`, and `TODO.md`, then reinstalled the touched runtime rules into `~/.claude/rules/`.

### Summary
The RULES repository now keeps active summaries focused on current issues while also keeping patch non-default during greenfield baseline formation.

---

<a id="version-89"></a>
## Version 8.9: Narrowed startup patch posture for greenfield baseline formation

**Date:** 2026-04-08
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/artifact-initiation-control.design.md` from v1.0 to v1.1 and runtime `artifact-initiation-control.md` from v1.0 to v1.1 so startup patch gating now defaults to `not required` during greenfield / baseline-formation work unless a real existing review surface or explicit user request exists.
- Updated `design/project-documentation-standards.design.md` from v2.13 to v2.14 and runtime `project-documentation-standards.md` from v2.13 to v2.14 so the repository role model and startup decision flow now treat patch as conditional on an existing governed surface rather than a default startup peer.
- Updated `design/document-patch-control.design.md` from v2.4 to v2.5 and runtime `document-patch-control.md` from v2.4 to v2.5 so patch semantics now explicitly assume an identifiable current/before surface and reject patch as the default startup artifact for baseline formation.
- Updated master design, README, TODO, and per-chain changelogs to reflect the narrower startup patch posture, while keeping patch fully valid for real before/after review artifacts.

### Summary
The RULES repo now distinguishes startup baseline formation from true reviewable deltas more cleanly, so new-project formation defaults to design/changelog/TODO/phase posture first and patch only enters when a real existing before/after surface or explicit user request justifies it.

---

<a id="version-88"></a>
## Version 8.8: Tightened compact review to reference-first directive form

**Date:** 2026-04-08
**Session:** 4e792d4b-8876-439b-8c07-2c5d4b04af3a

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.7 to v1.8.
- Updated source/bridge package metadata/docs from v1.2.5 to v1.2.6.
- Tightened compact `SessionStart` so `systemMessage` now says `review-required` explicitly.
- Reduced `hookSpecificOutput.additionalContext` to bounded instruction + locator + status only, removing aggressive carried-forward summary replay.
- Added `sessionstart-directive.json` as bounded directive proof and exposed `hasDirective` in the compact index.
- Added `patch/compact-reference-first-review-trigger-refinement.patch.md` plus `phase/phase-021-01-*` through `phase/phase-021-03-*` for the bounded Wave 021 rollout.
- Updated `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the new reference-first compact review model is visible in master governance surfaces.

### Summary
The RULES compact plugin now behaves more safely after compact by keeping review guidance reference-first rather than replaying old context back into Claude.

---

<a id="version-87"></a>
## Version 8.7: Turned compact SessionStart into an active review trigger

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

---

<a id="version-86"></a>
## Version 8.6: Added reviewRoot pointers to compact navigator messages

**Date:** 2026-04-07
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.5 to v1.6.
- Updated source/bridge package metadata and docs from v1.2.2 to v1.2.3 so the installed runtime can pick up the reviewRoot navigator refinement cleanly.
- Extended compact `SessionStart` trigger messages so success-path summaries now include `reviewRoot=<compact-root>` in addition to `review=sessions/<source-session-id>/`.
- Extended fallback trigger messages so they now include `reviewRoot=<compact-root>` in addition to `review=index.json`.
- Updated package docs so the operator can reconstruct the full stored review location directly from the hook message.

### Summary
The RULES compact plugin now shows both the compact data root and the relative review target in the visible navigator line, so the stored review location is easier to follow directly from the hook message.

---

<a id="version-85"></a>
## Version 8.5: Tightened compact SessionStart to exact session-id routing

**Date:** 2026-04-07
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.4 to v1.5.
- Updated `plugin/README.md` from v1.2.1 to v1.2.2.
- Updated `changelog/rules-plugin-extension.changelog.md` from v1.5 to v1.6.
- Tightened compact `SessionStart` routing so it now requires exact `session_id` equality with one pending source session instead of consuming by looser pending-set heuristics.
- Updated success-path proof reasoning to `exact_session_id_match`.
- Updated fallback trigger wording to `no exact pending session match`.
- Updated source and shared-bridge plugin package metadata from v1.2.1 to v1.2.2.

### Summary
The RULES compact plugin now uses exact compact-session id matching as the SessionStart routing rule, which aligns the resumed session with its own stored state more deterministically.

---

<a id="version-84"></a>
## Version 8.4: Added navigator review pointers to compact trigger messages

**Date:** 2026-04-07
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `plugin/README.md` from v1.2.0 to v1.2.1.
- Updated source and shared-bridge plugin package metadata from v1.2.0 to v1.2.1.
- Upgraded compact `SessionStart` trigger messages so success-path summaries now include `review=sessions/<source-session-id>/`.
- Upgraded ambiguous fallback trigger messages so they now include `review=index.json`.
- Kept the session-scoped carry-forward model unchanged while making stored review locations easier to discover directly from the hook message.

### Summary
The RULES compact plugin now surfaces a clearer navigator line in the hook trigger message so the operator can jump directly from the visible compact message to the stored session review state.

---

<a id="version-83"></a>
## Version 8.3: Replaced singleton compact files with session-scoped carry-forward state

**Date:** 2026-04-06
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.3 to v1.4.
- Updated `plugin/README.md` from v1.1.1 to v1.2.0.
- Updated `changelog/rules-plugin-extension.changelog.md` from v1.3 to v1.4.
- Replaced singleton compact plugin files with a session-scoped state layout using `index.json` plus per-session directories for `pending.json`, `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json`.
- Changed `PreCompact` behavior so it now extracts bounded pre-compact session context and derives selected carry-forward payloads per source session.
- Recorded the current bounded limitation that transcript-based objective extraction is still heuristic/noisy when recent transcript entries are dominated by tool/skill payload text, but now fails closed instead of injecting a guessed objective.
- Changed compact `SessionStart` behavior so it now resolves exactly one pending source session, injects only that session’s selected carry-forward content, emits a navigator-style trigger message through `systemMessage` with a short review pointer, and fails closed on ambiguity instead of consuming singleton mixed state.
- Changed cleanup behavior so expired session directories are pruned and the live compact index is rewritten after cleanup.
- Updated the shared `rules-compact-extension@darkwingtm` bridge package so the maintained runtime install path matches the RULES source package behavior.
- Added `patch/compact-session-scoped-carry-forward-state-refinement.patch.md` plus `phase/phase-019-01-replace-single-slot-compact-state-with-session-scoped-layout.md` and `phase/phase-019-02-sync-docs-and-verify-session-scoped-compact-carry-forward.md` for the bounded Wave 019 rollout.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the new session-scoped compact carry-forward model is visible in master governance surfaces.

### Summary
The optional RULES plugin companion now stores compact carry-forward state per source session instead of in singleton global files, which removes cross-session collision as the default active model and keeps injection bounded to one resolved session at a time.

---

<a id="version-82"></a>
## Version 8.2: Replaced compact witness files with an ephemeral handoff lifecycle

**Date:** 2026-04-06
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `design/rules-plugin-extension.design.md` from v1.1 to v1.3.
- Updated `plugin/README.md` from v1.0.1 to v1.1.1.
- Updated `changelog/rules-plugin-extension.changelog.md` from v1.1 to v1.3.
- Replaced the plugin’s latest-only witness model with one ephemeral handoff file under `${CLAUDE_PLUGIN_DATA}/compact/active-handoff.json`.
- Added `plugin/scripts/compact-handoff-common.sh` plus renamed lifecycle scripts so `PreCompact` now creates handoff state, compact `SessionStart` consumes/deletes it, emits the compact-resume line through user-visible `systemMessage` with a `[rules-compact-extension]` prefix, keeps the re-anchor reminder in `hookSpecificOutput.additionalContext` without duplicating the signal line there, writes one bounded `last-sessionstart-consumed.json` proof file, and `PostCompact` is prune-only.
- Updated `plugin/hooks/hooks.json` so the active package behavior now uses the handoff lifecycle instead of `last-*.json` witness recording.
- Updated plugin package metadata in `plugin/.claude-plugin/plugin.json` and `plugin/.claude-plugin/marketplace.json` to v1.1.1 and renamed the package-local marketplace to `darkwingtm`.
- Added `patch/compact-ephemeral-handoff-lifecycle-refinement.patch.md` plus `phase/phase-018-01-replace-latest-witness-model-with-ephemeral-handoff.md` and `phase/phase-018-02-sync-plugin-docs-and-verify-compact-handoff-lifecycle.md` for the bounded Wave 018 rollout.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the new ephemeral handoff lifecycle is visible in master governance surfaces.

### Summary
The optional RULES plugin companion now behaves like a short-lived compact handoff cache instead of a latest-witness store, which reduces stale compact-state drift while keeping the rules-first post-compact re-anchor model unchanged.

---

<a id="version-81"></a>
## Version 8.1: Added compact/post-compact re-anchor governance and an optional plugin companion extension

**Date:** 2026-04-06
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/accurate-communication.design.md` from v2.9 to v2.10.
- Updated runtime `accurate-communication.md` from v2.9 to v2.10.
- Added post-compact re-anchor wording so compacted-session continuation now re-anchors to the active objective and separates carried-forward facts from needs-recheck detail.
- Updated `design/authority-and-scope.design.md` from v1.8 to v1.9.
- Updated runtime `authority-and-scope.md` from v1.8 to v1.9.
- Added an explicit post-compact re-anchor boundary so stale assistant framing does not revive after compact.
- Updated `design/evidence-grounded-burden-of-proof.design.md` from v1.1 to v1.2.
- Updated runtime `evidence-grounded-burden-of-proof.md` from v1.1 to v1.2.
- Added `POST_COMPACT_NEEDS_RECHECK` handling so compacted carry-forward exact detail is treated as a recheck-needed state unless enough surviving evidence still preserves its exactness.
- Updated `design/explanation-quality.design.md` from v2.7 to v2.8.
- Updated runtime `explanation-quality.md` from v2.7 to v2.8.
- Added a compact post-compact re-anchor boundary so explanations resume from active state rather than replaying stale history.
- Updated `design/answer-presentation.design.md` from v1.12 to v1.13.
- Updated runtime `answer-presentation.md` from v1.12 to v1.13.
- Added compact post-compact re-anchor layout support with a canonical block shape for `Current objective`, `Carried-forward facts`, `Needs recheck`, and `Next action`.
- Created `design/rules-plugin-extension.design.md` and `changelog/rules-plugin-extension.changelog.md` as the root design/history authority for the optional plugin companion area.
- Created `plugin/README.md`, `plugin/.claude-plugin/plugin.json`, `plugin/.claude-plugin/marketplace.json`, `plugin/hooks/hooks.json`, and compact lifecycle scripts under `plugin/scripts/`.
- Added `patch/compact-post-compact-governance-refinement.patch.md` and `patch/rules-plugin-extension-companion.patch.md` as the governed before/after artifacts for Waves 016 and 017.
- Added `phase/phase-016-01-refine-compact-and-post-compact-governance.md`, `phase/phase-016-02-sync-master-docs-and-runtime-install.md`, `phase/phase-017-01-create-rules-plugin-extension-area.md`, and `phase/phase-017-02-sync-root-docs-and-verify-plugin-companion.md` as the bounded rollout families for the new refinement and extension waves.
- Updated `project-documentation-standards` design/runtime/changelog from v2.12 to v2.13 so `plugin/**` is modeled as a support / extension-only area rather than a second governance stack.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the compact/post-compact refinement and the optional plugin companion are visible in master governance surfaces.
- Expanded plugin install/use docs so the repository now explains package-root installation, compact hook flow, witness outputs, and duplicate-hook-path troubleshooting more explicitly.
- Reinstalled the touched runtime rules into `~/.claude/rules/` and verified parity for:
  - `accurate-communication.md`
  - `authority-and-scope.md`
  - `evidence-grounded-burden-of-proof.md`
  - `explanation-quality.md`
  - `answer-presentation.md`

### Summary
The RULES system now re-anchors explicitly after compact before continuing, and the repository also has an optional plugin companion package that reinforces compact lifecycle behavior through hooks without weakening root rules authority. The install and hook-flow docs are now detailed enough for package-root use and future git push/update review.

---

<a id="version-80"></a>
## Version 8.0: Added governing-basis clarification before deep branch analysis

**Date:** 2026-04-05
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/accurate-communication.design.md` from v2.8 to v2.9.
- Updated runtime `accurate-communication.md` from v2.8 to v2.9.
- Added ask-first governing-basis clarification so the assistant now pauses deep branch analysis when materially different policy/frame choices remain live.
- Updated `design/authority-and-scope.design.md` from v1.7 to v1.8.
- Updated runtime `authority-and-scope.md` from v1.7 to v1.8.
- Added an explicit user-owned governing-basis selection boundary unless checked authority or evidence already settles the active frame.
- Updated `design/evidence-grounded-burden-of-proof.design.md` from v1.0 to v1.1.
- Updated runtime `evidence-grounded-burden-of-proof.md` from v1.0 to v1.1.
- Added `UNRESOLVED_GOVERNING_BASIS` handling so materially outcome-changing basis ambiguity is treated as uncertainty that should trigger clarification rather than silent branch selection.
- Updated `design/explanation-quality.design.md` from v2.6 to v2.7.
- Updated runtime `explanation-quality.md` from v2.6 to v2.7.
- Added a governing-basis clarification boundary so one short clarification gate is preferred over deep multi-branch explanation.
- Updated `design/answer-presentation.design.md` from v1.11 to v1.12.
- Updated runtime `answer-presentation.md` from v1.11 to v1.12.
- Added compact governing-basis clarification layout support so materially outcome-changing basis ambiguity can be presented as a short structured question.
- Added `patch/governing-basis-clarification-before-branching.patch.md` as the governed before/after artifact for the refinement wave.
- Added `phase/phase-015-01-refine-governing-basis-clarification.md` and `phase/phase-015-02-sync-master-docs-and-runtime-install.md` as the bounded rollout family for the new refinement wave.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the governing-basis clarification refinement is visible in master governance surfaces.
- Reinstalled the touched runtime rules into `~/.claude/rules/` and verified parity for:
  - `accurate-communication.md`
  - `authority-and-scope.md`
  - `evidence-grounded-burden-of-proof.md`
  - `explanation-quality.md`
  - `answer-presentation.md`

### Summary
The RULES system now asks for governing-basis selection before deep branch analysis when materially different policy/frame choices remain live, instead of silently exploring complexity that may become irrelevant once the active basis is chosen.

---

<a id="version-79"></a>
## Version 7.9: Added team-agent dedup and stale-presence boundaries

**Date:** 2026-04-04
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/custom-agent-selection-priority.design.md` from v1.0 to v1.1.
- Updated runtime `custom-agent-selection-priority.md` from v1.0 to v1.1.
- Added reuse-before-spawn guidance so an existing matching teammate should be reused before another overlapping same-role teammate is created.
- Updated `design/authority-and-scope.design.md` from v1.6 to v1.7.
- Updated runtime `authority-and-scope.md` from v1.6 to v1.7.
- Added a team-expansion boundary so assistant-created team growth is no longer justified when an existing teammate already covers the role or the new teammate has no clearly distinct job.
- Updated `design/operational-failure-handling.design.md` from v1.1 to v1.2.
- Updated runtime `operational-failure-handling.md` from v1.1 to v1.2.
- Added a `TEAM_AGENT_DUPLICATE_OR_STALE_PRESENCE` case profile so duplicate-looking team-agent state is inspected before any same-role respawn.
- Updated `design/accurate-communication.design.md` from v2.7 to v2.8.
- Updated runtime `accurate-communication.md` from v2.7 to v2.8.
- Added evidence-honest reporting guidance for duplicate-looking team-agent state so observed UI duplication is separated from inference about real overlap versus stale cleanup.
- Added `patch/team-agent-dedup-and-stale-presence-boundary.patch.md` as the governed before/after artifact for the refinement wave.
- Added `phase/phase-014-01-refine-team-agent-dedup-boundaries.md` and `phase/phase-014-02-sync-master-docs-and-runtime-install.md` as the bounded rollout family for the new refinement wave.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the team-agent dedup/stale-presence refinement is visible in master governance surfaces.
- Reinstalled the touched runtime rules into `~/.claude/rules/` and verified parity for:
  - `custom-agent-selection-priority.md`
  - `authority-and-scope.md`
  - `operational-failure-handling.md`
  - `accurate-communication.md`

### Summary
The RULES system now prefers reusing existing matching teammates, blocks overlapping team expansion without distinct purpose, and treats duplicate-looking team-agent presence as an inspect-first cleanup problem instead of a respawn-first workflow.

---

<a id="version-78"></a>
## Version 7.8: Added goal-qualified proposal boundaries across the communication-owner set

**Date:** 2026-04-04
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/accurate-communication.design.md` from v2.6 to v2.7.
- Updated runtime `accurate-communication.md` from v2.6 to v2.7.
- Added wording guidance so future-work ideas remain clearly advisory and must be goal-qualified rather than reading like queued execution.
- Updated `design/authority-and-scope.design.md` from v1.5 to v1.6.
- Updated runtime `authority-and-scope.md` from v1.5 to v1.6.
- Added an explicit boundary so assistant-generated future-work proposals do not create an active branch, implied commitment, or pending continuation until the user selects them.
- Updated `design/explanation-quality.design.md` from v2.5 to v2.6.
- Updated runtime `explanation-quality.md` from v2.5 to v2.6.
- Added proposal framing support so future ideas after bounded completion state goal, improvement, and expected output/result rather than sounding like automatic continuation.
- Updated `design/answer-presentation.design.md` from v1.10 to v1.11.
- Updated runtime `answer-presentation.md` from v1.10 to v1.11.
- Added a compact proposal pattern and canonical proposal block shape using `Proposal`, `Goal`, `Improvement`, `Output`, and optional `Success condition`.
- Added `patch/goal-qualified-proposal-boundary.patch.md` as the governed before/after artifact for the refinement wave.
- Added `phase/phase-013-01-refine-goal-qualified-proposals.md` and `phase/phase-013-02-sync-master-docs-and-runtime-install.md` as the bounded rollout family for the new refinement wave.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the proposal-boundary refinement is visible in master governance surfaces.
- Reinstalled the touched runtime rules into `~/.claude/rules/` and verified parity for:
  - `accurate-communication.md`
  - `authority-and-scope.md`
  - `explanation-quality.md`
  - `answer-presentation.md`

### Summary
The RULES system now preserves useful future-work proposals while requiring them to stay advisory, goal-qualified, and visibly separate from active execution continuation.

---

<a id="version-77"></a>
## Version 7.7: Added identifier-explanation guidance across the communication-owner trio

**Date:** 2026-04-04
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/accurate-communication.design.md` from v2.5 to v2.6.
- Updated runtime `accurate-communication.md` from v2.5 to v2.6.
- Added wording guidance so variable names, field names, config keys, enum-like values, and internal labels are no longer treated as self-explanatory when the answer depends on them.
- Updated `design/explanation-quality.design.md` from v2.4 to v2.5.
- Updated runtime `explanation-quality.md` from v2.4 to v2.5.
- Added explanation-flow support so identifier-heavy walkthroughs explain what the identifier is, what it does, where it sits in the flow, and what important values mean before the deeper reasoning relies on it.
- Updated `design/answer-presentation.design.md` from v1.9 to v1.10.
- Updated runtime `answer-presentation.md` from v1.9 to v1.10.
- Added a variable-role presentation pattern and a canonical compact variable-role table shape for identifier-heavy explanations.
- Added `patch/variable-field-config-and-term-explanation.patch.md` as the governed before/after artifact for the refinement wave.
- Added `phase/phase-012-01-refine-variable-field-config-and-term-explanations.md` and `phase/phase-012-02-sync-master-docs-and-runtime-install.md` as the bounded rollout family for the new refinement wave.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the identifier-explanation refinement is visible in master governance surfaces.
- Reinstalled the touched runtime rules into `~/.claude/rules/` and verified parity for:
  - `accurate-communication.md`
  - `explanation-quality.md`
  - `answer-presentation.md`

### Summary
The RULES system now makes identifier-heavy explanations easier to understand by requiring key variables, fields, config keys, and internal labels to be unpacked in human terms before the deeper reasoning depends on them.

---

<a id="version-76"></a>
## Version 7.6: Added recommendation-plus-reason guidance for multi-option next steps

**Date:** 2026-04-03
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/accurate-communication.design.md` from v2.4 to v2.5.
- Updated runtime `accurate-communication.md` from v2.4 to v2.5.
- Added wording guidance so when multiple reasonable next actions are shown and one path is better-supported, the response names that path first as the recommendation and follows it with a short plain-language why-first reason.
- Updated `design/explanation-quality.design.md` from v2.3 to v2.4.
- Updated runtime `explanation-quality.md` from v2.3 to v2.4.
- Added explanation-ending support so recommendation-heavy endings now make the preferred next path explicit and explain briefly why it should happen first.
- Updated `design/answer-presentation.design.md` from v1.8 to v1.9.
- Updated runtime `answer-presentation.md` from v1.8 to v1.9.
- Added layout guidance and canonical label support for:
  - `Recommended`
  - `Why this first`
  - `Other options`
- Added `patch/recommended-option-and-why-this-first.patch.md` as the governed before/after artifact for the refinement wave.
- Added `phase/phase-011-01-refine-recommended-option-wording.md` and `phase/phase-011-02-sync-master-docs-and-runtime-install.md` as the bounded rollout family for the new refinement wave.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the recommendation-format refinement is visible in master governance surfaces.
- Reinstalled the touched runtime rules into `~/.claude/rules/` and verified parity for:
  - `accurate-communication.md`
  - `explanation-quality.md`
  - `answer-presentation.md`

### Summary
The RULES system now keeps multi-option next-step guidance easier to act on by making the preferred path and its reason visible, while still preserving at least one visible alternative when the real decision surface is genuinely multi-path.

---

<a id="version-75"></a>
## Version 7.5: Refined public install portability and source-vs-destination notation across hardcoding-governance owners

**Date:** 2026-04-03
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/portable-implementation-and-hardcoding-control.design.md` from v1.0 to v1.1.
- Updated runtime `portable-implementation-and-hardcoding-control.md` from v1.0 to v1.1.
- Expanded the portability owner so public onboarding/install docs, repo-root source guidance, source-vs-destination notation, and internal umbrella workspace roots as public defaults are now first-class governed concerns.
- Updated `design/project-documentation-standards.design.md` from v2.11 to v2.12.
- Updated runtime `project-documentation-standards.md` from v2.11 to v2.12.
- Added repository-level enforcement so public README/install docs now:
  - default to portable repo-root or equivalent source guidance when possible
  - avoid workstation-specific absolute paths as public defaults
  - distinguish source-side references from destination/runtime references
- Updated `design/document-consistency.design.md` from v1.4 to v1.5.
- Updated runtime `document-consistency.md` from v1.4 to v1.5.
- Added reference-role separation for portable shared references, source-side install references, destination/runtime references, checked local facts, and machine-scoped examples.
- Added `patch/install-doc-portability-and-source-destination-notation.patch.md` as the governed before/after artifact for the refinement wave.
- Added `phase/phase-010-01-refine-install-doc-portability-owners.md` and `phase/phase-010-02-sync-master-governance-and-runtime-install.md` as the bounded rollout family for the new refinement wave.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the public-install portability refinement is visible in master governance surfaces.
- Reinstalled the touched runtime rules into `~/.claude/rules/` and verified parity for:
  - `portable-implementation-and-hardcoding-control.md`
  - `project-documentation-standards.md`
  - `document-consistency.md`

### Summary
Strengthened the hardcoding-governance model so public install/onboarding docs now stay portable by default and keep source-side versus destination/runtime path roles explicit instead of letting one workstation path silently represent both.

---

<a id="version-74"></a>
## Version 7.4: Opened continuation-priority refinement across communication-owner chains

**Date:** 2026-04-03
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Opened `patch/continuation-priority-and-option-offering.patch.md` as the governed before/after artifact for the new refinement wave.
- Added `phase/phase-009-01-audit-continuation-vs-interruption.md` and `phase/phase-009-02-implement-continuation-priority.md` to track the bounded rollout.
- Updated `phase/SUMMARY.md` and `TODO.md` so the new refinement wave is visible in active execution tracking.
- Identified `accurate-communication` as the primary semantic owner for continuation-vs-option behavior, with `answer-presentation`, `explanation-quality`, and `authority-and-scope` as the adjacent overlap set.

### Summary
Opened a bounded RULES refinement wave that aims to make active work continue by default and narrow unnecessary mid-process option prompting across the communication-owner chains.

---

<a id="version-73"></a>
## Version 7.3: Deepened portability-rule integration across adjacent chains

**Date:** 2026-04-02
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `no-variable-guessing` to v1.4 so checked local values now explicitly stay scoped local facts and defer broader portable-default ownership to the new chain.
- Updated `accurate-communication` to v2.3 so machine-specific values in technical snapshots now stay presentation-scoped as local facts rather than reading like portable defaults.
- Updated `project-documentation-standards` to v2.11 so shared governed docs/templates now explicitly stay portable by default.
- Updated `strict-file-hygiene` to v1.3 so reusable artifacts now avoid machine-local hardcoded defaults by default.
- Updated `tactical-strategic-programming` to v1.2, `document-consistency` to v1.4, and `answer-presentation` to v1.7 as the next bounded adjacent integration slice.
- Added and completed `phase/phase-008-03-deepen-portability-integration.md` as the bounded second integration slice for the new owner.

### Summary
Deepened the new portability owner’s influence across adjacent chains so hardcoding-control now affects tactical execution, document consistency, and presentation behavior more concretely instead of remaining a standalone chain only.

---

<a id="version-72"></a>
## Version 7.2: Created first-class portable-implementation-and-hardcoding-control rule chain and synchronized hardcoding governance

**Date:** 2026-04-02
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/portable-implementation-and-hardcoding-control.design.md`, `portable-implementation-and-hardcoding-control.md`, and `changelog/portable-implementation-and-hardcoding-control.changelog.md` as a new first-class rule chain.
- Added `patch/portable-implementation-and-hardcoding-control.patch.md` as the governed before/after artifact for the rollout.
- Added `phase/phase-008-01-create-portable-implementation-rule.md` and `phase/phase-008-02-integrate-hardcoding-governance.md` as the rollout family for the new chain.
- Updated `design/design.md` from 34 to 35 active runtime rules and registered the new chain as the owner for portable defaults and anti-hardcoding discipline.
- Updated `README.md` so the public inventory now includes the new chain and describes its portable-implementation role explicitly.
- Updated `TODO.md` and `phase/SUMMARY.md` so the rollout is visible in execution tracking and phase indexing.

### Summary
Added one explicit semantic owner for portable implementation defaults, late-bound environment resolution, observed-local-fact separation, and anti-hardcoding discipline so machine-specific assumptions do not silently become shared defaults.

---

<a id="version-71"></a>
## Version 7.1: Created first-class custom-agent-selection-priority rule chain and synchronized agent-selection governance

**Date:** 2026-03-31
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/custom-agent-selection-priority.design.md`, `custom-agent-selection-priority.md`, and `changelog/custom-agent-selection-priority.changelog.md` as a new first-class rule chain.
- Added `patch/custom-agent-selection-priority.patch.md` as the governed before/after artifact for the rollout.
- Added `phase/phase-007-01-create-custom-agent-selection-rule.md` and `phase/phase-007-02-integrate-agent-selection-governance.md` as the rollout family for the new chain.
- Updated `design/design.md` from 33 to 34 active runtime rules and placed the new chain in the User Control category.
- Updated `README.md` so the public inventory now includes the new chain and describes its custom-agent priority role more explicitly.
- Updated `TODO.md` and `phase/SUMMARY.md` so the rollout is visible in execution tracking and phase indexing.

### Summary
Added one explicit semantic owner for preferring visible user custom agents as the primary specialist pool when task fit is clear, while keeping runtime discovery/loading as a separate concern.

---

<a id="version-70"></a>
## Version 7.0: Created first-class external-verification-and-source-trust rule chain and synchronized source-trust governance

**Date:** 2026-03-31
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/external-verification-and-source-trust.design.md`, `external-verification-and-source-trust.md`, and `changelog/external-verification-and-source-trust.changelog.md` as a new first-class rule chain.
- Added `patch/external-verification-and-source-trust.patch.md` as the governed before/after artifact for the rollout.
- Added `phase/phase-006-01-create-external-verification-rule.md` and `phase/phase-006-02-integrate-source-trust-governance.md` as the rollout family for the new chain.
- Updated `design/design.md` from 32 to 33 active runtime rules and placed the new chain in the Accuracy & Truth category.
- Updated `README.md` so the public inventory now includes the new chain and describes its source-trust role more explicitly.
- Updated `TODO.md` and `phase/SUMMARY.md` so the rollout is visible in execution tracking and phase indexing.

### Summary
Added one explicit semantic owner for proactive external verification, source-trust ranking, corroboration, and source-conflict handling so the RULES system can improve accuracy through stronger external-evidence workflow rather than only through cautious wording.

---

<a id="version-69"></a>
## Version 6.9: Hardened explicit phase-to-patch linkage in phased work

**Date:** 2026-03-30
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/phase-implementation.design.md` from v2.6 to v2.7.
- Updated runtime `phase-implementation.md` from v2.6 to v2.7.
- Added an explicit live-workspace linkage rule: when phased work uses governed patch artifacts, `phase/SUMMARY.md` and the relevant child phase files must declare that linkage explicitly.
- Clarified that `none` should be used only when patch is genuinely not required, not as a placeholder for an unresolved decision.
- Updated `phase-implementation-template.md` so the helper teaches the same explicit linkage expectation.
- Updated `design/project-documentation-standards.design.md` from v2.9 to v2.10.
- Updated runtime `project-documentation-standards.md` from v2.9 to v2.10.
- Added repository-level verification guidance so phased work with governed patch artifacts must show explicit patch linkage from `phase/SUMMARY.md` and relevant child phase files.
- Added `patch/phase-linkage-hardening.patch.md` as the governed before/after artifact for the refinement.
- Added `phase/phase-005-01-harden-phase-patch-linkage.md` and `phase/phase-005-02-sync-master-docs-and-history.md` as the rollout family for the narrow linkage-hardening wave.
- Updated `phase/SUMMARY.md` and `TODO.md` so the new wave is visible in phase indexing and execution history.

### Summary
Completed a narrow follow-up that preserves the existing phase/patch boundary model while making the relationship explicit in the live phase workspace whenever governed patch artifacts are in scope.

---

<a id="version-68"></a>
## Version 6.8: Created startup artifact-initiation governance and synchronized the repository to artifact-first work startup

**Date:** 2026-03-28
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/project-documentation-standards.design.md` from v2.8 to v2.9.
- Updated runtime `project-documentation-standards.md` from v2.8 to v2.9.
- Created `design/artifact-initiation-control.design.md`, `artifact-initiation-control.md`, and `changelog/artifact-initiation-control.changelog.md`.
- Added `artifact-initiation-control.md` as the startup-governance owner in the repository model.
- Updated `design/phase-implementation.design.md` from v2.5 to v2.6.
- Updated runtime `phase-implementation.md` from v2.5 to v2.6.
- Added an early phase-establishment bridge so `/phase` is established before drift when startup governance already shows phased work is required.
- Updated `design/todo-standards.design.md` and runtime `todo-standards.md` to v2.3.
- Created `changelog/todo-standards.changelog.md`.
- Updated `design/strict-file-hygiene.design.md`, `strict-file-hygiene.md`, and `changelog/strict-file-hygiene.changelog.md` to v1.2.
- Opened the new startup-governance rollout family under `phase/phase-004-01-*` through `phase/phase-004-03-*`.
- Updated `design/design.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` so the new startup-governance model is visible repository-wide.

### Summary
Completed the startup-governance rollout so meaningful governed work now resolves artifact posture before drift instead of relying on late-stage backfill.

---

<a id="version-67"></a>
## Version 6.7: Corrected the repository-wide patch model to explicit before/after artifacts in `patch/` or at root

**Date:** 2026-03-28
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `design/document-patch-control.design.md`, `document-patch-control.md`, and `changelog/document-patch-control.changelog.md` from v2.3 to v2.4.
- Updated `design/project-documentation-standards.design.md`, `project-documentation-standards.md`, and `changelog/project-documentation-standards.changelog.md` from v2.7 to v2.8.
- Updated `design/phase-implementation.design.md`, `phase-implementation.md`, and `changelog/phase-implementation.changelog.md` from v2.4 to v2.5.
- Updated `design/tactical-strategic-programming.design.md`, `tactical-strategic-programming.md`, and `changelog/tactical-strategic-programming.changelog.md` from v1.0 to v1.1.
- Replaced active `patches/` placement teaching with `patch/` or root `<context>.patch.md`.
- Clarified that patch means a self-identifying before/after artifact, not a prose-only recap.
- Updated `phase-implementation-template.md`, `README.md`, `design/design.md`, and related supporting design docs to the corrected patch model.
- Moved the in-repo example patches into `patch/` and rewrote them as explicit before/after artifacts.
- Updated patch changelogs, TODO tracking, and parent-document references to match the moved patch paths.

### Summary
Completed the repository-level patch-role correction so the active RULES model now teaches one explicit patch concept: governed before/after artifacts in `patch/` or at repository root.

---

<a id="version-65"></a>
## Version 6.5: Created natural-professional-communication rule chain and synchronized communication-owner refinements

**Date:** 2026-03-27
**Session:** a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2

### Changes
- Created `design/natural-professional-communication.design.md`, `natural-professional-communication.md`, and `changelog/natural-professional-communication.changelog.md` as a new first-class communication-style doctrine chain.
- Created `phase/SUMMARY.md` and `phase/phase-001-*` to `phase/phase-004-*` execution artifacts for the RULES development rollout of the new chain and related refinement wave.
- Updated `accurate-communication` to v2.2, `explanation-quality` to v2.2, `answer-presentation` to v1.6, `authority-and-scope` to v1.4, and `anti-sycophancy` to v1.4 with calmer, more natural, non-robotic, non-character-driven professional communication guidance.
- Updated `design/design.md` and `README.md` from 30 to 31 active runtime rules, corrected the canonical install set from the stale 29-rule wording, and normalized lingering `phase-010-*` README references to `phase-001-*`.
- Updated `TODO.md` to record rollout completion and re-synchronized touched runtime rules into `~/.claude/rules/` with parity verification.

### Summary
Added one explicit semantic authority for natural professional communication and aligned the wording, explanation, presentation, authority, and disagreement chains so the system now defaults to calmer, more human-readable, non-robotic professional communication.

---

<a id="version-64"></a>
## Version 6.4: Changed default phase numbering to 001/002/003 across phase-implementation governance

**Date:** 2026-03-17
**Session:** 9b6e3a46-d4f0-4968-9f5a-be083de4304c

### Changes
- Updated `phase-implementation` design/runtime/changelog to v2.2 with zero-padded contiguous child-phase numbering (`001/002/003`) instead of sparse `010/020/030`.
- Updated `phase-implementation-template.md` examples and helper guidance to the new numbering scheme.
- Updated `design/design.md` and `README.md` wording to reflect the new default numbering policy.
- Updated `TODO.md` completion/history tracking for the phase-numbering patch wave and synced the installed runtime copy.

### Summary
Refined the phase-planning model so default phase numbering is now human-readable and naturally sequential (`001/002/003`) rather than sparse by default.

---

<a id="version-63"></a>
## Version 6.3: Created first-class tactical-strategic-programming rule chain and synchronized master governance

**Date:** 2026-03-17
**Session:** 77d0802a-fd64-4023-a66d-88c165ccca12

### Changes
- Created `design/tactical-strategic-programming.design.md`, `tactical-strategic-programming.md`, and `changelog/tactical-strategic-programming.changelog.md` as a new first-class doctrine chain.
- Created `phase/SUMMARY.md` and `phase/phase-001-*` to `phase/phase-003-*` execution artifacts for the RULES development rollout of the new chain.
- Updated `design/design.md` and `README.md` from 29 to 30 active runtime rules and registered the new doctrine in the Quality & Governance model.
- Updated `TODO.md` to record rollout completion and installed the runtime rule into `~/.claude/rules/tactical-strategic-programming.md`.

### Summary
Added one explicit semantic authority for tactical entry, strategic target, convergence path, and strategic closure so fast local execution can be governed without strategic drift.
