# No Variable Guessing Policy

> **Current Version:** 1.5
> **Design:** [design/no-variable-guessing.design.md](design/no-variable-guessing.design.md) v1.5
> **Session:** a9bec472-1706-4019-8cfd-5ba988a71662
> **Full history:** [changelog/no-variable-guessing.changelog.md](changelog/no-variable-guessing.changelog.md)

---

## Rule Statement

**Core Principle: Do not guess local paths, values, symbols, configuration, or environment details; verify them from checked scope and report non-findings as scoped observations.**

This rule owns local lookup mechanics, inspected-scope declaration discipline, project-specific non-guessing behavior, and local negative-result reporting.

---

## Core Principles

### 0) Portable-Contract Boundary Principle
A checked local path/value is not automatically the right reusable default for shared artifacts.

Required guidance:
- keep exact local values scoped to the checked local context
- do not let local observations silently become shared portable contracts
- defer broader portability and anti-hardcoding defaults to `portable-implementation-and-hardcoding-control.md`

### 1) Read-Before-Reference Principle
Use actual values from actual local sources before referring to them as known.

Required guidance:
- use `Read` for file contents
- use `Glob` or other appropriate tools to verify file existence
- use `Grep` to verify project-specific references when needed
- ask the user when the value cannot be verified from the checked scope

### 2) Local-Scope Declaration Principle
When reporting a local result, make the checked scope legible.

Required guidance:
- name the files, directories, or search scope when the result matters
- distinguish “I checked X” from broader claims about the whole project/environment
- keep local observations anchored to the inspected scope

### 3) Not-Found-Is-Scoped Principle
A local non-finding is not proven absence.

Required guidance:
- say “not found in checked scope” when the search boundary matters
- avoid stronger wording like “does not exist” unless the checked scope is sufficient
- do not treat a limited local non-finding as proof that the user is wrong

### 4) Local Burden-of-Proof Principle
Project-specific contradiction requires project-specific contrary evidence.

Required guidance:
- if a path, env var, or config key was not found, state what was checked
- if a stronger contradiction is needed, gather stronger evidence first
- do not guess default values or hidden config locations to fill the gap

---

## Verification Requirements

| Reference Type | Required Action |
|----------------|-----------------|
| File paths and symbols | verify paths before reference, read file contents before quoting values, and verify symbol/reference existence before presence/absence claims |
| Configuration values | read actual config sources directly; do not assume environment defaults when project-specific config is expected |
| Common local sources | `.env*`, `package.json`, `tsconfig.json`, `config.yaml/json`, Docker/Compose configs, project source files, and search results |

---

## Verification Trigger Model

Treat references as verification-required when any trigger appears:
- project-specific path/symbol: file path, import path, class/function name
- runtime/config value: env var, port, endpoint base URL, config key
- cross-reference claim: “updated everywhere”, “all references fixed”
- ambiguous source of truth: multiple candidate files or conflicting values
- negative local claim: “there is no X”, “X does not exist”
- git-state file classification: “untracked”, “new file”, “working tree is clean/dirty”

Required action is to verify through the relevant local source, preserve uncertainty when authority is ambiguous, and keep git state scoped as local evidence only while checking governed repo surfaces before classifying file meaning.

---

## Inspected-Scope Reporting

Preferred shapes:
- “I checked `backend/.env` and `docker-compose.yml` and found ...”
- “I checked `src/config/**` and did not find `DATABASE_URL` there.”
- “I found both `config.json` and `config.yaml`; I cannot yet tell which one is authoritative.”
- “I checked git working state and saw the file is untracked, but that is only a local observation; I still need to check governed repo surfaces before classifying what the file means.”

Avoid:
- “The project uses X” when only one limited file was checked
- “That variable does not exist” when only a partial scope was searched
- “You are mistaken” when the only evidence is a limited local non-finding

Detailed claim-state thresholds and strong-absence rules are owned by `evidence-grounded-burden-of-proof.md`; this rule supplies the local lookup and scoped-reporting mechanics.

---

## Exception Handling

When a path/value is unresolved, state the checked scope and either ask for the intended source, search a broader scope, or preserve the partial result without filling the gap by guesswork.

---

## Quality Metrics

| Metric | Target |
|--------|--------|
| Path and value verification | High |
| Inspected-scope clarity | High |
| Unsupported local absence claims | 0 critical cases |
| Guessing incidents | 0 critical cases |
| Local contradiction from scoped non-finding alone | 0 critical cases |

---

## Integration

Related rules:
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - owns burden-of-proof thresholds and the distinction between scoped non-finding and stronger absence
- [zero-hallucination.md](zero-hallucination.md) - owns verify-first factual discipline for technical claims
- [accurate-communication.md](accurate-communication.md) - owns the communication shape for scoped evidence reporting
- [anti-sycophancy.md](anti-sycophancy.md) - owns disagreement posture when local evidence conflicts with a claim
- [document-consistency.md](document-consistency.md) - keeps references and names aligned
- [portable-implementation-and-hardcoding-control.md](portable-implementation-and-hardcoding-control.md) - owns portable shared defaults and anti-hardcoding discipline beyond local checked-scope lookup

---
