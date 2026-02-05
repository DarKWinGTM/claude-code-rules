# Strict File Hygiene Rule

> **Current Version:** 1.0
> **Design:** [design/strict-file-hygiene.design.md](design/strict-file-hygiene.design.md) v1.0

## Rule Statement

AI must not create non-functional files unless the user explicitly asks.

---

## Not Allowed

- Versioned copies such as `file-v2`, `_final`, `plan-2026`
- Checkpoint/summary/plan files not requested by user
- Proactive docs (README/PLAN/TODO) without asking
- "Work summary/Change summary" files not requested

---

## Allowed

- Functional code/config required for system operation
- Documents explicitly requested by user
- Temporary files in `/tmp` (should clean up when done)

---

## Procedure (Mandatory)

1. If existing file exists: Edit existing file, do NOT create new one
2. If user explicitly asks: Create file as requested
3. If uncertain: Always ask first

---

## Operational Rules

- **Existing file first**: If file exists, edit it only
- **Ask when unclear**: If document necessity is unclear, always ask first
- **Exception handling**: If new file is necessary, state brief reason before creating

---

## Integration

- **document-consistency**: Reduce duplicate files, reference main files only
- **no-variable-guessing**: Do NOT guess file requirements, ask if unclear
- **authority-and-scope**: If user commands to create, follow command

---

## Enforcement Notes

- **Single Source of Truth**: No duplicate file versions
- **Git handles history**: Let Git track history, not filename suffixes

---

> Full history: [changelog/strict-file-hygiene.changelog.md](changelog/strict-file-hygiene.changelog.md)
