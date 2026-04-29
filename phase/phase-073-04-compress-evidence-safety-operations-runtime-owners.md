# Phase 073-04 - Compress evidence, safety, and operations runtime owners

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-04
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md)
> **Patch References:** [../patch/runtime-rules-semantic-compression-inventory.patch.md](../patch/runtime-rules-semantic-compression-inventory.patch.md)

---

## Objective

Compress the next selected active root runtime rule owner cluster after P073-03, preserving behavior while reducing repeated explanation and duplicated examples.

## Runtime rule files in scope

This phase touches only active runtime rule files:
- `accurate-communication.md`
- `anti-sycophancy.md`
- `zero-hallucination.md`
- `no-variable-guessing.md`
- `external-verification-and-source-trust.md`
- `operational-failure-handling.md`
- `runtime-topology-control.md`

## Out of scope

- No compression of `design/`, `changelog/`, `TODO.md`, `phase/`, or `patch/` surfaces.
- No runtime install into `~/.claude/rules/`.
- No `CLAUDE.md` edits.
- No plugin, hook, custom-agent source, or unrelated delegation/cleanup work.

## Preservation targets

- evidence taxonomy and claim-state separation remain intact
- scoped non-finding remains weaker than global absence
- contradiction stays claim-focused and evidence-grounded
- local lookup mechanics remain explicit
- external source trust ranking remains explicit
- operational failure retry ceilings remain bounded
- runtime topology mutation still requires inspect-before-mutate and approval gates
- force words such as `must`, `never`, `verify`, `confirm`, `ask`, and `do not` are not weakened

## Metrics

Measured from the seven selected active runtime rule files in this phase.

| Metric | Pre-compression | Post-compression | Reduction |
|---|---:|---:|---:|
| Lines | 1,925 | 1,571 | 18.4% |
| Words | 13,424 | 10,854 | 19.1% |
| Bytes | 97,597 | 81,802 | 16.2% |

Per-file reduction:

| Rule file | Pre lines | Post lines | Line reduction | Pre words | Post words | Word reduction | Pre bytes | Post bytes | Byte reduction |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `accurate-communication.md` | 575 | 407 | 29.2% | 4,956 | 3,362 | 32.2% | 35,098 | 25,084 | 28.5% |
| `anti-sycophancy.md` | 172 | 130 | 24.4% | 866 | 755 | 12.8% | 6,287 | 5,730 | 8.9% |
| `zero-hallucination.md` | 179 | 151 | 15.6% | 1,062 | 966 | 9.0% | 7,423 | 6,844 | 7.8% |
| `no-variable-guessing.md` | 163 | 140 | 14.1% | 953 | 901 | 5.5% | 6,768 | 6,527 | 3.6% |
| `external-verification-and-source-trust.md` | 215 | 162 | 24.7% | 1,315 | 1,071 | 18.6% | 9,492 | 8,121 | 14.4% |
| `operational-failure-handling.md` | 375 | 335 | 10.7% | 2,672 | 2,308 | 13.6% | 20,438 | 18,088 | 11.5% |
| `runtime-topology-control.md` | 246 | 246 | 0.0% | 1,600 | 1,491 | 6.8% | 12,091 | 11,408 | 5.6% |

## Action points / execution checklist

- [x] Measure pre-compression metrics for the selected runtime files.
- [x] Compress selected runtime rule bodies conservatively/balanced by removing repeated explanation and duplicate examples.
- [x] Verify preserved semantic anchors for each touched file.
- [x] Measure post-compression metrics and reduction.
- [x] Verify source-only boundary.

## TODO coordination

Live execution is tracked by `#1163`.

## Verification

- [x] selected files remain active runtime rule files
- [x] no governed planning surface is compressed
- [x] semantic anchors still exist after compression
- [x] source-only boundary remains intact

Semantic anchor check preserved:
- evidence taxonomy and claim-state separation wording
- scoped non-finding weaker than global absence
- claim-focused contradiction and evidence-before-correction ladder
- local lookup mechanics with `Read`, `Glob`, and `Grep`
- external source trust ladder and source-conflict handling
- bounded retry ceilings, aggregate retry cap, and failure mini-schema
- runtime topology mutation gate, delta classes, and approval-sensitive actions
- Team Agent duplicate/stale-presence guard wording without performing unrelated delegation or cleanup work

## Exit criteria

- [x] Selected runtime rule files are compressed without behavioral weakening.
- [x] Metrics and semantic anchor checks are recorded.
- [x] P073 can proceed to remaining runtime owner compression.

## Next possible phases

- `073-05` — compress remaining communication, presentation, strategy, and support runtime rule owners only.
- `073-06` — sync governed source records without compressing governed planning surfaces.
- `073-07` — run final semantic parity and aggregate reduction audit for active runtime rule files only.
