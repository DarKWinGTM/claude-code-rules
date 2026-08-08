# Safe I/O (File Reading + Terminal Output)

> **Current Version:** 1.6
> **Design:** [design/safe-io.design.md](design/safe-io.design.md) v1.6
> **Session:** 92c4d51e-eb02-4299-823a-1a6b8270f045
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

### 3) Aggregate read/output burst detection
Before broad absorption, define the question, likely authority surface, and whether the leader needs raw content or a filtered result. Read or search only the smallest scope needed.

A burst is worker-fit when one decisive high-risk signal or two moderate signals are present, including repo-wide search plus follow-up reads, several authority surfaces for one claim, parent plus multiple shards, mixed code/docs/command output, dense active documents, noisy logs/tests/builds, or repeated offset/reread churn after compact.

When the gate fires, narrow the I/O or invoke `worker-routing-and-context.md` before further raw leader absorption. Do not continue with "one more" broad read. Direct handling remains allowed for narrow known files, exact edit/verification ranges, final anchor checks, tightly sequential interactive work, unavailable worker tooling, explicit user direction, or a stated narrow exception. A bounded excerpt supports only its checked scope.

Safe I/O owns burst detection and bounded capture. Worker Routing owns topology, dispatch, lane contracts, and handoff quality.

### 4) Parent-first governed-chain reading
For sharded design or changelog chains, read the compact active parent first for authority, declared shape, map, and selection guidance. Then open only the named sibling or same-stem child needed for the active question.

- do not infer a nested directory from the parent filename or absorb the whole shard set
- broad consistency/history audits may trigger the aggregate-burst gate
- report the checked parent/shard scope
- treat design children as active target-state truth, not history/done by default
- open `changelog/done/` only through an active reference or history/audit/rollback/provenance need
- when reading an example, keep observed shape, extracted doctrine, selected target, and equivalence basis distinct

### 5) Oversized governance entrypoints
When an active entrypoint exceeds practical read limits or causes compact thrash, inspect only enough current state to invoke the rollover contract in `document-integrity.md`. After rollover, start from the compact active entrypoint and open history/done only through an active reference or audit/rollback/provenance need.

### 6) Command and temporary-output safety
Use direct tools for known low-output work. When shell or high-output commands are necessary, choose deterministic line/character caps, capture/filter strategy, and session-unique `/tmp` output before running them.

- do not dump unknown logs, builds, recursive searches, HTTP bodies, generated/minified data, or binary/base64-like content into the conversation
- keep command, exit status, material stderr, and failure summary visible
- disclose truncation, partial scope, and where persisted output can be reviewed
- use focused searches/reruns instead of expanding noisy output blindly
- avoid repo-local ordinary debug artifacts; temporary cleanup is allowed, while repo-file deletion follows destructive confirmation
- route multi-pass or cross-file output review through the aggregate-burst gate

---

## Anti-Patterns

Avoid unbounded or repeated broad reads; whole-scope claims from excerpts; bypassing active parents/maps; delaying burst routing until raw context is already absorbed; hiding failures or truncation; treating output caps as verification; and creating persistent repo debug output for ordinary command review.

---

## Integration

Related owners:
- [worker-routing-and-context.md](worker-routing-and-context.md) — topology, dispatch, lane contracts, and handoff quality after burst detection
- [document-governance.md](document-governance.md) — governed chain semantics
- [document-integrity.md](document-integrity.md) — reference validation and rollover preservation
- [evidence-discipline.md](evidence-discipline.md) — claim strength from checked I/O
- [action-safety.md](action-safety.md) — risky commands, failures, retries, and destructive confirmation

---
