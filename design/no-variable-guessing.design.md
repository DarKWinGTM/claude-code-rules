# No Variable Guessing Policy

## 0) Document Control

> **Parent Scope:** Claude Code Rules System
> **Current Version:** 1.5
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662 (2026-04-17)

---

## 1) Goal

Define one local-evidence rule chain that prohibits guessing project-specific values and requires inspected-scope-aware reporting for paths, variables, configuration, and local references.

This chain owns:
- local lookup discipline
- project-specific anti-guessing behavior
- inspected-scope declaration behavior
- local non-finding semantics
- local burden-of-proof wording for contradiction and absence inside checked project scope

---

## 2) Problem Statement

The original no-variable-guessing rule correctly prohibited guessed values, but it still left one important communication gap under-specified: local non-findings were not strongly tied to inspected-scope reporting and could still be overstated.

Observed failure modes:
- guessed paths or config values are used without checking the project
- a partial local search is reported as if it covered the whole project
- "not found" is phrased like non-existence
- limited local non-findings are used as if they disproved the user
- multiple possible sources of truth are collapsed into one guessed answer

This design strengthens local evidence semantics without taking over broader factual-verification or disagreement ownership.

---

## 3) Core Principles

### 3.0 Portable-Contract Boundary Principle
Checked local values should not silently become shared portable defaults.

Required guidance:
- keep exact local paths/values scoped to checked local context
- treat local observations as evidence, not as reusable environment defaults
- defer broader anti-hardcoding ownership to `portable-implementation-and-hardcoding-control.md`

### 3.1 Read-Before-Reference Principle
Project-specific values should come from checked local sources, not assumptions.

Required guidance:
- read actual files before quoting values
- verify paths and symbols before referencing them as if known
- ask the user when the local source of truth cannot be identified from the checked scope

### 3.2 Local-Scope Declaration Principle
Local findings should say what was inspected.

Required guidance:
- identify the checked files, directories, or search scope when material
- distinguish between a checked subset and the whole repository/environment
- keep local claims anchored to observed local evidence

### 3.3 Scoped Non-Finding Principle
A local non-finding is weaker than project-wide absence.

Required guidance:
- report "not found in checked scope" when the search boundary matters
- do not upgrade a local non-finding into strong absence unless the checked scope is sufficient
- do not treat a limited non-finding as contradiction against the user by default

### 3.4 Local Burden-of-Proof Principle
Project-specific contradiction requires project-specific contrary evidence.

Required guidance:
- if the claim concerns a file, path, config value, or local symbol, gather the corresponding local evidence before contradicting it
- if only a partial local scope was checked, preserve that boundary in the communication
- do not fill missing local evidence with guessed defaults

---

## 4) Verification Model

### 4.1 Common local sources
- `.env`, `.env.local`, `.env.production`
- `package.json`, `tsconfig.json`
- `config.yaml`, `config.json`
- Docker / Compose configs
- source files and project search results

### 4.2 Trigger model
Treat local references as verification-required when these signals appear:

| Trigger | Typical Signal | Required Action |
|---------|----------------|-----------------|
| project-specific path or symbol | file path, import path, class/function name | verify with project tools before reference |
| runtime/config value | env var, port, base URL, config key | read the actual local source before use |
| cross-reference claim | "updated everywhere", "all references fixed" | verify the affected locations |
| ambiguous source of truth | multiple candidate files or conflicting values | preserve uncertainty and ask/verify |
| negative local claim | "there is no X", "X does not exist" | determine whether scoped non-finding or strong absence is justified |
| git-state file classification | "untracked", "new file", "working tree is clean/dirty" | keep git state scoped as local evidence only and check governed repo surfaces before classifying file meaning |

### 4.3 Reporting labels
- `Verified`
- `Unverified`
- `Not Found In Checked Scope`

---

## 5) Inspected-Scope Communication Contract

Required guidance:
- report what was checked when a local non-finding matters
- say when the scope remains partial
- distinguish between:
  - observed local fact
  - scoped non-finding
  - strong absence
- avoid implying repo-wide certainty from a narrow local check

Preferred examples:
- "I checked `backend/.env` and `docker-compose.yml` and found ..."
- "I checked `src/config/**` and did not find `DATABASE_URL` there."
- "I found multiple candidate config files, so I cannot yet tell which one is authoritative."
- "I checked git working state and saw the file is untracked, but that is only a local observation; I still need to check the governed repo surfaces before I can classify what the file means."

---

## 6) Anti-Patterns to Avoid

| Anti-Pattern | Why It Hurts | Better Shape |
|--------------|--------------|--------------|
| guessed path or value | creates environment mismatch | verify from local source |
| partial local search presented as project-wide truth | exaggerates certainty | identify the inspected scope |
| "not found" presented as non-existence | overstates the evidence | use scoped non-finding wording |
| scoped non-finding used as user contradiction | turns partial evidence into verdict | gather stronger local evidence first |
| guessed authoritative source among multiple candidates | hides uncertainty | surface the ambiguity |

---

## 7) Quality Metrics

| Metric | Target |
|--------|--------|
| Local verification discipline | High |
| Inspected-scope clarity | High |
| Unsupported local absence claims | 0 critical cases |
| Guessing incidents | 0 critical cases |
| Scoped non-finding honesty | High |

---

## 8) Integration

| Rule | Relationship |
|------|--------------|
| [../no-variable-guessing.md](../no-variable-guessing.md) | Runtime implementation |
| [evidence-grounded-burden-of-proof.design.md](evidence-grounded-burden-of-proof.design.md) | Owns burden-of-proof thresholds and scoped non-finding vs strong-absence distinction |
| [zero-hallucination.design.md](zero-hallucination.design.md) | Owns broader factual verify-first discipline |
| [accurate-communication.design.md](accurate-communication.design.md) | Owns wording shape for scoped evidence communication |
| [anti-sycophancy.design.md](anti-sycophancy.design.md) | Owns disagreement posture when local evidence conflicts with a claim |

---

> Full history: [../changelog/no-variable-guessing.changelog.md](../changelog/no-variable-guessing.changelog.md)
