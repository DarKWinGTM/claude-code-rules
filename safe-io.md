# Safe I/O (File Reading + Terminal Output)

> **Current Version:** 1.4
> **Design:** [design/safe-io.design.md](design/safe-io.design.md) v1.4
> **Session:** 1f1873d2-0feb-485f-a5ff-d383254590dd
> **Full history:** [changelog/safe-io.changelog.md](changelog/safe-io.changelog.md)

---

## Rule Statement

**Core Principle: Bound I/O operations — file reading and terminal output — so session stays responsive, paths are verified before factual claims, large/risky files use partial reads or searches, worker-fit aggregate read/output bursts are delegated before leader raw absorption when that is the safer context-budget choice, command output cannot flood context or hide material failures, governed design/changelog chains are read through their declared compact parent first whether they use flat sibling or same-stem shard mode, and oversized active governance entrypoints or autocompact thrash are treated as rollover-maintenance signals.**

---

## Core Contract

### 1) Prefer dedicated read tools

Prefer `Read` for known files and search tools for locating files/symbols. Use Bash reading only when dedicated tools don't fit or the user needs shell output.

- verify path existence or source authority before relying on local file claims
- use `offset`/`limit` for large files
- avoid raw full reads of large/minified/generated/binary-like files
- report partial scope when only part of a file was read

### 2) Bounded output by default (file reading)

File reading should not flood the session.

- normal source files: read a bounded range when large
- minified/bundled/generated files: preview/search only unless exact full content is necessary
- logs, maps, SVG, HTML, unknown JSON, base64-like files: targeted search or small preview
- if output exceeds tool limits, switch to narrower offsets/searches rather than rereading the whole file

### 3) Evaluate before broad reading and the delegate-first aggregate-read burst gate

Before broad file absorption or a multi-file governance/code read burst, identify the read's purpose and whether the leader needs raw content.

- read only the sections needed for the active claim or edit
- search first when looking for a symbol, config key, version, heading, or reference
- use worker-first filtering by default for broad governance/code scans, broad multi-file searches, context-heavy sweeps, or aggregate read plans crossing several authority surfaces
- dispatch the worker before the leader absorbs raw broad content
- worker findings must include conflicts, exact anchors, and leader verification needs
- direct leader reads allowed for narrow known files, exact line ranges, final verification anchors, tightly sequential interactive-control work, unavailable worker tooling, or a stated narrow exception
- do not treat a small excerpt as proof about the entire file unless checked scope is sufficient

Delegate-first aggregate-read burst signals include repo-wide search followed by several file opens, parent index plus multiple child shards or version details, mixed docs+code+command output, repeated offset hopping after compact, or dense markdown across several active docs.

Burst rule:
- one decisive high-risk signal or two moderate signals are enough to prefer delegate-first handling
- once burst signals are active, avoid "just one more raw read" drift; either narrow scope or hand off the burst
- safe-io owns the trigger; worker-routing owns topology selection and orchestration after the trigger fires

### 4) Sharded active design reading

For designs using a compact parent plus active child shards, start from the compact parent index and follow the declared chain shape.

- read the parent index first for purpose, authority boundary, target-state summary, selected chain shape, shard map, and shard-selection guidance
- if the parent declares `flat-sibling-shards`, open only the named sibling shard in the same folder rather than assuming a nested same-stem child directory
- if the parent declares `same-stem-subfolder-normalized`, open only the named child shard in the declared child directory rather than absorbing the whole child set
- do not invent a nested same-stem child directory from the parent filename alone; rely on the parent-declared chain shape
- read child/sibling shards selectively by target-state slice; do not absorb the whole shard set
- use worker filtering for broad shard audits, stale-shard checks, or multi-shard consistency sweeps
- report checked parent and shard scope when using selected shards as evidence
- do not treat child design shards as `history/`, `done/`, archive, or rollover surfaces by default; they remain active design truth unless governance says otherwise

### 5) Changelog version detail shard reading

For changelogs using a compact parent plus active version-detail shards, start from the active parent changelog and follow the declared chain shape.

- read the active parent changelog first for current version authority, selected chain shape, shard map, and navigation
- if the parent declares `flat-sibling-shards`, open only the named sibling version-detail shard in the same folder rather than assuming a nested same-stem child directory
- if the parent declares `same-stem-subfolder-normalized`, open only the named version-detail shard in the declared child directory rather than absorbing the whole chain shard directory
- do not invent a nested same-stem child directory from the parent filename alone; rely on the parent-declared chain shape
- read version detail shards selectively by version/topic; do not absorb the whole shard set
- use worker filtering for broad version-history audits, parent/shard consistency sweeps, or multi-shard migration reviews
- report checked parent and shard scope when using selected shards as evidence
- do not treat `changelog/done/` as the default same-chain detail namespace; consult it only through active references or for history, audit, rollback, provenance, or trace reconstruction

### 6) Oversized governance entrypoints

If active governance entrypoints such as `TODO.md` or `phase/SUMMARY.md` exceed practical read limits, trigger bounded inspection and rollover maintenance instead of repeatedly rereading the same oversized file.

- use offsets/searches to identify current state only long enough to preserve and compact it
- if a read fails from size or autocompact thrash points to repeated large file absorption, roll active detail into `history/`/`done/` shards
- after rollover, start active reads at the compact entrypoint and follow only the history/done shard actually needed
- do not treat the pre-rollover snapshot as active current context unless audit/rollback/provenance requires it

### 7) Safe fallback patterns for command-line reads

When a command-line read is unavoidable, use deterministic caps (line/character limits). Avoid `cat`/unbounded output for large or unknown files.

```text
preview/search first
  ↓
limit by lines and characters
  ↓
read narrower ranges when needed
```

Do not preserve exact shell snippets as reusable defaults when the dedicated tool is better.

### 8) Plan before high-output commands

Before running a command likely to emit large, noisy, repetitive, binary-like, minified, or long-line output, choose how output will be captured and reviewed.

- avoid dumping broad logs, builds, tests, grep recursion, find output, base64, or HTTP bodies directly into the conversation
- use bounded output, redirected files, targeted filters, or background tasks where appropriate
- prefer worker filtering for broad/noisy test, log, build, or search review when the leader does not need raw output
- if the output will immediately require multi-pass filtering or cross-reference with several files, treat it as a delegate-first burst instead of a direct leader read
- keep stderr visible enough to diagnose real failures

### 9) Bound terminal output without losing signal

Output limits protect context but must not hide material failure state.

- show command, exit status, and relevant failure summary when material
- cap raw snippets to the smallest useful evidence
- if output was truncated, say what was truncated and where persisted output can be reviewed when available
- use focused reruns or searches to isolate failure lines rather than expanding raw output blindly

### 10) Session-safe temporary output

When redirecting temporary output, avoid shared filenames that can collide across sessions or objectives.

- use session/process-unique temp names for ad hoc command output when temp files are necessary
- keep temp files in `/tmp` unless a repo artifact is intentionally required
- do not create persistent debug files in the repo for ordinary command output
- temp-file cleanup is allowed; deletion of repo files follows destructive-confirmation rules

### 11) Prefer direct tool behavior when safe

Do not add shell output indirection for simple low-output commands. Use direct commands when output is known to be small and useful.

---

## Risk Model

### File-shape risk

| File shape | Risk | Preferred behavior |
|---|---|---|
| Small normal source/doc | Low | Use Read directly |
| Large source/doc | Medium | Use Read with offset/limit |
| Sharded active design parent index | Low/Medium | Read compact parent index first; select relevant child shards |
| Sharded active design child/sibling shard set | Medium/High | Read the parent chain shape and shard map first, then targeted shards; worker filtering for broad audits |
| Active parent changelog | Low/Medium | Read parent authority, chain shape, and shard map before selected version detail shards |
| Changelog version detail child/sibling shard set | Medium/High | Read parent chain shape and shard map first, then targeted version shards; worker filtering for broad history audits |
| `changelog/done/` fallback history | Medium/High | Open only through active reference or history/audit/rollback/provenance need |
| Oversized `TODO.md` / `phase/SUMMARY.md` | High | Bounded read for current state, then rollover/compact active entrypoint |
| Aggregate multi-file read burst | High | Delegate-first filtering or narrow scope before leader raw reads |
| Mixed output + follow-up file investigation | High | Capture/filter first, then inspect anchors or worker digest |
| Minified/bundled/generated | High | Preview/search only |
| Logs/build outputs | High | Tail/search/filter; consider worker review |
| Unknown JSON/HTML/SVG/map | Medium/High | Search or preview by bounded range |
| Binary/base64-like content | High | Avoid raw read; inspect metadata or small prefix only |

### High-output command triggers

Use this rule strongly for:
- test/build logs
- server logs and operational traces
- recursive grep/find output
- package manager output
- JSON/HTML/API responses of unknown size
- base64 or binary-like data
- generated/minified assets
- any command likely to produce long lines or thousands of lines
- any output that will need cross-checking against several files or several reruns before the leader can act

### Recommended command flow

```text
Command planned
  ↓
Could output or follow-up reads become large/noisy?
  → NO: run directly if safe
  → YES: choose capture/filter strategy
  ↓
Burst signals present?
  → YES: delegate-first or persist/filter before leader review
  → NO: continue with bounded direct capture
  ↓
Review concise relevant evidence
  ↓
Report exit/result, checked scope, and any truncation
```

---

## Anti-Patterns

Avoid:
- raw full reads of large/minified files, or `cat`/`head`/`tail`/`sed` when Read fits
- unbounded output for unknown files/responses
- whole-project claims from narrow excerpts
- repeating failed oversized reads without narrowing scope
- leaving oversized active governance entrypoints untouched after read failures or autocompact thrash
- waiting until after a read/output burst has already filled leader context before deciding to delegate it
- reading broad file sets into leader context when a worker lane should filter them
- combining repo-wide search, dense docs, and noisy output in one leader pass when a filter lane should have handled the burst first
- reading every child shard before checking the compact parent design index
- treating sharded active design child docs as history/`done`/archive/rollover surfaces by default
- reading every changelog version detail shard before checking the active parent changelog shard map
- treating `changelog/done/` as the default same-chain version detail namespace
- presenting local path/file facts without checked scope
- dumping raw logs/builds/tests into the main context
- truncating output while claiming full verification
- hiding command failures behind suppressed stderr
- creating repo-local junk output files
- rerunning broad noisy commands instead of filtering
- using output caps to ignore material failures

---

## Integration

Related rules:
- [evidence-discipline.md](evidence-discipline.md) - verifies paths, symbols, config, scoped non-findings
- [evidence-discipline.md](evidence-discipline.md) - claim strength from partial reads
- [worker-routing-and-context.md](worker-routing-and-context.md) - routes broad read/search/output review to worker lanes
- [document-governance.md](document-governance.md) - parent design index and child shard semantics
- [document-governance.md](document-governance.md) - parent changelog, version shard, fallback history semantics
- [document-integrity.md](document-integrity.md) - references, shard maps, source/destination alignment
- [document-integrity.md](document-integrity.md) - daily-first rollover for oversized active entrypoints
- [action-safety.md](action-safety.md) - failure classification and retry posture
- [coding-discipline.md](coding-discipline.md) - verification strategy and evidence boundaries
- [action-safety.md](action-safety.md) - confirmation gates for risky commands

---
