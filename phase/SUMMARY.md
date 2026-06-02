# RULES Phase Summary

> **Current Version:** 2.05
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.35
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** No active phase selected; latest released baseline is v10.43 / P135 governed goal auto-plan-file authoring
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Daily History:** [history/2026-05-16.md](history/2026-05-16.md); [history/2026-05-08.md](history/2026-05-08.md)
> **Pre-Rollover Snapshot:** [history/2026-05-08-pre-rollover-SUMMARY.md](history/2026-05-08-pre-rollover-SUMMARY.md)
> **Completed Detail:** [done/released-phase-summary-archive.md](done/released-phase-summary-archive.md); [done/](done/)

---

## Current Purpose

This file is the compact active phase roadmap/index. Historical phase-map detail and released-phase rollout detail were compacted out of this entrypoint after P099 so active scans stay cheap.

Active scans should start here, then follow `history/` or `done/` links only when the current task needs completed detail or provenance.

---

## Active Phase Roadmap

### Active

- None currently selected. Latest released baseline is `v10.43 / P135`.

### Most Recently Completed

- **P135:** [phase-135-governed-goal-auto-plan-file-authoring.md](phase-135-governed-goal-auto-plan-file-authoring.md)
  - Output: governed `/goal` authoring now writes the route-only plan file first for non-trivial governed goals that need durable route support, then emits the final copied goal artifact with exact in-artifact `Plan reference`, while `/goal` remains the objective owner and the plan file remains route-only support.
  - Gate: auto-plan-file authoring integrity passed, no-save-plan-loop integrity passed, no-rerun-`/goal` loop integrity passed, `/goal` objective-ownership integrity passed, route-only plan-support integrity passed, touched design/changelog/README/TODO/phase/patch surfaces align to `v10.43 / P135`, `git diff --check` passed, and branch/default-branch/tag/release evidence now points to one promoted `v10.43` baseline.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.43
  - Patch: [../patch/governed-goal-auto-plan-file-authoring.patch.md](../patch/governed-goal-auto-plan-file-authoring.patch.md)

- **P134:** [phase-134-copyable-goal-plan-reference-hardening.md](phase-134-copyable-goal-plan-reference-hardening.md)
  - Output: governed `/goal` doctrine now requires any durable plan-backed route to keep `Plan reference` inside the same copied goal artifact, while `/goal` remains the objective owner and the plan file remains route-only support.
  - Gate: copyable goal plan-reference integrity passed, `/goal` objective-ownership integrity passed, route-only plan-support integrity passed, advisory `/goal` artifact template integrity passed, touched design/changelog/README/TODO/phase/patch surfaces align to `v10.42 / P134`, `git diff --check` passed, and branch/default-branch/tag/release evidence now points to one promoted `v10.42` baseline.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.42
  - Patch: [../patch/copyable-goal-plan-reference-hardening.patch.md](../patch/copyable-goal-plan-reference-hardening.patch.md)

- **P133:** [phase-133-quickstart-companion-plugin-setup.md](phase-133-quickstart-companion-plugin-setup.md)
  - Output: the root README now carries a Quick Start companion-plugin setup block that tells operators how to install `governed-docs` and `memory-context-intelligence` immediately after the runtime-rule install, while preserving the boundary that plugins still load separately from the active `.claude/rules/` payload.
  - Gate: Quick Start companion-plugin setup integrity passed, plugin/runtime boundary integrity passed, `memory-context-intelligence` first-use flow integrity passed, touched README/TODO/phase/patch/changelog surfaces align to `v10.41 / P133`, `git diff --check` passed, and branch/default-branch/tag/release evidence now points to one promoted `v10.41` baseline.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.41
  - Patch: [../patch/quickstart-companion-plugin-setup.patch.md](../patch/quickstart-companion-plugin-setup.patch.md)

- **P132:** [phase-132-companion-plugin-readmes-and-image-guidance.md](phase-132-companion-plugin-readmes-and-image-guidance.md)
  - Output: both requested plugin-local image assets now exist, both companion plugin READMEs have stronger orientation plus image references, and the root README now names the two companion plugins and what they help with while preserving the runtime/plugin boundary.
  - Gate: plugin-image-placement integrity passed, governed-docs README guidance/image integrity passed, memory-context-intelligence README guidance/image integrity passed, root README companion-plugin discovery integrity passed, touched README/TODO/phase/patch/changelog surfaces align to `v10.40 / P132`, `git diff --check` passed, and branch/default-branch/tag/release evidence now points to one promoted `v10.40` baseline.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.40
  - Patch: [../patch/companion-plugin-readmes-and-image-guidance.patch.md](../patch/companion-plugin-readmes-and-image-guidance.patch.md)

- **P131:** [phase-131-rules-diagram-infrastructure-doctrine.md](phase-131-rules-diagram-infrastructure-doctrine.md)
  - Output: `diagram/` is now required governed-docs infrastructure for RULES, governed diagram authority stays under `diagram/` only, `diagram/STRUCTURE.md` is the mandatory compact active whole-project diagram-side entrypoint, `diagram/STRUCTURE.md` owns concept/folder/topology/boundary/navigation mapping, and future `diagram/history/` / `diagram/done/` remain preservation infrastructure rather than cleanup authority.
  - Gate: required diagram-infrastructure integrity passed, diagram-authority-scope integrity passed, `diagram/STRUCTURE.md` ownership/navigation integrity passed, design-vs-diagram authority integrity passed, preservation-not-cleanup integrity passed, touched README/design/changelog/TODO/phase/patch surfaces align to `v10.39 / P131`, runtime install/update verification plus checked parity/body sufficiency passed, `git diff --check` passed, and branch/default-branch/tag/release evidence now points to one promoted `v10.39` baseline.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.39
  - Patch: [../patch/rules-diagram-infrastructure-doctrine.patch.md](../patch/rules-diagram-infrastructure-doctrine.patch.md)

- **P130:** [phase-130-always-on-plan-file-backed-goal-model.md](phase-130-always-on-plan-file-backed-goal-model.md)
  - Output: any actual governed `/goal` creation now prepares a full detailed plan file before final goal emission, emitted governed `/goal` output now references that route file through `Plan reference`, `/goal` remains the objective owner, the referenced plan file remains route-only support, and visible `/plan` remains explicit standalone planning, later route revision, or overflow only.
  - Gate: plan-first governed goal-authoring integrity passed, plan-reference compact-goal integrity passed, goal-vs-plan authority integrity passed, explicit-standalone-or-overflow-only `/plan` integrity passed, touched README/design/changelog/TODO/phase/patch surfaces align to `v10.38 / P130`, runtime install/update verification passed with 18 active runtime rules plus manifest, targeted source/runtime parity and source/destination body sufficiency for touched owners passed, `git diff --check` passed, and reconciled branch/default-branch/tag/release evidence now points to one promoted `v10.38` baseline.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.38
  - Patch: [../patch/always-on-plan-file-backed-goal-model.patch.md](../patch/always-on-plan-file-backed-goal-model.patch.md)


- **P129:** [phase-129-kroki-compatible-governed-diagram-doctrine.md](phase-129-kroki-compatible-governed-diagram-doctrine.md)
  - Output: governed `diagram/` source is now mandatory Kroki-compatible, allowed breadth is defined as Kroki-compatible + governance-suitable, `diagram/STRUCTURE.md` now acts as a bodyful whole-project detailed visual structure authority, subject diagrams are positioned as zoom-in / decomposition views of the global structure, and touched README/design/changelog/TODO/phase/patch surfaces are aligned to `v10.37 / P129`.
  - Gate: mandatory Kroki-compatible contract integrity passed, suitability/admission boundary integrity passed, design-vs-diagram authority integrity passed, inline-text-diagram boundary integrity passed, `diagram/STRUCTURE.md` bodyful whole-project authority integrity passed, `git diff --check` passed, and reconciled branch/default-branch/tag/release evidence now points to one promoted `v10.37` baseline.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.37
  - Patch: [../patch/rules-kroki-compatible-governed-diagram-doctrine.patch.md](../patch/rules-kroki-compatible-governed-diagram-doctrine.patch.md)
  - Historical note: this wave strengthens the RULES diagram lane contract only and does not reopen governed-docs implementation as an owner path.

### Previously Completed

- **P128:** [phase-128-rules-unified-diagram-doctrine-correction.md](phase-128-rules-unified-diagram-doctrine-correction.md)
  - Output: dedicated `diagram/` visual lane is now recognized in active owner docs, `diagram/STRUCTURE.md` is present as the whole-repo visual anchor, fragmented companion assumptions were withdrawn, touched README/design/changelog/TODO/phase/patch surfaces are aligned to `v10.36 / P128`, temporary project-local install proof passed for the touched runtime-owner surfaces, and the promoted state now mirrors onto the remote default branch.
  - Gate: design-vs-diagram authority boundary integrity passed, no touched active surface kept the old fragmented baseline as selected truth, `git diff --check` passed, temporary project-local install proof passed with 18 active runtime rule markdown files, touched runtime-owner parity matched for `document-governance.md` and `explanation-and-presentation.md`, and reconciled branch/default-branch/tag/release evidence now points to one promoted `v10.36` baseline.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.36
  - Patch: [../patch/rules-unified-diagram-doctrine-correction.patch.md](../patch/rules-unified-diagram-doctrine-correction.patch.md)
  - Historical note: this wave corrected doctrine before any future re-entry into tooling/plugin implementation and did not revive plugin-first execution as the default path.

### Previously Completed

- **P127:** [phase-127-readme-core-capabilities-list-and-doctrine-framing.md](phase-127-readme-core-capabilities-list-and-doctrine-framing.md)
  - Output: README Core Capabilities now use a readable doctrine-grounded list, Runtime Context Discipline stays front-page scoped, touched README/design/changelog/TODO/phase/patch sync is complete, runtime install into a checked project-local `.claude/rules/` target passed at 18/18 parity/body sufficiency, branch push completed, and GitHub release `v10.35` is published.
  - Gate: no grid/table capability block remains, no phase/execution chronology is used as capability meaning, front-page/doctrine framing integrity passed, non-runtime playground boundary remained intact, 18-file install-boundary preservation passed, `git diff --check` passed, branch push passed, remote default-branch verification passed, GitHub release verification passed, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.35
  - Patch: [../patch/readme-core-capabilities-list-and-doctrine-framing.patch.md](../patch/readme-core-capabilities-list-and-doctrine-framing.patch.md)
  - Historical note: this wave refines front-page capability presentation only; it does not turn README into a phase summary or reopen execution chronology as the explanation basis.

- **P126:** [phase-126-phase-grammar-forms-and-release-sync.md](phase-126-phase-grammar-forms-and-release-sync.md)
  - Output: explicit forward-valid `phase-NNN` / `phase-NNN-NN` / `phase-NNN-NN-NN` doctrine, legacy-only alphanumeric handling, touched master/design/changelog/TODO/phase/patch sync, runtime install into a checked project-local `.claude/rules/` target, 18/18 parity/body sufficiency, branch push, remote default-branch verification, and GitHub release `v10.34`.
  - Gate: explicit numeric phase-grammar integrity, explicit alphanumeric legacy-only integrity, no-rename/migration-in-wave integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, remote default-branch verification, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.34
  - Patch: [../patch/phase-grammar-forms-and-release-sync.patch.md](../patch/phase-grammar-forms-and-release-sync.patch.md)
  - Historical note: NodeClaw evidence drove the doctrine decision, but this release wave did not rename NodeClaw files; observed alphanumeric forms remain legacy-only until a later normalization wave is explicitly selected.

### Previously Completed

- **P125:** [phase-125-integrated-goal-planning-objective.md](phase-125-integrated-goal-planning-objective.md)
  - Output: touched runtime owners, one related playground/reference case update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch verification, and GitHub release `v10.33`.
  - Gate: integrated goal-surface integrity, automatic-when-necessary planning integrity, simple-goal direct-path integrity, subordinate-planning-support integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, remote default-branch verification, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.33
  - Published at `2026-05-30T15:59:23Z`.
  - Patch: [../patch/integrated-goal-planning-objective.patch.md](../patch/integrated-goal-planning-objective.patch.md)
  - Historical note: P124 remains an unreleased predecessor draft preserved as context for the narrower pre-goal plan-backed stage that led into this released model.

### Previously Completed

- **P123:** [phase-123-goal-internal-subagent-assistance-refinement.md](phase-123-goal-internal-subagent-assistance-refinement.md)
  - Output: touched runtime owners, one related playground/reference case update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch verification, and GitHub release `v10.31`.
  - Gate: objective-vs-route integrity, internal-helper-only subagent integrity, conditional agent-use integrity, leader-owned synthesis/proof integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, remote default-branch verification, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.31
  - Release tag `v10.31` resolves to commit `22974c982ea3f3c51ed0a42cdf945da7c6e0f82e`.
  - Published at `2026-05-28T10:14:31Z`.
  - Patch: [../patch/goal-internal-subagent-assistance-refinement.patch.md](../patch/goal-internal-subagent-assistance-refinement.patch.md)

### Most Recently Completed

- **P122:** [phase-122-goal-to-plan-default-next-surface-hardening.md](phase-122-goal-to-plan-default-next-surface-hardening.md)
  - Output: touched owner rules, one related playground case update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch verification, and GitHub release `v10.30`.
  - Gate: explicit `/plan` next-surface integrity, objective-vs-route integrity, goal-gate closeout integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, remote default-branch verification, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.30
  - Release tag `v10.30` resolves to commit `c22a6c09a16d3cea4fc522f9ac2a39160ce7d717`.
  - Published at `2026-05-27T20:53:00Z`.
  - Patch: [../patch/goal-to-plan-default-next-surface-hardening.patch.md](../patch/goal-to-plan-default-next-surface-hardening.patch.md)

### Most Recently Completed

- **P121:** [phase-121-goal-to-plan-bridge-doctrine.md](phase-121-goal-to-plan-bridge-doctrine.md)
  - Output: touched owner rules, one related playground case update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch update, and GitHub release `v10.29`.
  - Gate: objective-vs-route integrity, non-trivial bridge integrity, goal-gate closeout integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, default-branch update, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.29
  - Release tag `v10.29` resolves to commit `d30c378b0be3593cea131e0c10c521f52749f48f`.
  - Published at `2026-05-27T10:41:28Z`.
  - Patch: [../patch/goal-to-plan-bridge-doctrine.patch.md](../patch/goal-to-plan-bridge-doctrine.patch.md)

- **P120:** [phase-120-strategic-correction-posture-hardening-follow-up.md](phase-120-strategic-correction-posture-hardening-follow-up.md)
  - Output: touched strategic-reasoning owners, one related playground case update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch update, and GitHub release `v10.28`.
  - Gate: logic-first correction integrity, scope-proven narrowing integrity, shared-mechanism-before-exception integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, default-branch update, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.28
  - Release tag `v10.28` resolves to commit `6a69e8c98bda1b58631f5b055f827df3519a2dda`.
  - Published at `2026-05-22T14:21:29Z`.

- **P119:** [phase-119-active-exchange-language-alignment-hardening-follow-up.md](phase-119-active-exchange-language-alignment-hardening-follow-up.md)
  - Output: touched language-alignment owners, one related playground case update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch update, and GitHub release `v10.27`.
  - Gate: active-exchange-language integrity, exact-literal preservation integrity, anti-wrapper-only-translation integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, default-branch update, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.27
  - Release tag `v10.27` resolves to commit `54943578d587b1a0deb4bdfda8d402ab065fe111`.
  - Published at `2026-05-21T02:15:51Z`.

- **P118:** [phase-118-successor-surfacing-bridge-hardening-follow-up.md](phase-118-successor-surfacing-bridge-hardening-follow-up.md)
  - Output: touched successor-surfacing bridge owners, one related playground case update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch update, and GitHub release `v10.26`.
  - Gate: successor-bridge integrity, bounded successor-slice derivation integrity, anti-generic-future-note closing integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, default-branch update, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.26
  - Release tag `v10.26` resolves to commit `b0b4b46fba2725b1abad4d6d4768647a897f2249`.
  - Published at `2026-05-20T17:54:46Z`.

- **P117:** [phase-117-proactive-goal-surfacing-and-decision-ready-response-style-refinement.md](phase-117-proactive-goal-surfacing-and-decision-ready-response-style-refinement.md)
  - Output: touched goal-surfacing owners, communication/presentation/evidence-boundary owners, one new playground case family plus index update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch update, and GitHub release `v10.25`.
  - Gate: goal/doctrine integrity, response-style owner integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, default-branch update, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.25
  - Release tag `v10.25` resolves to commit `0a32fa1c81a81739094ab94c9e6e8627d024bc03`.
  - Published at `2026-05-20T13:05:37Z`.

### Most Recently Completed

- **P116:** [phase-116-end-to-end-language-aligned-goal-surface-refinement.md](phase-116-end-to-end-language-aligned-goal-surface-refinement.md)
  - Output: touched runtime owners and companions, one new playground case family plus index update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, and GitHub release `v10.24`.
  - Gate: runtime/doctrine integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, GitHub release verification, and closeout alignment passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.24
  - Release tag `v10.24` resolves to commit `68f623e26d46e381fc098ff87f04daf99b3e7818`.
  - Published at `2026-05-20T09:53:32Z`.

### Most Recently Completed

- **P115:** [phase-115-language-aware-candidate-goal-promotion-playground-case-update.md](phase-115-language-aware-candidate-goal-promotion-playground-case-update.md)
  - Output: `case-15-language-aware-candidate-goal-promotion.md`, updated playground index, touched design/master release surfaces, runtime install-boundary recheck, 18/18 parity/body sufficiency, branch push, and GitHub release `v10.23`.
  - Gate: playground-family integrity, non-runtime playground boundary, runtime install/parity/body sufficiency, `git diff --check`, branch push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.23
  - Release tag `v10.23` resolves to commit `f434a3b31baa3532d933687545ec3f2b3f229c60`.
  - Published at `2026-05-20T08:59:56Z`.

### Most Recently Completed

- **P114:** [phase-114-language-aware-candidate-goal-and-goal-command-doctrine.md](phase-114-language-aware-candidate-goal-and-goal-command-doctrine.md)
  - Output: dominant-session-language ownership for candidate goals and promoted `/goal`, candidate-goal-first successor recommendation mode, selective governed `/goal` promotion, two Thai-first governed examples, runtime install, 18/18 parity/body sufficiency, branch push, and GitHub release `v10.22`.
  - Gate: doctrine integrity, 18-rule install boundary, runtime install/parity/body sufficiency, `git diff --check`, branch push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.22
  - Release tag `v10.22` resolves to commit `3313fb193f96d5f18c6a6d45c7864e9971c8569d`.
  - Published at `2026-05-20T08:24:10Z`.


- **P113:** [phase-113-governed-work-only-goal-context-sourcing-doctrine.md](phase-113-governed-work-only-goal-context-sourcing-doctrine.md)
  - Output: governed-work-only `/goal` trigger doctrine, exact mandatory governed-surface triggers, design-first governed sourcing order, compact material-only output guidance, two concrete `/goal` examples, runtime install, 18/18 parity/body sufficiency, branch push, and GitHub release `v10.21`.
  - Gate: doctrine integrity, 18-rule install boundary, runtime install/parity/body sufficiency, `git diff --check`, branch push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.21
  - Release tag `v10.21` resolves to commit `53f80777bd3b0ec9d5ad84165bcd58e6e726c4f2`.
  - Published at `2026-05-20T07:54:14Z`.


- **P112:** [phase-112-grounded-playground-transcript-cases-and-realism-upgrade.md](phase-112-grounded-playground-transcript-cases-and-realism-upgrade.md)
  - Output: transcript-grounded observed log updates, richer multi-turn playground case traces, two grounded new scenario families, touched playground/design sync, runtime install parity/body sufficiency proof, push, and GitHub release `v10.20`.
  - Gate: transcript-anchor integrity, realism-trace integrity, non-runtime playground boundary, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.20
  - Release tag `v10.20` resolves to commit `4851338417501a391e7dc505d0b049d7fb6209db`.
  - Published at `2026-05-19T03:51:01Z`.

- **P111:** [phase-111-rules-playground-behavior-scenarios.md](phase-111-rules-playground-behavior-scenarios.md)
  - Output: playground architecture design, playground index/coverage/matrix/template/observed files, 10 scenario-family case files with prompt/response examples and flow diagrams, README pointer-only integration, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.19`.
  - Gate: playground family integrity, 18-rule coverage mapping, virtual matrix axis coverage, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.19
  - Release tag `v10.19` resolves to commit `e3e0bdfe255c2370085abcfebbb25a6544de9a1b`.
  - Published at `2026-05-19T01:39:59Z`.

### Previously Completed

- **P110:** [phase-110-project-local-claude-code-remote-install-helpers.md](phase-110-project-local-claude-code-remote-install-helpers.md)
  - Output: launcher-first README and AI install guidance, Bash/PowerShell launcher scripts over the helper execution layer, dedicated installer architecture design, explanation clarity doctrine refinements, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.18`.
  - Gate: installer contract integrity, explanation-doctrine sync, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.18
  - Release tag `v10.18` resolves to commit `b1ee4100b471b96a975c22a480137b81fa5efc8a`.
  - Published at `2026-05-19T00:42:14Z`.

- **P109:** [phase-109-lineage-first-phase-selection-and-subphase-enforcement.md](phase-109-lineage-first-phase-selection-and-subphase-enforcement.md)
  - Output: strict fall-through phase identity gate, explicit why-not-current / why-not-subphase basis, companion/master-surface sync, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.17`.
  - Gate: lineage integrity, README arrays 18/18, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.17
  - Release tag `v10.17` resolves to commit `a330d414c6fd20febf2222288651cc166d0c62b0`.
  - Published at `2026-05-18T14:01:40Z`.

- **P108:** [phase-108-worker-routing-runtime-compaction-and-owner-redistribution.md](phase-108-worker-routing-runtime-compaction-and-owner-redistribution.md)
  - Output: worker-routing compaction, owner redistribution into document-integrity/document-governance, companion/master-surface sync, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.16`.
  - Gate: compaction integrity, README arrays 18/18, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.16
  - Release tag `v10.16` resolves to commit `731624622af67e68869469d74f419d5c67a6752d`.
  - Published at `2026-05-18T05:01:02Z`.

- **P107:** [phase-107-explicit-goal-command-suggestion-doctrine.md](phase-107-explicit-goal-command-suggestion-doctrine.md)
  - Output: touched owner chains, companion/master-surface sync, `/goal` trigger doctrine, `/goal` output shape, `/goal` sourcing/writing doctrine, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.15`.
  - Gate: doctrine integrity, README arrays 18/18, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.15
  - Release tag `v10.15` resolves to commit `771a4769b65910cf28b9c7e6c30145551a88cec8`.
  - Published at `2026-05-18T02:34:32Z`.


- **P106:** [phase-106-parent-model-supersession-and-adherence-validation.md](phase-106-parent-model-supersession-and-adherence-validation.md)
  - Output: touched owner chains, companion/master-surface supersession sync, selected historical guard wording, expanded chronology/adherence verification, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.14`.
  - Gate: doctrine integrity, chronology clarity, README arrays 18/18, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.14
  - Release tag `v10.14` resolves to commit `3e163fc7be7922230155ef0f184f2484b73509a6`.
  - Published at `2026-05-17T23:36:10Z`.


- **P105:** [phase-105-folder-scoped-generic-parent-and-single-parent-authority.md](phase-105-folder-scoped-generic-parent-and-single-parent-authority.md)
  - Output: touched owner chains, master design/changelog doctrine sync, expanded `docs_analysis`, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.13`.
  - Gate: doctrine integrity, README arrays 18/18, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.13
  - Release tag `v10.13` resolves to commit `b1eba20b8c31041afd794625650a1107d8702e05`.
  - Published at `2026-05-17T13:43:03Z`.


- **P104:** [phase-104-semantic-parent-naming-and-bootstrap-first-normalization.md](phase-104-semantic-parent-naming-and-bootstrap-first-normalization.md)
  - Output: touched owner chains, master design/changelog doctrine sync, expanded `docs_analysis`, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.12`.
  - Gate: doctrine integrity, README arrays 18/18, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.12
  - Release tag `v10.12` resolves to commit `a5dfb34ab7a26dc91bff3861ca3425bf00c99d8a`.
  - Published at `2026-05-17T09:16:12Z`.

- **P102:** [phase-102-chain-shape-normalization-and-append-vs-shard-gate.md](phase-102-chain-shape-normalization-and-append-vs-shard-gate.md)
  - Output: touched owner chains, master design/changelog doctrine sync, docs-analysis gate, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.10`.
  - Gate: doctrine integrity, README arrays 18/18, runtime install/parity/body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.10
  - Release tag `v10.10` resolves to commit `941fde875dedc2cede3db6f4bee2d144c4b029c3`.
  - Published at `2026-05-17T01:55:18Z`.

- **P101:** [phase-101-governed-path-normalization-and-premise-separation.md](phase-101-governed-path-normalization-and-premise-separation.md)
  - Output: touched owner chains, normalized master design/changelog structures, docs sync, runtime install, 18/18 parity/body sufficiency, push, and GitHub release `v10.09`.
  - Gate: normalization integrity, runtime install, 18/18 source/runtime parity, source/destination body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.09
  - Release tag `v10.09` resolves to commit `c883b8617ebfda89ff8dc288533dffe835d6785b`.
  - Published at `2026-05-17T00:52:06Z`.

- **P100:** [phase-100-safe-first-active-runtime-compression.md](phase-100-safe-first-active-runtime-compression.md)
  - Output: safe-first compression across selected merged owners released as `v10.08`.
  - Gate: runtime install, 18/18 source/runtime parity, source/destination body sufficiency, push, and GitHub release verification passed.
  - Release URL: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.08
  - Release target and tag point to commit `f57d67727b52fea53078223725034730b882af09`.
  - Published at `2026-05-16T23:10:15Z`.

### Archived Completed Detail

- Earlier completed phase-map detail was compacted into [done/released-phase-summary-archive.md](done/released-phase-summary-archive.md).
- Per-phase closeout truth remains in the dedicated completed phase files such as [phase-098-conversation-intent-root-cause-and-scope-drift-refinement.md](phase-098-conversation-intent-root-cause-and-scope-drift-refinement.md) and [phase-097-source-merge-cleanup-compact-runtime-set.md](phase-097-source-merge-cleanup-compact-runtime-set.md).

---

## Verification Focus

Current promoted baseline after P135 closeout:
- released baseline is `v10.43 / P135`
- README current-state sections now expose governed goal auto-plan-file authoring as the current release posture for governed `/goal`
- active doctrine keeps `/goal` as semantic/objective authority for outcome, proof/checks, scope, and hard guardrails while the referenced plan file stays route-only support
- `execution-and-goal-frame.md`, `phase-todo-artifact.md`, `document-integrity.md`, `explanation-and-presentation.md`, `accurate-communication.md`, and `communication-register.md` now agree that actual governed `/goal` authoring writes the route-only plan file before final goal emission when the durable-route trigger holds, keeps the exact `Plan reference` inside the same copied goal artifact, and rejects save-plan / rerun-`/goal` loops when no real stop gate exists
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references
- `git diff --check` passed with no whitespace errors
- local source release state, remote `master`, and tag `v10.43` resolve to the same promoted commit lineage
- GitHub release `v10.43` was verified on the promoted state after default-branch reconciliation

---

## Rollback / Containment

If P135 is reversed after release:
- revert the touched governed goal auto-plan-file authoring edits as one governed rollback release
- restore the immediately previous released baseline as the active baseline
- keep the compact 18-file runtime install scope unchanged unless an explicit rollback gate selects another install action
- do not delete phase, patch, history, `done/`, unrelated runtime destination files, or observed-only extras as cleanup

---

## History and Done References

- Daily phase movement: [history/2026-05-16.md](history/2026-05-16.md); [history/2026-05-08.md](history/2026-05-08.md)
- Pre-rollover phase summary snapshot: [history/2026-05-08-pre-rollover-SUMMARY.md](history/2026-05-08-pre-rollover-SUMMARY.md)
- Archived completed phase-map detail: [done/released-phase-summary-archive.md](done/released-phase-summary-archive.md); [done/](done/)
- Current master changelog: [../changelog/changelog.md](../changelog/changelog.md)
