# Proof Reachability and Authenticated Evidence

> **Current Version:** 1.0
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Status:** active
> **Created At:** 2026-08-09T19:00:46Z
> **Creation Evidence:** Direct creator event: the Write tool created this previously absent target after exact collision preflight; one UTC instant captured with `date -u +%Y-%m-%dT%H:%M:%SZ` produced both this filename and matching metadata.
> **Target Design:** [RULES System](../design/design.md) v10.65; [Goal Authoring and Route Support](../design/goal-authoring-and-route-support.design.md) v1.3; [Execution and Goal Frame](../design/execution-and-goal-frame.design.md) v1.32; [Action Safety](../design/action-safety.design.md) v1.5; [External Verification and Source Trust](../design/external-verification-and-source-trust.design.md) v1.7; [Evidence Discipline](../design/evidence-discipline.design.md) v1.8; [Phase, TODO, and Artifact Initiation](../design/phase-todo-artifact.design.md) v1.36
> **Full history:** [Patch changelog](../changelog/proof-reachability-and-authenticated-evidence.changelog.md)

---

## Context

Governed source/local Goals and their work plans can become unclosable when proposed done points are not evaluated for actual reachability or silently require downstream Product proof that depends on deployment, installation, restart, authentication, or another state change outside the selected scope. The same gap can cause repeated private-access attempts without a usable authenticated session and can either discard supplied rendered evidence or overstate it as live proof.

## Analysis

The selected model separates proof-layer ownership from route prerequisites. Goal authoring records the required and currently reachable layers and classifies them from explicit done conditions, proof/checks, scope, and checked authority rather than operational nouns or Product-facing capability names; execution framing closes only at the selected gate and preserves any explicitly selected stronger terminal proof. Action safety determines whether authenticated/private access is executable and stops deterministic retries. External verification selects only eligible authorized witnesses. Evidence discipline limits supplied artifacts to what their inspected content can prove.

## Change Items

### 1. Goal proof reachability — `additive`

**Before:** governed Goal construction names proof/checks but does not explicitly separate required proof, current reachable proof, successor/excluded proof, and route prerequisites.

**After:** `goal-authoring-and-route-support.md` owns pre-emission done-point feasibility, proof-layer fields, reachability vocabulary, work-plan output/gate/reachability mapping, in-place repair of unselected infeasible points, prerequisite ordering, explicit terminal-gate preservation, and noun-safe classification so Product-facing diagnostic or recovery capability names cannot select live execution or mutation proof by themselves.

### 2. Current Goal closure versus successor proof — `additive`

**Before:** execution continuation can leave downstream Product proof inside a source-bounded Goal, infer live acceptance from generic completion wording, or demote a genuinely selected live terminal gate merely because its prerequisites are difficult.

**After:** `execution-and-goal-frame.md` closes source/code Goals at their selected reachable layer, prohibits assistant-inferred live acceptance, opens genuinely distinct downstream live proof as a successor, and keeps live proof binding only when the user or checked governed authority explicitly selected it.

### 3. Authenticated/private capability and retry gate — `additive`

**Before:** private verification may begin before target, network, tool/session mechanism, authorization, approval, and substitutes are classified, allowing repeated guest requests without new evidence.

**After:** `action-safety.md` preflights the capability and permits at most one evidence-backed discriminating correction before `DETERMINISTIC_NON_RETRIABLE / NO_RETRY_UNTIL_CHANGE`. Guest/login or `401` shows required authentication was not established; `403` shows refusal but does not alone distinguish missing authentication from insufficient authorization. None alone proves Product failure, and raw secret/session material remains prohibited as a convenience workaround.

### 4. Capability-bound source selection — `additive`

**Before:** source trust can rank an authoritative private source without first proving that the current mechanism can reach it safely and lawfully.

**After:** `external-verification-and-source-trust.md` consumes action-safety preflight, selects the strongest reachable authorized claim-fit source or bounded substitute, and leaves approval, credential, capability, and retry ownership outside the trust rule.

### 5. Supplied rendered-artifact proof boundaries — `additive`

**Before:** screenshots, Rendered HTML/text, semantic witnesses, sanitized exports, and authenticated harness results lack one canonical cross-witness proof boundary.

**After:** `evidence-discipline.md` distinguishes artifact provenance from directly inspected content and states what each witness supports and cannot prove alone. Shared doctrine uses `<supplied-rendered-artifact>` rather than machine-local paths.

### 6. Task-list proof reconciliation — `additive`

**Before:** implementation, source/non-live verification, and optional rendered/live observation can remain mixed in one task family, so an optional or assistant-inferred live task keeps an otherwise complete code Goal open.

**After:** `phase-todo-artifact.md` reconciles open tasks against the selected proof layer, closes satisfied implementation and source/non-live verification tasks, moves optional live/rendered observation to an unselected successor, and leaves explicitly required unavailable live proof blocked with a resume condition and `NO_RETRY_UNTIL_CHANGE`.

### 7. Scenario and governance integration — `replacement`

**Before:** Cases 17/12/04 and the matrix/coverage map do not jointly exercise proof reachability, explicit live-gate selection, task-list successor separation, authenticated capability, deterministic retry, and supplied-artifact evidence.

**After:** the scenario family and P149/v10.65 governance surfaces expose positive and forbidden-negative branches while preserving exactly 19 Runtime Rules and keeping the repository-specific install/push/tag/release lifecycle outside universal Runtime Rule doctrine.

## Verification

- The earlier five-triad/29-path candidate passed focused checks, fixtures, 32 Patch timeline tests, disposable 19/19 installation, and independent reviews, then was explicitly approved and installed into the runtime.
- Before publication, user-reported Goal-loop and task-list evidence expanded this review to six changed and 13 protected Runtime Rules across exactly 32 paths while the ordered inventory remains 19.
- Corrected doctrine/scenario/six-triad/governance checks, Bash/PowerShell fixtures, 32 Patch tests, compliant Patch inventory, and two-pass disposable 19/19 installation cover explicit live-gate selection, M33 noun-safe operational-capability classification, M34 done-point feasibility/in-place Goal-plan repair, task reconciliation, optional live-successor separation, and deterministic no-retry.
- Corrected doctrine and release/no-drift reviews pass. Renewed exact approval, runtime reinstallation, push, annotated tag, GitHub Release, and fresh-public verification remain gated and are not claimed by this Patch.

## Rollback Approach

Before publication, revert only the clean candidate's expanded 32-path allowlist and leave the dirty backup checkout untouched. Stop on unexplained overlap, unexpected path/mode/symlink changes, test failure, protected-byte drift, or remote-master change. After publication, preserve the annotated v10.65 tag immutably and correct defects through a later release.
