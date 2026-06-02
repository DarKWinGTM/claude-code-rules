---
name: init
description: Use when the operator wants to configure memory-context-intelligence through Claude Code question/choice dialogs and write the default user-scope config file.
version: 0.9.29
---

# Memory Context Intelligence Init

Public setup surface:
- `/memory-context-intelligence:init`

This surface is for configuration only.

Core contract:
- it is a **setup/config surface**, not a review surface
- it must use Claude Code **question/choice dialogs** as the main UX path
- it should default to `Comprehensive default (Recommended)`
- narrowing to `day / session / lookback` happens only when the operator explicitly chooses it
- final output writes `~/.claude/memory-context-intelligence.config.json`
- the written file must use the shared `analysis.scope_policy` + `analysis.source_policy` contract
- `trace_evidence` must remain the live promotion anchor
- do not expose `review` or `packet` as public surfaces

## Expected init flow

1. Explain what `/memory-context-intelligence:init` configures.
2. Offer `Comprehensive default (Recommended)` as the baseline.
3. Ask whether to keep the comprehensive default or explicitly narrow scope.
4. If narrowing is chosen, ask only the value needed for `day`, `session`, or `lookback`.
5. Ask for source-policy defaults.
6. Show a human-readable summary of the config that will be written.
7. Ask for final confirmation with `Write config now` as the recommended action.
8. Write `~/.claude/memory-context-intelligence.config.json`.

## Scope choices

Default choice:
- `Comprehensive default (Recommended)`

Explicit narrow choices:
- `day`
- `session`
- `lookback`

The surface must never make a narrow scope the default by accident.

## Config target

Default write target:
- `~/.claude/memory-context-intelligence.config.json`

The file should carry:
- `analysis.scope_policy`
- `analysis.source_policy`

## Operator summary after write

After writing the file, explain briefly:
- which scope mode is now the default
- whether source classes were changed from the all-four default
- whether same-day widening is enabled
- that `/memory-context-intelligence:analysis` will now read this user-scope default config unless the operator explicitly narrows the run
