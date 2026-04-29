# Changelog - Authority and Scope

> **Parent Document:** [../authority-and-scope.md](../authority-and-scope.md)
> **Current Version:** 2.5
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 2.5 | 2026-04-25 | **[Added runtime destination ownership boundary](#version-25)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| 2.4 | 2026-04-17 | **[Added repo-governed semantic-authority precedence over git-state cleanup heuristics](#version-24)** | a9bec472-1706-4019-8cfd-5ba988a71662 |
| 2.3 | 2026-04-13 | **[Deferred shared-board multi-session coordination semantics to the new coordination owner](#version-23)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.2 | 2026-04-12 | **[Deferred mode-selection semantics to the new execution-continuity owner](#version-22)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.1 | 2026-04-09 | **[Added path-scoped memory applicability boundary and current-scope-wins protection](#version-21)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 2.0 | 2026-04-09 | **[Added RULES-first-over-memory authority boundary](#version-20)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.9 | 2026-04-06 | **[Added post-compact re-anchor boundary for stale-frame recovery](#version-19)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.8 | 2026-04-05 | **[Added user-owned governing-basis selection boundary](#version-18)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.7 | 2026-04-04 | **[Added team-expansion boundary for overlapping teammate roles](#version-17)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.6 | 2026-04-04 | **[Kept future-work proposals advisory until explicitly selected](#version-16)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.5 | 2026-04-03 | **[Discouraged unnecessary option branching when one safe continuation exists](#version-15)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.4 | 2026-03-27 | **[Added neutral professional default-mode guidance to authority-and-scope](#version-14)** | a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2 |
| | | Summary: Extended authority-and-scope so the assistant now stays in a neutral professional communication mode by default unless the user explicitly asks for another style | |
| 1.3 | 2026-03-17 | **[Added fresh-user-directive override over previously offered assistant options](#version-13)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Refined authority-and-scope so assistant-generated options remain advisory only and a fresh user directive overrides prior option framing unless the user explicitly selected one | |
| 1.2 | 2026-03-08 | **[Normalized runtime metadata header to canonical cleanup-wave contract](#version-12)** | 41261a5a-d60b-4f6c-b174-229df0a58ac2 |
| | | Summary: Added canonical runtime header metadata and aligned the authority-and-scope chain to the cleanup-wave version state | |
| 1.1 | 2026-02-22 | **[Added deterministic precedence contract and tie-break semantics](#version-11-added-deterministic-precedence-contract-and-tie-break-semantics)** | f19e8a67-d3c2-4c85-aa11-4db6949e61f8 |
| | | - Upgraded rule/design alignment from v1.0 to v1.1 around explicit precedence ordering | |
| | | - Added normalized term definitions for hard-boundary conflict handling | |
| | | Summary: Synchronized authority rule and design to deterministic conflict-resolution behavior | |
| 1.0 | 2026-02-01 | **[Standardization](#version-10-standardization)** | a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7 |
| | | Summary: Migrated to standard template | |

---

<a id="version-25"></a>
## Version 2.5: Added runtime destination ownership boundary

**Date:** 2026-04-25
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Updated `authority-and-scope.md` from v2.4 to v2.5.
- Updated `design/authority-and-scope.design.md` from v2.4 to v2.5.
- Added explicit runtime co-location wording so a file appearing in a shared runtime directory does not become governed by the current source project.
- Added destination/runtime owner-scope guidance so files outside the current source-owned install set require owner/project scope resolution before classification, cleanup, or deletion is considered.

### Summary
Authority-and-scope now treats shared runtime directory placement as observed co-location only, not ownership authority, and requires owner/project scope resolution before classifying or cleaning up destination files outside the current source-owned install set.

---

<a id="version-24"></a>
## Version 2.4: Added repo-governed semantic-authority precedence over git-state cleanup heuristics

**Date:** 2026-04-17
**Session:** a9bec472-1706-4019-8cfd-5ba988a71662

### Changes
- Updated `authority-and-scope.md` from v2.3 to v2.4.
- Updated `design/authority-and-scope.design.md` from v2.3 to v2.4.
- Added a repository-governed semantic-authority bridge so checked master surfaces and checked governed owner chains now outrank git working state when classifying file meaning.
- Added explicit conflict, required-behavior, and anti-pattern wording so git cleanliness, untracked status, and cleanup/isolation heuristics no longer read like semantic authority or deletion permission.

### Summary
Authority-and-scope now explicitly keeps repo-governed semantic surfaces above git-state and cleanup heuristics, closing a key precedence gap behind cleanup-driven disposal misreads.

---

<a id="version-23"></a>
## Version 2.3: Deferred shared-board multi-session coordination semantics to the new coordination owner

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `authority-and-scope.md` from v2.2 to v2.3.
- Updated `design/authority-and-scope.design.md` from v2.2 to v2.3.
- Historical note: that wave originally deferred shared-board multi-session coordination semantics to `shared-execution-coordination.md` before Main RULES later retired that in-repo coordination owner from active doctrine.
- Preserved overall precedence, user authority, and fresh-directive override behavior.

### Summary
Authority-and-scope now keeps top-level precedence and user-authority behavior while deferring shared-board coordination protocol details to the new coordination owner.

---

<a id="version-22"></a>
## Version 2.2: Deferred mode-selection semantics to the new execution-continuity owner

**Date:** 2026-04-12
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `authority-and-scope.md` from v2.1 to v2.2.
- Updated `design/authority-and-scope.design.md` from v2.1 to v2.2.
- Added an explicit deferral so discussion-vs-execution mode selection and continuous-execution defaults now live in `execution-continuity-and-mode-selection.md` instead of remaining implicit here.
- Preserved user authority, governing-basis ownership, and fresh-directive override behavior.

### Summary
Authority-and-scope now keeps its precedence role while deferring execution-mode selection semantics to the new first-class execution-continuity owner.

---

<a id="version-21"></a>
## Version 2.1: Added path-scoped memory applicability boundary and current-scope-wins protection

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `authority-and-scope.md` from v2.0 to v2.1.
- Updated `design/authority-and-scope.design.md` from v2.0 to v2.1.
- Added an explicit deferral to `memory-governance-and-session-boundary.md` for memory applicability and memory organization semantics.
- Added a current-scope-wins boundary so path-scoped remembered context cannot override the current repo/objective when the scope does not match, even if the memory came from the same or a recent session.
- Added conflict-type, required-behavior, and anti-pattern coverage so same-session continuity no longer acts like proof that remembered context still applies.

### Summary
Authority-and-scope now keeps current repo/objective authority above non-matching path-scoped remembered context and defers memory applicability semantics to the new memory-governance owner.

---

<a id="version-20"></a>
## Version 2.0: Added RULES-first-over-memory authority boundary

**Date:** 2026-04-09
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `authority-and-scope.md` from v1.9 to v2.0.
- Updated `design/authority-and-scope.design.md` from v1.9 to v2.0.
- Added an explicit boundary that when the user says an issue should be solved in RULES rather than memory, the assistant must treat RULES refinement as the primary path and must not use a memory write as the substitute fix for that same issue.
- Added conflict-type and anti-pattern coverage so user-declared RULES-first handling no longer drifts into memory-first convenience.

### Summary
Authority-and-scope now keeps user-declared RULES-first issues on the RULES path instead of letting memory persistence substitute for the governing fix.

---

<a id="version-19"></a>
## Version 1.9: Added post-compact re-anchor boundary for stale-frame recovery

**Date:** 2026-04-06
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `authority-and-scope.md` from v1.8 to v1.9.
- Updated `design/authority-and-scope.design.md` from v1.8 to v1.9.
- Added an explicit post-compact re-anchor boundary so compacted-session continuation now preserves the latest active user directive and active governing basis.
- Added conflict-type, term-definition, required-behavior, and anti-pattern coverage so stale assistant framing does not quietly revive after compact.

### Summary
Authority-and-scope now requires post-compact continuation to re-anchor to the latest active user directive and active frame instead of resuming from stale assistant framing.

---

## Version 1.8: Added user-owned governing-basis selection boundary

**Date:** 2026-04-05
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `authority-and-scope.md` from v1.7 to v1.8.
- Updated `design/authority-and-scope.design.md` from v1.7 to v1.8.
- Added an explicit boundary that when multiple materially different governing bases remain unresolved, basis selection belongs to the user unless checked authority or evidence already settles it.
- Added conflict-type, term-definition, required-behavior, and anti-pattern coverage so exploratory framing no longer silently becomes the active basis.

### Summary
Authority-and-scope now keeps governing-basis selection user-owned when materially different policy/frame choices remain unresolved.

---

<a id="version-17"></a>
## Version 1.7: Added team-expansion boundary for overlapping teammate roles

**Date:** 2026-04-04
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `authority-and-scope.md` from v1.6 to v1.7.
- Updated `design/authority-and-scope.design.md` from v1.6 to v1.7.
- Added a boundary so assistant-created team expansion is not treated as a default move when an existing teammate already covers the role or the new teammate has no clearly distinct job.
- Added anti-pattern coverage against treating team expansion as the automatic answer when the role is already covered.

### Summary
Authority-and-scope now keeps overlapping teammate expansion advisory and bounded instead of letting it become an implicit default branch.

---

<a id="version-16"></a>
## Version 1.6: Kept future-work proposals advisory until explicitly selected

**Date:** 2026-04-04
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `authority-and-scope.md` from v1.5 to v1.6.
- Updated `design/authority-and-scope.design.md` from v1.5 to v1.6.
- Added an explicit rule that assistant-generated future-work proposals remain advisory only and do not create an active branch, implied commitment, or pending continuation unless the user explicitly selects them.
- Extended term-definition and anti-pattern coverage so future-wave suggestions no longer blur into active execution state.

### Summary
Authority-and-scope now keeps future-work proposals visibly advisory until the user explicitly chooses them as the next target.

---

<a id="version-15"></a>
## Version 1.5: Discouraged unnecessary option branching when one safe continuation exists

**Date:** 2026-04-03
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `authority-and-scope.md` from v1.4 to v1.5.
- Updated `design/authority-and-scope.design.md` from v1.4 to v1.5.
- Added a rule against generating unnecessary user-choice branches when one continuation path is already implied by the request and can be executed safely.
- Added matching anti-pattern and integration guidance so stale-option override logic no longer normalizes option generation as a default behavior.

### Summary
Authority-and-scope now keeps assistant-generated options advisory while also discouraging unnecessary option branching when one safe continuation path already exists.

---

<a id="version-14"></a>
## Version 1.4: Added neutral professional default-mode guidance to authority-and-scope

**Date:** 2026-03-27
**Session:** a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2

### Changes
- Updated `authority-and-scope.md` from v1.3 to v1.4.
- Updated `design/authority-and-scope.design.md` from v1.3 to v1.4.
- Added an explicit default-mode rule that the assistant should remain in a neutral professional communication mode unless the user explicitly requests another style.
- Added conflict and quality guidance so user-directed style requests can override the default in non-hard-boundary cases.
- Kept the existing fresh-user-directive override contract intact while adding default-mode clarity.

### Summary
Extended authority-and-scope so the assistant now stays in a neutral professional communication mode by default unless the user explicitly asks for another style.

---

<a id="version-13"></a>
## Version 1.3: Added fresh-user-directive override over previously offered assistant options

**Date:** 2026-03-17
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `authority-and-scope.md` from v1.2 to v1.3.
- Updated `design/authority-and-scope.design.md` from v1.2 to v1.3.
- Added an explicit rule that assistant-generated options are advisory only unless the user explicitly selects one.
- Added an explicit precedence rule that a fresh user directive overrides previously offered assistant options when it changes scope, task, or action.
- Extended the conflict-resolution contract and quality metrics to cover fresh-directive override behavior.

### Summary
Refined authority-and-scope so a new user instruction cannot get trapped behind previously offered assistant options unless the user explicitly chooses one of them.

---

<a id="version-12"></a>
## Version 1.2: Normalized runtime metadata header to canonical cleanup-wave contract

**Date:** 2026-03-08
**Session:** 41261a5a-d60b-4f6c-b174-229df0a58ac2

### Changes
- Updated `authority-and-scope.md` from v1.1 to v1.2.
- Updated `design/authority-and-scope.design.md` from v1.1 to v1.2.
- Added canonical root runtime header fields in active metadata order:
  - `Current Version`
  - `Design`
  - `Session`
  - `Full history`
- Preserved the existing deterministic authority-order and tie-break semantics.

### Summary
Normalized the authority-and-scope chain to the canonical cleanup-wave runtime header format while preserving substantive authority behavior.

---

## Version 1.1: Added deterministic precedence contract and tie-break semantics

**Date:** 2026-02-22
**Session:** f19e8a67-d3c2-4c85-aa11-4db6949e61f8

### Changes
- Updated `authority-and-scope.md` to v1.1 with explicit precedence matrix:
  - `HARD_BOUNDARY`
  - `USER_INSTRUCTION`
  - `RULE_CONTRACTS`
  - `DEFAULT_BEHAVIOR`
- Added deterministic term definitions for:
  - `higher-level safety policies`
  - `hard boundary`
  - `unresolved block`
- Added tie-break rules for hard-boundary conflicts and unresolved non-hard ambiguity.
- Updated `design/authority-and-scope.design.md` to v1.1 with matching conflict-resolution contract.

### Summary
Synchronized authority rule and design to deterministic precedence and tie-break semantics.

---

## Version 1.0: Standardization

**Date:** 2026-02-01
**Session:** a77b77ae-ef2a-49f6-93d9-f78c8ac2d2f7

### Changes
- Migrated rule to standard template
- Established version history in changelog file

### Summary
Migrated to standard template
