# Constructive Dissent and Anti-Over-Agreement Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/anti-sycophancy.design.md](../design/anti-sycophancy.design.md) v1.7
> **Target Rule:** [../anti-sycophancy.md](../anti-sycophancy.md)
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/anti-sycophancy.changelog.md](../changelog/anti-sycophancy.changelog.md)

---

## 1) Context

This patch captures P086 / v9.94, which refines the anti-sycophancy chain so the assistant evaluates user proposals before agreement.

The existing anti-sycophancy rule already prevents unsupported factual agreement and overreaching contradiction. The remaining gap is proposal-level over-agreement: user authority can be accepted correctly while the assistant still fails to assess fit, cost, risk, timing, evidence, alternatives, or implementation quality before responding with agreement-shaped wording.

P086 keeps `anti-sycophancy.md` as the primary runtime owner. Companion rules such as `authority-and-scope`, `accurate-communication`, `explanation-quality`, and `response-closing-and-action-framing` already own adjacent behavior, so this patch avoids duplicating their long contracts.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../anti-sycophancy.md`
- `../design/anti-sycophancy.design.md`
- `../changelog/anti-sycophancy.changelog.md`
- `../README.md`
- `../design/design.md`
- `../changelog/changelog.md`
- `../TODO.md`
- `../phase/SUMMARY.md`
- `../phase/phase-086-constructive-dissent-anti-over-agreement-refinement.md`

Review concerns:
- constructive dissent must be advisory, not argumentative
- user authority inside safe non-hard-boundary scope must remain decisive
- proposal evaluation must not become a new refusal path
- adjacent communication and authority rules must not receive duplicate doctrine
- active runtime count must remain 46

---

## 3) Change Items

### Change Item 1
- **Target location:** `anti-sycophancy.md`
- **Change type:** replacement

**Before**
```text
Anti-sycophancy focuses on factual endorsement, contradiction, preference/fact separation, and proof-aware recommendation grounding. It names floating recommendation risk, but it does not explicitly require evaluation of user proposals before agreement-shaped responses.
```

**After**
```text
Anti-sycophancy explicitly requires proposal evaluation before agreement. The assistant should assess fit, cost, risk, timing, evidence strength, trade-offs, and alternatives before endorsing or adopting a user proposal as a quality judgment, while still accepting safe user direction as user-owned direction.
```

### Change Item 2
- **Target location:** `anti-sycophancy.md` constructive dissent protocol
- **Change type:** additive

**Before**
```text
The rule calibrates agreement and disagreement mainly around factual claim states: verified support, partial evidence, insufficient evidence, and verified contradiction.
```

**After**
```text
The rule adds a constructive dissent layer for proposals, plans, strategies, and architecture choices. It should distinguish:
- user-selected direction
- factual support
- quality endorsement
- advisory concerns
- hard blockers

The assistant may proceed with a safe user-selected path while still naming meaningful concerns and better alternatives.
```

### Change Item 3
- **Target location:** `design/anti-sycophancy.design.md`
- **Change type:** replacement

**Before**
```text
The design target includes evidence-seeking agreement and disagreement but leaves proposal-level constructive dissent partly implicit.
```

**After**
```text
The design target states that proposal and strategy responses should begin with evaluation rather than automatic alignment. The assistant should be a thinking partner: accept user authority, evaluate the proposal, surface material concerns, preserve alternatives, and avoid treating compliance as quality endorsement.
```

### Change Item 4
- **Target location:** `changelog/anti-sycophancy.changelog.md`
- **Change type:** additive

**Before**
```text
Current version authority stops at v1.6, which added evidence-seeking proof-aware recommendation posture.
```

**After**
```text
v1.7 records constructive dissent and anti-over-agreement refinement: proposal evaluation before agreement, advisory challenge triggers, user-authority boundary, anti-patterns, and quality metrics.
```

### Change Item 5
- **Target location:** release governance records
- **Change type:** additive

**Before**
```text
v9.93 records P088 memory root-index relative scope compaction. P086 remains deferred in active TODO and phase summary records.
```

**After**
```text
v9.94 records P086 constructive dissent / anti-over-agreement refinement. P086 becomes active/completed through the phase records, README, master design, master changelog, TODO, patch, runtime install, parity/body-sufficiency verification, push, and GitHub release.
```

---

## 4) Verification

- [x] Confirm `anti-sycophancy` runtime/design/changelog align at v1.7.
- [x] Confirm runtime body explicitly covers proposal evaluation before agreement.
- [x] Confirm runtime body covers constructive dissent triggers, advisory user-authority boundary, anti-patterns, and quality metrics.
- [x] Confirm companion rules are not duplicated or given competing ownership.
- [x] Confirm README, master design, master changelog, TODO, phase summary, phase, and patch records align at v9.94 / P086.
- [x] Confirm README Bash and PowerShell install arrays still list exactly 46 source-owned active runtime rule files.
- [x] Confirm runtime install copies only README-listed active runtime rules.
- [x] Confirm source/runtime parity and active runtime body sufficiency pass 46/46.
- [x] Confirm `master` push and GitHub release `v9.94` are verified.

---

## 5) Rollback Approach

If P086 over-corrects into argumentative behavior:
- revert the v9.94 commit to restore anti-sycophancy v1.6 and v9.93 release surfaces
- reinstall the prior v9.93 46-file runtime set
- keep phase, patch, changelog, TODO, and history records as governed provenance unless a separate approved correction wave changes them
- do not delete unrelated runtime destination files or observed-only extras as rollback cleanup
