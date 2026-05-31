# governed-docs - TODO

> **Last Updated:** 2026-06-01
> **Current Wave:** P002 preview portal and sync wave completed in checked scope
> **Status:** P001 and P002 are implemented and locally verified in checked scope; no new implementation wave is currently selected
> **History:** none opened yet
> **Done Detail:** none opened yet

---

## Current

- [x] Convert the design-only posture into the P001 implementation program.
- [x] Open child phase files for the full v1 implementation wave: scanner, evaluator, repair planner, operator skill/agent surfaces, bounded executor boundary, release-gate flow, and article presentation.
- [x] Implement **P001-01** explicit target-workspace-path enforcement and the read-only governed-surface scan foundation.
- [x] Implement **P001-02** Layer B doctrine evaluator and maintenance problem-class classification.
- [x] Implement **P001-03** repair planner and generated review artifacts.
- [x] Implement **P001-04** operator skill surfaces and custom agent entry scaffolds.
- [x] Implement **P001-05** bounded executor policy and hook-light guardrails.
- [x] Implement **P001-06** release-gate flow and closeout consistency.
- [x] Implement **P001-07** governed-docs-owned Markdown/article presentation.
- [x] Add the plugin-local `README.md` front page so the governed-docs workspace satisfies the active governed-surface inventory.
- [x] Run final postflight verification for P001: full unittest suite plus `repair-plan`, `release-gate`, and `present-md` smoke checks.
- [x] Open and sync the P002 preview portal and sync wave across design / TODO / phase / patch.
- [x] Refactor `present-md` from `generated/article-preview/` to the root `preview/` path contract.
- [x] Implement `present-sync` for full preview-site rebuild/sync across governed doc families.
- [x] Add preview portal shell plus bounded preview helper subagents.
- [x] Run final P002 tests + smoke checks and verify sync mutates only `preview/**` while governed source docs stay unchanged.

No new implementation wave is currently selected for this plugin-local chain.

## Notes

- All user-facing commands still require an explicit target workspace path.
- `present-md` now writes into root `preview/` instead of `generated/article-preview/`.
- `present-sync` rebuilds `preview/index.html`, `preview/manifest.json`, and family pages under `preview/**`.
- `present-sync` is verified in checked local scope to leave selected governed source hashes unchanged.
- No hidden hook authority or broad governed-file auto-fix behavior is active.
