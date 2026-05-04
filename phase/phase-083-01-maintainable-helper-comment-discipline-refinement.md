# Phase 083-01 - Maintainable Helper and Comment Discipline Refinement

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 083-01
> **Status:** In Progress
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/maintainable-code-structure-and-decomposition.design.md](../design/maintainable-code-structure-and-decomposition.design.md)
> **Patch References:** [../patch/maintainable-helper-comment-discipline-refinement.patch.md](../patch/maintainable-helper-comment-discipline-refinement.patch.md)

---

## Objective

Refine the maintainable code structure owner so AI coding work avoids both under-decomposition and over-decomposition: no unnecessary God functions/files, no unnecessary helper-function inflation, and useful source-code comments when code needs explanation of purpose, process, constraints, side effects, or business rules.

พูดง่าย ๆ: code ต้องอ่านง่ายและแก้ต่อได้จริง แต่ไม่ใช่แตก helper ทุกอย่างหรือใส่ comment ทุกบรรทัดเพื่อให้ดูดี.

---

## Why This Phase Exists

P082 added the first-class maintainable code structure owner. The user then identified two practical gaps:
- avoiding God functions/files can accidentally push AI into too many tiny helper functions
- clean code still needs appropriate comments when business/process context is not obvious from names and structure

Supporting research and RULES overlap analysis found the best owner is the existing `maintainable-code-structure-and-decomposition.md` chain, not a new rule.

---

## Entry Conditions

- P082/v9.81 is complete, installed, pushed, and released.
- Active runtime count is 43.
- `maintainable-code-structure-and-decomposition.md` exists as the coding-time structure owner.
- User explicitly requested source refinement, runtime install, governed docs sync, git push, and release.

---

## Implementation Plan

### 1) Refine maintainable code structure owner

- Update runtime/design/changelog from v1.0 to v1.1.
- Add helper-function necessity guidance.
- Add guardrails against trivial helpers and pass-through helper chains.
- Add source-code comment discipline.
- Add comment spam and stale-comment smell triggers.
- Preserve no hard line-count and no template-doctrine posture.

### 2) Sync governed records

- Update `design/design.md` to v9.82 while preserving active runtime count 43.
- Update `changelog/changelog.md` with v9.82.
- Update `README.md` current-state guidance and maintainable-code rule description without changing install arrays.
- Update `TODO.md` durable tracking.
- Update `phase/SUMMARY.md` with phase 083.
- Keep this phase record and P083 patch synchronized.

### 3) Runtime install, release, and verification path

- Run source consistency audit.
- Install only README-listed 43 active runtime rule files into `/home/node/.claude/rules/`.
- Verify source/runtime hash parity for the 43 active runtime rules.
- Commit source changes.
- Push to `origin/master`.
- Create GitHub release `v9.82`.
- Close out phase/patch/TODO/README/changelog records only after release verification passes.

---

## Out of Scope

- No new active runtime rule file.
- No active runtime count increase.
- No broad rewrite of P082's maintainability doctrine.
- No mandatory helper extraction or mandatory inline-only doctrine.
- No comment-every-line doctrine.
- No replacement of governed design/spec documentation with source comments.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.
- No memory update for this RULES development wave.

---

## Affected Artifacts

### Refined active runtime rule chain

- `maintainable-code-structure-and-decomposition.md`
- `design/maintainable-code-structure-and-decomposition.design.md`
- `changelog/maintainable-code-structure-and-decomposition.changelog.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/maintainable-helper-comment-discipline-refinement.patch.md`
- `phase/phase-083-01-maintainable-helper-comment-discipline-refinement.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P083 as active during source sync and completed only after source audit, runtime install parity, git push, and GitHub release pass.
- `changelog/changelog.md` records v9.82 as the master version authority.
- The maintainable-code chain changelog records v1.1.
- README presents current-state guidance and active install scope, not a detailed changelog dump.

---

## Verification

- [x] `maintainable-code-structure-and-decomposition` runtime/design/changelog updated and audited at v1.1.
- [x] Master records describe v9.82 and active runtime count 43 consistently.
- [ ] README Bash and PowerShell install arrays still include exactly 43 active runtime rule files.
- [ ] Golden scenarios pass for no helper around trivial expression, useful helper extraction, comment usefulness, no comment spam, stale comment cleanup, and maintained God function/file boundaries.
- [x] Runtime install parity passes for 43 active runtime rule files.
- [ ] Source/runtime release artifacts are pushed and released as `v9.82`.

---

## Closeout Summary

Pending until source sync, runtime install parity, git push, and GitHub release `v9.82` pass.

---

## Exit Criteria

- Maintainable code structure runtime, design, and changelog versions align at v1.1.
- Master records describe v9.82 consistently.
- Active runtime count remains 43.
- P083 phase and patch records exist and link correctly.
- Final source audit passes.
- Runtime install parity passes for the 43 active runtime rule files.
- Source/runtime release artifacts are pushed and released as `v9.82`.

---

## Risks and Rollback Notes

Risk:
- Helper guidance could be overread as permission to keep unclear God functions.

Mitigation:
- Preserve God-function/God-file smell triggers and smallest-useful decomposition.

Risk:
- Comment guidance could become comment spam.

Mitigation:
- Keep comments focused on hidden purpose, process, constraints, side effects, external contracts, and business rules; remove syntax-repeating and stale comments.

Risk:
- Source comments could be treated as durable policy/spec authority.

Mitigation:
- Preserve `project-documentation-standards.md` as governed documentation owner and keep inline comments local.

Rollback:
- Narrow the v1.1 helper/comment wording through a governed rollback.
- Preserve P082 maintainability owner semantics unless a separate rollback retires or narrows them.
- Keep active runtime count at 43 unless a separate governed wave changes the active install set.
- Do not delete destination/runtime files outside the source-owned install set without separate explicit destructive authorization.

---

## Next Possible Phases

- None selected.
