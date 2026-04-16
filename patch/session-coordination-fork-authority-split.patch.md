# Session Coordination Fork Authority Split Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Active
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.30
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch records the RULES-side authority split that moves active coordination runtime ownership toward `claude-session-coordination@darkwingtm` while keeping semantic authority in RULES.

## 2) Analysis

Risk level: Medium

Primary concern:
- dual active ownership between the reduced RULES plugin and the new coordination package

## 3) Change Items

### Change Item 1
- **Target location:** RULES-side authority docs
- **Change type:** replacement

**Before**
```text
The RULES plugin was still described as one unified package that owned both compact support and active coordination runtime.
```

**After**
```text
RULES keeps semantic authority and the reduced migration/reference package role, while the active coordination runtime/package ownership moves to `claude-session-coordination@darkwingtm`.
```

## 4) Verification

- [ ] ownership split is explicit in root/plugin/design docs
- [ ] no docs still imply the old unified package is the long-term active owner of both compact and coordination runtime

## 5) Rollback Approach

If the fork direction is reversed:
- restore unified-package ownership wording explicitly instead of leaving ambiguous half-split language
