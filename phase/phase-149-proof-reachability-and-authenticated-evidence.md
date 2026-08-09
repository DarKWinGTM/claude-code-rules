# Phase 149 - Proof Reachability and Authenticated Evidence

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 149
> **Status:** Active — corrective six-triad verification and renewed approval-packet preparation in progress
> **Target Release:** v10.65
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/design.md](../design/design.md) v10.65; [../design/goal-authoring-and-route-support.design.md](../design/goal-authoring-and-route-support.design.md) v1.3; [../design/execution-and-goal-frame.design.md](../design/execution-and-goal-frame.design.md) v1.32; [../design/action-safety.design.md](../design/action-safety.design.md) v1.5; [../design/external-verification-and-source-trust.design.md](../design/external-verification-and-source-trust.design.md) v1.7; [../design/evidence-discipline.design.md](../design/evidence-discipline.design.md) v1.8; [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.36
> **Patch References:** [../patch/2026-08-09T19-00-46Z--proof-reachability-and-authenticated-evidence.patch.md](../patch/2026-08-09T19-00-46Z--proof-reachability-and-authenticated-evidence.patch.md)

---

## Objective

Make governed Goals closable at their explicitly selected reachable proof layer while preserving any explicitly selected live terminal gate, and prevent repeated authenticated/private access attempts when the current mechanism cannot authenticate. Keep safe supplied rendered artifacts useful as bounded evidence without projecting them into live, authenticated, complete, or stable proof.

## Lineage Decision

- At the clean candidate baseline, P148 / v10.64 was released and closed and no RULES release phase was active; P149 became active when this governed wave opened.
- This wave changes six Runtime Rule owner contracts and adds a distinct proof-reachability, explicit live-gate selection, task reconciliation, authenticated-capability, retry, and supplied-artifact evidence family with its own scenario, installation, and publication gates.
- The work is not a bounded child of Patch chronology governance or the earlier Case 17 route-scope correction family.
- P149 is therefore the smallest truthful new major. The checked public baseline had no P149 phase, v10.65 tag, or v10.65 GitHub Release when the clean candidate was established.

## Expected Output

- Goal authoring records the required proof layer, current reachable layer, successor/excluded layers, and route prerequisites.
- Execution framing closes source/code Goals at the selected reachable gate, prohibits assistant-inferred live acceptance, and preserves only a live gate explicitly selected by the user or checked governed authority as binding.
- Task reconciliation closes satisfied implementation and source/non-live verification tasks before optional live/rendered observation becomes an unselected successor; explicitly required unavailable live proof remains blocked without unchanged retry.
- Action safety preflights target, network, tool/session mechanism, authorization, approval, and bounded substitutes before authenticated/private access.
- Deterministic capability failure stops unchanged retries after at most one evidence-backed discriminating correction.
- External verification selects only reachable authorized sources after capability preflight.
- Evidence discipline defines claim boundaries for screenshots, Rendered HTML, rendered text/semantic witnesses, sanitized console/log/network exports, and authenticated harness results.
- Cases 17, 12, and 04 plus matrix/coverage make the positive and forbidden-negative branches inspectable.
- Candidate, Runtime Rule installation, publication, and fresh-public verification preserve exactly 19 Runtime Rules.

## Selected Semantic Coverage

| Obligation | Implementation state | Terminal disposition |
|---|---|---|
| Reachable proof-layer Goal fields and prerequisite ordering | implemented | verified |
| Source/local closure versus successor Product proof | implemented | verified |
| Explicit live-gate selection; no assistant-inferred live acceptance | implemented | verification pending |
| Task-list reconciliation and optional live-successor separation | implemented | verification pending |
| Authenticated/private capability and authorization preflight | implemented | verified |
| One bounded discriminating correction and deterministic no-retry | implemented | verified |
| Guest/login and 401 authentication boundary plus 403 refusal uncertainty | implemented | verified |
| Reachable authorized external-source selection | implemented | verified |
| Supplied rendered-artifact and authenticated-harness proof limits | implemented | verified |
| Real Runtime Rule installation | not started | requires approval |
| Public push, annotated tag, Release, and fresh-public proof | not started | requires approval |

## Lane Map

1. **Scenario/TestKit:** Cases 17/12/04 plus matrix and coverage define proof-reachability, terminal-gate, authenticated-capability, retry, and supplied-artifact branches.
2. **Doctrine triads:** advance six existing Runtime Rule/design/changelog owners without adding a twentieth Runtime Rule.
3. **Governed integration:** synchronize this Phase, its Patch and Patch changelog, release shard, master design/changelog, TODO, phase summary, and README.
4. **Candidate verification:** run doctrine/scenario/triad assertions, protected-byte and allowlist checks, fixture suites, Patch timeline regression, disposable install, and independent reviews.
5. **Approval-gated installation/publication:** prepare one exact SHA/scope packet before real Runtime Rule installation, push, annotated tag, GitHub Release, or dirty-checkout reconciliation.
6. **Fresh-public proof:** independently verify public master and tag, 19-Rule payload, fixtures, installation idempotence, release identity, and earlier-tag immutability.

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
- Case 17 closes a source-bounded Goal at its selected reachable layer and keeps distinct Product proof as an explicit successor.
- Case 17 prevents generic completion wording or assistant inference from selecting live acceptance and keeps authenticated Product proof inside the current Goal only when the user or checked governed authority explicitly selects it.
- Task-list reconciliation closes satisfied code/non-live tasks and routes optional live/rendered observation to an unselected successor; explicitly required unavailable live proof stays blocked without unchanged retry.
- Cases 12/04 preflight authenticated/private capability before access and stop unchanged retries after deterministic failure.
- Guest/login or `401` shows required authentication was not established; `403` shows refusal but does not alone distinguish missing authentication from insufficient authorization; none alone proves authenticated Product failure.
- Screenshot, Rendered HTML, rendered text/semantic witness, sanitized export, and authenticated harness evidence remain claim-bounded.
- No raw credential, cookie, bearer token, private key, auth-state dump, machine-local SMB/GVFS path, or universal push/tag/release requirement enters shared doctrine.
- Exactly six Runtime Rules change; the other 13 remain byte-identical and the ordered inventory remains exactly 19.
- The expanded candidate scope remains exactly 32 paths with no deletion, symlink change, or mode change.
- Bash/PowerShell fixtures, Patch timeline regression, disposable installation, second-pass idempotence, links, body sufficiency, and no governed/support runtime installation pass.
- Real runtime installation and public publication remain blocked until the exact candidate SHA/scope packet is explicitly approved.

Current evidence: the earlier five-triad/29-path candidate passed all gates, was explicitly approved, and was installed. Before publication, user-reported Goal-loop and task-list evidence expanded source to six triads and 32 paths. Corrected doctrine/scenario/six-triad/governance checks, Bash/PowerShell fixtures, 32 Patch tests, compliant Patch inventory, and two-pass disposable 19/19 installation pass. Independent reviews, renewed commit/approval, runtime reinstallation, publication, and fresh-public proof remain pending.

## Entry Conditions and Out of Scope

Entry conditions:
- clean candidate baseline is public `master` commit `2aebef62c27d3c9dd2c40e47ac2ab732dbec110c`;
- immutable v10.64 tag object `aba1ab0775188aa9ae65165a19c30e9138210014` peels to release commit `fe44a0af3885b2cf64d3556b6b3e620b9078e5c5`;
- no P149 phase, v10.65 tag, or v10.65 GitHub Release existed at baseline check;
- the dirty backup checkout is not source or publication authority and its relevant pre-existing allowlist paths matched the public baseline.

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
- publication can overwrite unrelated dirty state or drift from the approved candidate.

Rollback/containment:
- before publication, revert only the clean candidate's expanded 32-path allowlist;
- stop on any unexpected path, deletion, mode/symlink change, triad mismatch, protected-byte drift, fixture failure, or remote-master change;
- keep real Runtime Rule installation, push, tag, Release, and dirty-checkout reconciliation behind exact action-and-scope approval;
- after publication, preserve v10.65 immutably and correct defects through a later release rather than moving the tag.

## Exit Criteria

- Six owner triads are aligned, body-sufficient, and scenario-covered.
- Exactly six Runtime Rules change while the other 13 and the 19-file inventory remain protected.
- Expanded 32-path scope, references, modes, and README current-state wording pass.
- Fixture suites, Patch timeline regression, disposable install, idempotence, body/parity checks, and independent reviews pass.
- The exact candidate approval packet is accepted before real runtime installation or publication.
- Runtime installation proves 19/19 parity and second-pass idempotence.
- Public master, immutable annotated v10.65, GitHub Release, and fresh-public master/tag reproduce the verified result.
