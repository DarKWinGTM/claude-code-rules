# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 9.30
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb (2026-04-13)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

This active-state model must preserve UDVC-1 while supporting first-class phased execution planning, explicit patch/review artifacts, first-class startup artifact initiation control, a first-class owner for proactive external verification and source trust, a first-class owner for portable implementation defaults, public onboarding/install portability, and anti-hardcoding discipline, and a first-class owner for memory governance and session-boundary behavior.

---

## 2) Active Repository Model

### 2.1 Layer Roles

| Layer | Primary Artifacts | Active Role |
|------|--------------------|-------------|
| Overview | `README.md` | Repository overview and usage guidance only |
| Runtime | root `*.md` rules | Active runtime behavior |
| Design | `design/*.design.md` | Active target-state guidance |
| Phase | `phase/SUMMARY.md`, `phase/phase-NNN-<phase-name>.md`, `phase/phase-NNN-NN-<subphase-name>.md` | Governed live phase-planning summary/index and execution detail |
| Patch | `patch/<context>.patch.md` or root `<context>.patch.md` | Governed patch/review artifacts outside live phase planning |
| History | `changelog/*.changelog.md` | Authoritative chain history and latest chain version state |
| Execution | `TODO.md` | Execution tracking only |
| Support | `phase-implementation-template.md`, `support/**/*.md`, `plugin/**` | Root-level helper templates, reference-only/support materials, and an optional unified Rules-owned plugin companion that may include compact-helper runtime reinforcement plus operator-facing support skills outside governed chain authority |

### 2.2 Governance Principle

This repository uses one deterministic governance model:
- README is overview-only
- runtime rules are the active rule layer
- design docs hold active target-state guidance
- `phase/` is the live phased execution layer when staged planning is used
- phase IDs use `NNN` for major phases and `NNN-NN` for subphases
- patch docs are the governed patch/review layer outside live phase planning
- changelog files are the authority for governed chain history
- TODO tracks execution state only
- startup artifact posture is resolved before meaningful governed work drifts
- support and optional extension-package artifacts help authoring, reference reuse, or runtime reinforcement but do not masquerade as governed design, phase, or patch authorities

---

## 3) Rule Architecture

### 3.1 Active Runtime Inventory (40 Rules)

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | accurate-communication.md | accurate-communication.design.md v2.14 | Clear, context-complete, verification-honest, and evidence-threshold-aligned communication with concise synthesis, claim-focused contradiction guardrails, bounded technical snapshot wording, stronger human-language glosses, explicit clarification of variables/fields/config keys/internal labels when answers depend on them, goal-qualified proposal wording for advisory future-work ideas, duplicate-looking team-agent reporting honesty, governing-basis clarification before deep branch analysis when multiple materially different policies/frames remain live, post-compact re-anchor wording for compacted-session continuation, memory-derived-context disclosure wording for path-matched remembered context, natural-professional wording guidance, direct human-readable action/result wording preference over metaphor-heavy internal shorthand, explicit main-point-first operational framing for diagnosis/test/recommendation/proposal/update answers, scoped local-fact treatment for exact environment values in snapshots, continuation-first execution guidance, explicit recommendation-plus-reason wording that preserves alternatives when multiple next paths genuinely remain open, and active-summary guidance that keeps resolved topics available for reasoning without repeating them as current issues by default |
| 2 | answer-presentation.md | answer-presentation.design.md v1.22 | Principle-first, trigger-driven presentation guidance for readable, orderly, and scannable output, including purpose-first framing near the start of diagnosis/test/recommendation/proposal/update answers, compact goal-review presentation support, light readable tables when helpful, compact governing-basis clarification blocks, compact post-compact re-anchor blocks, compact memory-status blocks, narrower next-stage blocks that do not interrupt active execution, compact variable-role structures, and compact proposal layouts that distinguish advisory future-work ideas from queued execution |
| 3 | anti-mockup.md | anti-mockup.design.md v1.1 | Real systems over mocks |
| 4 | anti-sycophancy.md | anti-sycophancy.design.md v1.4 | Truth over pleasing with evidence-grounded, claim-focused disagreement |
| 5 | artifact-initiation-control.md | artifact-initiation-control.design.md v1.4 | Startup-governance owner that resolves design/changelog/TODO/phase/patch posture before meaningful governed work drifts, initializes live task tracking early when non-trivial work needs visible execution state, treats phase-backed live task tracking as expected startup behavior, keeps initialized live task lists as the continuing surface for the active objective, and keeps patch non-default during greenfield startup unless a real before/after review surface exists |
| 6 | authority-and-scope.md | authority-and-scope.design.md v2.3 | User authority, deterministic precedence, fresh-directive override behavior, a rule against unnecessary option branching when one safe continuation path already exists, advisory future-work boundaries, RULES-first-over-memory authority, memory-governance deferral plus current-scope-wins protection, user-owned governing-basis selection, post-compact active-frame preservation, team-expansion boundaries, deferral of discussion-vs-execution mode selection to the first-class execution-continuity owner, and deferral of shared-board multi-session coordination semantics to the first-class shared execution coordination owner |
| 7 | custom-agent-selection-priority.md | custom-agent-selection-priority.design.md v1.1 | First-class owner for preferring visible user custom agents as the primary specialist pool when task fit is clear, while reusing an existing matching teammate before spawning another overlapping role |
| 8 | dan-safe-normalization.md | dan-safe-normalization.design.md v1.2 | Normalize jailbreak-style wrappers into bounded intent evaluation |
| 9 | document-consistency.md | document-consistency.design.md v1.6 | Cross-reference validation with portable shared references, source-side references, destination/runtime references, local execution paths, and local or machine-scoped values kept distinct so tool-local paths do not silently become reusable source contracts |
| 10 | document-changelog-control.md | document-changelog-control.design.md v4.7 | Chain authority, metadata, and synchronization contract |
| 11 | document-design-control.md | document-design-control.design.md v1.8 | Active-state design-body standards |
| 12 | document-patch-control.md | document-patch-control.design.md v2.5 | Patch governance, metadata, lifecycle, explicit before/after patch meaning, comparison-friendly patch representation, and the boundary that patch is normally downstream of an established before-state rather than the default startup artifact |
| 13 | emergency-protocol.md | emergency-protocol.design.md v1.1 | High-signal emergency response |
| 14 | evidence-grounded-burden-of-proof.md | evidence-grounded-burden-of-proof.design.md v1.3 | First-class owner for evidence taxonomy, burden-of-proof thresholds, contradiction protocol, scoped negative-evidence semantics, unresolved governing-basis uncertainty handling when materially different policies/frames would change the answer, remembered path-matched context as a distinct evidence/claim state, and post-compact needs-recheck handling for compacted carry-forward exact detail |
| 15 | explanation-quality.md | explanation-quality.design.md v2.16 | Plain-language-first, layered analytical and technical explanation structure with variable/field clarification, direct human-readable translation of architecture-first wording, a purpose-first explanation step, continued comparison/list-first support, explicit deferral of continuation-vs-option policy to accurate-communication, a governing-basis clarification boundary, a compact post-compact re-anchor boundary, goal-qualified proposal framing, and explicit deferral of goal-review semantics to the first-class goal-set owner |
| 16 | external-verification-and-source-trust.md | external-verification-and-source-trust.design.md v1.0 | First-class owner for proactive external verification, source-trust ranking, corroboration, and source-conflict handling |
| 17 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md v1.1 | Text diagrams without frames or boxes |
| 18 | functional-intent-verification.md | functional-intent-verification.design.md v1.1 | Clarify destructive/expensive intent before execution |
| 19 | memory-governance-and-session-boundary.md | memory-governance-and-session-boundary.design.md v1.3 | First-class owner for memory role boundaries, root `MEMORY.md` index-only behavior, `global/path/archive` taxonomy, path-primary applicability, session provenance, canonical `SCOPE.md`, archive-inactive lifecycle semantics, and optional-extension recall guidance that keeps memsearch-style layers supplemental, availability-checked, and subordinate to stronger execution evidence |
| 20 | no-variable-guessing.md | no-variable-guessing.design.md v1.3 | Read before reference with inspected-scope local evidence discipline |
| 21 | operational-failure-handling.md | operational-failure-handling.design.md v1.2 | Profile-driven operational failure classification, bounded retry policy, honest cooldown/escalation behavior, and an inspect-first case for duplicate-looking or stale team-agent presence |
| 22 | phase-implementation.md | phase-implementation.design.md v2.14 | First-class semantic standard for phased execution planning with early phase-establishment bridge, current-phase-first live task-list linkage, explicit phase-to-patch linkage when patch is in scope, same-objective task-list continuity across repeated slices, bounded next-work discovery from the active phase workspace when the task list alone is insufficient, default visible session-state grammar for session-owned task-list work, distinct request-layer vs held-owner title forms for phase-linked execution work, deferral of shared-board coordination protocol details to the first-class coordination owner, and explicit receiving-side phase remap during cross-session handoff |
| 23 | project-documentation-standards.md | project-documentation-standards.design.md v2.23 | Repository-level document-role model plus startup artifact gate, explicit patch-linkage verification for phased work, a clarified live-task-list-vs-durable-TODO tracking split, same-objective live task-list continuity at the repository-model layer, explicit execution-discovery surface recognition during active execution, default visible session ownership for session-owned task-list work, explicit deferral of shared-board multi-session coordination semantics and session-state title grammar to the coordination owner, explicit separation between shared-board request naming and receiving-side execution phase structure, non-default startup patch posture for greenfield baseline formation, portable public onboarding/install guidance by default, portable-by-default package-local support assets when they are reusable source content, support-layer modeling for the optional `plugin/**` extension package area, and current coordination-companion integration references |
| 24 | recovery-contract.md | recovery-contract.design.md v1.5 | No dead-end constrained/refused responses |
| 25 | refusal-classification.md | refusal-classification.design.md v1.4 | Deterministic refusal taxonomy |
| 26 | refusal-minimization.md | refusal-minimization.design.md v1.5 | Prefer recoverable paths over premature refusal |
| 27 | safe-file-reading.md | safe-file-reading.design.md v1.3 | Plan-before-read file safety |
| 28 | safe-terminal-output.md | safe-terminal-output.design.md v1.3 | Plan-before-execute output safety |
| 29 | strict-file-hygiene.md | strict-file-hygiene.design.md v1.3 | Prevent junk files and duplicates while deferring to required governed startup artifacts and avoiding machine-local hardcoded defaults in reusable artifacts |
| 30 | todo-standards.md | todo-standards.design.md v2.12 | Durable TODO governance with startup-establishment bridge, current-phase-first built-in task-list usage for non-trivial live execution tracking, same-objective reuse/append retention, completed-task visibility until closure, task-list-first next-work discovery with bounded fallback to broader execution surfaces, default visible session ownership for session-owned work, explicit request-style / held-owner / blocked-owner title forms, and deferral of broader session-state grammar ownership to the first-class coordination owner |
| 31 | runtime-topology-control.md | runtime-topology-control.design.md v1.1 | Bounded runtime mutation posture with inspect-before-mutate discipline |
| 32 | unified-version-control-system.md | unified-version-control-system.design.md v1.2 | UDVC-1 controller-level governance view |
| 33 | tactical-strategic-programming.md | tactical-strategic-programming.design.md v1.2 | Tactical entry, strategic target, convergence path, strategic closure doctrine, and anti-hardcoding tactical-boundary discipline |
| 34 | natural-professional-communication.md | natural-professional-communication.design.md v1.2 | First-class doctrine for natural professional communication, including rejection of metaphor-heavy or management-style abstraction when direct human-readable wording would be clearer and explicit purpose-before-detail wording for operational answers |
| 35 | portable-implementation-and-hardcoding-control.md | portable-implementation-and-hardcoding-control.design.md v1.2 | First-class owner for portable implementation defaults, portable-by-default support/package source artifacts, public onboarding/install portability, late-bound environment resolution, scoped local observations, and anti-hardcoding discipline |
| 36 | zero-hallucination.md | zero-hallucination.design.md v1.3 | Verified information only with fact/inference/hypothesis separation and scoped non-finding discipline |
| 37 | high-signal-communication.md | high-signal-communication.design.md v1.1 | Bounded supplementary high-signal filtering that trims low-value extra content and repeated wording while deferring required-content ownership to the existing communication, explanation, and presentation chains |
| 38 | execution-continuity-and-mode-selection.md | execution-continuity-and-mode-selection.design.md v1.2 | First-class owner for discussion-vs-execution mode selection, continuous-execution defaults, active next-work discovery from execution surfaces, legitimate stop gates, the boundary that milestone reporting must not replace continued execution, and bounded deferral of shared-board coordination protocol details to the first-class coordination owner |
| 39 | goal-set-review-and-priority-balance.md | goal-set-review-and-priority-balance.design.md v1.0 | First-class owner for continuous goal-set review, structure-first priority balance, and protection against single-subtask fixation so work on A does not crowd out B and C |
| 40 | shared-execution-coordination.md | shared-execution-coordination.design.md v1.4 | First-class owner for shared execution coordination and the default session-state title grammar for session-owned task-list work, including visible session ownership across usage modes, request vs held vs blocked title forms, session lease/handoff lifecycle, request-layer vs execution-layer separation, receiving-side phase ownership, continuity-first retention, retention matrix semantics, availability-first memsearch intake with immediate fallback, and future-optional peer-messaging boundaries |

### 3.2 Category View

| Category | Rules | Purpose |
|----------|-------|---------|
| Accuracy & Truth | accurate-communication, evidence-grounded-burden-of-proof, external-verification-and-source-trust, zero-hallucination, anti-sycophancy, no-variable-guessing, memory-governance-and-session-boundary | Evidence-grounded, verified, scope-aware, memory-aware, and honest output |
| Portable Implementation | portable-implementation-and-hardcoding-control, no-variable-guessing, project-documentation-standards, tactical-strategic-programming | Portable defaults, public onboarding/install portability, late-bound environment resolution, and anti-hardcoding discipline for shared artifacts |
| Presentation & Readability | answer-presentation, explanation-quality, flow-diagram-no-frame, natural-professional-communication, high-signal-communication | Readable, orderly, scannable, naturally professional, and higher-signal output presentation |
| Output Safety | safe-file-reading, safe-terminal-output, flow-diagram-no-frame, strict-file-hygiene | Output flood prevention, safe text presentation, and file hygiene |
| Startup Governance | artifact-initiation-control, project-documentation-standards, todo-standards, phase-implementation | Resolve artifact posture before meaningful governed work drifts |
| User Control | authority-and-scope, custom-agent-selection-priority, emergency-protocol, functional-intent-verification, operational-failure-handling, refusal-classification, recovery-contract, runtime-topology-control, execution-continuity-and-mode-selection, shared-execution-coordination | Preserve user authority, correct mode selection, coordinate shared execution boards across sessions, and maintain safe operational posture |
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
- required artifacts may be reused, created now, asked about now, or marked not required
- startup establishment is distinct from later content synchronization order

### 4.4 Phase Planning Contract
The active phase-planning contract is:
- `phase-implementation.md` is the semantic authority for phased execution planning
- `artifact-initiation-control.md` decides whether `/phase` must be established before drift
- `phase/SUMMARY.md` is the governed summary/index for live phased execution
- executable phase files under `phase/` use `NNN` for major phases and `NNN-NN` for subphases
- patch docs remain separate governed patch/review artifacts outside the live phase workspace
- phased work with governed patch artifacts must declare that linkage explicitly in `phase/SUMMARY.md` and relevant child phase files

### 4.5 Memory Governance Contract
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
- [ ] Design docs remain active target-state guidance only
- [ ] Changelog remains version authority per chain
- [ ] TODO remains execution-only
- [ ] Startup artifact posture is resolved before meaningful governed work drifts
- [ ] Phase docs remain in `/phase` and use the active `NNN` / `NNN-NN` identity model
- [ ] Patch docs remain outside live phase planning
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
- `strict-file-hygiene.md`

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
