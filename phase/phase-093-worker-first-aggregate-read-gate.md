# P093 — Worker-First Aggregate-Read Gate

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P093
> **Status:** Active
> **Target Release:** v10.01
> **Design References:**
> - [../design/design.md](../design/design.md) v10.01
> - [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md) v1.5
> - [../design/context-load-and-document-density-control.design.md](../design/context-load-and-document-density-control.design.md) v1.4
> - [../design/safe-file-reading.design.md](../design/safe-file-reading.design.md) v1.7
> - [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md) v1.18
> - [../design/document-consistency.design.md](../design/document-consistency.design.md) v1.13
> **Patch References:** [../patch/worker-first-aggregate-read-gate.patch.md](../patch/worker-first-aggregate-read-gate.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Make worker-first aggregate-read handling an enforceable RULES behavior instead of a soft preference.

When a task requires broad governance or codebase reading, the leader session should route the broad scan through a standalone worker lane first, then read only selected anchors for edits and verification.

---

## Why This Phase Exists

The current rule set already prefers worker routing for broad work, but leader sessions can still read many bounded files directly and overflow context.

P093 closes that gap by making broad governance/code scans pass through an aggregate-read gate:
- use a worker first for broad multi-surface evidence gathering
- return filtered findings and exact anchors instead of raw document dumps
- let the leader verify anchors before edits, sync, no-drift, or release claims
- require a narrow stated exception before direct leader absorption of broad raw content

---

## Expected Output

- Worker routing defines broad governance/code scans as worker-fit by default.
- Context-load control defines aggregate read-burst thresholds and release/no-drift consequences when the gate is skipped.
- Safe file reading routes broad multi-file scans through worker filtering while preserving direct narrow reads.
- Execution continuity prevents momentum from bypassing the worker-first gate.
- Document consistency requires worker-gate compliance for broad sync/no-drift/closeout/release-ready claims.
- README, master design, master changelog, TODO, phase, and patch records align to v10.01 / P093.
- Active runtime count remains 47.

---

## Action Checklist

- [x] Open P093 phase and patch records.
- [x] Update worker-routing, context-load, safe-file-reading, execution-continuity, and document-consistency runtime rules.
- [x] Sync companion design and changelog files for touched owner chains.
- [x] Sync master README, design, changelog, TODO, phase, and patch records.
- [x] Validate version alignment, install arrays, active runtime body sufficiency, density, and God-artifact posture.
- [x] Install only README-listed active runtime rules.
- [x] Verify 47/47 source/runtime parity and active runtime body sufficiency.
- [ ] Push `master` and publish GitHub release `v10.01`.
- [ ] Close P093 records after release verification passes.

---

## Out of Scope

- Adding a new active runtime rule file.
- Installing design, changelog, TODO, phase, patch, support, or helper artifacts as runtime rules.
- Rewriting all historical broad-read guidance outside touched owner chains.
- Treating worker findings as final proof without leader anchor verification.
- Deleting history, done shards, destination runtime extras, or other-owner files.

---

## Completion Gate

- Source docs are synchronized for v10.01 / P093.
- Runtime install copies only README-listed active runtime rules.
- README Bash and PowerShell arrays still define exactly 47 source-owned active runtime files.
- Source/runtime parity and body sufficiency pass for 47/47 files.
- Touched active docs pass density and God-artifact review.
- Broad validation uses worker-first filtering or records a narrow direct-handling exception.
- `master` is pushed and GitHub release `v10.01` is verified.

---

## Rollback / Containment

If P093 is reversed:
- revert the v10.01 worker-first gate changes as one governed rollback
- restore prior v10.00 owner-chain versions and master records
- reinstall the prior 47-file runtime set only under an explicit rollback gate
- do not delete history/done shards, phase/patch records, runtime destination extras, or other-owner files as cleanup

---

## Current Status

P093 is active. Source sync, install, parity/body sufficiency, and density/God-artifact review passed. Push and GitHub release verification remain pending.
