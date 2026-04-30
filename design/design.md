# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 9.77
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-04-30)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

This active-state model must preserve UDVC-1 while supporting first-class phased execution planning, explicit patch/review artifacts, completed documentation history surfaces for phase/patch/changelog scan-bloat control, first-class startup artifact initiation control, proactive external verification and source trust, evidence-calibrated agreement so factual endorsement requires evidence while user-owned preference/direction remains separate, portable implementation defaults, public onboarding/install portability, anti-hardcoding discipline, memory governance and session-boundary behavior, source-only semantic-preserving runtime rule compression with complete patch inventory coverage before execution, explicit runtime install/parity verification when installation is separately requested, a runtime destination ownership boundary for co-located other-owner runtime files, phase-backed closeout reporting that states delivered work and impact before audit-only detail dominates, and design-to-phase execution synthesis so sufficiently clear governed design can become phase execution order and current-phase live tasks when staged execution is warranted.

---

## 2) Active Repository Model

### 2.1 Layer Roles

| Layer | Primary Artifacts | Active Role |
|------|--------------------|-------------|
| Overview | `README.md` | Repository overview and usage guidance only |
| Runtime | root `*.md` rules | Active runtime behavior |
| Design | `design/*.design.md` | Active target-state guidance; no default `design/done/` surface |
| Phase | `phase/SUMMARY.md`, `phase/phase-NNN-<phase-name>.md`, `phase/phase-NNN-NN-<subphase-name>.md`, `phase/done/phase-NNN-*.md` | Governed live phase-planning summary/index and execution detail, with inactive completed phase history under `phase/done/` |
| Patch | `patch/<context>.patch.md`, `patch/done/<context>.patch.md`, or root `<context>.patch.md` | Governed active patch/review artifacts plus inactive completed patch history outside live phase planning |
| History | `changelog/*.changelog.md`, `changelog/done/*.changelog.md` | Authoritative active chain history/version state plus inactive completed or older history when needed |
| Execution | `TODO.md` | Execution tracking only |
| Support | `phase-implementation-template.md`, `support/**/*.md` | Root-level helper templates and reference-only/support materials inside RULES only |

### 2.2 Governance Principle

This repository uses one deterministic governance model:
- README is overview-only
- runtime rules are the active rule layer
- factual agreement, contradiction, and preference/direction handling are evidence-calibrated: acknowledge concerns and accept user-owned direction without upgrading unverified factual claims into truth
- active runtime rule compression must preserve semantic parity and should start from a complete patch inventory/baseline before any rule-body rewrite begins
- repository-level compression record sync should describe completed runtime slices without turning governed planning surfaces into compression targets, without mass-bumping per-rule chains automatically, without claiming runtime install before that separate gate passes, and with runtime install/parity recorded only after that explicit gate is executed
- shared runtime destination co-location is not ownership authority; destination/runtime files outside the current source-owned install set require owner/project scope resolution before classification, cleanup, or deletion is considered, and adjacent documentation/hygiene/reference owners preserve that boundary without turning shared-destination co-location into ownership
- design docs hold active target-state guidance and do not use a default `design/done/` pattern
- `phase/` is the live phased execution layer when staged planning is used
- `phase/done/` is inactive-by-default completed phase history
- phase IDs use `NNN` for major phases and `NNN-NN` for subphases
- active patch docs are the governed patch/review layer outside live phase planning
- `patch/done/` is inactive-by-default completed patch history
- active changelog files are the authority for governed chain history and current version state
- `changelog/done/` may hold older/completed detailed history outside the active scan surface
- TODO tracks execution state only
- startup artifact posture is resolved before meaningful governed work drifts
- support and optional extension-package artifacts help authoring, reference reuse, or runtime reinforcement but do not masquerade as governed design, phase, or patch authorities
- older coordination-flavored rollout records in master/history surfaces remain historical context only after the later ownership split and do not override the current active runtime/design authority boundary

---

## 3) Rule Architecture

### 3.1 Active Runtime Inventory

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | accurate-communication.md | accurate-communication.design.md v2.19 | Clear, context-complete, verification-honest, and evidence-threshold-aligned communication with acknowledgement-without-endorsement wording, evidence-backed agreement, user-owned preference/direction separation, claim-focused contradiction guardrails, stronger human-language glosses, easy-explanation continuity so plain Thai explanations stay simple through the full answer, explicit clarification of variables/fields/config keys/internal labels when answers depend on them, duplicate-looking team-agent reporting honesty with observed-vs-inferred state separation, governing-basis clarification before deep branch analysis when multiple materially different policies/frames remain live, post-compact re-anchor wording for compacted-session continuation, memory-derived-context disclosure wording for path-matched remembered context, natural-professional wording guidance, direct human-readable action/result wording preference over metaphor-heavy internal shorthand, explicit main-point-first operational framing for diagnosis/test/recommendation/proposal/update answers, phase-backed closeout wording that makes delivered work, feature/improvement, impact, verification basis, and next phase state visible without overclaiming, and continuation-first execution guidance |
| 2 | answer-presentation.md | answer-presentation.design.md v1.26 | Principle-first, trigger-driven presentation guidance for readable, orderly, and scannable output, including purpose-first framing near the start of diagnosis/test/recommendation/proposal/update answers, compact goal-review presentation support, easy-explanation layout support with plain-language headings, more proactive light readable tables when side-by-side structure materially improves comprehension, compact governing-basis clarification blocks, compact post-compact re-anchor blocks, compact memory-status blocks, narrower next-stage blocks that do not interrupt active execution, compact variable-role structures, compact phase-backed closeout layout for delivered work, feature/improvement, impact, verification, and next phase state, and compact proposal layouts that distinguish advisory future-work ideas from queued execution |
| 3 | anti-mockup.md | anti-mockup.design.md v1.1 | Real systems over mocks |
| 4 | anti-sycophancy.md | anti-sycophancy.design.md v1.5 | Evidence-calibrated agreement/disagreement: truth over pleasing, user preference/direction accepted without factual endorsement, factual agreement requires evidence, and corrections remain claim-focused when contrary evidence exists |
| 5 | artifact-initiation-control.md | artifact-initiation-control.design.md v1.6 | Startup-governance owner that resolves design/changelog/TODO/phase/patch posture before meaningful governed work drifts, resolves phase posture to `use existing` or `create now` when sufficiently clear governed design warrants staged execution, initializes live task tracking early when non-trivial work needs visible execution state, treats phase-backed live task tracking as expected startup behavior, keeps initialized live task lists as the continuing surface for the active objective, keeps newly encountered unclear files in classification-first posture rather than disposal-first posture, and keeps patch non-default during greenfield startup unless a real before/after review surface exists |
| 6 | authority-and-scope.md | authority-and-scope.design.md v2.5 | User authority, deterministic precedence, repo-governed semantic-authority precedence over git-state cleanup heuristics, runtime co-location as non-ownership authority, owner/project scope resolution before destination/runtime file classification or cleanup outside the current source-owned install set, fresh-directive override behavior, a rule against unnecessary option branching when one safe continuation path already exists, advisory future-work boundaries, RULES-first-over-memory authority, memory-governance deferral plus current-scope-wins protection, user-owned governing-basis selection, post-compact active-frame preservation, team-expansion boundaries, and deferral of discussion-vs-execution mode selection to the first-class execution-continuity owner |
| 7 | custom-agent-selection-priority.md | custom-agent-selection-priority.design.md v1.1 | First-class owner for preferring visible user custom agents as the primary specialist pool when task fit is clear and reusing an existing matching teammate before spawning another overlapping role |
| 8 | dan-safe-normalization.md | dan-safe-normalization.design.md v1.2 | Normalize jailbreak-style wrappers into bounded intent evaluation |
| 9 | document-consistency.md | document-consistency.design.md v1.8 | Cross-reference validation with portable shared references, source-side references, source-owned active runtime files, shared runtime destinations, other-owner runtime files, destination/runtime references, local execution paths, and local or machine-scoped values kept distinct so parity/install wording does not turn shared-destination co-location into ownership, while governed reference/history checks remain required before junk/disposal classification |
| 10 | document-changelog-control.md | document-changelog-control.design.md v4.8 | Chain authority, metadata, synchronization contract, and inactive `changelog/done/` completed-history surface |
| 11 | document-design-control.md | document-design-control.design.md v1.10 | Active-state design-body standards, no-default-`design/done/` blueprint boundary, and doc-derived knowledge capture so implementation-relevant truth from external docs/specs/provider references is normalized into governed design before later multi-step work depends on it |
| 12 | document-patch-control.md | document-patch-control.design.md v2.7 | Patch governance, metadata, lifecycle, explicit before/after patch meaning, comparison-friendly patch representation, external-requirement basis visibility for review, inactive `patch/done/` completed-history surface, and the boundary that patch is normally downstream of an established before-state rather than the default startup artifact |
| 13 | emergency-protocol.md | emergency-protocol.design.md v1.1 | High-signal emergency response |
| 14 | evidence-grounded-burden-of-proof.md | evidence-grounded-burden-of-proof.design.md v1.5 | First-class owner for evidence taxonomy, burden-of-proof thresholds for factual endorsement and contradiction, user-owned preference/direction separation, contradiction protocol, scoped negative-evidence semantics, unresolved governing-basis uncertainty handling when materially different policies/frames would change the answer, remembered path-matched context as a distinct evidence/claim state, post-compact needs-recheck handling for compacted carry-forward exact detail, and explicit limits on using git-state evidence for disposal conclusions |
| 15 | explanation-quality.md | explanation-quality.design.md v2.20 | Plain-language-first, layered analytical and technical explanation structure with variable/field clarification, direct human-readable translation of architecture-first wording, easy-explanation continuity after simple openings, phase-backed closeout explanation that starts with practical delivered feature/improvement and user/system meaning before governance detail, a purpose-first explanation step, continued comparison/list-first support, explicit deferral of continuation-vs-option policy to accurate-communication, a governing-basis clarification boundary, a compact post-compact re-anchor boundary, goal-qualified proposal framing, and explicit deferral of goal-review semantics to the first-class goal-set owner |
| 16 | external-verification-and-source-trust.md | external-verification-and-source-trust.design.md v1.0 | First-class owner for proactive external verification, source-trust ranking, corroboration, and source-conflict handling |
| 17 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md v1.1 | Text diagrams without frames or boxes |
| 18 | functional-intent-verification.md | functional-intent-verification.design.md v1.2 | Clarify destructive/expensive intent before execution, including an explicit delete guard that blocks cleanup/isolation rationale from acting as deletion authorization |
| 19 | memory-governance-and-session-boundary.md | memory-governance-and-session-boundary.design.md v1.5 | First-class owner for memory role boundaries, root `MEMORY.md` index-only behavior, `global/path/archive` taxonomy, path-primary applicability, session provenance, canonical `SCOPE.md`, archive-inactive lifecycle semantics, and generic optional external recall guidance that stays supplemental and subordinate to stronger execution evidence without implying a Main RULES-managed custom skill path or retired bridge mechanism |
| 20 | no-variable-guessing.md | no-variable-guessing.design.md v1.5 | Read before reference with inspected-scope local evidence discipline, including git-state observations kept in the weak local-evidence lane until governed repo surfaces are checked |
| 21 | operational-failure-handling.md | operational-failure-handling.design.md v1.2 | Profile-driven operational failure classification, bounded retry policy, honest cooldown/escalation behavior, and a Team Agent duplicate/stale-presence profile that treats duplicate-looking or stale team-agent presence as inspect-before-respawn rather than respawn-first churn |
| 22 | phase-implementation.md | phase-implementation.design.md v2.25 | First-class semantic standard for phased execution planning with early phase-establishment bridge, explicit design-to-phase synthesis when sufficiently clear governed design warrants staged execution, inactive `phase/done/` completed-history behavior, current-phase-first but phase-context-aware live task-list linkage, explicit phase-to-patch linkage when patch is in scope, phase-backed closeout reporting that states delivered feature/improvement, impact, verification basis, and next phase state when relevant, bounded next-work discovery from the active phase workspace, session-language-aware phase-linked task wording, and an explicit boundary that shared-board/plugin/external coordination mechanics stay outside Main RULES current doctrine |
| 23 | project-documentation-standards.md | project-documentation-standards.design.md v2.31 | Repository-level document-role model plus startup artifact gate, completed documentation surface governance for `phase/done/`, `patch/done/`, and `changelog/done/`, no-default-`design/done/` blueprint boundary, governed companion status for required design/changelog/TODO/phase/patch surfaces, explicit patch-linkage verification for phased work, live-task-list-vs-durable-TODO split, phase-shaped task creation alignment, execution-discovery surface recognition, runtime installs scoped to the current project/source-owned active runtime rule set, other-owner runtime file boundary, non-default startup patch posture, portable public onboarding/install guidance, portable support assets, and the boundary that shared-board-specific coordination semantics stay outside Main RULES scope |
| 24 | recovery-contract.md | recovery-contract.design.md v1.5 | No dead-end constrained/refused responses |
| 25 | refusal-classification.md | refusal-classification.design.md v1.4 | Deterministic refusal taxonomy |
| 26 | refusal-minimization.md | refusal-minimization.design.md v1.5 | Prefer recoverable paths over premature refusal |
| 27 | safe-file-reading.md | safe-file-reading.design.md v1.3 | Plan-before-read file safety |
| 28 | safe-terminal-output.md | safe-terminal-output.design.md v1.3 | Plan-before-execute output safety |
| 29 | strict-file-hygiene.md | strict-file-hygiene.design.md v1.5 | Prevent junk files and duplicates while deferring to required governed startup artifacts, blocking cleanup/hygiene wording from acting as deletion authority, keeping destination/runtime files outside the current source-owned install set from being treated as junk by shared-destination co-location alone, and avoiding machine-local hardcoded defaults in reusable artifacts |
| 30 | todo-standards.md | todo-standards.design.md v2.20 | Durable TODO governance with startup-establishment bridge, current-phase-first but phase-context-aware built-in task-list usage for non-trivial live execution tracking, required inspection of relevant governed `/phase` context before task shaping when that context exists, task creation aligned to active phase or clearly implied staged/phase context, bounded use of already-authored `/phase` planning data for continuity and draft next-work discovery, task wording that follows the actual active session language pattern, same-objective reuse/append retention, completed-task visibility until closure, task-list-first next-work discovery with bounded fallback to broader execution surfaces, explicit required TODO synchronization as companion work rather than optional bookkeeping when `TODO.md` is needed, and an explicit boundary that shared-board/plugin/external coordination mechanics stay outside Main RULES current doctrine |
| 31 | runtime-topology-control.md | runtime-topology-control.design.md v1.1 | Bounded runtime mutation posture with inspect-before-mutate discipline |
| 32 | unified-version-control-system.md | unified-version-control-system.design.md v1.2 | UDVC-1 controller-level governance view |
| 33 | tactical-strategic-programming.md | tactical-strategic-programming.design.md v1.2 | Tactical entry, strategic target, convergence path, strategic closure doctrine, and anti-hardcoding tactical-boundary discipline |
| 34 | natural-professional-communication.md | natural-professional-communication.design.md v1.3 | First-class doctrine for natural professional communication, including easy-explanation register support for plain Thai answers, rejection of metaphor-heavy or management-style abstraction when direct human-readable wording would be clearer, and explicit purpose-before-detail wording for operational answers |
| 35 | portable-implementation-and-hardcoding-control.md | portable-implementation-and-hardcoding-control.design.md v1.2 | First-class owner for portable implementation defaults, portable-by-default support/package source artifacts, public onboarding/install portability, late-bound environment resolution, scoped local observations, and anti-hardcoding discipline |
| 36 | zero-hallucination.md | zero-hallucination.design.md v1.5 | Verified information only, including verified factual endorsement before agreement with factual claims, with fact/preference-direction/inference/hypothesis separation, scoped non-finding discipline, unsupported factual-endorsement risk, and explicit limits on using git-state observations as disposal truth |
| 37 | high-signal-communication.md | high-signal-communication.design.md v1.1 | Bounded supplementary high-signal filtering that trims low-value extra content and repeated wording while deferring required-content ownership to the existing communication, explanation, and presentation chains |
| 38 | execution-continuity-and-mode-selection.md | execution-continuity-and-mode-selection.design.md v1.7 | First-class owner for discussion-vs-execution mode selection, startup-gate-first execution boundaries, continuous-execution defaults after startup posture is resolved enough, active next-work discovery from execution surfaces, capture-before-continue protection when implementation-critical external knowledge has not yet been normalized into governed artifacts, legitimate stop gates, the boundary that milestone reporting must not replace continued execution, and the boundary that shared-board-specific coordination semantics stay outside Main RULES scope |
| 39 | goal-set-review-and-priority-balance.md | goal-set-review-and-priority-balance.design.md v1.0 | First-class owner for continuous goal-set review, structure-first priority balance, and protection against single-subtask fixation so work on A does not crowd out B and C |
| 40 | technical-snapshot-communication.md | technical-snapshot-communication.design.md v1.0 | First-class owner for bounded technical snapshot wording, exact/partial/inferred separation, scoped local-fact snapshot communication, and concise diagnostic snapshot state reporting |
| 41 | response-closing-and-action-framing.md | response-closing-and-action-framing.design.md v1.1 | First-class owner for concise end-of-response synthesis, clear action framing, recommendation-with-reason wording, alternative preservation, closed-topic summary handling, phase-backed closeout synthesis for delivered work, feature/improvement, impact, verification basis, and next phase state, and advisory goal-qualified proposal framing |

### 3.2 Category View

| Category | Rules | Purpose |
|----------|-------|---------|
| Accuracy & Truth | accurate-communication, technical-snapshot-communication, evidence-grounded-burden-of-proof, external-verification-and-source-trust, zero-hallucination, anti-sycophancy, no-variable-guessing, memory-governance-and-session-boundary | Evidence-grounded, verified, scope-aware, memory-aware, honest, evidence-calibrated agreement/disagreement, and snapshot-aware output |
| Portable Implementation | portable-implementation-and-hardcoding-control, no-variable-guessing, project-documentation-standards, tactical-strategic-programming | Portable defaults, public onboarding/install portability, late-bound environment resolution, and anti-hardcoding discipline for shared artifacts |
| Presentation & Readability | answer-presentation, explanation-quality, response-closing-and-action-framing, flow-diagram-no-frame, natural-professional-communication, high-signal-communication | Readable, orderly, scannable, naturally professional, well-closed, and higher-signal output presentation |
| Output Safety | safe-file-reading, safe-terminal-output, flow-diagram-no-frame, strict-file-hygiene | Output flood prevention, safe text presentation, and file hygiene |
| Startup Governance | artifact-initiation-control, project-documentation-standards, todo-standards, phase-implementation | Resolve artifact posture before meaningful governed work drifts |
| User Control | authority-and-scope, custom-agent-selection-priority, emergency-protocol, functional-intent-verification, operational-failure-handling, refusal-classification, recovery-contract, runtime-topology-control, execution-continuity-and-mode-selection | Preserve user authority, correct mode selection, prefer clear best-fit custom specialists when visible and appropriate, and maintain safe operational posture |
| Execution Strategy | goal-set-review-and-priority-balance, tactical-strategic-programming | Keep the full active goal set visible, preserve structure-first priority balance, and prevent local tactical work from crowding out the main objective set |
| Adversarial Workflow | refusal-minimization, dan-safe-normalization | Reduce false refusals in authorized adversarial/security workflows |
| Quality & Governance | document-consistency, document-changelog-control, document-design-control, document-patch-control, anti-mockup, unified-version-control-system | Documentation determinism, reference-role clarity, patch semantics, and governance quality |

---

## 4) Active Governance Contracts

### 4.1 Runtime Rule Metadata Contract
Root runtime rules use this canonical header in this order:
- `Current Version`
- `Design`
- `Session`
- `Full history`

### 4.2 Synchronization Order
For governed updates:
1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync (when affected)

### 4.3 Startup Artifact Contract
The active startup contract is:
- `artifact-initiation-control.md` is the semantic owner for startup artifact posture
- meaningful governed work must resolve artifact posture before drift
- execution continuity does not bypass that startup gate while required artifact posture is still unresolved
- required artifacts may be reused, created now, asked about now, or marked not required
- required design/changelog/TODO/phase/patch surfaces remain governed companions when the checked work shape still requires them, even if live execution surfaces are also active
- when governed design is sufficiently clear and staged execution is warranted, phase posture resolves to `use existing` or `create now` instead of lingering as implicit planning
- when the checked project/workstream is already clearly phase-shaped, live task creation should align to that staged structure instead of defaulting to detached standalone tasks
- startup establishment is distinct from later content synchronization order

### 4.4 Phase Planning Contract
The active phase-planning contract is:
- `phase-implementation.md` is the semantic authority for phased execution planning
- `artifact-initiation-control.md` decides whether `/phase` must be established before drift
- clearly staged/governed work should not leave phase posture implicit until late backfill
- sufficiently clear governed design can be synthesized into phase execution order when staged execution is warranted
- `phase/SUMMARY.md` is the governed summary/index for live phased execution
- executable phase files under `phase/` use `NNN` for major phases and `NNN-NN` for subphases
- patch docs remain separate governed patch/review artifacts outside the live phase workspace
- phased work with governed patch artifacts must declare that linkage explicitly in `phase/SUMMARY.md` and relevant child phase files

### 4.5 Completed Documentation Surface Contract
The active completed-history contract is:
- `phase/done/` may hold completed phase execution detail outside the active scan surface
- `patch/done/` may hold completed patch/review artifacts outside the active scan surface
- `changelog/done/` may hold older or completed detailed history outside the active scan surface
- `design/done/` is not a default governed design pattern because design remains active blueprint and target-state authority
- `done/` surfaces are inactive by default and are consulted for history, audit, rollback, provenance, or trace reconstruction only
- files in `done/` are not junk and completed status is not deletion authorization

### 4.6 Memory Governance Contract
The active memory-governance contract is:
- `memory-governance-and-session-boundary.md` is the semantic authority for memory role boundary and session/path applicability behavior
- root `MEMORY.md` remains present and acts as an active index only
- active memory is separated semantically into `global/`, `path/`, and `archive/`
- path is the primary applicability key for path-scoped memory
- session IDs are provenance only and do not become the primary applicability reason
- actual live-memory migration follows the governance contract rather than preceding it

---

## 5) Standard Templates

### 5.1 Runtime Rule Template
```markdown
# <Rule Name>

> **Current Version:** X.Y
> **Design:** [design/<rule>.design.md](design/<rule>.design.md) vX.Y
> **Session:** <real-session-id>
> **Full history:** [changelog/<rule>.changelog.md](changelog/<rule>.changelog.md)
```

### 5.2 Design Template
```markdown
# <Document Name>

## 0) Document Control

> **Parent Scope:** <scope>
> **Current Version:** X.Y
> **Session:** <real-session-id> (YYYY-MM-DD)
```

### 5.3 Changelog Template
```markdown
# Changelog - <Document>

> **Parent Document:** [../<doc>.md](../<doc>.md)
> **Current Version:** X.Y
> **Session:** <real-session-id>
```

---

## 6) Verification Checklist

- [ ] README remains overview-only
- [ ] Runtime rules remain the active rule layer
- [ ] Evidence-calibrated agreement remains separated from unsupported factual endorsement and from user-owned preference/direction
- [ ] Design docs remain active target-state guidance only and do not use a default `design/done/` surface
- [ ] Active changelogs remain version authority per chain while `changelog/done/` stays inactive history
- [ ] TODO remains execution-only
- [ ] Startup artifact posture is resolved before meaningful governed work drifts
- [ ] Active phase docs remain in `/phase`, use the active `NNN` / `NNN-NN` identity model, and move completed detail to `phase/done/` only as inactive history
- [ ] Active patch docs remain outside live phase planning while `patch/done/` stays inactive completed patch history
- [ ] Root helper and support artifacts remain non-governed

---

## 7) Integration

Related chains:
- `artifact-initiation-control.md`
- `document-changelog-control.md`
- `document-design-control.md`
- `phase-implementation.md`
- `project-documentation-standards.md`
- `document-patch-control.md`
- `todo-standards.md`
- `execution-continuity-and-mode-selection.md`
- `strict-file-hygiene.md`

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
