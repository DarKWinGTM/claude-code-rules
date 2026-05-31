# Design Index - governed-docs

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-05-31)
> **Selected Parent Model:** generic parent
> **Selected Chain Shape:** flat-sibling-shards

---

## 1) Purpose

This file is the active parent design index for the `governed-docs` plugin-local design chain.

It exists to keep the chain readable as a compact authority gateway while moving detailed target-state slices into flat sibling shards.

## 2) Why `design.md` is the active parent here

The current `design/` folder fully scopes one chain for this capsule. Under the current RULES doctrine, a generic parent is valid when the folder already acts as the full namespace for one chain.

This chain therefore uses:
- active parent model: `design.md`
- chain shape: `flat-sibling-shards`

## 3) Authority boundary

- This design chain is local to `plugin/governed-docs/` because the user selected a plugin-local governed extension form for this capsule.
- That selected local form applies to this capsule only. It must not be generalized automatically into root RULES doctrine or treated as proof that every `plugin/**` path should own a governed chain.
- Root RULES remains stronger than this capsule for active global RULES semantics.
- The plugin may inspect, classify, and prepare maintenance actions for governed docs, but it must not become the semantic owner of `README.md`, `design/`, `changelog/`, `TODO.md`, `phase/`, or `patch/`.
- Evidence produced by the plugin is operational evidence and maintenance input, not replacement authority.
- Hook output, generated artifacts, and agent findings remain support surfaces only until the main session or selected governed follow-up applies them.

## 4) Why this chain no longer stays bootstrap-only

This chain does not stay `single-file-bootstrap` because the target state already contains several coherent slices that should remain separate:
- purpose / scope / authority boundary
- architecture layers
- governed surface inventory
- maintenance problem classes
- skill + agent system
- generated artifacts + hook posture
- action policy + release gate
- article Markdown presentation

Keeping all of that in one parent file would immediately create a design God file.

## 5) Active shard map

- [00-purpose-scope-boundary.design.md](00-purpose-scope-boundary.design.md) — plugin purpose, v1 scope, non-goals, and RULES-vs-plugin authority boundary
- [01-architecture-layers.design.md](01-architecture-layers.design.md) — scanner, doctrine evaluator, repair planner, bounded executor, and end-to-end flow
- [02-governed-surface-inventory.design.md](02-governed-surface-inventory.design.md) — governed surfaces, doctrine inputs, and inspection targets the plugin must understand
- [03-maintenance-problem-classes.design.md](03-maintenance-problem-classes.design.md) — recurring drift/maintenance classes the plugin must detect and classify
- [04-skills-and-agent-system.design.md](04-skills-and-agent-system.design.md) — skill set, custom agent set, and operating responsibilities
- [05-generated-artifacts-and-hook-posture.design.md](05-generated-artifacts-and-hook-posture.design.md) — review/repair artifacts, hook posture, reminder boundaries, and non-hidden governance rules
- [06-action-policy-and-release-gate.design.md](06-action-policy-and-release-gate.design.md) — advisory / guarded-execute / bounded auto-normalize policy, approval boundary, automation-risk non-goals, and release-gate model
- [07-article-markdown-presentation.design.md](07-article-markdown-presentation.design.md) — governed-docs-owned Markdown-to-HTML article presentation, safe rendering boundary, and frontend/presentation contract
- [08-preview-portal-and-sync.design.md](08-preview-portal-and-sync.design.md) — root `preview/` portal contract, full-site sync model, UI/UX shell direction, and support-only preview authority boundary

## 6) V1 baseline

The explicit v1 target is:
- RULES-specific first
- runtime scope may include scanner, evaluator, repair planning, operator entry surfaces, bounded executor policy, release-gate logic, and governed-docs-owned article-style Markdown presentation
- no attempt to generalize into a framework before the RULES-specific operating model is stable
- default mutation posture: `guarded-execute`
- user-facing operations must require an explicit target workspace path rather than silently acting on ambient cwd
- article-style Markdown presentation may borrow structure and safety ideas from NodeClaw, but ownership and implementation stay inside governed-docs

## 7) Verification orientation

This design chain should be considered complete for the current goal only when:
- the parent stays compact and points to all active shards cleanly
- every shard owns one coherent responsibility
- no shard silently becomes semantic authority over root RULES surfaces
- the chain makes v1 RULES-specific scope explicit
- automation-risk non-goals are explicit
- the default posture is clearly `guarded-execute`

---

> Design chain rule: this chain remains the target-state authority for governed-docs behavior, while runtime implementation must stay inside the same RULES-specific ownership and safety boundaries it defines.
