# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 10.04
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-13)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

This active-state model must preserve UDVC-1 while keeping the active RULES system readable, source-owned, and evidence-grounded.

Current model focus:
- runtime rules are active behavior contracts with body-sufficient root files
- design files hold target-state truth and may use compact parent indexes with governed child shards for large active designs
- active parent changelogs remain version authority and may point to chain-scoped version detail shards, while TODO and phase stay compact current-state entrypoints
- broad raw evidence should be filtered through workers before it burdens the leader session when the task shape is context-heavy
- standing-role worker and teammate reuse should carry across phases when responsibility remains materially the same
- active governance docs should avoid God-line history dumps, route bulky same-chain changelog detail into parent-mapped version shards, repair clear low-risk touched God-line candidates, prevent God-file role overload, and route detected God artifact pressure into repair or visible planning
- startup, phase, patch, verification, portability, memory, audience-surface, and release boundaries stay with their dedicated owners

---

## 2) Active Repository Model

### 2.1 Layer Roles

| Layer | Primary Artifacts | Active Role |
|------|--------------------|-------------|
| Overview | `README.md` | Repository overview and usage guidance only |
| Runtime | root `*.md` rules | Active runtime behavior |
| Design | `design/*.design.md`, `design/<slug>/*.design.md` | Active target-state guidance with compact parent indexes and governed active child shards for large designs; no default `design/done/` surface |
| Phase | `phase/SUMMARY.md`, `phase/history/*.md`, `phase/phase-NNN-<phase-name>.md`, `phase/phase-NNN-NN-<subphase-name>.md`, `phase/done/phase-NNN-*.md` | Compact governed live phase-planning summary/index and execution detail, with referenced inactive daily/pre-rollover history under `phase/history/` and completed phase history under `phase/done/` |
| Patch | `patch/<context>.patch.md`, `patch/done/<context>.patch.md`, or root `<context>.patch.md` | Governed active patch/review artifacts plus inactive completed patch history outside live phase planning |
| History | `changelog/*.changelog.md`, `changelog/<chain>/v*.changelog.md`, `changelog/done/*.changelog.md` | Active parent changelog current-version authority, indexed chain-scoped version detail, plus legacy/archive/fallback inactive history when needed |
| Execution | `TODO.md`, `todo/history/*.md`, `todo/done/*.md` | Compact active execution tracking plus referenced inactive history/detail shards |
| Support | `phase-implementation-template.md`, `support/**/*.md` | Root-level helper templates and reference-only/support materials inside RULES only |

### 2.2 Governance Principle

This repository uses one deterministic governance model:
- README is overview-only
- runtime rules are the active rule layer and README-listed active runtime files must carry substantive behavior bodies, not metadata-only design pointers
- evidence-seeking proof-aware reasoning grounds substantial analysis, design, recommendation, agreement, and disagreement in practical checked evidence when material, while ordinary evidence remains reasoning support unless it is a hard constraint, authoritative requirement, safety boundary, or verified contradiction
- native worker-agent routing and context control keeps pasted technical evidence tied to the user’s active intent before project exploration, routes broad/noisy/high-context/multi-surface/high-output and broad research/design-improvement/source-heavy work by required worker capability, maps broad research objectives into focused research lanes before leader raw source absorption, prefers standalone subagent lanes for broad independent work, keeps Agent Team workflow as an exceptional coordination escalation, and lets custom-agent selection choose the best available specialist only after routing decides the worker path
- P081-02 remains the completed v9.87 native-worker-routing family refinement: it keeps the active runtime count at 44 while improving subagent research orchestration, external source-trust handoff quality, execution-continuity routing for broad research, and TODO tracking-friction recovery for bounded worker lanes
- P073-10 is the completed v9.88 runtime body-sufficiency corrective wave: it keeps the active runtime count at 44 while re-materializing 10 metadata-only root runtime files, adding controller/documentation/consistency validation so design/changelog metadata cannot substitute for installed runtime behavior, and verifying source/runtime parity plus body sufficiency 44/44 with destination extras observed-only
- P075-02 is the completed v9.89 roadmap-aware completion refinement: it keeps the active runtime count at 44 while teaching closeout to recommend supported next phases/waves from checked roadmap surfaces after true objective completion, preserving selected safe continuation and keeping unselected future work advisory
- P075-03 is the completed v9.90 goal-first working-frame refinement: it keeps the active runtime count at 44 while teaching non-trivial work to use proportional goal/output/gate navigation, triggered visible goal framing, continuation-first execution, and evidence-grounded next-goal recommendations without rigid template behavior
- P085-01 is the completed v9.91 refinement: it raises the source-owned active runtime set to 45 by adding `audience-surface-disclosure-control.md`, clarifies readiness-versus-completion wording, README current-state sync, memory index hygiene, mechanism-first coordination design, and direct-user-transparent audience-surface disclosure control, verifies source/runtime install parity plus body sufficiency 45/45 with destination extras observed-only, pushes `master`, and publishes GitHub release `v9.91`
- P087-01 is the completed v9.92 refinement: it raises the source-owned active runtime set to 46 by adding `governed-document-rollover-control.md`, keeps `TODO.md` and `phase/SUMMARY.md` compact as active current-state entrypoints, preserves pre-rollover snapshots, verifies source/runtime install parity plus body sufficiency 46/46 with destination extras observed-only, pushes `master`, and publishes GitHub release `v9.92`
- P088 is the completed v9.93 refinement: it keeps the source-owned active runtime set at 46, updates `memory-governance-and-session-boundary.md` to v1.7, compacts active root `MEMORY.md` into `Scope` plus `Memory base` path sections with visible relative hooks, verifies source/runtime install parity plus body sufficiency 46/46 with destination extras observed-only, pushes `master`, and publishes GitHub release `v9.93`
- P086 is the completed v9.94 constructive dissent and anti-over-agreement refinement: it keeps the source-owned active runtime set at 46, updates `anti-sycophancy.md` to v1.7, adds proposal evaluation before agreement-shaped wording, separates safe user direction from factual or quality endorsement, verifies source/runtime install parity plus body sufficiency 46/46 with destination extras observed-only, pushes `master`, and publishes GitHub release `v9.94`
- P076-04 is the completed v9.95 bounded main/subphase boundary refinement: it keeps the source-owned active runtime set at 46, updates `phase-implementation.md` to v2.32, requires subphase selection to preserve bounded goal/output/gate meaning rather than relying only on same-domain or historical-family evidence, adds phase-saturation and umbrella-escape signals, verifies source/runtime install parity plus body sufficiency 46/46 with destination extras observed-only, pushes `master`, and publishes GitHub release `v9.95`
- P089 is the completed v9.96 governed design sharding compact-index refinement: it keeps the source-owned active runtime set at 46, updates `document-design-control.md` to v1.11, `project-documentation-standards.md` to v2.38, `safe-file-reading.md` to v1.6, and `document-consistency.md` to v1.10 so large active designs can use compact parent indexes plus governed active child shards; runtime install plus source/runtime parity and body sufficiency passed 46/46 with destination extras observed-only, `master` was pushed, and GitHub release `v9.96` is published
- P090 is the completed v9.97 context-load and document-density control wave.
  - It raises the source-owned active runtime set to 47 by adding `context-load-and-document-density-control.md`.
  - It connects:
    - leader-context protection and worker-first broad raw evidence filtering
    - aggregate read-burst awareness and God-line prevention
    - append-vs-restructure gates, density-aware verification, and compact/thrash repair signals
  - Runtime install and 47/47 parity/body-sufficiency passed; `master` was pushed and GitHub release `v9.97` is published.
- P090-01 is the completed v9.98 opportunistic God-line repair refinement.
  - It keeps the source-owned active runtime set at 47 and advances `context-load-and-document-density-control` to v1.1.
  - It requires clear low-risk touched active-doc God-line candidates to be repaired in the same edit.
  - Broad, history-heavy, ambiguous, or meaning-risky density repairs are flagged or planned instead of silently rewritten.
  - Runtime install, 47/47 parity/body-sufficiency, density review, `master` push, and GitHub release `v9.98` verification passed.
- P091 is the released v9.99 governed document God-file prevention and repair wave.
  - It keeps the source-owned active runtime set at 47.
  - It adds document-capacity gates and role-aware repair routes across design, changelog, TODO, phase, patch, README, and active summary surfaces.
  - It advances the project-documentation, context-load, design, changelog, TODO, phase, patch, rollover, and consistency owner chains.
  - Runtime install, 47/47 parity/body-sufficiency, density/God-file review, `master` push, and GitHub release `v9.99` verification passed.
- P092 is the released v10.00 automatic God artifact planning and controlled repair wave.
  - It keeps the source-owned active runtime set at 47.
  - It turns detected touched-scope God pressure into action-mode routing, safe repair, visible repair planning, or closeout blocking.
  - It advances context-load, execution-continuity, startup, consistency, documentation, phase, TODO, patch, and rollover owner chains.
  - Runtime install, 47/47 parity/body sufficiency, density/God-artifact automation review, `master` push, and GitHub release `v10.00` verification passed.
- P096-01 is the completed v10.04 changelog chain version detail shard wave.
  - It keeps the source-owned active runtime set at 47.
  - It advances `document-changelog-control` to v4.12, `project-documentation-standards` to v2.41, `document-consistency` to v1.15, `safe-file-reading` to v1.8, and `context-load-and-document-density-control` to v1.6.
  - It makes `changelog/<chain>.changelog.md` the active parent changelog authority and `changelog/<chain>/vX.YY-short-topic.changelog.md` the indexed same-chain detail surface when large version detail needs sharding.
  - It keeps `changelog/done/` as legacy/archive/fallback history rather than the default ordinary same-chain detail namespace.
  - Runtime install, 47/47 source/runtime parity, source/destination active runtime body sufficiency, density review, push, and GitHub release `v10.04` verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.04
  - Release target and tag point to commit `3fa3935e2c7d12d474e8d8d3652ffde9997074c7`.
  - Published at `2026-05-13T16:53:38Z`.
- P095 is the released v10.03 standing-role worker reuse and audit boundary wave.
  - It keeps the source-owned active runtime set at 47.
  - It promotes standing-role worker/teammate reuse, phase-ID-as-context, lifecycle audit, scoped state evidence, and responsibility-based lane naming into Main RULES.
  - It advances `native-worker-agent-routing-and-context-control` to v1.7.
  - Plugin-owned shared-board/session/tmux mechanics remain outside Main RULES required behavior.
  - Runtime install, 47/47 source/runtime parity, and source/destination active runtime body sufficiency passed.
  - P095-specific density/God-artifact review passed; broader master governance density rollover remains deferred.
  - `master` push and GitHub release `v10.03` verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.03
  - Release target and tag point to commit `d5d7f1dbd3f16a1159f308e67b577878784f0356`.
  - Published at `2026-05-12T22:23:41Z`.
- P094 is the released v10.02 edit-capable governed-document repair delegation wave.
  - It keeps the source-owned active runtime set at 47.
  - It extends worker-first governance from filtered reads into bounded native edit-capable repair for governed documents.
  - Delegated repair must be explicit, non-overlapping, meaning-preserving, and leader-verifiable before final claims.
  - It advances `native-worker-agent-routing-and-context-control` to v1.6, `context-load-and-document-density-control` to v1.5, and `document-consistency` to v1.14.
  - Runtime install, 47/47 source/runtime parity, source/destination active runtime body sufficiency, and density/God-artifact review passed.
  - `master` push and GitHub release `v10.02` verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.02
  - Release target and tag point to commit `3c41b85cab832d197cb65e7a9661127fbf8f9e1c`.
  - Published at `2026-05-12T14:38:36Z`.
- P093 released v10.01 as the worker-first aggregate-read gate release wave.
  - It keeps the source-owned active runtime set at 47.
  - It turns broad governance/code aggregate reads into worker-first behavior before leader raw absorption unless a narrow direct-handling exception is stated.
  - It advances native-worker routing, context-load, safe-file-reading, execution-continuity, and document-consistency owner chains.
  - Runtime install, source/runtime parity, body sufficiency, and density/God-artifact review passed.
  - `master` push and GitHub release `v10.01` verification passed.
- maintainable code structure and decomposition gives coding-time work a first-class owner for responsibility boundaries, future changeability, code-smell triggers, smallest useful decomposition, helper-function necessity, useful source-code comments, God function/file pressure, wrong-abstraction avoidance, behavior-preserving refactor posture, and tactical structure-debt convergence without rigid architecture templates
- development verification and debug strategy gives non-trivial coding work a first-class owner for proportionate debug signal selection, testing depth, TestKit/scenario decisions, fake/local versus live evidence boundaries, and coding closeout that does not treat edits as proof
- active runtime rule compression must preserve semantic parity and should start from a complete patch inventory/baseline before any rule-body rewrite begins
- repository-level compression record sync should describe completed runtime slices without turning governed planning surfaces into compression targets, without mass-bumping per-rule chains automatically, without claiming runtime install before that separate gate passes, and with runtime install/parity recorded only after that explicit gate is executed; P073-09 remains the completed compression refresh for the then-43-file active runtime set, with final source metrics 35,017 words / 7,944-word reduction and 43/43 source/runtime parity
- shared runtime destination co-location is not ownership authority; destination/runtime files outside the current source-owned install set require owner/project scope resolution before classification, cleanup, or deletion is considered, and adjacent documentation/hygiene/reference owners preserve that boundary without turning shared-destination co-location into ownership
- design docs hold active target-state guidance, may use compact parent indexes plus governed active child shards for large designs, and do not use a default `design/done/` pattern
- `TODO.md` is the compact active execution-tracking entrypoint, while `todo/history/` and `todo/done/` hold referenced inactive history/detail when rollover moves old bulk out of active scans
- `phase/` is the live phased execution layer when staged planning is used
- `phase/SUMMARY.md` is the compact active phase roadmap/index, while `phase/history/` and `phase/done/` hold referenced inactive movement/snapshot/detail history
- `phase/done/` is inactive-by-default completed phase history
- phase IDs use `NNN` for major phases and `NNN-NN` for subphases
- before opening a new major phase, `phase-implementation.md` checks lineage and selects current-phase update, existing-family subphase, new major phase, or ask-now/recorded lineage posture
- P076-03 phase-visible task linkage requires non-trivial phase-backed live task entries to visibly point to active or clearly implied phase context in the subject or description while the phase files remain the phase authority
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

The active runtime inventory contains 47 source-owned root rule files.

| # | Rule | Design Doc | Purpose |
|---|------|------------|---------|
| 1 | accurate-communication.md | accurate-communication.design.md v2.22 | Evidence-honest communication for status, recommendations, agreement/disagreement, memory/post-compact context, phase closeout, and continuation wording |
| 2 | answer-presentation.md | answer-presentation.design.md v1.28 | Principle-first, trigger-driven presentation guidance for readable, orderly, and scannable output, including purpose-first framing, compact goal-aware working-frame layout for non-trivial work, roadmap-aware completion shape for next phase/wave/goal recommendations, optional deep-dive offers for easy-first answers, compact phase-backed closeout layout, and advisory proposal layouts that distinguish future-work ideas from queued execution |
| 3 | anti-mockup.md | anti-mockup.design.md v1.2 | Real systems over mocks with clear proof boundaries for mock/stub use |
| 4 | anti-sycophancy.md | anti-sycophancy.design.md v1.7 | Evidence-seeking proof-aware agreement, disagreement, recommendation, design, and constructive-dissent posture: truth over pleasing, user proposals evaluated for fit/cost/risk/timing/evidence/trade-offs/dependencies/alternatives before agreement-shaped wording, safe user direction accepted without factual or quality endorsement, ordinary evidence stays grounding input unless it creates a hard constraint, and corrections remain claim-focused when contrary evidence exists |
| 5 | artifact-initiation-control.md | artifact-initiation-control.design.md v1.9 | Startup-governance owner that resolves required artifacts early and resolves God artifact repair posture when safe in-place repair is not enough |
| 6 | authority-and-scope.md | authority-and-scope.design.md v2.5 | User authority, deterministic precedence, repo-governed semantic-authority precedence over git-state cleanup heuristics, runtime co-location as non-ownership authority, owner/project scope resolution before destination/runtime file classification or cleanup outside the current source-owned install set, fresh-directive override behavior, a rule against unnecessary option branching when one safe continuation path already exists, advisory future-work boundaries, RULES-first-over-memory authority, memory-governance deferral plus current-scope-wins protection, user-owned governing-basis selection, post-compact active-frame preservation, team-expansion boundaries, and deferral of discussion-vs-execution mode selection to the first-class execution-continuity owner |
| 7 | custom-agent-selection-priority.md | custom-agent-selection-priority.design.md v1.3 | First-class owner for preferring the best visible custom/specialist agent after native worker routing has classified user intent, identified the needed worker capability, and selected a direct/subagent/multi-subagent/team scale; it selects capability-fit specialists without becoming the owner of worker-scale routing, leader-context control, or Agent Team escalation |
| 8 | dan-safe-normalization.md | dan-safe-normalization.design.md v1.3 | Normalize jailbreak-style wrappers into bounded intent evaluation |
| 9 | document-consistency.md | document-consistency.design.md v1.15 | Cross-reference/no-drift validation, parity/body checks, God checks, worker-gate compliance, and delegated-repair preservation checks |
| 10 | document-changelog-control.md | document-changelog-control.design.md v4.12 | Changelog version authority, current navigation, inactive `changelog/done/`, and changelog God-file prevention |
| 11 | document-design-control.md | document-design-control.design.md v1.12 | Active-state design standards, compact design indexes, governed child shards, and Design God-file prevention |
| 12 | document-patch-control.md | document-patch-control.design.md v2.9 | Patch governance, before/after review meaning, inactive `patch/done/`, God Patch prevention, and automatic God Patch handling |
| 13 | emergency-protocol.md | emergency-protocol.design.md v1.2 | High-signal emergency response |
| 14 | evidence-grounded-burden-of-proof.md | evidence-grounded-burden-of-proof.design.md v1.6 | First-class owner for evidence-seeking proof-aware reasoning, evidence taxonomy, ordinary-evidence-versus-binding-constraint thresholds, burden-of-proof thresholds for factual endorsement and contradiction, user-owned preference/direction separation, contradiction protocol, scoped negative-evidence semantics, unresolved governing-basis uncertainty handling when materially different policies/frames would change the answer, remembered path-matched context as a distinct evidence/claim state, post-compact needs-recheck handling for compacted carry-forward exact detail, and explicit limits on using git-state evidence for disposal conclusions |
| 15 | explanation-quality.md | explanation-quality.design.md v2.23 | Plain-language-first, proof-aware, layered analytical and technical explanation structure that preserves proportional goal/output/gate framing when non-trivial work benefits from it, keeps easy-first answers complete without becoming overlong, explains roadmap-aware next phase/wave/goal recommendations at true closeout, offers one optional deeper-detail path when useful, and keeps evidence, mechanism, implication, and continuation boundaries readable |
| 16 | external-verification-and-source-trust.md | external-verification-and-source-trust.design.md v1.2 | First-class owner for proactive external verification, source-trust ranking, corroboration, source-conflict handling, orchestrated broad external research lanes, and current external evidence grounding for recommendation/design judgments without turning ordinary external evidence into an automatic design lock |
| 17 | flow-diagram-no-frame.md | flow-diagram-no-frame.design.md v1.2 | Text diagrams without frames or boxes |
| 18 | functional-intent-verification.md | functional-intent-verification.design.md v1.2 | Clarify destructive/expensive intent before execution, including an explicit delete guard that blocks cleanup/isolation rationale from acting as deletion authorization |
| 19 | memory-governance-and-session-boundary.md | memory-governance-and-session-boundary.design.md v1.7 | First-class owner for memory role boundaries, root `MEMORY.md` active-index behavior, visible one-line hook preservation, `Scope` + `Memory base` relative path compaction for repeated path scopes, loader-warning and index-bloat maintenance triggers, fake-alias and link-only hidden-memory-router avoidance, `global/path/archive` taxonomy, path-primary applicability, session provenance, canonical `SCOPE.md`, archive-inactive lifecycle semantics, and generic optional external recall guidance that stays supplemental and subordinate to stronger execution evidence |
| 20 | native-worker-agent-routing-and-context-control.md | native-worker-agent-routing-and-context-control.design.md v1.7 | Intent-first worker routing, aggregate-read gating, bounded edit-capable governed-document repair delegation, standing-role worker/teammate reuse, and lifecycle audit before reuse/spawn/respawn/shutdown/overlap reporting |
| 21 | no-variable-guessing.md | no-variable-guessing.design.md v1.5 | Read before reference with inspected-scope local evidence discipline, including git-state observations kept in the weak local-evidence lane until governed repo surfaces are checked |
| 22 | operational-failure-handling.md | operational-failure-handling.design.md v1.2 | Profile-driven operational failure classification, bounded retry policy, honest cooldown/escalation behavior, and a Team Agent duplicate/stale-presence profile that treats duplicate-looking or stale team-agent presence as inspect-before-respawn rather than respawn-first churn |
| 23 | phase-implementation.md | phase-implementation.design.md v2.34 | Phase planning with bounded lineage, compact summaries, phase-visible tasks, verification gates, next-goal closeout, God Phase prevention, and automatic God Phase handling |
| 24 | project-documentation-standards.md | project-documentation-standards.design.md v2.41 | Repository document-role model for README, design, changelog, TODO, phase, patch, runtime install scope, God-file prevention, and automatic God artifact planning |
| 25 | recovery-contract.md | recovery-contract.design.md v1.6 | No dead-end constrained/refused responses |
| 26 | refusal-classification.md | refusal-classification.design.md v1.5 | Deterministic refusal taxonomy |
| 27 | refusal-minimization.md | refusal-minimization.design.md v1.6 | Prefer recoverable paths over premature refusal |
| 28 | safe-file-reading.md | safe-file-reading.design.md v1.8 | Bounded reads, shard-selective design reads, and worker-first aggregate-read gating |
| 29 | safe-terminal-output.md | safe-terminal-output.design.md v1.4 | Plan-before-execute output safety |
| 30 | strict-file-hygiene.md | strict-file-hygiene.design.md v1.5 | Prevent junk files and duplicates while deferring to required governed startup artifacts, blocking cleanup/hygiene wording from acting as deletion authority, keeping destination/runtime files outside the current source-owned install set from being treated as junk by shared-destination co-location alone, and avoiding machine-local hardcoded defaults in reusable artifacts |
| 31 | todo-standards.md | todo-standards.design.md v2.28 | Durable TODO governance with compact active entrypoints, referenced history/done shards, phase-visible tasks, TODO God-file prevention, and God artifact repair task planning |
| 32 | runtime-topology-control.md | runtime-topology-control.design.md v1.2 | Bounded runtime mutation posture with inspect-before-mutate discipline and mechanism-first coordination/runtime classification before topology or transport claims |
| 33 | unified-version-control-system.md | unified-version-control-system.design.md v1.3 | UDVC-1 controller-level governance view with active runtime body-sufficiency validation |
| 34 | tactical-strategic-programming.md | tactical-strategic-programming.design.md v1.3 | Tactical entry, strategic target, convergence path, strategic closure doctrine, anti-hardcoding tactical-boundary discipline, and explicit deferral of coding-time responsibility/decomposition quality to the maintainable code structure owner |
| 35 | natural-professional-communication.md | natural-professional-communication.design.md v1.3 | First-class doctrine for natural professional communication, including easy-explanation register support for plain Thai answers, rejection of metaphor-heavy or management-style abstraction when direct human-readable wording would be clearer, and explicit purpose-before-detail wording for operational answers |
| 36 | portable-implementation-and-hardcoding-control.md | portable-implementation-and-hardcoding-control.design.md v1.2 | First-class owner for portable implementation defaults, portable-by-default support/package source artifacts, public onboarding/install portability, late-bound environment resolution, scoped local observations, and anti-hardcoding discipline |
| 37 | zero-hallucination.md | zero-hallucination.design.md v1.6 | Verified information only, including practical evidence-seeking for material factual premises and verified factual endorsement before agreement with factual claims, while keeping fact/preference-direction/inference/hypothesis/uncertainty separation, scoped non-finding discipline, unsupported factual-endorsement risk, proof-aware uncertainty, and explicit limits on using git-state observations as disposal truth |
| 38 | high-signal-communication.md | high-signal-communication.design.md v1.3 | Bounded supplementary high-signal filtering that trims low-value extra content and repeated wording while preserving required goal/output/gate framing, supported next-goal recommendations, roadmap recommendations, optional deep-dive offers at true completion boundaries, and other owner-required content |
| 39 | execution-continuity-and-mode-selection.md | execution-continuity-and-mode-selection.design.md v1.18 | Execution continuity and broad-read worker gating |
| 40 | goal-set-review-and-priority-balance.md | goal-set-review-and-priority-balance.design.md v1.1 | First-class owner for continuous goal-set review, structure-first priority balance, goal-first working frames, outcome-first goal navigation, goal/output/gate semantics, goal hierarchy, triggered goal visibility, anti-ritual boundaries, anti-fixation, and evidence-grounded next-goal recommendations |
| 41 | technical-snapshot-communication.md | technical-snapshot-communication.design.md v1.0 | First-class owner for bounded technical snapshot wording, exact/partial/inferred separation, scoped local-fact snapshot communication, and concise diagnostic snapshot state reporting |
| 42 | response-closing-and-action-framing.md | response-closing-and-action-framing.design.md v1.3 | First-class owner for concise end-of-response synthesis, clear action framing, recommendation-with-reason wording, alternative preservation, closed-topic summary handling, phase-backed closeout synthesis, advisory goal-qualified proposal framing, roadmap-aware completion shape, optional deep-dive offers, and supported next phase/wave/goal recommendations at true completion boundaries |
| 43 | maintainable-code-structure-and-decomposition.md | maintainable-code-structure-and-decomposition.design.md v1.2 | First-class owner for coding-time maintainability as future changeability, responsibility boundaries by reason to change, code-smell triggers rather than verdicts, smallest useful decomposition, helper-function necessity, useful source-code comment discipline, God function/file pressure, wrong-abstraction guardrails, explicit dependency/state boundaries, behavior-preserving refactor posture, verification-strategy deferral to the development verification owner, and tactical structure-debt convergence without rigid line-count or architecture-template doctrine |
| 44 | development-verification-and-debug-strategy.md | development-verification-and-debug-strategy.design.md v1.1 | First-class owner for proportionate coding-time verification strategy, debug signal selection, testing depth, TestKit/scenario decisions, fake/local versus live evidence boundaries, and coding closeout that distinguishes prepared, configured, implemented, tested, verified-in-scope, runtime/live-verified, working, fixed, and stable states |
| 45 | audience-surface-disclosure-control.md | audience-surface-disclosure-control.design.md v1.0 | First-class owner for full direct-user/project-owner transparency plus audience-aware disclosure minimization for generated public, customer-facing, operator-facing, demo, log, release, onboarding, and externally shared artifacts |
| 46 | governed-document-rollover-control.md | governed-document-rollover-control.design.md v1.2 | Daily-first TODO/phase rollover, history/done references, God-document routing, and automatic rollover repair planning |
| 47 | context-load-and-document-density-control.md | context-load-and-document-density-control.design.md v1.6 | Context-load, doc density, aggregate-read gating, and delegated repair routing |

### 3.2 Category View

#### Accuracy & Truth

- Rules:
  - `accurate-communication`, `technical-snapshot-communication`, `evidence-grounded-burden-of-proof`
  - `external-verification-and-source-trust`, `zero-hallucination`, `anti-sycophancy`
  - `no-variable-guessing`, `memory-governance-and-session-boundary`
- Purpose: evidence-seeking, proof-aware, verified, scope-aware, and memory-aware output.
- Communication posture: honest, evidence-calibrated agreement/disagreement and snapshot-aware reporting.

#### Portable Implementation

- Rules: `portable-implementation-and-hardcoding-control`, `no-variable-guessing`, `project-documentation-standards`, `tactical-strategic-programming`.
- Purpose: portable defaults, public onboarding portability, late-bound environment resolution, and anti-hardcoding discipline.

#### Presentation & Readability

- Rules:
  - `answer-presentation`, `explanation-quality`, `response-closing-and-action-framing`
  - `flow-diagram-no-frame`, `natural-professional-communication`, `high-signal-communication`
  - `audience-surface-disclosure-control`
- Purpose: readable, orderly, scannable, naturally professional, well-closed, audience-aware, and higher-signal output.

#### Output Safety

- Rules: `context-load-and-document-density-control`, `safe-file-reading`, `safe-terminal-output`, `flow-diagram-no-frame`, `strict-file-hygiene`.
- Purpose: context-load lifecycle control, output flood prevention, safe text presentation, and file hygiene.

#### Startup Governance

- Rules: `artifact-initiation-control`, `governed-document-rollover-control`, `project-documentation-standards`, `todo-standards`, `phase-implementation`.
- Purpose: resolve artifact posture before meaningful governed work drifts.
- Active-entrypoint posture: keep large active entrypoints compact with referenced history/done shards.

#### User Control

- Rules:
  - `authority-and-scope`, `custom-agent-selection-priority`, `emergency-protocol`
  - `functional-intent-verification`, `operational-failure-handling`, `refusal-classification`
  - `recovery-contract`, `runtime-topology-control`, `execution-continuity-and-mode-selection`
- Purpose: preserve user authority, correct mode selection, and safe operational posture.
- Scope guard: re-check intent before project exploration when technical evidence could be misread.
- Specialist guard: prefer clear best-fit custom specialists after routing selects specialist handling.

#### Execution Strategy

- Rules:
  - `native-worker-agent-routing-and-context-control`, `context-load-and-document-density-control`
  - `goal-set-review-and-priority-balance`, `tactical-strategic-programming`
  - `maintainable-code-structure-and-decomposition`, `development-verification-and-debug-strategy`
- Purpose: route broad or high-output work through intent-first worker lanes.
- Goal posture: protect leader context, keep the full goal set visible, and preserve structure-first balance.
- Coding posture: keep code maintainable and require proportionate verification before strong completion claims.

#### Adversarial Workflow

- Rules: `refusal-minimization`, `dan-safe-normalization`.
- Purpose: reduce false refusals in authorized adversarial/security workflows.

#### Quality & Governance

- Rules:
  - `document-consistency`, `document-changelog-control`, `document-design-control`, `document-patch-control`
  - `governed-document-rollover-control`, `anti-mockup`, `unified-version-control-system`
- Purpose: documentation determinism, reference-role clarity, active entrypoint rollover, patch semantics, and governance quality.

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
- phase `create now` delegates identity selection to `phase-implementation.md`, where creation may resolve to current-phase update, existing-family subphase, new major phase, or ask-now lineage handling
- when the checked project/workstream is already clearly phase-shaped, live task creation should align to that staged structure and visibly expose active or implied phase context instead of defaulting to detached standalone tasks
- startup establishment is distinct from later content synchronization order

### 4.4 Phase Planning Contract
The active phase-planning contract is:
- `phase-implementation.md` is the semantic authority for phased execution planning
- `artifact-initiation-control.md` decides whether `/phase` must be established before drift
- clearly staged/governed work should not leave phase posture implicit until late backfill
- sufficiently clear governed design can be synthesized into phase execution order when staged execution is warranted
- `phase/SUMMARY.md` is the governed summary/index for live phased execution
- executable phase files under `phase/` use `NNN` for major phases and `NNN-NN` for subphases
- phase identity selection is lineage-first: update current phase, create an existing-family subphase, open a genuinely new major phase, or ask/record the lineage basis when ambiguity remains
- subphase selection must preserve the parent family's bounded goal/output/gate meaning; same product area, broad domain, owner chain, historical label, or old phase family is supporting evidence only and is not sufficient by itself
- new major phases are appropriate when work has its own capability boundary, output, verification gate, release boundary, rollback/containment boundary, or when the old phase family has become a misleading or saturated umbrella
- completed phase status does not automatically break lineage, and new concern wording alone does not justify a new major phase
- patch docs remain separate governed patch/review artifacts outside the live phase workspace
- phased work with governed patch artifacts must declare that linkage explicitly in `phase/SUMMARY.md` and relevant child phase files
- non-trivial phase-backed live task entries visibly link to active or clearly implied phase context while remaining execution pointers rather than phase authority

### 4.5 Completed Documentation Surface Contract
The active completed-history contract is:
- `phase/done/` may hold completed phase execution detail outside the active scan surface
- `patch/done/` may hold completed patch/review artifacts outside the active scan surface
- `changelog/done/` may hold older or completed detailed history outside the active scan surface
- `design/done/` is not a default governed design pattern because design remains active blueprint and target-state authority
- `done/` surfaces are inactive by default and are consulted for history, audit, rollback, provenance, or trace reconstruction only
- files in `done/` are not junk and completed status is not deletion authorization

### 4.6 Daily-First Rollover Contract
The active rollover contract is:
- `governed-document-rollover-control.md` is the semantic authority for oversized active governance entrypoint rollover
- `TODO.md` and `phase/SUMMARY.md` remain compact active current-state entrypoints rather than historical archive dumps
- daily-first `todo/history/` and `phase/history/` shards preserve daily movement and pre-rollover snapshots
- `todo/done/` and `phase/done/` preserve large completed/detail surfaces outside active scans when applicable
- main entrypoints must reference relevant history/done shards and shards must link back to their parent entrypoint
- rollover is preservation and reference movement, not deletion authority

### 4.7 Memory Governance Contract
The active memory-governance contract is:
- `memory-governance-and-session-boundary.md` is the semantic authority for memory role boundary, root-index visibility, and session/path applicability behavior
- root `MEMORY.md` remains present and acts as a compact active index, not a full content dump or link-only router
- active one-line hooks stay visible enough for startup context to understand why each memory may matter before opening detail files
- path-scoped sections with repeated long memory paths declare one canonical `Scope` and one `Memory base`, then list entries as relative paths under that base
- fake markdown aliases such as `path = path` are not valid memory-index compaction because links would resolve incorrectly
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
- [ ] Evidence-seeking proof-aware reasoning remains proportional, grounded in checked evidence when material, separated from unsupported factual endorsement and user-owned preference/direction, and prevented from turning ordinary evidence into a rigid decision lock
- [ ] Native worker routing remains intent-first, capability-based, and standalone-subagent-first for broad independent work, keeps Agent Team workflow exceptional, and keeps custom-agent selection as candidate selection after routing rather than routing ownership
- [ ] Maintainable code structure guidance remains principle-based: code smells trigger investigation, decomposition follows responsibility/changeability, wrong abstractions are avoided, and tactical structure debt has convergence
- [ ] Design docs remain active target-state guidance only and do not use a default `design/done/` surface
- [ ] Active changelogs remain version authority per chain while `changelog/done/` stays inactive history
- [ ] Direct-user transparency remains complete while generated public/operator/customer/log/demo/external surfaces use audience-appropriate disclosure boundaries
- [ ] TODO remains execution-only, with `TODO.md` as the compact active entrypoint and `todo/history/` / `todo/done/` as referenced inactive history/detail surfaces
- [ ] Root `MEMORY.md` remains meaning-visible while repeated path-scope bases are compacted through `Scope` and `Memory base` relative entries
- [ ] Startup artifact posture is resolved before meaningful governed work drifts
- [ ] Oversized active governance entrypoints use daily-first rollover instead of duplicating historical archive detail in the active current-state file
- [ ] Active phase docs remain in `/phase`, use the active `NNN` / `NNN-NN` identity model, and move completed detail to `phase/done/` only as inactive history
- [ ] Phase identity selection remains lineage-aware before a new major phase is opened
- [ ] Subphase selection preserves bounded goal/output/gate meaning rather than relying only on broad same-domain, owner-chain, or historical-family signals
- [ ] Phase saturation and umbrella-escape signals are considered before distinct work is kept inside an old major family
- [ ] Startup posture, live task shaping, repository documentation sync, and execution momentum do not silently allocate a new major phase or hide active/implied phase context from non-trivial phase-backed live tasks
- [ ] Active patch docs remain outside live phase planning while `patch/done/` stays inactive completed patch history
- [ ] Root helper and support artifacts remain non-governed

---

## 7) Integration

Related chains:
- `artifact-initiation-control.md`
- `audience-surface-disclosure-control.md`
- `governed-document-rollover-control.md`
- `document-changelog-control.md`
- `document-design-control.md`
- `phase-implementation.md`
- `project-documentation-standards.md`
- `document-patch-control.md`
- `todo-standards.md`
- `execution-continuity-and-mode-selection.md`
- `native-worker-agent-routing-and-context-control.md`
- `custom-agent-selection-priority.md`
- `maintainable-code-structure-and-decomposition.md`
- `strict-file-hygiene.md`

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
