# Language-Aware Candidate Goal and Goal-Command Doctrine Patch

> **Current Version:** 1.0
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Status:** In progress
> **Target Design:** [design/design.md](../design/design.md) v10.22
> **Full history:** [changelog/changelog.md](../changelog/changelog.md)

---

## Context

This is the governed patch record for `v10.22 / P114`.

It packages a refinement so goal-oriented successor recommendations follow the dominant session language by default, appear as candidate goals before plain next-step choice lists, and promote only the best-supported governed repo candidate into advisory `/goal` command form.

---

## Analysis

The released `v10.21 / P113` baseline already hardened governed-work-only `/goal` sourcing, but it still leaves one language gap and one successor-shape gap.

The language gap is that `/goal` can still drift into English-shaped wording by habit even when the user's active working language is Thai-first.

The successor-shape gap is that several live next directions can still appear as plain options instead of compact candidate goals, which weakens the connection between outcome, output, and gate before command promotion is even considered.

P114 corrects both gaps while preserving the governed-work-only boundary from P113.

---

## Change Items

### 1) Dominant-session-language ownership

- **Target artifact:** `communication-register.md`, `accurate-communication.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** easy-language guidance exists, but `/goal` and candidate-goal wording are not yet explicitly bound to the dominant session language.
- **Target state:** candidate goals and promoted `/goal` suggestions follow the dominant session language by default unless the user explicitly selects another language.
- **Review point:** do not let isolated borrowed English terms silently override a Thai-first session.

### 2) Candidate-goal-first successor recommendations

- **Target artifact:** `execution-and-goal-frame.md`, `explanation-and-presentation.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** successor work can be recommended as next goals, but several live directions are not yet explicitly shaped as candidate goals before command promotion.
- **Target state:** when several meaningful successor directions remain live, they appear first as candidate goals rather than as a plain unlabeled choice list.
- **Review point:** keep candidate goals compact, outcome-shaped, and distinct from promoted `/goal` commands.

### 3) Selective promotion into governed `/goal`

- **Target artifact:** `execution-and-goal-frame.md`, `phase-todo-artifact.md`, related design/changelog companions
- **Change type:** corrective refinement
- **Current state:** governed `/goal` sourcing already exists, but the bridge does not yet explicitly say that only the best-supported governed candidate should be promoted when several goal options remain live.
- **Target state:** RULES shapes several directions as candidate goals first, then promotes only the best-supported governed repo candidate into advisory `/goal` form.
- **Review point:** preserve design-first sourcing and material-only changelog/patch/README inclusion from P113.

### 4) Master-surface and example sync

- **Target artifact:** README/design/changelog/TODO/phase/patch release surfaces
- **Change type:** release synchronization
- **Current state:** master surfaces still identify `v10.21 / P113` as the current released baseline.
- **Target state:** master surfaces open and later close P114 consistently while preserving two Thai-first governed examples for audit.
- **Review point:** keep runtime install scope at 18 and stay inside repo scope only.

---

## Example Outputs

### Example 1 — Thai-first governed non-release candidate goal and promoted `/goal`

```text
Candidate goals:
- Goal A: ปรับ doctrine ของ `/goal` ให้ยึดภาษาหลักของ session และเพิ่ม candidate-goal layer ก่อน command promotion
- Goal B: ปิดงานแค่ wording owner ก่อน แล้วค่อยคุม execution owner ใน wave ถัดไป

Suggested /goal:
/goal เสร็จเมื่อ RULES owner files ที่ map ไว้รองรับ dominant session language และ candidate-goal-first successor recommendations ครบตาม doctrine ใหม่. พิสูจน์ด้วย: แสดง diff ของ owner runtime/design/changelog ที่แตะ และรัน `git diff --check` ผ่าน. ขอบเขต: `/home/node/workplace/AWCLOUD/TEMPLATE/RULES` เท่านั้น. ข้อคงไว้: อย่าโปรโมตทุก candidate goal เป็น `/goal`, อย่าทำ `/goal` ให้ยาวเป็น template dump, และคง governed-work-only boundary เดิมไว้.
```

### Example 2 — Thai-first governed release-closeout candidate goal and promoted `/goal`

```text
Candidate goals:
- Goal A: ปล่อย `v10.22 / P114` ให้ครบ install / parity / push / release / closeout
- Goal B: หยุดที่ source sync แล้วเลื่อนไป release ในรอบถัดไป

Suggested /goal:
/goal เสร็จเมื่อ `v10.22 / P114` ถูกติดตั้ง, ตรวจ parity, push, release, และปิด closeout ครบทุก governed surface. พิสูจน์ด้วย: install active rules เข้า `~/.claude/rules`, verify 18/18 source/runtime parity และ source/destination body sufficiency, รัน `git diff --check` ผ่าน, แสดง push result, verify release URL/tag target, และ sync README/design/changelog/TODO/phase/patch ให้ตรงกัน. ขอบเขต: RULES repo และ active runtime install target ของมันเท่านั้น. ข้อคงไว้: ใช้ design-first sourcing, ใส่ changelog/patch/README เฉพาะเมื่อ material จริง, และคง `/goal` เป็น advisory ไม่ใช่ selected execution.
```

---

## Verification

Required checks before release closeout:
- active doctrine explicitly defines dominant-session-language ownership for candidate goals and promoted `/goal`
- active doctrine explicitly defines candidate-goal shaping for several live successor directions
- active doctrine explicitly defines selective promotion from candidate goal to governed `/goal`
- at least two Thai-first governed examples remain available for audit and review
- all 18 active source runtime files still exist and keep substantive bodies
- runtime install copies only the README-listed active root runtime rules
- source/runtime parity and source/destination body sufficiency pass for 18/18 files
- `git diff --check` passes
- GitHub release `v10.22` is created and verified before closeout wording claims release completion

---

## Implementation Status

P114 is in progress.

The language-aware candidate-goal runtime update is underway; master-surface sync, runtime install/parity, commit/push, GitHub release verification, and final closeout alignment remain pending.
