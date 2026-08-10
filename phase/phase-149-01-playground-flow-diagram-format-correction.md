# Phase 149-01 - Playground Flow Diagram Format Correction

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Parent Phase:** [P149](phase-149-proof-reachability-and-authenticated-evidence.md)
> **Phase ID:** 149-01
> **Status:** Active — local correction verified; exact publication approval pending
> **Target Release:** v10.66
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/design.md](../design/design.md) v10.65; [../design/explanation-and-presentation.design.md](../design/explanation-and-presentation.design.md) v1.24
> **Patch References:** none

---

## Objective

Remove prohibited Unicode Box Drawing characters from the P149 Case 04 and Case 12 flow diagrams without changing branch wording, ordering, proof strength, or semantic ownership. Publish the documentation-only correction as immutable v10.66 while preserving all 19 Runtime Rules and the immutable v10.65 predecessor.

## Lineage Decision

- P149 / v10.65 is published and immutable.
- A delayed SHA-bound audit found one residual Scenario/TestKit presentation defect introduced by P149: Case 04 and Case 12 use Unicode Box Drawing branch markers prohibited by the existing no-frame contract.
- The correction adds no Runtime Rule, capability, design semantic, installer behavior, or scenario family.
- P149 cannot be reopened or amended after publication; `149-01` is therefore the smallest truthful existing-family child.

## Selected Boundary

```text
P149-introduced Case 04/12 flow branches
→ remove U+2500–U+257F presentation characters
→ retain the same yes/no and nested recovery decisions
→ preserve all Runtime Rules, designs, installers, matrix/coverage, Case 17, and P149 Patch
→ publish prospective correction as immutable v10.66
```

## Exact Scopes

### Commit A — v10.65 publication/failure reconciliation

Exactly nine paths:

1. `../README.md`
2. `../TODO.md`
3. `../changelog/changelog.md`
4. `../changelog/changelog/v10.65-proof-reachability-and-authenticated-evidence.changelog.md`
5. `SUMMARY.md`
6. `phase-149-proof-reachability-and-authenticated-evidence.md`
7. `../design/design.md`
8. `history/2026-08-10.md`
9. `../todo/history/2026-08-10.md`

### Commit B — v10.66 release baseline

Exactly twelve paths:

1. `../README.md`
2. `../TODO.md`
3. `../changelog/changelog.md`
4. `../changelog/changelog/v10.65-proof-reachability-and-authenticated-evidence.changelog.md`
5. `../changelog/changelog/v10.66-playground-flow-diagram-format-correction.changelog.md`
6. `SUMMARY.md`
7. `phase-149-proof-reachability-and-authenticated-evidence.md`
8. `phase-149-01-playground-flow-diagram-format-correction.md`
9. `history/2026-08-10.md`
10. `../todo/history/2026-08-10.md`
11. `../playground/cases/case-04-destructive-action-and-topology-gate.md`
12. `../playground/cases/case-12-workflow-blocked-visual-qa.md`

The cumulative delta from immutable v10.65 through Commit B is exactly thirteen unique paths: the twelve Commit B paths plus `design/design.md` from Commit A.

`TODO.md`, `changelog/changelog.md`, and `phase/SUMMARY.md` preserve Git mode `100755`; all other selected paths use or preserve `100644`. No deletion, rename, symlink, submodule, binary, or mode change is allowed.

## Work Lanes

### Lane 1 - Scenario presentation correction

- Case 04 retains private-path preflight, one evidence-backed correction, `NO_RETRY_UNTIL_CHANGE`, and the normal non-private branch.
- Case 12 retains authorized-live versus blocked-route handling and the nested supplied-artifact versus exact-recovery-path decision.
- Only branch rendering changes; terminology, order, proof strength, and owner boundaries remain unchanged.
- Use allowed arrows, labels, and indentation; do not add Unicode Box Drawing characters or framed ASCII boxes.

### Lane 2 - Governance synchronization

- Preserve P149 as immutable v10.65 with its historical failed diagram-format gate.
- Add this child and the v10.66 release shard.
- Synchronize compact README/TODO/phase/changelog/history lifecycle anchors.
- Keep Patch posture `none` because the two-file formatting diff is directly reviewable.

### Lane 3 - Verification

- verify exact nine-path Commit A, twelve-path Commit B, and thirteen-path cumulative scopes;
- scan every added Markdown line and both complete corrected files for U+2500–U+257F;
- assert the required branch phrases and ordering;
- resolve local links and verify expected modes;
- prove all 19 Runtime Rules, designs/per-rule changelogs, installers/fixtures, Case 17, matrix/coverage, and Patch artifacts remain byte-and-mode identical to v10.65;
- run unchanged Bash/PowerShell fixture suites and two-pass disposable 19/19 installation;
- require independent presentation and release/no-drift reviews.

### Lane 4 - Publication and closeout

- prepare one exact SHA/scope packet before public v10.66 mutation;
- publish only by fast-forward, create a new annotated v10.66 tag, and create a non-draft/non-prerelease GitHub Release;
- fresh-clone public master and v10.66 independently and rerun the correction gates;
- after public proof, prepare a separate exact eight-path documentation-only closeout packet;
- never reinstall unchanged Runtime Rules or move v10.65.

## Development Verification / TestKit Coverage

Selected route: focused scenario-format and semantic assertions plus protected-byte, fixture, disposable-install, independent-review, publication-identity, and fresh-public gates.

Required positive assertions:

- both corrected scenario files contain zero codepoints in U+2500–U+257F;
- every added Markdown line in the cumulative release diff contains zero codepoints in that range;
- Case 04 branch phrases remain present and in order;
- Case 12 branch phrases remain present and in order;
- yes/no branches remain at equal logical depth and nested correction/artifact decisions remain subordinate;
- all 19 Runtime Rules and their ordered installation inventory remain unchanged;
- no runtime reinstall is required or claimed.

Forbidden assertions:

- any added Unicode Box Drawing character;
- semantic, proof-strength, ordering, or owner change in either scenario;
- Runtime Rule, design-shard, per-rule changelog, installer, fixture, Case 17, matrix, coverage, or Patch mutation;
- repository-wide zero-glyph claim beyond the two corrected files and added release lines;
- retroactive claim that v10.65 passed the failed diagram-format gate;
- public v10.66 identity before publication evidence exists.

## Out of Scope

- Runtime Rule installation or source change;
- design target-state change or version advancement;
- per-rule changelog change;
- matrix/coverage or Case 17 cleanup;
- whole-repository Unicode cleanup;
- new Patch or modification of the v10.65 Patch;
- dirty-checkout reconciliation;
- force push, tag movement, Release replacement, deletion, or cleanup.

## Risks and Containment

Risks:

- formatting edits may accidentally change branch meaning;
- a broad glyph scan may flag intentional doctrine examples or unrelated visuals;
- lifecycle wording may incorrectly claim v10.66 publication before evidence exists;
- public master may advance after approval.

Containment:

- use added-line and two-complete-file Unicode scopes rather than a whole-repository absence claim;
- combine token/order checks with independent whole-file review;
- use lifecycle-neutral candidate wording until public evidence exists;
- stop on any unexpected path, protected-byte drift, link/mode failure, semantic difference, remote-master movement, tag collision, or Release collision.

## Rollback

Before publication, keep the commits isolated on the corrective branch. If a gate fails, add a new corrective commit and regenerate evidence rather than rewriting an approved SHA. During publication, never force push or move/delete an existing tag or Release. After publication, v10.66 becomes immutable; later defects require a later release.

## Exit Criteria

- exact nine/twelve/thirteen path scopes and modes pass;
- the two scenarios contain no U+2500–U+257F characters and preserve semantics;
- protected Runtime Rule and repository surfaces remain unchanged;
- Bash/PowerShell fixtures and two-pass disposable 19/19 installation pass;
- independent reviews pass;
- exact publication approval is accepted;
- public master, immutable annotated v10.66, GitHub Release, and fresh-public master/tag checks pass;
- separately approved eight-path post-release closeout records the final public evidence without moving v10.66.
