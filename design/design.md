# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 10.15
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-17)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Shard Directory:** [design/](design/)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

The active model for `v10.15 / P107` should keep the RULES system readable, source-owned, evidence-grounded, explicit about governed chain-shape selection before doc normalization, explicit about when a folder-scoped single-chain namespace may use `design/design.md` or `changelog/changelog.md`, explicit about requiring exactly one active parent model per chain, explicit about separating observed project shape from extracted doctrine and the selected target form, explicit about active-doctrine precedence over older completed-history wording when chronology conflicts, explicit about when a compact `/goal` suggestion is appropriate, and less likely to confuse a bounded next-step command with silent continuation or vague prose.

---

## 2) Current Active-State Summary

Current target-state priorities:
- runtime rules stay as body-sufficient active behavior contracts
- active runtime/design doctrine must outrank older completed phase/patch wording when chronology conflicts
- governed design/changelog chains must classify chain shape before appending or sharding detail
- folder-scoped single-chain namespaces may use `design/design.md` or `changelog/changelog.md` when the folder already fully identifies one chain
- each chain must still keep exactly one active parent model: generic parent or semantic parent, never both
- single-design chains should stay `single-file-bootstrap` until a checked `bootstrap_exit_trigger` and `shard_opening_basis` justify same-stem shards
- flat sibling shards are valid when the current folder already scopes the chain and only a few coherent slices are needed
- broad mature design/changelog chains should still strongly prefer compact parent indexes plus active same-stem child shard paths
- checked example structure must stay distinct from extracted doctrine and the selected target form when governance recommendations are derived from another project or chain
- `docs_analysis` must record observed project shape, extracted doctrine, selected target form, equivalence-claim basis, namespace scope, parent model choice, and single-parent authority basis when normalization work is in scope
- chronology/supersession review must stay explicit when active doctrine and reachable completed history discuss the same normalization rule
- compact `/goal` suggestions should be allowed only when a bounded successor objective is clear, measurable, and provable in transcript
- compact `/goal` suggestions should be sourced from checked Goal/Output/Gate/Verification surfaces rather than improvised from vague next-step prose
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
