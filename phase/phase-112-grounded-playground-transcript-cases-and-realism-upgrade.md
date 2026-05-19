# P112 — Grounded Playground Transcript Cases and Realism Upgrade

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P112
> **Status:** Completed / Released
> **Target Release:** v10.20
> **Design References:**
> - [../design/design.md](../design/design.md) v10.20
> - [../design/design/playground-architecture.design.md](../design/design/playground-architecture.design.md) v10.20
> **Patch References:** [../patch/grounded-playground-transcript-cases-and-realism-upgrade.patch.md](../patch/grounded-playground-transcript-cases-and-realism-upgrade.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Upgrade the governed `playground/` family so it includes new observed cases grounded in real Claude Code session JSONL transcripts on this machine, richer multi-turn scenario dialogues, stronger flow explanations, and broader scenario diversity while keeping the family non-runtime and evidence-calibrated.

---

## Why This Phase Exists

The released `v10.19 / P111` wave established the playground baseline, but the first scenario set is still too idealized.

That leaves four realism gaps:
- many scenarios still rely on clean one-turn dialogues rather than the messy multi-turn shape of real Claude Code work
- several observed sections still lack transcript-grounded examples from actual sessions on this machine
- the current families do not yet cover enough claim-audit / workflow-block / evidence-boundary patterns from real usage
- the matrix and template still need stronger realism cues such as user correction, partial evidence, blockers, retries, and tool-driven discovery

P112 exists to upgrade the playground from rule-complete baseline into a more realistic and transcript-grounded behavior library.

---

## Expected Output

- `playground/observed/2026-05.md` includes new transcript-derived observed entries with exact checked transcript paths and anchor hints.
- existing scenario files are upgraded with richer multi-turn prompt/response traces and stronger flow diagrams.
- the playground template supports realistic multi-turn traces and transcript-anchor recording.
- the matrix includes stronger realism axes such as turn count, user behavior, evidence source, failure mode, tool discovery, and completion state.
- at least two new grounded scenario-family files exist if the checked transcript evidence justifies opening them.
- the active runtime install set remains 18 and `playground/` stays outside the runtime install payload.

---

## Action Checklist

- [x] Confirm released baseline is `v10.19 / P111` with no active phase open.
- [x] Confirm `v10.20` / `P112` are absent in checked scope.
- [x] Update the playground architecture design for transcript-grounded observed cases and realism upgrades.
- [x] Update the playground template for realistic multi-turn traces.
- [x] Add transcript-derived observed entries from checked session JSONL transcripts.
- [x] Upgrade existing scenario files with richer multi-turn examples where the checked evidence supports them.
- [x] Add new scenario-family files only where checked transcript evidence shows a real uncovered pattern.
- [x] Sync touched README/design/changelog/TODO/phase/patch/playground surfaces to the P112 source-release state.
- [x] Verify all updated observed cases remain factual, scoped, and anchored to exact transcript paths plus search hints.
- [x] Verify `playground/` remains outside the runtime install payload and `git diff --check` passes.
- [x] Commit source release, push `master`, create GitHub release `v10.20`, and verify release state.
- [x] Finalize P112 closeout records after release verification passes.

---

## Out of Scope

- inventing observed incidents or unverified transcript storytelling
- broad README rewrite or turning README into the scenario owner
- expanding the active runtime install set beyond 18 root rules
- adding `playground/` to `.claude/rules/` installer payloads
- plugin-scope work or support-claim drift outside the selected playground realism goal
- adding Codex CLI or Gemini CLI support claims

---

## Completion Gate

- updated observed cases cite exact checked transcript paths and anchor hints
- updated scenarios still separate `rule-enforced fact`, `observed case`, and `virtual variant`
- updated scenarios now include richer multi-turn traces and stronger flow diagrams where relevant
- any new scenario families are justified by checked transcript evidence rather than convenience
- `playground/` remains outside the runtime install payload and the active runtime set remains 18
- `git diff --check` passes
- `master` push and GitHub release `v10.20` verification pass

---

## Current Status

P112 is completed and released for `v10.20`.

Completed delivery:
- the current released baseline advanced from `v10.19 / P111` to `v10.20 / P112`
- the grounded `playground/` upgrade now includes transcript-derived observed entries with exact checked transcript paths plus anchor hints
- the updated scenario set now uses richer multi-turn traces, stronger flow explanations, and two grounded new scenario families for completion-claim audit and workflow-blocked visual QA
- README pointer-only integration keeps the playground out of the runtime install payload while the active runtime set remains 18
- project-local install proof passed with 18/18 parity/body sufficiency and `playground/` remained outside `.claude/rules/`
- GitHub release `v10.20` is published at https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.20
- release tag `v10.20` resolves to commit `4851338417501a391e7dc505d0b049d7fb6209db` and was published at `2026-05-19T03:51:01Z`

Still pending:
- none
