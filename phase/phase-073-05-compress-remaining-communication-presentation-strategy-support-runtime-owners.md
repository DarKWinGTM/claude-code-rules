# Phase 073-05 - Compress remaining communication, presentation, strategy, and support runtime owners

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-05
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md)
> **Patch References:** [../patch/runtime-rules-semantic-compression-inventory.patch.md](../patch/runtime-rules-semantic-compression-inventory.patch.md)

---

## Objective

Compress the remaining selected active root runtime rule owner cluster for P073, preserving behavior while reducing repeated explanation, duplicated examples, and cross-owner overlap.

พูดง่าย ๆ: phase นี้เก็บ rule ที่เหลือซึ่งยังยาวเพราะมีตัวอย่าง/คำอธิบายซ้ำกัน แล้วบีบให้สั้นลงโดยไม่ลดกฎจริงที่ Claude ต้องทำตาม.

## Runtime rule files in scope

This phase touches only active runtime rule files from the README install list:
- `technical-snapshot-communication.md`
- `response-closing-and-action-framing.md`
- `answer-presentation.md`
- `explanation-quality.md`
- `natural-professional-communication.md`
- `high-signal-communication.md`
- `execution-continuity-and-mode-selection.md`
- `goal-set-review-and-priority-balance.md`
- `tactical-strategic-programming.md`
- `portable-implementation-and-hardcoding-control.md`
- `document-consistency.md`

## Out of scope

- No compression of `design/`, `changelog/`, `TODO.md`, `phase/`, or `patch/` surfaces.
- No runtime install into `~/.claude/rules/`.
- No `CLAUDE.md` edits.
- No plugin, hook, custom-agent source, or unrelated delegation/cleanup work.

## Preservation targets

- exact/partial/inferred technical snapshot separation remains intact
- scoped local-fact wording remains intact
- closing synthesis, recommendation-with-reason, alternative preservation, and advisory proposal boundaries remain intact
- presentation layout ownership remains intact, including light table, snapshot, scope-boundary, full-set-first, next-stage, post-compact, memory-status, and variable-role patterns
- explanation flow remains plain-language-first with claim/mechanism/implication, diagnostic snapshot placement, easy-explanation continuity, stage progression, and governing-basis clarification
- natural professional tone remains signal-over-ceremony and non-persona-driven
- high-signal filtering remains a supplementary tightening layer, not an ultra-short-answer mandate
- execution continuity keeps discussion-vs-execution mode, startup gate, continuation-first behavior, next-work discovery, and legitimate stop gates
- goal-set review keeps full active goal-set visibility, priority balance, and structure-first behavior
- tactical/strategic programming keeps strategic target, convergence path, bounded tactical scope, and no permanent tactical drift
- portable implementation keeps portable core, late binding, observed-local-fact separation, source-vs-destination notation, and anti-hardcoding boundaries
- document consistency keeps verified references, source/destination/runtime/local role separation, and master-surface consultation before file classification
- force words such as `must`, `never`, `verify`, `confirm`, `ask`, and `do not` are not weakened

## Baseline metrics

Measured from the eleven selected active runtime rule files before P073-05 compression on 2026-04-24.

| Metric | Pre-compression |
|---|---:|
| Lines | 2,777 |
| Words | 20,565 |
| Bytes | 141,826 |

Per-file baseline:

| Rule file | Lines | Words | Bytes |
|---|---:|---:|---:|
| `technical-snapshot-communication.md` | 164 | 1,013 | 7,554 |
| `response-closing-and-action-framing.md` | 167 | 1,311 | 9,278 |
| `answer-presentation.md` | 645 | 4,931 | 32,451 |
| `explanation-quality.md` | 641 | 5,410 | 35,561 |
| `natural-professional-communication.md` | 203 | 1,345 | 9,473 |
| `high-signal-communication.md` | 98 | 482 | 3,293 |
| `execution-continuity-and-mode-selection.md` | 161 | 1,560 | 10,873 |
| `goal-set-review-and-priority-balance.md` | 114 | 860 | 5,923 |
| `tactical-strategic-programming.md` | 174 | 1,116 | 8,250 |
| `portable-implementation-and-hardcoding-control.md` | 248 | 1,585 | 11,940 |
| `document-consistency.md` | 162 | 952 | 7,230 |

## Action points / execution checklist

- [x] Confirm P073-05 phase file did not already exist.
- [x] Record active-runtime-only scope and pre-compression metrics.
- [x] Compress selected runtime rule bodies conservatively/balanced by removing repeated explanation and duplicate examples.
- [x] Verify preserved semantic anchors for each touched file.
- [x] Measure post-compression metrics and reduction.
- [x] Verify source-only boundary.

## Post-compression metrics

Measured after P073-05 source-only runtime body compression on 2026-04-24.

| Metric | Pre-compression | Post-compression | Reduction |
|---|---:|---:|---:|
| Lines | 2,777 | 2,158 | 22.3% |
| Words | 20,565 | 12,032 | 41.5% |
| Bytes | 141,826 | 86,856 | 38.8% |

Per-file result:

| Rule file | Pre lines | Post lines | Line reduction | Pre words | Post words | Word reduction | Pre bytes | Post bytes | Byte reduction |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `technical-snapshot-communication.md` | 164 | 127 | 22.6% | 1,013 | 638 | 37.0% | 7,554 | 4,973 | 34.2% |
| `response-closing-and-action-framing.md` | 167 | 139 | 16.8% | 1,311 | 734 | 44.0% | 9,278 | 5,552 | 40.2% |
| `answer-presentation.md` | 645 | 392 | 39.2% | 4,931 | 2,290 | 53.6% | 32,451 | 15,447 | 52.4% |
| `explanation-quality.md` | 641 | 371 | 42.1% | 5,410 | 2,331 | 56.9% | 35,561 | 16,125 | 54.7% |
| `natural-professional-communication.md` | 203 | 176 | 13.3% | 1,345 | 898 | 33.2% | 9,473 | 6,582 | 30.5% |
| `high-signal-communication.md` | 98 | 93 | 5.1% | 482 | 396 | 17.8% | 3,293 | 2,820 | 14.4% |
| `execution-continuity-and-mode-selection.md` | 161 | 164 | -1.9% | 1,560 | 1,104 | 29.2% | 10,873 | 7,829 | 28.0% |
| `goal-set-review-and-priority-balance.md` | 114 | 115 | -0.9% | 860 | 622 | 27.7% | 5,923 | 4,428 | 25.2% |
| `tactical-strategic-programming.md` | 174 | 177 | -1.7% | 1,116 | 936 | 16.1% | 8,250 | 6,994 | 15.2% |
| `portable-implementation-and-hardcoding-control.md` | 248 | 237 | 4.4% | 1,585 | 1,275 | 19.6% | 11,940 | 9,835 | 17.6% |
| `document-consistency.md` | 162 | 167 | -3.1% | 952 | 808 | 15.1% | 7,230 | 6,271 | 13.3% |

## TODO coordination

Live execution is tracked by `#1161`.

## Changelog coordination

P073-05 changelog/master-history synchronization is deferred to the P073-06 source-only governed-record sync phase unless a narrow local status row is needed during this phase.

## Verification

- [x] selected files are active runtime rule files in the README install list
- [x] governed planning surfaces are excluded from compression
- [x] semantic anchors still exist after compression
- [x] source-only boundary remains intact

Semantic anchor check result: all anchors present.

Source-only boundary check result: no runtime install into `~/.claude/rules/`, no `CLAUDE.md` edits, no plugin/hook/custom-agent source edits, and no unrelated delegation/cleanup work in this phase.

## Exit criteria

- [x] Selected runtime rule files are compressed without behavioral weakening.
- [x] Metrics and semantic anchor checks are recorded.
- [x] P073 can proceed to source-only governed record sync.

## Next possible phases

- `073-06` — sync governed source records without compressing governed planning surfaces.
- `073-07` — run final semantic parity and aggregate reduction audit for active runtime rule files only.
