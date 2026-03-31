# External Verification and Source Trust Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented - Pending Review
> **Target Design:** [../design/external-verification-and-source-trust.design.md](../design/external-verification-and-source-trust.design.md) v1.0
> **Target Rule:** [../external-verification-and-source-trust.md](../external-verification-and-source-trust.md)
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/external-verification-and-source-trust.changelog.md](../changelog/external-verification-and-source-trust.changelog.md)

---

## 1) Context

This patch captures the introduction of a first-class rule chain for proactive external verification and source-trust analysis.

Why this change matters:
- the RULES system already has strong anti-hallucination and burden-of-proof foundations
- but source reliability, corroboration, and proactive WebSearch/WebFetch verification were still split implicitly across several adjacent rules
- a dedicated chain is needed so the system becomes more accurate, not just more cautious

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../zero-hallucination.md`
- `../evidence-grounded-burden-of-proof.md`
- `../accurate-communication.md`
- `../anti-sycophancy.md`
- `../operational-failure-handling.md`

Review concern:
- the new chain should add one clear owner for external verification and source trust without blurring adjacent rule ownership

---

## 3) Change Items

### Change Item 1
- **Target location:** RULES runtime inventory
- **Change type:** additive

**Before**
```text
External verification and source trust behavior was distributed implicitly across zero-hallucination, burden-of-proof, anti-sycophancy, accurate-communication, and operational-failure-handling.
```

**After**
```text
A dedicated first-class rule chain owns proactive external verification triggers, source-reliability ranking, corroboration, and source-conflict handling.
```

### Change Item 2
- **Target location:** factual verification model
- **Change type:** additive

**Before**
```text
Verify external facts with authoritative sources when possible, but no single chain defined when web verification is required versus preferred or how multiple sources should be compared.
```

**After**
```text
The new chain defines:
- when WebSearch/WebFetch-backed verification is required or preferred
- when one source is enough versus when corroboration is needed
- how to rank external sources by reliability
- how to handle source conflicts honestly
```

### Change Item 3
- **Target location:** adjacent-chain integration
- **Change type:** additive

**Before**
```text
Adjacent chains referenced source priority and burden-of-proof but did not defer a deeper external source-trust workflow to one owner.
```

**After**
```text
Adjacent chains keep their current authority while the new chain becomes the semantic owner of external verification and source-trust workflow.
```

---

## 4) Verification

- [ ] Confirm the design/runtime/changelog triad exists for the new chain
- [ ] Confirm the rule defines proactive verification triggers, source ranking, corroboration, and source-conflict handling
- [ ] Confirm adjacent chains retain their own authority boundaries
- [ ] Confirm the patch remains readable as a before/after governance artifact

---

## 5) Rollback Approach

If the chain proves redundant or over-scoped:
- narrow the chain to external source-trust workflow only
- preserve the triad and patch history rather than silently deleting the ownership experiment
- revert any adjacent-chain integration wording that overstates the new chain’s scope
