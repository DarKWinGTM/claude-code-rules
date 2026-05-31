# memory-context-intelligence

> **Status:** Usable in checked scope for `/memory-context-intelligence:analysis`; `review` and `packet` remain deferred
> **Current Version:** 0.1.72
> **Plugin Package Version:** 0.9.25
> **Session:** d42465eb-30a7-4bc8-b9d6-03e52306e9a5 (2026-06-01)

---

## What this plugin does

`memory-context-intelligence` is a Claude Code plugin that reads bounded work evidence from prepared memory traces and turns it into topic cards that help you spot recurring workflow, RULES, and operating-pattern issues worth reviewing.

In plain terms, this plugin is not for writing product features directly. It is for questions like:
- Are we getting stuck on the same workflow problem repeatedly?
- Is there a RULES gap that should be turned into a proposal?
- Which governance or workflow topic should we investigate first to improve the next wave of work?

Current checked public surface:
- `/memory-context-intelligence:analysis`

Current checked behavior that matters:
- the default mode is **historical-first analysis**, not current-session-only summary
- `trace_evidence` remains the live promotion anchor
- `recall_evidence`, `durable_memory_context`, and `governance_context` can strengthen wording and context, but they do not replace trace proof
- if no config file is loaded, the plugin can show a **guided config helper** instead of expecting raw arguments as the normal UX

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

## Install Claude Code

Install Claude Code first, then install this plugin.

### Linux / WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows PowerShell

```powershell
irm https://claude.ai/install.ps1 | iex
```

### Windows CMD

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

Notes:
- On native Windows, **Git for Windows is recommended** so Claude Code can use the Bash tool.
- If Git for Windows is not installed, Claude Code falls back to PowerShell as its shell tool.
- After installation, start Claude Code with:

```bash
claude
```

If you have not logged in yet, do it inside the session with:

```text
/login
```

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
- then call the slash surface below

## First use: start with `/memory-context-intelligence:analysis`

### Minimal first run

Inside the Claude Code session you want to analyze, run:

```text
/memory-context-intelligence:analysis
```

This is the current checked public entrypoint and should be your normal starting point.

### What you should expect

If usable evidence is available, you should get topic-card output such as:
- `Topic 1`, `Topic 2`, `Topic 3`
- each card explains what the topic is about
- why it surfaced from evidence
- what the before/after behavior looks like
- that the result is still `candidate only; advisory only; not approved yet`

At the end of the output, you should also see `Next action options`, such as:
- choose a topic number
- type a direct request
- ask for deep thinking, websearch, or webfetch first

### If no config file is loaded

If the current run does not load `memory-context-intelligence.config.json`, you should see a **Config helper** that asks operator-facing questions such as:
- should the default scope stay historical-first or narrow down
- which source classes should stay enabled
- whether same-day widening should be allowed
- whether the next config choice should be saved as a project default or used once

Important boundary:
- the helper is **advisory only**
- the plugin does **not** auto-write config files for you
- it helps you choose a source policy, then you decide whether to create the file yourself

## Optional config file

If you want explicit source-policy control, create a file named:

```text
memory-context-intelligence.config.json
```

The runtime looks for this file through **upward discovery** from the current working directory.

Example shape:

```json
{
  "analysis": {
    "source_policy": {
      "enabled_source_classes": [
        "trace_evidence",
        "recall_evidence",
        "durable_memory_context",
        "governance_context"
      ],
      "max_historical_shards": 5,
      "allow_same_day_widening": true
    }
  }
}
```

Current checked keys:
- `enabled_source_classes`
- `max_historical_shards`
- `allow_same_day_widening`

Important behavior:
- this config file is a **late-bound source policy** only
- it does not create a fifth evidence class
- it does not weaken the role of `trace_evidence` as the live promotion anchor
- if you disable `trace_evidence` or leave only context-only sources in scope, the result must not be overclaimed as a promotable live candidate

## Boundaries you should know

Current checked boundaries for this plugin:
- the only proved public surface is `/memory-context-intelligence:analysis`
- bare `/analysis` is **not** current proved runtime behavior
- `/memory-context-intelligence:review` and `/memory-context-intelligence:packet` are still deferred
- `bin/memory-context-intelligence` is an internal implementation adapter, not the main user workflow
- plugin-managed auto-flow is not currently claimed as proved behavior
- this README does not claim external marketplace publication or broad production readiness

In plain terms: after installation, you should expect an **analysis command that you run when you want a workflow-pattern review**, not a plugin that silently runs itself all the time.

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

## Current truth summary

If you want the shortest version, remember these 5 steps:
1. install Claude Code first
2. add the local marketplace from `<template-root>`
3. install `memory-context-intelligence@darkwingtm`
4. run `/reload-plugins`
5. start with `/memory-context-intelligence:analysis`

If your first run does not load a config file yet, that is fine — the plugin should guide you with the config helper instead of forcing raw arguments as the normal starting UX.