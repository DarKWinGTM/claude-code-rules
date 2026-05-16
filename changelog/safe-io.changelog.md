# Changelog - Safe I/O

> **Parent Document:** [../safe-io.md](../safe-io.md)
> **Current Version:** 1.1
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.1 | 2026-05-16 | **[Added P099 delegate-first aggregate-burst doctrine](#version-11)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| | | Summary: Extended `safe-io.md` and its design companion so the merged runtime owner now covers delegate-first aggregate read/output burst signals, burst-risk posture, and high-output flow updates while preserving the compact 18-rule runtime set. | |
| 1.0 | 2026-05-16 | **[Created merged runtime owner chain](#version-10)** | 6ecc64cf-8eed-497a-9b84-02f5d5228ee3 |
| | | Summary: Created `safe-io.md` as a body-sufficient merged runtime owner for bounded file reading and terminal output with parent-index-first and worker-first behavior in the compact 18-rule runtime set. | |

---

<a id="version-11"></a>
## Version 1.1: Added P099 delegate-first aggregate-burst doctrine

**Date:** 2026-05-16
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Extended `safe-io.md` for the P099 proactive subagent-efficiency doctrine wave.
- Added delegate-first aggregate read/output burst signals, burst-risk rows in the I/O risk model, and high-output flow updates for worker-first filtering.
- Updated `design/safe-io.design.md` to preserve the new read/output trigger semantics and the no-new-root-rule / 18-active-runtime-set boundary.

### Summary
`safe-io.md` now carries the P099 delegate-first aggregate-burst doctrine while preserving its safe-I/O ownership boundary and the compact active runtime set.

<a id="version-10"></a>
## Version 1.0: Created merged runtime owner chain

**Date:** 2026-05-16
**Session:** 6ecc64cf-8eed-497a-9b84-02f5d5228ee3

### Changes
- Created `safe-io.md` as an active runtime rule in the compact merged runtime set.
- Created `design/safe-io.design.md` as the target-state companion for the merged owner chain.
- Preserved absorbed-rule behavior for safe file reading, safe terminal output, sharded design/changelog reads, and high-output command control.
- Kept historical legacy root files outside the active runtime authority after merge cleanup.

### Summary
`safe-io.md` now provides one governed runtime owner for bounded file reading and terminal output with parent-index-first and worker-first behavior, reducing root-rule fragmentation while preserving execution-relevant doctrine.
