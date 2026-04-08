# Phase 018-01 - Replace latest witness model with ephemeral handoff

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 018-01
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/compact-ephemeral-handoff-lifecycle-refinement.patch.md](../patch/compact-ephemeral-handoff-lifecycle-refinement.patch.md)

---

## Objective

Replace the plugin’s latest-only compact witness model with a one-shot ephemeral handoff lifecycle.

## Why this phase exists

The current plugin already loads and its hooks already fire, but the latest-only witness files keep compact artifacts longer than needed and can preserve stale unrelated state. The package should act like a short-lived handoff cache instead.

## Action points / execution checklist

- [x] replace raw witness-file behavior with one `active-handoff.json` contract
- [x] add shared helper logic for compact data-dir resolution, TTL, and prune behavior
- [x] change `PreCompact` to create/refresh handoff state
- [x] change compact `SessionStart` to consume/delete handoff state, emit the compact-resume signal plus re-anchor reminder, and leave one bounded `last-sessionstart-consumed.json` proof file
- [x] change `PostCompact` to prune-only behavior
- [x] remove active package references to `last-precompact.json`, `last-postcompact.json`, and `last-sessionstart-compact.json`

## Verification

- plugin runtime files and hook wiring now describe one ephemeral handoff lifecycle
- the implementation no longer centers on latest-only witness storage
- the package remains support-only and hook-first

## Exit criteria

- plugin runtime behavior is defined around one-shot handoff creation, consume/delete, and prune-only cleanup
- the old latest-witness model is no longer the active package contract
- the package remains clearly subordinate to root RULES authority
