# Phase 073-10 - Active Runtime Body Sufficiency Corrective Validation

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-10
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md), [../design/unified-version-control-system.design.md](../design/unified-version-control-system.design.md), [../design/project-documentation-standards.design.md](../design/project-documentation-standards.design.md), [../design/document-consistency.design.md](../design/document-consistency.design.md)
> **Patch References:** [../patch/active-runtime-body-sufficiency-corrective-validation.patch.md](../patch/active-runtime-body-sufficiency-corrective-validation.patch.md)

---

## Objective

Repair active runtime rule body sufficiency after discovering that several README-listed active runtime files were installed as metadata-only stubs instead of substantive runtime behavior contracts.

พูดง่าย ๆ: ไฟล์ root runtime rule ต้องเป็นกฎที่ runtime อ่านแล้วใช้ได้จริง ไม่ใช่แค่หัวไฟล์ที่ชี้ไปหา design.

---

## Why This Phase Exists

P073 runtime install/parity work proved source-to-runtime hash parity, but the checked evidence showed parity can pass even when the source-owned active runtime file is semantically empty. The issue is visible in 10 active runtime files that are listed in README install arrays and master active runtime inventory but contain only title/version/design/session metadata.

This phase exists to restore the correct runtime/design/changelog triad:

```text
root runtime rule = active behavior contract
Design file = target-state / rationale authority
Changelog = version and history authority
```

---

## Entry Conditions

- P073 runtime install/parity lineage exists.
- v9.87 active runtime install parity verified 44/44, but body sufficiency was not part of the parity gate.
- User identified `unified-version-control-system.md` as an abnormal active runtime file because it contains only a design link and metadata.
- Investigation confirmed 10 metadata-only active runtime files.
- User requested fixing all files with this abnormality.

---

## Implementation Plan

### 1) Materialize active runtime bodies

Restore substantive runtime bodies for:

- `anti-mockup.md`
- `dan-safe-normalization.md`
- `emergency-protocol.md`
- `flow-diagram-no-frame.md`
- `recovery-contract.md`
- `refusal-classification.md`
- `refusal-minimization.md`
- `safe-file-reading.md`
- `safe-terminal-output.md`
- `unified-version-control-system.md`

Each root runtime file must include canonical metadata with `Full history` and a body containing at minimum a rule statement, operational contract, verification/checklist or metrics, and integration/boundary guidance.

### 2) Synchronize rule chain companions

Update design and changelog companions for the 10 repaired chains, keeping design as active target-state truth and changelog as version/history authority.

### 3) Add active runtime body-sufficiency validation doctrine

Update `unified-version-control-system`, `project-documentation-standards`, and `document-consistency` so active runtime parity cannot pass from metadata-only root files.

### 4) Sync master records

Update `design/design.md`, `changelog/changelog.md`, `README.md`, `TODO.md`, and `phase/SUMMARY.md` for v9.88 / P073-10 with active runtime count unchanged at 44.

### 5) Install, verify, push, release

Install only README-listed active runtime files to `/home/node/.claude/rules/`, verify 44/44 source/runtime parity and no metadata-only active runtime files, then commit, push `master`, and create GitHub release `v9.88`.

---

## Out of Scope

- No new active runtime rule count increase.
- No deletion of destination/runtime extras such as `shared-task-list-path-coordination.md` or `team-agent-coordination.md`.
- No migration of design bodies into historical dumps.
- No rollback to old `Based on:` headers.
- No plugin/shared-board coordination doctrine changes.

---

## Affected Artifacts

### Runtime bodies

- `anti-mockup.md`
- `dan-safe-normalization.md`
- `emergency-protocol.md`
- `flow-diagram-no-frame.md`
- `recovery-contract.md`
- `refusal-classification.md`
- `refusal-minimization.md`
- `safe-file-reading.md`
- `safe-terminal-output.md`
- `unified-version-control-system.md`

### Companion chains

- `design/<rule>.design.md` for each repaired rule
- `changelog/<rule>.changelog.md` for each repaired rule
- `project-documentation-standards.md`, design, and changelog
- `document-consistency.md`, design, and changelog

### Master records

- `design/design.md`
- `changelog/changelog.md`
- `README.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/active-runtime-body-sufficiency-corrective-validation.patch.md`

---

## TODO and Changelog Coordination

- `TODO.md` records P073-10 as completed after source body-sufficiency checks, runtime install parity, git push, and GitHub release pass.
- `changelog/changelog.md` records `v9.88` as the master release when the wave completes.
- Each repaired chain changelog records its local body materialization version.
- README stays current-state guidance and release details, not a changelog dump.

---

## Development Verification / TestKit Coverage

This phase changes governance/runtime-rule text rather than product code. No TestKit scenario is required. Verification is source/runtime body-sufficiency and parity review:

- every README-listed active runtime file exists
- active runtime count remains 44
- every active runtime file has `Full history`
- no README-listed active runtime file is metadata-only
- repaired runtime files have substantive rule bodies
- source/runtime parity passes for all 44 active runtime files
- destination extras remain observed-only

---

## Verification

- [x] P073-10 phase and patch records are opened.
- [x] The 10 metadata-only active runtime files are materialized into substantive bodies.
- [x] The 10 repaired rule/design/changelog chains are version-aligned.
- [x] Body-sufficiency validation doctrine is added to the governance owners.
- [x] Master records describe v9.88 with unchanged 44 active runtime rules.
- [x] README Bash and PowerShell install arrays include exactly 44 active runtime files.
- [x] Source body-sufficiency audit passes for all README-listed active runtime files.
- [x] Runtime install parity passes 44/44 with no metadata-only active runtime files.
- [x] Source/runtime release artifacts are pushed and GitHub release `v9.88` is created.

---

## Exit Criteria

- All README-listed active runtime files have substantive runtime bodies.
- The root runtime/design/changelog role split is restored.
- Active runtime count remains 44.
- Body-sufficiency validation is documented so parity cannot hide metadata-only stubs.
- Runtime install parity passes 44/44.
- Source/runtime release artifacts are pushed and released as `v9.88`.

---

## Risks and Rollback Notes

Risk:
- Restoring old body wording could reintroduce stale doctrine.

Mitigation:
- Current design/changelog authority wins; git history is provenance only.

Risk:
- Runtime bodies could become design dumps.

Mitigation:
- Keep root bodies concise and operational while design remains target-state authority.

Risk:
- Body-sufficiency validation could become a mechanical line-count-only rule.

Mitigation:
- Use structural checks plus content thresholds and governance wording.

Rollback:
- Revert the v9.88 commit if the corrective wave is wrong.
- Reinstall prior v9.87 44-file runtime set only under explicit rollback gate.
- Do not delete observed-only runtime destination extras.

---

## Closeout Summary

P073-10 restores the installed runtime-rule layer so README-listed active runtime roots carry real behavior contracts, not metadata-only design pointers. The practical impact is that runtime parity now proves both byte-level sync and active body sufficiency for the unchanged 44-file rule set.

Verification basis:
- source active runtime inventory: 44 files
- README Bash and PowerShell install arrays: 44 files and matched
- source body-sufficiency audit: passed for all 44 active runtime files
- runtime install/parity audit: 44/44 passed with no metadata-only active runtime files
- destination extras: observed-only and untouched

Next phase state: no next phase opened; optional automation support remains a future proposal only.

---

## Next Possible Phases

- Optional automation support for a reusable runtime body-sufficiency audit script if future release workflow needs a checked-in helper.
