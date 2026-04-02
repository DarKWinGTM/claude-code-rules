# Portable Implementation and Hardcoding Control Patch

## 0) Document Control

> **Current Version:** 1.0
> **Status:** Implemented - Pending Review
> **Target Design:** [../design/portable-implementation-and-hardcoding-control.design.md](../design/portable-implementation-and-hardcoding-control.design.md) v1.0
> **Target Rule:** [../portable-implementation-and-hardcoding-control.md](../portable-implementation-and-hardcoding-control.md)
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e
> **Full history:** [../changelog/portable-implementation-and-hardcoding-control.changelog.md](../changelog/portable-implementation-and-hardcoding-control.changelog.md)

---

## 1) Context

This patch captures the introduction of a first-class rule chain for portable implementation defaults and anti-hardcoding control.

Why this change matters:
- adjacent rules already covered local verification, accurate reporting, and project-documentation structure
- but no single chain owned the broader problem of hardcoded environment assumptions in shared artifacts
- a dedicated chain is needed so path hardcoding, install-location assumptions, localhost defaults, and similar machine-bound implementation drift are governed consistently instead of handled ad hoc

---

## 2) Analysis

Risk level: Low

Dependencies:
- `../no-variable-guessing.md`
- `../accurate-communication.md`
- `../project-documentation-standards.md`
- `../strict-file-hygiene.md`
- `../tactical-strategic-programming.md`

Review concern:
- the new chain should add one clear owner for environment-binding and hardcoding control without blurring adjacent rule ownership

---

## 3) Change Items

### Change Item 1
- **Target location:** RULES runtime inventory
- **Change type:** additive

**Before**
```text
Hardcoded environment assumptions were addressed only indirectly across several adjacent rules, with no first-class owner for portable implementation defaults.
```

**After**
```text
A dedicated first-class rule chain now owns portable implementation defaults, late-bound environment resolution, observed-local-fact separation, and anti-hardcoding discipline for shared artifacts.
```

### Change Item 2
- **Target location:** implementation-quality model
- **Change type:** additive

**Before**
```text
The system discouraged guessing and required local verification, but did not yet define one canonical model for portable placeholders, env/config resolution, and allowed machine-scoped exceptions.
```

**After**
```text
The new chain defines:
- portable-core defaults
- late-bound env/config resolution
- separation between shared contracts and observed local facts
- canonical placeholder and env notation
- forbidden anti-patterns for hardcoded environment assumptions
```

### Change Item 3
- **Target location:** adjacent-chain integration
- **Change type:** additive

**Before**
```text
Adjacent chains referenced local verification, accurate wording, and documentation quality, but no single owner governed the broader implementation-hardcoding problem.
```

**After**
```text
Adjacent chains keep their current authority while the new chain becomes the semantic owner of portable implementation and anti-hardcoding workflow.
```

---

## 4) Verification

- [ ] Confirm the design/runtime/changelog triad exists for the new chain
- [ ] Confirm the rule defines portable defaults, late binding, exception handling, and anti-hardcoding controls
- [ ] Confirm adjacent chains retain their own authority boundaries
- [ ] Confirm the patch remains readable as a before/after governance artifact

---

## 5) Rollback Approach

If the chain proves redundant or over-scoped:
- narrow the chain to portable implementation defaults and machine-scoped exception handling only
- preserve the triad and patch history rather than silently deleting the ownership experiment
- revert any adjacent-chain integration wording that overstates the new chain’s scope
