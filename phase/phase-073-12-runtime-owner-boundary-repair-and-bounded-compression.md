# Phase 073-12 - Runtime Owner Boundary Repair and Bounded Compression

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-12
> **Status:** Active — candidate/canonical/root verified; publication pending
> **Target Release:** v10.60
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/design.md](../design/design.md), [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md), [../design/goal-authoring-and-route-support.design.md](../design/goal-authoring-and-route-support.design.md), [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md), [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md), [../design/document-governance.design.md](../design/document-governance.design.md), [../design/document-integrity.design.md](../design/document-integrity.design.md), [../design/action-safety.design.md](../design/action-safety.design.md), [../design/worker-routing-and-context.design.md](../design/worker-routing-and-context.design.md)
> **Patch References:** [../patch/runtime-owner-boundary-repair-and-bounded-compression.patch.md](../patch/runtime-owner-boundary-repair-and-bounded-compression.patch.md)

---

## Objective

Repair three verified semantic-owner conflicts and compact repeated cross-owner wording across the 19 Active Runtime Rules without weakening combined behavior, exact guards, approval/stop/recovery gates, or runtime body sufficiency.

พูดง่าย ๆ: ให้ decision, construction, rendering, startup, safety, และ worker lifecycle มี owner ชัดเจน แล้วลดเฉพาะคำอธิบายซ้ำ ไม่ตัดกลไก.

## Lineage Decision

- No current active phase exists, so current-phase update is unavailable.
- P073-09/10/11 already own the same 19-Rule compression, installation, parity, body-sufficiency, and release family.
- This wave preserves the exact 19-Rule capability boundary and extends that family with owner-boundary repair plus bounded compaction.
- Therefore `073-12` is the smallest truthful existing-family child; a new major is not justified.

## Baseline and Target

| Metric | Baseline | Target posture | Current candidate |
|---|---:|---:|---:|
| Active Runtime Rules | 19 | 19 unchanged | 19 |
| Total bytes | 273,734 | reduce safely by 6.2-9.0 KB | 266,520 (-7,214; -2.635%) |
| Total lines | 3,216 | reduce safely by 39-55 | 3,075 (-141) |
| Total words | 35,552 | reduce safely by 800-1,150 | 34,266 (-1,286) |

Metric targets never authorize weakening force words, enum registries, safety gates, exact artifacts, or body sufficiency.

## Selected Semantic Obligations

1. `execution-and-goal-frame.md` alone decides direct continuation, candidate-goal surfacing, advisory `/goal` eligibility, clarification, or no successor.
2. `goal-authoring-and-route-support.md` constructs the execution-selected goal and owns subordinate route support; it does not independently promote a candidate.
3. `explanation-and-presentation.md` renders the selected posture; it does not select or promote it.
4. The exact copied artifact keeps `/goal` first and `Plan reference:` second; the reference is forbidden until the route-only plan exists and is verified.
5. Startup evaluates diagram after design only when structure, visual authority, diagram relationships, visual topology, or existing diagram correctness materially changes; ordinary design edits may mark diagram `not required`.
6. `document-governance.md` synchronizes diagram only when the startup owner triggers it; `document-integrity.md` accepts the selected artifact without becoming another trigger owner.
7. `action-safety.md` owns `AGENT_TEAM_DUPLICATE_OR_STALE_TEAMMATE_PRESENCE` classification as `LIKELY_SYSTEMIC` / `STOP_AND_ESCALATE` and blocks unchanged same-role respawn while unresolved.
8. `worker-routing-and-context.md` owns inspected teammate state and the reuse, steer, wait, distinct-partition, spawn, or evidence-supported respawn decision.
9. All 19 Integration tails and selected consumer clauses become concise owner pointers while protected behavior and local consequences remain body-sufficient.

## Lane Map

### Lane 1 - Semantic Owner Repair

- separate goal decision, construction, and rendering ownership
- add conditional diagram startup and synchronization ownership
- rename the Agent Team failure profile and separate safety classification from worker lifecycle decisions

### Lane 2 - Owner-Canonical Compression

- compact all 19 Integration tails
- remove only complete doctrine repeated from a canonical owner
- preserve activation, local consequence, exact error-prevention literals, and owner handoffs
- inspect force-word deltas before acceptance

### Lane 3 - Verification and Installation

- verify exact 77-path allowlist, 19-file inventory, all-19 triad versions, body sufficiency, links, semantics, protected literals, and metrics
- run unchanged Bash and PowerShell fixture matrices plus disposable installation
- synchronize only verified allowlisted paths to canonical source
- install from canonical to `/home/node/.claude/rules` and prove 19/19 parity plus unrelated-file preservation

### Lane 4 - Governance and Release

- synchronize active design, diagram, changelog, TODO, phase, patch, playground, history, and surgical README anchors
- push only clean public `master`
- create immutable annotated `v10.60`, publish GitHub Release, and verify a fresh public tag clone
- after fresh-tag proof, publish one documentation-only closeout commit without moving the tag

## Out of Scope

- adding, deleting, merging, or renaming Active Runtime Rule files
- modifying Support Ticket product source or any `data/tickets/` path
- rewriting README structure or onboarding
- changing installer/fixture implementation without a separately reproduced defect and re-scope
- rewriting completed historical phases or patches
- cleaning, resetting, stashing, rebasing, merging, deleting, or pushing `backup/active-rules-source-2026-08-05`
- deletion, automatic fallback, or automatic restoration from quarantine

## Development Verification / TestKit Coverage

Selected route: existing playground Cases 01/05/09/14/17, focused static assertions, protected-literal/force-word review, exact allowlist and triad checks, unchanged installer fixture matrices, disposable install, canonical/root parity, and fresh public tag proof.

Required checks:

- exactly 19 ordered Active Runtime Rule filenames remain
- all 19 Runtime Rule/design/changelog versions match the v10.60 version table
- the former Agent Team profile identifier is absent from active Runtime Rules and the new identifier exists at the safety owner
- direct continuation, candidate goals, advisory construction, rendering, and `Plan reference:` ordering pass focused scenarios
- conditional diagram startup and synchronization pass ordinary-design and structural/visual branches
- duplicate/stale teammate state stops unchanged retry before worker-routing decides lifecycle
- exact refusal, evidence, status, migration, topology, retry, phase, worker, recovery, and approval registries remain
- `must`, `never`, `only`, `confirm`, `verify`, `block`, and `stop` reductions are manually justified
- all 19 bodies remain substantive
- Bash and PowerShell manifests/fixtures remain ordered-identical and pass
- disposable install preserves unrelated files, is idempotent, and creates no unexpected quarantine
- candidate/canonical/root/tag parity and fresh-clone checks pass in named scope

## Risks and Rollback

Risks:
- compaction can silently weaken force or remove a rare high-consequence guard
- copied goal artifacts can drift from the construction owner
- conditional diagram wording can become mandatory for every design edit or silently optional for structural changes
- safety classification can accidentally duplicate worker lifecycle authority
- broad synchronization can touch unrelated dirty canonical/root state

Containment:
- work only in the clean release clone until candidate verification passes
- use the exact 77-path allowlist and reject unexpected paths
- leader verifies helper handoff anchors before source edits or completion wording
- stop canonical sync on overlapping unrelated changes
- copy only allowlisted files; never use delete-capable broad synchronization

Rollback:
- before publication, discard only the scoped clean-lane candidate
- canonical/root rollback requires explicit action-and-scope approval and an independently verified known-good release source
- after publication, correct defects through a later release; never amend or force-move `v10.60`

## Current Verification and Semantic Disposition

Implementation coverage:
- semantic owner repairs: verified in focused candidate scenarios
- all-19 triad version advancement: verified and body-sufficient 19/19
- Integration-tail and body compaction: verified at 7,214 bytes, 141 lines, and 1,286 words reduced
- governed synchronization: verified inside the exact 77-path allowlist with zero newly introduced broken links
- canonical synchronization/root installation: verified at 77/77 and 19/19 parity with unrelated root files preserved
- public release/fresh-tag proof: not started

Candidate, canonical, and root installation obligations are verified in scope. Terminal release disposition remains open until public `master`, annotated tag, GitHub Release, fresh-tag reproduction, and documentation-only closeout pass.

## Exit Criteria

- all nine selected semantic obligations are `verified` or explicitly carried forward
- exactly 19 body-sufficient Active Runtime Rules remain
- measured reduction is reported against the frozen baseline without weakening protected behavior
- the exact 77-path candidate matches canonical and 19 installed root Rules match canonical while unrelated root files remain unchanged
- installer implementations/fixtures remain byte-identical and their matrices pass
- clean public `master`, annotated `v10.60`, GitHub Release, and fresh public tag clone are verified at their exact lifecycle states
- documentation-only closeout reflects the proof without moving the immutable tag or overclaiming stability
