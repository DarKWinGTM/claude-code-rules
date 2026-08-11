# Verification and Integration - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.68
> **Session:** 48a3ef9b-50cf-4574-8f00-4f6b6e28f76e (2026-08-11)
> **Section:** Verification checklist and integration
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Verification Checklist

### Runtime and governed authority

- [ ] README remains overview/onboarding/current-state only; detailed target truth, history, execution, and before/after review stay with their owning surfaces
- [ ] Current user direction or checked project-local authority identifies one Active Project Root before meaningful mutation, and every source/governed/config/script/test/plugin-support-tooling/commit/release input originates there
- [ ] `/tmp`, worktrees, clean clones, alternate checkouts, public remotes, tags, and Releases are read-only evidence/reference or disposable-verification surfaces unless user/project authority explicitly selects another root
- [ ] Dirty, modified, and untracked root state is inspected and preserved pending owner classification; a permission/conflict/ownership blocker stops work with an exact recovery condition rather than creating an alternate implementation lane
- [ ] Runtime Rules remain body-sufficient active behavior contracts and the source-owned install inventory remains exactly the ordered 19 root files
- [ ] Runtime payload parity proves only the selected order/modes/bodies/manifests/destination set; full-project convergence is checked separately from the Active Project Root across relevant governed/source/config/scripts/tests/plugin/support/tooling/generated-input/mode/classified-working-state surfaces
- [ ] Candidate/tag/release/fresh-clone/installed payload equality never authorizes Active Project Root replacement or whole-project/no-drift wording while source state remains split or unexplained
- [ ] Governed design/changelog chains classify `single-file-bootstrap`, `flat-sibling-shards`, `same-stem-subfolder-normalized`, or `archive-history-reference-only` before meaningful normalization
- [ ] Exactly one active parent model remains per chain; inactive history, quarantine, and `done/` never become competing authority, generated input, or automatic fallback
- [ ] Parent/shard/version links, maps, and back-links resolve across the selected chain shape
- [ ] `TODO.md` and `phase/SUMMARY.md` remain bodyful active entrypoints with reachable history/done detail; touched size pressure is repaired or assigned a visible governed repair slice
- [ ] Phase identity stays lineage-first and forward-valid numeric forms remain `phase-NNN`, `phase-NNN-NN`, and `phase-NNN-NN-NN`
- [ ] Non-trivial analysis/design completes material outcome, constraint, dependency, failure, alternative, and verification gaps without fabricating facts or replacing user authority
- [ ] Implementation closeout covers or explicitly disposes material behavior, state, integration, failure, observability, and verification obligations
- [ ] Material route/service/client/transport/registry/state/read-write/fallback/authority mutation checks the active design and current owner/producer/state/readers/writers/consumers/dependencies before source editing
- [ ] Missing field/output evidence is classified as regression, state/config drift, dormant/disconnected path, contract mismatch, unresolved state, or verified capability gap before infrastructure is proposed
- [ ] Architecture deltas remain `OBSERVE_ONLY` when material ownership/design/security/rollback evidence is incomplete, use `REPAIR_IN_PLACE` for bounded in-authority defects, and require exact approval for additive, replacement-authority, or multi-authority scope
- [ ] Architecture-bearing completion requires functional proof through the selected design path plus negative architecture-fitness proof against unauthorized alternate owner/route/client/transport/registry/state key/dual read-write/shadow/fallback/discovery
- [ ] User or checked-design no-fork correction retires incompatible tasks, plans, tests, and source branches before continuation
- [ ] Successor posture follows execution decision → goal construction → presentation rendering, with no consumer-side promotion and exact `/goal` then `Plan reference:` order
- [ ] Structural/visual changes resolve diagram posture after design; ordinary design edits may use `not required` without opening a subject diagram
- [ ] Duplicate/stale Agent Team presence blocks unchanged retry in action safety, then worker routing audits and decides lifecycle
- [ ] Governed Patch filenames and `Created At` represent the same verified original-creation UTC instant, retain semantic identity, and introduce no Patch ID/index or collision suffix fallback
- [ ] Legacy Patch manifests block ambiguous evidence and duplicate destinations, update only resolved exact references, preserve suspended archives, and prove target convergence plus former-path inactivity
- [ ] The Patch timeline Tool passes focused creation/audit/plan/apply/verify/rollback tests, replays preview-approved creation time, rejects multiline governed metadata, excludes URI-shaped text from exact-reference rewrites, keeps command count expectations aligned, persists a synced journal before mutation, rejects ancestor symlinks, uses atomic publication boundaries, supports restartable explicit rollback, and remains outside the 19-file Runtime payload

### Installer, quarantine, and restoration

- [ ] The [installer architecture](installer-architecture.design.md) and both platform implementations select one project-root target and the same ordered 19-file payload
- [ ] Manifest validation rejects malformed, duplicate, traversal, or directory-like records before active payload mutation
- [ ] Symlink/reparse-point ancestors under the selected project boundary, direct linked rules/quarantine directories, and manifest/active-target links including broken links fail closed without modifying external trees or replacing other-owner directory entries
- [ ] Active-name ownership preflight preserves matching current/prior/historical source-owned files and fails closed on modified or unowned collisions
- [ ] Every planned quarantine source/type is checked before mutation; deterministic later failures leave the project tree unchanged
- [ ] The complete active payload and manifest are staged before runtime replacement, with rollback state for quarantine moves, active replacements, and manifest replacement
- [ ] Unchanged obsolete manifest-owned files, repository-matching retired candidates, and prior installer-owned in-tree quarantine move to external execution-disconnected quarantine rather than being deleted
- [ ] Modified manifest-owned, unmatched, unknown, unrelated, and other-owner files remain unchanged
- [ ] External quarantine is absent from active manifests/discovery and is never read by normal install, retry, restart, rebuild, test, fallback, or restoration paths
- [ ] Quarantine poisoning, rename, or unavailability does not affect normal reinstall; idempotent reruns do not restore former files or create a second authority
- [ ] Controlled restoration uses an independently verified exact known-good source/tag/commit through the normal installer and re-establishes exactly one active authority without consulting quarantine
- [ ] Bash and PowerShell fixture matrices cover equivalent ownership, quarantine, disconnection, idempotency, restoration, traversal, collision, parity, and body-sufficiency cases

### Release and evidence boundary

- [ ] Changed-path allowlist, `git diff --check`, changed triad versions, unchanged-chain versions, links, literals, force words, and file modes pass
- [ ] Case 19 and M41-M45 cover forbidden alternate development, correct root-only work, disposable evidence, blocked-root stop behavior, and Runtime-payload-PASS/project-convergence-BLOCKED results
- [ ] Case 18/M35-M40 remain protected architecture-conformance evidence and are not rewritten into project-root authority
- [ ] Exactly the authority-and-scope 2.8 and document-integrity 1.14 Runtime/design/changelog triads advance; the other 17 Runtime Rules remain byte-and-mode identical
- [ ] Final `plugin/**` path/status/mode/hash state equals the pre-wave verification-only baseline, with no mutation outside the P151 allowlist
- [ ] Bash/PowerShell installer and fixture arrays preserve the same exact ordered 19-file Runtime payload
- [ ] Two-pass disposable installation from the Active Project Root passes 19/19 order/mode/body parity, idempotence, unrelated-file preservation, and governed/plugin/support/template/playground exclusion
- [ ] Runtime payload parity and Active Project Root convergence are reported separately; mixed proof blocks completion
- [ ] Fresh public clone reproduction is required only after separately approved publication from the Active Project Root
- [ ] `implemented`, `tested`, `verified-in-scope`, `installed`, `released`, `fresh-clone-verified`, and `migration complete` wording never outruns the named evidence

## Integration

Primary runtime/governance owners:
- `document-governance.md`
- `document-integrity.md`
- `phase-todo-artifact.md`
- `coding-discipline.md`
- `action-safety.md`
- `evidence-discipline.md`
- `execution-and-goal-frame.md`
- `accurate-communication.md`
- `communication-register.md`
- `explanation-and-presentation.md`

Installer and fixture evidence surfaces:
- [Installer architecture](installer-architecture.design.md)
- [`script/setup-claude-code-rules.sh`](../../script/setup-claude-code-rules.sh)
- [`script/setup-claude-code-rules.ps1`](../../script/setup-claude-code-rules.ps1)
- [`script/test-setup-claude-code-rules.sh`](../../script/test-setup-claude-code-rules.sh)
- [`script/test-setup-claude-code-rules.ps1`](../../script/test-setup-claude-code-rules.ps1)

Execution/release entrypoints:
- [`README.md`](../../README.md)
- [`TODO.md`](../../TODO.md)
- [`phase/SUMMARY.md`](../../phase/SUMMARY.md)
- [`changelog/changelog.md`](../../changelog/changelog.md)
