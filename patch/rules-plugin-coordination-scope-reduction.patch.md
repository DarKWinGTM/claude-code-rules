# RULES Plugin Coordination Scope Reduction Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Active
> **Target Design:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md) v1.30
> **Session:** 1b81d009-cf82-44a3-9739-cd3ea4af34dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## 1) Context

This patch captures the RULES-side reduction of active plugin scope so coordination runtime surfaces stop being presented as fully owned by `claude-code-rules@darkwingtm`.

## 2) Analysis

Risk level: Medium

Main concern:
- package manifests/docs/hooks can continue to imply one unified active owner even after the coordination fork exists

## 3) Change Items

### Change Item 1
- **Target location:** RULES plugin packaging/docs/hooks
- **Change type:** replacement

**Before**
```text
The RULES plugin package was presented as the active home of both compact/runtime support and coordination runtime.
```

**After**
```text
The RULES plugin package is reduced toward a migration/reference role, while active coordination ownership is documented as moved to `claude-session-coordination@darkwingtm`.
```

## 4) Verification

- [ ] plugin manifests/docs/hooks reflect the reduced RULES package role
- [ ] no lingering package surface still presents RULES as the sole active owner of the coordination runtime

## 5) Rollback Approach

If scope reduction is postponed:
- restore a clear unified-package claim temporarily instead of leaving ambiguous mixed wording
