# Phase 073-02 - Compress high-risk contract owners conservatively

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-02
> **Status:** Completed
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd
> **Design References:** [../design/design.md](../design/design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md), [../design/functional-intent-verification.design.md](../design/functional-intent-verification.design.md), [../design/strict-file-hygiene.design.md](../design/strict-file-hygiene.design.md), [../design/authority-and-scope.design.md](../design/authority-and-scope.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/todo-standards.design.md](../design/todo-standards.design.md), [../design/document-design-control.design.md](../design/document-design-control.design.md), [../design/document-patch-control.design.md](../design/document-patch-control.design.md), [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md)
> **Patch References:** [../patch/runtime-rules-semantic-compression-inventory.patch.md](../patch/runtime-rules-semantic-compression-inventory.patch.md)

---

## Objective

Compress the high-risk contract-owner runtime rules conservatively while preserving force words, safety boundaries, evidence semantics, phase/task behavior, and source-only runtime-install deferral.

## Why this phase exists

P073-01 created the complete 41-rule master patch inventory and froze the initial baseline. P073-02 captured the then-current active runtime-rule baseline before editing high-risk runtime rule bodies.

Current continuation rule: P073 must not use out-of-scope delegation or cleanup work as semantic authority. Before any later P073 compression phase, refresh the active-runtime-only baseline from the current RULES source state and keep `design/`, `changelog/`, `TODO.md`, `phase/`, and `patch/` as sync/audit/planning surfaces only, not compression targets.

The target is conservative reduction for high-risk owners, not maximum compression. Repeated examples and duplicated explanatory prose may be shortened only when the runtime rule set still keeps the same operational contract at equal strength.

## Entry conditions / prerequisites

- P073-01 is completed and the master patch inventory covers all 41 README-installed active runtime rule files.
- The active pre-compression baseline is captured before runtime rule body compression starts.
- Compression remains source-only in this phase.
- Later P073 continuation requires a fresh active-runtime-only baseline after out-of-scope work is excluded from authority.

## Baseline refresh

| Metric | Historical P073-02 active pre-compression baseline |
|---|---:|
| Active runtime rule files | 41 |
| Total lines | 7,341 |
| Total words | 53,627 |
| Total bytes | 379,491 |
| Changed inventory row since P073-01 | `RSC-009` only |
| `RSC-009` current metrics | 177 lines / 1,437 words / 9,818 bytes |

## Action points / execution checklist

- [x] Re-measure the README-installed active runtime rule files before P073-02 high-risk compression.
- [x] Refresh `patch/runtime-rules-semantic-compression-inventory.patch.md` to target master design v9.67 and the then-current baseline metrics.
- [x] Compress `evidence-grounded-burden-of-proof.md` conservatively without weakening claim-state, contradiction, absence, memory, or post-compact thresholds.
- [x] Compress `functional-intent-verification.md` conservatively without weakening destructive-action confirmation, cleanup-is-not-authorization, scope/impact, or safe defaults.
- [x] Compress `strict-file-hygiene.md` conservatively without weakening existing-file-first, no-junk-docs, governed-startup exceptions, or deletion-boundary wording.
- [x] Compress `authority-and-scope.md` conservatively without weakening user authority, fresh-directive override, RULES-first handling, memory applicability boundaries, or git-state authority limits.
- [x] Compress `phase-implementation.md` and `todo-standards.md` conservatively without weakening current-phase-first task shaping, phase-context inspection, live-vs-durable tracking, or future-phase boundaries.
- [x] Compress `document-design-control.md` and `document-patch-control.md` conservatively without weakening design target-state authority, doc-derived knowledge capture, patch before/after reviewability, or phase/patch separation.
- [x] Compress `memory-governance-and-session-boundary.md` and `project-documentation-standards.md` conservatively without weakening memory-as-context, path-primary applicability, startup artifact governance, or source-vs-runtime install boundaries.
- [x] Measure post-compression per-file and aggregate reductions for the touched high-risk owner set.
- [x] Verify semantic parity against the high-risk contract registry in the master patch inventory.
- [x] Verify source-only scope: no runtime install into `~/.claude/rules/`, no `CLAUDE.md` edits, and no plugin/package surface edits.

## Out of scope

- No runtime install into `~/.claude/rules/`.
- No `CLAUDE.md` edits.
- No plugin, hook, custom-agent, support, suspend, or archive edits.
- No compression of lower-risk communication/presentation/support owners in this phase.
- No broad rewrite that moves required runtime behavior only into design, changelog, phase, patch, or TODO surfaces.

## Affected artifacts

Runtime rule bodies in scope:
- `evidence-grounded-burden-of-proof.md`
- `functional-intent-verification.md`
- `strict-file-hygiene.md`
- `authority-and-scope.md`
- `phase-implementation.md`
- `todo-standards.md`
- `document-design-control.md`
- `document-patch-control.md`
- `memory-governance-and-session-boundary.md`
- `project-documentation-standards.md`

Governed companion surfaces in scope:
- `patch/runtime-rules-semantic-compression-inventory.patch.md`
- `phase/phase-073-02-compress-high-risk-contract-owners-conservatively.md`
- `phase/SUMMARY.md`
- `TODO.md`

## TODO coordination

Live execution is tracked through the current built-in task list:
- `#1146` covers P073-02 baseline refresh and phase/TODO alignment.
- `#1147` covers conservative compression of the high-risk runtime owners.
- `#1148` covers semantic parity, reduction measurement, and source-only boundary verification.

Durable `TODO.md` should record P073-02 as active until high-risk compression and verification pass.

## Changelog coordination

The final P073 high-risk compression outcome should be recorded in `changelog/changelog.md` when this phase exits or during the later P073 source-only synchronization phase. The changelog entry must distinguish baseline refresh from actual runtime rule body compression.

## Post-compression metrics

| File | Lines | Words | Bytes | Word reduction |
|---|---:|---:|---:|---:|
| `evidence-grounded-burden-of-proof.md` | 194 | 1,532 | 11,135 | 37.1% |
| `functional-intent-verification.md` | 172 | 910 | 6,530 | 5.4% |
| `strict-file-hygiene.md` | 145 | 764 | 5,823 | 0.7% |
| `authority-and-scope.md` | 170 | 1,215 | 8,640 | 28.9% |
| `phase-implementation.md` | 235 | 1,761 | 12,393 | 22.5% |
| `todo-standards.md` | 233 | 1,516 | 10,178 | 26.1% |
| `document-design-control.md` | 107 | 682 | 5,439 | 7.8% |
| `document-patch-control.md` | 248 | 1,336 | 9,817 | 29.3% |
| `memory-governance-and-session-boundary.md` | 229 | 1,293 | 9,072 | 12.4% |
| `project-documentation-standards.md` | 254 | 1,847 | 14,118 | 23.7% |
| **Touched high-risk set total** | **1,987** | **12,856** | **93,145** | **23.1%** |

Aggregate touched-set reduction: 9.9% lines, 23.1% words, and 21.7% bytes. The reductions remain conservative by design for safety-critical owners.

## Verification

- [x] Active runtime baseline was re-measured from the README install list before P073-02 compression.
- [x] The master patch inventory records the historical P073-02 baseline and RSC-009 metrics from that point in time.
- [x] All touched high-risk rule files preserve the applicable high-risk contracts from the master inventory.
- [x] Force words such as `must`, `never`, `confirm`, `verify`, and `ask first` are not weakened by compression.
- [x] Post-compression metrics are recorded for touched files and aggregate source state.
- [x] No runtime install into `~/.claude/rules/` occurs in this phase.
- [x] No `CLAUDE.md` or plugin/package surfaces are modified.

## Exit criteria

- High-risk runtime owner files are compressed conservatively and remain semantically equivalent.
- The master patch inventory remains the single review surface for the active compression program.
- Reduction metrics are recorded for the touched high-risk owner set.
- Source-only and no-`CLAUDE.md` boundaries pass verification.
- P073-02 task list entries can be marked completed without overclaiming final aggregate 35-45% completion for the whole P073 program.

## Risks / rollback notes

Risk: High-risk owners contain safety and authority contracts that can be weakened by overly aggressive summarization.

Rollback direction:
- restore the last known source wording for any contract that loses operational strength
- prefer smaller reductions over semantic weakening
- keep baseline-refresh history visible, but do not let out-of-scope delegation or cleanup work become authority for later P073 compression
- stop compression if source-only boundary or high-risk contract parity fails

## Next possible phases

- `073-03` — close runtime-compression scope drift and refresh the active-runtime-only target; `design/`, `changelog/`, `TODO.md`, `phase/`, and `patch/` remain sync/audit surfaces only, not compression targets.
- `073-04` — compress the next selected active root runtime rule owner cluster only.
- `073-05` — compress remaining communication, presentation, strategy, and support runtime rule owners only.
- `073-06` — sync governed source surfaces only, with no governed planning-surface compression.
- `073-07` — run final semantic parity and aggregate reduction audit for active runtime rule files only.
