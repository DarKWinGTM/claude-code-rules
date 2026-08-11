# Claude Code Rules - TODO

> **Last Updated:** 2026-08-11
> **Current Release:** v10.67 candidate active; v10.66 remains latest published and immutable
> **Active Wave:** P150 / v10.67 architecture conformance and no-fork gates
> **History:** [2026-08-10 movement](todo/history/2026-08-10.md); [2026-08-09 movement](todo/history/2026-08-09.md); [2026-08-09 pre-rollover snapshot](todo/history/2026-08-09-pre-rollover-TODO.md); [earlier history](todo/history/)
> **Done Detail:** [rules release closeouts](todo/done/rules-release-closeouts.md); [todo/done/](todo/done/)

---

## Active / In Progress

- [ ] **P150 / v10.67 architecture conformance and no-fork gates** is active on a clean public-master candidate.
  - Goal: bind architecture-bearing source mutation to active design and the existing owner/producer/state/readers/writers/consumers path before implementation.
  - Selected owners: `execution-and-goal-frame.md`, `action-safety.md`, and `coding-discipline.md`; no new Runtime Rule or installer inventory change.
  - Verification: one Case 18 family covers route-owner fork, regression-versus-gap, invented-path tests, ordinary repair, approved expansion, and no-fork correction lock.
  - Governance: [P150](phase/phase-150-architecture-conformance-and-no-fork-gates.md) and [Patch](patch/2026-08-11T05-01-55Z--architecture-conformance-and-no-fork-gates.patch.md); diagram posture `not required`.
  - Implemented in candidate scope: Case 18/M35-M40, three advanced designs, three Runtime Rule gates, three per-rule changelogs, master design/changelog, release shard, README, phase/TODO/Patch, and playground synchronization.
  - Verified on the repaired 25-path candidate: focused Case 18/triad assertions, metadata, links/anchors, whitespace/modes, no-Box-Drawing checks, three-changed/16-protected Runtime Rules, unchanged 19-file arrays, Bash/PowerShell fixtures, Patch tests 32/32, and two-pass disposable 19/19 installation passed.
  - Repair scope added two required integration design shards and one August observed-evidence log while keeping governed/playground content outside the Runtime payload.
  - Independent doctrine/security, fresh 25-path payload, and final release/no-drift re-reviews pass; the exact Patch creator event is anchored.
  - Current gate: create the local candidate commit, regenerate the exact commit-bound publication/install evidence packet, and request explicit approval before any public or real-install mutation.
  - Publication and real runtime installation remain separate exact SHA/scope approval-gated actions.

---

## Recently Completed

- [x] **P149-01 / v10.66 playground flow-diagram format correction** was fast-forwarded to public `master`, annotated-tagged, released, and fresh-public master/tag verified.
  - Published release commit `d8bffccaa304b949a713b40cd7dd2e7da4f6486e` at immutable annotated tag object `f785e254d844b895340328c3c689a728ae449384`; Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.66
  - Verified exact 9/12/1 commit scopes and 13-path cumulative scope, zero U+2500–U+257F characters in the corrected scenarios and added Markdown lines, semantic preservation, protected bytes, links/modes, independent reviews, Bash/PowerShell fixtures, and two-pass disposable 19/19 installations locally and from fresh public master/tag clones.
  - All 19 Runtime Rules and installers remained unchanged, so no real runtime reinstall was required. Patch posture remained `none`.
- [x] **P149 / v10.65 proof reachability and authenticated evidence** was installed, pushed to public `master`, annotated-tagged, released, and fresh-public technically verified.
  - Published release commit `2e751bbb620eb68527e5a67eb6348196a67727e7` at immutable annotated tag object `cc7d322d3b1e4e7785373370d2d3c9eb8a8a395e`; Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.65
  - A delayed audit found prohibited Unicode Box Drawing characters introduced in Case 04 and Case 12. The historical v10.65 diagram-format gate remains failed; P149-01/v10.66 owns the prospective correction without changing v10.65.
- [x] **P148 / v10.64 Patch timeline governance and RULES Tool** was synchronized to canonical, installed into the root profile, pushed to public `master`, annotated-tagged, released, and fresh-public master/tag verified.
  - Added verified original-creation UTC Patch identity, matching `Created At`/Creation Evidence, exact-reference migration integrity, and the reusable dependency-free `script/patch-timeline.mjs` Tool without Patch IDs or an index.
  - Verified 32 focused Tool tests, independent Tool/governance reviews, the NodeClaw 576-selected/199-preserved zero-mutation audit, Bash/PowerShell fixtures, exact 27-path canonical parity, two-pass root and fresh-public 19/19 installation parity/idempotence, Tool exclusion, and no quarantine.
  - Published release commit `fe44a0af3885b2cf64d3556b6b3e620b9078e5c5` at immutable annotated tag object `aba1ab0775188aa9ae65165a19c30e9138210014`; actual NodeClaw Patch migration remains unselected.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.64
- [x] **memory-context-intelligence v0.1.79 / package 0.9.31 corrective public-skill alignment** was pushed on the dedicated corrective branch, annotated-tagged, released, and fresh-tag verified.
  - Corrected the immutable v0.9.30 metadata defect by aligning the manifest, analysis skill, and init skill at `0.9.31`; also corrected user-scope config wording, evidence/release descriptions, and the native-agent design shard metadata.
  - Verified exact 17-path plugin scope with zero deletions, focused `21 passed`, source/clean-candidate/fresh-tag full suites `132 passed`, plugin validation PASS, remote branch/tag parity at `5e58f018a2b057ffdd009aeca3d88146e0cfab20`, and non-draft/non-prerelease GitHub Release identity.
  - Confirmed the earlier v0.9.30 branch and annotated tag still resolve to `02b15e29fe5eaf7c05e0a81d0b92ef4773cfd677`; no tag or release was moved or replaced.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/memory-context-intelligence--v0.9.31

- [x] **memory-context-intelligence v0.1.78 / package 0.9.30 deterministic standalone additional-stage emission** was pushed on the dedicated plugin branch, annotated-tagged, released, and fresh-tag verified.
  - Delivered read-only initial analysis, explicit later trial selection, one rich standalone artifact per Topic, normalized evidence, full-set collision refusal, no overwrite path, and additional-root containment while keeping Main RULES promotion separate.
  - Verified exact 37-path plugin scope with zero unexpected paths/deletions, clean-clone `113 passed` focused and `132 passed` full suites, remote branch/tag parity at `02b15e29fe5eaf7c05e0a81d0b92ef4773cfd677`, non-draft GitHub Release identity, and fresh-tag manifest `0.9.30` with `132 passed` plus plugin validation PASS.
  - Main RULES, other plugins, and the fifteen existing additional-stage artifacts remained outside the release scope.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/memory-context-intelligence--v0.9.30

- [x] **P073-15 / v10.63 Case 17 bounded-goal route-scope correction** was pushed to public `master`, tagged, released, and fresh-public-tag verified.
  - Corrected the final Case 17 contradiction by keeping queue/worker-lease work as the only selected plan/proof slice and retaining retry/backoff plus status visibility solely as deferred sibling notes outside execution and proof.
  - Verified exact nine-path release scope/modes/links, section-bounded assertions, independent whole-file doctrine review, protected 19-Rule bytes, Bash/PowerShell fixtures, disposable installation, canonical convergence, two-pass root installation, annotated tag and GitHub Release identity, and fresh-public master/tag reproduction.
  - Runtime Rules and installer sources remained unchanged; root installation was an operator-requested idempotent 19/19 parity witness.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.63
- [x] **P073-13 / v10.61 Case 17 semantic-owner consistency correction** was pushed to public `master`, tagged, released, and fresh-public-tag verified.
  - Corrected candidate/advisory posture separation, goal-authoring route ownership, phase/TODO evidence/linkage boundaries, and the narrow queue/worker-lease goal; P073-14 owns the later visible-order/branch residuals and P073-15 owns the final retry/status route-scope contradiction.
  - Verified the exact tagged v10.61 scope, protected-byte identity, Bash/PowerShell fixtures, disposable install, candidate/canonical/public/tag parity, annotated tag, GitHub Release identity, and v10.60 immutability.
  - Runtime Rules and root installation remained unchanged at 19/19 parity.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.61
- [x] **P073-12 / v10.60 runtime owner-boundary repair and bounded compression** was installed, pushed to public `master`, tagged, released, and fresh-public-tag verified.
  - Delivered the Runtime Rule decision → construction → rendering contract, conditional diagram startup/synchronization, Agent Team safety-to-worker lifecycle separation, and all-19 bounded Runtime Rule compaction.
  - Verified the exact 77-path scope, 19 aligned/body-sufficient triads, protected registries/force words, zero newly introduced broken links, Bash/PowerShell fixture matrices, disposable install, candidate/canonical/root/public-tag parity, unrelated-file preservation, annotated tag, and GitHub Release identity. A later integrated review found stale owner wording isolated to Case 17; P073-13 owns that corrective release.
  - Runtime reduction: 7,214 bytes, 141 lines, and 1,286 words; active inventory remains exactly 19.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.60
- [x] **P147 / v10.59 evidence-first counter-analysis and owner-integrity corrections** was installed, pushed to public `master`, tagged, released, and fresh-public-tag verified.
  - Delivered premise-before-expansion, completed-baseline protection, proactive counter-analysis, evidence-shaped agreement and explicit retraction, corrected changelog owner vocabulary, and bounded-helper authority clarification while keeping the 19-Rule runtime boundary unchanged.
  - Verified the exact 35-path allowlist, four advanced triads, 15 byte-identical Runtime Rules, scenario/matrix anchors, Bash and PowerShell fixture matrices, disposable install, 35/35 candidate/canonical parity, 19/19 canonical/root/tag parity and body sufficiency, unrelated-file preservation, annotated tag, and GitHub Release identity.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.59
- [x] **P146 / v10.58 strategic design completeness and authority convergence** was installed, pushed to `master`, tagged, released, and fresh-public-clone verified.
  - Delivered proactive non-trivial analysis/design completeness, one-active-authority migration convergence, execution-disconnected external quarantine, controlled restoration, and hardened Bash/PowerShell installer ownership/path/link handling.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.58
- [x] **P073-11 / v10.57 runtime owner semantic conflict resolution and compression** was installed, pushed, tagged, released, and verified.
  - Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.57
- Earlier completed release detail remains reachable through the [2026-08-09 pre-rollover snapshot](todo/history/2026-08-09-pre-rollover-TODO.md), [rules release closeouts](todo/done/rules-release-closeouts.md), and dedicated completed phase/patch/changelog files.

---

## Deferred / Not Selected

- [ ] `memory-context-intelligence` phase 030 shared-marketplace bridge/reproof remains planned and approval-sensitive.
  - Gate: recheck current runtime state and obtain explicit action-and-scope approval before marketplace/install/enable/registry/cache mutation.
- [ ] `memory-context-intelligence` phases 017-018 main RULES promotion/merge remain deferred; trial and historical evidence do not authorize promotion.
- [ ] README and master changelog density repair remains deferred to a dedicated post-P150 `document-integrity` / `document-governance` phase; P150 uses exact anchored edits only, and the repair must open before the next broad absorption into either parent. Master-design pressure remains part of the same owner review.
- [ ] Automated documentation-compliance validation and broad integration testing remain deferred by user direction.

---

## History and Preservation

- Current rollover movement: [todo/history/2026-08-09.md](todo/history/2026-08-09.md)
- Exact pre-rollover active entrypoint: [todo/history/2026-08-09-pre-rollover-TODO.md](todo/history/2026-08-09-pre-rollover-TODO.md)
- Earlier daily movement: [todo/history/2026-05-16.md](todo/history/2026-05-16.md); [todo/history/2026-05-08.md](todo/history/2026-05-08.md)
- Earlier pre-rollover snapshot: [todo/history/2026-05-08-pre-rollover-TODO.md](todo/history/2026-05-08-pre-rollover-TODO.md)
- Completed-detail archive: [todo/done/rules-release-closeouts.md](todo/done/rules-release-closeouts.md); [todo/done/](todo/done/)
