# Phase 075-01 - Phase Closeout Feature Impact Reporting

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 075-01
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/response-closing-and-action-framing.design.md](../design/response-closing-and-action-framing.design.md), [../design/phase-implementation.design.md](../design/phase-implementation.design.md), [../design/answer-presentation.design.md](../design/answer-presentation.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md)
> **Patch References:** [../patch/phase-closeout-feature-impact-reporting.patch.md](../patch/phase-closeout-feature-impact-reporting.patch.md)

---

## Objective

Improve phase-backed completion reporting so closeouts explain what the phase developed or improved, what feature/capability changed, and what user/system impact it has before or alongside checked-scope and audit status.

พูดง่าย ๆ: เวลาปิด phase ต้องเห็น “งานนี้ทำอะไรให้ระบบดีขึ้น” ไม่ใช่เห็นแค่รายชื่อไฟล์ที่ตรวจแล้ว.

---

## Why This Phase Exists

The current RULES already ask for concise phase/progress explanation, but closeout reporting can still collapse into audit-style output: checked files, versions, task IDs, and drift status. That is technically useful but does not answer the product/system question: what did this phase deliver and why does it matter?

---

## Entry Conditions

- User explicitly requested RULES improvement for phase closeout reporting.
- P074-02 completed runtime install/parity and preserved the 41-file active runtime boundary.
- This phase is a narrow runtime rule improvement, not a broad documentation rewrite.
- Development docs/design/changelog/TODO/phase/patch changes are companion sync only.

---

## Runtime Active Rule Changes

- [x] Update `response-closing-and-action-framing.md` as the primary closeout/action-framing owner.
- [x] Update `phase-implementation.md` so phase closeout has feature/improvement/impact/verification/next-phase-state expectations.
- [x] Update `answer-presentation.md` with a compact phase closeout output pattern.
- [x] Update `accurate-communication.md` so feature/impact closeout wording remains evidence-honest.
- [x] Update `explanation-quality.md` so phase closeout explanation starts with practical delivered meaning before governance detail.

---

## Development Docs / Governed Record Sync Only

- [x] Sync paired design files for the five touched runtime owners.
- [x] Sync paired changelog files for the five touched runtime owners.
- [x] Sync `design/design.md` and `changelog/changelog.md`.
- [x] Sync `README.md`, `TODO.md`, and `phase/SUMMARY.md`.
- [x] Mark this phase and patch completed after verification.
- [x] Install only the 41 README-listed active runtime rule files.
- [x] Verify source/runtime parity and confirm other-owner runtime files remain untouched.

---

## Out of Scope

- Changing the 41-file active runtime install list.
- Treating README/TODO/phase/patch/design/changelog as runtime rule targets.
- Rewriting all communication rules broadly.
- Forcing long closeout templates for trivial, non-phase, or low-value completion messages.
- Claiming a feature is fixed/stable when only edit or partial verification evidence exists.
- Managing, classifying as junk, deleting, or editing plugin/project-owned runtime files in the shared destination.
- Git push or release.

---

## Affected Artifacts

Runtime active rule changes:
- `response-closing-and-action-framing.md`
- `phase-implementation.md`
- `answer-presentation.md`
- `accurate-communication.md`
- `explanation-quality.md`

Development docs / governed record sync only:
- `design/response-closing-and-action-framing.design.md`
- `design/phase-implementation.design.md`
- `design/answer-presentation.design.md`
- `design/accurate-communication.design.md`
- `design/explanation-quality.design.md`
- `changelog/response-closing-and-action-framing.changelog.md`
- `changelog/phase-implementation.changelog.md`
- `changelog/answer-presentation.changelog.md`
- `changelog/accurate-communication.changelog.md`
- `changelog/explanation-quality.changelog.md`
- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/phase-closeout-feature-impact-reporting.patch.md`

Runtime destination:
- active runtime copies only for the README-installed 41-file set

---

## Verification

- [x] The five runtime owners contain phase-backed closeout guidance.
- [x] Closeout pattern includes delivered work, feature/improvement, impact, verification, and next phase state when relevant.
- [x] Guidance remains concise and does not force templates onto simple completions.
- [x] Claim-strength wording still distinguishes edited, tested, working, stable/fixed, and not-started states.
- [x] Companion docs are labeled and used as sync/governed records only.
- [x] README active runtime rule count remains 41.
- [x] Runtime install copies only active runtime rules.
- [x] Source/runtime parity passes for the 41 active runtime files.
- [x] Other-owner runtime files in the destination remain untouched.

---

## Exit Criteria

- P075 runtime owner updates are complete.
- Companion governed records are synchronized.
- Patch and phase records are marked completed with verification.
- Runtime install/parity passes for active runtime rules only.
- No plugin/project-owned runtime destination file is managed or deleted.

---

## Risks and Rollback Notes

Risk: closeout guidance could become a rigid report template and add noise to simple responses.

Rollback posture: narrow or revert only P075 closeout-reporting wording and companion records while preserving existing phase/progress explanation guidance and active runtime install boundaries.

---

## Next Possible Phases

None opened by this phase. Any later broader closeout/reporting redesign requires a separate user-selected scope.
