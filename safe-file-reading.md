# Safe File Reading Guide

> **Current Version:** 1.8
> **Design:** [design/safe-file-reading.design.md](design/safe-file-reading.design.md) v1.8
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/safe-file-reading.changelog.md](changelog/safe-file-reading.changelog.md)

---

## Rule Statement

**Core Principle: Read files in a bounded, purpose-aware way that preserves session responsiveness, avoids terminal/output flooding, verifies paths before factual claims, uses partial reads or searches for large or risky files, treats oversized active governance entrypoints or autocompact thrash as rollover-maintenance signals, reads sharded active designs through compact parent indexes before child shards, and reads chain-scoped changelog version shards through active parent changelog maps before detail shards.**

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

### 3) Evaluate before broad reading and the worker-first aggregate-read gate

Before broad file absorption or a multi-file governance/code read burst, identify the purpose of the read and whether the leader needs raw content.

Required guidance:
- read only the sections needed for the active claim or edit
- search first when looking for a symbol, config key, version, heading, or reference
- use worker-first filtering by default for broad governance/code scans, broad multi-file searches, context-heavy sweeps, or aggregate read plans that cross several authority surfaces
- dispatch the worker before the leader absorbs raw broad content
- require worker findings to include conflicts, exact anchors, and leader verification needs
- allow direct leader reads for narrow known files, exact line ranges, final verification anchors, tightly sequential interactive-control work, unavailable worker tooling, or a stated narrow direct-handling exception
- do not treat a small excerpt as proof about the entire file unless the checked scope is sufficient

### 4) Sharded active design reading

When a governed design uses `design/<slug>.design.md` plus `design/<slug>/*.design.md`, start from the compact parent index and select only the child shards needed for the active question.

Required guidance:
- read the parent index first to understand purpose, authority boundary, target-state summary, shard map, and shard-selection guidance
- read child shards selectively by target-state slice instead of absorbing the whole shard directory by default
- use worker filtering for broad shard audits, stale-shard checks, or multi-shard consistency sweeps
- report checked shard scope when using selected shards as evidence
- do not treat child design shards as `history/`, `done/`, archive, or rollover surfaces by default; they remain active design truth unless governance says otherwise

### 5) Changelog version detail shard reading

When a governed changelog uses `changelog/<chain>.changelog.md` plus `changelog/<chain>/v*.changelog.md`, start from the active parent changelog and select only the version detail shards needed for the active question.

Required guidance:
- read the active parent changelog first to understand current version authority, shard map, and navigation
- read version detail shards selectively by version/topic instead of absorbing the whole chain shard directory by default
- use worker filtering for broad version-history audits, parent/shard consistency sweeps, or multi-shard migration reviews
- report checked parent and shard scope when using selected shards as evidence
- do not treat `changelog/done/` as the default same-chain detail namespace; consult it only through active references or for history, audit, rollback, provenance, or trace reconstruction

### 6) Oversized governance entrypoints

If active governance entrypoints such as `TODO.md` or `phase/SUMMARY.md` exceed practical read limits, trigger bounded inspection and rollover maintenance instead of repeatedly reading the same oversized active file.

Required guidance:
- use offsets/searches to identify current state only long enough to preserve and compact it
- if a read fails from size or autocompact thrash points to repeated large file absorption, treat that as a hard signal to roll active detail into `history/`/`done/` shards
- after rollover, start active reads at the compact entrypoint and follow history/done references only when needed
- do not treat the pre-rollover snapshot as active current context unless audit/rollback/provenance requires it

### 7) Safe fallback patterns

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
| Sharded active design parent index | Low/Medium | Read compact parent index first and select relevant child shards |
| Sharded active design child shard set | Medium/High | Read shard map first, then targeted shards; use worker filtering for broad audits |
| Active parent changelog | Low/Medium | Read parent authority and shard map before selected version detail shards |
| Changelog version detail shard set | Medium/High | Read parent shard map first, then targeted version shards; use worker filtering for broad history audits |
| `changelog/done/` fallback history | Medium/High | Open only through active reference or history/audit/rollback/provenance need |
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
- reading every child shard of a sharded active design before checking the compact parent index
- treating sharded active design child docs as history, `done`, archive, or rollover surfaces by default
- reading every changelog version detail shard before checking the active parent changelog shard map
- treating `changelog/done/` as the default same-chain version detail namespace
- presenting local path/file facts without checked scope

Better behavior: read with purpose, cap output, search targeted content, and disclose the checked scope.

---

## Verification Checklist

- [ ] Dedicated read/search tools were preferred where suitable.
- [ ] Large or risky files used bounded reads/searches.
- [ ] Checked scope was clear when reporting file facts or non-findings.
- [ ] Broad governance/code scans and aggregate read plans used worker-first filtering unless a narrow direct-handling exception was stated.
- [ ] Sharded active designs started at compact parent index and used shard-selective reads.
- [ ] Changelog version detail reads started at the active parent changelog shard map and used version-shard-selective reads.
- [ ] `changelog/done/` was opened only through active reference or history/audit/rollback/provenance need.
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
| Sharded design read selectivity | High |
| Changelog parent-map-first read selectivity | High |
| Dedicated tool preference | High |

---

## Integration

Related rules:
- [safe-terminal-output.md](safe-terminal-output.md) - owns terminal command output limits
- [no-variable-guessing.md](no-variable-guessing.md) - verifies paths, symbols, config, and scoped non-findings
- [evidence-grounded-burden-of-proof.md](evidence-grounded-burden-of-proof.md) - defines claim strength from partial reads
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - routes broad read/search work to worker lanes when appropriate
- [document-design-control.md](document-design-control.md) - owns compact parent design index and governed child shard semantics
- [document-changelog-control.md](document-changelog-control.md) - owns active parent changelog, chain-scoped version detail shard, and fallback history semantics
- [document-consistency.md](document-consistency.md) - keeps references, shard maps, and source/destination roles aligned
- [governed-document-rollover-control.md](governed-document-rollover-control.md) - owns daily-first rollover when active governance entrypoints become too large to read safely

---

> **Full history:** [changelog/safe-file-reading.changelog.md](changelog/safe-file-reading.changelog.md)
