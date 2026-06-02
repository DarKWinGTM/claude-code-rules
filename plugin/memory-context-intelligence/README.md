# memory-context-intelligence

> **Status:** Plugin-scoped init-configuration surface completed in checked scope; `/memory-context-intelligence:init` now owns guided setup, `/memory-context-intelligence:analysis` remains the review surface, `review` and `packet` remain deferred, and packet/additional emission stays one-topic-per-artifact
> **Current Version:** 0.1.77
> **Plugin Package Version:** 0.9.29
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-02)

---

## What this plugin does

`memory-context-intelligence` is a Claude Code plugin that reads bounded work evidence from prepared memory traces and turns it into topic cards that help you spot recurring workflow, RULES, and operating-pattern issues worth reviewing.

In plain terms, this plugin is not for writing product features directly. It is for questions like:
- Are we getting stuck on the same workflow problem repeatedly?
- Is there a RULES gap that should be turned into a proposal?
- Which governance or workflow topic should we investigate first to improve the next wave of work?

<p align="center">
  <img src="img/MCI.png" alt="Memory Context Intelligence visual" width="520">
</p>

> ภาพนี้เป็น visual identity ของ plugin ตัวนี้ — มันสื่อแนวคิดหลักของ plugin ว่าใช้ memory + context + evidence เพื่อช่วย review pattern การทำงาน ไม่ใช่เพื่อกระโดดไปแก้ product code ตรง ๆ

Current checked public surfaces:
- `/memory-context-intelligence:analysis`
- `/memory-context-intelligence:init`

Current checked behavior that matters:
- the default mode is **historical-first analysis**, not current-session-only summary
- `trace_evidence` remains the live promotion anchor
- `recall_evidence`, `durable_memory_context`, and `governance_context` can strengthen wording and context, but they do not replace trace proof
- when adaptive deep-analysis marks a top topic as requiring deeper review, the checked current skill contract now requires one **bounded read-only deepening pass** before the first response instead of silently skipping it
- that deepening can use read-only subagent help plus optional web/external research support, but it still stays advisory-only and cannot replace local trace proof
- if several advisory topics are deepened or compared, any later packet-derived or additional-stage output must still keep **one selected topic per artifact** and must **split into separate per-topic artifacts** instead of emitting a combined file
- if no config file is loaded, the plugin can show a **guided config helper** and point the operator to `/memory-context-intelligence:init` instead of expecting raw arguments as the normal UX
- the default config target is now the user-scope file `~/.claude/memory-context-intelligence.config.json`

---

## At a glance

Use this plugin when you want an **evidence-first reflection tool** that can:
- scan historical work traces for repeated workflow/RULES issues
- surface candidate topics before you decide what to improve next
- keep trace evidence as the live anchor while still benefiting from recall, durable memory, and governance context
- offer a guided setup path so the normal UX does not depend on raw config arguments

This plugin is especially useful after a work stretch when you want to understand:
- what keeps repeating
- what should become a proposal next
- which issue is worth investigating first

---

## When to use it

Use this plugin when you want Claude Code to review your past work patterns in an evidence-first way, for example:
- after a stretch of work, when you want to see which blockers keep repeating
- when you want candidate topics for improving RULES, workflow, or governance
- when you want a broader historical review instead of a narrow current-session-only summary
- when you want to limit source classes or historical depth through a config file without changing the core evidence model

This is **not** the right tool when you want to:
- jump straight into fixing product code without caring about trace history
- treat bare `/analysis` as the public command
- rely on the plugin to auto-run in the background through hooks or monitors

---

## Install and load this plugin

In checked scope, this plugin is currently distributed through a **local marketplace named `darkwingtm`** at the root `TEMPLATE` directory, and its marketplace entry points to:
- `./RULES/plugin/memory-context-intelligence`

That means the current end-user flow is:

### 1) Prepare a local checkout of TEMPLATE

You need a local `TEMPLATE` directory on your machine, and its root must contain `.claude-plugin/marketplace.json`.

Portable placeholder:
- `<template-root>` = the path to your local `TEMPLATE` directory

Example path shapes:
- Linux / WSL: `/home/<user>/work/TEMPLATE`
- Windows: `C:\Users\<user>\work\TEMPLATE`

### 2) Add the marketplace

Inside Claude Code, add the marketplace from the local path:

```text
/plugin marketplace add <template-root>
```

If you prefer to point directly to the file:

```text
/plugin marketplace add <template-root>/.claude-plugin/marketplace.json
```

### 3) Install the plugin

```text
/plugin install memory-context-intelligence@darkwingtm
```

The checked Claude Code plugin docs say that direct installs like this use **user scope by default**.

If you want a different scope:
- open `/plugin`
- go to Discover or the plugin details view
- choose `user`, `project`, or `local`

### 4) Reload plugins

```text
/reload-plugins
```

### 5) Verify the install

The simplest verification path is:
- open `/plugin` and confirm the plugin is installed and enabled
- then call the slash surfaces below

---

## First use workflow

### Step 1 — guided setup

Inside the Claude Code session, run the setup surface first:

```text
/memory-context-intelligence:init
```

That flow should use question/choice dialogs, default to `Comprehensive default (Recommended)`, and write:

```text
~/.claude/memory-context-intelligence.config.json
```

### Step 2 — run the analysis surface

After setup, your normal review command remains:

```text
/memory-context-intelligence:analysis
```

### What you should expect

If usable evidence is available, you should get topic-card output such as:
- `Topic 1`, `Topic 2`, `Topic 3`
- each card explains what the topic is about
- why it surfaced from evidence
- what the before/after behavior looks like
- that the result is still `candidate only; advisory only; not approved yet`
- multiple topic cards are still advisory comparison output only; they are not a combined packet/additional artifact candidate
- when the adaptive payload flags a top topic for deeper review, the first response may now include one bounded read-only deepening pass before the cards are finished, while still keeping the final result advisory-only and trace-anchored

At the end of the output, you should also see `Next action options`, such as:
- choose a topic number
- type a direct request
- ask for deep thinking, websearch, or webfetch first

### If no config file is loaded

If the current run does not load `~/.claude/memory-context-intelligence.config.json`, you should see a **Config helper** that points you toward `/memory-context-intelligence:init` and asks operator-facing questions such as:
- should the default scope stay broad historical-first or narrow down
- which source classes should stay enabled
- whether same-day widening should be allowed
- whether the next config choice should be written now

Important boundary:
- the helper is still **advisory only** inside `/memory-context-intelligence:analysis`
- the dedicated write path now belongs to `/memory-context-intelligence:init`
- `/memory-context-intelligence:analysis` remains the review surface

---

## Default config file

The default config target is now:

```text
~/.claude/memory-context-intelligence.config.json
```

The preferred way to create/update it is:

```text
/memory-context-intelligence:init
```

Example shape:

```json
{
  "analysis": {
    "scope_policy": {
      "default_scope_mode": "historical-comprehensive",
      "scope_day_shard": null,
      "scope_session_id": null,
      "scope_lookback_minutes": null
    },
    "source_policy": {
      "enabled_source_classes": [
        "trace_evidence",
        "recall_evidence",
        "durable_memory_context",
        "governance_context"
      ],
      "max_historical_shards": 10,
      "allow_same_day_widening": true
    }
  }
}
```

Current checked keys:
- `default_scope_mode`
- `scope_day_shard`
- `scope_session_id`
- `scope_lookback_minutes`
- `enabled_source_classes`
- `max_historical_shards`
- `allow_same_day_widening`

Important behavior:
- this config file is a late-bound analysis default, not semantic authority
- `scope_policy` defines the stored default scope, but explicit runtime narrowing still wins
- `source_policy` stays bounded to source classes, shard cap, and same-day widening
- it does not create a fifth evidence class
- it does not weaken the role of `trace_evidence` as the live promotion anchor
- if you disable `trace_evidence` or leave only context-only sources in scope, the result must not be overclaimed as a promotable live candidate

---

## Boundaries you should know

Current checked boundaries for this plugin:
- the proved public analysis surface is `/memory-context-intelligence:analysis`
- the setup/configuration surface is `/memory-context-intelligence:init`
- bare `/analysis` is **not** current proved runtime behavior
- `/memory-context-intelligence:review` and `/memory-context-intelligence:packet` are still deferred
- `bin/memory-context-intelligence` is an internal implementation adapter, not the main user workflow
- packet/additional-stage emission remains a single-topic-per-artifact flow; if several topics are ever carried forward, they must split into separate per-topic artifacts rather than one combined file
- plugin-managed auto-flow is not currently claimed as proved behavior
- this README does not claim external marketplace publication or broad production readiness

In plain terms: after installation, you should expect an **analysis command that you run when you want a workflow-pattern review**, plus a dedicated init/setup surface — not a plugin that silently runs itself all the time.

---

## Troubleshooting

### `/memory-context-intelligence:analysis` does not appear or does not work

Check in this order:
1. run `/reload-plugins`
2. open `/plugin` and confirm the plugin is still installed and enabled
3. confirm the installed source is `memory-context-intelligence@darkwingtm`
4. if the plugin was updated while this session was already running, restart the Claude Code session and retry

### `memory-context-intelligence@darkwingtm` will not install

This is usually a marketplace-path problem.

Check that:
- you added the correct `<template-root>` marketplace path
- the root of that path contains `.claude-plugin/marketplace.json`
- the marketplace entry for `memory-context-intelligence` still points to `./RULES/plugin/memory-context-intelligence`

### The result is `blocked`, `dormant`, or `no-topics`

That does not automatically mean the plugin is broken.

Typical meanings:
- `blocked` = required analysis input or dependency is not ready
- `dormant` = the available memory input is too stale
- `no-topics` = there is not yet a repeated enough pattern to promote into a proposal

What to do next:
- keep working until there is more trace history to analyze
- adjust source policy or historical depth if needed
- use a narrower scope intentionally if that better fits the review you want

### The session is old and behavior does not match the latest source

The current checked contract includes an advisory warning named `possible stale long-lived session`.

If you see it:
- restart the Claude Code session
- run `/memory-context-intelligence:analysis` again

This is only a temporary diagnostic safeguard. It does **not** mean long-lived session mismatch is considered normal behavior.

---

## Advanced notes

### Evidence model at a glance

The current implemented evidence model uses 4 classes:
- `trace_evidence`
- `recall_evidence`
- `durable_memory_context`
- `governance_context`

Core rules:
- `trace_evidence` remains the live anchor
- source mix should stay visible when durable memory or governance context materially shaped a candidate
- historical-first is the default, but explicit narrowing is still available when the operator wants it

### Narrowing runs intentionally

If you want a narrower review slice, the current design still supports concepts such as:
- `day=YYYY-MM-DD`
- `session=<id>`
- `lookback=<minutes|hours>`

But the checked public UX is intentionally built around the slash surface and guided helper first, not around making raw arguments the main normal path.

### What this plugin is not

This plugin is not:
- an automatic rule writer
- a background monitor
- proof that bare `/analysis` is publicly available
- a shortcut for bypassing evidence gates
- a replacement for real work traces

A better mental model is:
- `historical workflow reviewer`
- `RULES / governance topic suggester`
- `evidence-first reflection tool`

---

## Current truth summary

If you want the shortest version, remember these 5 steps:
1. add the local marketplace from `<template-root>`
2. install `memory-context-intelligence@darkwingtm`
3. run `/reload-plugins`
4. run `/memory-context-intelligence:init`
5. use `/memory-context-intelligence:analysis`

Image asset used by this README:
- [`img/MCI.png`](img/MCI.png)

If your first run does not load a config file yet, that is fine — the plugin should guide you with the config helper and `/memory-context-intelligence:init` instead of forcing raw arguments as the normal starting UX.
