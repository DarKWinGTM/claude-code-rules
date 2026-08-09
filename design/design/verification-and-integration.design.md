# Verification and Integration - RULES System Design

> **Parent Design:** [../design.md](../design.md)
> **Current Version:** 10.60
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045 (2026-08-09)
> **Section:** Verification checklist and integration
> **Full history:** [../../changelog/changelog.md](../../changelog/changelog.md)
> **Status:** Active target-state shard

---

## Verification Checklist

### Runtime and governed authority

- [ ] README remains overview/onboarding/current-state only; detailed target truth, history, execution, and before/after review stay with their owning surfaces
- [ ] Runtime Rules remain body-sufficient active behavior contracts and the source-owned install inventory remains exactly the ordered 19 root files
- [ ] Governed design/changelog chains classify `single-file-bootstrap`, `flat-sibling-shards`, `same-stem-subfolder-normalized`, or `archive-history-reference-only` before meaningful normalization
- [ ] Exactly one active parent model remains per chain; inactive history, quarantine, and `done/` never become competing authority, generated input, or automatic fallback
- [ ] Parent/shard/version links, maps, and back-links resolve across the selected chain shape
- [ ] `TODO.md` and `phase/SUMMARY.md` remain bodyful active entrypoints with reachable history/done detail; touched size pressure is repaired or assigned a visible governed repair slice
- [ ] Phase identity stays lineage-first and forward-valid numeric forms remain `phase-NNN`, `phase-NNN-NN`, and `phase-NNN-NN-NN`
- [ ] Non-trivial analysis/design completes material outcome, constraint, dependency, failure, alternative, and verification gaps without fabricating facts or replacing user authority
- [ ] Implementation closeout covers or explicitly disposes material behavior, state, integration, failure, observability, and verification obligations
- [ ] Successor posture follows execution decision → goal construction → presentation rendering, with no consumer-side promotion and exact `/goal` then `Plan reference:` order
- [ ] Structural/visual changes resolve diagram posture after design; ordinary design edits may use `not required` without opening a subject diagram
- [ ] Duplicate/stale Agent Team presence blocks unchanged retry in action safety, then worker routing audits and decides lifecycle

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
- [ ] Candidate/canonical/root parity and body sufficiency pass 19/19 while unrelated runtime files remain byte-identical
- [ ] Fresh public clone reproduces the installer/scenario proof from the released commit
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
