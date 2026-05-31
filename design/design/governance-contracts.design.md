# Governance Contracts - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.13
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd (2026-05-17)
> **Section:** Active governance contracts
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Runtime Rule Metadata Contract

Root runtime rules use this canonical header order:
- `Current Version`
- `Design`
- `Session`
- `Full history`

## Synchronization Order

For governed updates:
1. design
2. runtime rule
3. changelog
4. TODO
5. patch metadata final sync when affected

## Startup Artifact Contract

The active startup contract is:
- `phase-todo-artifact.md` owns startup artifact posture
- meaningful governed work resolves artifact posture before drift
- execution continuity does not bypass unresolved startup posture
- required artifacts may be reused, created now, asked now, or marked not required
- required design/changelog/TODO/phase/patch surfaces remain governed companions when the work shape still requires them
- clearly phase-shaped work should expose phase posture and phase-linked task visibility instead of remaining implicit

## Phase Planning Contract

The active phase-planning contract is:
- phased execution consumes normalized design truth one-way
- `phase/SUMMARY.md` is the governed summary/index for live phased execution
- phase identity remains lineage-first
- forward-valid phase grammar explicitly includes `NNN`, `NNN-NN`, and `NNN-NN-NN`
- observed alphanumeric phase forms such as `NNN-NNa` remain legacy-only unless a later doctrine explicitly normalizes them
- deeper hybrid forms such as `NNN-NN-NNb` are not forward-valid grammar by default
- non-trivial phase-backed live tasks visibly link to active or clearly implied phase context
- patch docs remain separate governed review artifacts outside live phase planning

## Completed Documentation Surface Contract

Completed surfaces remain reachable but inactive by default:
- `phase/done/` for completed phase execution detail
- `patch/done/` for completed patch/review artifacts
- `changelog/done/` for older or fallback history
- no default `design/done/` surface because design remains active target-state authority

## Daily-First Rollover Contract

The active rollover contract is:
- `TODO.md` and `phase/SUMMARY.md` remain compact active current-state entrypoints
- daily movement goes to `todo/history/` and `phase/history/`
- large completed/detail surfaces go to `todo/done/` and `phase/done/`
- main entrypoints must keep references to those history/done shards
- rollover is preservation and reference movement, not deletion authority

## Normalized Broad-Chain Contract

When a design or changelog chain is touched for meaningful normalization, classify the chain naming basis and chain shape first:
- `single-file-bootstrap`
- `flat-sibling-shards`
- `same-stem-subfolder-normalized`
- `archive-history-fallback`

Contract:
- first decide whether the current folder already fully scopes one chain or is a shared folder containing several chains
- if the current folder fully scopes one chain, generic parents such as `design/design.md` and `changelog/changelog.md` are valid
- if the current folder is shared by several chains, use subject-derived semantic parent filenames so each chain stays self-identifying in that shared folder
- placeholder names are illustrative only and must not become mandatory literal active names unless they match the checked chain subject
- one chain must keep exactly one active parent model: generic parent or semantic parent, never both at the same time
- `single-file-bootstrap` is valid only while the parent remains compact and coherent enough that detail has not yet outgrown parent-only ownership
- if a chain still has one compact body and no checked `bootstrap_exit_trigger`, keep it bootstrap-first instead of opening same-stem shards early
- `flat-sibling-shards` is valid when the current folder already scopes the chain and only a few coherent slices are needed; the parent remains the compact authority gateway and exposes the active shard map
- `same-stem-subfolder-normalized` remains the strong-preferred form for broad, root-heavy, multi-shard, or God-file-prone chains once a checked `shard_opening_basis` justifies the split
- keep the parent compact as the active authority gateway
- keep child design shards as active target-state truth
- keep changelog version shards as parent-indexed detail, not competing authority
- keep `changelog/done/` as legacy/archive/fallback, not the default active detail path
- do not create a redundant same-stem nested folder until chain-shape classification says the current folder is no longer the right namespace and a real shard-opening basis exists
- keep `observed project shape` as the checked example structure only
- keep `extracted doctrine` as the reusable governance lesson inferred from that checked structure
- keep `selected target form` as the structure intentionally chosen for the current RULES chain
- do not describe the selected target form as the literal observed project pattern unless checked equivalence evidence supports that claim

## Memory Governance Contract

The active memory-governance contract is:
- `memory-governance-and-session-boundary.md` owns memory boundary and applicability behavior
- root `MEMORY.md` stays as a compact active index, not a full dump or link-only router
- path remains the primary applicability key and session IDs remain provenance only
