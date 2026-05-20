# Claude Code Rules System

## 0) Document Control

> **Parent Scope:** RULES System Design
> **Current Version:** 10.25
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-20)
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Shard Directory:** [design/](design/)

---

## 1) Goal

Define the active-state architecture for the RULES repository so it teaches one deterministic governance model and avoids accidental rule-poisoning through mixed authority signals.

The active model for `v10.20 / P112` should keep the RULES system readable, source-owned, evidence-grounded, explicit about governed chain-shape selection before doc normalization, explicit about when a folder-scoped single-chain namespace may use `design/design.md` or `changelog/changelog.md`, explicit about requiring exactly one active parent model per chain, explicit about separating observed project shape from extracted doctrine and the selected target form, explicit about active-doctrine precedence over older completed-history wording when chronology conflicts, explicit about when a compact `/goal` suggestion is appropriate, less likely to let phase selection skip current-phase reuse or truthful subphase fit before opening a new major phase, explicit that Claude Code helper installs should prefer project-local `.claude/rules/` without overclaiming unsupported cross-harness install surfaces, and explicit that the `playground/` family remains a governed non-runtime surface while transcript-derived observed cases must stay factual, anchored, and visibly distinct from virtual variants.

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
- compact `/goal` suggestions should stay light or be omitted entirely for trivial non-governed next steps
- candidate goals should be the preferred shape for multi-path successor recommendations when several meaningful directions remain live
- candidate goals may also surface at real decision boundaries when several materially different next slices remain live and no one continuation path clearly dominates
- candidate goals and promoted `/goal` suggestions should follow the dominant session language by default unless the user explicitly selects another language
- compact `/goal` suggestions should be allowed only when a bounded governed-work successor objective is clear, measurable, provable in transcript, and better than direct continuation
- governed-surface context for `/goal` should become mandatory only for repo-governed multi-step, phase-backed, design-impacting, doc-sync, release-sync, runtime-rule-impacting, or materially current-state/review-sensitive work
- governed `/goal` suggestions should source design first, then current phase/task/TODO/checked implementation state, with changelog/patch/README included only when they materially shape completion, review, or current-state impact
- when several candidate goals remain live, only the best-supported governed candidate should be promoted into advisory `/goal` form; the others may stay prose goals
- phase identity selection should stay lineage-first: current active phase update first, existing-family subphase second, new major only after visible why-not-current / why-not-subphase evidence
- Claude Code helper installs should prefer project-local `.claude/rules/` as the primary runtime target, use owner-aware manifest cleanup, and avoid overclaiming unsupported non-native harnesses for that install surface
- AI explanation should stay meaning-first: explain what an identifier is, what it does, and what changes if it changes before leaning on raw field or variable names alone
- non-trivial answers should usually open with one short plain-language summary, use a small table when several axes matter, continue with grouped explanation by concept, and end with a concise decision-ready close
- flow/process/queue/order/concurrency explanations may prefer an overview → small table → grouped explanation → concise summary shape when that structure reduces cognitive load
- nested keys should normally be explained parent → child, and UI mental model versus storage model should stay explicit when that distinction matters to understanding
- readable grouping of verified fact, inference, and hypothesis belongs to the communication owners, while proof thresholds and evidence semantics stay with `evidence-discipline.md`
- `TODO.md` and `phase/SUMMARY.md` stay compact active entrypoints, with `history/` and `done/` as normalized overflow paths
- current release and version authority stay in active parent changelogs, while bulky same-chain detail moves to chain-scoped version shards
- concern, factual claim, goal request, proposal, and assistant next action should stay separated before endorsement or continuation
- a governed `playground/` family may show how RULES change AI behavior in practice, but it must keep `rule-enforced fact`, `observed case`, and `virtual variant` visibly separate
- transcript-derived observed cases inside the playground must include exact checked paths and anchor hints rather than loose storytelling
- playground examples should prefer more realistic multi-turn traces when they help show how RULES alter the assistant path
- playground scenario coverage may include a language-aware candidate-goal promotion family so dominant-session-language ownership, candidate-goal-first successor recommendations, and selective `/goal` promotion remain inspectable as operational behavior
- candidate goals, promoted `/goal`, recommendation labels, and recap/closing lines should follow the dominant session language end-to-end, with English preserved only for exact literals such as command names, file paths, version tags, and code-level identifiers unless the user explicitly selects another language style
- playground scenario coverage may also include an end-to-end language-aligned goal surface family so wrapper labels, candidate-goal headings, promoted `/goal`, and recap lines can be inspected operationally rather than only as doctrine text
- governed behavior playground material stays outside the runtime install payload unless a later explicit doctrine changes that boundary
- worker-first/context-safe reading still starts from parent indexes and then follows the declared smallest relevant shard or detail surface

Historical release-by-release detail lives in [../changelog/changelog.md](../changelog/changelog.md), not in this active target-state parent.

---

## 3) Shard Map

Open the smallest shard that answers the question.

- [repository-model.design.md](design/repository-model.design.md) — active surface roles and normalized documentation model
- [runtime-architecture.design.md](design/runtime-architecture.design.md) — 18-rule runtime inventory and category view
- [governance-contracts.design.md](design/governance-contracts.design.md) — metadata, sync order, startup, phase, rollover, and memory contracts
- [installer-architecture.design.md](design/installer-architecture.design.md) — project-local Claude Code helper install contract, cleanup boundary, and verification model
- [playground-architecture.design.md](design/playground-architecture.design.md) — governed playground family role, fact/observed/virtual separation, coverage model, and update flow
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
