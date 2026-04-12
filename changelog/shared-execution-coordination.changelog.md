# Changelog - Shared Execution Coordination

> **Parent Document:** [../shared-execution-coordination.md](../shared-execution-coordination.md)
> **Current Version:** 1.1
> **Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-04-13 | **[Separated handoff request naming from receiving-side phase ownership](#version-11)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| 1.0 | 2026-04-13 | **[Created first-class shared execution coordination rule chain](#version-10)** | 11c4bd2f-216e-4779-81bf-26d34a4fcaeb |
| | | Summary: Created a new coordination owner for multi-session shared execution boards, session lease/handoff semantics, retention/aging policy, and optional memsearch / future optional peer-messaging boundaries | |

---

<a id="version-11"></a>
## Version 1.1: Separated handoff request naming from receiving-side phase ownership

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Updated `shared-execution-coordination.md` from v1.0 to v1.1.
- Updated `design/shared-execution-coordination.design.md` from v1.0 to v1.1.
- Added explicit request-layer vs execution-layer separation semantics.
- Added an explicit receiving-side phase ownership rule so sender phase labels do not become the default visible handoff title.
- Added canonical request naming, handoff note, and accept-and-remap guidance.

### Summary
Shared execution coordination now clearly separates cross-session request naming from receiving-side execution phase ownership, reducing phase-owner ambiguity during handoff.

---

<a id="version-10"></a>
## Version 1.0: Created first-class shared execution coordination rule chain

**Date:** 2026-04-13
**Session:** 11c4bd2f-216e-4779-81bf-26d34a4fcaeb

### Changes
- Created `shared-execution-coordination.md` as the first-class owner for multi-session shared execution coordination.
- Created `design/shared-execution-coordination.design.md` as the target-state design companion.
- Defined the shared task list as an execution-coordination layer rather than semantic truth.
- Defined session-lease, handoff, and context-bridge semantics for shared execution boards.
- Defined continuity-first retention, partial cleanup, and aging-eligibility boundaries so shared task history is not cleared too aggressively.
- Defined memsearch as an optional supplemental context bridge and `claude-peers-mcp` as future optional live coordination infrastructure rather than active required behavior.

### Summary
Created a first-class shared execution coordination owner so multi-session task-list coordination, context-bridge behavior, and anti-overclear policy now have one explicit semantic authority.
