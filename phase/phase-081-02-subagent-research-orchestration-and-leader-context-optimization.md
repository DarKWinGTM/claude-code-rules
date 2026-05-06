# Phase 081-02 - Subagent Research Orchestration and Leader Context Optimization

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 081-02
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md), [../design/external-verification-and-source-trust.design.md](../design/external-verification-and-source-trust.design.md)
> **Patch References:** [../patch/subagent-research-orchestration-and-leader-context-optimization.patch.md](../patch/subagent-research-orchestration-and-leader-context-optimization.patch.md)

---

## Objective

Refine the existing P081 native-worker routing family so broad external research, design-improvement research, and source-heavy evidence gathering are decomposed into focused subagent research lanes before the leader session absorbs raw search results.

พูดง่าย ๆ: ถ้างานคือ “ไปหาข้อมูลมาเยอะ ๆ เพื่อวิเคราะห์/ออกแบบให้ดีขึ้น” leader ควรวางหัวข้อและแบ่งเลนค้นคว้า แล้วให้ subagent ไปค้น วิเคราะห์ และส่งสรุปคุณภาพสูงกลับมา ไม่ใช่ให้ leader ทำ websearch/raw reading ทั้งหมดเอง.

---

## Why This Phase Exists

P081-01 already made broad work intent-first, capability-based, and standalone-subagent-first. The remaining gap is research orchestration: the current rule says broad external research is worker-fit, but it does not strongly define how the leader should decompose research topics, let subagents refine search strategy inside their lane, protect leader context from raw source volume, or recover when non-material live task tracking friction appears during worker dispatch.

P081-02 is a subphase, not a new major phase, because it refines the same native-worker routing owner chain rather than creating a separate runtime-rule domain.

---

## Entry Conditions

- P080 native worker routing owner exists.
- P081-01 standalone-subagent-first and intent-first refinement is completed.
- P084-01 development verification/debug strategy is completed and released as `v9.86` with 44 active runtime rules.
- User requested RULES improvement, runtime install, governed docs sync, git push, release, and systematic phase planning.

---

## Implementation Plan

### 1) Refine native worker research routing

- Add a research orchestration gate to `native-worker-agent-routing-and-context-control.md`.
- Define when broad research/design-improvement work should be split into one or more focused subagent lanes.
- Define leader responsibilities: research objective, lane map, synthesis, conflict resolution, and final verification.
- Define subagent responsibilities: scoped search strategy, query/topic refinement, source-quality filtering, analyzed findings, conflicts, implications, and evidence limits.

### 2) Integrate adjacent external research and continuation owners

- Update `external-verification-and-source-trust` so external verification can be orchestrated through subagent research lanes when source volume, comparison cost, or topic breadth is high.
- Update `execution-continuity-and-mode-selection` so broad research/design-improvement continuation does not become default leader raw search absorption.
- Update `todo-standards` only if needed to preserve live tracking expectations without letting task-list friction derail worker routing.

### 3) Sync governed master records

- Update `design/design.md`, `changelog/changelog.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` for `v9.87` while keeping active runtime count at 44.
- Keep README as current-state guidance with release details, not a changelog dump, and preserve existing detail.

### 4) Install, verify, push, release

- Install only README-listed active runtime rules into `/home/node/.claude/rules/`.
- Verify source/runtime parity for all 44 active runtime rule files.
- Commit, push `master`, and create GitHub release `v9.87`.
- Close phase, patch, TODO, changelog, and phase summary records after release verification passes.

---

## Out of Scope

- No new first-class runtime rule owner unless source evidence later proves existing ownership is insufficient.
- No changes to plugin/shared-board exact title grammar.
- No drift into `claude-session-coordination` package work.
- No mandatory Agent Team workflow for research lanes; standalone subagents remain the normal path for independent research.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.

---

## Affected Artifacts

### Primary runtime rule chain

- `native-worker-agent-routing-and-context-control.md`
- `design/native-worker-agent-routing-and-context-control.design.md`
- `changelog/native-worker-agent-routing-and-context-control.changelog.md`

### Adjacent runtime rule chains

- `external-verification-and-source-trust.md`
- `execution-continuity-and-mode-selection.md`
- `todo-standards.md` if tracking-friction wording is required

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/subagent-research-orchestration-and-leader-context-optimization.patch.md`
- `phase/phase-081-02-subagent-research-orchestration-and-leader-context-optimization.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P081-02 as active during source sync and completed only after source audit, runtime install parity, git push, and GitHub release pass.
- `changelog/changelog.md` records `v9.87` as the master version authority when the wave completes.
- Touched chain changelogs record their local version bumps.
- README presents current-state guidance, release details, and unchanged 44-rule install scope.

---

## Development Verification / TestKit Coverage

This phase changes governance/runtime-rule text rather than product code. No TestKit scenario is required. Verification is document/runtime parity and semantic scenario review:

- broad design-improvement web research should decompose into focused research lanes
- standalone subagent lanes remain preferred before Agent Team escalation
- leader receives analyzed findings rather than raw search dumps
- leader verifies final claims and resolves source conflicts
- task tracking friction does not collapse worker routing when tracking is non-material or can be repaired

---

## Verification

- [x] Native-worker research orchestration wording is added and version-aligned.
- [x] External verification, execution continuity, and TODO companion integrations are synchronized where touched.
- [x] Master records describe `v9.87` with unchanged 44 active runtime rules.
- [x] README Bash and PowerShell install arrays still include exactly 44 active runtime files.
- [x] Runtime install parity passes for 44 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.87` is created.

---

## Exit Criteria

- Research orchestration semantics are active in the native-worker routing chain.
- Adjacent owner integrations are synchronized and version-aligned.
- Master records describe `v9.87` consistently.
- Active runtime count remains 44.
- Runtime install parity passes for 44 active runtime rule files.
- Source/runtime release artifacts are pushed and released as `v9.87`.

---

## Closeout Summary

P081-02 delivered subagent research orchestration inside the existing native-worker routing family, so broad research/design-improvement/source-heavy recommendation work now gets mapped into focused research lanes before leader raw source absorption.

Feature / Improvement: leader responsibilities now include research objective and lane mapping, while subagent handoffs preserve checked scope, source quality, conflicts, implications, evidence limits, and leader verification needs.

Impact: future broad research requests can use subagents for more coverage and lower leader context load without weakening source-trust, evidence-calibration, or direct-handling exceptions for trivial work.

Verification basis: touched owner chains are version-aligned, master records are synchronized for v9.87, README Bash and PowerShell install arrays contain the same 44 active runtime files, runtime install parity verified 44/44 with destination extras observed-only, and source/runtime release artifacts are pushed and released as `v9.87`.

Next phase state: none opened.

---

## Risks and Rollback Notes

Risk:
- Research routing could become over-delegation for simple lookup work.

Mitigation:
- Preserve direct leader handling for trivial, exact, low-output, tightly sequential, or user-directed direct work.

Risk:
- Agent Team workflow could be overused when one standalone subagent is enough.

Mitigation:
- Keep standalone subagent-first wording and Agent Team escalation only for shared coordination needs.

Risk:
- Subagent search output could become raw dump instead of useful synthesis.

Mitigation:
- Require analyzed research handoffs with checked scope, source quality, conflicts, implications, and leader verification needs.

Rollback:
- Narrow or remove P081-02 research orchestration wording from the native-worker and adjacent chains.
- Keep P081-01 intent-first and standalone-subagent-first baseline intact unless separately rolled back.
- Reinstall the prior 44-rule runtime set only under a separate explicit rollback gate.

---

## Next Possible Phases

- None selected.
