# governed-docs - TODO

> **Last Updated:** 2026-06-01
> **Current Wave:** P001 phase-backed implementation program completed in checked scope
> **Status:** scanner, evaluator, repair planner, operator entry surfaces, bounded executor policy, release-gate flow, article presentation, and governed-surface closeout are all implemented and locally verified in checked scope
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
- [x] Run final postflight verification: full unittest suite plus `repair-plan`, `release-gate`, and `present-md` smoke checks.

No new implementation wave is currently selected for this plugin-local chain.

## Notes

- All user-facing commands still require an explicit target workspace path.
- `release-gate` now returns `pass` against the governed-docs workspace in checked local scope.
- `present-md` writes local preview output under `generated/article-preview/` and reports that no governed files were edited.
- No hidden hook authority or broad governed-file auto-fix behavior is active.
