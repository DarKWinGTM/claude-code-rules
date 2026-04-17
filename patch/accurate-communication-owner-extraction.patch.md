# Accurate Communication Owner Extraction Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Completed
> **Target Design:** [../design/accurate-communication.design.md](../design/accurate-communication.design.md) v2.17
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the bounded refinement wave that extracts two first-class specialized communication owners out of `accurate-communication.md`:
- `technical-snapshot-communication.md`
- `response-closing-and-action-framing.md`

Why this change matters:
- `accurate-communication` had grown to own both broad communication honesty and narrower specialist communication subdomains
- technical snapshot wording had enough semantic detail to become a first-class rule chain
- response-closing / action / proposal framing had enough semantic detail to become a first-class rule chain
- the owner split should reduce duplicate active authority while preserving behavior

---

## 2) Analysis

Risk level: Medium

Dependencies:
- `../accurate-communication.md`
- `../technical-snapshot-communication.md`
- `../response-closing-and-action-framing.md`
- `../answer-presentation.md`
- `../explanation-quality.md`
- `../design/design.md`
- `../README.md`
- `../TODO.md`
- `../phase/SUMMARY.md`

Review concern:
- extraction must preserve meaning without turning the new chains into duplicate active authority
- closing/action framing must not absorb execution-mode ownership that already belongs elsewhere
- technical snapshot wording must not absorb layout or explanation-flow ownership that already belongs elsewhere

---

## 3) Change Items

### Change Item 1
- **Target location:** new first-class snapshot owner
- **Change type:** additive

**Before**
```text
Bounded technical snapshot wording lived inside accurate-communication as one specialized subdomain of a broader communication owner.
```

**After**
```text
A first-class `technical-snapshot-communication` chain now owns compact technical snapshot wording, exact/partial/inferred separation, and scoped local-fact snapshot communication.
```

### Change Item 2
- **Target location:** new first-class closing/action owner
- **Change type:** additive

**Before**
```text
Concise synthesis, recommendation-with-reason wording, closed-topic summary handling, and advisory proposal framing lived inside accurate-communication as one specialized subdomain of a broader communication owner.
```

**After**
```text
A first-class `response-closing-and-action-framing` chain now owns end-of-response synthesis, action framing, alternative preservation, and goal-qualified advisory proposal wording.
```

### Change Item 3
- **Target location:** `accurate-communication.md`
- **Change type:** replacement

**Before**
```text
Accurate-communication actively owned both broad communication honesty and the extracted specialized snapshot/closing domains.
```

**After**
```text
Accurate-communication keeps the broader communication-honesty owner role and explicitly defers the extracted specialist domains to the two new chains.
```

### Change Item 4
- **Target location:** adjacent owners and master surfaces
- **Change type:** replacement

**Before**
```text
Adjacent integrations still pointed snapshot/closing semantics at accurate-communication, and master surfaces did not yet include the two new chains.
```

**After**
```text
Adjacent integrations point to the new specialist owners where appropriate, while design/README/changelog/TODO/phase surfaces record the new chains coherently.
```

---

## 4) Verification

- [x] `technical-snapshot-communication` exists as a new governed design/runtime/changelog triad
- [x] `response-closing-and-action-framing` exists as a new governed design/runtime/changelog triad
- [x] `accurate-communication` now defers the extracted specialist domains instead of owning them directly
- [x] touched adjacent integrations are retargeted to the new owners where appropriate
- [x] master surfaces can be synchronized to show both new chains coherently

---

## 5) Rollback Approach

If the extraction proves too broad:
- preserve the new chain history and phase records
- narrow the integrations before removing the new chains entirely
- avoid rolling back to a state where the specialist domains are again scattered with duplicate active authority inside broader owners
- preserve bounded history rather than silently erasing the extraction wave
