# Repository Model - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.11
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-11)
> **Section:** Active repository model
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Layer Roles

| Layer | Primary Artifacts | Active Role |
|---|---|---|
| Project source | user- or project-selected Active Project Root | Sole source/governed/config/script/test/plugin-support-tooling/commit/release-input authority for the active objective |
| Overview | `README.md` | Repository overview and usage guidance only |
| Runtime payload | exact ordered 19 root `*.md` rules selected by installer sources | Active runtime behavior and installation payload; not the whole project source set |
| Design | `design/*.design.md`, `design/<slug>/*.design.md` | Active target-state guidance with compact parent indexes plus governed child or sibling shards chosen by declared chain shape |
| Phase | `phase/SUMMARY.md`, `phase/phase-NNN-*.md`, `phase/phase-NNN-NN-*.md`, `phase/phase-NNN-NN-NN-*.md`, `phase/history/`, `phase/done/` | Compact live roadmap/index and phased execution detail with explicit forward-valid numeric phase grammar plus referenced inactive history |
| Patch | `patch/<context>.patch.md`, `patch/done/` | Governed before/after review artifacts outside live phase planning |
| History | `changelog/*.changelog.md`, `changelog/<chain>/v*.changelog.md`, `changelog/done/*.changelog.md` | Active parent version authority with indexed detail shards in sibling or same-stem mode plus legacy/archive fallback history |
| Execution | `TODO.md`, `todo/history/`, `todo/done/` | Compact active execution tracking plus referenced inactive history/detail |
| Plugin/support/tooling | `plugin/**`, `support/**`, `template/phase-authoring-template.md`, `script/**`, `playground/**` | Project source state owned from the Active Project Root; excluded from the 19-file Runtime payload unless a separate contract selects it |

---

## Repository Governance Principles

This repository uses one deterministic governance model:
- one Active Project Root selected by current user direction or checked project-local authority owns all development and governed source for the active objective
- `/tmp`, worktrees, clean clones, alternate checkouts, public remotes, tags, and Releases remain evidence/reference or disposable-verification surfaces unless user/project authority explicitly selects another root
- dirty, modified, and untracked root state is inspected and preserved pending owner classification; it never authorizes bypass, replacement, or sync-back from public/released state
- README is overview-only
- runtime rules remain the active rule layer and the README-listed exact 19-file runtime set must stay body-sufficient, but Runtime payload parity does not prove full-project convergence
- design remains active target-state truth and governed design/changelog parents must classify chain shape before detail keeps accumulating
- flat sibling shards are valid when the current folder already scopes the chain and the parent still exposes the authority gateway and shard map clearly
- broad mature chains should strongly prefer a compact parent plus active same-stem shard path
- active parent changelogs remain version authority and broad chains should still converge to chain-scoped version detail shards
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with `history/` / `done/` as normalized overflow paths
- worker/context-safe reading begins from parent indexes and the smallest relevant shard or detail surface selected by the declared chain shape
- concern, factual claim, goal request, proposal, and assistant next action should stay separated before endorsement or continuation
- startup, phase, patch, verification, portability, memory, audience-surface, and release boundaries stay with their dedicated owners

---

## Historical Boundary

Older release-by-release rollout narratives are historical context only after the ownership split and do not override the current active runtime/design authority boundary.

Those records belong in [../../changelog/changelog.md](../../changelog/changelog.md), not in this active repository-model shard.
