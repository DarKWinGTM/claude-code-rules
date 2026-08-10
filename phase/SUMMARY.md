# RULES Phase Summary

> **Current Version:** 2.21
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.35
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Status:** P149-01 completed — immutable v10.66 released and fresh-public verified; no next phase selected
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Daily History:** [history/2026-08-10.md](history/2026-08-10.md); [history/2026-08-09.md](history/2026-08-09.md); [history/2026-05-16.md](history/2026-05-16.md); [history/2026-05-08.md](history/2026-05-08.md)
> **Pre-Rollover Snapshot:** [history/2026-08-09-pre-rollover-SUMMARY.md](history/2026-08-09-pre-rollover-SUMMARY.md)
> **Completed Detail:** [done/released-phase-summary-archive.md](done/released-phase-summary-archive.md); [done/](done/)

---

## Current Purpose

This file is the compact active roadmap/index. Start here for current execution state; follow history/done or dedicated phase files only when detailed provenance, rollback, or completed-release evidence is needed.

---

## Active Phase Roadmap

### Active

No release phase is currently selected.

### Blocked Predecessor

- **P149:** [Proof reachability and authenticated evidence](phase-149-proof-reachability-and-authenticated-evidence.md) — immutable v10.65 published; post-publication diagram-format gate failed.
  - Published output: six Runtime Rule triads and Cases 17/12/04 implement closable proof-layer goals, authenticated/private capability preflight, deterministic no-retry, and bounded supplied-artifact evidence.
  - Blocker: a delayed SHA-bound audit found P149-introduced Unicode Box Drawing markers in the Case 04 and Case 12 flow diagrams, contrary to the existing no-frame contract.
  - Convergence owner: selected child P149-01/v10.66; immutable v10.65 remains unchanged.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.65

- **P073-14:** [Case 17 goal-first route-branch correction](phase-073-14-case-17-goal-first-route-branch-correction.md) — v10.62 published; semantic closeout blocked.
  - Published output: v10.62 makes the advisory `/goal` visible before subordinate route support and models compact-in-goal versus `/plan` as alternative goal-authoring branches.
  - Blocker: retry/status sibling candidates still act as ordered plan and verification obligations outside the queue/worker-lease-only goal scope.
  - Convergence owner: P073-15; immutable v10.62 remains unchanged.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.62

### Most Recently Completed

- **P149-01:** [Playground flow-diagram format correction](phase-149-01-playground-flow-diagram-format-correction.md)
  - Output: v10.66 removes P149-introduced Unicode Box Drawing characters from the Case 04 and Case 12 flow diagrams without changing branch wording, ordering, proof strength, or owner boundaries.
  - Gate: exact 9/12/1 commit scopes and 13-path cumulative scope, Unicode and semantic-preservation checks, protected-byte and link/mode integrity, independent reviews, Bash/PowerShell fixtures, immutable publication, and fresh-public master/tag two-pass disposable 19/19 verification passed.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.66
  - Identity: release commit `d8bffccaa304b949a713b40cd7dd2e7da4f6486e`; annotated tag object `f785e254d844b895340328c3c689a728ae449384`.
  - Runtime boundary: all 19 Runtime Rules and installers remained unchanged; no real runtime reinstall was required. Patch: none.

- **P148:** [Patch timeline governance and RULES Tool](phase-148-patch-timeline-governance-and-rules-tool.md)
  - Output: v10.64 adds verified original-creation Patch chronology, three aligned owner triads, the reusable dependency-free `script/patch-timeline.mjs` Tool, and governed lifecycle coverage without Patch IDs/indexes or Runtime Rule payload expansion.
  - Gate: 32 focused Tool tests, independent Tool/governance reviews, exact references and archive preservation, NodeClaw 576-selected/199-preserved zero mutation, exact 27-path canonical parity, two-pass canonical/root and fresh-public 19/19 installation, Bash/PowerShell fixtures, immutable annotated tag, GitHub Release identity, and fresh-public master/tag reproduction passed.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.64
  - Identity: release commit `fe44a0af3885b2cf64d3556b6b3e620b9078e5c5`; annotated tag object `aba1ab0775188aa9ae65165a19c30e9138210014`.
  - Patch: [Patch timeline governance and RULES Tool](../patch/2026-08-09T13-49-15Z--patch-timeline-governance-and-rules-tool.patch.md).

- **P073-15:** [Case 17 bounded-goal route-scope correction](phase-073-15-case-17-bounded-goal-route-scope-correction.md)
  - Output: v10.63 keeps queue/worker-lease as the only selected plan/proof slice and retains retry/backoff plus status visibility solely as deferred sibling notes outside execution and proof.
  - Gate: exact nine-path release scope/modes/links, section-bounded semantic assertions, independent pre-publication and fresh-tag whole-file reviews, protected 19-Rule identity, Bash/PowerShell fixtures, disposable installation, canonical convergence, two-pass root installation, immutable annotated tag, GitHub Release identity, and fresh-public master/tag reproduction passed.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.63
  - Root boundary: the unchanged 19-file canonical payload was installed twice as an operator-requested idempotent parity witness, not a Runtime Rule Git change.
  - Patch: none; the one-scenario semantic diff was directly reviewable.

- **P073-13:** [Case 17 semantic-owner consistency correction](phase-073-13-case-17-semantic-owner-consistency-correction.md)
  - Output: v10.61 corrects candidate/advisory separation, bounded-goal scope, and the semantic owner map while all 19 Runtime Rules and installation payloads remain unchanged; P073-14 owns the later-discovered visible-order/branch residuals and P073-15 owns the final route-scope contradiction.
  - Gate: scoped positive/forbidden owner assertions, exact nine-path/mode/link checks, protected-byte identity, Bash/PowerShell fixtures, disposable install, canonical/public/tag parity, immutable annotated tag, GitHub Release identity, and fresh-public-tag proof passed for the tagged v10.61 scope.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.61
  - Patch: none; the one-scenario semantic diff was directly reviewable.

- **P073-12:** [runtime owner-boundary repair and bounded compression](phase-073-12-runtime-owner-boundary-repair-and-bounded-compression.md)
  - Output: v10.60 repairs the Runtime Rule goal/diagram/Agent-Team owner contracts, compacts repeated context across all 19 Runtime Rules, synchronizes the exact 77-path release set, and preserves the 19-file active inventory.
  - Gate: Runtime Rule owner contracts, diagram and Agent-Team scenarios, protected literals/force words, all-19 triads, fixtures, disposable install, parity, tag, Release, and fresh-tag proof passed; later Case 17 corrections remain isolated to P073-13 through P073-15.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.60
  - Patch: [runtime owner-boundary repair and bounded compression](../patch/runtime-owner-boundary-repair-and-bounded-compression.patch.md).

- **P147:** [phase-147-evidence-first-counter-analysis-and-owner-integrity.md](phase-147-evidence-first-counter-analysis-and-owner-integrity.md)
  - Output: v10.59 adds premise-before-expansion, completed-baseline protection, proactive counter-analysis, explicit recommendation retraction, corrected changelog owner vocabulary, and bounded-helper authority clarification without widening the 19-Rule runtime set.
  - Gate: four advanced triads, 15 unchanged Runtime Rules, the exact 35-path allowlist, scenario/matrix anchors, matched Bash/PowerShell fixtures, disposable install, candidate/canonical/root/tag parity, unrelated-file preservation, annotated tag, GitHub Release identity, and fresh-public-tag verification passed.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.59
  - Children: [P147-01 premise-before-expansion and explicit retraction](phase-147-01-premise-before-expansion-and-explicit-retraction.md); [P147-02 changelog role vocabulary](phase-147-02-changelog-role-vocabulary-correction.md); [P147-03 internal helper authority](phase-147-03-internal-helper-authority-boundary.md).
  - Patches: [counter-analysis/retraction](../patch/evidence-first-counter-analysis-and-retraction.patch.md); [changelog vocabulary](../patch/changelog-role-vocabulary-correction.patch.md); [helper authority](../patch/internal-helper-authority-boundary.patch.md).

- **P146:** [phase-146-active-runtime-strategic-completeness-and-authority-convergence.md](phase-146-active-runtime-strategic-completeness-and-authority-convergence.md)
  - Output: v10.58 strengthened proactive non-trivial design collaboration and made completed migrations converge to one verified active authority with execution-disconnected quarantine and controlled restoration.
  - Gate: nine changed triads, ten unchanged runtime chains, matched Bash/PowerShell fixtures, 19/19 candidate/canonical/root/fresh-clone parity/body, exact manifest order, unrelated-file preservation, clean master, annotated tag, and GitHub Release identity passed.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.58
  - Children: [P146-01](phase-146-01-proactive-analysis-and-design-completeness.md); [P146-02](phase-146-02-single-authority-migration-and-quarantine.md).

Earlier released phase-map detail remains preserved in the [2026-08-09 pre-rollover snapshot](history/2026-08-09-pre-rollover-SUMMARY.md), [released phase archive](done/released-phase-summary-archive.md), and dedicated completed phase files.

---

## P149 Lineage and Lane Map

### Lineage

P149 / v10.65 introduced the distinct proof-reachability and authenticated-evidence family and was published immutably. Its doctrine, runtime installation, and public technical reproduction passed, but a delayed audit found a residual presentation defect in two P149 Scenario/TestKit files. Because the correction changes no capability, Runtime Rule, architecture, or scenario family, selected `P149-01 / v10.66` is the smallest truthful existing-family child; P149 and v10.65 must not be reopened or amended.

### Lanes

| Lane | Owner/output | Verification gate | Status |
|---|---|---|---|
| P149 released capability | six Runtime Rule triads plus Cases 17/12/04 | doctrine, runtime parity, publication, fresh-public technical reproduction | released; historical diagram-format gate failed |
| P149-01 scenario correction | Case 04 and Case 12 flow diagrams | zero Box Drawing characters; branch semantics unchanged | released and fresh-public verified |
| Corrective governance | child Phase, release shard, README/TODO/summary/changelog/history | truthful v10.65 failure record, exact links/modes/scopes | completed |
| Protected state | 19 Runtime Rules, designs/per-rule changelogs, installers/fixtures, Case 17, matrix/coverage, P149 Patch | byte/mode identity against immutable v10.65 | verified unchanged |
| Publication | public master, annotated v10.66, Release, fresh clones | exact approval, immutable identities, fresh-public reproduction | released and verified; no runtime reinstall required |

---

## P148 Lineage and Lane Map

### Lineage

P073-15 and P147 were closed, while P148 introduced a distinct Patch-governance and reusable-Tool capability with its own migration, verification, install, and release gates. Current-phase and existing-family child fit were therefore ruled out; P148 was the smallest truthful new major.

### Lanes

| Lane | Owner/output | Verification gate | Status |
|---|---|---|---|
| Tool | `script/patch-timeline.mjs` plus focused Node tests | filename/metadata/evidence, manifest, exact reference, create/apply/verify/rollback, archive preservation | verified and released; 32 tests and independent review pass |
| Doctrine | three Runtime Rule/design/changelog triads | owner separation, no ID/index, no inferred timestamps, substantive bodies | verified and released; independent governance review passes |
| Governed integration | Patch, Case 09, matrix/coverage, Phase/TODO/changelog/README | exact links, modes, truthful lifecycle state | verified and released; canonical convergence passed |
| NodeClaw audit | 576 selected and 199 preserved files | before/after Git and filesystem zero-mutation witnesses | verified read-only; 0 mutation rows and 576 evidence blockers |
| Canonical/root | exact allowlist and 19 installed Runtime Rules | overlap safety, 19/19 parity, two-pass idempotence, Tool excluded | verified; 27-path parity and two-pass 19/19 install pass |
| Publication | public master, annotated v10.64, Release, fresh clones, closeout | immutable identity and fresh-public reproduction | verified and released; documentation-only closeout published |

---

## Earlier Lineage References

P073-13, P073-15, and P147 are released historical families. Their lineage, lane, verification, and rollback detail remains reachable through their dedicated phase files, the [2026-08-09 pre-rollover snapshot](history/2026-08-09-pre-rollover-SUMMARY.md), and the [released phase archive](done/released-phase-summary-archive.md); they no longer occupy detailed active-entrypoint space.

---

## Selected Semantic Coverage

- **Done-point feasibility:** proposed Goal/plan completion points are assessed against current scope, environment, capability, approval, and observable proof path before they become binding.
- **Proof reachability:** governed Goals identify required proof, current reachable proof, successor/excluded layers, and prerequisite state without treating prerequisite completion as proof.
- **In-place repair:** an assistant-inferred infeasible Goal/plan point that was never explicitly selected moves to successor scope without requiring a replacement Goal or retry loop; tasks reconcile immediately.
- **Reachable closure:** a truthfully source/local Goal closes at its selected reachable layer; a genuinely distinct downstream Product proof becomes an explicit prerequisite-bearing successor.
- **Terminal-gate preservation:** authenticated/live Product proof explicitly selected as the current terminal gate remains binding until passed or explicitly narrowed.
- **Noun-safe proof classification:** Product-facing names such as pinned-host SSH diagnostics, exact-request recovery, database, or mutation-capable code do not select live execution or mutation proof; the declared done condition, proof gate, scope, and checked authority control.
- **Authenticated capability:** target, network, tool/session mechanism, authorization, approval, and bounded substitutes are classified before private access.
- **Deterministic retry:** after at most one checked discriminating correction, unchanged capability failure becomes `DETERMINISTIC_NON_RETRIABLE / NO_RETRY_UNTIL_CHANGE`.
- **Access witness:** a guest/login response or `401` shows required authentication was not established; `403` shows refusal but leaves missing-authentication versus insufficient-authorization cause unresolved; none alone proves Product failure.
- **Source eligibility:** external verification ranks reachable authorized claim-fit sources or bounded substitutes after capability preflight.
- **Supplied evidence:** screenshot, Rendered HTML, rendered text/semantic witness, sanitized console/log/network export, and authenticated harness results remain bounded to their directly inspected evidence dimensions.
- **Protected scope:** this wave adds no Runtime Rule, installer feature, raw secret/session path, machine-local shared default, universal release doctrine, or dirty-checkout mutation.
- **Patch chronology:** timestamped semantic filenames and matching metadata represent verified original creation time; revisions and moves preserve that identity.
- **Creation evidence:** direct creator/transcript/birthtime/operator evidence is admissible; mtime/ctime and indirect chronology remain prohibited.
- **Safe lifecycle:** creation captures UTC once and fails exclusively on collision; no Patch ID/index or auto-suffix exists.
- **Migration integrity:** manifest/hash-bound exact-reference updates, wildcard/serialized exclusions, archive sentinels, former-path inactivity, and explicit rollback remain one verification gate.
- **RULES Tool boundary:** `script/patch-timeline.mjs` is repository support and never enters the 19-file Runtime Rule install payload.
- **NodeClaw boundary:** existing Patch migration is out of scope; only the 576-selected/199-preserved zero-mutation audit is selected.
- **Bounded-goal route scope:** the selected queue/worker-lease `/goal`, `Plan draft`, and verification route stay within queue/lease execution and proof; retry/backoff and status visibility remain deferred sibling notes outside that goal.
- **Goal-owner scenario consistency:** execution selects posture, goal-authoring constructs and selects one subordinate route branch, and presentation renders only after the artifact or surface is complete.
- **Visible goal-first ordering:** advisory `/goal` precedes `Plan draft`, `Plan basis`, deferred sibling notes, and verification-route support; compact-in-goal support and `/plan` remain alternative branches.
- **Durable route reference:** keep `/goal` before `Plan reference:` and emit no reference until a route-only file exists and was verified; Case 17 creates no such file.
- **Premise integrity:** separate goal, checkable premise, path, and action; inspect current ownership/dependencies before material expansion.
- **Completed baseline:** checked narrow completed work remains active until evidence shows a real scope/gate defect.
- **Counter-analysis:** preserve a valid goal while correcting a false premise and recommending the smallest supported route.
- **Recommendation correction:** retract/revise invalidated assistant advice with failed premise, contrary evidence, corrected route, and remaining gate.
- **Changelog ownership:** active same-chain detail remains indexed under its active chain; `changelog/done/` remains inactive reference/provenance history; no fallback owner exists.
- **Helper authority:** new objective/durable Team expansion remains advisory; the smallest bounded support topology inside a selected objective may be invoked under the canonical routing owner and remains leader-verified.
- **Out of scope:** ticket application/data migration, installer behavior changes, new Runtime Rule, new scenario family, broad owner rewrites, and any automatic restoration path.

---

## Development Verification / TestKit Coverage

Selected route: `new_testkit_scenario` through Cases 17/12/04 plus exact doctrine/triad/allowlist/protected-byte checks, Bash/PowerShell installer fixtures, Patch timeline regression, disposable installation, independent reviews, approval-gated runtime installation, and fresh-public verification.

Required checks:
- Proposed Goal/plan done points receive a closability check before emission; M34 repairs an unselected assistant-authored infeasible point in place rather than requiring a replacement Goal or impossible retries.
- A source-bounded Goal closes at its selected reachable proof layer and a distinct Product proof remains an explicit successor.
- Operational capability names do not select live proof; the pinned-host SSH diagnostic and exact-request recovery variant closes at codebase + non-live proof while deploy/restart/runtime/live result/mutation/apply remain successors.
- An explicitly selected authenticated/live Product terminal gate remains inside the current Goal until passed or explicitly narrowed.
- Authenticated/private capability and authorization are preflighted before access; guest/login or `401` indicates required authentication was not established, while `403` indicates refusal without identifying authentication versus authorization cause.
- At most one evidence-backed discriminating correction runs before deterministic `NO_RETRY_UNTIL_CHANGE`.
- Screenshots, Rendered HTML, rendered text/semantic witnesses, sanitized exports, and authenticated harness results remain within their canonical proof limits.
- No raw credential/session material, machine-local SMB/GVFS path, private shared default, or universal repository publication requirement enters the candidate.
- Exactly six Runtime Rules advance; the other 13 remain byte-identical and the ordered inventory stays exactly 19.
- The expanded scope remains exactly 32 paths with no deletion, symlink change, unexpected file, or mode change.
- Task reconciliation closes satisfied code/non-live tasks before optional live observation becomes an unselected successor; explicitly required unavailable live proof remains blocked with a resume condition and no unchanged retry.
- Links, versions, sessions, master maps, substantive bodies, and candidate-safe lifecycle wording align.
- Bash/PowerShell installer fixtures, Patch timeline regression, disposable installation, second-pass idempotence, and exclusion of governed/support files from runtime scope pass.
- Independent doctrine and release/no-drift reviews pass before the exact install/publication approval packet is presented.
- Real Runtime Rule installation, public master, annotated v10.65, GitHub Release, and fresh-public master/tag proof pass before closeout.

Current evidence: P149 / v10.65 was installed and published immutably, after which a delayed SHA-bound audit found P149-introduced Box Drawing characters in Cases 04 and 12; its historical format gate remains failed. P149-01 published the prospective correction as v10.66 from release commit `d8bffccaa304b949a713b40cd7dd2e7da4f6486e` at annotated tag object `f785e254d844b895340328c3c689a728ae449384`. Public master/tag scope, Unicode, semantics, protected bytes, fixtures, and two-pass disposable 19/19 installation were fresh-clone verified without a real runtime reinstall.

---

## Rollback / Containment

- Preserve immutable v10.65 and all earlier tags/Releases; correct the format defect only through selected child P149-01/v10.66.
- Stop on unexpected paths, deletion, symlink/mode change, protected-byte drift, semantic change in Cases 04/12, test/review failure, or remote-master change.
- v10.66 push, annotated tag, GitHub Release, and any later closeout push each require their exact SHA/scope/target/evidence packet and explicit approval.
- Do not reinstall unchanged Runtime Rules, mutate the dirty backup checkout, or request raw credential/session material.

---

## Next State

P149 / v10.65 remains published and immutable with its delayed diagram-format failure preserved. P149-01 / v10.66 is released and fresh-public verified, with scenario semantics, all 19 Runtime Rules, installers, matrix/coverage, Case 17, and the P149 Patch unchanged. No next release phase is selected; the documentation-only closeout remains separately approval-gated until pushed.

---

## History and Done References

- Current movement: [history/2026-08-09.md](history/2026-08-09.md)
- Exact pre-rollover summary: [history/2026-08-09-pre-rollover-SUMMARY.md](history/2026-08-09-pre-rollover-SUMMARY.md)
- Earlier movement: [history/2026-05-16.md](history/2026-05-16.md); [history/2026-05-08.md](history/2026-05-08.md)
- Earlier snapshot: [history/2026-05-08-pre-rollover-SUMMARY.md](history/2026-05-08-pre-rollover-SUMMARY.md)
- Released phase archive: [done/released-phase-summary-archive.md](done/released-phase-summary-archive.md); [done/](done/)
- Current master changelog: [../changelog/changelog.md](../changelog/changelog.md)
