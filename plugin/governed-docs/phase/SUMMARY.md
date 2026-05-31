# governed-docs Phase Summary

> **Current Version:** 0.1.0
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** P001 and P002 completed in checked scope; no open phase remains in the current program
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **History:** none opened yet
> **Completed Detail:** none opened yet

---

## Current Purpose

This file is the compact active phase roadmap/index for the `governed-docs` plugin-local chain.

The current implemented program is complete in checked scope across two rollout families:
- **P001** — scanner, evaluator, repair planner, operator surfaces, bounded executor policy, release-gate flow, and article-style single-document rendering
- **P002** — root `preview/` portal architecture, `present-md` path refactor, `present-sync` full-site rebuild, preview helper surfaces, and preview-wave verification/closeout

---

## Design-shard source of truth mapping

- **P001** ← bootstrap and authority boundary from [`design/design.md`](../design/design.md), [`00-purpose-scope-boundary.design.md`](../design/00-purpose-scope-boundary.design.md)
- **P001-01** ← entry gate + Layer A scanner from [`01-architecture-layers.design.md`](../design/01-architecture-layers.design.md), [`02-governed-surface-inventory.design.md`](../design/02-governed-surface-inventory.design.md), [`06-action-policy-and-release-gate.design.md`](../design/06-action-policy-and-release-gate.design.md)
- **P001-02** ← Layer B doctrine evaluator and problem-class handling from [`01-architecture-layers.design.md`](../design/01-architecture-layers.design.md), [`02-governed-surface-inventory.design.md`](../design/02-governed-surface-inventory.design.md), [`03-maintenance-problem-classes.design.md`](../design/03-maintenance-problem-classes.design.md)
- **P001-03** ← Layer C repair planner and generated artifact model from [`01-architecture-layers.design.md`](../design/01-architecture-layers.design.md), [`03-maintenance-problem-classes.design.md`](../design/03-maintenance-problem-classes.design.md), [`05-generated-artifacts-and-hook-posture.design.md`](../design/05-generated-artifacts-and-hook-posture.design.md)
- **P001-04** ← operator skill set and custom agent set from [`04-skills-and-agent-system.design.md`](../design/04-skills-and-agent-system.design.md)
- **P001-05** ← bounded executor boundary, hook posture, and action policy enforcement from [`01-architecture-layers.design.md`](../design/01-architecture-layers.design.md), [`05-generated-artifacts-and-hook-posture.design.md`](../design/05-generated-artifacts-and-hook-posture.design.md), [`06-action-policy-and-release-gate.design.md`](../design/06-action-policy-and-release-gate.design.md)
- **P001-06** ← release-gate flow and closeout consistency from [`05-generated-artifacts-and-hook-posture.design.md`](../design/05-generated-artifacts-and-hook-posture.design.md), [`06-action-policy-and-release-gate.design.md`](../design/06-action-policy-and-release-gate.design.md)
- **P001-07** ← governed-docs-owned article Markdown presentation from [`07-article-markdown-presentation.design.md`](../design/07-article-markdown-presentation.design.md)
- **P002** ← preview portal and sync wave from [`08-preview-portal-and-sync.design.md`](../design/08-preview-portal-and-sync.design.md) plus article presentation and generated-artifact doctrine
- **P002-01** ← root `preview/` output-path contract and `present-md` single-document refactor
- **P002-02** ← `present-sync` full preview-site inventory / manifest / portal rebuild
- **P002-03** ← preview portal UI shell and present-layer helper agents
- **P002-04** ← preview-wave verification, smoke checks, and governed closeout sync

---

## Implementation order

1. **P001-01** — explicit target-path gate + read-only scanner foundation (**completed**)
2. **P001-02** — doctrine evaluator and problem-class classification (**completed**)
3. **P001-03** — repair planner and generated review artifacts (**completed**)
4. **P001-04** — operator skill surfaces and custom agent entry scaffolds (**completed**)
5. **P001-05** — bounded executor boundary, hook-light guardrails, and action policy enforcement (**completed**)
6. **P001-06** — release-gate flow and closeout consistency (**completed**)
7. **P001-07** — governed-docs-owned article-style Markdown presentation (**completed**)
8. **P002-01** — root `preview/` path refactor for `present-md` (**completed**)
9. **P002-02** — `present-sync` full preview-site build (**completed**)
10. **P002-03** — preview portal UI shell and helper subagents (**completed**)
11. **P002-04** — preview-wave verification and closeout (**completed**)

---

## Phase Roadmap

### Completed in checked scope

- **P001:** [phase-001-governed-docs-design-chain-bootstrap.md](phase-001-governed-docs-design-chain-bootstrap.md)
- **P001-01:** [phase-001-01-explicit-path-read-only-governed-surface-scan.md](phase-001-01-explicit-path-read-only-governed-surface-scan.md)
- **P001-02:** [phase-001-02-doctrine-evaluator-and-problem-class-classification.md](phase-001-02-doctrine-evaluator-and-problem-class-classification.md)
- **P001-03:** [phase-001-03-repair-planner-and-generated-review-artifacts.md](phase-001-03-repair-planner-and-generated-review-artifacts.md)
- **P001-04:** [phase-001-04-operator-skill-and-agent-entry-surfaces.md](phase-001-04-operator-skill-and-agent-entry-surfaces.md)
- **P001-05:** [phase-001-05-bounded-executor-policy-and-hook-guardrails.md](phase-001-05-bounded-executor-policy-and-hook-guardrails.md)
- **P001-06:** [phase-001-06-release-gate-flow-and-closeout-consistency.md](phase-001-06-release-gate-flow-and-closeout-consistency.md)
- **P001-07:** [phase-001-07-article-markdown-presentation-separate-later-phase.md](phase-001-07-article-markdown-presentation-separate-later-phase.md)
- **P002:** [phase-002-preview-portal-and-sync-wave.md](phase-002-preview-portal-and-sync-wave.md)
- **P002-01:** [phase-002-01-preview-path-and-present-md-refactor.md](phase-002-01-preview-path-and-present-md-refactor.md)
- **P002-02:** [phase-002-02-present-sync-site-build.md](phase-002-02-present-sync-site-build.md)
- **P002-03:** [phase-002-03-preview-portal-ui-and-subagents.md](phase-002-03-preview-portal-ui-and-subagents.md)
- **P002-04:** [phase-002-04-preview-wave-verification-and-closeout.md](phase-002-04-preview-wave-verification-and-closeout.md)

### Open phases

- none selected or opened

---

## Verification Focus

Latest checked implementation proof:
- `python3 -m unittest discover -s tests -v` passed with **45 tests**
- `./bin/governed-docs present-md /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs design/07-article-markdown-presentation.design.md` wrote to `preview/design/07-article-markdown-presentation/index.html`
- `./bin/governed-docs present-sync /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` generated `preview/index.html` and `preview/manifest.json`
- source hash verification across selected governed files remained unchanged before/after `present-sync`
- old leftover `generated/article-preview/` artifact was removed after the root `preview/` migration

Verification route policy remained per-slice:
- scanner / evaluator / planner / executor / release-gate / presentation all used focused local tests plus bounded smoke checks where the public operator surface mattered
- the preview wave added focused tests for `present-sync`, preview path routing, stale-page pruning, and no-source-rewrite behavior
- no slice introduced ambient-cwd fallback, hidden hook authority, or broad auto-fix behavior

---

## Rollback / Containment

If future work reopens this chain:
- keep explicit target-path gating as the strongest preserved boundary
- keep scanner facts, doctrine judgments, repair planning, executor policy, release-gate logic, and preview portal sync separated by layer
- keep `preview/**` as a presentation/support surface only
- keep source authority in the governed doc families, not in preview output
- keep hook behavior advisory/support-only unless a later explicit wave selects stronger activation with checked proof
