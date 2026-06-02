# Init Configuration Surface

## 0) Document Control

> **Parent Scope:** memory-context-intelligence plugin-local governed design chain
> **Current Version:** 0.1.77
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-02)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define `/memory-context-intelligence:init` as the public setup/config surface for the plugin so operators can configure default analysis behavior through Claude Code question/choice dialogs instead of raw-arg-first setup.

## 2) Surface role

`/memory-context-intelligence:init` is a setup/config surface only.

It does:
- guide the operator through scope + source-policy choices
- default to the broadest current runtime analysis posture
- allow explicit narrowing to `day`, `session`, or `lookback`
- write the chosen defaults into the shared config file

It does not:
- run review/packet flow
- replace `/memory-context-intelligence:analysis`
- weaken `trace_evidence` as the live promotion anchor

## 3) Default posture

The default preset is:
- `Comprehensive default (Recommended)`
- no explicit `day`, `session`, or `lookback` narrowing
- all four source classes enabled unless the operator narrows them
- `allow_same_day_widening = true`
- `max_historical_shards = 10`

## 4) Config location and contract

The default config target is now user-scope:
- `~/.claude/memory-context-intelligence.config.json`

The written file uses:
- `analysis.scope_policy`
- `analysis.source_policy`

`analysis.scope_policy` shape:
- `default_scope_mode`
- `scope_day_shard`
- `scope_session_id`
- `scope_lookback_minutes`

`analysis.source_policy` shape stays bounded to:
- `enabled_source_classes`
- `max_historical_shards`
- `allow_same_day_widening`

## 5) Precedence rules

Stored defaults apply only when the operator did not explicitly narrow the analysis run.

Priority order:
1. explicit runtime/slash narrowing
2. stored user-scope init config
3. built-in broad historical default

## 6) Operator flow

The init wizard should:
1. explain what it configures
2. offer `Comprehensive default (Recommended)`
3. allow explicit narrowing only if the operator chooses it
4. ask source-policy questions
5. show a final summary
6. confirm write
7. write `~/.claude/memory-context-intelligence.config.json`

## 7) Boundary notes

- user-scope config is now the selected default ownership model for this plugin
- project-local upward discovery is no longer the primary default path
- explicit `--config` remains allowed as an override/debug path
- the analysis surface may still show guided config questions when no config file is loaded, but the preferred setup path should point to `/memory-context-intelligence:init`

---

> Full history: [../changelog/changelog.md](../changelog/changelog.md)
