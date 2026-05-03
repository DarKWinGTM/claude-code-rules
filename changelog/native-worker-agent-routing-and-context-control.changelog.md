# Changelog - Native Worker Agent Routing and Context Control

> **Parent Document:** [../native-worker-agent-routing-and-context-control.md](../native-worker-agent-routing-and-context-control.md)
> **Current Version:** 1.0
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.0 | 2026-05-03 | **[Created native worker routing and context-control owner](#version-10)** | d42465eb-30a7-4bc8-b9d6-03e52306e9a5 |
| | | Summary: Created a first-class rule chain for proactive workload-shaped worker routing, smallest-effective subagent/Agent Team selection, analyzed handoffs, parallel edit containment, and leader verification | |

---

<a id="version-10"></a>
## Version 1.0: Created native worker routing and context-control owner

**Date:** 2026-05-03
**Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5

### Changes
- Created `native-worker-agent-routing-and-context-control.md` as the active runtime rule owner for native worker routing and leader-context protection.
- Created `design/native-worker-agent-routing-and-context-control.design.md` as the target-state design companion.
- Defined the worker-scale gate for broad, noisy, context-heavy, multi-surface, or naturally parallel work.
- Defined the direct leader, focused subagent, multiple subagent, and Agent Team routing model.
- Added workload-shape routing criteria so delegation is not tied rigidly to specific tool names.
- Added the worker handoff quality contract: analyzed, proportionate, no raw dumps, and no fixed generic word cap.
- Added parallel edit containment and mandatory leader verification before completion claims.
- Positioned `custom-agent-selection-priority.md` as the downstream best-fit specialist selection owner after routing establishes that delegation is appropriate.

### Summary
Native worker routing is now a first-class RULES owner so the assistant can proactively offload suitable broad work to subagents or Agent Teams while keeping the leader session responsible for synthesis, verification, and user-facing claims.
