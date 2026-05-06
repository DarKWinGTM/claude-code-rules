# Safe Terminal Output Guide

> **Current Version:** 1.4
> **Design:** [design/safe-terminal-output.design.md](design/safe-terminal-output.design.md) v1.4
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5
> **Full history:** [changelog/safe-terminal-output.changelog.md](changelog/safe-terminal-output.changelog.md)

---

## Rule Statement

**Core Principle: Plan command-output handling before execution so terminal output stays bounded, readable, session-safe, and evidence-useful without flooding context or hiding material failures.**

This rule owns command-output safety. It does not replace command safety, destructive confirmation, operational failure handling, or the dedicated file-reading rule.

---

## Core Contract

### 1) Plan before high-output commands

Before running a command likely to emit large, noisy, repetitive, binary-like, minified, or long-line output, choose how output will be captured and reviewed.

Required guidance:
- avoid dumping broad logs, builds, tests, grep recursion, find output, base64, or HTTP bodies directly into the conversation
- use bounded output, redirected files, targeted filters, or background tasks where appropriate
- prefer worker filtering for broad/noisy test, log, build, or search review when the leader does not need raw output
- keep stderr visible enough to diagnose real failures

### 2) Bound output without losing signal

Output limits protect context, but they must not hide material failure state.

Required guidance:
- show command, exit status, and relevant failure summary when material
- cap raw snippets to the smallest useful evidence
- if output was truncated, say what was truncated and where the persisted output can be reviewed when available
- use focused reruns or searches to isolate failure lines rather than expanding raw output blindly

### 3) Session-safe temporary output

When redirecting temporary output, avoid shared filenames that can collide across sessions or objectives.

Required guidance:
- use session/process-unique temp names for ad hoc command output when creating temporary files is necessary
- keep temporary files in `/tmp` unless a repo artifact is intentionally required
- do not create persistent debug files in the repo for ordinary command output
- cleanup of temp files is allowed, but deletion of repo files follows destructive-confirmation rules

### 4) Prefer direct tool behavior when safe

Do not add shell output indirection for simple low-output commands. Use direct commands when output is known to be small and useful.

---

## High-Output Triggers

Use this rule strongly for:
- test/build logs
- server logs and operational traces
- recursive grep/find output
- package manager output
- JSON/HTML/API responses of unknown size
- base64 or binary-like data
- generated/minified assets
- any command likely to produce long lines or thousands of lines

---

## Recommended Flow

```text
Command planned
  ↓
Could output be large/noisy?
  → NO: run directly if safe
  → YES: choose capture/filter strategy
  ↓
Run command with bounded output or persisted capture
  ↓
Review concise relevant evidence
  ↓
Report exit/result, checked scope, and any truncation
```

---

## Anti-Patterns

Avoid:
- dumping raw logs/builds/tests into the main context
- using `cat` or unbounded output for unknown files/responses
- truncating output while claiming full verification
- hiding command failures behind suppressed stderr
- creating repo-local junk output files
- rerunning broad noisy commands repeatedly instead of filtering
- using output caps as a reason to ignore material failures

Better behavior: plan output handling, capture safely, filter for signal, and report the real checked scope.

---

## Verification Checklist

- [ ] High-output risk was evaluated before running the command.
- [ ] Output was bounded, filtered, or captured safely when needed.
- [ ] Exit status and material failure lines remained visible.
- [ ] Truncation or partial review was reported when material.
- [ ] Temporary output did not create repo junk.
- [ ] Broad noisy output used worker filtering when appropriate.

---

## Quality Metrics

| Metric | Target |
|---|---|
| Terminal/context flooding incidents | 0 critical cases |
| Hidden command failure from over-suppression | 0 critical cases |
| Truncation honesty | High |
| Repo junk output files | 0 |
| High-output worker filtering | High when broad/noisy |

---

## Integration

Related rules:
- [safe-file-reading.md](safe-file-reading.md) - owns bounded file-reading behavior
- [operational-failure-handling.md](operational-failure-handling.md) - classifies failures and retry posture
- [native-worker-agent-routing-and-context-control.md](native-worker-agent-routing-and-context-control.md) - routes broad/noisy output review to workers
- [development-verification-and-debug-strategy.md](development-verification-and-debug-strategy.md) - chooses verification strategy and evidence boundaries
- [functional-intent-verification.md](functional-intent-verification.md) - confirmation gates for risky commands remain active

---

> **Full history:** [changelog/safe-terminal-output.changelog.md](changelog/safe-terminal-output.changelog.md)
