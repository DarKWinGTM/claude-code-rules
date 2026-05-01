# Phase 079-01 - Evidence-Seeking Proof-Aware Reasoning Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 079-01
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/evidence-grounded-burden-of-proof.design.md](../design/evidence-grounded-burden-of-proof.design.md), [../design/external-verification-and-source-trust.design.md](../design/external-verification-and-source-trust.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/explanation-quality.design.md](../design/explanation-quality.design.md), [../design/anti-sycophancy.design.md](../design/anti-sycophancy.design.md), [../design/zero-hallucination.design.md](../design/zero-hallucination.design.md)
> **Patch References:** [../patch/evidence-seeking-proof-aware-reasoning-refinement.patch.md](../patch/evidence-seeking-proof-aware-reasoning-refinement.patch.md)

---

## Objective

Add evidence-seeking proof-aware reasoning so substantial analysis, design, recommendation, agreement, and disagreement use practical checked evidence when it materially improves judgment.

พูดง่าย ๆ: ให้ AI หาหลักฐานที่หาได้จริงมาช่วยคิด แต่ไม่ทำให้หลักฐานธรรมดากลายเป็นคำสั่งตายตัวว่าต้องเลือกทางเดียว.

---

## Why This Phase Exists

P078 already made factual agreement evidence-calibrated, but a broader reasoning gap remained: the assistant could still recommend, design, or challenge from plausible but unchecked assumptions even when bounded evidence would materially improve accuracy.

P079 defines a bounded proof-aware model:
- seek practical evidence for material factual premises
- classify what evidence proves, suggests, and leaves unresolved
- use evidence as grounding input for judgment and trade-offs
- bind only hard constraints, authoritative requirements, safety boundaries, and verified contradictions
- continue with labeled assumptions or hypotheses when evidence is unavailable or incomplete

---

## Entry Conditions

- P078 evidence-calibrated agreement refinement is complete and installed after its explicit runtime gate.
- The user requested a principle that encourages fact/proof/evidence during analysis/design/recommendation without making evidence a rigid final lock.
- The user explicitly requested implementation, docs sync, runtime install, git push, and release for this wave.

---

## Implementation Plan

### 1) Active rule changes

- Update `evidence-grounded-burden-of-proof.md` to own evidence-seeking / proof-aware reasoning and ordinary-evidence-versus-binding-constraint thresholds.
- Update `external-verification-and-source-trust.md` to cover external evidence grounding for design/recommendation/disagreement.
- Update `accurate-communication.md` to add proof-aware recommendation/design wording.
- Update `explanation-quality.md` to add proof-aware explanation flow.
- Update `anti-sycophancy.md` to seek evidence before substantial factual alignment or challenge.
- Update `zero-hallucination.md` to prevent proof-aware reasoning from becoming invented certainty.

### 2) Design and changelog sync

- Sync companion design files for the six touched rule chains.
- Add per-chain changelog entries for:
  - `evidence-grounded-burden-of-proof` v1.6
  - `external-verification-and-source-trust` v1.1
  - `accurate-communication` v2.20
  - `explanation-quality` v2.21
  - `anti-sycophancy` v1.6
  - `zero-hallucination` v1.6

### 3) Master record sync

- Update `design/design.md` to v9.78 and describe evidence-seeking proof-aware reasoning as the current active model.
- Update `changelog/changelog.md` to v9.78.
- Update `README.md` current-state sections without adding a changelog dump.
- Update `TODO.md` durable tracking/history.
- Update `phase/SUMMARY.md` with phase 079 references.
- Create the P079 patch artifact and this P079 phase record.

### 4) Runtime install, release, and verification path

- Run source consistency audit.
- Install only the README-listed 41 active runtime rule files into `~/.claude/rules/`.
- Verify source/runtime hash parity and keep destination markdown files outside the active install set observed-only.
- Commit source changes.
- Push to `origin/master`.
- Create GitHub release `v9.78`.

---

## Out of Scope

- No change to the README-listed 41-file active runtime install set.
- No plugin/shared-board exact grammar changes.
- No deletion, cleanup, or classification of runtime destination files.
- No rule that requires external research for every trivial answer.
- No hard decision lock from ordinary evidence, examples, or precedent.

---

## Affected Artifacts

### Active runtime rule files

- `evidence-grounded-burden-of-proof.md`
- `external-verification-and-source-trust.md`
- `accurate-communication.md`
- `explanation-quality.md`
- `anti-sycophancy.md`
- `zero-hallucination.md`

### Companion design files

- `design/evidence-grounded-burden-of-proof.design.md`
- `design/external-verification-and-source-trust.design.md`
- `design/accurate-communication.design.md`
- `design/explanation-quality.design.md`
- `design/anti-sycophancy.design.md`
- `design/zero-hallucination.design.md`
- `design/design.md`

### Changelog and tracking files

- `changelog/evidence-grounded-burden-of-proof.changelog.md`
- `changelog/external-verification-and-source-trust.changelog.md`
- `changelog/accurate-communication.changelog.md`
- `changelog/explanation-quality.changelog.md`
- `changelog/anti-sycophancy.changelog.md`
- `changelog/zero-hallucination.changelog.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/evidence-seeking-proof-aware-reasoning-refinement.patch.md`
- `phase/phase-079-01-evidence-seeking-proof-aware-reasoning-refinement.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P079 as durable governed work after source sync, runtime install, and release pass.
- `changelog/changelog.md` records v9.78 as the master version authority for P079.
- Per-chain changelogs record the specific rule-owner version bumps.
- README presents the current-state model and install status without dumping version history.

---

## Verification

- [x] Evidence-seeking is proportional and applies to material factual premises, not every trivial answer.
- [x] Ordinary evidence is grounding input, not a rigid final decision lock.
- [x] Hard constraints, authoritative requirements, safety boundaries, and verified contradictions remain binding inside their real scope.
- [x] Incomplete evidence stays labeled as assumption, hypothesis, bounded recommendation, or unresolved uncertainty.
- [x] Companion runtime, design, and per-chain changelog versions are synchronized.
- [x] Master `design/design.md`, `changelog/changelog.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` describe the same P079 scope.
- [x] Runtime install parity is verified for the 41 active runtime files.
- [x] Source/runtime release artifacts are ready for git publish and release.

---

## Closeout Summary

What this phase delivers:
- P079 adds evidence-seeking proof-aware reasoning so substantial recommendations, designs, agreements, and disagreements are grounded in practical checked evidence when that evidence materially improves judgment.

Feature / Improvement:
- Proof-aware reasoning across burden-of-proof, source-trust, communication, explanation, anti-sycophancy, and zero-hallucination owners.

Impact:
- The assistant can reason from stronger factual grounding without pretending evidence is perfect or forcing one path unless the proof is genuinely binding.

Verification:
- Source owner changes, companion chain changelogs, master records, and runtime install parity are synchronized and verified; git publish/release is the final external step after source commit.

Next phase state:
- No next phase selected.

---

## Exit Criteria

- P079 owner-chain runtime, design, and changelog versions are synchronized.
- Master records describe v9.78 consistently.
- P079 phase and patch records exist and link correctly.
- Final source audit passes.
- Runtime install parity passes for the 41 active runtime rule files.
- Source/runtime release artifacts are ready for git push and release `v9.78`.

---

## Risks and Rollback Notes

Risk:
- Evidence-seeking could be misread as requiring exhaustive proof before any useful answer.

Mitigation:
- Keep practical/proportional language and preserve bounded recommendations when evidence is incomplete.

Risk:
- Evidence could be overread as a rigid architecture mandate.

Mitigation:
- Preserve the rule that only hard constraints, authoritative requirements, safety boundaries, or verified contradictions become binding locks.

Rollback:
- Narrow only the proof-aware trigger wording if needed.
- Preserve evidence-calibrated agreement from P078.
- Preserve zero-hallucination guardrails against invented certainty.
- Preserve external source-trust ranking and conflict handling.

---

## Next Possible Phases

- None selected.
