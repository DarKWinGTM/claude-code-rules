# Phase 080-01 - Native Worker Agent Routing and Context Control

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 080-01
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md), [../design/custom-agent-selection-priority.design.md](../design/custom-agent-selection-priority.design.md), [../design/execution-continuity-and-mode-selection.design.md](../design/execution-continuity-and-mode-selection.design.md)
> **Patch References:** [../patch/native-worker-agent-routing-and-context-control.patch.md](../patch/native-worker-agent-routing-and-context-control.patch.md)

---

## Objective

Add native worker-agent routing and context control so broad, high-output, high-context, multi-surface, or naturally parallel work is proactively delegated to the smallest effective worker structure instead of defaulting to leader-session raw absorption.

พูดง่าย ๆ: ให้ main session คุมและ verify งาน แต่ใช้ subagent หรือ Agent Team ช่วยกรอง/ค้น/ตรวจ/ทำงานคู่ขนานเมื่อรูปงานเหมาะสม.

---

## Why This Phase Exists

The user clarified that the desired behavior is not a rigid rule like “tool X uses agent,” and not a fixed 300-word worker summary. The intended model is workload-shaped routing:
- decide by context cost, output noise, independence, parallel value, risk, coordination need, and edit overlap
- use agents natively during real work, not only after explicit user prompts
- keep worker handoffs analyzed and proportionate
- keep leader session responsible for synthesis and verification

---

## Entry Conditions

- P079/v9.78 evidence-seeking proof-aware reasoning is complete, installed, pushed, and released.
- The user selected Option A: create a first-class runtime rule owner.
- The user requested source update, runtime install, governed docs sync, git push, and release for this wave.

---

## Implementation Plan

### 1) New active rule owner

- Create `native-worker-agent-routing-and-context-control.md`.
- Create `design/native-worker-agent-routing-and-context-control.design.md`.
- Create `changelog/native-worker-agent-routing-and-context-control.changelog.md`.

### 2) Adjacent rule integration

- Update `custom-agent-selection-priority.md` and companion design/changelog to clarify that it selects specialists after worker routing decides delegation is appropriate.
- Update `execution-continuity-and-mode-selection.md` and companion design/changelog so continuation into broad next work does not bypass worker routing.

### 3) Master and governed record sync

- Update `design/design.md` to v9.79 and active runtime count 42.
- Update `changelog/changelog.md` to v9.79.
- Update `README.md` current-state and install arrays for the 42-rule active runtime set.
- Update `TODO.md` durable tracking.
- Update `phase/SUMMARY.md` with phase 080.
- Create the P080 patch artifact and this phase record.

### 4) Runtime install, release, and verification path

- Run source consistency audit.
- Install only the README-listed 42 active runtime rule files into `/home/node/.claude/rules/`.
- Verify source/runtime hash parity and keep destination markdown files outside the active install set observed-only.
- Commit source changes.
- Push to `origin/master`.
- Create GitHub release `v9.79`.

---

## Out of Scope

- No exact plugin/shared-board task grammar changes.
- No package-owned custom tmux bridge activation.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.
- No rule forcing agents for trivial one-step work.
- No fixed generic worker handoff word cap.

---

## Affected Artifacts

### New active runtime rule chain

- `native-worker-agent-routing-and-context-control.md`
- `design/native-worker-agent-routing-and-context-control.design.md`
- `changelog/native-worker-agent-routing-and-context-control.changelog.md`

### Adjacent active runtime rule chains

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
- `patch/native-worker-agent-routing-and-context-control.patch.md`
- `phase/phase-080-01-native-worker-agent-routing-and-context-control.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P080 as completed after source sync, source audit, runtime install, and parity verification, with governed source/runtime artifacts prepared for git publish/release.
- `changelog/changelog.md` records v9.79 as the master version authority.
- Per-chain changelogs record new or bumped owner versions.
- README presents current-state install guidance without dumping version history.

---

## Verification

- [x] New P080 rule/design/changelog triad exists and links correctly.
- [x] `custom-agent-selection-priority` remains candidate-selection owner, not workload-routing owner.
- [x] `execution-continuity-and-mode-selection` reflects the worker-routing continuation boundary.
- [x] Master records describe v9.79 and active runtime count 42 consistently.
- [x] README Bash and PowerShell install arrays include the new active runtime rule.
- [x] Golden semantic scenarios pass for broad delegation, trivial direct handling, analyzed handoff, and leader verification.
- [x] Runtime install parity passes for 42 active runtime rule files.
- [x] Source/runtime release artifacts are ready for git publish and release.

---

## Closeout Summary

What this phase delivers:
- P080 adds a native worker-routing owner so suitable broad work can be delegated to subagents or Agent Teams before the leader session absorbs all raw context.

Feature / Improvement:
- Workload-shaped agent routing and leader-context protection across execution, research, audit, and verification workflows.

Impact:
- The assistant can preserve main-session context, use parallel workers more intelligently, and still keep final synthesis and completion claims evidence-verified.

Verification:
- Source sync, source audit, golden semantic scenario coverage, and 42-rule runtime install parity have passed; source/runtime artifacts are ready for git publish and v9.79 release.

Next phase state:
- None selected.

---

## Exit Criteria

- P080 owner-chain runtime, design, and changelog exist and align.
- Adjacent owner chains describe the routing/selection/continuation boundary correctly.
- Master records describe v9.79 consistently.
- P080 phase and patch records exist and link correctly.
- Final source audit passes.
- Runtime install parity passes for the 42 active runtime rule files.
- Source/runtime release artifacts are ready for git push and release `v9.79`.

---

## Risks and Rollback Notes

Risk:
- Worker routing could be overread as requiring agents for every task.

Mitigation:
- Preserve direct-handling exceptions for trivial, low-output, tightly sequential, or high-overlap work.

Risk:
- New rule could overlap with `custom-agent-selection-priority.md`.

Mitigation:
- Keep P080 as routing owner and custom-agent-selection as candidate-selection owner.

Risk:
- Runtime/plugin/shared-board details could leak into Main RULES.

Mitigation:
- Keep exact plugin/shared-board/custom tmux mechanics out of scope.

Rollback:
- Narrow or remove P080 routing triggers through a governed rollback.
- Preserve leader verification and custom-agent selection boundary if still useful.
- Do not delete other runtime destination markdown files without separate explicit destructive authorization.

---

## Next Possible Phases

- None selected.
