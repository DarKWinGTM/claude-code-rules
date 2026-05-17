# Repository Model - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.09
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-17)
> **Section:** Active repository model
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Layer Roles

| Layer | Primary Artifacts | Active Role |
|---|---|---|
| Overview | `README.md` | Repository overview and usage guidance only |
| Runtime | root `*.md` rules | Active runtime behavior |
| Design | `design/*.design.md`, `design/<slug>/*.design.md` | Active target-state guidance with compact parent indexes and governed active child shards for broad chains |
| Phase | `phase/SUMMARY.md`, `phase/phase-NNN*.md`, `phase/history/`, `phase/done/` | Compact live roadmap/index and phased execution detail with referenced inactive history |
| Patch | `patch/<context>.patch.md`, `patch/done/` | Governed before/after review artifacts outside live phase planning |
| History | `changelog/*.changelog.md`, `changelog/<chain>/v*.changelog.md`, `changelog/done/*.changelog.md` | Active parent version authority with indexed detail shards and legacy/archive fallback history |
| Execution | `TODO.md`, `todo/history/`, `todo/done/` | Compact active execution tracking plus referenced inactive history/detail |
| Support | `phase-implementation-template.md`, `support/**` | Helper/reference surfaces that do not become active authority by proximity |

---

## Repository Governance Principles

This repository uses one deterministic governance model:
- README is overview-only
- runtime rules remain the active rule layer and the README-listed runtime set must stay body-sufficient
- design remains active target-state truth and broad chains should strongly prefer a compact parent plus active same-stem shard path
- active parent changelogs remain version authority and broad chains should strongly prefer a compact parent plus chain-scoped version detail shards
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with `history/` / `done/` as normalized overflow paths
- worker/context-safe reading begins from parent indexes and the smallest relevant shard or detail surface
- concern, factual claim, goal request, proposal, and assistant next action should stay separated before endorsement or continuation
- startup, phase, patch, verification, portability, memory, audience-surface, and release boundaries stay with their dedicated owners

---

## Historical Boundary

Older release-by-release rollout narratives are historical context only after the ownership split and do not override the current active runtime/design authority boundary.

Those records belong in [../../changelog/changelog.md](../../changelog/changelog.md), not in this active repository-model shard.
