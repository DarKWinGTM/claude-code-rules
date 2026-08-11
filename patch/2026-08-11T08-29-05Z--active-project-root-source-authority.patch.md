# Active Project Root Source Authority

> **Current Version:** 1.0
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e
> **Status:** locally verified candidate — publication and installation pending approval
> **Created At:** 2026-08-11T08:29:05Z
> **Creation Evidence:** direct creator event
> **Target Design:** design/design.md v10.68
> **Full history:** changelog/changelog.md

## Context

The checked failure moved RULES development into a clean `/tmp`/alternate checkout while the full local project remained in `/home/node/workplace/AWCLOUD/TEMPLATE/RULES`. Selected Runtime and governed release surfaces were published from the alternate location, then the canonical root was replaced from public state. Runtime payload parity passed, but newer plugin/support/project state remained split across locations.

P151/v10.68 repairs the missing authority and proof boundaries. The user-selected Active Project Root remains the only development and governed-source authority; temporary or alternate locations may provide read-only evidence or disposable verification only.

## Analysis

Existing doctrine already covers destructive confirmation, tactical convergence, evidence strength, and file-ownership classification. The missing contracts are narrower:

1. `authority-and-scope.md` must define who selects the Active Project Root and forbid assistant-selected alternate implementation authority.
2. `document-integrity.md` must distinguish the exact Runtime installation payload from the full relevant project source set and block closeout when those proof layers disagree.
3. Project-local `CLAUDE.md` must no longer recommend clean-clone/worktree development followed by sync-back.
4. Scenario/TestKit coverage must prove that a dirty or blocked root causes inspection or an explicit stop, not development elsewhere.

The Runtime inventory remains exactly 19. No new Runtime Rule is justified.

## Change Items

### 1. Active Project Root authority — replacement

**Targets:** `authority-and-scope.md`, `design/authority-and-scope.design.md`, `changelog/authority-and-scope.changelog.md`

**Before:** user and governed semantic authority were defined, but a cleaner alternate checkout could become the practical source, commit, release, or governed-state owner by assistant choice.

**After:** the Active Project Root is the canonical development workspace selected by current user direction or checked project-local authority. All source and governed mutation stays there. `/tmp`, worktrees, clean clones, alternate checkouts, public remotes, tags, and Releases are evidence/reference or disposable-verification surfaces only unless the user/project explicitly selects another root.

Dirty, modified, or untracked state must be inspected and preserved pending classification. A blocker produces an exact stop/recovery condition rather than an alternate implementation lane.

### 2. Payload versus project convergence — replacement

**Targets:** `document-integrity.md`, `design/document-integrity.design.md`, `changelog/document-integrity.changelog.md`

**Before:** selected 19-file Runtime payload parity, clean candidate parity, tag parity, or fresh-clone parity could be mistaken for whole-project convergence.

**After:** Runtime payload parity proves only the selected ordered installation payload. Full-project convergence is evaluated from the Active Project Root and covers the relevant Runtime, governed, source/config, scripts/tests, plugin/support/tooling, generated-input, mode, and classified modified/untracked state.

Mixed proof is reported explicitly:

```text
Runtime payload parity: passed
Active Project Root convergence: failed or blocked
Completion: blocked
```

### 3. Project-local source guidance — replacement

**Target:** `CLAUDE.md`

**Before:** a dirty checkout could justify completing source work in a clean clone/worktree and syncing the local checkout from released state.

**After:** `/home/node/workplace/AWCLOUD/TEMPLATE/RULES` is the checked Active Project Root. Development continues there with dirty state inspected and preserved. Temporary paths are limited to read-only evidence or disposable verification; if the root blocks safe continuation, work stops with the exact blocker.

### 4. Master governed synchronization — restructuring

**Targets:** `design/design.md`, `design/design/repository-model.design.md`, `design/design/verification-and-integration.design.md`, `README.md`, `changelog/changelog.md`, `TODO.md`, `phase/SUMMARY.md`, `phase/phase-151-active-project-root-source-authority.md`, and this Patch.

**Before:** active project surfaces report v10.67/P150 completed state and the repository model contains a stale `phase-implementation-template.md` support-path reference.

**After:** active surfaces report v10.68/P151 candidate state, distinguish project source authority from the 19-file Runtime payload, preserve portable Main RULES wording, and correct the support-path reference to `template/phase-authoring-template.md` without activating the support template.

### 5. Scenario/TestKit evidence — additive

**Targets:** `playground/cases/case-19-active-project-root-source-authority.md`, `playground/README.md`, `playground/matrix.md`, `playground/coverage.md`, and `playground/observed/2026-08.md` only when exact observed anchors are checked.

**After:** M41-M45 cover forbidden alternate development, correct root-only work, disposable evidence, blocked-root stop behavior, and two-layer proof. Observed and virtual evidence remain distinct; no provenance is fabricated.

## Verification

- Confirm all P151 source and governed mutations occur in `/home/node/workplace/AWCLOUD/TEMPLATE/RULES`.
- Compare final `plugin/**` path/status/mode/hash state against the initial verification-only baseline with zero drift.
- Verify exactly two Runtime Rule triads advance and the other 17 Runtime Rules remain byte/mode identical.
- Verify all installer/fixture arrays retain the exact ordered 19-file payload.
- Run focused Case 19/M41-M45 checks, link/version/session/body checks, `git diff --check`, and unexpected-file-shape checks.
- Run Bash and available PowerShell fixtures plus two-pass disposable installation from the Active Project Root.
- Report Runtime payload parity and Active Project Root convergence separately.
- Obtain independent doctrine and release/no-drift reviews before preparing exact publication or real-install approval packets.

Current status: local candidate verification passes. The checked evidence includes the exact 22-path non-plugin allowlist, two changed/17 protected Runtime Rules, four identical ordered 19-file arrays, 366 local-link targets, Case 19/M41-M45 assertions, Bash/PowerShell fixtures, Patch tests 32/32, two-pass disposable 19/19 installation, 179/0 Patch inventory, and a final 1,188-entry plugin baseline match. Two independent review findings were corrected, and both bounded rechecks pass with no remaining material finding. Publication, immutable v10.68 tag/Release, real runtime installation, and post-release closeout are not yet approved or verified.

## Rollback Approach

Before publication, revert only the P151 allowlisted paths inside the Active Project Root while preserving all pre-existing `plugin/**` and unrelated state. Do not clean, reset, restore, checkout, stash, replace, or sync the root from another location without explicit action-and-scope approval.

After publication, preserve immutable tags and Releases and use a later governed release for corrections. Before real installation, capture an owner-only rollback snapshot of the installed exact 19-Rule payload; restoration remains a separately approved deliberate replacement.
