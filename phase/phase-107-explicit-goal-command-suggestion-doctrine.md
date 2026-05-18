# P107 — Explicit Goal-Command Suggestion Doctrine

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P107
> **Status:** Active / In Progress
> **Target Release:** v10.15
> **Design References:**
> - [../design/design.md](../design/design.md) v10.15
> - touched owner design companions under [../design/](../design/)
> **Patch References:** [../patch/explicit-goal-command-suggestion-doctrine.patch.md](../patch/explicit-goal-command-suggestion-doctrine.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Strengthen RULES so AI can propose compact, high-signal Claude Code `/goal` commands when a bounded successor objective is clear, measurable, provable in transcript, and better surfaced as an advisory next-step command than as silent continuation or vague prose.

---

## Why This Phase Exists

The released `v10.14 / P106` wave clarified chronology/adherence around parent-model doctrine, but RULES still has no explicit doctrine for when to suggest the actual Claude Code `/goal` command.

The current RULES already knows how to express supported next goals, goal/output/gate framing, verification, and advisory proposals. The remaining gap is translation: AI still lacks an explicit rule for when to convert those governed surfaces into a compact `/goal` command, when not to do so, and how to keep that command within the 4000-character limit with transcript-visible proof.

---

## Expected Output

- RULES explicitly states when a `/goal` suggestion is appropriate.
- RULES explicitly states when the assistant should continue directly instead of suggesting `/goal`.
- RULES defines a compact `/goal` command shape based on outcome, proof, scope, hard guardrails, and stop bound.
- RULES defines how `/goal` suggestions are sourced from checked Goal/Output/Gate/Verification surfaces instead of being improvised.
- `/goal` suggestions remain advisory, not implied selected execution.
- `/goal` suggestions remain compact and high-signal rather than mini-spec dumps.
- Current active runtime install set remains exactly 18 root runtime files.
- Runtime install and source/runtime parity pass for 18/18 active rules.
- GitHub release `v10.15` is created and verified.

---

## Action Checklist

- [ ] Confirm current baseline is released `v10.14 / P106` with no active phase open before P107 startup.
- [ ] Confirm `v10.15` release/tag is not already present.
- [ ] Confirm README Bash and PowerShell arrays still define the same 18 active runtime files.
- [ ] Confirm the untracked `plugin/` tree remains preserved and out of scope.
- [ ] Open P107 phase/patch/changelog startup artifacts and sync active roadmap/TODO state.
- [x] Add `/goal` trigger and no-trigger doctrine in the touched runtime/design owners.
- [x] Add compact `/goal` output-shape doctrine in the closing/presentation owner.
- [x] Add `/goal` sourcing doctrine from Goal/Output/Gate/Verification surfaces.
- [x] Add advisory wording and high-signal pruning guards for `/goal` suggestions.
- [x] Sync touched owner design/changelog companions plus master release surfaces to P107 pre-release state.
- [x] Validate doctrine integrity, install scope, runtime install, and 18/18 parity/body sufficiency.
- [ ] Commit source release, push `master`, create GitHub release `v10.15`, and verify release state.
- [ ] Finalize P107 closeout records after release verification passes.

---

## Out of Scope

- Creating a new standalone runtime owner for `/goal`.
- Expanding the active runtime install scope away from 18 root rules.
- Reopening `plugin/` as an active edit or release scope for this wave.
- Treating `/goal` suggestions as selected execution by default.
- Suggesting `/goal` when RULES should continue directly.
- Relying on proof the `/goal` evaluator cannot judge from surfaced conversation.
- Deleting existing history/done/archive surfaces as cleanup.

---

## Completion Gate

- README Bash and PowerShell install arrays define exactly the same 18 active runtime files.
- Touched owner/runtime/design/changelog files align to `v10.15 / P107`.
- Active doctrine explicitly states when `/goal` should be suggested and when it should not.
- Active doctrine explicitly defines a compact `/goal` command shape based on outcome, proof, scope, hard guardrails, and stop bound.
- Active doctrine explicitly defines that `/goal` suggestions are sourced from checked Goal/Output/Gate/Verification surfaces.
- `/goal` suggestions remain advisory and high-signal.
- Current P106 chronology/adherence doctrine remains intact.
- `TODO.md` and `phase/SUMMARY.md` remain compact active entrypoints with reachable `history/` / `done/` references.
- Runtime install copies only the 18 README-listed active runtime rules.
- 18/18 source/runtime parity and source/destination body sufficiency pass.
- `shared-task-list-path-coordination.md` remains observed-only and outside the source-owned install set.
- `master` push and GitHub release `v10.15` verification pass.

---

## Current Status

P107 is active in pre-release implementation for `v10.15`.

Completed so far:
- the current released baseline is `v10.14 / P106`
- no active phase is open before P107 startup
- `v10.15` tag/release is absent in checked scope
- the current 18-rule runtime install scope remains intact in README arrays
- the untracked `plugin/` tree remains preserved as out-of-scope observed evidence
- P107 phase/patch/changelog startup plus active roadmap/TODO sync are open in source scope
- `/goal` trigger doctrine, command-shape doctrine, sourcing/writing doctrine, and pruning/writing guards are complete in source scope
- runtime install plus 18/18 source/runtime parity and source/destination body sufficiency passed locally
- `git diff --check` passed with no whitespace errors so far

Still pending:
- source release commit, push, and GitHub release verification
- final closeout after release verification
