# RULES Phase Summary

> **Current Version:** 2.23
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.35
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Status:** P150 completed — immutable v10.67 is fresh-public verified and the exact released 19-Rule payload is installed
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

- No active release phase is selected. Open the next governed objective only after design/TODO/phase/Patch startup and lineage checks identify its owner, output, and verification gate.

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

- **P150:** [Architecture conformance and no-fork gates](phase-150-architecture-conformance-and-no-fork-gates.md)
  - Output: v10.67 binds material architecture mutation to active design and the existing owner/producer/state/readers/writers/consumers path, distinguishes regressions from verified capability gaps, and blocks invented-path functional success from satisfying architecture completion.
  - Gate: exact 25-path scope, Case 18/M35-M40, three advanced Runtime Rule triads, 16 protected Runtime Rules, exact 19-file arrays, independent reviews, Bash/PowerShell fixtures, Patch tests 32/32, immutable publication, fresh-public master/tag reproduction, rollback capture, and two-pass real 19/19 installation passed.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.67
  - Identity: release commit `bd3aa36ff0d7c7712270750249031f362968854c`; annotated tag object `24c3b8982c9e8ad01456bb6139a9e6cee9246fa7`.
  - Runtime boundary: exactly three Runtime Rules changed; the other 16 and ordered 19-file inventory remained protected. The approved prior installed state is preserved at `/home/node/.claude/rules-rollback/v10.67-bd3aa36ff0d7c7712270750249031f362968854c-preinstall`.
  - Patch: [Architecture Conformance and No-Fork Gates](../patch/2026-08-11T05-01-55Z--architecture-conformance-and-no-fork-gates.patch.md).

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

## P150 Lineage and Lane Map

P150 is a distinct new major because it changes three Runtime Rule owner contracts and adds a new architecture-conformance Scenario/TestKit family rather than extending P149 proof reachability or its P149-01 presentation correction.

| Lane | Owner/output | Verification gate | Status |
|---|---|---|---|
| Scenario evidence | Case 18, observed August record, M35-M40, coverage/index | fact/observed/virtual separation, mixed dialogue, exact checked transcript, six branches | local checks and doctrine re-review pass |
| Design target | three owner designs plus runtime/verification integration shards | owner split, 1.33/1.6/1.6, architecture delta and fitness boundaries | local checks and doctrine re-review pass |
| Runtime doctrine | execution, action safety, coding discipline | exactly three changed, 16 protected, body-sufficient owner contracts | local and fresh independent payload audit pass |
| Governed sync | README, TODO, summary, phase, Patch, master design/changelog, release shard | links, sessions, lifecycle wording, density defer owner, Patch evidence | candidate checks and release re-review pass |
| Verification/publication/install | focused/full checks, fixtures, disposable payload, exact packets, fresh-public and installed parity | no unresolved review finding; exact approval before each consequential action | completed; immutable release, fresh-public proof, rollback capture, and two-pass real install pass |

---

## Earlier Lineage References

P149/P149-01, P148, P073-13 through P073-15, and P147 are released historical families. Their lineage, lane, verification, and rollback detail remains reachable through dedicated phase files, the [2026-08-09 pre-rollover snapshot](history/2026-08-09-pre-rollover-SUMMARY.md), and the [released phase archive](done/released-phase-summary-archive.md); they no longer occupy detailed active-entrypoint space.

---

## Selected Semantic Coverage

- **Architecture mutation preflight:** material route/service/client/transport/registry/state/read-write/fallback/authority change binds to active design and the current owner/producer/state/readers/writers/consumers/dependencies before source editing.
- **Regression-versus-gap:** a missing field or output is classified as existing-path regression, state/config drift, dormant/disconnected path, contract mismatch, unresolved state, or verified capability gap before infrastructure is proposed.
- **Delta ownership:** incomplete design/owner/security/rollback evidence stays `OBSERVE_ONLY`; bounded in-authority defects use `REPAIR_IN_PLACE`; additive, authority-replacement, and multi-authority changes require exact action-and-scope approval.
- **Design-backed expansion:** existing-owner insufficiency may justify expansion, but active design may independently select a new architecture; either path still uses the canonical safety approval boundary.
- **Architecture fitness:** functional proof passes through the selected design path and negative checks reject unauthorized alternate owners, routes, clients, transports, registries, state keys, dual read/write, shadows, fallback, and discovery.
- **No-fork correction:** user or checked-design rejection retires stale tasks, plans, tests, and source branches rather than preserving an alternate path through sunk work.
- **Ordinary repair:** local mapping or transformation correction inside the selected authority remains proportionate and does not inherit topology-expansion ceremony.
- **Protected runtime:** exactly three Runtime Rule triads advance; the other 16 rules and the ordered 19-file installer/fixture inventory remain protected.
- **Evidence shape:** Case 18 separates rule-enforced fact, checked observed evidence, and virtual branches; its mixed dialogue is labeled and the checked local transcript path is recorded as evidence, not portable runtime doctrine.
- **Governed density:** README and master changelog broad repair is deferred to a dedicated post-P150 document owner; current edits remain exact and bounded.
- **Out of scope:** project-specific application/data migration, installer behavior changes, a new Runtime Rule, dirty-backup reconciliation, and unapproved publication or real installation.

---

## Development Verification / TestKit Coverage

Selected route: `new_testkit_scenario` through Case 18, with Cases 17/12/04 protected as prior-family evidence, plus exact doctrine/triad/allowlist/protected-byte checks, Bash/PowerShell installer fixtures, Patch compliance, disposable installation, independent reviews, approval-gated runtime installation, and fresh-public verification.

Required checks:
- Material architecture-bearing mutation invokes the design/safety preflight before source editing, while ordinary bounded repair remains proportionate.
- Missing field/output evidence is classified through the existing owner/producer/state/readers/writers/consumers chain before a capability gap is accepted.
- Design-backed expansion or replacement is classified by `action-safety.md` and receives exact approval without requiring existing-owner insufficiency as the only valid design basis.
- Functional success for an unauthorized alternate path remains architecture-incomplete; negative alternate-authority checks and the one-authority invariant must pass.
- User or checked-design no-fork correction retires stale tasks, plans, tests, and source branches rather than preserving the rejected path through sunk work.
- Case 18 includes a realistic labeled four-turn mixed dialogue, explicit fact/observed/virtual separation, exact checked transcript evidence, and M35-M40 mapping.
- Exactly three Runtime Rules advance; the other 16 remain byte-and-mode identical and all four installer/fixture arrays preserve the exact ordered 19-file payload.
- The repaired candidate has no deletion, rename, symlink, submodule, binary, or tracked mode drift; exact path count and manifest are regenerated after final edits.
- Links, versions, sessions, master maps, substantive bodies, Patch creation evidence, density-defer owner, and candidate-safe lifecycle wording align.
- Bash/PowerShell installer fixtures, Patch timeline regression, disposable installation, second-pass idempotence, and exclusion of governed/playground files from runtime scope pass.
- Independent doctrine/security, payload, and release/no-drift reviews pass before the exact install/publication approval packet is presented.
- Exact approved publication, fresh-public verification, rollback snapshot, real Runtime Rule installation, and installed parity pass before closeout.

Current evidence: release commit `bd3aa36ff0d7c7712270750249031f362968854c` preserves the repaired 25-path candidate at immutable annotated tag object `24c3b8982c9e8ad01456bb6139a9e6cee9246fa7`. Focused Case 18/triad assertions, metadata/link/mode/shape and protected-byte checks, Bash/PowerShell fixtures, Patch timeline 32/32, Patch inventory 173/0, two-pass disposable installation, and independent doctrine/security, payload, and release/no-drift reviews passed. Fresh public master/tag clones reproduced the approved tree and gates. The exact public-tag payload then passed two real `/home/node/.claude/rules` installation passes at 19/19 byte-and-mode parity with identical second pass, ownership-manifest convergence, unrelated-file preservation, and no unexpected quarantine. Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.67.

---

## Rollback / Containment

- Preserve immutable release commit `bd3aa36ff0d7c7712270750249031f362968854c`, annotated tag object `24c3b8982c9e8ad01456bb6139a9e6cee9246fa7`, and the v10.67 GitHub Release; use a later release for any defect.
- Preserve the approved pre-install byte-and-mode rollback snapshot at `/home/node/.claude/rules-rollback/v10.67-bd3aa36ff0d7c7712270750249031f362968854c-preinstall`; installation passed, so restoration was not required.
- Keep the dirty backup checkout, unrelated repository/runtime state, and non-runtime governed/playground artifacts outside the 19-Rule install authority.
- Any later public closeout or correction remains a separate exact SHA/scope/target/evidence action and must not move the immutable tag.

---

## Next State

P150 / v10.67 is completed. Immutable publication, fresh-public master/tag verification, rollback capture, and two-pass real installation passed. No successor release phase is selected; the next governed objective must establish its own owner, output, and verification gate.

---

## History and Done References

- Current movement: [history/2026-08-09.md](history/2026-08-09.md)
- Exact pre-rollover summary: [history/2026-08-09-pre-rollover-SUMMARY.md](history/2026-08-09-pre-rollover-SUMMARY.md)
- Earlier movement: [history/2026-05-16.md](history/2026-05-16.md); [history/2026-05-08.md](history/2026-05-08.md)
- Earlier snapshot: [history/2026-05-08-pre-rollover-SUMMARY.md](history/2026-05-08-pre-rollover-SUMMARY.md)
- Released phase archive: [done/released-phase-summary-archive.md](done/released-phase-summary-archive.md); [done/](done/)
- Current master changelog: [../changelog/changelog.md](../changelog/changelog.md)
