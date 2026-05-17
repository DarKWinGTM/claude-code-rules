# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 10.11
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-17)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Shard Directory:** [design/](design/)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

The active model for `v10.11 / P103` should keep the RULES system readable, source-owned, evidence-grounded, explicit about governed chain-shape selection before doc normalization, explicit about separating observed project shape from extracted doctrine and the selected target form, and less likely to overclaim checked examples as one-to-one proof of the selected RULES target form.

---

## 2) Current Active-State Summary

Current target-state priorities:
- runtime rules stay as body-sufficient active behavior contracts
- governed design/changelog chains must classify chain shape before appending or sharding detail
- flat sibling shards are valid when the current folder already scopes the chain and only a few coherent slices are needed
- broad mature design/changelog chains should still strongly prefer compact parent indexes plus active same-stem child shard paths
- checked example structure must stay distinct from extracted doctrine and the selected target form when governance recommendations are derived from another project or chain
- `docs_analysis` must record observed project shape, extracted doctrine, selected target form, and equivalence-claim basis when example-backed normalization work is in scope
- `TODO.md` and `phase/SUMMARY.md` stay compact active entrypoints, with `history/` and `done/` as normalized overflow paths
- current release and version authority stay in active parent changelogs, while bulky same-chain detail moves to chain-scoped version shards
- concern, factual claim, goal request, proposal, and assistant next action should stay separated before endorsement or continuation
- worker-first/context-safe reading still starts from parent indexes and then follows the declared smallest relevant shard or detail surface

Historical release-by-release detail lives in [../changelog/changelog.md](../changelog/changelog.md), not in this active target-state parent.

---

## 3) Shard Map

Open the smallest shard that answers the question.

- [repository-model.design.md](design/repository-model.design.md) — active surface roles and normalized documentation model
- [runtime-architecture.design.md](design/runtime-architecture.design.md) — 18-rule runtime inventory and category view
- [governance-contracts.design.md](design/governance-contracts.design.md) — metadata, sync order, startup, phase, rollover, and memory contracts
- [templates.design.md](design/templates.design.md) — standard templates for runtime, design, and changelog artifacts
- [verification-and-integration.design.md](design/verification-and-integration.design.md) — master verification checklist and related-chain integration

---

## 4) Compact Parent Boundary

This parent is the active authority gateway for the RULES system design.

It should remain compact enough to:
- expose current architecture and normalization direction quickly
- point readers to the correct child shard without broad raw absorption
- avoid becoming a history dump, template dump, or umbrella God file

Child shards under [design/](design/) remain active target-state truth, not archive or `done/` history.

---

## 5) Verification Orientation

Release validation for this master design chain should confirm:
- this parent remains compact and body-sufficient
- child shards are reachable and role-correct
- runtime/design/changelog versions align
- observed project shape, extracted doctrine, selected target form, and any equivalence-claim basis stay distinct when checked examples ground governance recommendations
- history/release detail stays with changelog authority instead of re-accumulating in active design truth

---

## 6) Integration

Primary related surfaces:
- [../README.md](../README.md)
- [../changelog/changelog.md](../changelog/changelog.md)
- [../TODO.md](../TODO.md)
- [../phase/SUMMARY.md](../phase/SUMMARY.md)
