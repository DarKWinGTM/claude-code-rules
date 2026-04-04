# Changelog - Operational Failure Handling

> **Parent Document:** [../operational-failure-handling.md](../operational-failure-handling.md)
> **Current Version:** 1.2
> **Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.2 | 2026-04-04 | **[Added team-agent duplicate and stale-presence handling profile](#version-12)** | dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e |
| 1.1 | 2026-03-12 | **[Upgraded operational-failure-handling to explicit case-profile semantics](#version-11)** | 451fb64e-f2a5-43a5-bf98-47f01244f15c |
| | | Summary: Refined the chain from generic retry policy into a profile-driven operational-failure model with seeded Web Search, WebFetch, local-path, permission, and approval-denial cases plus a future-extension contract | |
| 1.0 | 2026-03-12 | **[Created first-class operational-failure-handling rule chain for generalized technical failure handling](#version-10)** | 451fb64e-f2a5-43a5-bf98-47f01244f15c |
| | | Summary: Created a new design/runtime/changelog chain that governs operational failure classification, retry ceilings, cooldown honesty, and stop/escalation behavior without redefining refusal or emergency authority | |

---

<a id="version-12"></a>
## Version 1.2: Added team-agent duplicate and stale-presence handling profile

**Date:** 2026-04-04
**Session:** dd0bf4af-a66b-4b07-bb9d-a90a0e57b54e

### Changes
- Updated `operational-failure-handling.md` from v1.1 to v1.2.
- Updated `design/operational-failure-handling.design.md` from v1.1 to v1.2.
- Added a new case profile: `TEAM_AGENT_DUPLICATE_OR_STALE_PRESENCE`.
- Classified duplicate-looking or stale team-agent presence as an inspect-first case rather than a respawn-first case.
- Added recovery guidance so assistant behavior now prefers verifying team state, cleanup, and distinct-role need before spawning another same-role teammate.

### Summary
Operational-failure-handling now treats duplicate-looking or stale team-agent presence as a first-class inspect-before-respawn case instead of letting overlapping teammate churn count as progress.

---

<a id="version-11"></a>
## Version 1.1: Upgraded operational-failure-handling to explicit case-profile semantics

**Date:** 2026-03-12
**Session:** 451fb64e-f2a5-43a5-bf98-47f01244f15c

### Changes
- Updated `design/operational-failure-handling.design.md` from v1.0 to v1.1.
- Updated runtime `operational-failure-handling.md` from v1.0 to v1.1.
- Refined the chain from a generic retry taxonomy into a profile-driven operational-failure model.
- Added explicit immediate-retry gating so the rule now distinguishes between:
  - cases where one immediate retry probe is justified
  - cases where provider guidance forbids immediate retry
  - cases where no retry is justified until input, authorization, permission, approval, or context changes
- Added seeded case-specific profiles for:
  - `WEB_SEARCH_TIMEOUT`
  - `WEB_SEARCH_429_WITH_RETRY_AFTER`
  - `WEB_SEARCH_5XX_OR_PROVIDER_UNAVAILABLE`
  - `WEB_FETCH_PRIVATE_OR_AUTH_REQUIRED`
  - `WEB_FETCH_INVALID_URL_OR_BAD_INPUT`
  - `LOCAL_FILE_NOT_FOUND`
  - `LOCAL_PERMISSION_DENIED`
  - `TOOL_APPROVAL_DENIED`
- Added a future-extension contract so new operational cases can be added later using one shared mandatory profile schema and one shared precedence model.
- Clarified precedence so case-specific profiles override generic defaults while still yielding to higher authority boundaries and explicit upstream/provider guidance.

### Summary
Upgraded `operational-failure-handling` from a generic retry policy into a case-by-case operational-failure rule with explicit Web Search and WebFetch handling plus an extensible profile model for future cases.

---

<a id="version-10"></a>
## Version 1.0: Created first-class operational-failure-handling rule chain for generalized technical failure handling

**Date:** 2026-03-12
**Session:** 451fb64e-f2a5-43a5-bf98-47f01244f15c

### Changes
- Created `design/operational-failure-handling.design.md` as the active target-state design for generalized operational failure handling.
- Created runtime `operational-failure-handling.md` as a first-class rule defining:
  - deterministic failure classes: `POTENTIALLY_TRANSIENT`, `LIKELY_SYSTEMIC`, and `DETERMINISTIC_NON_RETRIABLE`
  - default retry ceilings and recommended cooldowns
  - same-objective aggregate retry protections across tools and domains
  - stop and escalation behavior for repeated or broader failures
  - a deterministic post-failure mini-schema: `failure_class`, `retry_posture`, `attempts_used`, `recommended_cooldown`, `reason`, `what_can_be_done_now`, `how_to_proceed`
- Explicitly bounded rule authority so the chain defines classification, retry ceilings, cooldown recommendations, stop conditions, escalation logic, and communication obligations without pretending that rules themselves can deterministically sleep, enforce timer backoff, or guarantee delayed re-execution.
- Positioned the chain as adjacent to:
  - `recovery-contract`
  - `refusal-minimization`
  - `functional-intent-verification`
  - `refusal-classification`
  - `emergency-protocol`
  - `authority-and-scope`
  - `zero-hallucination`
  - `no-variable-guessing`
  while preserving each adjacent chain's existing authority boundary.

### Summary
Created a first-class `operational-failure-handling` rule chain so ordinary technical failure handling now has explicit governed policy for retry ceilings, cooldown honesty, and escalation without creating a parallel refusal or emergency framework.
