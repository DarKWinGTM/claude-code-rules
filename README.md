# Claude Code Rules & Framework

A professional ruleset for Claude Code with deterministic governance, evidence-grounded communication, artifact-first startup control, and disciplined phased execution.

---

## Quick Start

```bash
# clone and install

git clone https://github.com/DarKWinGTM/claude-code-rules.git && \
mkdir -p ~/.claude/rules && \
cp claude-code-rules/*.md ~/.claude/rules/
```

---

## Installation

### Full installation

```bash
git clone https://github.com/DarKWinGTM/claude-code-rules.git
cd claude-code-rules
mkdir -p ~/.claude/rules
cp *.md ~/.claude/rules/
ls ~/.claude/rules/
ls ~/.claude/rules/unified-version-control-system.md
```

### Selective installation

```bash
curl -o ~/.claude/rules/anti-sycophancy.md \
  https://raw.githubusercontent.com/DarKWinGTM/claude-code-rules/master/anti-sycophancy.md
```

### Project-specific installation

```bash
mkdir -p .claude/rules
cp /path/to/claude-code-rules/*.md .claude/rules/
```

### Installation paths

| Location | Scope | Path | Use Case |
|----------|-------|------|----------|
| Global | All projects | `~/.claude/rules/*.md` | Default recommendation |
| Project | Current project only | `./.claude/rules/*.md` | Project-specific needs |

---

## Design Documentation Structure

| Location | Purpose | File Type |
|----------|---------|-----------|
| `./design/*.design.md` | Design specifications | Design docs |
| `*.md` (root) | Active runtime rules | Rules files |
| `./changelog/changelog.md` | Master repository-wide history | Master changelog |
| `./changelog/*.changelog.md` | Per-chain authoritative history | Changelogs |
| `./phase/SUMMARY.md` | Governed summary/index for live phase planning | Phase summary doc |
| `./phase/phase-NNN-<phase-name>.md` | Governed major-phase execution detail | Major phase docs |
| `./phase/phase-NNN-NN-<subphase-name>.md` | Governed subphase execution detail | Subphase docs |
| `./patch/<context>.patch.md` or `./<context>.patch.md` | Governed patch/review artifacts outside live phase planning | Patch docs |
| `./phase-implementation-template.md` | Root helper for phased planning | Helper artifact |

---

## Integration Guide

This section defines how `design`, `changelog`, `runtime rules`, `TODO`, and governed phase-planning artifacts should be updated together.

### Document Roles

| Document | Role | Update Trigger |
|----------|------|----------------|
| `design/*.design.md` | Target behavior/specification | Requirement or policy change |
| `*.md` (root runtime rules) | Active runtime behavior | Approved design change requires runtime sync |
| `changelog/changelog.md` | Master repository-wide synchronization history | Repository-level governed sync events |
| `changelog/*.changelog.md` | Authoritative per-chain version history | Any rule/design update with version impact |
| `phase/SUMMARY.md` | Governed summary/index for live phased execution | Phased implementation work needs one summary file with a phase map, source-input extraction rollup, review rollup, and global coordination |
| `phase/phase-NNN-<phase-name>.md` and `phase/phase-NNN-NN-<subphase-name>.md` | Governed phase-detail layer | Multi-stage execution detail under `/phase` |
| `patch/<context>.patch.md` or root `<context>.patch.md` | Governed patch/review artifact layer | Patch or review work outside live phase planning |
| `TODO.md` | Execution and progress tracking | Work starts/completes or task state changes |

### Startup Artifact Gate

Before meaningful governed work drifts, the repository now expects startup artifact posture to be resolved through `artifact-initiation-control.md`.

That means design / changelog / TODO / phase / patch should be explicitly resolved as:
- use existing
- create now
- ask now
- not required

---

## Rule Files

### Core policies
- `anti-mockup.md`
- `anti-sycophancy.md`
- `zero-hallucination.md`

### Quality and safety
- `accurate-communication.md`
- `answer-presentation.md`
- `artifact-initiation-control.md`
- `authority-and-scope.md`
- `document-changelog-control.md`
- `document-consistency.md`
- `document-design-control.md`
- `document-patch-control.md`
- `emergency-protocol.md`
- `evidence-grounded-burden-of-proof.md`
- `explanation-quality.md`
- `functional-intent-verification.md`
- `natural-professional-communication.md`
- `operational-failure-handling.md`
- `phase-implementation.md`
- `project-documentation-standards.md`
- `runtime-topology-control.md`
- `strict-file-hygiene.md`
- `todo-standards.md`
- `unified-version-control-system.md`

### Best practices
- `flow-diagram-no-frame.md`
- `no-variable-guessing.md`
- `safe-file-reading.md`
- `safe-terminal-output.md`
- `tactical-strategic-programming.md`

**Active Runtime Rules: 32**

---

## Notes

- Active phase naming uses:
  - major phases: `NNN`
  - subphases: `NNN-NN`
- Startup artifact posture is resolved before meaningful governed work drifts.
- Historical changelog and TODO references to older numbering remain historical records.
- The helper at `phase-implementation-template.md` is readable guidance, not authority.
