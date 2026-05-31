# governed-docs Design Chain Bootstrap Patch

> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36
> **Status:** Draft / Review-ready
> **Target Design:** [../design/design.md](../design/design.md) v0.1.0
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Context

This patch captures the before/after review surface for the first governed-docs design-wave bootstrap.

## Analysis

Before this wave, `plugin/governed-docs/` had no governed design chain and no synced plugin-local changelog / TODO / phase / patch support surfaces.

The design goal is to define a RULES-native companion model without implementing runtime behavior yet.

## Change Items

### 1) Create plugin-local design chain
- **Target artifact:** `design/design.md` and sibling design shards
- **Change type:** additive
- **Before state:** no plugin-local governed design chain existed
- **After state:** one compact parent plus seven design shards define the target model

### 2) Add explicit path-targeting doctrine
- **Target artifact:** design parent and relevant shards
- **Change type:** refinement
- **Before state:** command-path safety was not captured in the new design chain
- **After state:** user-facing operations require one explicit target workspace path and fail closed when it is missing or ambiguous

### 3) Sync support surfaces
- **Target artifact:** plugin-local changelog / TODO / phase / patch docs
- **Change type:** additive
- **Before state:** support surfaces did not exist for the plugin design wave
- **After state:** the design-wave state is reflected consistently across those governed docs

## Verification

Review should confirm:
- the parent design stays compact
- shard responsibilities do not overlap
- v1 remains design-only
- path targeting is explicit and not left to ambient cwd inference
- the plugin is not described as semantic owner of root governed surfaces

## Implementation Status

This artifact is design-wave only. No runtime implementation is claimed here.
