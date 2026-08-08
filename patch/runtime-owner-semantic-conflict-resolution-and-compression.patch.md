# Runtime Owner Semantic Conflict Resolution and Compression Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Active — release verification pending
> **Target Design:** [../design/design.md](../design/design.md) v10.57
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

The v10.54 baseline contains 19 body-sufficient Active Runtime Rules totaling 273,721 bytes. This patch resolves six checked semantic ambiguities, adds explicit helper invocation routing, and produces a checked v10.57 source candidate totaling 254,032 bytes while preserving the same 19-file capability boundary.

This patch packages a behavior-preserving owner-canonical compaction wave. It removes duplicated or non-decision-changing prose only after confirming a loaded canonical owner, and it preserves rare high-consequence safety and error-prevention behavior.

## 2) Analysis

Risk: High for runtime governance meaning; Medium for text-only implementation.

Preservation requirements:
- exactly 19 Active Rule files
- exact enums/literals and force-word strength
- authority, evidence, safety, approval, stop, recovery, phase-lineage, goal/route, and body-sufficiency contracts
- no deletion by cleanup, isolation, worktree, co-location, or git state
- no README rewrite or unrelated governed-history rewrite

Compression is successful only when combined behavior remains equivalent or clearer while duplicated ownership and payload size decrease.

## 3) Change Items

### RSC-001 - Operational runtime worker vocabulary

- **Target:** `../action-safety.md`; boundary check in `../worker-routing-and-context.md`
- **Type:** clarification
- **Before:** unqualified `worker` can mean an operational process or a Claude delegated worker.
- **After:** topology vocabulary uses operational runtime worker/job/entity and excludes Claude subagents/teammates, whose routing remains owned by `worker-routing-and-context.md`.

### RSC-002 - Authorized destruction versus hard block

- **Target:** `../refusal-and-recovery.md`, `../action-safety.md`
- **Type:** semantic correction
- **Before:** activation grammar can read as if every destructive operation is independently a `HARD_BLOCK`.
- **After:** malicious or unauthorized destruction may be hard-blocked; missing authorization routes to workflow context; authorized bounded destruction follows exact action-and-scope confirmation.

### RSC-003 - Emergency containment ordering

- **Target:** `../action-safety.md`, `../phase-todo-artifact.md`, `../execution-and-goal-frame.md`
- **Type:** precedence clarification
- **Before:** reversible urgent containment and full artifact startup ordering can appear to block one another.
- **After:** only the smallest safe reversible containment/diagnostic action may precede full startup when delay increases immediate harm; authority/approval remain and governance resumes immediately after containment.

### RSC-004 - Implementation versus terminal disposition

- **Target:** `../phase-todo-artifact.md` with status-owner checks in `../accurate-communication.md`, `../coding-discipline.md`, and `../execution-and-goal-frame.md`
- **Type:** closeout correction
- **Before:** `implemented` appears among states an item may reach before closeout even when material verification remains.
- **After:** implementation coverage and terminal disposition are separate; `implemented` remains intermediate until verified or explicitly carried forward.

### RSC-005 - Public lookup versus consequential external action

- **Target:** `../external-verification-and-source-trust.md`, `../action-safety.md`, `../execution-and-goal-frame.md`
- **Type:** scope clarification
- **Before:** broad `external action` wording can capture ordinary public read-only evidence lookup.
- **After:** public read-only lookup is evidence gathering; authenticated/private, mutating, sending/publishing, purchase/payment, deployment, account/shared-state, sensitive-data, meaningful-cost, or terms-acceptance actions remain gated.

### RSC-006 - Active startup owner reference

- **Target:** `../document-integrity.md`
- **Type:** narrow reference correction
- **Before:** the active Rule Statement names retired `artifact-initiation-control` ownership.
- **After:** active ownership points to `phase-todo-artifact.md`; historical absorbed/changelog provenance remains unchanged.

### RSC-007 - Complete image-derived strategy integration

- **Target:** `../communication-register.md`, `../explanation-and-presentation.md`, `../document-governance.md`, `../worker-routing-and-context.md`, with preservation checks across existing owners
- **Type:** additive refinement plus owner projection
- **Before:** high-signal pruning exists, but the general supporting-copy error-prevention exception is not explicit in one canonical admission owner.
- **After:** reader-facing support is opt-in/non-repetitive but required when silence hides risk, ambiguity, irreversible effect, verification limit, confirmation/recovery, or a necessary next action. Rendering stays separate. Cross-Rule exact copies remain bounded owner-linked exceptions. Conditional planning, verification-before-done, simplicity, evidence-first diagnosis, live-task/TODO roles, and durable memory gates remain with their existing owners. Worker routing now governs invocation as well as lane context: primary source/integration stays in the context-rich leader session; one standalone subagent handles one bounded independent axis; parallel standalone agents are invoked together for independent research/review/testing/metrics matrix cells; teammates are reserved for shared dependencies, staged coordinated testing, or cross-lane messaging. Active Rule/product source, README, integration, install, git, and release remain leader-owned.

### RSC-008 - Owner-canonical hotspot compaction

- **Target:** all 19 Active Rules are audited; only verified owner/consumer deltas are edited.
- **Type:** restructuring
- **Before:** repeated role explanations, trigger/anti-pattern mirrors, examples, progress/closeout patterns, and integration recaps inflate combined runtime context.
- **After:** canonical owners retain complete operational contracts; consumers keep activation, local consequence, handoff, or minimum exact error-prevention copy.

Measured target result:

| Rule | Baseline | Target posture | Checked candidate |
|---|---:|---:|---:|
| `document-governance.md` | 27,850 bytes | approximately 21-22 KB | 18,834 bytes |
| `phase-todo-artifact.md` | 25,346 bytes | approximately 20-21 KB | 17,148 bytes |
| `explanation-and-presentation.md` | 25,158 bytes | approximately 18-19 KB | 16,494 bytes |
| Combined 19 Rules | 273,721 bytes | reduce safely by about 18-24 KB | 254,032 bytes; down 19,689 (7.19%) |
| Checked pre-compression baseline | 405,914 bytes | preserve combined behavior | down 151,882 (37.42%) |

### RSC-009 - Governed synchronization and release

- **Target:** touched design/changelog chains, master design/changelog, TODO, P073-11, phase summary, this patch, and exact README current-state anchors.
- **Type:** synchronization
- **Before:** v10.56 is current and no active phase is selected.
- **After:** release surfaces describe the verified v10.57/P073-11 semantic-resolution and compaction result without README restructure, historical rewrite, or unrelated scope absorption.

## 4) Verification

Checked source-candidate evidence:
- Active Rule inventory and exact filenames remain 19; body sufficiency passes 19/19
- exact literal/enum and invocation registries, selected high-risk clauses, force-word review, six semantic settlements, and image-strategy owner map pass
- measured payload is 254,032 bytes, 3,092 lines, and 33,038 words
- independent bounded reviews were leader-verified and all material findings were repaired
- 39-path allowlist, 10/10 touched triads, changed-scope links, and `git diff --check` pass
- Bash/PowerShell manifests remain ordered-identical at 19; both disposable installs pass 19/19 parity and unrelated-sentinel preservation
- latest canonical synchronization passes candidate/canonical 39/39; canonical/root SHA-256 parity and body sufficiency pass 19/19; unrelated `shared-task-list-path-coordination.md` remains preserved
- README remains an exact 7-addition/7-removal current-state diff with no restructure and the approved `100755` to `100644` mode correction

Remaining release gates:
- push only clean `master`
- backup branch unchanged
- annotated tag and GitHub Release resolve to the same commit as remote master
- fresh public clone reproduces inventory, metrics, body, install, and reference checks

## 5) Rollback Approach

- Before commit/push: discard only scoped changes in the clean release lane.
- Canonical synchronization: stop on any overlapping unrelated edit; never broad-delete or overwrite without reconciliation.
- Runtime: reinstall the known-good v10.56 19-Rule set only under explicit rollback approval and preserve unrelated destination files.
- After public release: use a corrective commit and new release; never force-move the published tag.
