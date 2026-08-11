# Phase 151 — Active Project Root Source Authority

> **Phase ID:** P151
> **Current Version:** 1.0
> **Status:** completed — v10.68 released, fresh-public verified, and installed
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Target Release:** v10.68 released
> **Design References:** [Master design](../design/design.md); [Authority and scope](../design/authority-and-scope.design.md); [Document integrity](../design/document-integrity.design.md); [Repository model](../design/design/repository-model.design.md); [Verification and integration](../design/design/verification-and-integration.design.md)
> **Patch References:** [Active Project Root Source Authority](../patch/2026-08-11T08-29-05Z--active-project-root-source-authority.patch.md)
> **Full history:** [Master changelog](../changelog/changelog.md)

---

## Objective

Make the user- or project-selected Active Project Root the only source and governed-development authority for an active objective, and prevent selected Runtime payload parity from being mistaken for full-project convergence.

พูดง่าย ๆ: งานพัฒนาต้องแก้และพิสูจน์จาก project root ตัวจริง ไม่ fork ไปทำใน `/tmp`, worktree, clean clone, หรือ alternate checkout แล้วค่อยเอากลับมาทับ root.

## Why This Phase

The checked incident showed that a clean alternate checkout could publish a correct selected Runtime payload while newer local plugin/support/project state remained elsewhere. Payload parity passed, but full-project source authority split. Existing rules covered deletion, tactical convergence, and evidence wording, but did not explicitly lock one Active Project Root or separate payload proof from project convergence.

P151 is a new major phase because it changes two Runtime owner contracts and adds a new Scenario/TestKit family rather than extending P150 architecture-path conformance.

## Expected Output

- `authority-and-scope.md` defines Active Project Root selection, precedence, and no-bypass behavior.
- `document-integrity.md` separates Runtime payload parity from Active Project Root full-project convergence.
- Project-local `CLAUDE.md` requires development directly in `/home/node/workplace/AWCLOUD/TEMPLATE/RULES` and removes clean-clone/worktree sync-back guidance.
- Master design, changelog, README, TODO, phase, and Patch surfaces align to released v10.68 state.
- Case 19 and M41-M45 exercise forbidden alternate development, root-only work, disposable verification, blocked-root stop behavior, and mixed proof results.
- The Runtime inventory remains exactly 19; only two Runtime Rule triads advance.
- Pre-existing `plugin/**` state remains path/status/mode/byte preserved.

## Completion / Verification Gate

P151 may close only when:

1. all source and governed changes exist in the Active Project Root;
2. no implementation, commit-source, release-source, or governed authority exists in `/tmp`, a worktree, clean clone, or alternate checkout;
3. the authority and integrity Runtime/design/changelog triads align at 2.8 and 1.14;
4. the other 17 Runtime Rules and the exact ordered 19-file installer payload remain byte/mode protected;
5. Case 19/M41-M45 and their index/coverage links pass focused checks;
6. Bash and available PowerShell fixtures plus two-pass disposable installation pass from the Active Project Root;
7. the final `plugin/**` baseline equals the pre-wave verification-only baseline with zero drift;
8. Runtime payload parity and Active Project Root convergence are reported separately;
9. independent doctrine and release/no-drift reviews have no unresolved material finding; and
10. publication, real installation, and post-release closeout occur only after separate exact approval.

## Entry Conditions

- Active Project Root is `/home/node/workplace/AWCLOUD/TEMPLATE/RULES`.
- Local `master`, local `HEAD`, upstream, and public `origin/master` were checked equal at `7b172a6f7c1c8e1f576788372ab8d8b9bcfdfe82`, ahead/behind `0/0`, before P151 mutation.
- Pre-existing working-tree divergence was checked under `plugin/**` only: 63 modified tracked paths and 1,125 untracked paths, with no staged, deleted, renamed, type/mode-changed, or unmerged paths.
- Verification-only plugin baseline: `/tmp/rules-v10.68-active-root-plugin-baseline.json`, mode `0600`, SHA-256 `20f806be4450ef7e6f1b8457f20107e1f6e5ebdbf741b346b2fe51ad5c8a3688`. It is evidence only and never source authority.
- No P151 phase, Case 19, or v10.68 changelog-detail collision existed when startup was opened.

## Selected Design Slice and Semantic Coverage

| Obligation | Implementation state | Terminal disposition |
|---|---|---|
| One Active Project Root selected by user/project authority | implemented in selected Runtime/design owner | verified in local candidate scope |
| No alternate implementation, commit, release, or governed authority | implemented in selected Runtime/design owner and project-local guidance | verified in local candidate scope |
| Dirty/untracked state inspected and preserved, not treated as bypass authority | implemented in selected Runtime/design owner | verified in local candidate scope |
| Temporary paths limited to read-only evidence or disposable verification | implemented in selected Runtime/design owner | verified in local candidate scope |
| Root blocker produces explicit stop/recovery condition | implemented in selected Runtime/design owner | verified in local candidate scope |
| Runtime payload parity distinct from full-project convergence | implemented in selected integrity Runtime/design owner | verified in local candidate scope |
| Split or unexplained source state blocks closeout | implemented in selected integrity Runtime/design owner | verified in local candidate scope |
| Case 19/M41-M45 | implemented with checked observed and virtual evidence boundaries | verified in local candidate scope |
| Plugin zero drift | final 1,188-entry baseline comparison passed | verified in local candidate scope |
| Publication and real install | released and installed from immutable v10.68 tag | verified in released scope |

## Lanes

| Lane | Owner/output | Gate | Status |
|---|---|---|---|
| Root baseline and governed startup | plugin baseline, P151 phase/TODO/Patch/summary | exact root identity, no non-plugin pre-existing drift, plugin exclusion | verified in local candidate scope |
| Runtime doctrine | authority and integrity Runtime/design/changelog triads; project-local `CLAUDE.md` | exact owner split, no duplicate destructive/tactical taxonomy, two changed/17 protected | verified in local candidate scope |
| Master governed sync | master design shards, README, changelog, TODO, phase, Patch | versions, links, candidate-safe wording, stale template reference repair | verified in local candidate scope |
| Scenario evidence | Case 19, M41-M45, coverage/index, bounded observed evidence | fact/observed/virtual separation and five required branches | verified in local candidate scope |
| Verification | static checks, fixtures, disposable install, plugin baseline comparison, independent reviews | payload and full-project proof separated; zero plugin drift | completed in local and fresh-public scope |
| Publication/install | commit/push, immutable tag/Release, rollback snapshot, real 19-Rule install | separate exact action-and-scope approval for each consequential stage | completed after exact approvals |

## Affected Artifacts

### Runtime owners

- `authority-and-scope.md`
- `document-integrity.md`

### Owner designs and changelogs

- `design/authority-and-scope.design.md`
- `design/document-integrity.design.md`
- `changelog/authority-and-scope.changelog.md`
- `changelog/document-integrity.changelog.md`

### Project and governed surfaces

- `CLAUDE.md`
- `README.md`
- `design/design.md`
- `design/design/repository-model.design.md`
- `design/design/verification-and-integration.design.md`
- `changelog/changelog.md`
- `changelog/changelog/v10.68-active-project-root-source-authority.changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- this phase file
- `patch/2026-08-11T08-29-05Z--active-project-root-source-authority.patch.md`

### Scenario/TestKit

- `playground/cases/case-19-active-project-root-source-authority.md`
- `playground/README.md`
- `playground/matrix.md`
- `playground/coverage.md`
- `playground/observed/2026-08.md` only if exact incident anchors are checked

## Out of Scope

- Any mutation under `plugin/**`.
- A new Runtime Rule or a change to the exact 19-file inventory.
- Worktree, clean-clone, alternate-checkout, or `/tmp` development.
- Root replacement, sync-back from released/public state, clean/reset/restore/checkout/stash, force push, tag movement, or Release replacement.
- Globalizing this repository's mandatory release lifecycle to unrelated repositories.
- Real runtime installation, push, tag, GitHub Release, or post-release commit without exact approval.

## Development Verification / TestKit Coverage

Selected route: `new_testkit_scenario` through Case 19 plus exact doctrine, triad, allowlist, protected-byte, fixture, disposable-install, and preservation checks.

Required checks:

- Active Project Root is defined once by `authority-and-scope.md`; consumers reference rather than redefine selection authority.
- Positive clean-clone/worktree/`/tmp` development or sync-back guidance is absent from active project contracts.
- Temporary paths remain valid for bounded read-only evidence and disposable verification only.
- Payload/candidate/tag/release/fresh-clone equality cannot satisfy full-project convergence.
- A dirty or blocked root causes inspection or an explicit stop, not an alternate implementation lane.
- Case 19 maps exactly to M41-M45 and reports mixed proof as:

```text
Runtime payload parity: passed
Active Project Root convergence: failed or blocked
Completion: blocked
```

- Exactly two Runtime Rules advance; the other 17 remain byte/mode identical.
- Bash and available PowerShell fixtures preserve the exact ordered 19-file payload.
- Two-pass disposable installation from the Active Project Root proves 19/19 byte/mode/order/body parity, idempotence, unrelated-file preservation, and exclusion of governed/plugin/support/template/playground files.
- Final `plugin/**` path/status/mode/hash state equals the initial baseline.
- Independent doctrine and release/no-drift reviews pass before an approval packet is prepared.

## Risks and Containment

- **Plugin state loss:** `plugin/**` is excluded from the mutation allowlist and compared to a pre-wave baseline before closeout.
- **Proof overclaim:** payload parity and project convergence remain separate named results.
- **Source split recurrence:** no source or governed mutation outside the Active Project Root counts as implementation.
- **Dirty-root bypass:** any real root blocker stops work with an exact recovery condition.
- **Publication drift:** commit, push, tag, Release, and real install remain separately approval-gated.

## Rollback Direction

Before publication, rollback means reverting only P151 allowlisted files inside the Active Project Root while preserving all pre-existing plugin and unrelated state. No destructive rollback runs without explicit action-and-scope approval.

After publication, immutable tags and Releases are never moved or deleted; corrections use a later governed release. Before real installation, capture an owner-only rollback snapshot of the installed 19-Rule payload and restore only through separately approved deliberate replacement.

## Current State

P151 is complete. Release commit `04c1c91faa6cff50cdb61b3d31c82cbb3c23819f` was fast-forwarded from the Active Project Root to public `master`, immutable annotated tag object `2a68d0e09511f879327831b5f21170399cf7be2a` selects that commit, and the non-draft/non-prerelease Release is https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.68. Fresh-public full-history tag fixtures pass. The exact 22-path release scope, two changed/17 protected Runtime Rules, four ordered installer arrays, 366 local links, Case 19/M41-M45, Bash/PowerShell fixtures, Patch tests 32/32, 179/0 Patch inventory, independent review corrections, and final 1,188-entry plugin baseline comparison pass. The owner-only rollback snapshot is `/home/node/.claude/rules-rollback/v10.68-04c1c91faa6cff50cdb61b3d31c82cbb3c23819f-preinstall`; two-pass real installation passes 19/19 byte-mode parity, identical second-pass state, and unrelated-file preservation.
