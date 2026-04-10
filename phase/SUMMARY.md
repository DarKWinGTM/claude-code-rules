# RULES Phase Summary

> **Current Version:** 1.15
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.7
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb
> **Status:** Mixed historical review state
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This phase workspace records governed RULES rollout programs using the active deterministic phase identity model:
- major phases use `NNN`
- subphases use `NNN-NN`

The current workspace contains twenty-eight rollout families:
- major phase `001` = tactical-strategic-programming rollout
- major phase `002` = natural-professional-communication rollout
- major phase `003` = patch-model correction rollout
- major phase `004` = artifact-initiation-control rollout
- major phase `005` = explicit phase-to-patch linkage hardening rollout
- major phase `006` = external-verification-and-source-trust rollout
- major phase `007` = custom-agent-selection-priority rollout
- major phase `008` = portable-implementation-and-hardcoding-control rollout
- major phase `009` = continuation-priority and option-offering refinement rollout
- major phase `010` = install-doc portability and source-destination notation refinement rollout
- major phase `011` = recommended-option and why-this-first refinement rollout
- major phase `012` = variable, field, config, and internal-term explanation refinement rollout
- major phase `013` = goal-qualified proposal boundary refinement rollout
- major phase `014` = team-agent dedup and stale-presence refinement rollout
- major phase `015` = governing-basis clarification before deep branch analysis refinement rollout
- major phase `016` = compact and post-compact re-anchor refinement rollout
- major phase `017` = RULES plugin extension companion rollout
- major phase `018` = compact ephemeral handoff lifecycle refinement rollout
- major phase `019` = session-scoped compact carry-forward state refinement rollout
- major phase `020` = active review-trigger compact refinement rollout
- major phase `021` = reference-first compact review refinement rollout
- major phase `022` = direct human-readable wording refinement rollout
- major phase `023` = rules-first over memory and portable support artifact refinement rollout
- major phase `024` = purpose-first communication framing refinement rollout
- major phase `025` = compact markdown table default refinement rollout
- major phase `026` = memory-governance and session-boundary refinement rollout
- major phase `027` = task-list-first execution-tracking refinement rollout
- major phase `028` = plain aligned no-frame table-style refinement rollout

The goal of this summary is to index those rollout families without ambiguity, so the repository no longer relies on symbolic labels such as `P1/P2/P3/P4/P5` or flat child numbering that hides parent-child relationships.

---

## Source-Input Extraction Summary

| Major Phase | Phase | Phase File | Design Source | Patch Source | Derived Execution Work | Target Outcome |
|------------|-------|------------|---------------|--------------|------------------------|----------------|
| 001 | 001-01 | `phase/phase-001-01-create-tactical-strategic-rule.md` | `design/tactical-strategic-programming.design.md` | n/a | Create the first-class `tactical-strategic-programming` rule chain | First-class doctrine owner exists |
| 001 | 001-02 | `phase/phase-001-02-integrate-related-rules.md` | `design/tactical-strategic-programming.design.md` | n/a | Align master documentation and related owner references with the new doctrine | Repository-level governance reflects the new rule chain |
| 001 | 001-03 | `phase/phase-001-03-install-and-verify.md` | `design/tactical-strategic-programming.design.md` | n/a | Install the new runtime rule and verify source/install alignment | Installed runtime rule matches source |
| 002 | 002-01 | `phase/phase-002-01-create-natural-professional-rule.md` | `design/natural-professional-communication.design.md` | n/a | Create the first-class doctrine owner for natural professional communication | First-class communication-style owner exists |
| 002 | 002-02 | `phase/phase-002-02-refine-primary-communication-chains.md` | `design/natural-professional-communication.design.md` + existing communication-owner designs | n/a | Align wording, explanation, and presentation owners to the new doctrine | Primary communication chains implement the doctrine concretely |
| 002 | 002-03 | `phase/phase-002-03-tighten-default-mode-and-correction-boundaries.md` | `design/natural-professional-communication.design.md` + `authority-and-scope` + `anti-sycophancy` designs | n/a | Align default-mode and disagreement posture with the communication doctrine | Default register and correction posture are consistent |
| 002 | 002-04 | `phase/phase-002-04-sync-master-docs-install-and-verify.md` | runtime files + master docs | n/a | Sync master governance docs, install runtime copies, and verify parity | Repo and installed runtime state are synchronized |
| 003 | 003-01 | `phase/phase-003-01-define-patch-model.md` | `design/document-patch-control.design.md` + `design/project-documentation-standards.design.md` | `patch/consistency-rule-enhancement.patch.md` + `patch/legacy-rules-migration.patch.md` | Define the corrected patch concept and normalize in-repo patch examples | Active patch model is explicit and deterministic |
| 003 | 003-02 | `phase/phase-003-02-realign-dependent-docs.md` | `design/document-patch-control.design.md` + `design/project-documentation-standards.design.md` + `design/phase-implementation.design.md` | n/a | Realign dependent governance docs to the corrected patch model | Active repo docs no longer contradict the patch model |
| 003 | 003-03 | `phase/phase-003-03-sync-history-and-verify.md` | `design/document-patch-control.design.md` + `design/project-documentation-standards.design.md` + `design/design.md` | `patch/consistency-rule-enhancement.patch.md` + `patch/legacy-rules-migration.patch.md` | Sync changelog/TODO history and verify remaining old patch references are historical only | Active state and history are coherent |
| 004 | 004-01 | `phase/phase-004-01-create-artifact-initiation-rule.md` | `design/project-documentation-standards.design.md` + `design/phase-implementation.design.md` + `design/todo-standards.design.md` | n/a | Create the first-class `artifact-initiation-control` rule chain | Startup artifact posture has one semantic owner |
| 004 | 004-02 | `phase/phase-004-02-realign-startup-governance.md` | `design/project-documentation-standards.design.md` + `design/phase-implementation.design.md` + `design/todo-standards.design.md` + `design/strict-file-hygiene.design.md` | n/a | Realign startup-governance owner chains to the new rule | Existing owners stop weakening startup artifact-first behavior |
| 004 | 004-03 | `phase/phase-004-03-sync-master-docs-and-history.md` | `design/design.md` + `design/project-documentation-standards.design.md` | n/a | Sync master docs, TODO, changelog, and phase summary for the new startup-governance wave | Repo-level governance reflects the new startup rule |
| 005 | 005-01 | `phase/phase-005-01-harden-phase-patch-linkage.md` | `design/phase-implementation.design.md` + `design/project-documentation-standards.design.md` | `patch/phase-linkage-hardening.patch.md` | Harden the explicit phase-to-patch linkage rule in the live phase workspace | Phased work with governed patch artifacts must declare that linkage explicitly |
| 005 | 005-02 | `phase/phase-005-02-sync-master-docs-and-history.md` | `design/design.md` + `design/project-documentation-standards.design.md` | `patch/phase-linkage-hardening.patch.md` | Sync master docs, TODO, changelog, and phase summary for the narrow linkage-hardening wave | Repo-level governance reflects the explicit linkage refinement |
| 006 | 006-01 | `phase/phase-006-01-create-external-verification-rule.md` | `design/external-verification-and-source-trust.design.md` | `patch/external-verification-and-source-trust.patch.md` | Create the first-class external-verification-and-source-trust rule chain | One semantic owner exists for proactive web verification and source trust |
| 006 | 006-02 | `phase/phase-006-02-integrate-source-trust-governance.md` | `design/external-verification-and-source-trust.design.md` + `design/design.md` + adjacent owner designs | `patch/external-verification-and-source-trust.patch.md` | Sync master docs, TODO, changelog, and phase summary for the new source-trust wave | Repo-level governance reflects the new external-verification owner |
| 007 | 007-01 | `phase/phase-007-01-create-custom-agent-selection-rule.md` | `design/custom-agent-selection-priority.design.md` | `patch/custom-agent-selection-priority.patch.md` | Create the first-class custom-agent-selection-priority rule chain | One semantic owner exists for custom user agent selection preference |
| 007 | 007-02 | `phase/phase-007-02-integrate-agent-selection-governance.md` | `design/custom-agent-selection-priority.design.md` + `design/design.md` + adjacent owner designs | `patch/custom-agent-selection-priority.patch.md` | Sync master docs, TODO, changelog, and phase summary for the new custom-agent selection wave | Repo-level governance reflects the new agent-selection owner |
| 008 | 008-01 | `phase/phase-008-01-create-portable-implementation-rule.md` | `design/portable-implementation-and-hardcoding-control.design.md` | `patch/portable-implementation-and-hardcoding-control.patch.md` | Create the first-class portable-implementation-and-hardcoding-control rule chain | One semantic owner exists for portable defaults and anti-hardcoding discipline |
| 008 | 008-02 | `phase/phase-008-02-integrate-hardcoding-governance.md` | `design/portable-implementation-and-hardcoding-control.design.md` + `design/design.md` | `patch/portable-implementation-and-hardcoding-control.patch.md` | Sync master docs, TODO, changelog, and phase summary for the new hardcoding-control wave | Repo-level governance reflects the new portable-implementation owner |
| 008 | 008-03 | `phase/phase-008-03-deepen-portability-integration.md` | `design/portable-implementation-and-hardcoding-control.design.md` + touched adjacent designs | `patch/portable-implementation-and-hardcoding-control.patch.md` | Deepen the adjacent-chain integration slice so portability ownership affects strategy, consistency, and presentation behavior more concretely | Portability owner becomes more operationally real across adjacent chains |
| 009 | 009-01 | `phase/phase-009-01-audit-continuation-vs-interruption.md` | `design/accurate-communication.design.md` + `design/answer-presentation.design.md` + `design/explanation-quality.design.md` + `design/authority-and-scope.design.md` | `patch/continuation-priority-and-option-offering.patch.md` | Audit the current option-offering and next-stage drift across communication/presentation/explanation owners | Primary owner and overlap set are explicit |
| 009 | 009-02 | `phase/phase-009-02-implement-continuation-priority.md` | `design/accurate-communication.design.md` + touched adjacent designs | `patch/continuation-priority-and-option-offering.patch.md` | Implement continuation-first behavior so active work proceeds by default and options appear only when genuinely necessary | Communication-layer behavior prioritizes execution over interruption |
| 010 | 010-01 | `phase/phase-010-01-refine-install-doc-portability-owners.md` | `design/portable-implementation-and-hardcoding-control.design.md` + `design/project-documentation-standards.design.md` + `design/document-consistency.design.md` | `patch/install-doc-portability-and-source-destination-notation.patch.md` | Refine the owner and adjacent enforcement chains so public install docs stay portable by default | Install-doc portability and source-destination notation have explicit governance owners |
| 010 | 010-02 | `phase/phase-010-02-sync-master-governance-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/install-doc-portability-and-source-destination-notation.patch.md` | Sync master docs, phase indexing, TODO/changelog history, and installed runtime copies for the new refinement wave | Repo-level governance and installed runtime state reflect the install-doc portability refinement |
| 011 | 011-01 | `phase/phase-011-01-refine-recommended-option-wording.md` | `design/accurate-communication.design.md` + `design/explanation-quality.design.md` + `design/answer-presentation.design.md` | `patch/recommended-option-and-why-this-first.patch.md` | Refine multi-option next-step wording so the preferred path is named first, explained briefly, and does not hide real alternatives | Recommendation-heavy next-step guidance becomes easier to act on without collapsing genuine multi-path states |
| 011 | 011-02 | `phase/phase-011-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/recommended-option-and-why-this-first.patch.md` | Sync master docs, phase indexing, TODO/changelog history, and installed runtime copies for the recommendation-format refinement | Repo-level governance and installed runtime state reflect the recommendation-format refinement |
| 012 | 012-01 | `phase/phase-012-01-refine-variable-field-config-and-term-explanations.md` | `design/accurate-communication.design.md` + `design/explanation-quality.design.md` + `design/answer-presentation.design.md` | `patch/variable-field-config-and-term-explanation.patch.md` | Refine identifier-heavy explanations so variables, fields, config keys, enum-like values, and internal labels are unpacked before the deeper reasoning depends on them | Identifier-heavy technical explanations become easier to follow without creating a new first-class doctrine chain |
| 012 | 012-02 | `phase/phase-012-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/variable-field-config-and-term-explanation.patch.md` | Sync master docs, phase indexing, TODO/changelog history, and installed runtime copies for the identifier-explanation refinement | Repo-level governance and installed runtime state reflect the identifier-explanation refinement |
| 013 | 013-01 | `phase/phase-013-01-refine-goal-qualified-proposals.md` | `design/accurate-communication.design.md` + `design/authority-and-scope.design.md` + `design/explanation-quality.design.md` + `design/answer-presentation.design.md` | `patch/goal-qualified-proposal-boundary.patch.md` | Refine future-work proposal behavior so ideas stay advisory, goal-qualified, and visibly separate from active execution | Future-wave concepts become easier to evaluate without sounding like queued continuation |
| 013 | 013-02 | `phase/phase-013-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/goal-qualified-proposal-boundary.patch.md` | Sync master docs, phase indexing, TODO/changelog history, and installed runtime copies for the proposal-boundary refinement | Repo-level governance and installed runtime state reflect the proposal-boundary refinement |
| 014 | 014-01 | `phase/phase-014-01-refine-team-agent-dedup-boundaries.md` | `design/custom-agent-selection-priority.design.md` + `design/authority-and-scope.design.md` + `design/operational-failure-handling.design.md` + `design/accurate-communication.design.md` | `patch/team-agent-dedup-and-stale-presence-boundary.patch.md` | Refine team-agent behavior so matching teammates are reused before spawn and duplicate-looking team state is inspected before respawn | Team-agent duplication and stale-presence handling become governed instead of ad hoc |
| 014 | 014-02 | `phase/phase-014-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/team-agent-dedup-and-stale-presence-boundary.patch.md` | Sync master docs, phase indexing, TODO/changelog history, and installed runtime copies for the team-agent dedup/stale-presence refinement | Repo-level governance and installed runtime state reflect the team-agent dedup/stale-presence refinement |
| 015 | 015-01 | `phase/phase-015-01-refine-governing-basis-clarification.md` | `design/accurate-communication.design.md` + `design/authority-and-scope.design.md` + `design/evidence-grounded-burden-of-proof.design.md` + `design/explanation-quality.design.md` + `design/answer-presentation.design.md` | `patch/governing-basis-clarification-before-branching.patch.md` | Refine ambiguity handling so materially different governing bases are clarified first through a compact structured question instead of unnecessary deep branch analysis | Governing-basis ambiguity becomes ask-first rather than branch-first |
| 015 | 015-02 | `phase/phase-015-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/governing-basis-clarification-before-branching.patch.md` | Sync master docs, phase indexing, TODO/changelog history, and installed runtime copies for the governing-basis clarification refinement | Repo-level governance and installed runtime state reflect the governing-basis clarification refinement |
| 016 | 016-01 | `phase/phase-016-01-refine-compact-and-post-compact-governance.md` | `design/accurate-communication.design.md` + `design/authority-and-scope.design.md` + `design/evidence-grounded-burden-of-proof.design.md` + `design/explanation-quality.design.md` + `design/answer-presentation.design.md` | `patch/compact-post-compact-governance-refinement.patch.md` | Refine compacted-session continuation so the assistant re-anchors to the active objective and does not silently treat compressed-away detail as exact verified truth | Post-compact continuation becomes re-anchor-first rather than stale-replay-first |
| 016 | 016-02 | `phase/phase-016-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/compact-post-compact-governance-refinement.patch.md` | Sync master docs, phase indexing, TODO/changelog history, and installed runtime copies for the compact/post-compact refinement | Repo-level governance and installed runtime state reflect the compact/post-compact refinement |
| 017 | 017-01 | `phase/phase-017-01-create-rules-plugin-extension-area.md` | `design/rules-plugin-extension.design.md` + `design/project-documentation-standards.design.md` | `patch/rules-plugin-extension-companion.patch.md` | Create the optional `plugin/` companion area for hook-based compact handling while keeping root RULES as the only semantic authority | A clean optional plugin companion exists without duplicate governance drift |
| 017 | 017-02 | `phase/phase-017-02-sync-root-docs-and-verify-plugin-companion.md` | `design/design.md` + `design/project-documentation-standards.design.md` + `design/rules-plugin-extension.design.md` | `patch/rules-plugin-extension-companion.patch.md` | Sync root docs and verify that the plugin companion remains support/extension-only | Root governance and plugin package boundaries are aligned and reviewable |
| 018 | 018-01 | `phase/phase-018-01-replace-latest-witness-model-with-ephemeral-handoff.md` | `design/rules-plugin-extension.design.md` | `patch/compact-ephemeral-handoff-lifecycle-refinement.patch.md` | Replace the plugin’s latest-only compact witness model with a one-shot ephemeral handoff lifecycle | The optional plugin companion behaves like a short-lived handoff cache instead of a witness store |
| 018 | 018-02 | `phase/phase-018-02-sync-plugin-docs-and-verify-compact-handoff-lifecycle.md` | `design/design.md` + `design/rules-plugin-extension.design.md` | `patch/compact-ephemeral-handoff-lifecycle-refinement.patch.md` | Sync package/root docs and verify the new compact handoff lifecycle with real runtime checks | Root governance, package docs, and runtime verification align on the ephemeral handoff model |
| 019 | 019-01 | `phase/phase-019-01-replace-single-slot-compact-state-with-session-scoped-layout.md` | `design/rules-plugin-extension.design.md` | `patch/compact-session-scoped-carry-forward-state-refinement.patch.md` | Replace singleton compact state with a small index and per-session carry-forward directories | Compact runtime state becomes session-scoped instead of singleton-scoped |
| 019 | 019-02 | `phase/phase-019-02-sync-docs-and-verify-session-scoped-compact-carry-forward.md` | `design/design.md` + `design/rules-plugin-extension.design.md` | `patch/compact-session-scoped-carry-forward-state-refinement.patch.md` | Sync docs and verify session-scoped compact carry-forward behavior | Root governance, docs, and runtime verification align on the session-scoped model |
| 020 | 020-01 | `phase/phase-020-01-tighten-active-review-trigger.md` | `design/rules-plugin-extension.design.md` | `patch/compact-active-review-trigger-and-memsearch-assist-refinement.patch.md` | Turn SessionStart into an active review trigger that names exact-session review files before continuation | Compact resume becomes explicitly review-oriented instead of passive carry-forward-only |
| 020 | 020-02 | `phase/phase-020-02-add-optional-memsearch-assist-boundary.md` | `design/rules-plugin-extension.design.md` | `patch/compact-active-review-trigger-and-memsearch-assist-refinement.patch.md` | Record memsearch as a later assist-layer boundary while keeping the current runtime local-review-first | Active runtime behavior stays local-review-first and memsearch remains deferred |
| 020 | 020-03 | `phase/phase-020-03-sync-docs-and-verify-active-review-behavior.md` | `design/design.md` + `design/rules-plugin-extension.design.md` | `patch/compact-active-review-trigger-and-memsearch-assist-refinement.patch.md` | Sync docs/versions and verify the new active review-trigger behavior | Root governance, docs, and runtime verification align on the Wave 020 review-trigger refinement |
| 021 | 021-01 | `phase/phase-021-01-tighten-systemmessage-review-required.md` | `design/rules-plugin-extension.design.md` | `patch/compact-reference-first-review-trigger-refinement.patch.md` | Make the visible compact navigator line explicitly say review is required before continuation | User-visible compact resume becomes clearly review-required instead of path-only |
| 021 | 021-02 | `phase/phase-021-02-tighten-additionalcontext-reference-first.md` | `design/rules-plugin-extension.design.md` | `patch/compact-reference-first-review-trigger-refinement.patch.md` | Reduce additionalContext to instruction + locator + bounded status only | Compact resume stays reference-first instead of becoming a hidden context-restore channel |
| 021 | 021-03 | `phase/phase-021-03-add-bounded-directive-proof-and-sync.md` | `design/design.md` + `design/rules-plugin-extension.design.md` | `patch/compact-reference-first-review-trigger-refinement.patch.md` | Add bounded directive proof and sync docs/version surfaces | Root governance, docs, and runtime verification align on the Wave 021 reference-first refinement |
| 022 | 022-01 | `phase/phase-022-01-refine-direct-human-readable-wording.md` | `design/accurate-communication.design.md` + `design/explanation-quality.design.md` + `design/natural-professional-communication.design.md` + `design/answer-presentation.design.md` | `patch/direct-human-readable-wording-over-metaphor-heavy-shorthand.patch.md` | Refine the communication-owner set so direct human-readable action/result wording is preferred over metaphor-heavy internal shorthand | Metaphor-heavy internal shorthand is no longer treated like a good default explanation style when a direct practical statement would be clearer |
| 022 | 022-02 | `phase/phase-022-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/direct-human-readable-wording-over-metaphor-heavy-shorthand.patch.md` | Sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the new refinement wave | Repo-level governance and installed runtime state reflect the direct human-readable wording refinement |
| 023 | 023-01 | `phase/phase-023-01-rules-first-over-memory-boundary.md` | `design/authority-and-scope.design.md` + `design/portable-implementation-and-hardcoding-control.design.md` + `design/project-documentation-standards.design.md` + `design/document-consistency.design.md` | `patch/rules-first-over-memory-and-portable-support-artifacts.patch.md` | Refine authority and portability owners so user-declared RULES-first issues are fixed in RULES rather than memory and reusable support/package source artifacts stay portable by default | Memory no longer acts as the substitute remedy for a user-declared RULES-first issue, and support/package source artifacts are explicitly governed as portable-by-default source content |
| 023 | 023-02 | `phase/phase-023-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/rules-first-over-memory-and-portable-support-artifacts.patch.md` | Sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the new refinement wave | Repo-level governance and installed runtime state reflect the rules-first-over-memory and portable-support-artifact refinement |
| 024 | 024-01 | `phase/phase-024-01-refine-purpose-first-communication.md` | `design/accurate-communication.design.md` + `design/explanation-quality.design.md` + `design/answer-presentation.design.md` + `design/natural-professional-communication.design.md` | `patch/purpose-first-communication-framing.patch.md` | Refine the communication-owner set so diagnosis, test, recommendation, proposal, and implementation-update answers state what they are doing before the supporting detail expands | Operational answers expose their purpose earlier instead of making the reader infer it from later detail |
| 024 | 024-02 | `phase/phase-024-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/purpose-first-communication-framing.patch.md` | Sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the new refinement wave | Repo-level governance and installed runtime state reflect the purpose-first communication refinement |
| 025 | 025-01 | `phase/phase-025-01-refine-compact-table-defaults.md` | `design/answer-presentation.design.md` + `design/explanation-quality.design.md` | `patch/compact-markdown-table-default-and-minimal-table-usage.patch.md` | Refine the presentation/explanation owner set so compact markdown tables become the default table form when useful and list-first alternatives stay explicit | Ordinary answer formatting becomes lighter, less decorative, and more consistent across table/list choices |
| 025 | 025-02 | `phase/phase-025-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/compact-markdown-table-default-and-minimal-table-usage.patch.md` | Sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the new refinement wave | Repo-level governance and installed runtime state reflect the compact-table / list-first refinement |
| 026 | 026-01 | `phase/phase-026-01-create-memory-governance-rule-chain.md` | `design/memory-governance-and-session-boundary.design.md` | `patch/memory-governance-and-session-boundary.patch.md` | Create the first-class rule chain that owns memory governance and session-boundary behavior before live-memory migration | One durable owner exists for memory role boundary, root `MEMORY.md`, path scope, session provenance, and archive semantics |
| 026 | 026-02 | `phase/phase-026-02-integrate-memory-governance-companions.md` | `design/memory-governance-and-session-boundary.design.md` + touched adjacent designs | `patch/memory-governance-and-session-boundary.patch.md` | Integrate authority, wording, burden-of-proof, and presentation owners narrowly with the new memory-governance chain | Adjacent owners acknowledge the new memory contract without duplicating ownership |
| 026 | 026-03 | `phase/phase-026-03-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/memory-governance-and-session-boundary.patch.md` | Sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the new governance wave | Repo-level governance and installed runtime state reflect the memory-governance refinement |
| 026 | 026-04 | `phase/phase-026-04-run-postflight-memory-governance-audit.md` | `design/memory-governance-and-session-boundary.design.md` + touched adjacent designs + `design/design.md` | `patch/memory-governance-and-session-boundary.patch.md` | Run the final consistency and parity sweep so the wave remains governance-only and does not over-claim live-memory migration | Wave `026` completes with coherent semantics, explicit later migration boundary, and verified source/install parity |
| 027 | 027-01 | `phase/phase-027-01-refine-task-list-first-execution-tracking.md` | `design/todo-standards.design.md` + `design/artifact-initiation-control.design.md` + `design/project-documentation-standards.design.md` | `patch/task-list-first-execution-tracking.patch.md` | Refine the owner set so the built-in task list becomes the live execution surface for non-trivial active work while `TODO.md` remains the durable tracking artifact | Execution tracking becomes more visible during active work without creating a new rule chain |
| 027 | 027-02 | `phase/phase-027-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/task-list-first-execution-tracking.patch.md` | Sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the task-list-first refinement | Repo-level governance and installed runtime state reflect the task-list-first refinement |
| 028 | 028-01 | `phase/phase-028-01-refine-plain-aligned-table-style.md` | `design/answer-presentation.design.md` + `design/explanation-quality.design.md` | `patch/plain-aligned-no-frame-table-style-refinement.patch.md` | Refine the owner set so ordinary answer tables use the selected light plain aligned no-frame form while table usage remains available when genuinely useful | Table style becomes correct without turning the wave into a reduce-table-frequency doctrine |
| 028 | 028-02 | `phase/phase-028-02-sync-master-docs-and-runtime-install.md` | `design/design.md` + touched adjacent designs | `patch/plain-aligned-no-frame-table-style-refinement.patch.md` | Sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the table-style refinement | Repo-level governance and installed runtime state reflect the selected plain aligned no-frame table style |

---

## Overview Flow

Need deterministic governed rollout identities across RULES phase artifacts
  → 001-01: create tactical-strategic doctrine owner
  → 001-02: align master governance docs for that doctrine
  → 001-03: install and verify runtime parity
  → 002-01: create natural-professional communication doctrine owner
  → 002-02: align wording, explanation, and presentation owners
  → 002-03: tighten default-mode and correction boundaries
  → 002-04: sync master docs, install touched runtime files, and verify parity
  → 003-01: define the corrected patch model and normalize patch examples
  → 003-02: realign dependent governance docs to the corrected patch contract
  → 003-03: sync history layers and verify legacy patch references are historical only
  → 004-01: create artifact-initiation startup owner
  → 004-02: realign startup-governance owner chains
  → 004-03: sync master docs and history for the startup-governance wave
  → 005-01: harden explicit phase-to-patch linkage in the live phase workspace
  → 005-02: sync master docs and history for the linkage-hardening wave
  → 006-01: create external-verification-and-source-trust rule chain
  → 006-02: sync master docs and history for the source-trust wave
  → 007-01: create custom-agent-selection-priority rule chain
  → 007-02: sync master docs and history for the agent-selection wave
  → 008-01: create portable-implementation-and-hardcoding-control rule chain
  → 008-02: sync master docs and history for the hardcoding-control wave
  → 008-03: deepen adjacent-chain integration for the hardcoding-control wave
  → 009-01: audit continuation-vs-interruption behavior across communication/presentation/explanation owners
  → 009-02: implement continuation-first behavior and narrow unnecessary option prompting
  → 010-01: refine install-doc portability owners and source-destination notation enforcement
  → 010-02: sync master governance surfaces and installed runtime copies for the install-doc portability wave
  → 011-01: refine recommended-option wording so multi-path next steps name the preferred path first without collapsing real alternatives
  → 011-02: sync master governance surfaces and installed runtime copies for the recommendation-format wave
  → 012-01: refine identifier-heavy explanations so variables, fields, config keys, enum-like values, and internal labels are explained before deeper reasoning depends on them
  → 012-02: sync master governance surfaces and installed runtime copies for the identifier-explanation wave
  → 013-01: refine future-work proposals so they stay advisory, goal-qualified, and visibly separate from active execution
  → 013-02: sync master governance surfaces and installed runtime copies for the proposal-boundary wave
  → 014-01: refine team-agent behavior so matching teammates are reused before spawn and duplicate-looking team state is inspected before respawn
  → 014-02: sync master governance surfaces and installed runtime copies for the team-agent dedup/stale-presence wave
  → 015-01: refine ambiguity handling so materially different governing bases are clarified first instead of explored through deep branch analysis
  → 015-02: sync master governance surfaces and installed runtime copies for the governing-basis clarification wave
  → 016-01: refine compacted-session continuation so the assistant re-anchors to the active objective before resuming
  → 016-02: sync master governance surfaces and installed runtime copies for the compact/post-compact refinement wave
  → 017-01: create the optional RULES plugin companion area for hook-based compact handling
  → 017-02: sync root governance surfaces and verify the plugin companion stays support-only
  → 018-01: replace the plugin’s latest-only compact witness model with one ephemeral handoff lifecycle
  → 018-02: sync package/root docs and verify create → consume/delete → prune behavior for the new compact handoff model
  → 019-01: replace singleton compact files with a small live index and per-session carry-forward directories
  → 019-02: sync docs and verify session-scoped carry-forward injection plus fail-closed ambiguous routing
  → 020-01: turn compact SessionStart into an active review trigger that names the exact-session review files before continuation
  → 020-02: keep memsearch as a later assist boundary while the active runtime remains local-review-first
  → 020-03: sync docs and verify the active review-trigger behavior across source, bridge, and master governance surfaces
  → 021-01: make the visible compact navigator line explicitly say review is required before continuation
  → 021-02: reduce additionalContext to instruction + locator + bounded status only
  → 021-03: add bounded directive proof and sync docs/version surfaces to the reference-first compact review model
  → 022-01: refine the communication-owner set so direct human-readable action/result wording is preferred over metaphor-heavy internal shorthand
  → 022-02: sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the direct human-readable wording refinement
  → 023-01: refine authority and portability owners so user-declared RULES-first issues are fixed in RULES rather than memory and support/package source artifacts remain portable by default
  → 023-02: sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the rules-first-over-memory and portable-support-artifact refinement
  → 024-01: refine the communication-owner set so diagnosis, test, recommendation, proposal, and implementation-update answers state what they are doing before the supporting detail expands
  → 024-02: sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the purpose-first communication refinement
  → 025-01: refine the presentation/explanation owner set so compact markdown tables become the default table form when useful and list-first alternatives stay explicit
  → 025-02: sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the compact-table / list-first refinement
  → 026-01: create the first-class memory-governance owner so memory role boundary, root `MEMORY.md`, path scope, session provenance, and archive lifecycle are defined before live-memory migration
  → 026-02: integrate authority, communication, burden-of-proof, and presentation owners narrowly with the new memory-governance chain
  → 026-03: sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the memory-governance refinement
  → 026-04: run the final memory-governance audit so the wave stays governance-only and does not over-claim live-memory migration
  → 027-01: refine tracking/startup/documentation owners so the built-in task list becomes the live execution surface for non-trivial active work while `TODO.md` remains the durable tracking artifact
  → 027-02: sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the task-list-first refinement
  → 028-01: refine the table-style owners so ordinary answer tables use the selected light plain aligned no-frame form while table usage remains available when genuinely useful
  → 028-02: sync master docs, TODO/changelog history, phase indexing, and installed runtime copies for the table-style refinement
  → active RULES workspace uses explicit major/subphase identities, one deterministic patch model, artifact-first startup governance, explicit phase-to-patch linkage when patch is in scope, a first-class external source-trust verification owner, a first-class custom-agent selection owner, a first-class portable-implementation owner, continuation-first communication behavior, an explicit install-doc portability model that keeps source-side and destination/runtime path roles distinct, a clearer recommendation-plus-reason format when multiple next steps are shown, a clearer identifier-explanation model for variable-heavy technical answers, a goal-qualified proposal model for future-wave suggestions, explicit reuse-before-spawn / inspect-before-respawn handling for duplicate-looking team-agent state, explicit post-compact re-anchor behavior after context compression, a direct human-readable wording preference that rejects metaphor-heavy internal shorthand as a default explanation style, an explicit RULES-first-over-memory authority boundary for user-declared governance issues, portable-by-default support/package source artifact handling, a purpose-first communication model that exposes what diagnosis/test/recommendation/proposal/update answers are doing earlier, and an optional plugin companion area that reinforces compact handling without weakening root rules authority while now using session-scoped compact carry-forward state, an active review-trigger SessionStart model, and a tighter reference-first review contract instead of passive carry-forward-only behavior or hidden context replay

---

## Review Summary

| Major Phase | Phase | Phase File | Sign-Off Status | Reviewer Severity | Reviewer Disposition | Blocker / Follow-Up State |
|------------|-------|------------|-----------------|-------------------|----------------------|---------------------------|
| 001 | 001-01 | `phase/phase-001-01-create-tactical-strategic-rule.md` | Approved | None | Approved As-Is | none |
| 001 | 001-02 | `phase/phase-001-02-integrate-related-rules.md` | Approved | None | Approved As-Is | none |
| 001 | 001-03 | `phase/phase-001-03-install-and-verify.md` | Approved | None | Approved As-Is | none |
| 002 | 002-01 | `phase/phase-002-01-create-natural-professional-rule.md` | Approved | None | Approved As-Is | none |
| 002 | 002-02 | `phase/phase-002-02-refine-primary-communication-chains.md` | Approved | None | Approved As-Is | none |
| 002 | 002-03 | `phase/phase-002-03-tighten-default-mode-and-correction-boundaries.md` | Approved | None | Approved As-Is | none |
| 002 | 002-04 | `phase/phase-002-04-sync-master-docs-install-and-verify.md` | Approved | None | Approved As-Is | none |
| 003 | 003-01 | `phase/phase-003-01-define-patch-model.md` | Approved | None | Approved As-Is | none |
| 003 | 003-02 | `phase/phase-003-02-realign-dependent-docs.md` | Approved | None | Approved As-Is | none |
| 003 | 003-03 | `phase/phase-003-03-sync-history-and-verify.md` | Approved | None | Approved As-Is | none |
| 004 | 004-01 | `phase/phase-004-01-create-artifact-initiation-rule.md` | Approved | None | Approved As-Is | none |
| 004 | 004-02 | `phase/phase-004-02-realign-startup-governance.md` | Approved | None | Approved As-Is | none |
| 004 | 004-03 | `phase/phase-004-03-sync-master-docs-and-history.md` | Approved | None | Approved As-Is | none |
| 005 | 005-01 | `phase/phase-005-01-harden-phase-patch-linkage.md` | Implemented - Pending Review | Review Pending | Awaiting Review | narrow linkage refinement applied |
| 005 | 005-02 | `phase/phase-005-02-sync-master-docs-and-history.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master docs/history synchronized |
| 006 | 006-01 | `phase/phase-006-01-create-external-verification-rule.md` | Implemented - Pending Review | Review Pending | Awaiting Review | new external verification owner created |
| 006 | 006-02 | `phase/phase-006-02-integrate-source-trust-governance.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master source-trust integration completed |
| 007 | 007-01 | `phase/phase-007-01-create-custom-agent-selection-rule.md` | Implemented - Pending Review | Review Pending | Awaiting Review | new custom-agent selection owner created |
| 007 | 007-02 | `phase/phase-007-02-integrate-agent-selection-governance.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master agent-selection integration completed |
| 008 | 008-01 | `phase/phase-008-01-create-portable-implementation-rule.md` | Implemented - Pending Review | Review Pending | Awaiting Review | new portable-implementation owner created |
| 008 | 008-02 | `phase/phase-008-02-integrate-hardcoding-governance.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master integration wave underway |
| 008 | 008-03 | `phase/phase-008-03-deepen-portability-integration.md` | Implemented - Pending Review | Review Pending | Awaiting Review | deeper adjacent integration wave underway |
| 009 | 009-01 | `phase/phase-009-01-audit-continuation-vs-interruption.md` | Completed | None | Approved As-Is | owner/overlap diagnosis completed |
| 009 | 009-02 | `phase/phase-009-02-implement-continuation-priority.md` | Implemented - Pending Review | Review Pending | Awaiting Review | continuation-first refinement applied across touched owner chains |
| 010 | 010-01 | `phase/phase-010-01-refine-install-doc-portability-owners.md` | Implemented - Pending Review | Review Pending | Awaiting Review | owner/enforcement refinement applied for install-doc portability |
| 010 | 010-02 | `phase/phase-010-02-sync-master-governance-and-runtime-install.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master docs and installed runtime copies synchronized |
| 011 | 011-01 | `phase/phase-011-01-refine-recommended-option-wording.md` | Implemented - Pending Review | Review Pending | Awaiting Review | recommendation-plus-reason wording applied across touched owner chains |
| 011 | 011-02 | `phase/phase-011-02-sync-master-docs-and-runtime-install.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master docs and runtime-install sync completed for the recommendation-format refinement |
| 012 | 012-01 | `phase/phase-012-01-refine-variable-field-config-and-term-explanations.md` | Implemented - Pending Review | Review Pending | Awaiting Review | identifier-explanation refinement applied across the communication-owner trio |
| 012 | 012-02 | `phase/phase-012-02-sync-master-docs-and-runtime-install.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master docs and runtime-install sync completed for the identifier-explanation refinement |
| 013 | 013-01 | `phase/phase-013-01-refine-goal-qualified-proposals.md` | Implemented - Pending Review | Review Pending | Awaiting Review | goal-qualified proposal refinement applied across the communication-owner set |
| 013 | 013-02 | `phase/phase-013-02-sync-master-docs-and-runtime-install.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master docs and runtime-install sync completed for the proposal-boundary refinement |
| 014 | 014-01 | `phase/phase-014-01-refine-team-agent-dedup-boundaries.md` | Implemented - Pending Review | Review Pending | Awaiting Review | team-agent dedup refinement applied across selection, authority, operations, and reporting owners |
| 014 | 014-02 | `phase/phase-014-02-sync-master-docs-and-runtime-install.md` | Implemented - Pending Review | Review Pending | Awaiting Review | master docs and runtime-install sync completed for the team-agent dedup/stale-presence refinement |
| 015 | 015-01 | `phase/phase-015-01-refine-governing-basis-clarification.md` | Completed | None | Approved As-Is | governing-basis clarification refinement applied across wording, authority, burden-of-proof, explanation, and presentation owners |
| 015 | 015-02 | `phase/phase-015-02-sync-master-docs-and-runtime-install.md` | Completed | None | Approved As-Is | master docs and runtime-install sync completed for the governing-basis clarification refinement |
| 016 | 016-01 | `phase/phase-016-01-refine-compact-and-post-compact-governance.md` | Completed | None | Approved As-Is | compact/post-compact refinement applied across wording, authority, burden-of-proof, explanation, and presentation owners |
| 016 | 016-02 | `phase/phase-016-02-sync-master-docs-and-runtime-install.md` | Completed | None | Approved As-Is | master docs and runtime-install sync completed for the compact/post-compact refinement |
| 017 | 017-01 | `phase/phase-017-01-create-rules-plugin-extension-area.md` | Completed | None | Approved As-Is | optional plugin companion created under `plugin/` without duplicate governance drift |
| 017 | 017-02 | `phase/phase-017-02-sync-root-docs-and-verify-plugin-companion.md` | Completed | None | Approved As-Is | root docs and plugin-package boundaries synchronized and verified |
| 018 | 018-01 | `phase/phase-018-01-replace-latest-witness-model-with-ephemeral-handoff.md` | Completed | None | Approved As-Is | latest-witness compact storage replaced with one ephemeral handoff lifecycle |
| 018 | 018-02 | `phase/phase-018-02-sync-plugin-docs-and-verify-compact-handoff-lifecycle.md` | Completed | None | Approved As-Is | package/root docs synchronized and runtime verification confirmed create → consume/delete → prune behavior |
| 019 | 019-01 | `phase/phase-019-01-replace-single-slot-compact-state-with-session-scoped-layout.md` | Completed | None | Approved As-Is | singleton compact files replaced with session-scoped state directories and live index |
| 019 | 019-02 | `phase/phase-019-02-sync-docs-and-verify-session-scoped-compact-carry-forward.md` | Completed | None | Approved As-Is | docs synchronized and session-scoped verification confirmed create → consume/proof → fail-closed ambiguity behavior |
| 020 | 020-01 | `phase/phase-020-01-tighten-active-review-trigger.md` | Completed | None | Approved As-Is | active review-trigger refinement applied and exact-session review pointers are now part of compact resume behavior |
| 020 | 020-02 | `phase/phase-020-02-add-optional-memsearch-assist-boundary.md` | Completed | None | Approved As-Is | memsearch remains deferred while local-review-first behavior stays active |
| 020 | 020-03 | `phase/phase-020-03-sync-docs-and-verify-active-review-behavior.md` | Completed | None | Approved As-Is | root docs synchronized and active review-trigger behavior verified |
| 021 | 021-01 | `phase/phase-021-01-tighten-systemmessage-review-required.md` | Completed | None | Approved As-Is | user-visible compact resume now explicitly says review is required before continuation |
| 021 | 021-02 | `phase/phase-021-02-tighten-additionalcontext-reference-first.md` | Completed | None | Approved As-Is | compact additionalContext now stays reference-first instead of replaying old context |
| 021 | 021-03 | `phase/phase-021-03-add-bounded-directive-proof-and-sync.md` | Completed | None | Approved As-Is | bounded directive proof added and sync surfaces aligned for the reference-first compact review model |
| 022 | 022-01 | `phase/phase-022-01-refine-direct-human-readable-wording.md` | Completed | None | Approved As-Is | direct human-readable wording refinement applied across wording, explanation, presentation, and style owners |
| 022 | 022-02 | `phase/phase-022-02-sync-master-docs-and-runtime-install.md` | Completed | None | Approved As-Is | master docs synchronized and runtime-install parity restored for the direct human-readable wording refinement |
| 023 | 023-01 | `phase/phase-023-01-rules-first-over-memory-boundary.md` | Completed | None | Approved As-Is | rules-first-over-memory boundary applied and support/package artifact portability clarified |
| 023 | 023-02 | `phase/phase-023-02-sync-master-docs-and-runtime-install.md` | Completed | None | Approved As-Is | master docs synchronized and runtime-install parity restored for the rules-first-over-memory refinement |
| 024 | 024-01 | `phase/phase-024-01-refine-purpose-first-communication.md` | Completed | None | Approved As-Is | purpose-first refinement applied across wording, explanation, presentation, and style owners |
| 024 | 024-02 | `phase/phase-024-02-sync-master-docs-and-runtime-install.md` | Completed | None | Approved As-Is | master docs synchronized and runtime-copy parity restored |
| 025 | 025-01 | `phase/phase-025-01-refine-compact-table-defaults.md` | Completed | None | Approved As-Is | compact-table / list-first refinement applied across presentation and explanation owners |
| 025 | 025-02 | `phase/phase-025-02-sync-master-docs-and-runtime-install.md` | Completed | None | Approved As-Is | master-surface sync completed and runtime-copy parity restored |
| 026 | 026-01 | `phase/phase-026-01-create-memory-governance-rule-chain.md` | Completed | None | Approved As-Is | new memory-governance owner chain created |
| 026 | 026-02 | `phase/phase-026-02-integrate-memory-governance-companions.md` | Completed | None | Approved As-Is | companion authority/writing/burden-of-proof/presentation integrations applied |
| 026 | 026-03 | `phase/phase-026-03-sync-master-docs-and-runtime-install.md` | Completed | None | Approved As-Is | master-surface sync and runtime-install parity completed |
| 026 | 026-04 | `phase/phase-026-04-run-postflight-memory-governance-audit.md` | Completed | None | Approved As-Is | governance-only boundary and source/install parity verified |
| 027 | 027-01 | `phase/phase-027-01-refine-task-list-first-execution-tracking.md` | In Progress | Review Pending | Awaiting Review | task-list-first refinement is being applied across tracking/startup/documentation owners |
| 027 | 027-02 | `phase/phase-027-02-sync-master-docs-and-runtime-install.md` | In Progress | Review Pending | Awaiting Review | master-surface sync and runtime-install parity are in progress for the task-list-first refinement |
| 028 | 028-01 | `phase/phase-028-01-refine-plain-aligned-table-style.md` | In Progress | Review Pending | Awaiting Review | plain aligned no-frame table-style correction is being applied across presentation/explanation owners |
| 028 | 028-02 | `phase/phase-028-02-sync-master-docs-and-runtime-install.md` | In Progress | Review Pending | Awaiting Review | master-surface sync and runtime-install parity are in progress for the table-style refinement |

---

## Phase Map

| Major Phase | Phase | Status | File | Objective | Depends On |
|------------|-------|--------|------|-----------|------------|
| 001 | 001-01 | Completed | `phase/phase-001-01-create-tactical-strategic-rule.md` | Create the first-class `tactical-strategic-programming` rule chain | none |
| 001 | 001-02 | Completed | `phase/phase-001-02-integrate-related-rules.md` | Align master documentation and related owner references with the new doctrine | `001-01` |
| 001 | 001-03 | Completed | `phase/phase-001-03-install-and-verify.md` | Install the new runtime rule and verify source/install alignment | `001-02` |
| 002 | 002-01 | Completed | `phase/phase-002-01-create-natural-professional-rule.md` | Create the first-class doctrine owner chain | none |
| 002 | 002-02 | Completed | `phase/phase-002-02-refine-primary-communication-chains.md` | Align wording, explanation, and presentation owners | `002-01` |
| 002 | 002-03 | Completed | `phase/phase-002-03-tighten-default-mode-and-correction-boundaries.md` | Align neutral default mode and constructive correction posture | `002-02` |
| 002 | 002-04 | Completed | `phase/phase-002-04-sync-master-docs-install-and-verify.md` | Synchronize master docs, install, and verify parity | `002-03` |
| 003 | 003-01 | Completed | `phase/phase-003-01-define-patch-model.md` | Define the corrected patch concept and normalize patch examples | none |
| 003 | 003-02 | Completed | `phase/phase-003-02-realign-dependent-docs.md` | Realign dependent governance docs to the corrected patch model | `003-01` |
| 003 | 003-03 | Completed | `phase/phase-003-03-sync-history-and-verify.md` | Sync changelog/TODO history and verify remaining old patch references are historical only | `003-02` |
| 004 | 004-01 | Completed | `phase/phase-004-01-create-artifact-initiation-rule.md` | Create the first-class `artifact-initiation-control` rule chain | none |
| 004 | 004-02 | Completed | `phase/phase-004-02-realign-startup-governance.md` | Realign startup-governance owner chains to the new rule | `004-01` |
| 004 | 004-03 | Completed | `phase/phase-004-03-sync-master-docs-and-history.md` | Sync master docs, TODO, changelog, and phase summary for the new startup-governance wave | `004-02` |
| 005 | 005-01 | Implemented - Pending Review | `phase/phase-005-01-harden-phase-patch-linkage.md` | Harden explicit phase-to-patch linkage in the live phase workspace | none |
| 005 | 005-02 | Implemented - Pending Review | `phase/phase-005-02-sync-master-docs-and-history.md` | Sync master docs, TODO, changelog, and phase summary for the new linkage-hardening wave | `005-01` |
| 006 | 006-01 | Implemented - Pending Review | `phase/phase-006-01-create-external-verification-rule.md` | Create the first-class external-verification-and-source-trust rule chain | none |
| 006 | 006-02 | Implemented - Pending Review | `phase/phase-006-02-integrate-source-trust-governance.md` | Sync master docs, TODO, changelog, and phase summary for the new source-trust wave | `006-01` |
| 007 | 007-01 | Implemented - Pending Review | `phase/phase-007-01-create-custom-agent-selection-rule.md` | Create the first-class custom-agent-selection-priority rule chain | none |
| 007 | 007-02 | Implemented - Pending Review | `phase/phase-007-02-integrate-agent-selection-governance.md` | Sync master docs, TODO, changelog, and phase summary for the new custom-agent selection wave | `007-01` |
| 008 | 008-01 | Implemented - Pending Review | `phase/phase-008-01-create-portable-implementation-rule.md` | Create the first-class portable-implementation-and-hardcoding-control rule chain | none |
| 008 | 008-02 | Implemented - Pending Review | `phase/phase-008-02-integrate-hardcoding-governance.md` | Sync master docs, TODO, changelog, and phase summary for the new hardcoding-control wave | `008-01` |
| 008 | 008-03 | Implemented - Pending Review | `phase/phase-008-03-deepen-portability-integration.md` | Deepen the adjacent-chain integration slice for the new hardcoding-control owner | `008-02` |
| 009 | 009-01 | Completed | `phase/phase-009-01-audit-continuation-vs-interruption.md` | Audit overlap that encourages unnecessary mid-process option prompting | none |
| 009 | 009-02 | Implemented - Pending Review | `phase/phase-009-02-implement-continuation-priority.md` | Implement continuation-first behavior across the communication-owner chains | `009-01` |
| 010 | 010-01 | Implemented - Pending Review | `phase/phase-010-01-refine-install-doc-portability-owners.md` | Refine install-doc portability ownership and source-destination notation governance | none |
| 010 | 010-02 | Implemented - Pending Review | `phase/phase-010-02-sync-master-governance-and-runtime-install.md` | Sync master governance surfaces and runtime install parity for the new refinement wave | `010-01` |
| 011 | 011-01 | Implemented - Pending Review | `phase/phase-011-01-refine-recommended-option-wording.md` | Refine multi-option next-step wording so the preferred path is explicit and briefly justified | none |
| 011 | 011-02 | Implemented - Pending Review | `phase/phase-011-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the recommendation-format refinement | `011-01` |
| 012 | 012-01 | Implemented - Pending Review | `phase/phase-012-01-refine-variable-field-config-and-term-explanations.md` | Refine identifier-heavy explanations so variables, fields, config keys, enum-like values, and internal labels are explained before deeper reasoning depends on them | none |
| 012 | 012-02 | Implemented - Pending Review | `phase/phase-012-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the identifier-explanation refinement | `012-01` |
| 013 | 013-01 | Implemented - Pending Review | `phase/phase-013-01-refine-goal-qualified-proposals.md` | Refine future-work proposals so they stay advisory, goal-qualified, and visibly separate from active execution | none |
| 013 | 013-02 | Implemented - Pending Review | `phase/phase-013-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the proposal-boundary refinement | `013-01` |
| 014 | 014-01 | Implemented - Pending Review | `phase/phase-014-01-refine-team-agent-dedup-boundaries.md` | Refine team-agent behavior so matching teammates are reused before spawn and duplicate-looking team state is inspected before respawn | none |
| 014 | 014-02 | Implemented - Pending Review | `phase/phase-014-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the team-agent dedup/stale-presence refinement | `014-01` |
| 015 | 015-01 | Completed | `phase/phase-015-01-refine-governing-basis-clarification.md` | Refine ambiguity handling so materially different governing bases are clarified first instead of explored through deep branch analysis | none |
| 015 | 015-02 | Completed | `phase/phase-015-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the governing-basis clarification refinement | `015-01` |
| 016 | 016-01 | Completed | `phase/phase-016-01-refine-compact-and-post-compact-governance.md` | Refine compacted-session continuation so the assistant re-anchors to the active objective and active frame before resuming | none |
| 016 | 016-02 | Completed | `phase/phase-016-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the compact/post-compact refinement | `016-01` |
| 017 | 017-01 | Completed | `phase/phase-017-01-create-rules-plugin-extension-area.md` | Create the optional `plugin/` companion area for hook-based compact handling while keeping root RULES as the only semantic authority | `016-02` |
| 017 | 017-02 | Completed | `phase/phase-017-02-sync-root-docs-and-verify-plugin-companion.md` | Synchronize root governance surfaces and verify that the plugin companion remains support / extension-only | `017-01` |
| 018 | 018-01 | Completed | `phase/phase-018-01-replace-latest-witness-model-with-ephemeral-handoff.md` | Replace the plugin’s latest-only compact witness model with a one-shot ephemeral handoff lifecycle | `017-02` |
| 018 | 018-02 | Completed | `phase/phase-018-02-sync-plugin-docs-and-verify-compact-handoff-lifecycle.md` | Synchronize package/root docs and verify the new compact handoff lifecycle with real runtime checks | `018-01` |
| 019 | 019-01 | Completed | `phase/phase-019-01-replace-single-slot-compact-state-with-session-scoped-layout.md` | Replace singleton compact state with a small index and per-session carry-forward directories | `018-02` |
| 019 | 019-02 | Completed | `phase/phase-019-02-sync-docs-and-verify-session-scoped-compact-carry-forward.md` | Synchronize docs and verify session-scoped compact carry-forward behavior | `019-01` |
| 020 | 020-01 | Completed | `phase/phase-020-01-tighten-active-review-trigger.md` | Turn compact SessionStart into an active review trigger that names exact-session review files before continuation | `019-02` |
| 020 | 020-02 | Completed | `phase/phase-020-02-add-optional-memsearch-assist-boundary.md` | Record memsearch as a later assist-layer boundary while keeping the active runtime local-review-first | `020-01` |
| 020 | 020-03 | Completed | `phase/phase-020-03-sync-docs-and-verify-active-review-behavior.md` | Synchronize docs/versions and verify the active review-trigger behavior | `020-02` |
| 021 | 021-01 | Completed | `phase/phase-021-01-tighten-systemmessage-review-required.md` | Make the visible compact navigator line explicitly say review is required before continuation | `020-03` |
| 021 | 021-02 | Completed | `phase/phase-021-02-tighten-additionalcontext-reference-first.md` | Reduce additionalContext to instruction + locator + bounded status only | `021-01` |
| 021 | 021-03 | Completed | `phase/phase-021-03-add-bounded-directive-proof-and-sync.md` | Add bounded directive proof and synchronize docs/version surfaces | `021-02` |
| 022 | 022-01 | Completed | `phase/phase-022-01-refine-direct-human-readable-wording.md` | Refine the communication-owner set so direct human-readable action/result wording is preferred over metaphor-heavy internal shorthand | none |
| 022 | 022-02 | Completed | `phase/phase-022-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the direct human-readable wording refinement | `022-01` |
| 023 | 023-01 | Completed | `phase/phase-023-01-rules-first-over-memory-boundary.md` | Refine authority and portability owners so user-declared RULES-first issues are fixed in RULES rather than memory and support/package source artifacts remain portable by default | none |
| 023 | 023-02 | Completed | `phase/phase-023-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the rules-first-over-memory and portable-support-artifact refinement | `023-01` |
| 024 | 024-01 | Completed | `phase/phase-024-01-refine-purpose-first-communication.md` | Refine the communication-owner set so diagnosis, test, recommendation, proposal, and implementation-update answers state what they are doing before the supporting detail expands | none |
| 024 | 024-02 | Completed | `phase/phase-024-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the purpose-first communication refinement | `024-01` |
| 025 | 025-01 | Completed | `phase/phase-025-01-refine-compact-table-defaults.md` | Refine the presentation/explanation owner set so compact markdown tables become the default table form when useful and list-first alternatives stay explicit | none |
| 025 | 025-02 | Completed | `phase/phase-025-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the compact-table / list-first refinement | `025-01` |
| 026 | 026-01 | Completed | `phase/phase-026-01-create-memory-governance-rule-chain.md` | Create the first-class rule chain that owns memory governance and session-boundary behavior | none |
| 026 | 026-02 | Completed | `phase/phase-026-02-integrate-memory-governance-companions.md` | Integrate adjacent authority, wording, burden-of-proof, and presentation owners with the new chain | `026-01` |
| 026 | 026-03 | Completed | `phase/phase-026-03-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the memory-governance refinement | `026-02` |
| 026 | 026-04 | Completed | `phase/phase-026-04-run-postflight-memory-governance-audit.md` | Run the final consistency and parity sweep for the memory-governance refinement | `026-03` |
| 027 | 027-01 | In Progress | `phase/phase-027-01-refine-task-list-first-execution-tracking.md` | Refine the owner set so the built-in task list becomes the live execution surface for non-trivial active work while `TODO.md` remains the durable tracking artifact | none |
| 027 | 027-02 | In Progress | `phase/phase-027-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the task-list-first refinement | `027-01` |
| 028 | 028-01 | In Progress | `phase/phase-028-01-refine-plain-aligned-table-style.md` | Refine the owner set so ordinary answer tables use the selected light plain aligned no-frame form while table usage remains available when genuinely useful | none |
| 028 | 028-02 | In Progress | `phase/phase-028-02-sync-master-docs-and-runtime-install.md` | Synchronize master governance surfaces and runtime install parity for the table-style refinement | `028-01` |

---

## Global TODO / Changelog Coordination

- `TODO.md` should record the source-trust rollout, the custom-agent-selection rollout, the portable-implementation rollout, the continuation-priority refinement, the install-doc portability refinement, the identifier-explanation refinement, the proposal-boundary refinement, the team-agent dedup/stale-presence refinement, the governing-basis clarification refinement, the compact/post-compact refinement, the plugin extension companion rollout, the compact handoff lifecycle refinement, the session-scoped compact carry-forward refinement, the active review-trigger compact refinement, the reference-first compact review refinement, the direct human-readable wording refinement, the rules-first-over-memory refinement, the purpose-first communication refinement, the compact-table / list-first refinement, the memory-governance / session-boundary refinement, the task-list-first execution-tracking refinement, and the plain aligned no-frame table-style refinement in dated history until final review is complete.
- `changelog/changelog.md` should record the repository-level source-trust rollout, the custom-agent-selection rollout, the portable-implementation rollout, the continuation-priority refinement, the install-doc portability refinement, the identifier-explanation refinement, the proposal-boundary refinement, the team-agent dedup/stale-presence refinement, the governing-basis clarification refinement, the compact/post-compact refinement, the plugin extension companion rollout, the compact handoff lifecycle refinement, the session-scoped compact carry-forward refinement, the active review-trigger compact refinement, the reference-first compact review refinement, the direct human-readable wording refinement, the rules-first-over-memory refinement, the purpose-first communication refinement, the compact-table / list-first refinement, the memory-governance / session-boundary refinement, the task-list-first execution-tracking refinement, and the plain aligned no-frame table-style refinement after the touched chains are aligned.
- touched chain changelogs should record the new external-verification, custom-agent-selection, portable-implementation, continuation-priority, install-doc portability, identifier-explanation, proposal-boundary, team-agent dedup/stale-presence, governing-basis clarification, compact/post-compact, plugin extension support-layer, compact handoff lifecycle, session-scoped compact carry-forward, active review-trigger, reference-first compact review, direct human-readable wording, rules-first-over-memory, purpose-first communication, compact-table / list-first, memory-governance / session-boundary, task-list-first execution-tracking, and plain aligned no-frame table-style changes without broadening ownership boundaries unnecessarily.

---

## Final Verification

- active phase workspace uses `NNN` for majors and `NNN-NN` for subphases
- no symbolic `P1/P2/P3/P4/P5` identifiers remain in the active `phase/` workspace
- summary tables reference real phase files
- parent-child grouping is visible in the summary
- historical records remain in changelog/TODO rather than being rewritten here
- phased work with governed patch artifacts is expected to show explicit linkage from `phase/SUMMARY.md` and relevant child phase files
- the external-verification chain exists as a governed triad with visible rollout indexing in the phase workspace
- the custom-agent-selection chain exists as a governed triad with visible rollout indexing in the phase workspace
- the portable-implementation-and-hardcoding-control chain exists as a governed triad with visible rollout indexing in the phase workspace
- the install-doc portability refinement wave exists as a bounded `010` family with explicit patch linkage and master-governance synchronization
- the identifier-explanation refinement wave exists as a bounded `012` family with explicit patch linkage and master-governance synchronization
- the goal-qualified proposal refinement wave exists as a bounded `013` family with explicit patch linkage and master-governance synchronization
- the team-agent dedup/stale-presence refinement wave exists as a bounded `014` family with explicit patch linkage and master-governance synchronization
- the governing-basis clarification refinement wave exists as a bounded `015` family with explicit patch linkage and master-governance synchronization
- the compact/post-compact refinement wave exists as a bounded `016` family with explicit patch linkage and master-governance synchronization
- the plugin extension companion rollout exists as a bounded `017` family with explicit patch linkage and support-layer boundary visibility
- the compact handoff lifecycle refinement exists as a bounded `018` family with explicit patch linkage, package/root doc synchronization, and runtime verification of the ephemeral handoff model
- the session-scoped compact carry-forward refinement exists as a bounded `019` family with explicit patch linkage, per-session storage layout, fail-closed ambiguous routing, and runtime verification of the session-scoped injection model
- the active review-trigger compact refinement exists as a bounded `020` family with explicit patch linkage, review-trigger behavior, and synchronized master-governance surfaces
- the reference-first compact review refinement exists as a bounded `021` family with explicit patch linkage, reference-first additionalContext behavior, and synchronized master-governance surfaces
- the direct human-readable wording refinement exists as a bounded `022` family with explicit patch linkage, owner-set wording/explanation/style/presentation integration, and synchronized master-governance surfaces
- the rules-first-over-memory refinement exists as a bounded `023` family with explicit patch linkage, authority/portability integration, and synchronized master-governance surfaces
- the purpose-first communication refinement exists as a bounded `024` family with explicit patch linkage, owner-set wording/explanation/presentation/style integration, and synchronized master-governance surfaces
- the compact-table / list-first refinement exists as a bounded `025` family with explicit patch linkage, presentation/explanation-owner integration, and synchronized master-governance surfaces
- the memory-governance / session-boundary refinement exists as a bounded `026` family with explicit patch linkage, a new first-class memory-governance owner, narrow companion-owner integration, synchronized master-governance surfaces, and an explicit governance-first / migration-later boundary
- the task-list-first execution-tracking refinement exists as a bounded `027` family with explicit patch linkage, owner-set refinement across tracking/startup/documentation surfaces, synchronized master-governance surfaces, and preserved distinction between live built-in task tracking and durable `TODO.md` tracking
- the plain aligned no-frame table-style refinement exists as a bounded `028` family with explicit patch linkage, owner-set refinement across presentation/explanation surfaces, synchronized master-governance surfaces, and preserved distinction between table style correction and table-frequency reduction

---

## Overall Rollback / Containment

If the compact/post-compact refinement or plugin companion rollout proved incorrect, rollback would require:
- narrowing the post-compact re-anchor wording in the touched owner chains
- restoring prior master-governance wording where needed while preserving any still-useful compact-state caution that remains valid
- keeping `plugin/` clearly subordinate or removing the optional package while preserving the recorded design/phase/patch/changelog history instead of silently erasing the rollout evidence

---
