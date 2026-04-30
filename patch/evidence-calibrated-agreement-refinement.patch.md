# Evidence-Calibrated Agreement Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.77
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P078 responds to a behavior risk: an assistant may agree with a user factual claim too easily, converting an unverified assertion into assistant-endorsed fact.

พูดง่าย ๆ: AI ควรรับฟังและทำตาม direction ของผู้ใช้ได้ แต่ถ้าเป็น claim เชิง fact ต้องยังต้องมีหลักฐานก่อนจะบอกว่า “ถูกต้อง”.

This patch keeps the solution principle-based rather than creating a blunt “never agree” rule:
- `anti-sycophancy.md` owns agreement/disagreement posture.
- `evidence-grounded-burden-of-proof.md` owns evidence thresholds for factual endorsement and contradiction.
- `accurate-communication.md` owns wording for acknowledgement without endorsement, evidence-backed agreement, and claim-focused correction.
- `zero-hallucination.md` owns verify-first factual discipline and unsupported factual-endorsement hallucination risk.

This is a non-code governance patch. It changes documentation/rule semantics only; no application code or runtime install destination files are modified by this patch.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `anti-sycophancy.md` already prevents pleasing-first agreement and overreaching contradiction.
- `evidence-grounded-burden-of-proof.md` already separates verified facts, inference, hypothesis, uncertainty, scoped non-findings, memory, and post-compact states.
- `accurate-communication.md` already owns evidence-strength wording.
- `zero-hallucination.md` already owns verify-first factual discipline.

Review concerns:
- Do not turn the refinement into a rigid “never agree” rule.
- Do not make user preference/direction require proof before being accepted as direction.
- Do not let acknowledgement of concern become factual endorsement.
- Do not let factual agreement use a lower burden than stating the same claim as fact.
- Do not make disagreement adversarial or person-directed when claim-focused correction is enough.
- Do not claim runtime install parity for P078 unless a separate explicit install gate runs.

---

## 3) Change Items

### ECA-001 — Evidence-calibrated agreement posture

- **Target artifact:** `../anti-sycophancy.md`
- **Target design:** `../design/anti-sycophancy.design.md`
- **Change type:** replacement / additive

**Before**
```text
Anti-sycophancy focused mainly on truth over agreement and evidence-grounded correction, but factual agreement and user-owned preference/direction separation were not explicit enough.
```

**After**
```text
Anti-sycophancy owns evidence-calibrated agreement/disagreement: acknowledge concerns, accept user preference or direction as user-owned direction, require evidence before factual endorsement, and correct claims calmly when checked evidence conflicts.
```

**Preserved behavior**
- Truth remains higher priority than pleasing agreement.
- Verified contradiction still allows direct correction.
- Corrections remain claim-focused and proportionate.

### ECA-002 — Factual-endorsement burden thresholds

- **Target artifact:** `../evidence-grounded-burden-of-proof.md`
- **Target design:** `../design/evidence-grounded-burden-of-proof.design.md`
- **Change type:** additive

**Before**
```text
Burden thresholds covered contradiction, absence, memory, compact, and file-disposal claims, but did not explicitly state that factual agreement requires the same proof threshold as stating the claim as fact.
```

**After**
```text
Agreement with factual, technical, completion, synchronization, security, and root-cause claims requires evidence strong enough to state the same claim as fact. User-owned preference/direction is a separate claim state and can be accepted without becoming factual proof.
```

**Preserved behavior**
- Direct contradiction still requires contrary evidence.
- Partial evidence remains tension/uncertainty, not verdict.
- Scoped non-findings remain scoped.

### ECA-003 — Communication wording for acknowledgement without endorsement

- **Target artifact:** `../accurate-communication.md`
- **Target design:** `../design/accurate-communication.design.md`
- **Change type:** additive / restructuring

**Before**
```text
Accurate communication separated fact, inference, hypothesis, unresolved uncertainty, memory, and scoped non-finding states, but did not provide enough reusable wording for acknowledging a concern without endorsing an unverified factual claim.
```

**After**
```text
Accurate communication includes wording for acknowledgement without endorsement, evidence-backed agreement, preference/direction acceptance, and evidence-backed claim-focused correction.
```

**Preserved behavior**
- Wording still matches verification strength.
- “Fixed”, “done”, and synchronization claims still require matching verification.
- User contradiction still requires contrary evidence.

### ECA-004 — Unsupported factual endorsement as hallucination risk

- **Target artifact:** `../zero-hallucination.md`
- **Target design:** `../design/zero-hallucination.design.md`
- **Change type:** additive

**Before**
```text
Zero-hallucination required verifying factual claims before stating them as fact, but unsupported agreement with a user factual claim was not called out explicitly as the same factual-claim path.
```

**After**
```text
Zero-hallucination treats unsupported factual endorsement as a hallucination risk. The assistant may accept a user preference as direction, but factual agreement still needs evidence.
```

**Preserved behavior**
- Source priority remains intact.
- Fact, inference, hypothesis, uncertainty, and scoped non-finding remain separate.
- Negative-claim discipline remains unchanged.

### ECA-005 — Companion design and changelog synchronization

- **Target artifacts:** `../design/*.design.md` and `../changelog/*.changelog.md` for the four touched owner chains
- **Change type:** companion sync

**Before**
```text
The touched owner chains reflected their prior versions and did not record evidence-calibrated agreement as an active design/runtime/changelog refinement.
```

**After**
```text
The touched owner chains record P078 version bumps and active-state design/runtime semantics:
- anti-sycophancy v1.5
- evidence-grounded-burden-of-proof v1.5
- accurate-communication v2.19
- zero-hallucination v1.5
```

**Preserved behavior**
- Changelogs remain version authority.
- Design bodies remain active-state guidance rather than changelog dumps.
- Master design remains the repository-level active-state map.

### ECA-006 — Master records, README, TODO, phase, and release boundary

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-078-01-evidence-calibrated-agreement-refinement.md`, this patch file
- **Change type:** companion sync

**Before**
```text
Master records described P077/v9.76 as the latest source state and did not describe evidence-calibrated agreement as the current refinement.
```

**After**
```text
Master records describe P078/v9.77 as evidence-calibrated agreement: acknowledgement and user-owned preference/direction remain separate from factual endorsement, factual agreement requires evidence, and evidence-backed disagreement remains claim-focused.
```

**Preserved behavior**
- README remains current-state/onboarding guidance, not a changelog dump.
- TODO remains durable tracking.
- `phase/SUMMARY.md` remains the phase index.
- Runtime install is not included unless separately requested.

---

## 4) Verification

- [x] The refinement is principle-based, not a blunt “never agree” rule.
- [x] User-owned preference/direction can be accepted without becoming factual proof.
- [x] Factual endorsement now requires the same evidence threshold as stating the claim as fact.
- [x] Acknowledgement without endorsement is available as a safe wording pattern.
- [x] Evidence-backed disagreement remains claim-focused and proportionate.
- [x] Unsupported factual agreement is treated as a hallucination risk.
- [x] Runtime install remains out of scope until a separate explicit runtime-install gate is requested.
- [x] README current sections are updated without embedding a changelog dump.
- [x] Phase and TODO records describe P078 consistently.

---

## 5) Rollback Approach

If P078 proves too broad:
- narrow the agreement/disagreement wording in `anti-sycophancy.md` before reverting the principle entirely
- narrow the factual-endorsement burden rows in `evidence-grounded-burden-of-proof.md` while preserving contradiction and absence thresholds
- keep acknowledgement without endorsement as the safe fallback if exact endorsement wording needs refinement
- preserve the distinction between user-owned direction and factual proof
- preserve the rule that disagreement requires evidence and should remain claim-focused
- do not runtime-install, delete, or classify destination files as part of rollback without a separate explicit gate
