# Changelog - Worker Routing and Context Control

> **Parent Document:** [../worker-routing-and-context.md](../worker-routing-and-context.md)
> **Current Version:** 1.10
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

---

## Version History (Unified)

| Version | Date | Changes | Session ID |
|---------|------|---------|------------|
| 1.10 | 2026-05-28 | **[Added P123 goal-owned helper lane refinement](#version-110)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.9 | 2026-05-18 | **[Added P108 routing-core compaction and owner redistribution](#version-19)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.8 | 2026-05-18 | **[Added P106 chronology-aware authority routing](#version-18)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.7 | 2026-05-17 | **[Added P105 folder-scoped generic-parent routing refinement](#version-17)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.6 | 2026-05-17 | **[Added P104 naming-aware append-vs-shard routing gate](#version-16)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.5 | 2026-05-17 | **[Added P103 observed-example handoff separation](#version-15)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.4 | 2026-05-17 | **[Added P102 append-vs-shard routing gate](#version-14)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.3 | 2026-05-17 | **[Applied P100 safe-first compression refinement](#version-13)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| 1.2 | 2026-05-16 | **[Added P099 proactive delegation efficiency doctrine](#version-12)** | 1f1873d2-0feb-485f-a5ff-d383254590dd |
| | | Summary: Extended `worker-routing-and-context.md` and its design companion so the merged runtime owner now covers proactive delegation triggers, work-shape topology selection, reusable lane/swarm presets, stronger worker handoffs, leader context budget, and delegation-efficiency review signals while keeping the active runtime count at 18. | |
| 1.1 | 2026-05-16 | **[Added P098 intent-grounding refinement](#version-11)** | 808f88f7-3682-45ad-8f3e-3caf233d3835 |
| | | Summary: Extended `worker-routing-and-context.md` so the merged runtime owner now covers intent taxonomy, routing implications, diagnosis-first mixed-intent handling, and context-safe worker selection for the P098 intent-grounding conversation doctrine release wave. | |
| 1.0 | 2026-05-16 | **[Created merged runtime owner chain](#version-10)** | 6ecc64cf-8eed-497a-9b84-02f5d5228ee3 |
| | | Summary: Created `worker-routing-and-context.md` as a body-sufficient merged runtime owner for leader-context protection, worker routing, custom-agent selection, and document-density control in the compact 18-rule runtime set. | |

---

<a id="version-110"></a>
## Version 1.10: Added P123 goal-owned helper lane refinement

**Date:** 2026-05-28
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `worker-routing-and-context.md` from v1.9 to v1.10.
- Updated `design/worker-routing-and-context.design.md` from v1.9 to v1.10.
- Added bounded goal-owned internal helper lane guidance for analysis, verification, testing, and compact plan drafting.
- Preserved minimally scoped helper use, read-only-by-default posture where appropriate, and leader-owned synthesis/proof verification.
- Preserved worker findings as input instead of automatic goal-completion proof.

### Summary
`worker-routing-and-context.md` now makes conditional goal-owned helper lanes explicit so native subagents can support `/goal` without becoming a new public surface or a proof shortcut.

---

<a id="version-19"></a>
## Version 1.9: Added P108 routing-core compaction and owner redistribution

**Date:** 2026-05-18
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `worker-routing-and-context.md` from v1.8 to v1.9.
- Updated `design/worker-routing-and-context.design.md` from v1.8 to v1.9.
- Removed non-routing document-density, append-vs-shard, compact/thrash, and delegated governed-document repair doctrine from the routing owner.
- Kept routing-core behavior, routing-only document-boundary deferral, and leader-verification boundaries intact while reducing runtime size.

### Summary
`worker-routing-and-context.md` now stays focused on routing-core behavior while deferring non-routing document doctrine to the correct owners.

---

<a id="version-18"></a>
## Version 1.8: Added P106 chronology-aware authority routing

**Date:** 2026-05-18
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `worker-routing-and-context.md` from v1.7 to v1.8.
- Updated `design/worker-routing-and-context.design.md` from v1.7 to v1.8.
- Added chronology-aware routing guidance so reachable completed history cannot silently override the active P105 parent-model doctrine.
- Kept namespace-scope parent selection and the no-dual-parent boundary intact.

### Summary
`worker-routing-and-context.md` now forces routing/handoff decisions to name the active authority explicitly when older completed wording is still reachable.

---

<a id="version-17"></a>
## Version 1.7: Added P105 folder-scoped generic-parent routing refinement

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `worker-routing-and-context.md` from v1.6 to v1.7.
- Updated `design/worker-routing-and-context.design.md` from v1.6 to v1.7.
- Replaced master-only generic-parent assumptions in the append-vs-shard gate with namespace-scope parent-model decisions.
- Added routing guidance that folder-scoped single-chain namespaces may keep a generic parent while shared folders should prefer self-identifying semantic parents.
- Preserved bootstrap-first timing checks and the no-dual-parent boundary.

### Summary
`worker-routing-and-context.md` now carries the P105 corrective refinement needed to route parent-model decisions from namespace scope rather than from a blanket semantic-parent rule.

---

<a id="version-16"></a>
## Version 1.6: Added P104 naming-aware append-vs-shard routing gate

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `worker-routing-and-context.md` from v1.5 to v1.6.
- Updated `design/worker-routing-and-context.design.md` from v1.5 to v1.6.
- Expanded append-vs-shard questions so routing decisions distinguish master-chain versus subject-chain naming, semantic parent filename choice, compatibility-parent role, bootstrap exit trigger, and shard-opening basis.
- Added explicit bootstrap-first behavior when no checked trigger justifies leaving a compact semantic parent body yet.
- Preserved leader verification responsibility, aggregate-read gating, and the released P102/P103 routing semantics.

### Summary
`worker-routing-and-context.md` now carries the P104 routing refinement needed to keep naming and shard-opening decisions explicit before assistants mirror or open structure by momentum.

---

<a id="version-15"></a>
## Version 1.5: Added P103 observed-example handoff separation

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `worker-routing-and-context.md` from v1.4 to v1.5.
- Updated `design/worker-routing-and-context.design.md` from v1.4 to v1.5.
- Added handoff doctrine so workers and leaders separate observed example shape, extracted doctrine, selected target form, and verified equivalence basis when example-backed normalization is in scope.
- Extended the append-vs-shard gate so example-grounded decisions must identify what was observed, what doctrine is being extracted, and what target form is selected here.
- Preserved leader verification responsibility, aggregate-read gating, and worker-routing ownership boundaries.

### Summary
`worker-routing-and-context.md` now carries the P103 handoff refinement needed to stop example-backed structure recommendations from collapsing into one unsupported claim.

---

<a id="version-14"></a>
## Version 1.4: Added P102 append-vs-shard routing gate

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `worker-routing-and-context.md` from v1.3 to v1.4.
- Updated `design/worker-routing-and-context.design.md` from v1.3 to v1.4.
- Extended touched-doc append-vs-restructure behavior into append-vs-shard gating for compact design/changelog parents.
- Added trigger coverage so governed parent authorities must classify chain shape before silently absorbing more detail.
- Preserved leader verification responsibility and worker-routing ownership boundaries.

### Summary
`worker-routing-and-context.md` now carries the P102 append-vs-shard routing gate so document-structure drift is checked before parent authority files keep growing by momentum.

---

<a id="version-13"></a>
## Version 1.3: Applied P100 safe-first compression refinement

**Date:** 2026-05-17
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Updated `worker-routing-and-context.md` from v1.2 to v1.3.
- Updated `design/worker-routing-and-context.design.md` from v1.2 to v1.3.
- Compressed repeated intent-routing explanation, aggregate-read gate prose, preset descriptions, and audit-heuristic wording.
- Preserved intent-first routing, aggregate-read gate behavior, proactive trigger logic, topology selection, stronger handoff contract, leader verification duty, and the safe-io ownership split.

### Summary
`worker-routing-and-context.md` now stays more compact while preserving its routing/orchestration mechanism and owner boundary for the P100 safe-first compression wave.

---

<a id="version-12"></a>
## Version 1.2: Added P099 proactive delegation efficiency doctrine

**Date:** 2026-05-16
**Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd

### Changes
- Extended `worker-routing-and-context.md` for the P099 proactive subagent-efficiency doctrine wave.
- Added proactive delegation trigger matrix coverage, work-shape topology selection, lane/swarm preset guidance, stronger handoff requirements, leader context-budget doctrine, and delegation-efficiency review signals.
- Updated `design/worker-routing-and-context.design.md` to preserve the new runtime semantics and the no-new-root-rule / 18-active-runtime-set boundary.

### Summary
`worker-routing-and-context.md` now carries the P099 proactive delegation efficiency doctrine while preserving its routing/orchestration owner boundary and the compact active runtime set.

<a id="version-11"></a>
## Version 1.1: Added P098 intent-grounding refinement

**Date:** 2026-05-16
**Session:** 808f88f7-3682-45ad-8f3e-3caf233d3835

### Changes
- Extended `worker-routing-and-context.md` for the P098 intent-grounding conversation doctrine wave.
- Added doctrine coverage for intent taxonomy, routing implications, diagnosis-first mixed-intent handling, and context-safe worker selection.
- Preserved the compact merged runtime owner structure and kept the active runtime install count unchanged at 18.

### Summary
`worker-routing-and-context.md` now carries the P098 intent-grounding refinement while preserving its existing merged-owner boundary.

<a id="version-10"></a>
## Version 1.0: Created merged runtime owner chain

**Date:** 2026-05-16
**Session:** 6ecc64cf-8eed-497a-9b84-02f5d5228ee3

### Changes
- Created `worker-routing-and-context.md` as an active runtime rule in the compact merged runtime set.
- Created `design/worker-routing-and-context.design.md` as the target-state companion for the merged owner chain.
- Preserved absorbed-rule behavior for native worker routing, custom agent priority, context-load control, and God-line/God-document routing.
- Kept historical legacy root files outside the active runtime authority after merge cleanup.

### Summary
`worker-routing-and-context.md` now provides one governed runtime owner for leader-context protection, worker routing, custom-agent selection, and document-density control, reducing root-rule fragmentation while preserving execution-relevant doctrine.
