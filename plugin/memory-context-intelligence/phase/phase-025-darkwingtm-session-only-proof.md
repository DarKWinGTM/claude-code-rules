# Phase 025 - darkwingtm session-only proof

## Summary File

[SUMMARY.md](SUMMARY.md)

## Phase ID

025

## Status

Completed / Historical evidence

## Historical Reclassification

Phase 025 remains valid historical checked evidence from the temporary/remapped `darkwingtm` state. After the runtime marketplace mapping was restored to `darkwingtm` -> `<template-plugin-root>`, this phase no longer represents current runtime truth or current `memory-context-intelligence@darkwingtm` availability under the restored shared marketplace.

## Design References

- [../design/design.md](../design/design.md)
- [../design/06-plugin-installability.design.md](../design/06-plugin-installability.design.md)

## Patch References

- [../patch/memory-context-intelligence-design-only-baseline.patch.md](../patch/memory-context-intelligence-design-only-baseline.patch.md)

## Objective

Record the truthful darkwingtm namespace-aligned session proof under the newly verified Claude Code semantics without claiming persistent install or uninstall behavior.

## Why this phase exists

Phase 021 proved only `memory-context-intelligence@inline` through `--plugin-dir`. Phase 024 then selected `memory-context-intelligence@darkwingtm` as the target namespace and preserved phases 020-023 as transitional evidence. Phase 025 exists to close the session-only proof gap without turning session-only disk loading into a false marketplace-qualified identity claim.

## Goal

Explain and preserve the split-proof model now supported by checked Claude Code behavior:

- marketplace-qualified catalog availability under `darkwingtm`
- session-only disk load from the active source home
- the product boundary that direct session-loaded identity remains `@inline`

## Output

Completed split-proof output:

- `claude plugin list --available --json` includes the available marketplace entry `memory-context-intelligence@darkwingtm` with `marketplaceName: "darkwingtm"` and source `./memory-context-intelligence`
- `claude --bare --plugin-dir "<repo-root>/plugin/memory-context-intelligence" plugin list --json` yields `memory-context-intelligence@inline` with `scope: "session"`
- the target marketplace namespace `darkwingtm` is effectively mapped to `<repo-root>/plugin` in the CLI marketplace listing
- direct session-loaded identity does not become `memory-context-intelligence@darkwingtm`; this is a Claude Code product behavior boundary, not a plugin bug
- phase 026 and phase 027 remain planned and approval-sensitive because persistent install and uninstall lifecycle proof are separate runtime-mutation gates

## Gate

Completed in checked scope as a split proof, not as a persistent install proof.

Exact split-proof wording used for this phase:

```text
Phase 025 is completed as a split-proof under current Claude Code semantics: marketplace-qualified availability under `darkwingtm` is proved by `claude plugin list --available --json`, which lists `memory-context-intelligence@darkwingtm` from source `./memory-context-intelligence`, while session-only loading from the active source home is proved separately by `claude --bare --plugin-dir "<repo-root>/plugin/memory-context-intelligence" plugin list --json`, which surfaces `memory-context-intelligence@inline` with `scope: "session"`. Direct session-loaded identity does not become `memory-context-intelligence@darkwingtm`; that `@inline` session identity is a Claude Code product behavior boundary, not a plugin bug. Together, those two checked surfaces form the truthful darkwingtm namespace-aligned session proof: catalog availability is marketplace-qualified, and one-session disk load is inline-scoped.
```

This closes the phase-025 session-only proof gate under current Claude Code semantics while preserving that persistent install and uninstall lifecycle proof still belong to phases 026-027.

## Owner

Plugin session-load verification owner.

## Files

Docs updated for the completed split-proof closeout:

- `phase/SUMMARY.md`
- this phase file
- `design/06-plugin-installability.design.md`
- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `changelog/v0.1.30-completed-darkwingtm-session-split-proof.changelog.md`
- `patch/memory-context-intelligence-design-only-baseline.patch.md`
- `<repo-root>/TODO.md`

Runtime install/uninstall surfaces intentionally not mutated in this phase:

- no persistent install was run
- no uninstall was run
- phases 026-027 remain the planned install/uninstall proof path

## Verification

Verification route: `not_applicable_with_reason` for this docs-only correction turn; the phase record relies on the newly checked Claude Code semantics provided for this correction and does not run install or uninstall commands.

Checked facts recorded in this phase:

```text
claude plugin list --available --json
→ includes memory-context-intelligence@darkwingtm
→ marketplaceName: darkwingtm
→ source: ./memory-context-intelligence
```

```text
claude --bare --plugin-dir "<repo-root>/plugin/memory-context-intelligence" plugin list --json
→ memory-context-intelligence@inline
→ scope: session
```

Covers the darkwingtm namespace-aligned session proof under current Claude Code semantics. Does not cover persistent install, reload/new-process persistence after install, uninstall lifecycle behavior, publication, external marketplace release, slash-command/chat invocation, stable/broad production readiness, main RULES promotion, main RULES mutation, or main RULES merge.

## Risks / limits

- direct session-loaded identity remains `memory-context-intelligence@inline`; expecting `--plugin-dir` to surface `memory-context-intelligence@darkwingtm` would contradict current Claude Code product behavior
- current darkwingtm marketplace remap can cause marketplace mismatch errors for existing installed `@darkwingtm` plugins that are not present in the current `<repo-root>/plugin` marketplace root
- broader shared-marketplace normalization may still be needed later, but phase 025 does not expand scope to fix that
- phase 026 and phase 027 are still approval-sensitive runtime mutation phases and must not be treated as completed by this docs-only split proof

## Rollback notes

Phase 025 is a docs-only correction closeout for the supported split-proof model. It does not install or uninstall `memory-context-intelligence@darkwingtm`, does not intentionally mutate user-scope runtime state, does not touch main RULES phases 017-018, and does not change `/additional/` behavior.

Rollback, if selected, should be limited to reverting the phase-025 governed documentation sync. Do not delete the source package, retained `rules-local` evidence, retained cache/data, current marketplace mappings, existing installed plugin state, or `/additional/` trial material without explicit action-and-scope confirmation.
