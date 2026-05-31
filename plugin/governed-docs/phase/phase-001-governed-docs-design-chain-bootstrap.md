# P001 — governed-docs Design Chain Bootstrap

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P001
> **Status:** Completed in checked scope
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Patch References:** [../patch/governed-docs-design-chain-bootstrap.patch.md](../patch/governed-docs-design-chain-bootstrap.patch.md)
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Bootstrap one plugin-local governed design chain for `governed-docs` so the companion model is documented cleanly before implementation begins.

## Why this phase existed

- The governed-docs concept was broad enough that one parent design file alone would immediately become a God file.
- The plugin needed explicit authority boundaries because it operates next to root RULES but must not replace RULES semantics.
- The user added a safety-critical requirement: user-facing operations must require an explicit target workspace path rather than relying on ambient cwd.

## Expected Output

- one compact parent design index under `design/design.md`
- one flat sibling shard set covering the planned architecture and policy surfaces
- one plugin-local changelog parent
- one plugin-local TODO current-state index
- one plugin-local phase summary and current phase file
- one bounded patch artifact for before/after review

## Completion Gate

- all plugin-local governed docs for this wave exist under `plugin/governed-docs/`
- design parent and shard map are readable without becoming a God file
- shard responsibilities are distinct and non-overlapping
- the v1 scope is explicitly RULES-specific first
- the command model explicitly requires a target workspace path and fails closed when omitted
- the wave remains design-only and does not claim implementation behavior

## Out of Scope

- code implementation
- custom agent runtime wiring
- hook wiring
- CLI/skill implementation
- automatic cleanup execution
- any promotion of the plugin into root RULES semantic authority

## Closeout Summary

P001 completed the design-chain bootstrap in checked scope.

Delivered result:
- the governed-docs companion now has a compact parent design, shard map, support docs, and a locked explicit-path safety doctrine

Impact:
- implementation can now start from a checked RULES-specific source of truth instead of continuing from chat-only design notes

Next phase state:
- **P001-01** is the selected first implementation slice for explicit target-path gating and the read-only governed-surface scan foundation
