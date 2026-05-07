# Safe File Reading Guide

> **Current Version:** 1.5
> **Design:** [design/safe-file-reading.design.md](design/safe-file-reading.design.md) v1.5
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/safe-file-reading.changelog.md](changelog/safe-file-reading.changelog.md)

---

## Rule Statement

**Core Principle: Read files in a bounded, purpose-aware way that preserves session responsiveness, avoids terminal/output flooding, verifies paths before factual claims, uses partial reads or searches for large or risky files, and treats oversized active governance entrypoints or autocompact thrash as rollover-maintenance signals.**

This rule owns file-reading safety and output-size control. It does not replace no-variable-guessing, evidence thresholds, or the dedicated Read tool preference.

---

## Core Contract

### 1) Prefer dedicated read tools

Use the dedicated `Read` tool for known files whenever possible. Use search tools for locating files or symbols. Use Bash reading commands only when a dedicated tool cannot fit the task or the user explicitly needs shell output.

Required guidance:
- verify path existence or source authority before relying on local file claims
- use `offset` and `limit` for large files
- avoid raw full reads of large/minified/generated/binary-like files
- report partial scope when only part of a file was read

### 2) Bounded output by default

File reading should not flood the session.

Default safety limits:
- normal source files: read a bounded range when large
- minified/bundled/generated files: preview/search only unless exact full content is necessary
- logs, maps, SVG, HTML, unknown JSON, and base64-like files: use targeted search or small preview
- if output exceeds tool limits, switch to narrower offsets/searches rather than repeatedly reading the same whole file

### 3) Evaluate before broad reading

Before broad file absorption, identify the purpose of the read.

Required guidance:
- read only the sections needed for the active claim or edit
- search first when looking for a symbol, config key, version, heading, or reference
- use worker routing for broad multi-file searches or context-heavy sweeps when appropriate
- do not treat a small excerpt as proof about the entire file unless the checked scope is sufficient

### 4) Oversized governance entrypoints

If active governance entrypoints such as `TODO.md` or `phase/SUMMARY.md` exceed practical read limits, trigger bounded inspection and rollover maintenance instead of repeatedly reading the same oversized active file.

Required guidance:
- use offsets/searches to identify current state only long enough to preserve and compact it
- if a read fails from size or autocompact thrash points to repeated large file absorption, treat that as a hard signal to roll active detail into `history/`/`done/` shards
- after rollover, start active reads at the compact entrypoint and follow history/done references only when needed
- do not treat the pre-rollover snapshot as active current context unless audit/rollback/provenance requires it

### 5) Safe fallback patterns

When a command-line read is unavoidable, use deterministic caps such as line and character limits. Avoid `cat`/unbounded output for large or unknown files.

Preferred shell pattern concept:

```text
preview/search first
  ↓
limit by lines and characters
  ↓
read narrower ranges when needed
```

Do not preserve exact shell snippets as reusable defaults when the dedicated tool is better.

---

## Risk Model

| File shape | Risk | Preferred behavior |
|---|---|---|
| Small normal source/doc | Low | Use Read directly |
| Large source/doc | Medium | Use Read with offset/limit |
| Oversized `TODO.md` / `phase/SUMMARY.md` | High | Bounded read for current state, then rollover/compact active entrypoint |
| Minified/bundled/generated | High | Preview/search only |
| Logs/build outputs | High | Tail/search/filter; consider worker review |
| Unknown JSON/HTML/SVG/map | Medium/High | Search or preview by bounded range |
| Binary/base64-like content | High | Avoid raw read; inspect metadata or small prefix only |

---

## Anti-Patterns

Avoid:
- raw full reads of large or minified files
- using Bash `cat`, `head`, `tail`, or `sed` when the dedicated Read tool is the right tool
- making whole-project claims from narrow excerpts
- repeating failed oversized reads without narrowing scope
- leaving oversized active governance entrypoints untouched after read failures or autocompact thrash identify them as context-bloat sources
- reading broad file sets into leader context when a worker lane should filter them
- presenting local path/file facts without checked scope

Better behavior: read with purpose, cap output, search targeted content, and disclose the checked scope.

---

## Verification Checklist

- [ ] Dedicated read/search tools were preferred where suitable.
- [ ] Large or risky files used bounded reads/searches.
- [ ] Checked scope was clear when reporting file facts or non-findings.
- [ ] Broad reads used worker routing when context-heavy.
- [ ] Oversized active governance entrypoints triggered rollover/compaction review instead of repeated full reads.
- [ ] No unbounded terminal/file output was introduced.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Session flooding from file reads | 0 critical cases |
| Unbounded reads of risky files | Low |
| Read-before-reference discipline | High |
| Scoped non-finding clarity | High |
| Dedicated tool preference | High |

---

## Integration

Related rules:
- [safe-terminal-output.md](safe-terminal-output.md) - owns terminal command output limits
- [no-variable-guessing.md](no-variable-guessing.md) - verifies paths, symbols, config, and scoped non-findings
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - defines claim strength from partial reads
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - routes broad read/search work to worker lanes when appropriate
- [document-consistency.md](document-consistency.md) - keeps references and source/destination roles aligned
- [governed-document-rollover-control.md](governed-document-rollover-control.md) - owns daily-first rollover when active governance entrypoints become too large to read safely

---

> **Full history:** [changelog/safe-file-reading.changelog.md](changelog/safe-file-reading.changelog.md)
