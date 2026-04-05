# Changelog - RULES Plugin Extension

> **Parent Document:** [../design/rules-plugin-extension.design.md](../design/rules-plugin-extension.design.md)
> **Current Version:** 1.1
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-04-06 | **[Expanded plugin install and hook-behavior documentation](#version-11)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.0 | 2026-04-06 | **[Created design authority for the RULES plugin extension area](#version-10)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |

---

<a id="version-10"></a>
## Version 1.1: Expanded plugin install and hook-behavior documentation

**Date:** 2026-04-06
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `plugin/README.md` with step-by-step installation guidance from the package root.
- Added clearer explanation of how `SessionStart`, `PreCompact`, and `PostCompact` behave in the current first slice.
- Documented the expected witness files under `${CLAUDE_PLUGIN_DATA}/compact/`.
- Added explicit troubleshooting guidance for the duplicate `hooks/hooks.json` load failure and documented the correct package pattern.
- Extended `design/rules-plugin-extension.design.md` so the install/runtime contract now captures the same first-pass package behavior more explicitly.

### Summary
Expanded the RULES plugin companion docs so installation, runtime hook behavior, witness outputs, and the duplicate-hook-path pitfall are easier to understand before git push/update.

---

## Version 1.0: Created design authority for the RULES plugin extension area

**Date:** 2026-04-06
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Created `design/rules-plugin-extension.design.md` as the root design authority for the optional `plugin/` companion area.
- Defined `plugin/` as a support / extension package rather than a second rules authority.
- Recorded the package-local scaffold for `README.md`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `hooks/hooks.json`, and compact lifecycle scripts.
- Explicitly prohibited duplicate governance drift under `plugin/`.

### Summary
Created one root design document for the RULES plugin companion so hook-based compact handling can be packaged cleanly without weakening root RULES authority.
