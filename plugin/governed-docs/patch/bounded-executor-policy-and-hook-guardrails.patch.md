# governed-docs bounded executor policy and hook guardrails patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Implemented / Checked-scope verified
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures P001-05, the bounded executor-policy and hook-guardrail slice.

## Analysis

Before this slice:
- the plugin could scan, classify, and plan, but it still lacked a controlled answer for what may be executed automatically
- there was no policy layer separating allowed preview behavior from blocked classes
- hook posture had no implementation scaffold

After this slice:
- executor-policy decisions distinguish advisory, guarded-execute, bounded-auto-normalize, and blocked paths
- preview normalization remains bounded and read-only
- hook guardrails exist only as advisory/support scaffolds and not as hidden mutation authority

## Change Items

### 1) Add executor policy decisions
- **Target artifact:** `src/governed_docs/executor_policy.py`
- **Change type:** additive
- **Before state:** no bounded execution decision layer existed
- **After state:** repair-plan items can be classified into allowed/blocked execution postures without widening into unsafe mutation by default

### 2) Add preview-only normalizer
- **Target artifact:** `src/governed_docs/normalizer.py`
- **Change type:** additive
- **Before state:** there was no bounded preview path for safe candidates
- **After state:** safe candidates can produce a no-mutation normalization preview while blocked items hard-stop

### 3) Add hook guardrail module and scaffold
- **Target artifact:** `src/governed_docs/hook_guardrails.py`, `.claude/hooks/governed-docs-reminder.sh`
- **Change type:** additive
- **Before state:** hook posture was design-only
- **After state:** the plugin has an explicit advisory/support-only reminder scaffold with no hidden mutation behavior

## Verification

Checked verification for this patch:
- `python3 -m unittest discover -s tests -v` → 40 tests passed
- the suite includes executor-policy, preview-normalizer, and hook-guardrail checks proving allowed and blocked branches remain distinct

Covers:
- blocked-class enforcement
- bounded preview behavior for safe candidates
- advisory-only hook guardrail posture

Does not cover:
- real governed-file mutation
- background hook activation as an authority surface

## Rollback approach

If this slice needs containment or partial rollback:
- keep blocked classes blocked by default
- prefer removing preview behavior before widening blocked scopes
- remove advisory hook scaffolds entirely before allowing them to drift into hidden authority
