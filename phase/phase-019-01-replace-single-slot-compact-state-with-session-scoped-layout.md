# Phase 019-01 - Replace single-slot compact state with session-scoped layout

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 019-01
> **Status:** Completed
> **Design References:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Patch References:** [../patch/compact-session-scoped-carry-forward-state-refinement.patch.md](../patch/compact-session-scoped-carry-forward-state-refinement.patch.md)

---

## Objective

Replace singleton compact plugin state with a session-scoped layout that separates pending, selected carry-forward, and proof files per source session.

## Why this phase exists

The previous singleton compact files were bounded, but still structurally weak: they could collide across multiple sessions and could not express many session states safely without turning into mixed global blobs.

## Action points / execution checklist

- [x] replace singleton compact-state path builders with session-directory path builders
- [x] add `index.json` as the small live routing/cleanup file
- [x] add per-session `pending.json`
- [x] add per-session `precompact-context.json`
- [x] add per-session `carry-forward-selected.json`
- [x] add per-session `sessionstart-proof.json`
- [x] change `PreCompact` to create session-scoped state
- [x] change `SessionStart` to resolve exactly one pending source session and fail closed on ambiguity
- [x] change cleanup to prune expired session directories and rewrite the index
- [x] mirror the same runtime behavior into the shared `rules-compact-extension@darkwingtm` bridge package

## Verification

- one compact cycle creates a small index plus a per-session directory tree
- no singleton global handoff/proof files remain as the active model
- carry-forward injection comes from the resolved session’s selected file only
- ambiguous multi-session state does not cause cross-session consume

## Exit criteria

- compact plugin runtime state is session-scoped rather than singleton-scoped
- selected carry-forward state is stored per source session
- proof is local to the session that was resolved or evaluated
- shared runtime bridge stays aligned with the RULES source package
