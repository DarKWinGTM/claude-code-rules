# Phase 073-08 - Install runtime rules and verify parity

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 073-08
> **Status:** Completed
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Design References:** [../design/design.md](../design/design.md)
> **Patch References:** [../patch/runtime-rules-semantic-compression-inventory.patch.md](../patch/runtime-rules-semantic-compression-inventory.patch.md)

---

## Objective

Install the 41 README-installed active runtime rule files into `/home/node/.claude/rules/` and verify source-to-runtime parity without installing governed planning surfaces or deleting destination files outside the active install set.

พูดง่าย ๆ: phase นี้คือเอา rule runtime ที่ audit ผ่านแล้วไปวางใน runtime จริง แล้วเช็กว่าไฟล์ source กับไฟล์ที่ติดตั้งตรงกันทุกตัว.

## Why this phase exists

P073-07 completed the source-only semantic parity and aggregate reduction audit, but intentionally left runtime install as a separate gate. The user then explicitly requested runtime installation into `~/.claude/rules/`, so P073-08 records that later install/parity gate.

## Entry conditions

- P073-07 final source-only semantic parity audit is complete.
- The active runtime inventory remains the 41 root rule files listed by the README Quick Start install set.
- Runtime install is explicitly requested by the user.
- No deletion, cleanup, or ownership classification of destination files outside the active install set is authorized.

## Scope

### In scope

- install the 41 active runtime rule files into `/home/node/.claude/rules/`
- verify active source/runtime hash parity
- record destination markdown files outside the active install set as observed-only and untouched
- synchronize governed source records for the P073-08 install/parity gate

### Out of scope

- no install of `README.md`, `TODO.md`, `checkpoint.md`, `phase-implementation-template.md`, or governed planning/support directories as runtime rules
- no deletion or cleanup classification of files outside the active install set already present in `/home/node/.claude/rules/`
- no `CLAUDE.md` edits
- no plugin, hook, custom-agent source, unrelated delegation/cleanup work
- no git push or release

## Affected artifacts

- `/home/node/.claude/rules/` active runtime copies
- `README.md`
- `design/design.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- `patch/runtime-rules-semantic-compression-inventory.patch.md`
- `phase/phase-073-08-install-runtime-rules-and-verify-parity.md`

## Action points / execution checklist

- [x] Confirm no existing P073-08 phase file was present before this record was created.
- [x] Install only the 41 README-installed active runtime rule files into `/home/node/.claude/rules/`.
- [x] Verify all 41 active source files exist.
- [x] Verify all 41 active destination runtime copies exist.
- [x] Verify source/runtime SHA-256 parity for all 41 active runtime files.
- [x] Record destination markdown files outside the active install set as observed-only and untouched.
- [x] Sync governed source records for the runtime install/parity gate.

## TODO coordination

Live execution is tracked by `#1176`.

## Changelog coordination

P073-08 adds a repository-level master changelog entry for the explicit runtime install/parity gate. It does not claim release, push, deletion of extra runtime files, or any plugin/hook/custom-agent work.

## Verification

Runtime install command result:

```text
INSTALLED_COUNT 41
MISSING_SOURCE []
DESTINATION /home/node/.claude/rules
```

Runtime parity check result:

```text
ACTIVE_SOURCE_COUNT 41
ACTIVE_DEST_COUNT 41
MISSING_SOURCE []
MISSING_DEST []
HASH_MISMATCHES []
EXTRA_DEST_MD_NOT_TOUCHED ['checkpoint.md', 'shared-task-list-path-coordination.md']
PARITY_PASS True
```

Boundary verification:
- [x] only the README-installed 41 active runtime rule files were installed as part of this phase
- [x] no governed planning/support surfaces were installed as runtime rules
- [x] destination markdown files outside the active install set were observed only, not classified or removed
- [x] no `CLAUDE.md`, plugin/hook/custom-agent source, push, release, or unrelated cleanup work was performed

## Exit criteria

- [x] All 41 active runtime rule files are installed into `/home/node/.claude/rules/`.
- [x] Source/runtime parity passes for the active runtime install set.
- [x] Destination markdown files outside the active install set remain untouched unless a later explicit owner-scoped delete/cleanup instruction is given.
- [x] Governed source records describe P073-08 runtime install/parity completion without rewriting P073-01 through P073-07 source-only history.

## Risks / rollback notes

- If an active runtime copy later drifts, recopy only the affected active runtime rule from the source repository and re-run parity verification.
- If a destination file outside the active install set needs cleanup later, treat that as a separate explicit owner-scoped deletion request; this phase does not authorize removal or ownership classification.
- If a runtime behavior issue appears after install, compare the installed active runtime file against its source hash first before changing source doctrine.

## Next possible phases

- none for P073 unless the user explicitly requests a separate owner-scoped cleanup, release, push, or future runtime-maintenance wave.
