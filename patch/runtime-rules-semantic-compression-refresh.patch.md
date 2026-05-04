# Runtime Rules Semantic Compression Refresh Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.84
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch refreshes the P073 semantic compression inventory for the current 43 README-listed active runtime rule files.

The user-selected compression target is semantic-preserving and safety-first:
- preferred reduction: about 7,580-7,944 words
- optional audited upper: about 8,050 words, not forced
- no rule mechanism, safety gate, evidence threshold, phase-lineage behavior, worker-routing behavior, runtime install boundary, or destructive-confirmation contract may be weakened
- compression targets active root runtime rule files only
- governed design/changelog/TODO/phase/patch surfaces remain synchronization and audit records, not compression targets

This patch supersedes the old 41-file P073 compression inventory for the current wave while preserving it as historical P073 evidence.

---

## 2) Analysis

Risk level: High.

Why:
- runtime rules directly shape Claude Code behavior
- many repeated phrases preserve prior user-corrected edge cases
- two new active runtime rules were added after the older P073 baseline
- compression pressure can silently weaken `must`, `never`, `do not`, `confirm`, `verify`, `ask`, `not required`, `observed-only`, and `source-owned` semantics

Compression posture:
- use source-only edits first
- keep no-compress zones near-verbatim when needed
- compress repeated examples, duplicated anti-patterns, repeated integration lists, redundant quality tables, and overlapping owner explanations
- preserve rule statement, core contract, trigger/decision gates, forbidden behaviors, and owner-boundary language
- install runtime only after source semantic audit passes

---

## 3) Current Baseline Measurement

Measured on 2026-05-04 from README-listed active runtime files.

| Metric | Current P073-09 baseline |
|---|---:|
| Active runtime rule files | 43 |
| Total lines | 4,982 |
| Total words | 42,961 |
| Total bytes | 316,988 |
| README Bash install count | 43 |
| README PowerShell install count | 43 |
| Missing source files | 0 |
| Preferred word reduction | 7,580-7,944 |
| Optional audited upper | ~8,050 |

### Active runtime inventory

| Patch ID | Rule file | Lines | Words | Bytes | Risk tier | Planned safe reduction |
|---|---|---:|---:|---:|---|---:|
| RSC2-001 | `accurate-communication.md` | 215 | 2487 | 17987 | High | 500 |
| RSC2-002 | `technical-snapshot-communication.md` | 127 | 638 | 4973 | Medium | 200 |
| RSC2-003 | `response-closing-and-action-framing.md` | 169 | 917 | 6926 | Medium | 200 |
| RSC2-004 | `answer-presentation.md` | 283 | 2319 | 15758 | Medium | 500 |
| RSC2-005 | `anti-mockup.md` | 5 | 15 | 186 | High | 0 |
| RSC2-006 | `anti-sycophancy.md` | 159 | 1234 | 9268 | High | 150 |
| RSC2-007 | `artifact-initiation-control.md` | 129 | 1350 | 9573 | High | 150 |
| RSC2-008 | `authority-and-scope.md` | 134 | 1151 | 8340 | High | 150 |
| RSC2-009 | `custom-agent-selection-priority.md` | 158 | 1300 | 9057 | Medium | 200 |
| RSC2-010 | `dan-safe-normalization.md` | 5 | 14 | 207 | High | 0 |
| RSC2-011 | `document-consistency.md` | 120 | 943 | 7346 | High | 150 |
| RSC2-012 | `document-changelog-control.md` | 57 | 330 | 2827 | High | 150 |
| RSC2-013 | `document-design-control.md` | 118 | 798 | 6263 | High | 150 |
| RSC2-014 | `document-patch-control.md` | 142 | 1313 | 10068 | High | 150 |
| RSC2-015 | `emergency-protocol.md` | 5 | 17 | 219 | High | 0 |
| RSC2-016 | `evidence-grounded-burden-of-proof.md` | 178 | 2249 | 16556 | High | 300 |
| RSC2-017 | `explanation-quality.md` | 264 | 2538 | 17784 | Medium | 500 |
| RSC2-018 | `external-verification-and-source-trust.md` | 105 | 986 | 7657 | High | 150 |
| RSC2-019 | `flow-diagram-no-frame.md` | 5 | 22 | 233 | Medium | 0 |
| RSC2-020 | `functional-intent-verification.md` | 126 | 872 | 6295 | High | 150 |
| RSC2-021 | `memory-governance-and-session-boundary.md` | 96 | 779 | 5896 | High | 150 |
| RSC2-022 | `maintainable-code-structure-and-decomposition.md` | 220 | 2528 | 18116 | Medium | 500 |
| RSC2-023 | `natural-professional-communication.md` | 123 | 846 | 6163 | Medium | 200 |
| RSC2-024 | `native-worker-agent-routing-and-context-control.md` | 218 | 2303 | 16736 | Medium | 500 |
| RSC2-025 | `no-variable-guessing.md` | 140 | 901 | 6527 | High | 150 |
| RSC2-026 | `operational-failure-handling.md` | 139 | 1002 | 8108 | High | 150 |
| RSC2-027 | `phase-implementation.md` | 208 | 1885 | 13551 | High | 300 |
| RSC2-028 | `portable-implementation-and-hardcoding-control.md` | 137 | 1237 | 9622 | High | 150 |
| RSC2-029 | `project-documentation-standards.md` | 187 | 1989 | 15653 | High | 300 |
| RSC2-030 | `recovery-contract.md` | 5 | 14 | 192 | High | 0 |
| RSC2-031 | `refusal-classification.md` | 5 | 14 | 207 | High | 0 |
| RSC2-032 | `refusal-minimization.md` | 5 | 14 | 201 | High | 0 |
| RSC2-033 | `runtime-topology-control.md` | 98 | 788 | 6391 | High | 150 |
| RSC2-034 | `safe-file-reading.md` | 5 | 18 | 222 | High | 0 |
| RSC2-035 | `safe-terminal-output.md` | 5 | 18 | 234 | High | 0 |
| RSC2-036 | `strict-file-hygiene.md` | 119 | 854 | 6578 | High | 150 |
| RSC2-037 | `tactical-strategic-programming.md` | 134 | 1047 | 7973 | Medium | 200 |
| RSC2-038 | `todo-standards.md` | 158 | 1566 | 10648 | High | 300 |
| RSC2-039 | `unified-version-control-system.md` | 5 | 15 | 231 | Medium | 0 |
| RSC2-040 | `zero-hallucination.md` | 124 | 1125 | 8033 | High | 150 |
| RSC2-041 | `high-signal-communication.md` | 93 | 396 | 2820 | Medium | 200 |
| RSC2-042 | `execution-continuity-and-mode-selection.md` | 139 | 1507 | 10935 | Medium | 300 |
| RSC2-043 | `goal-set-review-and-priority-balance.md` | 115 | 622 | 4428 | Medium | 200 |

---

## 4) High-Risk Semantic Anchor Registry

Compression may shorten wording only when these runtime contracts remain active at equal or stronger meaning:

| Anchor ID | Contract that must survive | Primary owner(s) |
|---|---|---|
| P07309-HRC-001 | Claim states stay separate: verified fact, observed local fact, inference, hypothesis, unresolved uncertainty, memory context, post-compact needs-recheck, scoped non-finding, strong absence | `evidence-grounded-burden-of-proof.md`, `zero-hallucination.md`, `accurate-communication.md` |
| P07309-HRC-002 | Factual endorsement, contradiction, completion, synchronization, root-cause, and security claims require evidence at the matching threshold | evidence/communication owners |
| P07309-HRC-003 | User preference/direction is accepted as direction, not upgraded into factual proof | `authority-and-scope.md`, `anti-sycophancy.md`, evidence owners |
| P07309-HRC-004 | Destructive delete/overwrite requires explicit confirmation tied to action and scope | `functional-intent-verification.md` |
| P07309-HRC-005 | Cleanup, hygiene, isolation, worktree, git state, or runtime co-location is not deletion/ownership authority | `strict-file-hygiene.md`, `authority-and-scope.md`, `project-documentation-standards.md` |
| P07309-HRC-006 | Startup artifact posture is resolved before meaningful governed work drifts | `artifact-initiation-control.md` |
| P07309-HRC-007 | Design/changelog/TODO/phase/patch roles stay distinct; built-in task list stays live execution surface | documentation/phase/TODO owners |
| P07309-HRC-008 | Phase lineage gate selects current phase, existing-family subphase, new major, or ask-now based on checked lineage | `phase-implementation.md` and adjacent owners |
| P07309-HRC-009 | Broad/high-output/context-heavy work applies worker routing before leader raw absorption; standalone subagent-first remains distinct from Agent Team escalation | `native-worker-agent-routing-and-context-control.md`, `execution-continuity-and-mode-selection.md` |
| P07309-HRC-010 | Custom-agent selection remains downstream of worker routing and does not force delegation | `custom-agent-selection-priority.md` |
| P07309-HRC-011 | Memory remains context, path scope is primary, session ID is provenance only, and current-state claims require recheck | `memory-governance-and-session-boundary.md` |
| P07309-HRC-012 | Runtime install copies only source-owned README-listed active runtime rules; destination extras stay observed-only unless separately selected | README/install boundary and docs/hygiene owners |
| P07309-HRC-013 | Runtime topology inspect-before-mutate, additive expansion approval, retry budget, and deterministic failure gates remain active | `runtime-topology-control.md`, `operational-failure-handling.md` |
| P07309-HRC-014 | Maintainable code structure preserves responsibility boundaries without helper inflation or comment spam | `maintainable-code-structure-and-decomposition.md` |

---

## 5) Change Items

### Change Item A — Runtime rule body compression

- **Target artifacts:** all 43 README-listed root runtime rule files.
- **Change type:** restructuring.
- **Before:** active runtime rules contain repeated owner lists, anti-pattern tables, examples, trigger tables, quality metrics, integration links, and overlapping explanation of shared evidence/document/phase/worker semantics.
- **After:** runtime rules keep rule statement, core contracts, trigger gates, forbidden behaviors, owner boundaries, verification checklists, and essential examples while removing duplicate wording and delegating overlapping semantics to the correct owner.
- **Verification:** word count, semantic-anchor grep/audit, golden-scenario checks, and selective manual inspection of high-risk owner edits.

### Change Item B — Compression cluster sequencing

- **Target artifacts:** runtime rules grouped by non-overlapping responsibility clusters.
- **Change type:** restructuring.
- **Before:** compression decisions could over-focus on the largest files and miss high-risk owner boundaries.
- **After:** compression proceeds by clusters:
  1. communication/presentation owners
  2. evidence/claim-state owners
  3. documentation governance owners
  4. phase/TODO/execution owners
  5. worker/authority/runtime-safety owners
  6. small/stub/maintainable-code owners
- **Verification:** each cluster reports before/after word deltas and semantic anchors before the next cluster is treated as complete.

### Change Item C — Source-only then runtime install gate

- **Target artifacts:** source runtime rules first, `/home/node/.claude/rules/` second.
- **Change type:** staged replacement.
- **Before:** runtime destination currently matches the v9.83 source-owned 43-file install set.
- **After:** runtime destination is updated only after source compression audits pass, and only for the README-listed active files.
- **Verification:** `missing_source=[]`, `missing_destination=[]`, `hash_mismatches=[]`, destination markdown extras observed-only.

### Change Item D — Governed record synchronization and release

- **Target artifacts:** README, master design, master changelog, TODO, phase summary, this patch, and P073-09 phase file.
- **Change type:** synchronization.
- **Before:** master records described v9.83 / P076-02 as current release state and old P073 compression history through P073-08.
- **After:** master records describe v9.84 / P073-09 as the current 43-file semantic compression release state, including final reduction metrics, runtime install/parity, push, and release.
- **Verification:** source consistency audit, git status/diff/log checks, push success, and GitHub release view.

---

## 6) Verification Plan

Source-only audits before install:
- active runtime files from README Bash and PowerShell arrays match and total 43
- every listed source file exists
- aggregate reduction is in the user-accepted range or stopped by semantic safety gate
- high-risk anchors remain findable and semantically equivalent
- no governed planning/support surfaces are compressed as runtime targets
- no runtime behavior is moved only into design/changelog/TODO/phase/patch surfaces

Golden scenarios:
1. destructive cleanup request still requires explicit confirmation and scoped impact
2. user factual claim still requires evidence before agreement or contradiction
3. scoped non-finding still cannot become global absence
4. phase-shaped follow-up still checks lineage before opening a new major phase
5. broad/noisy/high-context work still routes to the smallest effective worker lane before leader raw absorption
6. standalone subagent remains distinct from teammate/Agent Team workflow
7. custom-agent selection occurs only after worker routing decides delegation/specialist handling is appropriate
8. runtime install copies only README-listed active runtime rules and treats destination extras as observed-only
9. memory remains path-scoped context, not current verified repo truth
10. topology/retry gates still block unapproved additive expansion and deterministic retry loops

Runtime install audits after source pass:
- copy only 43 active runtime source files to `/home/node/.claude/rules/`
- verify source/runtime SHA-256 parity
- report destination markdown extras as observed-only and untouched

### Completed verification

```text
p07309_source_inventory_word_audit=PASS
active_runtime_count=43
source_baseline_words=42961
final_source_words=35017
reduction_words=7944
preferred_reduction_words=7580-7944
within_preferred=true
p07309_behavior_anchor_audit=PASS
p07309_golden_scenario_audit=PASS
p07309_source_boundary_audit=PASS
runtime_install=PASS
runtime_parity=PASS
runtime_parity_files=43/43
missing_source=[]
missing_destination=[]
hash_mismatches=[]
destination_extra_markdown=observed_only
observed_only_destination_extras=[shared-task-list-path-coordination.md, team-agent-coordination.md]
observed_only_source_root_extra=[checkpoint.md]
```

---

## 7) Rollback Approach

- If one rule loses a semantic anchor, restore that file from git and reapply only narrower compression.
- If a cluster fails audit, rollback that cluster before continuing to the next cluster.
- If source/runtime parity fails after install, recopy only README-listed active files and re-run parity.
- If docs sync conflicts with verified source/runtime state, trust checked source/runtime evidence and repair docs before commit.
- If git push or release fails, leave source/runtime state verified and stop for credential or remote-state resolution.
- Do not delete runtime destination extras as rollback; they are outside this source-owned install set unless separately authorized.
