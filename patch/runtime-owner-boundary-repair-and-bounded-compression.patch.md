# Runtime Owner Boundary Repair and Bounded Compression Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed — released and fresh-public-tag verified
> **Target Design:** [../design/design.md](../design/design.md) v10.60
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The v10.59 baseline contains exactly 19 body-sufficient Active Runtime Rules totaling 273,734 bytes, 3,216 lines, and 35,552 words. The checked audit found three semantic-owner conflicts plus repeated Integration and consumer wording that can be compacted without removing behavior.

This patch records the bounded before/after review surface for v10.60. It does not authorize file deletion, Runtime Rule inventory changes, README restructuring, historical rewrite, installer changes, or force-word weakening.

## 2) Analysis

Risk: High for combined runtime-governance meaning; Medium for text-only implementation.

Protected behavior includes:
- evidence classes and claim states
- readiness/status and migration lifecycle ladders
- topology, refusal, retry, and recovery registries
- destructive confirmation, approval-sensitive external action, quarantine, and controlled restoration
- phase identity grammar and lineage order
- worker invocation/lifecycle, lane permissions, handoff fields, and leader verification
- exact `/goal` then `Plan reference:` artifact order
- force words including `must`, `never`, `only`, `confirm`, `verify`, `block`, and `stop`

Compression succeeds only when one complete canonical owner remains and each consumer retains the activation, local consequence, required literal/order, or likely-error guard it needs.

## 3) Change Items

### RBR-001 - Goal decision, construction, and rendering ownership

- **Targets:** `../execution-and-goal-frame.md`, `../goal-authoring-and-route-support.md`, `../explanation-and-presentation.md` and matching design/changelog companions
- **Type:** semantic correction and restructuring
- **Before:** execution, authoring, and presentation can each read as if they choose or promote an advisory `/goal`.
- **After:** execution alone selects direct continuation, candidate goals, advisory eligibility, clarification, or no successor; goal-authoring constructs the selected artifact and route support; presentation renders the selected posture only.
- **Exact guard:** `/goal` precedes `Plan reference:` inside one copyable artifact, and no durable reference is emitted before the route-only plan exists and is verified.

### RBR-002 - Conditional diagram startup and synchronization

- **Targets:** `../phase-todo-artifact.md`, `../document-governance.md`, `../document-integrity.md`, matching designs, `../design/design/governance-contracts.design.md`, and `../diagram/STRUCTURE.md`
- **Type:** semantic correction
- **Before:** diagram is mandatory governed infrastructure but absent from startup/synchronization order, leaving unclear whether every design edit must mutate diagram or whether structural changes may skip it.
- **After:** startup evaluates diagram after design when structure, visual authority, diagram relationships, visual topology, or existing diagram correctness changes. Ordinary design edits may mark it `not required`; no subject diagram opens automatically. Document governance synchronizes only a triggered diagram, while document integrity remains a consumer.

### RBR-003 - Agent Team failure classification versus lifecycle decisions

- **Targets:** `../action-safety.md`, `../worker-routing-and-context.md` and matching design/changelog companions
- **Type:** identifier migration and owner correction
- **Before:** `TEAM_AGENT_DUPLICATE_OR_STALE_PRESENCE` is noncanonical and the safety profile restates lifecycle choices.
- **After:** `AGENT_TEAM_DUPLICATE_OR_STALE_TEAMMATE_PRESENCE` is classified as `LIKELY_SYSTEMIC` / `STOP_AND_ESCALATE`; unchanged same-role respawn is blocked while unresolved. Worker routing inspects state and decides reuse, steer, wait, distinct partition, spawn, or evidence-supported respawn.

### RBR-004 - All-19 owner-canonical compaction

- **Targets:** all 19 Active Runtime Rules and matching design/changelog triads
- **Type:** behavior-preserving restructuring
- **Before:** Integration tails and selected consumers repeat complete doctrine already owned elsewhere.
- **After:** Integration tails become compact canonical-owner links and consumer bodies keep only decision-changing activation, consequence, exact literals/order, or error-prevention guards. Every Runtime Rule remains substantive.

Conservative target:

| Metric | Baseline | Target reduction |
|---|---:|---:|
| Bytes | 273,734 | 6.2-9.0 KB |
| Lines | 3,216 | 39-55 |
| Words | 35,552 | 800-1,150 |
| Active Runtime Rule files | 19 | 0 inventory change |

The target is measurement guidance, never an acceptance override.

### RBR-005 - Governed synchronization and release

- **Targets:** the exact 77-path allowlist covering 19 triads, active design/diagram/master changelog, TODO/phase/patch, surgical README anchors, focused playground cases/matrix, and current daily history
- **Type:** synchronization
- **Before:** public/canonical/root state remains v10.59 and P073-12 is not represented.
- **After:** active surfaces describe the implemented v10.60/P073-12 candidate, then advance to released/fresh-public-tag verified only after the matching gates pass.

## 4) Verification

Required candidate proof:
- exact 77 changed paths and no unexpected mode drift
- exactly 19 ordered Active Runtime Rule filenames and 19 aligned triads
- focused semantic assertions for all three owner repairs
- protected literal/enum/force-word review and 19/19 body sufficiency
- changed-scope links, session/backlink integrity, `git diff --check`, README surgical-anchor checks, and measured runtime metrics
- unchanged Bash/PowerShell installer and fixture bytes; both fixture matrices pass
- disposable install proves 19/19 parity, manifest order, idempotency, unrelated-file preservation, and no unexpected quarantine

Required installation/release proof:
- candidate/canonical parity for all 77 allowlisted paths after overlap checks
- canonical/root parity and body sufficiency 19/19 while unrelated root files remain byte-identical
- clean `master` push, immutable annotated `v10.60`, GitHub Release identity, and fresh public tag clone rerun
- documentation-only closeout only after fresh-tag proof; the tag remains on the verified release commit

Current evidence: candidate static/semantic/link/registry/force/body/fixture/disposable-install gates, 77/77 candidate/canonical parity, 19/19 canonical/root parity, unrelated-file preservation, public `master`, annotated `v10.60`, GitHub Release identity, and fresh-public-tag static/fixture/disposable-install reproduction pass. The immutable tag remains on release commit `33ad330120b88461978c408bc6a857e269e4c73d`.

## 5) Rollback Approach

- Before canonical synchronization: discard only the scoped clean-clone candidate if a gate fails.
- Canonical synchronization: stop on any overlapping unrelated edit; copy only allowlisted files and never use delete-capable broad sync.
- Runtime installation: use the unchanged transactional installer, verify unrelated-file preservation, and require explicit approval for controlled restoration.
- Before publication: revert only scoped P073-12 changes in the clean lane if needed.
- After publication: use a later corrective release; never amend or force-move `v10.60`.
- Quarantine is preservation-only, execution-disconnected, never an automatic fallback, restoration source, or deletion authority.
