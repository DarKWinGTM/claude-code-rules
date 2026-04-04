# Master Changelog - Claude Code Rules

> **Project:** Claude Code Rules System
> **Current Version:** 7.8
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 7.8 | 2026-04-04 | **[Added goal-qualified proposal boundaries across the communication-owner set](#version-78)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.7 | 2026-04-04 | **[Added identifier-explanation guidance across the communication-owner trio](#version-77)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.6 | 2026-04-03 | **[Added recommendation-plus-reason guidance for multi-option next steps](#version-76)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Updated `accurate-communication` to v2.5 so multi-path next-step guidance now names the recommended option first and explains briefly why it should happen first | |
| | | - Updated `explanation-quality` to v2.4 and `answer-presentation` to v1.9 so explanation endings and layouts now reinforce the same recommendation-plus-reason pattern without reintroducing option-first interruption | |
| | | - Added `patch/recommended-option-and-why-this-first.patch.md` plus `phase/phase-011-01-*` and `phase/phase-011-02-*` to record the bounded refinement wave | |
| | | - Updated master design, README, TODO, changelog, and `phase/SUMMARY.md`, then reinstalled the touched runtime rules into `~/.claude/rules/` | |
| | | Summary: When multiple next actions are genuinely shown, the RULES system now makes the preferred path easier to act on by pairing `Recommended` with a short `Why this first` reason while still keeping at least one visible alternative when the decision surface is truly multi-path | |
| 7.5 | 2026-04-03 | **[Refined public install portability and source-vs-destination notation across hardcoding-governance owners](#version-75)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Updated `portable-implementation-and-hardcoding-control` to v1.1 so public onboarding/install docs, source-side versus destination/runtime notation, and internal umbrella workspace roots as public defaults are now first-class portability concerns | |
| | | - Updated `project-documentation-standards` to v2.12 and `document-consistency` to v1.5 so README/install docs now enforce portable repo-root guidance and keep source-side references distinct from destination/runtime references | |
| | | - Added `patch/install-doc-portability-and-source-destination-notation.patch.md` plus `phase/phase-010-01-*` and `phase/phase-010-02-*` to record the bounded refinement wave | |
| | | - Updated master design, README, TODO, changelog, and `phase/SUMMARY.md`, then reinstalled the touched runtime rules into `~/.claude/rules/` | |
| | | Summary: The hardcoding-governance model now explicitly treats public install/onboarding path posture as a portability concern and stops one workstation path from silently acting as both source and destination/runtime truth | |
| 7.4 | 2026-04-03 | **[Opened continuation-priority refinement across communication-owner chains](#version-74)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 7.3 | 2026-04-02 | **[Deepened portability-rule integration across adjacent chains](#version-73)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Updated `no-variable-guessing`, `accurate-communication`, `project-documentation-standards`, and `strict-file-hygiene` to defer broader anti-hardcoding ownership to `portable-implementation-and-hardcoding-control` | |
| | | - Deepened the next integration slice into `tactical-strategic-programming`, `document-consistency`, and `answer-presentation` so machine-specific defaults are less likely to leak through tactical behavior, reference examples, or presentation patterns | |
| | | - Opened and completed `phase-008-03-deepen-portability-integration.md` as the bounded second integration slice | |
| | | Summary: The portable-implementation owner now has meaningful adjacent-chain integration rather than existing only as a standalone chain | |
| 7.2 | 2026-04-02 | **[Created first-class portable-implementation-and-hardcoding-control rule chain and synchronized hardcoding governance](#version-72)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Created `design/portable-implementation-and-hardcoding-control.design.md`, `portable-implementation-and-hardcoding-control.md`, and `changelog/portable-implementation-and-hardcoding-control.changelog.md` as a new first-class chain | |
| | | - Added `patch/portable-implementation-and-hardcoding-control.patch.md` plus `phase/phase-008-01-*` and `phase/phase-008-02-*` to record the rollout family | |
| | | - Updated master design, README, TODO, changelog, and `phase/SUMMARY.md` so the new portable-implementation owner is visible across the active repository model | |
| | | Summary: Added one explicit semantic owner for portable implementation defaults, late-bound environment resolution, scoped local observations, and anti-hardcoding discipline so machine-specific assumptions do not silently become shared defaults | |
| 7.1 | 2026-03-31 | **[Created first-class custom-agent-selection-priority rule chain and synchronized agent-selection governance](#version-71)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Created `design/custom-agent-selection-priority.design.md`, `custom-agent-selection-priority.md`, and `changelog/custom-agent-selection-priority.changelog.md` as a new first-class chain | |
| | | - Added `patch/custom-agent-selection-priority.patch.md` plus `phase/phase-007-01-*` and `phase/phase-007-02-*` to record the rollout family | |
| | | - Updated master design, README, TODO, changelog, and `phase/SUMMARY.md` so the new agent-selection owner is visible across the active repository model | |
| | | Summary: Added one explicit semantic owner for preferring visible user custom agents as the primary specialist pool when task fit is clear, without pretending that prompt rules control runtime discovery | |
| 7.0 | 2026-03-31 | **[Created first-class external-verification-and-source-trust rule chain and synchronized source-trust governance](#version-70)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Created `design/external-verification-and-source-trust.design.md`, `external-verification-and-source-trust.md`, and `changelog/external-verification-and-source-trust.changelog.md` as a new first-class chain | |
| | | - Added `patch/external-verification-and-source-trust.patch.md` plus `phase/phase-006-01-*` and `phase/phase-006-02-*` to record the rollout family | |
| | | - Updated master design, README, TODO, and `phase/SUMMARY.md` so the new source-trust owner is visible across the active repository model | |
| | | Summary: Added one explicit semantic owner for proactive external verification, source-trust ranking, corroboration, and source-conflict handling so the RULES system becomes more accurate through better external evidence workflow, not just more cautious phrasing | |
| 6.9 | 2026-03-30 | **[Hardened explicit phase-to-patch linkage in phased work](#version-69)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Updated `phase-implementation` design/runtime/helper to require explicit patch linkage in `phase/SUMMARY.md` and relevant child phase files when patch is in scope | |
| | | - Updated `project-documentation-standards` design/runtime to verify the same live workspace behavior | |
| | | - Added `patch/phase-linkage-hardening.patch.md` plus `phase/phase-005-01-*` and `phase/phase-005-02-*` to record the narrow rollout | |
| | | Summary: Completed a narrow follow-up that keeps phase and patch separate but now requires their relationship to be explicit in the live phase workspace when governed patch artifacts are active | |
| 6.8 | 2026-03-28 | **[Created startup artifact-initiation governance and synchronized the repository to artifact-first work startup](#version-68)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Created `design/artifact-initiation-control.design.md`, `artifact-initiation-control.md`, and `changelog/artifact-initiation-control.changelog.md` as a new first-class startup-governance owner chain | |
| | | - Updated `project-documentation-standards` design/runtime to v2.9 so meaningful governed work now resolves startup artifact posture before drift | |
| | | - Updated `phase-implementation` design/runtime to v2.6 so `/phase` is established early when startup governance already shows phased work is required | |
| | | - Updated `todo-standards` design/runtime to v2.3 and created `changelog/todo-standards.changelog.md` so TODO presence is resolved early while TODO content still syncs later | |
| | | - Updated `strict-file-hygiene` design/runtime/changelog to v1.2 so required governed startup artifacts are no longer blocked as junk docs | |
| | | - Opened `phase-004` from the start with `phase/phase-004-01-*` through `phase/phase-004-03-*` and updated `phase/SUMMARY.md` to track the rollout family | |
| | | - Updated `README.md`, `design/design.md`, `TODO.md`, and `phase/SUMMARY.md` so the new startup-governance model is visible across the active repository surfaces | |
| | | Summary: Completed the startup-governance rollout so design/changelog/TODO/phase/patch posture is now resolved before meaningful governed work drifts instead of being backfilled later | |
| 6.7 | 2026-03-28 | **[Corrected the repository-wide patch model to explicit before/after artifacts in `patch/` or at root](#version-67)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| | | - Updated `document-patch-control` design/runtime/changelog from v2.3 to v2.4 to explicitly define patch as a governed before/after artifact, remove generic `patch.md` allowance, and standardize active placement to `patch/<context>.patch.md` or root `<context>.patch.md` | |
| | | - Updated `project-documentation-standards` design/runtime/changelog from v2.7 to v2.8 so the repository role model now teaches the same corrected patch placement and patch meaning everywhere | |
| | | - Updated `phase-implementation` runtime/changelog to v2.5 and aligned `design/phase-implementation.design.md` to the same active patch-artifact boundary model while preserving the one-way synthesis boundary | |
| | | - Updated `tactical-strategic-programming` design/runtime/changelog from v1.0 to v1.1 so tactical artifact examples now point to the corrected patch model | |
| | | - Updated `README.md`, `design/design.md`, `phase-implementation-template.md`, `design/document-changelog-control.design.md`, and `design/unified-version-control-system.design.md` to remove active `patches/` teaching and align wording to the corrected patch concept | |
| | | - Moved the in-repo example patches into `patch/` and rewrote them as explicit before/after artifacts: `patch/consistency-rule-enhancement.patch.md` and `patch/legacy-rules-migration.patch.md` | |
| | | - Updated patch changelogs, TODO tracking, and parent-document references to match the moved patch paths and normalized patch examples | |
| | | Summary: Completed the patch-concept correction so the active RULES repository now teaches one deterministic patch model: self-identifying before/after artifacts in `patch/` or at repository root, never prose-only patch summaries | |
| 6.5 | 2026-03-27 | **[Created natural-professional-communication rule chain and synchronized communication-owner refinements](#version-65)** | a0fe4e7f-e9e7-41ac-a473-3fcdbbf39ba2 |
| | | - Created `design/natural-professional-communication.design.md`, `natural-professional-communication.md`, and `changelog/natural-professional-communication.changelog.md` as a new first-class communication-style doctrine chain | |
| | | - Created `phase/SUMMARY.md` and `phase/phase-001-*` to `phase/phase-004-*` execution artifacts for the RULES development rollout of the new chain and related refinement wave | |
| | | - Updated `accurate-communication` to v2.2, `explanation-quality` to v2.2, `answer-presentation` to v1.6, `authority-and-scope` to v1.4, and `anti-sycophancy` to v1.4 with calmer, more natural, non-robotic, non-character-driven professional communication guidance | |
| | | - Updated `design/design.md` and `README.md` from 30 to 31 active runtime rules, corrected the canonical install set from the stale 29-rule wording, and normalized lingering `phase-010-*` README references to `phase-001-*` | |
| | | - Updated `TODO.md` to record rollout completion and re-synchronized touched runtime rules into `~/.claude/rules/` with parity verification | |
| | | Summary: Added one explicit semantic authority for natural professional communication and aligned the wording, explanation, presentation, authority, and disagreement chains so the system now defaults to calmer, more human-readable, non-robotic professional communication | |
| 6.4 | 2026-03-17 | **[Changed default phase numbering to 001/002/003 across phase-implementation governance](#version-64)** | 9b6e3a46-d4f0-4968-9f5a-be083de4304c |
| | | - Updated `phase-implementation` design/runtime/changelog to v2.2 with zero-padded contiguous child-phase numbering (`001/002/003`) instead of sparse `010/020/030` | |
| | | - Updated `phase-implementation-template.md` examples and helper guidance to the new numbering scheme | |
| | | - Updated `design/design.md` and `README.md` wording to reflect the new default numbering policy | |
| | | - Updated `TODO.md` completion/history tracking for the phase-numbering patch wave and synced the installed runtime copy | |
| | | Summary: Refined the phase-planning model so default phase numbering is now human-readable and naturally sequential (`001/002/003`) rather than sparse by default | |
| 6.3 | 2026-03-17 | **[Created first-class tactical-strategic-programming rule chain and synchronized master governance](#version-63)** | 77d0802a-fd64-4023-a66d-88c165ccca12 |
| | | - Created `design/tactical-strategic-programming.design.md`, `tactical-strategic-programming.md`, and `changelog/tactical-strategic-programming.changelog.md` as a new first-class doctrine chain | |
| | | - Created `phase/SUMMARY.md` and `phase/phase-001-*` to `phase/phase-003-*` execution artifacts for the RULES development rollout of the new chain | |
| | | - Updated `design/design.md` and `README.md` from 29 to 30 active runtime rules and registered the new doctrine in the Quality & Governance model | |
| | | - Updated `TODO.md` to record rollout completion and installed the runtime rule into `~/.claude/rules/tactical-strategic-programming.md` | |
| | | Summary: Added one explicit semantic authority for tactical entry, strategic target, convergence path, and strategic closure so fast local execution can be governed without strategic drift | |

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
