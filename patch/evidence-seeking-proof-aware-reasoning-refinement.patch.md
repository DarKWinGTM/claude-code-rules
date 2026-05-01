# Evidence-Seeking Proof-Aware Reasoning Refinement Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/design.md](../design/design.md) v9.78
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

P079 responds to a reasoning-quality gap: an assistant can analyze, design, recommend, agree, or disagree from floating assumptions even when practical evidence is available.

พูดง่าย ๆ: AI ควรพยายามหา fact/proof/evidence ที่หาได้จริงมาใช้พยุงการคิด แต่ไม่ใช่เอา evidence ธรรมดาไปล็อกว่าต้องเลือกทางเดียวเสมอ.

This patch keeps evidence useful without making it falsely deterministic:
- `evidence-grounded-burden-of-proof.md` owns evidence-seeking / proof-aware reasoning thresholds.
- `external-verification-and-source-trust.md` owns current external fact checks, source trust, and external-evidence grounding.
- `accurate-communication.md` owns wording that separates checked evidence, assumptions, hard constraints, and open trade-offs.
- `explanation-quality.md` owns explanation flow for what evidence proves, suggests, and does not prove.
- `anti-sycophancy.md` owns evidence-seeking before factual alignment, recommendation, or challenge.
- `zero-hallucination.md` owns the guard that evidence-seeking must not become invented proof.

This is a non-code governance patch. It changes documentation/rule semantics and includes a later explicit runtime install/parity gate because the user requested `install Rules` for this wave.

---

## 2) Analysis

Risk level: Medium

Dependencies:
- P078 already made factual agreement evidence-calibrated.
- Existing burden-of-proof and zero-hallucination owners already separate fact, inference, hypothesis, uncertainty, and scoped non-findings.
- Existing external-verification owner already ranks source trust and corroboration for current external facts.
- Existing communication/explanation owners already shape evidence-strength wording and practical explanation flow.

Review concerns:
- Do not turn evidence-seeking into a hard requirement for every trivial answer.
- Do not block useful analysis waiting for perfect proof when evidence is unavailable or disproportionate to fetch.
- Do not treat ordinary evidence, examples, precedent, or tendency as a rigid final decision lock.
- Do not weaken hard constraints, authoritative requirements, safety boundaries, or verified contradictions.
- Do not let proof-aware reasoning invent evidence or make assumptions sound verified.
- Do not claim runtime install parity until the install/audit gate actually runs.

---

## 3) Change Items

### PAA-001 — Evidence-seeking burden thresholds

- **Target artifact:** `../evidence-grounded-burden-of-proof.md`
- **Target design:** `../design/evidence-grounded-burden-of-proof.design.md`
- **Change type:** additive / restructuring

**Before**
```text
The chain owned evidence taxonomy and burden thresholds, but did not explicitly require practical evidence-seeking before substantial analysis, design, recommendation, agreement, or disagreement when factual grounding would materially improve judgment.
```

**After**
```text
The chain owns proof-aware reasoning: identify material factual questions, seek available evidence when practical and proportional, classify what the evidence proves/suggests/leaves unresolved, and continue with labeled assumptions or hypotheses when evidence remains incomplete.
```

**Preserved behavior**
- Contradiction still requires contrary evidence.
- Scoped non-findings remain scoped.
- Memory and post-compact details still require current recheck before verified current-state wording.

### PAA-002 — Evidence as grounding, not automatic lock

- **Target artifact:** `../evidence-grounded-burden-of-proof.md`
- **Target design:** `../design/evidence-grounded-burden-of-proof.design.md`
- **Change type:** additive

**Before**
```text
Evidence strength governed factual endorsement, contradiction, and absence claims, but ordinary evidence versus binding constraints was not explicit enough for design/recommendation work.
```

**After**
```text
Evidence grounds judgment and trade-offs. It becomes binding only when it represents a hard constraint, authoritative requirement, safety boundary, or verified contradiction; otherwise alternatives and user-owned goals remain visible.
```

**Preserved behavior**
- True hard constraints remain binding inside their real scope.
- User authority remains decisive in non-hard-boundary space.
- Ordinary evidence improves judgment without erasing valid alternatives.

### PAA-003 — External evidence for design and recommendation grounding

- **Target artifact:** `../external-verification-and-source-trust.md`
- **Target design:** `../design/external-verification-and-source-trust.design.md`
- **Change type:** additive / restructuring

**Before**
```text
External verification covered current external factual claims, source ranking, corroboration, conflict handling, and recommendation integrity, but did not explicitly cover design judgment grounding.
```

**After**
```text
External verification now covers recommendation and design judgments that materially depend on current external facts, while distinguishing binding authoritative requirements from ordinary external evidence used as reasoning support.
```

**Preserved behavior**
- Primary official technical authorities remain highest trust for external facts.
- Source conflicts must still be reported honestly.
- Incomplete verification still falls back to bounded wording rather than false certainty.

### PAA-004 — Proof-aware communication and explanation wording

- **Target artifacts:** `../accurate-communication.md`, `../explanation-quality.md`
- **Target designs:** `../design/accurate-communication.design.md`, `../design/explanation-quality.design.md`
- **Change type:** additive

**Before**
```text
Communication and explanation owners handled evidence-strength wording, but did not provide enough direct shape for proof-aware recommendations and designs.
```

**After**
```text
Communication and explanation owners now show checked evidence, what it proves, what it suggests, what it does not prove, and whether the evidence is a hard constraint or ordinary grounding input.
```

**Preserved behavior**
- Wording still matches verification strength.
- Practical explanation still starts plainly and deepens only as needed.
- Recommendations remain bounded and evidence-calibrated.

### PAA-005 — Anti-sycophancy and zero-hallucination companion guardrails

- **Target artifacts:** `../anti-sycophancy.md`, `../zero-hallucination.md`
- **Target designs:** `../design/anti-sycophancy.design.md`, `../design/zero-hallucination.design.md`
- **Change type:** additive

**Before**
```text
P078 prevented unsupported factual endorsement and over-agreement, but evidence-seeking before substantial recommendation/design/alignment/challenge was not explicit enough.
```

**After**
```text
Anti-sycophancy now seeks practical evidence before substantial factual alignment or challenge, while zero-hallucination blocks proof-aware reasoning from becoming invented proof or false certainty.
```

**Preserved behavior**
- Acknowledgement remains separate from endorsement.
- User preference/direction remains accepted as direction.
- Verified contradiction still allows direct claim-focused correction.

### PAA-006 — Governed records, install gate, and release boundary

- **Target artifacts:** `../design/design.md`, `../changelog/changelog.md`, `../README.md`, `../TODO.md`, `../phase/SUMMARY.md`, `../phase/phase-079-01-evidence-seeking-proof-aware-reasoning-refinement.md`, this patch file
- **Change type:** companion sync

**Before**
```text
Master records described P078/v9.77 as the latest source state and did not describe evidence-seeking proof-aware reasoning as the current refinement.
```

**After**
```text
Master records describe P079/v9.78 as proof-aware reasoning: practical evidence should ground substantial analysis, design, recommendation, agreement, and disagreement, while only hard constraints, authoritative requirements, safety boundaries, and verified contradictions become binding locks.
```

**Preserved behavior**
- README remains current-state/onboarding guidance, not a changelog dump.
- TODO remains durable tracking.
- `phase/SUMMARY.md` remains the phase index.
- Runtime install copies only the 41 README-listed active runtime rules and does not classify other destination markdown files as junk.

---

## 4) Verification

- [x] Evidence-seeking is proportional, not mandatory for every trivial answer.
- [x] Missing or incomplete evidence uses assumptions, hypotheses, or bounded recommendations rather than fabricated proof.
- [x] Ordinary evidence is not treated as a rigid final decision lock.
- [x] Hard constraints, authoritative requirements, safety boundaries, and verified contradictions remain binding inside their real scope.
- [x] External evidence can ground recommendation/design judgments without replacing user goals.
- [x] Communication and explanation wording show what evidence proves and what it does not prove when that boundary matters.
- [x] Master records, README, TODO, phase, and patch records are synchronized for P079.
- [x] Runtime install parity is verified for the 41 active runtime rule files after the source audit gate.
- [x] Source/runtime release artifacts are ready for git push and release v9.78.

---

## 5) Rollback Approach

If P079 proves too broad:
- narrow the evidence-seeking trigger to substantial analysis/design/recommendation/disagreement only
- keep the ordinary-evidence-versus-binding-constraint distinction
- preserve evidence-calibrated agreement from P078
- preserve zero-hallucination protection against invented proof
- preserve source-trust ranking and conflict handling in the external-verification owner
- do not delete runtime destination files or other-owner runtime rules as part of rollback without a separate explicit destructive gate
