# Phase 085-01 - Status, Documentation, Memory, and Public-Surface Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 085-01
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/development-verification-and-debug-strategy.design.md](../design/development-verification-and-debug-strategy.design.md), [../design/memory-governance-and-session-boundary.design.md](../design/memory-governance-and-session-boundary.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/document-changelog-control.design.md](../design/document-changelog-control.design.md), [../design/native-worker-agent-routing-and-context-control.design.md](../design/native-worker-agent-routing-and-context-control.design.md), [../design/runtime-topology-control.design.md](../design/runtime-topology-control.design.md), [../design/natural-professional-communication.design.md](../design/natural-professional-communication.design.md), [../design/audience-surface-disclosure-control.design.md](../design/audience-surface-disclosure-control.design.md)
> **Patch References:** [../patch/status-doc-memory-surface-refinement.patch.md](../patch/status-doc-memory-surface-refinement.patch.md)

---

## Objective

Refine RULES behavior from checked memory-driven work patterns without adding the excluded post-compact/resume gate: clarify readiness-versus-completion wording, keep README sync current-state-oriented instead of changelog-dump-oriented, add memory index overflow maintenance triggers, require mechanism-first coordination design, and add a direct-user-transparent audience/public-surface disclosure owner.

พูดง่าย ๆ: งานนี้ทำให้ AI พูดสถานะให้ตรงหลักฐาน, sync README ให้เป็นหน้าปัจจุบัน, ดูแล MEMORY.md ไม่ให้กลายเป็นหนังสือทั้งเล่ม, ไม่ออกแบบ coordination จากกลไกที่ยังไม่ได้พิสูจน์, และไม่เอาข้อมูล internal ไปโชว์ใน public/generated surface ผิดที่ โดยยังต้องโปร่งใสกับ user เจ้าของงานเต็มที่.

---

## Current Goal / Output / Gate

- **Goal:** add the selected P085-01 refinements to the active RULES runtime and governed records.
- **Output:** synchronized runtime/design/changelog/TODO/phase/patch/README/master records for v9.91, with `audience-surface-disclosure-control.md` added as an active runtime rule if validation passes.
- **Gate:** source consistency, README install arrays, source/runtime install parity, active runtime body sufficiency, final governance audit, git push, and GitHub release `v9.91` pass.

---

## Runtime Active Rule Changes

- [x] Update `accurate-communication.md` so readiness/completion/status wording uses a clearer evidence ladder and direct-user transparency is not weakened by public-surface disclosure control.
- [x] Update `development-verification-and-debug-strategy.md` so coding/runtime closeout distinguishes prepared, configured, implemented, tested, verified, live-verified, fixed, and stable states.
- [x] Update `memory-governance-and-session-boundary.md` so root `MEMORY.md` loader warnings, truncation risk, and index bloat are maintenance signals with compact-index recovery guidance.
- [x] Update `project-documentation-standards.md` so README release sync updates current sections and current quality/install/status signals instead of dumping changelog history.
- [x] Update `document-changelog-control.md` so changelog remains the history/timeline layer and README remains the current front page.
- [x] Update `native-worker-agent-routing-and-context-control.md` so broad coordination-design work classifies the actual mechanism before proposing behavior.
- [x] Update `runtime-topology-control.md` so coordination/runtime mechanism classification separates passive board, hook, injected context, tmux transport, recall, official team, and external plugin/MCP mechanisms before mutation/design claims.
- [x] Update `natural-professional-communication.md` to v1.3 and align with direct-user-transparent, audience-aware wording boundaries.
- [x] Create `audience-surface-disclosure-control.md` as the first-class owner for direct-user transparency plus public/operator/customer/generated-surface disclosure minimization.

---

## Development Docs / Governed Record Sync

- [x] Create and sync `design/audience-surface-disclosure-control.design.md` and `changelog/audience-surface-disclosure-control.changelog.md`.
- [x] Sync paired design/changelog chains for all touched runtime owners.
- [x] Sync `design/design.md` and `changelog/changelog.md` for v9.91.
- [x] Sync `README.md` current-state sections and install arrays for the active runtime count.
- [x] Sync `TODO.md` active/completed work and verification lines.
- [x] Sync `phase/SUMMARY.md` with P085-01 lineage and active runtime count changes.
- [x] Keep destination extras such as `shared-task-list-path-coordination.md` and `team-agent-coordination.md` observed-only.

---

## Out of Scope

- Enforcing or redesigning Claude Code post-compact/resume behavior.
- Hiding verified internal/project details from the direct authorized user or project owner.
- Moving plugin/shared-board exact grammar into Main RULES doctrine.
- Managing, deleting, or classifying runtime destination files outside the source-owned active runtime install set.
- Treating memory review output as current repo truth without rechecking current RULES surfaces.

---

## Development Verification / TestKit Coverage

This is RULES governance/runtime-doctrine work, not product code. The verification route is source consistency, runtime install parity, body-sufficiency validation, and release-surface audit rather than TestKit scenario creation.

Verification route:
- `not_applicable_with_reason` for code TestKit: no executable product behavior is changed
- `source_consistency`: rule/design/changelog version alignment and master surface sync
- `runtime_parity`: README-listed active runtime files copied to `~/.claude/rules/` with hash parity
- `body_sufficiency`: no README-listed active runtime file is metadata-only
- `release_audit`: git push and GitHub release verification

---

## Verification

- [x] Runtime owners contain the selected readiness/completion, README sync, memory index hygiene, mechanism-first coordination, and audience disclosure guidance.
- [x] Direct-user transparency is preserved and public/generated-surface disclosure minimization is scoped to audience surfaces.
- [x] Post-compact/resume gate behavior is not added back into scope.
- [x] Companion design and changelog chains are updated for touched owners.
- [x] Master README/design/changelog/TODO/phase records reflect v9.91 and P085-01.
- [x] README Bash and PowerShell active runtime arrays match and include the correct active runtime count.
- [x] Runtime install copies only README-listed active runtime rules.
- [x] Source/runtime parity and body-sufficiency checks pass for all active runtime files.
- [x] Other-owner runtime destination files remain observed-only and untouched.
- [x] Git push and GitHub release `v9.91` are verified.

---

## Exit Criteria

- P085-01 runtime owner updates are complete.
- Companion design/changelog records are synchronized.
- Master README/design/changelog/TODO/phase records are synchronized.
- Runtime install/parity/body-sufficiency checks pass for the active runtime set.
- No post-compact/resume control doctrine is introduced.
- No direct-user transparency restriction is introduced.
- `master` is pushed and GitHub release `v9.91` exists.

---

## Risks and Rollback Notes

Risk: audience-surface disclosure could be misread as hiding information from the direct user.

Risk: README sync rules could over-constrain normal README maintenance instead of targeting release/current-state sync.

Risk: mechanism-first coordination guidance could drift into plugin-specific shared-board doctrine.

Rollback posture: narrow or revert only the P085-01 refinements and the new audience-surface owner if it proves unnecessary; preserve P075 goal-first behavior, P081 worker routing, P084 development verification, P073 body-sufficiency gates, and the source-owned runtime install boundary unless separately challenged.

---

## Next Possible Phases

No next phase is selected by this phase. If later usage shows the audience-surface disclosure owner is too broad or too quiet, a future P085-02 threshold-tuning phase can refine audience classes and artifact triggers without weakening direct-user transparency.
