# P111 — RULES Playground Behavior Scenarios

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** P111
> **Status:** Completed / Released
> **Target Release:** v10.19
> **Design References:**
> - [../design/design.md](../design/design.md) v10.19
> - [../design/design/playground-architecture.design.md](../design/design/playground-architecture.design.md) v10.19
> **Patch References:** [../patch/rules-playground-behavior-scenarios.patch.md](../patch/rules-playground-behavior-scenarios.patch.md)
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [../changelog/changelog.md](../changelog/changelog.md)

---

## Objective

Establish a governed `playground/` family that shows how current RULES change AI behavior in practice through 10 scenario families, a full 18-rule coverage map, a virtual-case matrix, and an ongoing observed-case update path.

---

## Why This Phase Exists

The current README still has a high-level `Before & After` surface, but it is not the right owner for a growing set of grounded behavior scenarios.

That gap creates four problems:
- README would become noisy if detailed scenario material keeps being appended there
- checked rule behavior, observed examples, and virtual illustrations could get mixed together too loosely
- it is hard to show that all 18 active runtime rules are covered without a dedicated matrix surface
- future observed cases have no governed place to accumulate over time

P111 exists to open a governed non-runtime family that demonstrates RULES behavior impact more precisely while keeping the active runtime install set unchanged.

---

## Expected Output

- `design/design/playground-architecture.design.md` exists and governs the playground family.
- `playground/README.md` exists as the family entrypoint.
- `playground/coverage.md` maps all 18 active runtime rules to at least one scenario family.
- `playground/matrix.md` defines a virtual-case matrix with several decision axes.
- `playground/templates/case-template.md` defines the case shape for future additions.
- `playground/observed/2026-05.md` exists as the current monthly observed log.
- 10 scenario-family case files exist under `playground/cases/`.
- `README.md` keeps only a compact pointer to the playground family.
- `playground/` stays outside the runtime install payload and the active runtime set remains 18.

---

## Action Checklist

- [x] Confirm released baseline is `v10.18 / P110` with no active phase open.
- [x] Confirm `v10.19` / `P111` are absent in checked scope.
- [x] Create the dedicated playground architecture design shard.
- [x] Create the playground family baseline files.
- [x] Create 10 grounded scenario-family case files.
- [x] Add a compact playground pointer into `README.md` without broad rewrite.
- [x] Sync touched design/changelog/TODO/phase/patch surfaces to the P111 source-release state.
- [x] Verify all 18 runtime rules are covered by at least one scenario family.
- [x] Verify each scenario visibly separates `rule-enforced fact`, `observed case`, and `virtual variant`.
- [x] Verify `playground/` remains outside the runtime install payload and `git diff --check` passes.
- [x] Commit source release, push `master`, create GitHub release `v10.19`, and verify release state.
- [x] Finalize P111 closeout records after release verification passes.

---

## Out of Scope

- Expanding the active runtime install scope beyond 18 root rules.
- Adding `playground/` to `.claude/rules/` installer payloads.
- Inventing observed incidents that are not supported by checked repo/work history.
- Rewriting README into a scenario dump.
- Plugin-specific work or support-claim drift outside the selected playground goal.
- Adding Codex CLI or Gemini CLI support claims.

---

## Completion Gate

- The baseline playground file set exists at the selected paths.
- 10 scenario-family files exist under `playground/cases/`.
- Every scenario visibly separates `rule-enforced fact`, `observed case`, and `virtual variant`.
- All 18 active runtime rules are covered by at least one scenario family.
- The virtual-case matrix covers several explicit axes such as request type, evidence state, scope clarity, risk, and expected rule response.
- README keeps only a compact playground pointer.
- `playground/` remains outside the runtime install payload and the active runtime count remains 18.
- `git diff --check` passes.
- `master` push and GitHub release `v10.19` verification pass.

---

## Current Status

P111 is completed and released for `v10.19`.

Completed delivery:
- the current released baseline advanced from `v10.18 / P110` to `v10.19 / P111`
- the governed non-runtime `playground/` family now exists with 10 scenario-family files, coverage/matrix surfaces, an observed log, and a reusable template
- each scenario now separates `rule-enforced fact`, `observed case`, and `virtual variant`, and also includes prompt/response examples plus a lightweight flow diagram
- README pointer-only integration keeps the playground out of the runtime install payload while the active runtime set remains 18
- project-local install proof passed with 18/18 parity/body sufficiency and `playground/` remained outside `.claude/rules/`
- GitHub release `v10.19` is published at https://github.com/DarKWinGTM/claude-code-rules/releases/tag/v10.19
- release tag `v10.19` resolves to commit `e3e0bdfe255c2370085abcfebbb25a6544de9a1b` and was published at `2026-05-19T01:39:59Z`

Still pending:
- none
