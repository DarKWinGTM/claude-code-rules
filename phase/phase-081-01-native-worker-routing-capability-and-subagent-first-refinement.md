# Phase 081-01 - Native Worker Routing Capability and Subagent-First Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 081-01
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md), [../design/custom-agent-selection-priority.design.md](../design/custom-agent-selection-priority.design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md)
> **Patch References:** [../patch/native-worker-routing-capability-and-subagent-first-refinement.patch.md](../patch/native-worker-routing-capability-and-subagent-first-refinement.patch.md)

---

## Objective

Refine the P080 worker-routing model so broad work is subagent-first, capability-based, and intent-first, while Agent Team / teammate workflow remains an exceptional coordination escalation rather than the normal worker path.

พูดง่าย ๆ: ให้ RULES สอน AI ว่า “งานอ่านเยอะ/search เยอะ/audit เยอะ ให้ใช้ subagent ก่อนถ้าเหมาะ” แต่ต้องไม่ไหลไปสำรวจ project ถ้าผู้ใช้ถามเรื่องพฤติกรรมของ AI.

---

## Why This Phase Exists

After P080 was released, user testing showed the behavior was still not sharp enough in one important case: the assistant treated pasted logs and project paths from another session as a project-exploration request instead of recognizing that the user was asking about AI/RULES behavior and subagent usage.

The user also clarified:
- the target is standalone subagent usage, not Agent Team over-tasking
- a ban on teammate / Agent Team does not ban `Agent(...)`, `Explore(...)`, or comparable standalone worker mechanisms
- rules should not hardcode one tool name to one agent path
- routing should identify intent, workload shape, and required worker capability first

---

## Entry Conditions

- P080/v9.79 native worker routing is complete, installed, pushed, and released.
- The user requested RULES improvement, runtime install, governed docs sync, git push, and release.
- Active runtime rule count should remain 42 because P081 refines existing owner chains rather than adding a new runtime rule.

---

## Implementation Plan

### 1) Refine native worker-routing owner

- Update `native-worker-agent-routing-and-context-control.md` to v1.1.
- Update companion design and changelog to v1.1.
- Add intent-first behavior before project exploration.
- Add subagent-first worker-scale language.
- Add capability-based routing and team-restriction boundary.

### 2) Refine custom-agent selection boundary

- Update `custom-agent-selection-priority.md` to v1.3.
- Update companion design and changelog to v1.3.
- Clarify this chain selects the best visible specialist for the required capability after native routing has already selected delegation/specialist handling.
- Prevent this chain from escalating standalone subagent-fit work into Agent Team workflow.

### 3) Refine execution-continuity boundary

- Update `execution-continuity-and-mode-selection.md` to v1.9.
- Update companion design and changelog to v1.9.
- Add intent recheck before project exploration when pasted logs/paths/snippets could be misread.
- Keep broad continuation routed through subagent-first worker routing.

### 4) Master and governed record sync

- Update `design/design.md` to v9.80 while keeping active runtime count 42.
- Update `changelog/changelog.md` with the v9.80 release entry.
- Update `README.md` current-state guidance and install guidance without turning README into a changelog dump.
- Update `TODO.md` durable tracking.
- Update `phase/SUMMARY.md` with phase 081.
- Keep this phase record and the P081 patch synchronized.

### 5) Runtime install, release, and verification path

- Run source consistency audit.
- Install only the README-listed 42 active runtime rule files into `/home/node/.claude/rules/`.
- Verify source/runtime hash parity and keep destination markdown files outside the active install set observed-only.
- Commit source changes.
- Push to `origin/master`.
- Create GitHub release `v9.80`.

---

## Out of Scope

- No new active runtime rule file.
- No memory update for this behavior correction; the correction belongs in RULES.
- No NodeClaw project implementation or operator console inspection.
- No exact tool-name taxonomy that hardcodes every tool to a specific worker path.
- No Agent Team / teammate workflow unless a later task truly needs shared ownership, dependencies, messaging, or implementation/review/test/docs sync.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.

---

## Affected Artifacts

### Touched active runtime rule chains

- `native-worker-agent-routing-and-context-control.md`
- `design/native-worker-agent-routing-and-context-control.design.md`
- `changelog/native-worker-agent-routing-and-context-control.changelog.md`
- `custom-agent-selection-priority.md`
- `design/custom-agent-selection-priority.design.md`
- `changelog/custom-agent-selection-priority.changelog.md`
- `execution-continuity-and-mode-selection.md`
- `design/execution-continuity-and-mode-selection.design.md`
- `changelog/execution-continuity-and-mode-selection.changelog.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/native-worker-routing-capability-and-subagent-first-refinement.patch.md`
- `phase/phase-081-01-native-worker-routing-capability-and-subagent-first-refinement.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P081 as completed after source sync, source audit, runtime install parity, git push, and GitHub release passed.
- `changelog/changelog.md` should record v9.80 as the master version authority.
- Per-chain changelogs should record v1.1, v1.3, and v1.9.
- README should present current-state guidance and active install scope, not a detailed changelog dump.

---

## Verification

- [x] `native-worker-agent-routing-and-context-control` v1.1 source/design/changelog updated.
- [x] `custom-agent-selection-priority` v1.3 source/design/changelog updated.
- [x] `execution-continuity-and-mode-selection` v1.9 source/design/changelog updated.
- [x] Master records describe v9.80 and active runtime count 42 consistently.
- [x] README Bash and PowerShell install arrays still include exactly the 42 active runtime rule files.
- [x] Golden semantic scenarios pass for intent-first behavior, subagent-first broad work, Agent Team restriction boundary, capability routing, analyzed handoff, and leader verification.
- [x] Runtime install parity passes for 42 active runtime rule files.
- [x] Source/runtime release artifacts are ready for git publish and release.

---

## Closeout Summary

What this phase delivers:
- P081 refined the native worker-routing behavior and shipped the synchronized v9.80 source/runtime release.

Feature / Improvement:
- Intent-first, capability-based, standalone-subagent-first routing refinement for broad independent work.

Impact:
- The leader session should avoid unnecessary project exploration and context-heavy raw absorption when the user is asking about AI/RULES behavior or when a bounded standalone worker lane can filter broad evidence first.

Verification:
- Owner-chain source edits, v9.80 master records, source audit, 42-file runtime install/parity, git push, and GitHub release `v9.80` are complete.

Next phase state:
- No next phase selected.

---

## Exit Criteria

- P081 owner-chain runtime, design, and changelog versions align.
- Master records describe v9.80 consistently.
- Active runtime count remains 42.
- P081 phase and patch records exist and link correctly.
- Final source audit passes.
- Runtime install parity passes for the 42 active runtime rule files.
- Source/runtime release artifacts are pushed and released as `v9.80`.

---

## Risks and Rollback Notes

Risk:
- Subagent-first wording could be overread as requiring agents for every task.

Mitigation:
- Preserve direct-handling exceptions for trivial, low-output, tightly sequential, exact interactive-control, or high-overlap work.

Risk:
- Capability-based routing could drift into vague non-action if no worker is actually dispatched.

Mitigation:
- Keep the delegate-or-justify gate: broad worker-fit work must dispatch a worker or state a narrow direct-handling reason.

Risk:
- Team/teammate restrictions could again be misread as all-agent bans.

Mitigation:
- State the restriction boundary explicitly: Agent Team bans do not ban standalone subagents unless the user says so.

Rollback:
- Narrow P081 trigger wording through a governed rollback.
- Preserve the P080 first-class worker-routing owner if still useful.
- Preserve leader verification and custom-agent selection boundary.
- Do not delete other runtime destination markdown files without separate explicit destructive authorization.

---

## Next Possible Phases

- None selected.
