# Master Changelog - governed-docs

> **Project:** governed-docs plugin design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Selected Parent Model:** generic parent
> **Selected Chain Shape:** single-file-bootstrap

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 0.1.0 | 2026-06-01 | **Created the initial RULES-native governed-docs design chain and synchronized plugin-local design/TODO/phase/patch documentation** | b7f7ee85-27ec-467a-ba63-568c831fcd36 |

---

<a id="version-010"></a>
## Version 0.1.0: Created the initial governed-docs design chain bootstrap

**Date:** 2026-06-01
**Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36

### Changes
- Created a plugin-local design parent and flat sibling shard map under `plugin/governed-docs/design/`.
- Locked the plugin purpose, v1 RULES-specific scope, and RULES-vs-plugin authority boundary.
- Defined the four-layer architecture: scanner, doctrine evaluator, repair planner, and bounded executor.
- Defined the governed surface inventory and the six maintenance problem classes.
- Defined the planned skill set, custom agent set, generated artifact model, hook posture, and release-gate model.
- Added the explicit target-workspace-path command requirement so user-facing operations fail closed instead of relying on ambient cwd.
- Synchronized plugin-local `TODO.md`, `phase/SUMMARY.md`, one phase file, and one patch artifact for the design wave.

### Summary
This bootstrap establishes `governed-docs` as a RULES-native companion design chain. It is design-only, does not implement runtime wiring, and keeps semantic authority in root RULES while giving the plugin a defined maintenance-support role.

---

## Working note: first implementation slice under the current design baseline

**State:** implemented and tested in checked scope; this is not a new release tag.

**Date:** 2026-06-01
**Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36

### Added runtime surfaces
- `src/governed_docs/target_path.py`
- `src/governed_docs/scan_result.py`
- `src/governed_docs/surface_scanner.py`
- `src/governed_docs/commands/scan.py`
- `tests/test_target_path.py`
- `tests/test_surface_scanner.py`
- `tests/test_scan_command.py`

### Behavior now implemented in checked scope
- user-facing scan behavior requires one explicit target workspace path
- missing, non-existent, and file-path targets hard-stop before scan work begins
- the scanner inventories the current read-only governed surface foundation from the named target path only
- inactive `history/` / `done/` surfaces are classified as inactive/referenced rather than cleanup targets
- the command layer remains report-only and explicitly states that no files were edited

### Verification
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && python3 -m unittest discover -s tests -v` → 9 tests passed
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && PYTHONPATH=src python3 -m governed_docs.commands.scan /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` → report-only scan output with no file edits
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && PYTHONPATH=src python3 -m governed_docs.commands.scan` → exit code 1 with explicit target-path error

### Notes
- This first slice is still Layer A only: no doctrine evaluator, repair planner, executor, hook wiring, or agent wiring is implemented yet.
- The checked NodeClaw article reference shows that Markdown/article HTML presentation should be opened as a separate later phase rather than folded into the first scanner slice.

---

## Working note: phase-backed implementation program expansion

**State:** synced in checked scope; phase coverage expanded without overclaiming later slices as implemented.

**Date:** 2026-06-01
**Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36

### Changes
- Expanded `phase/SUMMARY.md` so the v1 implementation wave explicitly covers scanner, evaluator, repair planner, skill/agent entry surfaces, bounded executor policy/hook guardrails, and release-gate flow.
- Opened child phase files `P001-02` through `P001-06` with objective / expected output / gate / out-of-scope / affected-artifact boundaries.
- Added `P001-07` as a separate later proposal phase for Markdown/article presentation based on the checked NodeClaw article reference.
- Re-synchronized `TODO.md` and patch surfaces so the opened later phases are visible without being overstated as completed implementation.

### Verification
- checked scope confirms that the later required implementation-wave coverage is now represented in explicit child phase files
- P001-01 remains the only runtime slice claimed implemented in checked scope
- no later slice is claimed release-ready or complete without its own proof route

### Notes
- this working note expands the phase program only; it does not add new runtime behavior beyond the already verified first scanner slice

---

## Working note: P001-02 doctrine evaluator and problem-class classification

**State:** implemented and tested in checked scope; this is not a new release tag.

**Date:** 2026-06-01
**Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36

### Added runtime surfaces
- `src/governed_docs/finding_models.py`
- `src/governed_docs/doctrine_evaluator.py`
- `tests/test_doctrine_evaluator.py`

### Behavior now implemented in checked scope
- evaluator runtime consumes `ScanResult` read-only and emits doctrine findings
- evaluator exposes classification states `compliant`, `legacy-but-allowed`, `drift`, `ambiguous-needs-basis`, `safe-auto-repair`, and `blocked`
- evaluator maps the main maintenance problem classes: role drift, structure drift, rollover pressure, phase grammar drift, release sync drift, and preservation risk
- evaluator remains separate from repair planning, executor behavior, hook wiring, and article-style presentation

### Verification
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && python3 -m unittest discover -s tests -v` → 17 tests passed
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && PYTHONPATH=src python3 - <<'PY' ... scan_governed_surfaces(...) + evaluate_scan_result(...) ... PY` → read-only scanner→evaluator runtime emitted compliant + drift findings in checked scope for the governed-docs workspace
- existing explicit-path scan command behavior remained intact after evaluator implementation

### Notes
- P001-02 is still Layer B only: no repair planner, generated repair artifacts, bounded executor, hook wiring, public skill installation, or release-gate flow is implemented yet.
- Markdown/article HTML presentation remains a separate later phase and was not implemented here.

---

## Working note: remaining runtime layers, article presentation, and governed-surface closeout

**State:** implemented and tested in checked scope; this is not a new release tag.

**Date:** 2026-06-01
**Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36

### Added and synchronized surfaces
- `src/governed_docs/generated_artifacts.py`
- `src/governed_docs/repair_planner.py`
- `src/governed_docs/commands/repair_plan.py`
- `src/governed_docs/executor_policy.py`
- `src/governed_docs/normalizer.py`
- `src/governed_docs/hook_guardrails.py`
- `src/governed_docs/release_gate.py`
- `src/governed_docs/commands/release_gate.py`
- `src/governed_docs/article_presentation.py`
- `src/governed_docs/commands/present_md.py`
- `.claude-plugin/plugin.json`
- `bin/governed-docs`
- `skills/scan/SKILL.md`
- `skills/review/SKILL.md`
- `skills/repair-plan/SKILL.md`
- `skills/phase-audit/SKILL.md`
- `skills/release-gate/SKILL.md`
- `skills/present-md/SKILL.md`
- `agents/governed-docs-scout.md`
- `agents/governed-docs-doctrine-evaluator.md`
- `agents/governed-docs-repair-architect.md`
- `agents/governed-docs-normalizer.md`
- `agents/governed-docs-release-auditor.md`
- `agents/governed-docs-phase-lineage-auditor.md`
- `.claude/hooks/governed-docs-reminder.sh`
- `design/07-article-markdown-presentation.design.md`
- `README.md`
- `tests/test_generated_artifacts.py`
- `tests/test_repair_planner.py`
- `tests/test_executor_policy.py`
- `tests/test_bounded_normalizer.py`
- `tests/test_entry_surfaces.py`
- `tests/test_release_gate.py`
- `tests/test_article_presentation.py`
- `tests/test_present_md_command.py`
- `tests/test_cli_router.py`
- later-phase patch artifacts plus final `TODO.md` / `phase` / `changelog` closeout sync

### Behavior now implemented in checked scope
- doctrine findings can be transformed into bounded repair-plan artifacts with explicit approval boundaries
- operator entry surfaces now exist through a plugin manifest, bin router, skill wrappers, and agent scaffolds
- bounded executor policy remains preview-only for safe candidates and keeps blocked classes blocked
- hook guardrails remain advisory/support-only rather than hidden governance authority
- release-gate verdict flow now returns explicit closeout states from the checked governed-surface set
- governed-docs now owns a Markdown-to-HTML article preview path with safe-link handling and TOC generation
- the plugin-local chain now includes its README front page, allowing the active governed-surface set to satisfy the scanner/release-gate inventory in checked local scope

### Verification
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && python3 -m unittest discover -s tests -v` → 40 tests passed
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && ./bin/governed-docs repair-plan /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` → emitted a read-only repair-plan artifact with `Mutated: False`
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && ./bin/governed-docs release-gate /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` → returned `Verdict: pass`
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && ./bin/governed-docs present-md /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs design/07-article-markdown-presentation.design.md` → generated `generated/article-preview/07-article-markdown-presentation-design.html` and reported `No governed files were edited.`

### Notes
- all user-facing command paths still require explicit target workspace paths and do not fall back to ambient cwd
- this closeout is verified in checked local scope for the plugin workspace; it is not a claim about external deployment or broader runtime environments

---

## Working note: P002 preview portal and sync wave

**State:** implemented and tested in checked scope; this is not a new release tag.

**Date:** 2026-06-01
**Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36

### Added and synchronized surfaces
- `src/governed_docs/preview_paths.py`
- `src/governed_docs/preview_site.py`
- `src/governed_docs/commands/present_sync.py`
- `skills/present-sync/SKILL.md`
- `agents/governed-docs-present-inventory-scout.md`
- `agents/governed-docs-present-architect.md`
- `agents/governed-docs-present-renderer.md`
- `agents/governed-docs-present-sync-auditor.md`
- `design/08-preview-portal-and-sync.design.md`
- `phase/phase-002-preview-portal-and-sync-wave.md`
- `phase/phase-002-01-preview-path-and-present-md-refactor.md`
- `phase/phase-002-02-present-sync-site-build.md`
- `phase/phase-002-03-preview-portal-ui-and-subagents.md`
- `phase/phase-002-04-preview-wave-verification-and-closeout.md`
- `patch/preview-portal-and-sync-wave.patch.md`
- updated `README.md`, `TODO.md`, `phase/SUMMARY.md`, `.gitignore`, and preview-related tests/docs

### Behavior now implemented in checked scope
- `present-md` now writes to the root `preview/` portal structure instead of `generated/article-preview/`
- `present-sync` rebuilds `preview/index.html`, `preview/manifest.json`, and family pages from governed source docs
- preview portal output is bounded to `preview/**`
- selected governed source docs remain unchanged across sync verification
- preview helper skill/agent surfaces exist for inventory, architecture, rendering, and sync auditing

### Verification
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && python3 -m unittest discover -s tests -v` → 45 tests passed
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && ./bin/governed-docs present-md /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs design/07-article-markdown-presentation.design.md` → wrote `preview/design/07-article-markdown-presentation/index.html`
- `cd /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs && ./bin/governed-docs present-sync /home/node/workplace/AWCLOUD/TEMPLATE/RULES/plugin/governed-docs` → generated `preview/index.html` and `preview/manifest.json`
- selected source-hash verification confirmed that `TODO.md`, `phase/SUMMARY.md`, `design/design.md`, and `patch/preview-portal-and-sync-wave.patch.md` stayed unchanged across `present-sync`
- leftover `generated/article-preview/` artifact was removed after the root `preview/` migration

### Notes
- the preview tree is a presentation/support surface only and not a governed source-of-truth document family
- no background auto-sync path was added; sync remains explicit-command driven in checked scope
- ambient cwd fallback remains blocked for both `present-md` and `present-sync`
