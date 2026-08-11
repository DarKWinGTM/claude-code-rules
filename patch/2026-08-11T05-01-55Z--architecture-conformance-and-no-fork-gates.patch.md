# Architecture Conformance and No-Fork Gates

> **Current Version:** 1.0
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Status:** Candidate verified — creator evidence and all independent reviews pass; local commit, publication approval, and installation approval pending
> **Created At:** 2026-08-11T05:01:55Z
> **Creation Evidence:** Direct creator event in session 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e: transcript tool result `call_NiaIFNoeco6la1TCYkWD6Aq1` at 2026-08-11T05:02:09.184Z confirms `patch-timeline create --execute` created this path with `createdAt` 2026-08-11T05:01:55Z and manifest SHA-256 `0d03c677d875aabdc88833918ca5824786a1dfafbae8e8a1c477a7b303cdc3c0` (`executed: true`).
> **Target Design:** design/design.md v10.67
> **Full history:** changelog/changelog.md

## Context

A checked session showed two architecture-fork episodes: route ownership moved away from governed design, and a missing sanitized field was misclassified as a missing credential architecture before the existing producer/state/consumer path was traced. The second episode implemented a new route, module, client, integration, and tests before the assistant reconstructed the existing authority path. Existing RULES already state design authority, premise checking, one-authority topology, and verification discipline, but they do not activate one deterministic cross-owner pre-source-mutation and architecture-fitness gate.

This Patch reviews a direct Main RULES correction. No Trial/additional artifact or new Runtime Rule is selected.

## Analysis

The smallest owner-correct change is:

```text
execution-and-goal-frame trigger
→ action-safety architecture delta preflight
→ coding-discipline regression/gap and fitness verification
```

The target keeps ordinary bounded repair lightweight while stopping route, service, client, transport, registry, state-key, reader/writer, fallback, or authority expansion until active design and the existing architecture are checked.

## Change Items

### 1. Architecture-bearing mutation trigger

**Type:** restructuring

| Current | Target |
|---|---|
| Premise-before-expansion requires ownership/readers/writers/state/dependency checks, but architecture-bearing source mutation has no explicit canonical preflight invocation. | Material route/service/client/state/authority mutations invoke the canonical architecture delta preflight before source editing. User/design no-fork correction invalidates incompatible pending branches, tasks, and tests. |

**Owner:** `execution-and-goal-frame.md` and its design/changelog triad.

### 2. Design-conformance architecture delta preflight

**Type:** additive

| Current | Target |
|---|---|
| Runtime topology mutation classifies entities, authority, delta, and approval, but the mutation gate does not explicitly bind active design plus producer/state/reader/writer/consumer mapping to ordinary architecture-bearing implementation. | The canonical safety owner requires active design, existing architecture map, last-known-working path, proposed delta, existing-owner absorption check, security boundary, approval state, and retirement/rollback direction. Unknown or incomplete state remains `OBSERVE_ONLY`. |

**Owner:** `action-safety.md` and its design/changelog triad.

### 3. Regression-versus-architecture-gap diagnosis

**Type:** additive

| Current | Target |
|---|---|
| Debug strategy requires a symptom, hypothesis, and discriminating signal, but a missing field/output can still be interpreted as missing infrastructure before the existing chain is traced. | Coding diagnosis identifies producer, stored state/transport, readers, writers, consumers, design contract, and working evidence before classifying existing-path regression, state/config drift, dormant/disconnected path, contract mismatch, unresolved state, or verified capability gap. |

**Owner:** `coding-discipline.md` and its design/changelog triad.

### 4. Architecture fitness verification

**Type:** additive

| Current | Target |
|---|---|
| Functional tests may prove that an invented route/client behaves as written without proving design or one-authority conformance. | Architecture-bearing changes require functional proof through the selected path plus negative proof against unauthorized alternate owner/route/client/state key/dual read-write/shadow/fallback/discovery. Passing tests for an unapproved path cannot close the objective. |

**Owner:** `coding-discipline.md`, with topology/approval semantics delegated to `action-safety.md`.

### 5. Scenario/TestKit family

**Type:** additive

Add one Case 18 family covering:

1. route-owner fork;
2. regression mistaken for architecture gap;
3. invented path with passing functional tests;
4. ordinary repair control;
5. verified approved capability expansion control;
6. no-fork correction lock.

Update the playground README, August observed-evidence log, matrix, coverage, and owning design shard. Case 18 records the exact checked local transcript path as scoped evidence while portable Runtime doctrine remains free of project-specific paths, providers, credentials, or local hosts.

### 6. Governed release and installation

**Type:** restructuring

Open P150/v10.67, align design/runtime/changelog/TODO/phase/Patch/README surfaces, preserve the exact 19-file Runtime Rule payload, run focused/full/disposable-install verification, and require exact evidence-packet approval before public publication and real runtime installation.

## Verification

- Case 18 RED was captured before Runtime Rule changes: the architecture-bearing trigger, design-conformance preflight, regression-gap gate, and architecture-fitness gate were absent as expected.
- The pre-review candidate passed focused GREEN for the four Runtime doctrine anchors, Case 18, and M35-M40. Independent review then found Case 18 evidence-shape and topology-wording defects; those defects are repaired in the working candidate and require a fresh focused rerun.
- Cross-owner references preserve design, safety, evidence, coding, task, and presentation ownership.
- Exactly three Runtime Rules advance; the other 16 remain byte-and-mode identical.
- Runtime inventory/order remains exactly 19 in Bash/PowerShell installers and fixtures.
- Master and triad versions, links, sessions, Patch filename/`Created At` equivalence, phase/TODO state, playground matrix/coverage, and release wording align; transcript result `call_NiaIFNoeco6la1TCYkWD6Aq1` provides the admissible exact creator-event anchor.
- On the repaired 25-path candidate, focused doctrine/Case checks, `git diff --check`, link/metadata/mode/shape checks, protected-byte checks, Bash/PowerShell fixtures, Patch tests 32/32, and two-pass disposable 19/19 installation passed; the exact commit-bound manifest remains future work.
- Fresh independent doctrine/security, 25-path payload, and final release/no-drift re-reviews pass. The prior findings are repaired and Patch creation evidence is direct-event anchored; candidate commit preparation is unblocked.
- Public push/tag/Release and real installation run only after exact SHA/scope approval.

## Rollback Approach

Before publication, retain candidate work on the isolated branch and repair through additional commits. Do not mutate the protected dirty backup. Before real installation, capture exact bytes and modes for all installed Runtime Rules and use that approved snapshot for rollback if parity fails. After publication, preserve immutable release identities; any defect requires a later release rather than force push, tag movement, Release deletion, or historical rewrite.
