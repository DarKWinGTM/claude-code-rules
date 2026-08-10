# Phase 149 - Proof Reachability and Authenticated Evidence

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 149
> **Status:** Released — immutable v10.65; post-publication diagram-format gate failed; corrective child P149-01 selected
> **Target Release:** v10.65
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/design.md](../design/design.md) v10.65; [../design/goal-authoring-and-route-support.design.md](../design/goal-authoring-and-route-support.design.md) v1.3; [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.32; [../design/action-safety.design.md](../design/action-safety.design.md) v1.5; [../design/external-verification-and-source-trust.design.md](../design/external-verification-and-source-trust.design.md) v1.7; [../design/evidence-discipline.design.md](../design/evidence-discipline.design.md) v1.8; [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.36
> **Patch References:** [../patch/2026-08-09T19-00-46Z--proof-reachability-and-authenticated-evidence.patch.md](../patch/2026-08-09T19-00-46Z--proof-reachability-and-authenticated-evidence.patch.md)

---

## Objective

Make governed Goals and their work plans select done points that can truthfully close in the current scope, repair assistant-inferred infeasible gates in place, preserve any explicitly selected live terminal gate, prevent operational capability names from selecting live proof by inference, and prevent repeated authenticated/private access attempts when the current mechanism cannot authenticate. Keep safe supplied rendered artifacts useful as bounded evidence without projecting them into live, authenticated, complete, or stable proof.

## Lineage Decision

- At the clean candidate baseline, P148 / v10.64 was released and closed and no RULES release phase was active; P149 became active when this governed wave opened.
- This wave changes six Runtime Rule owner contracts and adds a distinct proof-reachability, explicit live-gate selection, task reconciliation, authenticated-capability, retry, and supplied-artifact evidence family with its own scenario, installation, and publication gates.
- The work is not a bounded child of Patch chronology governance or the earlier Case 17 route-scope correction family.
- P149 is therefore the smallest truthful new major. The checked public baseline had no P149 phase, v10.65 tag, or v10.65 GitHub Release when the clean candidate was established.

## Expected Output

- Goal authoring evaluates proposed done points against scope/environment/capability/approval/proof-path reachability, records the required proof layer, current reachable layer, successor/excluded layers, and route prerequisites, and keeps the work plan ending at the selected current gate.
- Execution framing repairs an unselected assistant-inferred infeasible Goal/plan gate in place, closes source/code Goals at the selected reachable gate, prohibits assistant-inferred live acceptance from generic wording or operational Product-facing capability names, and preserves only a live gate explicitly selected by the user or checked governed authority as binding.
- Task reconciliation closes satisfied implementation and source/non-live verification tasks before optional live/rendered observation becomes an unselected successor; explicitly required unavailable live proof remains blocked without unchanged retry.
- Action safety preflights target, network, tool/session mechanism, authorization, approval, and bounded substitutes before authenticated/private access.
- Deterministic capability failure stops unchanged retries after at most one evidence-backed discriminating correction.
- External verification selects only reachable authorized sources after capability preflight.
- Evidence discipline defines claim boundaries for screenshots, Rendered HTML, rendered text/semantic witnesses, sanitized console/log/network exports, and authenticated harness results.
- Cases 17, 12, and 04 plus matrix/coverage make the positive and forbidden-negative branches inspectable.
- Candidate construction, Runtime Rule installation, publication, and fresh-public verification preserve exactly 19 Runtime Rules.

## Selected Semantic Coverage

| Obligation | Implementation state | Terminal disposition |
|---|---|---|
| Done-point feasibility before Goal/plan emission | implemented | verified |
| In-place repair for an unselected assistant-inferred infeasible gate | implemented | verified |
| Reachable proof-layer Goal fields and prerequisite ordering | implemented | verified |
| Source/local closure versus successor Product proof | implemented | verified |
| Explicit live-gate selection; no assistant-inferred live acceptance | implemented | verified |
| Operational capability names do not select live execution or mutation proof | implemented | verified |
| Task-list reconciliation and optional live-successor separation | implemented | verified |
| Authenticated/private capability and authorization preflight | implemented | verified |
| One bounded discriminating correction and deterministic no-retry | implemented | verified |
| Guest/login and 401 authentication boundary plus 403 refusal uncertainty | implemented | verified |
| Reachable authorized external-source selection | implemented | verified |
| Supplied rendered-artifact and authenticated-harness proof limits | implemented | verified |
| Real Runtime Rule installation | implemented | verified — 19/19 parity and idempotence passed |
| Public push, annotated tag, Release, and fresh-public technical proof | implemented | verified |
| Case 04/12 no-frame diagram format | implemented in v10.65 | failed after delayed audit; P149-01 owns correction |

## Lane Map

1. **Scenario/TestKit:** Cases 17/12/04 plus matrix and coverage define proof-reachability, terminal-gate, authenticated-capability, retry, and supplied-artifact branches.
2. **Doctrine triads:** advance six existing Runtime Rule/design/changelog owners without adding a twentieth Runtime Rule.
3. **Governed integration:** synchronize this Phase, its Patch and Patch changelog, release shard, master design/changelog, TODO, phase summary, and README.
4. **Candidate verification:** doctrine/scenario/triad assertions, protected-byte and allowlist checks, fixture suites, Patch timeline regression, disposable install, and independent reviews passed before publication.
5. **Installation/publication:** exact approval preceded real 19-Rule installation, fast-forward push, annotated v10.65 tag, and GitHub Release; dirty-checkout reconciliation remained excluded.
6. **Fresh-public proof and delayed audit:** public master/tag, 19-Rule payload, fixtures, idempotence, release identity, and earlier-tag immutability passed; a later SHA-bound review found the Case 04/12 no-frame violation and selected P149-01/v10.66 as convergence owner.

## Affected Artifacts

- `goal-authoring-and-route-support.md` triad → 1.3
- `execution-and-goal-frame.md` triad → 1.32
- `action-safety.md` triad → 1.5
- `external-verification-and-source-trust.md` triad → 1.7
- `evidence-discipline.md` triad → 1.8
- `phase-todo-artifact.md` triad → 1.36
- Cases 17, 12, and 04 plus `playground/matrix.md` and `playground/coverage.md`
- master design/changelog, README, TODO, phase summary, this Phase, its Patch/Patch changelog, and the v10.65 release shard

## Development Verification / TestKit Coverage

Selected route: `new_testkit_scenario` plus exact triad/allowlist/protected-byte checks, Bash/PowerShell installer fixtures, Patch timeline regression, disposable installation, and independent doctrine/release review.

Required checks:
- Case 17/M34 evaluates whether proposed Goal/plan done points can close in the current environment and repairs an unselected assistant-authored infeasible point in place without a replacement Goal or retry loop.
- Case 17 closes a source-bounded Goal at its selected reachable layer and keeps distinct Product proof as an explicit successor.
- Case 17 prevents generic completion wording, assistant inference, or operational capability names such as pinned-host SSH diagnostics and an exact-request recovery path from selecting live acceptance; authenticated Product proof stays inside the current Goal only when the user or checked governed authority explicitly selects it.
- Task-list reconciliation closes satisfied code/non-live tasks and routes optional live/rendered observation to an unselected successor; explicitly required unavailable live proof stays blocked without unchanged retry.
- Cases 12/04 preflight authenticated/private capability before access and stop unchanged retries after deterministic failure.
- Guest/login or `401` shows required authentication was not established; `403` shows refusal but does not alone distinguish missing authentication from insufficient authorization; none alone proves authenticated Product failure.
- Screenshot, Rendered HTML, rendered text/semantic witness, sanitized export, and authenticated harness evidence remain claim-bounded.
- No raw credential, cookie, bearer token, private key, auth-state dump, machine-local SMB/GVFS path, or universal push/tag/release requirement enters shared doctrine.
- Exactly six Runtime Rules change; the other 13 remain byte-identical and the ordered inventory remains exactly 19.
- The expanded candidate scope remains exactly 32 paths with no deletion, symlink change, or mode change.
- Bash/PowerShell fixtures, Patch timeline regression, disposable installation, second-pass idempotence, links, body sufficiency, and no governed/support runtime installation pass.
- Exact candidate approval preceded real runtime installation and public publication; both completed without widening the 19-Rule payload.

Current evidence: the final six-triad/32-path candidate passed doctrine/scenario/governance checks, Bash/PowerShell fixtures, 32 Patch tests, compliant Patch inventory, independent reviews, and two-pass disposable installation. After exact approval, real runtime installation passed 19/19 byte-and-mode parity and idempotence; v10.65 was published from commit `2e751bbb620eb68527e5a67eb6348196a67727e7` at annotated tag object `cc7d322d3b1e4e7785373370d2d3c9eb8a8a395e`, with GitHub Release and fresh-public technical reproduction. A delayed SHA-bound audit then found prohibited Unicode Box Drawing characters introduced in the Case 04 and Case 12 flow diagrams. The v10.65 format gate remains failed, and selected child P149-01/v10.66 owns the prospective correction.

## Entry Conditions and Out of Scope

Entry conditions at phase opening:
- clean candidate baseline was public `master` commit `2aebef62c27d3c9dd2c40e47ac2ab732dbec110c`;
- immutable v10.64 tag object `aba1ab0775188aa9ae65165a19c30e9138210014` peeled to release commit `fe44a0af3885b2cf64d3556b6b3e620b9078e5c5`;
- no P149 phase, v10.65 tag, or v10.65 GitHub Release existed at baseline check;
- the dirty backup checkout was not source or publication authority.

Out of scope:
- a new Runtime Rule or installer feature;
- universal release lifecycle doctrine for unrelated repositories;
- direct authenticated access without supported capability, authorization, and approval;
- raw credentials, cookies, tokens, private keys, or session-state transfer;
- hardcoded workstation, SMB/GVFS, localhost, or private-host paths in shared doctrine;
- dirty-checkout reset, cleanup, overwrite, broad merge, deletion, force push, or published-tag movement;
- broad README/master-governance density repair beyond the current contradiction and active-state sync; the existing deferred repair owner remains visible in `TODO.md`.

## Risks and Rollback

Risks:
- weakening a selected live terminal gate can make completion wording false;
- leaving unreachable downstream proof inside a source-bounded Goal can make the Goal unclosable;
- repeated guest requests can waste attempts without adding evidence;
- supplied artifacts can be overprojected into live/authenticated/stability claims;
- positive scenario semantics can pass while presentation still violates the active no-frame format contract.

Rollback/containment:
- preserve immutable v10.65 and its failed format-gate record;
- correct the residual presentation defect only through selected child P149-01/v10.66;
- stop on unexpected paths, semantic change, mode/symlink drift, protected-byte drift, fixture failure, or remote-master change;
- keep v10.66 publication and any later documentation-only closeout behind separate exact action-and-scope approvals;
- keep dirty-checkout reconciliation excluded.

## Exit Criteria

- Six owner triads are aligned, body-sufficient, installed, and published in immutable v10.65.
- Exactly six Runtime Rules changed while the other 13 and the 19-file inventory remained protected.
- The 32-path release, references, modes, fixtures, Patch regression, installation parity, publication, and fresh-public technical checks passed.
- The delayed Case 04/12 diagram-format failure is preserved rather than retroactively passed.
- Corrective ownership is transferred to child [P149-01](phase-149-01-playground-flow-diagram-format-correction.md) and [candidate v10.66](../changelog/changelog/v10.66-playground-flow-diagram-format-correction.changelog.md#version-1066); P149 and v10.65 remain immutable.
