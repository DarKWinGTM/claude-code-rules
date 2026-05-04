# Phase 082-01 - Maintainable Code Structure and Decomposition

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 082-01
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/maintainable-code-structure-and-decomposition.design.md](../design/maintainable-code-structure-and-decomposition.design.md), [../design/tactical-strategic-programming.design.md](../design/tactical-strategic-programming.design.md)
> **Patch References:** [../patch/maintainable-code-structure-and-decomposition.patch.md](../patch/maintainable-code-structure-and-decomposition.patch.md)

---

## Objective

Create a first-class RULES owner for maintainable code structure and decomposition so AI coding work avoids unnecessary God functions, God files, hidden dependencies, and wrong abstractions while staying principle-based and flexible.

พูดง่าย ๆ: ให้ AI เขียนโค้ดแบบอ่านง่าย แก้ง่าย test ง่าย โดยแยก responsibility เมื่อจำเป็นจริง ไม่ใช่แตกไฟล์หรือสร้าง architecture template แบบแข็ง ๆ.

---

## Why This Phase Exists

The existing `tactical-strategic-programming.md` rule is useful for deciding whether work is tactical, strategic, or tactical-with-strategic-track, but the user identified a more specific coding-time gap: AI should plan and structure code responsibly during implementation.

The user specifically wanted:
- no unnecessary God function / God file
- code split into good responsibility boundaries when useful
- a principle and concept model, not rigid inflexible rules
- research-grounded practical behavior
- integration with tactical/strategic programming without letting tactical/strategic absorb this whole concern

---

## Entry Conditions

- P081/v9.80 native worker routing refinement is complete, installed, pushed, and released.
- Focused research identified maintainability, code smells, separation of concerns, cohesion/coupling, wrong-abstraction caution, behavior-preserving refactor, and evolutionary architecture as useful grounding.
- The user requested RULES improvement, runtime install, governed docs sync, git push, and release.
- Active runtime rule count should increase from 42 to 43 because P082 adds one new first-class runtime rule.

---

## Implementation Plan

### 1) Create maintainable code structure owner

- Create `maintainable-code-structure-and-decomposition.md` v1.0.
- Create companion design and changelog at v1.0.
- Add maintainability-as-change-cost guidance.
- Add responsibility-by-reason-to-change guidance.
- Add code-smell trigger model without making smells automatic verdicts.
- Add smallest-useful-decomposition and wrong-abstraction guardrails.
- Add behavior-preserving refactor and verification-honesty guidance.

### 2) Integrate tactical/strategic boundary

- Update `tactical-strategic-programming.md` to v1.3.
- Update companion design and changelog to v1.3.
- Clarify that tactical/strategic owns convergence, while the new rule owns code responsibility and decomposition quality.
- Clarify tactical fixes may remain local but should not silently worsen God-function/God-file drift or leave material structure debt without a convergence path.

### 3) Master and governed record sync

- Update `design/design.md` to v9.81 and active runtime count 43.
- Update `changelog/changelog.md` with v9.81.
- Update `README.md` current-state guidance, rule list, and Bash/PowerShell install arrays to 43 active runtime files.
- Update `TODO.md` durable tracking.
- Update `phase/SUMMARY.md` with phase 082.
- Keep this phase record and P082 patch synchronized.

### 4) Runtime install, release, and verification path

- Run source consistency audit.
- Install only README-listed 43 active runtime rule files into `/home/node/.claude/rules/`.
- Verify source/runtime hash parity and keep destination markdown files outside the active install set observed-only.
- Commit source changes.
- Push to `origin/master`.
- Create GitHub release `v9.81`.

---

## Out of Scope

- No hard line-count limits for functions or files.
- No mandatory Clean Architecture, MVC, service/repository, controller/service/repository, or framework-specific template doctrine.
- No requirement to split every long function or large file.
- No project implementation work in this phase.
- No deletion or cleanup of runtime destination files outside the source-owned active install set.
- No memory update for this RULES development wave.

---

## Affected Artifacts

### New active runtime rule chain

- `maintainable-code-structure-and-decomposition.md`
- `design/maintainable-code-structure-and-decomposition.design.md`
- `changelog/maintainable-code-structure-and-decomposition.changelog.md`

### Touched adjacent runtime rule chain

- `tactical-strategic-programming.md`
- `design/tactical-strategic-programming.design.md`
- `changelog/tactical-strategic-programming.changelog.md`

### Master records and tracking files

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/maintainable-code-structure-and-decomposition.patch.md`
- `phase/phase-082-01-maintainable-code-structure-and-decomposition.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P082 as completed after source sync, source audit, runtime install parity, git push, and GitHub release pass.
- `changelog/changelog.md` records v9.81 as the master version authority.
- Per-chain changelogs record `maintainable-code-structure-and-decomposition` v1.0 and `tactical-strategic-programming` v1.3.
- README presents current-state guidance and active install scope, not a detailed changelog dump.

---

## Verification

- [x] `maintainable-code-structure-and-decomposition` v1.0 source/design/changelog created.
- [x] `tactical-strategic-programming` v1.3 source/design/changelog updated.
- [x] Master records describe v9.81 and active runtime count 43 consistently.
- [x] README Bash and PowerShell install arrays include exactly 43 active runtime rule files.
- [x] Golden semantic scenarios pass for God function/file triggers, no forced split for cohesive long code, smallest useful decomposition, wrong-abstraction avoidance, tactical convergence, behavior-preserving refactor, and verification-honest reporting.
- [x] Runtime install parity passes for 43 active runtime rule files.
- [x] Source/runtime release artifacts are pushed and released as `v9.81`.

---

## Closeout Summary

P082 delivered a first-class maintainable code structure and decomposition owner, integrated tactical/strategic convergence boundaries with that owner, synchronized v9.81 / 43-rule governance records, installed the README-listed runtime set, verified source/runtime parity, pushed master, and published GitHub release `v9.81`.

---

## Exit Criteria

- P082 new rule runtime, design, and changelog versions align.
- Tactical-strategic runtime, design, and changelog versions align at v1.3.
- Master records describe v9.81 consistently.
- Active runtime count becomes 43.
- P082 phase and patch records exist and link correctly.
- Final source audit passes.
- Runtime install parity passes for the 43 active runtime rule files.
- Source/runtime release artifacts are pushed and released as `v9.81`.

---

## Risks and Rollback Notes

Risk:
- Maintainability wording could be overread as rigid line-count policing.

Mitigation:
- Preserve smell-as-trigger-not-verdict and no hard line-count doctrine.

Risk:
- Decomposition guidance could cause overengineering.

Mitigation:
- Keep smallest-useful-decomposition, local clarity, and wrong-abstraction guardrails.

Risk:
- Tactical/strategic integration could blur ownership.

Mitigation:
- State the boundary explicitly: tactical/strategic owns convergence; maintainable code structure owns coding-time responsibility and decomposition quality.

Rollback:
- Remove the new rule from active install lists only through a governed rollback.
- Revert tactical-strategic v1.3 integration only if the new owner is retired or narrowed.
- Do not delete other runtime destination markdown files without separate explicit destructive authorization.

---

## Next Possible Phases

- None selected.
