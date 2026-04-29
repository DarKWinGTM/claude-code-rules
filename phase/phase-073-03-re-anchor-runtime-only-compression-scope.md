# Phase 073-03 - Re-anchor runtime-only compression scope

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-03
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md)
> **Patch References:** [../patch/runtime-rules-semantic-compression-inventory.patch.md](../patch/runtime-rules-semantic-compression-inventory.patch.md)

---

## Objective

Close P073 scope drift before later compression by re-anchoring the target to active root runtime rule files only.

## Why this phase exists

The user clarified that P073 compression must not compress `design/`, `changelog/`, `TODO.md`, `phase/`, or `patch/` surfaces. Those surfaces are planning, audit, history, and synchronization records, not compression targets.

P073 therefore continues only against the active runtime rule files listed in the README install block.

## Baseline refresh

Measured from the current README Bash `rule_files` install list.

| Metric | Current checked state |
|---|---:|
| Active runtime rule files | 41 |
| Missing active runtime files | 0 |
| Current total lines | 7,141 |
| Current total words | 50,141 |
| Current total bytes | 356,403 |

Largest current runtime rule files by words:

| Rule file | Lines | Words | Bytes |
|---|---:|---:|---:|
| `explanation-quality.md` | 641 | 5,410 | 35,561 |
| `accurate-communication.md` | 575 | 4,956 | 35,098 |
| `answer-presentation.md` | 645 | 4,931 | 32,451 |
| `operational-failure-handling.md` | 375 | 2,672 | 20,438 |
| `project-documentation-standards.md` | 254 | 1,847 | 14,118 |
| `phase-implementation.md` | 235 | 1,760 | 12,384 |
| `custom-agent-selection-priority.md` | 190 | 1,645 | 11,180 |
| `runtime-topology-control.md` | 246 | 1,600 | 12,091 |
| `portable-implementation-and-hardcoding-control.md` | 248 | 1,585 | 11,940 |
| `execution-continuity-and-mode-selection.md` | 161 | 1,560 | 10,873 |

## Action points / execution checklist

- [x] Confirm README active runtime install list still contains 41 files.
- [x] Confirm no active runtime rule file from the README list is missing.
- [x] Confirm governed planning surfaces are not compression targets.
- [x] Record current active-runtime-only baseline metrics.
- [x] Define the next valid P073 target as runtime rule owner clusters only.

## Out of scope

- No compression of `design/`, `changelog/`, `TODO.md`, `phase/`, or `patch/` surfaces.
- No runtime install into `~/.claude/rules/`.
- No `CLAUDE.md` edits.
- No plugin, hook, custom-agent source, or unrelated delegation/cleanup work.

## Affected artifacts

- `phase/phase-073-03-re-anchor-runtime-only-compression-scope.md`
- `phase/phase-073-01-verify-patch-coverage-and-repair-master-drift.md`
- `phase/phase-073-02-compress-high-risk-contract-owners-conservatively.md`
- `patch/runtime-rules-semantic-compression-inventory.patch.md`
- `TODO.md`

## TODO coordination

Live execution is tracked by `#1159` for this re-anchor phase.

Durable `TODO.md` should keep P073 active work focused on runtime-rule-only compression and must not represent planning surfaces as compression targets.

## Changelog coordination

Record this as a source-only P073 scope-correction/re-anchor if the later P073 source sync phase updates master changelog. The entry should say no governed planning-surface compression occurred.

## Verification

- [x] Active runtime scope is README-derived and contains 41 files.
- [x] Current active-runtime-only baseline is recorded.
- [x] Governed planning surfaces are explicitly out of compression scope.
- [x] P073 next phases target active runtime rule owner clusters only.
- [x] Source-only boundary remains intact.

## Exit criteria

- P073 no longer describes `design/`, `changelog/`, `TODO.md`, `phase/`, or `patch/` as compression targets.
- Later P073 compression can proceed only by selecting runtime rule owner clusters.
- `073-04` may compress the next selected runtime rule cluster after this re-anchor.

## Next possible phases

- `073-04` — compress the next selected active root runtime rule owner cluster only.
- `073-05` — compress remaining communication, presentation, strategy, and support runtime rule owners only.
- `073-06` — sync governed source records without compressing governed planning surfaces.
- `073-07` — run final semantic parity and aggregate reduction audit for active runtime rule files only.
