# Proof Reachability and Authenticated Evidence

> **Current Version:** 1.0
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Status:** active
> **Created At:** 2026-08-09T19:00:46Z
> **Creation Evidence:** Direct creator event: the Write tool created this previously absent target after exact collision preflight; one UTC instant captured with `date -u +%Y-%m-%dT%H:%M:%SZ` produced both this filename and matching metadata.
> **Target Design:** [RULES System](../design/design.md) v10.65; [Goal Authoring and Route Support](../design/goal-authoring-and-route-support.design.md) v1.3; [Execution and Goal Frame](../design/execution-and-goal-frame.design.md) v1.32; [Action Safety](../design/action-safety.design.md) v1.5; [External Verification and Source Trust](../design/external-verification-and-source-trust.design.md) v1.7; [Evidence Discipline](../design/evidence-discipline.design.md) v1.8
> **Full history:** [Patch changelog](../changelog/proof-reachability-and-authenticated-evidence.changelog.md)

---

## Context

Governed source/local Goals can become unclosable when they silently require downstream Product proof that depends on deployment, installation, restart, authentication, or another state change outside the selected scope. The same gap can cause repeated private-access attempts without a usable authenticated session and can either discard supplied rendered evidence or overstate it as live proof.

## Analysis

The selected model separates proof-layer ownership from route prerequisites. Goal authoring records the required and currently reachable layers; execution framing closes only at the selected gate and preserves any explicitly selected stronger terminal proof. Action safety determines whether authenticated/private access is executable and stops deterministic retries. External verification selects only eligible authorized witnesses. Evidence discipline limits supplied artifacts to what their inspected content can prove.

## Change Items

### 1. Goal proof reachability — `additive`

**Before:** governed Goal construction names proof/checks but does not explicitly separate required proof, current reachable proof, successor/excluded proof, and route prerequisites.

**After:** `goal-authoring-and-route-support.md` owns the proof-layer fields, reachability vocabulary, prerequisite ordering, and explicit terminal-gate preservation in the `/goal` artifact.

### 2. Current Goal closure versus successor proof — `additive`

**Before:** execution continuation can leave downstream Product proof inside a source-bounded Goal or demote a selected live terminal gate merely because its prerequisites are difficult.

**After:** `execution-and-goal-frame.md` closes source/local Goals at their selected reachable layer, opens genuinely distinct downstream live proof as a successor, and keeps explicitly selected live terminal proof binding until passed or explicitly narrowed.

### 3. Authenticated/private capability and retry gate — `additive`

**Before:** private verification may begin before target, network, tool/session mechanism, authorization, approval, and substitutes are classified, allowing repeated guest requests without new evidence.

**After:** `action-safety.md` preflights the capability and permits at most one evidence-backed discriminating correction before `DETERMINISTIC_NON_RETRIABLE / NO_RETRY_UNTIL_CHANGE`. Guest/login or `401` shows required authentication was not established; `403` shows refusal but does not alone distinguish missing authentication from insufficient authorization. None alone proves Product failure, and raw secret/session material remains prohibited as a convenience workaround.

### 4. Capability-bound source selection — `additive`

**Before:** source trust can rank an authoritative private source without first proving that the current mechanism can reach it safely and lawfully.

**After:** `external-verification-and-source-trust.md` consumes action-safety preflight, selects the strongest reachable authorized claim-fit source or bounded substitute, and leaves approval, credential, capability, and retry ownership outside the trust rule.

### 5. Supplied rendered-artifact proof boundaries — `additive`

**Before:** screenshots, Rendered HTML/text, semantic witnesses, sanitized exports, and authenticated harness results lack one canonical cross-witness proof boundary.

**After:** `evidence-discipline.md` distinguishes artifact provenance from directly inspected content and states what each witness supports and cannot prove alone. Shared doctrine uses `<supplied-rendered-artifact>` rather than machine-local paths.

### 6. Scenario and governance integration — `replacement`

**Before:** Cases 17/12/04 and the matrix/coverage map do not jointly exercise proof reachability, terminal-gate preservation, authenticated capability, deterministic retry, and supplied-artifact evidence.

**After:** the scenario family and P149/v10.65 governance surfaces expose positive and forbidden-negative branches while preserving exactly 19 Runtime Rules and keeping the repository-specific install/push/tag/release lifecycle outside universal Runtime Rule doctrine.

## Verification

- Focused doctrine, scenario, triad, governance/allowlist/protected-byte/mode/link, and README checkers pass for the exact 29-path candidate.
- Exactly five Runtime Rules changed, the other 14 remain byte-identical, the ordered inventory remains 19, and no machine-local/private-secret/universal-release wording entered the checked scope.
- Bash and PowerShell installer fixtures pass; all 32 Patch timeline regression tests pass; this timestamped Patch inventories as compliant.
- A two-pass disposable installation proves 19/19 byte-and-mode parity, identical second-pass state, governed/support exclusion, and unrelated-file preservation.
- Independent doctrine and release/no-drift reviews pass after the HTTP `403` and active-phase baseline corrections; focused checks and disposable installation were rerun after repair.
- The candidate commit and exact approval packet are prepared; explicit approval, real Runtime Rule installation, push, annotated tag, GitHub Release, and fresh-public verification remain gated and are not claimed by this Patch.

## Rollback Approach

Before publication, revert only the clean candidate's frozen 29-path allowlist and leave the dirty backup checkout untouched. Stop on unexplained overlap, unexpected path/mode/symlink changes, test failure, protected-byte drift, or remote-master change. After publication, preserve the annotated v10.65 tag immutably and correct defects through a later release.
