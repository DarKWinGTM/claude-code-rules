# Claude Code Rules & Framework

Overview repository for a governed Claude Code rules system.

This repository has two valid usage scopes:

1. **Runtime-only install**
   - Copy selected root runtime rules into `~/.claude/rules/` or `./.claude/rules/`
   - Use this when you only want active runtime rule behavior

2. **Full governed repository workflow**
   - Keep the repository structure intact
   - Use runtime rules, design docs, changelogs, TODO, and patches together
   - Use this when you want governed change tracking and deterministic documentation synchronization

---

## Quick Start

### Option A: Runtime-only install

```bash
git clone https://github.com/DarKWinGTM/claude-code-rules.git && \
mkdir -p ~/.claude/rules && \
for f in \
  accurate-communication.md \
  answer-presentation.md \
  anti-mockup.md \
  anti-sycophancy.md \
  authority-and-scope.md \
  dan-safe-normalization.md \
  document-consistency.md \
  document-changelog-control.md \
  document-design-control.md \
  document-patch-control.md \
  emergency-protocol.md \
  explanation-quality.md \
  flow-diagram-no-frame.md \
  functional-intent-verification.md \
  no-variable-guessing.md \
  phase-implementation.md \
  project-documentation-standards.md \
  recovery-contract.md \
  refusal-classification.md \
  refusal-minimization.md \
  safe-file-reading.md \
  safe-terminal-output.md \
  strict-file-hygiene.md \
  todo-standards.md \
  unified-version-control-system.md \
  zero-hallucination.md; do \
  cp "claude-code-rules/$f" ~/.claude/rules/; \
done
```

This installs the 26 active root runtime rules only.
It intentionally uses an allowlist, so overview/helper/audit artifacts such as `README.md`, `TODO.md`, `phase-implementation-template.md`, and `cleanup-audit.md` are not copied into the runtime rules directory.
It does **not** install the full governed repository workflow.

### Option B: Full governed repository workflow

Keep the repository layout intact:

```text
README.md                         # Overview/reference only
*.md                              # Active root runtime rules
TODO.md                           # Execution tracking only
design/*.design.md                # Active target-state guidance
changelog/changelog.md            # Master/system-wide changelog for repository-level history
changelog/*.changelog.md          # Authoritative per-chain changelogs
patches/*.patch.md                # Governed execution plans
support/**/*.md                   # Support/reference-only artifacts
phase-implementation-template.md  # Root-level non-governed helper
```

Use this mode when you want design-first governance, the master repository changelog plus authoritative per-chain changelogs, synchronized updates across the repository, and governed phased execution plans.

---

## Repository Truth Model

### What each layer means

| Layer | Role | Authority Level |
|------|------|-----------------|
| `README.md` | Overview, onboarding, repository map | Not chain authority |
| Root runtime rules (`*.md`) | Active runtime behavior | Active rule layer |
| `design/*.design.md` | Active target-state guidance | Design layer |
| `patches/*.patch.md` | Governed execution plans and live phased execution-plan instances | Governed plan layer |
| `changelog/changelog.md` | Master/system-wide changelog for repository-level synchronization history | Repository-level history authority |
| `changelog/*.changelog.md` | Authoritative per-chain history and latest chain version state | Chain authority |
| `TODO.md` | Execution tracking only | Not version authority |
| `phase-implementation-template.md` | Readable reusable phase-planning helper | Non-governed helper |
| `support/**/*.md` | Support/reference artifacts | Not governed design layer |

### Important boundaries

- Design docs do **not** carry embedded version-history tables in the active design body.
- `changelog/changelog.md` records repository-level synchronization history for the RULES system as a whole.
- `changelog/*.changelog.md` files remain the authoritative history source for their individual governed chains.
- `phase-implementation.md` is the semantic rule for phased execution planning.
- `patches/*.patch.md` remains the live governed execution-plan instance when phased planning is used.
- `phase-implementation-template.md` is a helper only, even when it is more detailed and readable than a minimal template.
- `26 active runtime rules` refers to the active root runtime inventory only, not the total count of governed/support artifacts in the repository.

---

## Active Runtime Rule Inventory

### Core Policies (3)
- `anti-mockup.md`
- `anti-sycophancy.md`
- `zero-hallucination.md`

### Quality & Safety (17)
- `accurate-communication.md`
- `authority-and-scope.md`
- `dan-safe-normalization.md`
- `document-consistency.md`
- `document-changelog-control.md`
- `document-design-control.md`
- `document-patch-control.md`
- `emergency-protocol.md`
- `functional-intent-verification.md`
- `phase-implementation.md`
- `project-documentation-standards.md`
- `recovery-contract.md`
- `refusal-classification.md`
- `refusal-minimization.md`
- `strict-file-hygiene.md`
- `todo-standards.md`
- `unified-version-control-system.md`

### Presentation & Readability (3)
- `answer-presentation.md`
- `explanation-quality.md`
- `flow-diagram-no-frame.md`

### Best Practices (3)
- `no-variable-guessing.md`
- `safe-file-reading.md`
- `safe-terminal-output.md`

**Active runtime inventory:** 26 root runtime rules.

---

## Phase Planning Model

Use these artifacts together when staged execution planning matters:

- `phase-implementation.md` → semantic rule for phased execution behavior
- `patches/*.patch.md` → live governed execution-plan instances
- `phase-implementation-template.md` → readable reusable root helper
- `TODO.md` → execution tracking companion
- `changelog/changelog.md` → master repository history companion
- `changelog/*.changelog.md` → per-chain history companion

This separation keeps the plan readable and traceable without turning the helper, TODO, or changelog into the primary phase authority.

---

## Governance Workflow

For governed repository updates, use this order:

```text
design
  → runtime rule
  → changelog
  → TODO
  → patch metadata final sync (when affected)
```

This keeps active-state docs, chain authority, and execution tracking aligned.

---

## Verification Examples

### Verify runtime-only install

```bash
ls ~/.claude/rules/
head -20 ~/.claude/rules/anti-sycophancy.md
```

This verifies that runtime rules were copied into the Claude rules path.

### Verify full governed repository workflow

Check that the repository still preserves all active layers:

```text
README.md
*.md runtime rules
design/*.design.md
changelog/*.changelog.md
TODO.md
patches/*.patch.md
phase-implementation-template.md
support/**/*.md
```

This verifies repository scope, not just runtime installation scope.

---

## Related Governance Files

For the active repository model, see:

- `design/design.md`
- `phase-implementation.md`
- `document-changelog-control.md`
- `document-design-control.md`
- `document-patch-control.md`
- `project-documentation-standards.md`
- `todo-standards.md`
- `unified-version-control-system.md`

---

## Notes

- This README is intentionally overview-only.
- Historical rollout and audit detail belongs in changelog files.
- Support/reference artifacts should not be treated as governed design docs unless intentionally normalized into that role.
