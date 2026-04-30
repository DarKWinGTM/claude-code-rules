# Phase 078-01 - Evidence-Calibrated Agreement Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 078-01
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/anti-sycophancy.design.md](../design/anti-sycophancy.design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/zero-hallucination.design.md](../design/zero-hallucination.design.md)
> **Patch References:** [../patch/evidence-calibrated-agreement-refinement.patch.md](../patch/evidence-calibrated-agreement-refinement.patch.md)

---

## Objective

Add evidence-calibrated agreement so the assistant can acknowledge user concerns and accept user-owned preference/direction without endorsing unverified factual claims.

พูดง่าย ๆ: รับ direction ของผู้ใช้ได้ แต่ถ้าเป็นเรื่อง fact ต้องมีหลักฐานก่อนจะบอกว่า “ถูกต้อง”.

---

## Why This Phase Exists

The prior owner set already resisted sycophancy and unsupported contradiction, but it did not make factual agreement explicit enough as its own evidence-sensitive path. That gap can let acknowledgement or helpfulness sound like verification.

P078 defines a bounded calibration model:
- acknowledgement is allowed without endorsement
- user-owned preference/direction can be accepted as direction
- factual endorsement requires evidence strong enough to state the claim as fact
- evidence-backed disagreement remains claim-focused and proportionate
- unsupported factual agreement is treated as a hallucination risk

---

## Entry Conditions

- P077 completed documentation surface governance is complete.
- The user requested analysis first, then selected a principle-based refinement rather than a blunt prohibition.
- The user explicitly requested implementation, README update, git commit, push, and release.
- Runtime install is not part of this phase unless separately requested.

---

## Implementation Plan

### 1) Active rule changes

- Update `anti-sycophancy.md` to own evidence-calibrated agreement/disagreement posture.
- Update `evidence-grounded-burden-of-proof.md` to add factual-endorsement burden thresholds and user-owned preference/direction handling.
- Update `accurate-communication.md` to add acknowledgement-without-endorsement, evidence-backed agreement, preference/direction acceptance, and claim-focused correction wording.
- Update `zero-hallucination.md` to treat unsupported factual endorsement as a hallucination risk.

### 2) Design and changelog sync

- Sync companion design files for the touched rule chains.
- Add per-chain changelog entries for:
  - `anti-sycophancy` v1.5
  - `evidence-grounded-burden-of-proof` v1.5
  - `accurate-communication` v2.19
  - `zero-hallucination` v1.5

### 3) Master record sync

- Update `design/design.md` to v9.77 and add evidence-calibrated agreement to the active repository model.
- Update `changelog/changelog.md` to v9.77.
- Update `README.md` current-state sections to describe the new calibration model without adding a changelog dump.
- Update `TODO.md` with durable tracking/history.
- Update `phase/SUMMARY.md` with phase 078 references.
- Create the P078 patch artifact and this P078 phase record.

### 4) Release path

- Verify cross-artifact consistency.
- Commit source changes.
- Push to `origin/master`.
- Create GitHub release `v9.77`.

---

## Out of Scope

- No runtime install to `~/.claude/rules/` in this phase unless a separate explicit runtime-install gate is opened.
- No change to the README-listed 41-file active runtime install set.
- No plugin/shared-board exact grammar changes.
- No deletion, cleanup, or classification of runtime destination files.
- No blanket “never agree” rule.

---

## Affected Artifacts

### Active runtime rule files

- `anti-sycophancy.md`
- `evidence-grounded-burden-of-proof.md`
- `accurate-communication.md`
- `zero-hallucination.md`

### Companion design files

- `design/anti-sycophancy.design.md`
- `design/evidence-grounded-burden-of-proof.design.md`
- `design/accurate-communication.design.md`
- `design/zero-hallucination.design.md`
- `design/design.md`

### Changelog and tracking files

- `changelog/anti-sycophancy.changelog.md`
- `changelog/evidence-grounded-burden-of-proof.changelog.md`
- `changelog/accurate-communication.changelog.md`
- `changelog/zero-hallucination.changelog.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/evidence-calibrated-agreement-refinement.patch.md`
- `phase/phase-078-01-evidence-calibrated-agreement-refinement.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P078 as durable completed governance work after source sync and audit pass.
- `changelog/changelog.md` records v9.77 as the master version authority for P078.
- Per-chain changelogs record the specific rule-owner version bumps.
- README presents the current-state model and usage guidance, not version-history prose.

---

## Verification

- [x] Owner chains align across runtime, design, and changelog versions.
- [x] Master `design/design.md`, `changelog/changelog.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` describe the same P078 scope.
- [x] Factual agreement requires checked evidence strong enough to state the claim as fact.
- [x] User preference/direction remains accepted as direction rather than factual proof.
- [x] Acknowledgement without endorsement is preserved as a safe communication pattern.
- [x] Evidence-backed disagreement remains claim-focused and proportionate.
- [x] Runtime install remains out of scope until separately requested.
- [x] Source release artifacts are ready for the requested git commit/push/release step after source audit.

---

## Closeout Summary

What this phase delivered:
- P078 adds evidence-calibrated agreement so the assistant can acknowledge concerns and accept user-owned direction without turning unverified factual claims into assistant-endorsed truth.

Feature / Improvement:
- Evidence-calibrated agreement/disagreement across anti-sycophancy, burden-of-proof, accurate communication, and zero-hallucination owners.

Impact:
- The assistant can be helpful without automatically agreeing, and can disagree when checked evidence conflicts while keeping correction calm and claim-focused.

Verification:
- Source records are synchronized for P078; runtime install remains out of scope, and git publish/release is the final external step after source commit.

Next phase state:
- None opened.

---

## Exit Criteria

- P078 owner-chain runtime, design, and changelog versions are synchronized.
- Master records describe v9.77 consistently.
- P078 phase and patch records exist and link correctly.
- Final source audit passes.
- Source release artifacts are ready for the requested git commit, push, and release step.

---

## Risks and Rollback Notes

Risk:
- Agreement calibration could be misread as a prohibition against agreeing.

Mitigation:
- Keep the principle explicit: agree when evidence supports the factual claim, accept preference/direction as user-owned direction, and acknowledge uncertainty when proof is incomplete.

Risk:
- Correction behavior could become adversarial.

Mitigation:
- Keep disagreement claim-focused and evidence-grounded; avoid person-directed verdicts unless genuinely necessary and strongly supported.

Rollback:
- Narrow only the P078 evidence-calibrated agreement wording if needed.
- Preserve the distinction between acknowledgement, user-owned direction, factual endorsement, and evidence-backed correction.
- Preserve existing zero-hallucination and burden-of-proof thresholds.

---

## Next Possible Phases

- None selected.
- A future runtime-install/parity wave may be opened only if explicitly requested.
