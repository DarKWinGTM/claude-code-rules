# RULES Phase Summary

> **Current Version:** 2.00
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.34
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** Active P123 / target v10.31 goal internal native subagent assistance refinement; latest released baseline remains v10.30 / P122
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

- **P123:** [phase-123-goal-internal-subagent-assistance-refinement.md](phase-123-goal-internal-subagent-assistance-refinement.md)
  - Goal: keep `/goal` as the objective owner, keep `/plan` as the route owner, and let `/goal` conditionally use internal native subagent assistance for analysis, verification, testing, and bounded plan drafting when the selected governed goal remains non-trivial or route-heavy.
  - Output: touched runtime owners, one related playground/reference case update, touched master release surfaces, runtime install into `~/.claude/rules`, 18/18 parity/body sufficiency, branch push, remote default-branch update, and GitHub release `v10.31`.
  - Gate: objective-vs-route integrity, internal-helper-only subagent integrity, conditional agent-use integrity, leader-owned synthesis/proof integrity, non-runtime playground boundary, 18-file install-boundary preservation, parity/body sufficiency, `git diff --check`, branch push, default-branch update, GitHub release verification, and closeout alignment.
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

Latest released baseline before P123 work:
- released baseline is `v10.30 / P122`
- route-heavy selected governed goals already explicitly recommend `/plan` as the default next surface instead of broad prose follow-up
- `/goal` already remains the objective owner while `/plan` already remains the route owner
- closeout already returns to the goal gate instead of treating plan completion alone as sufficient proof
- the updated playground case already keeps the explicit `/plan` recommendation delta inspectable
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references
- runtime install copied only the 18 README-listed active runtime rules into `~/.claude/rules`
- 18/18 source/runtime parity and source/destination body sufficiency passed for the latest released baseline
- `playground/` remains outside the runtime install payload while the active runtime count remains 18
- `git diff --check` passed for the latest released baseline
- branch `goal-governed-work-only` and GitHub release `v10.30` are the current checked released state before P123 opens

Current P123 verification focus:
- a selected governed non-trivial or route-heavy goal may now conditionally use internal native subagent assistance for analysis, verification, testing, or bounded plan drafting without creating a new user-facing command
- `/goal` must still remain the objective owner and `/plan` must still remain the route owner
- helper findings must remain subordinate to leader-owned synthesis/proof wording rather than becoming automatic completion proof
- one updated playground/reference case should keep the helper-vs-owner behavior delta inspectable
- `playground/` must remain outside the runtime install payload while the active runtime count remains 18
- runtime install, source/runtime parity, source/destination body sufficiency, `git diff --check`, branch push, default-branch update, and GitHub release verification still remain required before P123 closeout
- the updated playground case keeps the explicit `/plan` recommendation delta inspectable
- `TODO.md` and `phase/SUMMARY.md` remain compact current entrypoints with reachable `history/` / `done/` references
- runtime install copied only the 18 README-listed active runtime rules into `~/.claude/rules`
- 18/18 source/runtime parity and source/destination body sufficiency passed
- `playground/` remains outside the runtime install payload while the active runtime count remains 18
- `git diff --check` passed with no whitespace errors
- branch `goal-governed-work-only` was pushed to origin, the remote default branch remained `goal-governed-work-only`, and GitHub release `v10.30` was published at `2026-05-27T20:53:00Z`

---

## Rollback / Containment

If P123 is reversed after release:
- revert the touched governed `/goal` doctrine edits as one governed rollback release
- restore the released `v10.30 / P122` source state as the active baseline
- keep the compact 18-file runtime install scope unchanged unless an explicit rollback gate selects another install action
- do not delete phase, patch, history, `done/`, unrelated runtime destination files, or observed-only extras as cleanup

---

## History and Done References

- Daily phase movement: [history/2026-05-16.md](history/2026-05-16.md); [history/2026-05-08.md](history/2026-05-08.md)
- Pre-rollover phase summary snapshot: [history/2026-05-08-pre-rollover-SUMMARY.md](history/2026-05-08-pre-rollover-SUMMARY.md)
- Archived completed phase-map detail: [done/released-phase-summary-archive.md](done/released-phase-summary-archive.md); [done/](done/)
- Current master changelog: [../changelog/changelog.md](../changelog/changelog.md)
