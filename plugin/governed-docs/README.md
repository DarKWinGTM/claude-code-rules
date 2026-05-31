# governed-docs

`governed-docs` is a RULES-native maintenance companion for governed document families.

พูดง่าย ๆ คือมันช่วยตรวจดูว่า `README.md`, `design/`, `changelog/`, `TODO.md`, `phase/`, และ `patch/` ของ workspace เป้าหมายยังอยู่ในรูปแบบที่สอดคล้องกับ RULES หรือไม่ โดยไม่ยึด ambient cwd เป็นตัวตัดสินเอง

---

## Current state

Implemented and verified in checked local scope:
- explicit target-workspace-path gate
- read-only governed-surface scanner
- doctrine evaluator and maintenance problem-class classification
- repair-plan generation
- operator command/skill/agent entry surfaces
- bounded executor-policy preview path
- release-gate verdict flow
- `present-md` single-document preview rendering into root `preview/`
- `present-sync` full preview-portal rebuild/sync for governed source families

This plugin is a maintenance/support companion only.

It does **not**:
- replace RULES as semantic authority
- guess a target workspace from ambient cwd
- auto-fix across approval boundaries
- rename or migrate governed files automatically
- turn hook reminders into hidden governance authority

---

## Install and load this plugin

This plugin is now included as a source package under the RULES repo local plugin marketplace.

Portable placeholder:
- `<rules-repo-root>` = the path to your local `TEMPLATE/RULES` checkout

Current checked marketplace source file:
- `<rules-repo-root>/plugin/.claude-plugin/marketplace.json`

Recommended install flow inside Claude Code:

### 1) Add the local marketplace

```text
/plugin marketplace add <rules-repo-root>/plugin
```

Or point directly to the marketplace file:

```text
/plugin marketplace add <rules-repo-root>/plugin/.claude-plugin/marketplace.json
```

### 2) Install governed-docs

```text
/plugin install governed-docs@darkwingtm
```

### 3) Reload plugins

```text
/reload-plugins
```

### 4) Verify the public entry surface

Start with one of these commands against an explicit target workspace:

```text
./bin/governed-docs scan <explicit-target-workspace-path>
./bin/governed-docs release-gate <explicit-target-workspace-path>
./bin/governed-docs present-md <explicit-target-workspace-path> <source-markdown-relative-path>
./bin/governed-docs present-sync <explicit-target-workspace-path>
```

Boundary:
- the marketplace entry identifies the local source package only
- it does not by itself prove runtime load, persistent install, or external marketplace publication

---

## Required command contract

Every user-facing operation requires an explicit target workspace path.

Generic shape:

```bash
./bin/governed-docs <command> <explicit-target-workspace-path> [extra-args]
```

Examples:

```bash
./bin/governed-docs scan <explicit-target-workspace-path>
./bin/governed-docs repair-plan <explicit-target-workspace-path>
./bin/governed-docs release-gate <explicit-target-workspace-path>
./bin/governed-docs present-md <explicit-target-workspace-path> <source-markdown-relative-path>
```

If the target path is missing, invalid, or points outside the allowed workspace scope, the command fails closed.

---

## Available commands

| Command | What it does |
|---|---|
| `scan` | Read-only inventory of governed surfaces in the named target workspace |
| `review` | Operator-facing review entry on top of the scanner/evaluator foundation |
| `repair-plan` | Converts doctrine findings into reviewable repair-plan items |
| `phase-audit` | Focused phase-shape / phase-lineage audit entry surface |
| `release-gate` | Produces `pass`, `pass-with-notes`, `rework`, or `blocked` from checked governed-surface state |
| `present-md` | Renders one governed-docs-owned document page into the root `preview/` portal structure |
| `present-sync` | Rebuilds and resyncs the full root `preview/` portal, manifest, and family pages from governed source docs |

---

## Markdown article presentation

`present-md` is governed-docs-owned presentation work.

Current behavior in checked scope:
- `present-md` reads one governed Markdown/doc source that must stay inside the named target workspace
- `present-md` renders a safe article-style HTML page with TOC support
- `present-md` blocks unsafe link schemes such as `javascript:` and `data:`
- `present-md` writes into the root preview portal structure, for example:

```text
preview/design/<slug>/index.html
preview/todo/index.html
preview/phase/index.html
```

- `present-sync` rebuilds the full preview portal from governed source families and writes:

```text
preview/index.html
preview/manifest.json
preview/<family>/<slug>/index.html
```

The `preview/` tree is a presentation/support surface only, not a governed source-of-truth document family.

NodeClaw article behavior was used only as a checked reference input for design direction. Ownership of this implementation remains inside `governed-docs`.

---

## Project surfaces

Primary governed/current-state surfaces for this plugin-local chain:
- [README.md](README.md)
- [design/design.md](design/design.md)
- [changelog/changelog.md](changelog/changelog.md)
- [TODO.md](TODO.md)
- [phase/SUMMARY.md](phase/SUMMARY.md)
- [patch/](patch/)

---

## Verification posture

Current local proof route for this chain is focused local verification:
- Python unit tests for scanner, evaluator, planner, executor-policy, release-gate, and article presentation
- command smoke checks for repair-plan, release-gate, and present-md

Evidence boundary:
- verified in checked local scope for the plugin workspace and the named target workspace used in verification
- not a claim about external deployment, public hosting, or broader non-selected runtime environments
