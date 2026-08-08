# Phase 073-11 - Runtime Owner Semantic Conflict Resolution and Compression

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-11
> **Status:** Active — release verification pending
> **Target Release:** v10.57
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/design.md](../design/design.md), [../design/action-safety.design.md](../design/action-safety.design.md), [../design/refusal-and-recovery.design.md](../design/refusal-and-recovery.design.md), [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md), [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md), [../design/external-verification-and-source-trust.design.md](../design/external-verification-and-source-trust.design.md), [../design/document-integrity.design.md](../design/document-integrity.design.md), [../design/communication-register.design.md](../design/communication-register.design.md), [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md), [../design/document-governance.design.md](../design/document-governance.design.md), [../design/worker-routing-and-context.design.md](../design/worker-routing-and-context.design.md)
> **Patch References:** [../patch/runtime-owner-semantic-conflict-resolution-and-compression.patch.md](../patch/runtime-owner-semantic-conflict-resolution-and-compression.patch.md)

---

## Objective

Resolve six checked semantic ambiguities, integrate the complete image-derived strategy set into existing canonical owners, and compact the 19 Active Runtime Rules without weakening combined behavior, exact guards, approval/stop/recovery gates, or runtime body sufficiency.

พูดง่าย ๆ: ลด context ด้วยการรวมความหมายที่ซ้ำให้เหลือ owner เดียว ไม่ใช่ตัดความสามารถหรือคำเตือนที่ป้องกัน silent error.

## Lineage Decision

- No current active phase exists, so current-phase update is unavailable.
- P073-09 and P073-10 already own active-runtime compression, installation, parity, and body-sufficiency correction.
- This wave preserves the same 19-Rule capability boundary and verification/rollback family; it does not introduce a new runtime architecture.
- Therefore `073-11` is the smallest truthful existing-family child. A new major is not justified.

## Baseline and Target

| Metric | Baseline | Target posture | Checked candidate |
|---|---:|---:|---:|
| Active Runtime Rules | 19 | 19 unchanged | 19 |
| Total bytes | 273,721 | reduce safely by about 18,000-24,000 | 254,032; down 19,689 (7.19%) |
| `document-governance.md` | 27,850 | approximately 21-22 KB | 18,834 |
| `phase-todo-artifact.md` | 25,346 | approximately 20-21 KB | 17,148 |
| `explanation-and-presentation.md` | 25,158 | approximately 18-19 KB | 16,494 |
| Checked pre-compression baseline | 405,914 | preserve combined behavior while reducing context | down 151,882 (37.42%) |

Metric targets do not authorize weakening force words, semantic guards, or rare high-consequence safety behavior.

## Selected Semantic Obligations

1. Operational runtime workers/jobs/entities remain distinct from Claude subagents and Agent Team teammates.
2. Malicious or unauthorized destruction may be `HARD_BLOCK`; authorized bounded destructive work follows `action-safety.md` confirmation.
3. Smallest safe reversible emergency containment may precede full artifact startup only when delay materially increases immediate harm; normal governance resumes immediately afterward.
4. `implemented` is intermediate while material verification remains; terminal closeout is verified or explicitly carried forward.
5. Public read-only lookup is evidence gathering; consequential authenticated/private/mutating/sending/purchasing external action remains approval-sensitive.
6. Active startup ownership points to `phase-todo-artifact.md`; historical absorbed-owner provenance remains historical.
7. Reader-facing supporting explanation is opt-in and non-repetitive, but required when silence hides material risk, ambiguity, irreversible effect, verification limits, confirmation/recovery, or a necessary next action.
8. The remaining image strategies stay with existing owners: conditional planning, verification-before-done, simplicity/minimal impact, evidence-first diagnosis, built-in tasks live/TODO durable, and durable-value memory writes.
9. Primary source implementation and final integration stay in the context-rich leader session. Invocation follows work shape: one standalone subagent for one bounded independent axis; parallel standalone dispatch for independent research/review/testing/metrics matrix cells; Agent Team/teammates only for real shared dependencies, staged coordinated testing, or cross-lane messaging. Helpers do not autonomously change Active Rule/product source, README, integration, installation, git, or release state.

## Lane Map

### Lane 1 - Design and Semantic Settlement

- establish owner decisions in touched design companions
- resolve the six conflict anchors
- preserve exact literals and force-word strength

### Lane 2 - Owner-Canonical Compression

- compact document governance/integrity
- compact phase/execution/goal
- compact communication/rendering
- compact only verified coding/evidence/worker/safety mirrors

### Lane 3 - Verification and Installation

- invoke one standalone subagent for one bounded verification axis; invoke independent test/metrics/matrix cells together as parallel standalone lanes with one shared rubric
- use teammates only when a staged test workflow has shared fixtures/state, dependencies, or cross-lane messaging that standalone lanes cannot coordinate cleanly
- group potentially related failures before fan-out, reuse or steer aligned workers, and require filtered handoffs; leader verifies selected anchors, resolves conflicts, applies source fixes, reruns proportionate tests, and owns the combined completion claim
- verify 19-file manifests, exact guards, body sufficiency, references, metrics, and README scope
- test disposable installation with unrelated-file preservation
- synchronize the verified allowlist to canonical source
- install 19 Rules to the user runtime target and verify 19/19 parity

### Lane 4 - Governance and Release

- synchronize touched design/changelog chains, master records, TODO, phase, patch, and surgical README current-state anchors
- push only clean `master`, publish the annotated release tag, and verify a fresh public clone

## Out of Scope

- adding, deleting, merging, or renaming Active Rule files
- rewriting README structure, onboarding, or unrelated wording
- rewriting completed historical phases or patches
- plugin, playground, companion-plugin, or installer architecture changes unless the active 19-file contract actually changes
- deleting or pushing `backup/active-rules-source-2026-08-05`
- claiming Claude Code warning elimination without a controlled runtime witness

## Development Verification / TestKit Coverage

This phase changes runtime governance text, not product code. No product TestKit scenario applies. Verification uses deterministic rule inventory, semantic guards, force-word review, payload metrics, source/install hashes, body sufficiency, disposable install behavior, README no-churn checks, and release identity.

Required checks:

- Bash and PowerShell manifests match in the same order and count 19
- no Active Rule file is added, removed, renamed, merged, or reduced to a pointer-only body
- all exact enum/literal families remain
- all six conflicts have one unambiguous settlement
- full image-derived strategy coverage remains visible without duplicate doctrine
- source and installed body sufficiency pass 19/19
- unrelated destination Rules remain untouched
- README changes are exact-anchor current-state updates only
- remote master, peeled annotated tag, GitHub Release, canonical source, installed runtime, and fresh clone align

## Risks and Rollback

Risks:
- compression can silently weaken `must`, `never`, `only`, `confirm`, `verify`, `block`, or `stop`
- consumer handoffs can become circular or point to non-runtime design-only truth
- broad README or historical-document edits can hide unrelated churn
- the dirty backup checkout can contaminate a release

Mitigation:
- work from a clean remote-master clone
- verify one owner cluster at a time
- preserve exact guards and inspect force-word deltas
- use an explicit changed-path allowlist
- synchronize to canonical source only after overlap checks

Rollback:
- before publication, discard only the clean release lane's scoped candidate changes
- after public release, use a corrective commit/release; do not force-move a public tag
- runtime rollback requires explicit approval and reinstalls the known-good v10.56 19-Rule set while preserving unrelated destination files

## Current Verification and Semantic Disposition

Source-candidate checks completed:
- all nine selected semantic obligations are implemented and verified in the checked source scope
- independent read-only reviews identified and the leader repaired material regressions in phase/TODO, presentation, document governance, worker routing, and destructive-confirmation ordering
- Active Rule count is 19; static body sufficiency is 19/19; exact literal/enum registry and selected high-risk clause checks pass
- final candidate payload after explicit helper-invocation routing is 254,032 bytes, 3,092 lines, and 33,038 words; semantic/static, 39-path allowlist, 10/10 triad, changed-link, `git diff --check`, and README 7/7/mode checks pass
- Bash/PowerShell disposable installs pass 19/19 with unrelated-sentinel preservation; the latest allowlist is synchronized to canonical source and canonical/root SHA-256 parity plus body sufficiency pass 19/19 while unrelated root Rules remain preserved

Terminal phase disposition remains `blocked` on publication verification only. This is not yet a completed or released phase.

## Exit Criteria

- all selected semantic obligations are `verified` or explicitly carried forward
- Active Rule count remains 19
- safe payload reduction is measured and reported without overclaiming warning elimination
- canonical source and user runtime Rules pass 19/19 parity and body sufficiency
- governed design/changelog/TODO/phase/patch/README state is aligned
- clean master push, annotated release tag, GitHub Release, and fresh-clone audit pass
