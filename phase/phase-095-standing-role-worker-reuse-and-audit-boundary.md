# P095 — Standing-Role Worker Reuse and Audit Boundary

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P095
> **Status:** Active
> **Target Release:** v10.03
> **Design References:**
> - [../design/design.md](../design/design.md) v10.03
> - [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md) v1.7
> **Patch References:** [../patch/standing-role-worker-reuse-and-audit-boundary.patch.md](../patch/standing-role-worker-reuse-and-audit-boundary.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Promote the universal parts of `claude-session-coordination` clause 6 into Main RULES.

The target behavior is stable standing-role worker and teammate reuse across phases, with evidence-based audit before reuse, spawn, respawn, shutdown, or duplicate/overlap reporting.

---

## Why This Phase Exists

Phase changes can make duplicate-looking workers or teammates appear when the real responsibility did not change.

P095 makes the global behavior explicit:
- phase or task IDs are assignment context, not worker identity
- active or recent aligned standing-role workers are reused or steered before duplicate spawns
- new workers require a genuinely distinct role, audited unavailability, user-selected separation, or simultaneous distinct scope
- simultaneous same-role lanes are named by responsibility, surface, or output rather than phase ID alone
- lifecycle decisions use scoped coordination evidence instead of stale UI residue or unverified assumptions

---

## Expected Output

- `native-worker-agent-routing-and-context-control` defines global standing-role reuse and audit doctrine.
- Main RULES uses mechanism-neutral worker/teammate lifecycle wording.
- Plugin-only `claude-session-coordination` mechanics remain outside Main RULES ownership.
- README, master design, master changelog, TODO, phase, and patch records align to v10.03 / P095.
- Active runtime count remains 47.

---

## Action Checklist

- [x] Open P095 phase and patch records.
- [x] Update native-worker routing design/runtime/changelog to v1.7.
- [x] Sync master README, design, changelog, TODO, phase, and patch records.
- [x] Verify 47/47 README install-array scope and active runtime body sufficiency.
- [x] Verify semantic promotion and plugin-mechanic exclusion gates.
- [x] Install only README-listed active runtime rules.
- [x] Verify source/runtime parity and source/destination body sufficiency for 47/47 files.
- [x] Validate P095-specific density/God-artifact posture.
- [ ] Push `master` and publish GitHub release `v10.03`.
- [ ] Close P095 records after release verification passes.

---

## Out of Scope

- Adding a new active runtime rule file.
- Installing design, changelog, TODO, phase, patch, support, or helper artifacts as runtime rules.
- Importing shared-board title grammar, session-short-id prefixes, creator-owner hooks, hidden registries, package tmux bridge behavior, or exact `--teammate-mode tmux` behavior into Main RULES.
- Treating stale UI residue or unverified worker presence as proof of live duplicate overlap.
- Deleting history, done shards, destination runtime extras, or other-owner files.

---

## Completion Gate

- Source docs are synchronized for v10.03 / P095.
- Runtime install copied only README-listed active runtime rules for the current 47-file set.
- README Bash and PowerShell arrays still define exactly 47 matching active runtime files.
- Source/runtime parity and source/destination active runtime body sufficiency pass for 47/47 files.
- Standing-role reuse, phase-ID-as-context, lifecycle audit, scoped state evidence, responsibility-based lane naming, and worker-scale rules pass validation.
- Plugin-only mechanics remain excluded from Main RULES required behavior.
- Touched active docs pass density and God-artifact review.
- Broad validation uses worker-first filtering or records a narrow direct-handling exception.
- `master` push and GitHub release `v10.03` verification pass.

---

## Rollback / Containment

If P095 is reversed:
- revert the v10.03 standing-role reuse/audit changes as one governed rollback
- restore prior v10.02 owner-chain versions and master records
- reinstall the prior 47-file runtime set only under an explicit rollback gate
- do not delete history/done shards, phase/patch records, runtime destination extras, or other-owner files as cleanup

---

## Current Status

P095 is active.

Verified in source/runtime:
- phase and patch records are open
- native-worker owner-chain updates are complete
- master source sync is complete
- runtime install copied the 47 README-listed root rules
- source/runtime parity and source/destination body sufficiency passed for 47/47 files
- semantic promotion, plugin exclusion, and P095-specific density review passed
- broader master governance density rollover remains deferred in `TODO.md`

Pending gates:
- push and release verification
