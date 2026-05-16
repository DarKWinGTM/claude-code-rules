# P098 — Conversation Intent, Root-Cause, and Scope-Drift Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P098
> **Status:** Active / Release Preparation
> **Target Release:** v10.06
> **Design References:**
> - [../design/design.md](../design/design.md) v10.06
> - touched merged-owner design companions under [../design/](../design/)
> **Patch References:** [../patch/conversation-intent-root-cause-and-scope-drift-refinement.patch.md](../patch/conversation-intent-root-cause-and-scope-drift-refinement.patch.md)
> **Session:** 808f88f7-3682-45ad-8f3e-3caf233d3835
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Improve Main RULES so the assistant reads user intent more clearly before deep analysis or execution, clarifies only when ambiguity materially changes the outcome, and frames diagnosis toward root cause rather than symptom dumping.

---

## Why This Phase Exists

Current merged RULES already classify intent internally, but they do not yet make the assistant expose a concise working interpretation when that prevents drift.

P098 adds visible intent read, selective clarification, root-cause framing, and repair re-anchor doctrine across existing merged owner rules so conversation quality improves without expanding the active runtime install set beyond 18 rules.

---

## Expected Output

- Existing merged owner rules teach visible intent read, selective clarification, root-cause framing, and repair re-anchor behavior.
- Intent taxonomy, trigger additions, anti-patterns, response examples, and success metrics are added in the correct owners.
- The compact active runtime install set remains 18 root runtime rules.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.06` is created and verified.

---

## Action Checklist

- [x] Confirm `v10.06` release/tag is not already present.
- [x] Confirm current baseline is released `v10.05 / P097` with the compact 18-rule runtime set.
- [x] Open P098 phase/patch and sync active roadmap/TODO state.
- [ ] Update touched merged runtime owners with intent-grounding doctrine.
- [ ] Sync touched owner design and changelog companions.
- [ ] Sync README, master design, master changelog, TODO, phase summary, phase, and patch records to P098 pre-release state.
- [ ] Validate README install arrays, metadata links, source body sufficiency, runtime install, and source/runtime parity.
- [ ] Commit source release, push `master`, create GitHub release `v10.06`, and verify release state.
- [ ] Finalize P098 closeout records after release verification passes.

---

## Out of Scope

- Adding a new root runtime rule file.
- Increasing the active runtime install set above 18 rules.
- Reclassifying or deleting the runtime destination extra `shared-task-list-path-coordination.md`.
- Turning ordinary conversational intent-read into destructive-action confirmation behavior.
- Claiming GitHub release verification before push and release checks pass.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- Touched owner/runtime/design/changelog files align to `v10.06 / P098`.
- Visible intent read, selective clarification, root-cause framing, repair re-anchor, intent taxonomy, trigger additions, anti-patterns, examples, and success metrics are present in role-correct owners.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `master` push and GitHub release `v10.06` verification pass.

---

## Current Status

P098 is active in release preparation.

Completed so far:
- preflight confirmed `v10.06` release and tag were not found
- current baseline is released `v10.05 / P097`
- current active runtime install set remains 18 rules
- P098 phase and patch startup artifacts are opened
- active TODO and phase roadmap state are synchronized to P098 pre-release mode

Pending:
- doctrine implementation, owner-chain sync, validation, runtime install, commit, push, GitHub release, and closeout verification
