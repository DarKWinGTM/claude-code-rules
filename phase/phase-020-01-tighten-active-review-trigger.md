# Phase 020-01 - Tighten active review trigger

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 020-01
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/compact-active-review-trigger-and-memsearch-assist-refinement.patch.md](../patch/compact-active-review-trigger-and-memsearch-assist-refinement.patch.md)

---

## Objective

Turn the compact SessionStart hook into an explicit active review trigger so resumed continuation is instructed to review stored session data before proceeding.

## Why this phase exists

The earlier navigator signal and selected carry-forward payload improved visibility, but the hook still behaved too passively. The next bounded step is to make the model-facing `additionalContext` explicitly review-oriented.

## Action points / execution checklist

- [x] keep exact `session_id` routing unchanged
- [x] keep the visible navigator-style `systemMessage`
- [x] upgrade success-path `additionalContext` into an explicit review directive
- [x] name the exact per-session review directory on success
- [x] name `precompact-context.json`, `carry-forward-selected.json`, and `sessionstart-proof.json` on success
- [x] tell Claude not to treat the carried-forward summary as settled truth before review when recheck markers exist
- [x] upgrade fallback `additionalContext` so it explicitly points to `index.json` and review-before-continuation behavior
- [x] mirror the same runtime behavior into the shared `rules-compact-extension@darkwingtm` bridge package

## Verification

- success-path `additionalContext` explicitly says review stored session data before continuing
- success-path `additionalContext` names the exact review files for the resolved source session
- fallback `additionalContext` explicitly names `index.json`
- visible navigator signal remains short and operator-facing
- no memsearch runtime dependency is introduced in this phase

## Exit criteria

- compact SessionStart behaves like an active review trigger instead of passive carry-forward-only status
- exact-session review file pointers are visible in model-facing context
- fallback remains fail-closed and review-oriented
- shared runtime bridge stays aligned with the RULES source package
