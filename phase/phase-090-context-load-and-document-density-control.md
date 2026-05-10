# Phase 090 - Context Load and Document Density Control

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 090
> **Status:** In Progress
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:**
> - [../design/design.md](../design/design.md)
> - [../design/context-load-and-document-density-control.design.md](../design/context-load-and-document-density-control.design.md)
> - [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md)
> - [../design/safe-file-reading.design.md](../design/safe-file-reading.design.md)
> - [../design/governed-document-rollover-control.design.md](../design/governed-document-rollover-control.design.md)
> **Patch References:** [../patch/context-load-and-document-density-control.patch.md](../patch/context-load-and-document-density-control.patch.md)

---

## Objective

Add a RULES owner for context-load and document-density control. The goal is to prevent leader-session context overload by routing broad raw evidence through workers and by writing active docs in a shape that stays cheap to read, diff, edit, and verify later.

พูดง่าย ๆ: อ่านเยอะไม่ใช่ปัญหาเสมอไป แต่ leader ไม่ควรแบก raw content กว้าง ๆ เอง และ docs ไม่ควรถูกเขียนเป็นบรรทัดยักษ์ที่ทำให้รอบถัดไป context พัง.

---

## Why This Phase Exists

The checked NodeClaw evidence showed a real context-load failure pattern:
- multiple bounded governance reads combined into a large aggregate burst
- some small-looking line ranges were high-density because single markdown lines were thousands of characters
- active summary lines carried version history, current state, verification, caveats, and exclusions in one line
- compact/thrash happened after restored context plus broad raw reads refilled the window quickly

This is a new major phase because it adds a first-class runtime owner for context-load lifecycle and document-density strategy. It is related to safe reading and worker routing, but it is not only a read-limit refinement.

---

## Entry Conditions

- P089 / v9.96 governed design sharding compact-index release is complete, installed, pushed, and released.
- Active runtime count before this phase is 46.
- The user explicitly requested RULES improvement, runtime install, design/changelog/TODO/phase/patch sync, git push, release, and systematic phase planning.
- NodeClaw files are evidence for RULES behavior only; this phase does not edit NodeClaw project files.

---

## Expected Output

- New runtime rule `context-load-and-document-density-control.md` exists with substantive behavior body.
- New design and changelog companions exist at v1.0.
- README Bash and PowerShell install arrays include 47 source-owned active runtime files.
- Master design/changelog/TODO/phase/patch records align to v9.97 / P090.
- Runtime install copies only README-listed active runtime rules.
- Source/runtime parity and active runtime body sufficiency pass for 47/47 files.
- Git `master` push and GitHub release `v9.97` are verified.

---

## Implementation Plan

### 1) Open governed execution records

- Create this P090 phase record.
- Create `patch/context-load-and-document-density-control.patch.md` as the before/after review surface.
- Track P090 in `TODO.md` and `phase/SUMMARY.md` until release gates pass.

### 2) Add context-load owner chain

- Create `context-load-and-document-density-control.md` v1.0.
- Create `design/context-load-and-document-density-control.design.md` v1.0.
- Create `changelog/context-load-and-document-density-control.changelog.md` v1.0.

### 3) Sync master records

- Update `design/design.md` to v9.97 with active runtime count 47.
- Update `changelog/changelog.md` with v9.97 history.
- Update `README.md` current-state cards, latest refinement, install arrays, verification guidance, and footer as needed.
- Update `TODO.md`, `phase/SUMMARY.md`, this phase record, and the P090 patch.

### 4) Verify, install, push, and release

- Verify README Bash and PowerShell install arrays contain the same 47 files.
- Verify the new rule/design/changelog chain aligns at v1.0.
- Install only README-listed active runtime rules into `/home/node/.claude/rules/`.
- Verify source/runtime parity and body sufficiency for all 47 active runtime files.
- Run a density-oriented check on touched active docs.
- Commit the governed changes.
- Push `master`.
- Publish and verify GitHub release `v9.97`.

---

## Out of Scope

- No direct edits to NodeClaw files.
- No deletion or cleanup of runtime destination extras.
- No blanket post-compact ban on reading design/changelog/TODO/phase/patch.
- No replacement of `native-worker-agent-routing-and-context-control.md`, `safe-file-reading.md`, or rollover owners.
- No plugin/shared-board or external coordination runtime changes.

---

## Affected Artifacts

### New runtime owner chain

- `context-load-and-document-density-control.md`
- `design/context-load-and-document-density-control.design.md`
- `changelog/context-load-and-document-density-control.changelog.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/context-load-and-document-density-control.patch.md`
- `phase/phase-090-context-load-and-document-density-control.md`

### Runtime destination

- `/home/node/.claude/rules/context-load-and-document-density-control.md`
- Existing destination extras remain observed-only and out of cleanup scope.

---

## TODO and Changelog Coordination

- `TODO.md` records P090 as active during source sync and completed only after source audit, runtime install parity/body sufficiency, git push, and release pass.
- `changelog/changelog.md` records v9.97 as current source version during P090 and uses final release wording only after runtime install, push, and release gates pass.
- README presents current-state guidance and latest refinement context, not a copied changelog timeline.

---

## Development Verification / TestKit Coverage

This is governance and runtime-rule work, not product code.

Verification route:
- `not_applicable_with_reason` for product TestKit because no product runtime behavior changes.
- Source/runtime parity and active runtime body sufficiency are the main runtime checks.
- README install-array parity and density checks are required closeout checks.

---

## Verification

- [x] Phase and patch records exist and link correctly.
- [x] New runtime/design/changelog owner chain exists at v1.0.
- [x] Master records describe v9.97 / P090 consistently.
- [x] README Bash and PowerShell install arrays include exactly 47 active runtime rule files.
- [x] Runtime install copies only README-listed active runtime rules.
- [x] Source/runtime parity passes for 47 active runtime files.
- [x] Active runtime body sufficiency passes for 47 active runtime files.
- [x] Touched active docs pass a density-oriented check.
- [ ] `master` push and GitHub release `v9.97` are verified.

---

## Exit Criteria

- Context-load and document-density doctrine is installed as an active runtime owner.
- P090 phase and patch records are synchronized.
- Master records describe v9.97 consistently.
- Active runtime count is 47.
- Source consistency, runtime parity, body sufficiency, and density gates pass.
- Source/runtime release artifacts are pushed and released as `v9.97`.

---

## Risks and Rollback Notes

Risk:
- The new rule could be misread as “never read much” instead of “route broad raw reads correctly.”

Mitigation:
- State that reading a lot can be valid, but broad raw absorption should usually happen in worker lanes.

Risk:
- The rule could become a blunt post-compact restriction.

Mitigation:
- Frame compact/thrash as a repair signal for document structure and workflow.

Risk:
- Density checks could become mechanical line-length policing.

Mitigation:
- Treat long lines as repair triggers and inspect responsibility mixing before restructuring.

Rollback:
- Narrow or remove P090 doctrine through a governed rollback if it overreaches.
- Restore prior v9.96 master records only through governed rollback.
- Reinstall the prior 46-file runtime set only under an explicit rollback gate.
- Do not delete runtime destination extras or NodeClaw evidence files as cleanup.

---

## Next Possible Phases

- None selected during P090 execution.
