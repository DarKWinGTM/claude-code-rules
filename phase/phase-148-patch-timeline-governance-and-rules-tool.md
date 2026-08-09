# Phase 148 - Patch Timeline Governance and RULES Tool

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 148
> **Status:** Completed — released and fresh-public-tag verified
> **Target Release:** v10.64
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)
> **Design References:** [../design/design.md](../design/design.md) v10.64, [../design/document-governance.design.md](../design/document-governance.design.md) v1.20, [../design/phase-todo-artifact.design.md](../design/phase-todo-artifact.design.md) v1.35, [../design/document-integrity.design.md](../design/document-integrity.design.md) v1.13
> **Patch References:** [../patch/2026-08-09T13-49-15Z--patch-timeline-governance-and-rules-tool.patch.md](../patch/2026-08-09T13-49-15Z--patch-timeline-governance-and-rules-tool.patch.md)

---

## Objective

Give governed Patch artifacts deterministic chronological identity from verified original creation time, provide a reusable RULES-owned Tool for safe creation/audit/migration, and release the updated Runtime Rules without changing the 19-file install boundary or mutating existing NodeClaw Patch files.

## Lineage Decision

- No RULES release phase is active; P073-15/v10.63 and P147/v10.59 are closed.
- This wave changes three Runtime Rule contracts and adds a reusable repository Tool with distinct implementation, evidence, migration, installation, and release gates.
- It is not a residual child of the Case 17/owner-compression family and cannot fit truthfully under a closed phase.
- P148 is therefore the smallest truthful new major. The checked master changelog has no v10.64 entry or tag, so v10.64 is the selected release.

## Expected Output

- Canonical timestamped Patch filename and creation-evidence contract with no Patch ID or index.
- Deterministic one-time UTC capture and exclusive creation lifecycle.
- Evidence/hash-bound exact-reference migration and explicit rollback integrity.
- `script/patch-timeline.mjs` plus focused Node tests.
- Updated Case 09 and matrix/coverage anchors.
- Read-only NodeClaw audit covering 576 selected and 199 preserved suspended-archive Patch files.
- Verified candidate/canonical/root parity, immutable annotated v10.64, GitHub Release, fresh-public proof, and documentation-only closeout.

## Selected Semantic Coverage

| Obligation | Implementation state | Terminal disposition |
|---|---|---|
| Timestamped semantic filename and matching metadata | implemented | verified |
| Original-creation meaning and admissible evidence | implemented | verified |
| No Patch ID/index or collision suffix fallback | implemented | verified |
| One-time UTC capture and exclusive create | implemented | verified |
| Exact reference resolution and relative-path recomputation | implemented | verified |
| Manifest/source/reference hash and mode gates | implemented | verified |
| Suspended archive preservation and serialized/wildcard exclusion | implemented | verified |
| Explicit apply/verify/rollback without automatic fallback | implemented | verified |
| NodeClaw existing-Patch rename | not started | out of scope |

## Lane Map

1. **Tool and tests:** implement inventory, audit-evidence, plan, create, apply, verify, rollback, deterministic manifests, and focused fixtures.
2. **Doctrine triads:** advance document governance, artifact initiation, and document integrity without duplicating exact grammar across owners.
3. **Governed integration:** Patch, Case 09, matrix/coverage, phase/TODO/changelog/README, and release shard.
4. **Read-only external validation:** classify NodeClaw's 576 selected and 199 preserved Patch files with zero filesystem or Git mutation.
5. **Verification and convergence:** Tool tests, doctrine assertions, links, modes, triads, installer fixtures, disposable install, canonical sync, and two-pass root installation.
6. **Publication:** fast-forward master, annotated tag, GitHub Release, fresh-public reproduction, and documentation-only closeout without moving the tag.

## Affected Artifacts

- `document-governance.md` triad → 1.20
- `phase-todo-artifact.md` triad → 1.35
- `document-integrity.md` triad → 1.13
- `script/patch-timeline.mjs` and `script/test-patch-timeline.mjs`
- master design parent plus governance-contract and verification/integration shards → 10.64
- `playground/cases/case-09-governed-artifact-lifecycle.md`, `playground/matrix.md`, `playground/coverage.md`
- this Phase, its Patch and Patch changelog, `phase/SUMMARY.md`, `TODO.md`, master/release changelog, README, and daily histories

## Development Verification / TestKit Coverage

Selected route: a new focused Node test suite plus existing governed lifecycle scenario coverage, installer matrices, disposable install, and read-only NodeClaw audit.

Required checks:
- canonical timestamp grammar and real-calendar validation;
- filename/`Created At` equivalence and authoritative Creation Evidence;
- mtime/ctime and ambiguous evidence rejection;
- one clock call, stable approved-`Created At` replay across CLI preview/execute, dry-run default, exact approval hash, and exclusive collision refusal;
- single-line governed metadata fields while Patch body content remains multiline-capable;
- deterministic manifests, selected/preserved count parity across commands, and stale source/reference rejection;
- exact governed references only, with URI, wildcard, and serialized payload exclusion;
- apply/verify convergence and explicit rollback behavior;
- suspended archive bytes/modes/paths remain unchanged;
- NodeClaw counts are exactly 576 selected plus 199 preserved, with before/after zero-mutation witnesses;
- Tool and governed artifacts stay outside the exact 19-file Runtime Rule payload;
- Bash/PowerShell fixtures, disposable install, two-pass root parity/idempotence, public/tag/Release identity, and fresh-clone reproduction pass.

Current evidence: focused Tool suite passes 32 tests, including stable creation-time replay, metadata/URI/count guards, and final hash/mode revalidation before replacement or removal; NodeClaw read-only proof returned 576 selected, 199 preserved, 0 mutation rows, and identical repeated before/after Patch and Git witnesses; Bash/PowerShell installer matrices, a two-pass disposable 19-Rule install, and independent Tool/governance reviews pass with the Tool excluded. The exact 27-path candidate synchronized to canonical with unrelated state preserved, and two canonical root-install passes proved 19/19 byte-and-mode parity, 19 manifest rows, no Tool installation, no quarantine, and identical converged state. Public master and fresh master/tag checkouts reproduced release commit `fe44a0af3885b2cf64d3556b6b3e620b9078e5c5`, 32 tests, fixture proof, and two-pass 19-Rule installation. Annotated tag object `aba1ab0775188aa9ae65165a19c30e9138210014` peels to the release commit, and the GitHub Release is published, non-draft, and non-prerelease.

## Entry Conditions and Out of Scope

Entry conditions:
- public master is `945503fee3cd95b7f30a33526cb7727b9765b72f`;
- immutable v10.63 tag object `24a13f14960babe01a64967dd91d7695661741ec` peels to `c7f42ecf73c965249611f6c08692310fd8bb7644`;
- no v10.64 tag/release or active RULES phase exists;
- relevant canonical files match public except the known unrelated compact TODO block.

Out of scope:
- any NodeClaw Patch rename or metadata insertion;
- Patch ID/index/registry creation;
- Runtime Rule inventory expansion;
- installer behavior changes;
- suspended archive normalization or activation;
- serialized request/transcript rewriting;
- deletion, automatic fallback/restoration, or force-moving tags.

## Risks and Rollback

Risks:
- inferred creation time can falsify chronology;
- basename replacement can corrupt unrelated references;
- interruption or path substitution can leave ambiguous state unless journal durability, descriptor-bound path checks, atomic publication, and restartable rollback all remain intact;
- archive discovery can silently reconnect suspended material;
- the Tool can accidentally enter the Runtime Rule payload.

Rollback/containment:
- before publication, revert only P148's clean-candidate allowlist;
- stop canonical synchronization on any overlap beyond the known TODO block;
- apply file-syncs and directory-syncs an exclusive journal before mutation, binds Linux mutations to opened parent directories, rejects ancestor symlinks, publishes sources from synced same-directory temporary files without clobbering, replaces references atomically, and keeps rollback explicit and hash/mode-gated across unchanged, staged, or applied states; true kernel power-loss durability remains outside checked proof;
- NodeClaw remains read-only, so no NodeClaw rollback path is selected;
- after publication, correct defects through a later release and never move v10.64.

## Exit Criteria

- Three owner triads are aligned and body-sufficient.
- Tool tests and Case 09 positive/forbidden-negative assertions pass.
- The governed P148 Patch verifies against the new filename/metadata contract.
- NodeClaw proves 576 selected plus 199 preserved files with zero mutation.
- Installer manifests remain exactly 19 Rules and exclude the Tool.
- Candidate/canonical/root parity and two-pass idempotence pass with unrelated files preserved.
- Public master, immutable annotated v10.64, GitHub Release, and fresh-public tag reproduce the verified result.
- Documentation-only closeout is pushed without moving v10.64.

## Closeout

- Release commit: `fe44a0af3885b2cf64d3556b6b3e620b9078e5c5`.
- Immutable annotated tag object: `aba1ab0775188aa9ae65165a19c30e9138210014`, peeled to the release commit.
- GitHub Release: https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.64 — published, non-draft, non-prerelease.
- Fresh public master and tag reproduced the 32-test Tool suite, Bash/PowerShell fixtures, exact 19-Rule payload, Tool exclusion, and two-pass installation idempotence.
- Canonical/root 19/19 parity remains verified, prior v10.60-v10.63 tag objects remain unchanged, and NodeClaw remained read-only at 576 selected plus 199 preserved Patch files.
- Actual NodeClaw Patch migration remains a separate unselected goal.
