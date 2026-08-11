# RULES Phase Summary

> **Current Version:** 2.24
> **Target Design:** [../design/phase-implementation.design.md](../design/phase-implementation.design.md) v2.35
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Status:** P151 active — v10.68 Active Project Root authority and payload-versus-project convergence candidate
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

- **P151:** [Active Project Root source authority](phase-151-active-project-root-source-authority.md) — v10.68 candidate active.
  - Goal: make the user- or project-selected Active Project Root the sole development and governed-source authority, with `/tmp`, worktrees, clean clones, and alternate checkouts limited to read-only evidence or disposable verification.
  - Output: two Runtime owner triads, corrected project-local guidance, master governed sync, and Case 19/M41-M45 without changing the exact 19-Rule inventory.
  - Gate: two changed/17 protected Runtime Rules, plugin zero drift, Case 19, fixtures, two-pass disposable install, independent reviews, and separate Runtime payload parity versus Active Project Root convergence results.
  - Patch: [Active Project Root Source Authority](../patch/2026-08-11T08-29-05Z--active-project-root-source-authority.patch.md).

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

## P151 Lineage and Lane Map

P151 is a distinct new major because it changes two Runtime Rule owner contracts and adds a new source-authority Scenario/TestKit family. It does not extend P150 architecture-path conformance: P150 governs mutation inside the selected architecture, while P151 governs which project root may own development and how project convergence is proved.

| Lane | Owner/output | Verification gate | Status |
|---|---|---|---|
| Root baseline/startup | Active Project Root audit, plugin baseline, P151 phase/TODO/Patch/summary | exact root identity, no non-plugin pre-existing drift, plugin exclusion | verified in local candidate scope |
| Runtime doctrine | authority and integrity Runtime/design/changelog triads plus project-local `CLAUDE.md` | root-only development, proof-layer separation, two changed/17 protected | verified in local candidate scope |
| Master governed sync | master design shards, README, changelog, TODO, phase, Patch | links, versions, candidate-safe wording, stale template reference repair | verified in local candidate scope |
| Scenario evidence | Case 19, M41-M45, coverage/index, bounded observed evidence | five branches and fact/observed/virtual separation | verified in local candidate scope |
| Verification/publication/install | static checks, fixtures, disposable payload, plugin comparison, reviews, approval packets | no plugin drift; payload and project proof reported separately; exact approval before consequential action | local candidate checks passed; publication/install blocked pending approval |

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

- **Active Project Root:** current user direction or checked project-local authority selects one canonical development workspace for the active objective.
- **Root-only mutation:** source, Runtime Rule, governed document, config, script, test, plugin/support/tooling, commit-source, and publication-source mutation stays inside that root.
- **Alternate-path boundary:** `/tmp`, worktrees, clean clones, alternate checkouts, public remotes, tags, and Releases remain read-only evidence/reference or disposable-verification surfaces unless user/project authority explicitly selects another root.
- **Dirty-root handling:** modified or untracked state is inspected, owner-classified, and preserved pending decision; it neither proves ownership nor authorizes bypass, replacement, or sync-back from public state.
- **Blocked-root behavior:** permission, conflict, or ownership ambiguity produces an exact stop/recovery condition rather than an alternate implementation lane.
- **Proof separation:** Runtime payload parity proves only the selected ordered installation payload; full-project convergence checks the relevant source set from the Active Project Root.
- **Mixed proof:** payload success cannot close the objective while project source/governed/plugin/support/tooling/generated-input/mode or classified working state remains split or unexplained.
- **Protected runtime:** exactly two Runtime Rule triads advance; the other 17 and the ordered 19-file installer/fixture inventory remain protected.
- **Evidence shape:** Case 19 separates rule-enforced doctrine, checked incident evidence when exact anchors are available, and virtual M41-M45 branches.
- **Project-local binding:** `CLAUDE.md` names the checked local Active Project Root; portable Main RULES uses the semantic term rather than exporting the workstation path.
- **Out of scope:** `plugin/**` mutation, a new Runtime Rule, root replacement, alternate-checkout development, force push, unapproved publication, and unapproved real installation.

---

## Development Verification / TestKit Coverage

Selected route: `new_testkit_scenario` through Case 19, with Case 18 protected as prior-family evidence, plus exact doctrine/triad/allowlist/protected-byte checks, Bash/PowerShell installer fixtures, Patch compliance, two-pass disposable installation, plugin baseline comparison, and independent reviews.

Required checks:
- `authority-and-scope.md` is the sole owner of Active Project Root selection; consumers reference rather than redefine that authority.
- Active project contracts contain no positive clean-clone/worktree/alternate-checkout/`/tmp` development or sync-back guidance.
- Temporary paths remain valid for bounded read-only evidence and disposable verification, but their mutations never count as implementation.
- A dirty or blocked Active Project Root causes inspection or an explicit stop/recovery condition, never assistant-selected alternate development.
- `document-integrity.md` states explicitly that Runtime payload parity is not full-project convergence and blocks mixed-proof closeout.
- Case 19 maps forbidden alternate development, correct root-only work, disposable evidence, blocked-root stop behavior, and two-layer proof to M41-M45.
- Exactly two Runtime Rules advance; the other 17 remain byte-and-mode identical and all installer/fixture arrays preserve the exact ordered 19-file payload.
- The candidate has no deletion, rename, symlink, submodule, binary, unexpected mode, or mutation outside the approved P151 allowlist.
- Final `plugin/**` path/status/mode/hash state equals the initial verification-only baseline with zero drift.
- Links, versions, sessions, master maps, substantive bodies, Patch creation evidence, and candidate-safe lifecycle wording align.
- Bash and available PowerShell fixtures plus two-pass disposable installation pass with 19/19 byte/mode/order/body parity, idempotence, unrelated-file preservation, and governed/plugin/support/template/playground exclusion.
- Independent doctrine and release/no-drift reviews pass before exact publication or real-install approval packets are presented.

Current evidence: the pre-wave audit checked local `master`, local `HEAD`, upstream, and public `origin/master` equal at `7b172a6f7c1c8e1f576788372ab8d8b9bcfdfe82`, ahead/behind `0/0`. The local candidate passes the exact 22-path non-plugin allowlist, two changed/17 protected Runtime Rules, four identical ordered 19-file arrays, 366 local-link targets, Case 19/M41-M45 assertions, Bash/PowerShell fixtures, Patch tests 32/32, two-pass disposable 19/19 installation, and 179/0 Patch inventory. The final plugin comparison matches the verification-only baseline at 1,188 entries: 63 modified tracked, 1,125 untracked, 1,187 regular files, and one symlink; baseline mode `0600` and SHA-256 `20f806be4450ef7e6f1b8457f20107e1f6e5ebdbf741b346b2fe51ad5c8a3688` remain intact. Independent reviews found two material status/evidence-label issues; both were corrected, and both bounded rechecks passed with no remaining material finding. Publication and real installation remain unverified and approval-gated.

---

## Rollback / Containment

- Preserve all pre-existing `plugin/**` paths, statuses, modes, and bytes against the verification-only baseline; any drift blocks continuation.
- Before publication, rollback is limited to the P151 allowlist inside the Active Project Root and must not reset, clean, restore, checkout, stash, replace, or sync the root from another location.
- Preserve immutable v10.67 release commit `bd3aa36ff0d7c7712270750249031f362968854c`, tag object `24c3b8982c9e8ad01456bb6139a9e6cee9246fa7`, Release, and installed rollback snapshot; P151 uses a later release rather than mutating them.
- Commit/push, annotated v10.68 tag/Release, real installation, and post-release closeout each remain separate exact action-and-scope approval gates.

---

## Next State

P151 / v10.68 is locally verified in the Active Project Root. The governed startup, plugin preservation baseline, Patch, two Runtime/design/changelog owner triads, project-local guidance, master governed sync, and Case 19/M41-M45 exist; candidate checks and plugin zero-drift comparison pass. Two independent review findings were corrected, and their bounded rechecks pass. The exact commit/push approval packet is ready; annotated tag/Release, real installation, and post-release closeout remain later separate approval gates.

---

## History and Done References

- Current movement: [history/2026-08-09.md](history/2026-08-09.md)
- Exact pre-rollover summary: [history/2026-08-09-pre-rollover-SUMMARY.md](history/2026-08-09-pre-rollover-SUMMARY.md)
- Earlier movement: [history/2026-05-16.md](history/2026-05-16.md); [history/2026-05-08.md](history/2026-05-08.md)
- Earlier snapshot: [history/2026-05-08-pre-rollover-SUMMARY.md](history/2026-05-08-pre-rollover-SUMMARY.md)
- Released phase archive: [done/released-phase-summary-archive.md](done/released-phase-summary-archive.md); [done/](done/)
- Current master changelog: [../changelog/changelog.md](../changelog/changelog.md)
