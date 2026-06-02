# governed-docs

`governed-docs` is a RULES-native maintenance companion for governed document families.

พูดง่าย ๆ คือมันช่วยตรวจดูว่า `README.md`, `design/`, `changelog/`, `TODO.md`, `phase/`, `patch/`, และ `diagram/` ของ workspace เป้าหมายยังอยู่ในรูปแบบที่สอดคล้องกับ RULES หรือไม่ โดยไม่ยึด ambient cwd เป็นตัวตัดสินเอง

<p align="center">
  <img src="img/GOD.png" alt="Governed Docs visual" width="520">
</p>

> ภาพนี้เป็น visual identity ของ plugin ตัวนี้ — จุดสำคัญคือมันสื่อว่า plugin นี้เป็นเครื่องมือฝั่ง governance/maintenance สำหรับ governed docs ไม่ใช่ semantic authority แทน RULES เอง

---

## At a glance

Use `governed-docs` when you need a **document-governance companion** that can:
- scan a named workspace for governed-document health
- classify drift and maintenance problem classes in RULES terms
- turn findings into a reviewable repair plan instead of mutating files silently
- give a release-gate style verdict before you claim docs are synchronized
- generate a root index preview flow for governed document navigation and review

This plugin stays on the **support side** of the boundary:
- RULES remains the semantic / doctrinal authority
- `governed-docs` helps you inspect, review, plan, gate, and preview governed documentation work safely

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
- root `<project>/index.html` as the only public root-index preview entry flow
- access-first workspace gate with a centered permission/login-like card, explicit expected workspace-path hint, required markers, and one primary `Grant workspace access` CTA
- metadata-only bootstrap manifest support state for the index flow under `preview/manifest.json`
- marker-based workspace validation before any live source sync is accepted
- post-grant live source-Markdown catalog enrichment for document titles, summaries, headings, content snippets, refs, warnings, and relation context
- post-grant `Explore | Content` shell with a shell-level search bridge that routes searches into Explore, focuses `#gd-global-search`, and keeps Explore as the grouped `Documents` / `Headings` / `Content` results home
- Content shell search handoff back into Explore search, while Content remains the live source-backed article reading surface
- route-aware Quick family links that switch to Explore and reveal/focus the target family without requiring manual expansion
- auto-detected governed families for design, changelog, todo, phase, patch, and diagram sources
- index-owned preview support state under `preview/**`, with project Markdown/doc files remaining the only semantic authority

This plugin is a maintenance/support companion only.

It does **not**:
- replace RULES as semantic authority
- guess a target workspace from ambient cwd
- auto-fix across approval boundaries
- rename or migrate governed files automatically
- turn hook reminders into hidden governance authority

---

## Typical workflows

### 1) Inspect a target workspace
Use this when you want to know whether a governed repo is structurally healthy.

```bash
./bin/governed-docs scan <explicit-target-workspace-path>
```

Expected result:
- a read-only inventory of governed surfaces
- doctrine-aware findings instead of raw file noise

### 2) Turn findings into a repair route
Use this when the scanner already found drift and you want a reviewable route before editing.

```bash
./bin/governed-docs repair-plan <explicit-target-workspace-path>
```

Expected result:
- grouped maintenance problems
- a bounded repair-plan shape instead of hidden mutation

### 3) Gate readiness / closeout claims
Use this before you say a governed documentation wave is synchronized or release-ready.

```bash
./bin/governed-docs release-gate <explicit-target-workspace-path>
```

Expected result:
- `pass`
- `pass-with-notes`
- `rework`
- `blocked`

### 4) Generate the governed-docs preview entrypoint
Use this when you want an index-driven preview shell for governed docs.

```bash
./bin/governed-docs index <explicit-target-workspace-path>
```

Expected result:
- root `index.html`
- metadata-only preview bootstrap state
- gated workspace access before any live source-backed reading begins

---

## Install and load this plugin

This plugin is included as a source package under the RULES repo local plugin marketplace.

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

If the plugin is already installed and the source version changes, update the installed copy first:

```text
/plugin update governed-docs@darkwingtm
```

If `/reload-plugins` is unavailable in the current environment, restart Claude Code or verify the installed version from a fresh Claude process before testing.

### 4) Verify the public entry surface

Start with one of these commands against an explicit target workspace:

```text
./bin/governed-docs scan <explicit-target-workspace-path>
./bin/governed-docs release-gate <explicit-target-workspace-path>
./bin/governed-docs index <explicit-target-workspace-path>
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
./bin/governed-docs index <explicit-target-workspace-path>
```

If the target path is missing, nonexistent, or is not a directory, the command fails closed. There is no ambient cwd fallback.

---

## Primary public commands

| Command | What it does |
|---|---|
| `scan` | Read-only inventory of governed surfaces in the named target workspace |
| `review` | Operator-facing review entry on top of the scanner/evaluator foundation |
| `repair-plan` | Converts doctrine findings into reviewable repair-plan items |
| `phase-audit` | Focused phase-shape / phase-lineage audit entry surface |
| `release-gate` | Produces `pass`, `pass-with-notes`, `rework`, or `blocked` from checked governed-surface state |
| `index` | The only public preview entry flow: generates root `<target>/index.html` plus metadata-only index support state for the root-index document portal |

---

## Index-backed preview model

`index` is the public preview path.

Current behavior in checked scope:
- `index` reads the named target workspace and generates root `index.html`
- before grant, the generated root entry stays gate-only: it shows a centered permission/login-like access card, the expected workspace path, the required markers `README.md`, `design/design.md`, `TODO.md`, and `phase/SUMMARY.md`, and one primary `Grant workspace access` CTA
- before grant, no sidebar, quick family links, semantic tree, global search, document lists, or article content are shown
- workspace access is browser-mediated through `showDirectoryPicker({ mode: 'read' })`, and the selected File System Access handle is accepted only after required-marker validation succeeds
- pre-grant `#doc=<sourceAuthorityPath>` routes with optional `&section=<anchor>` are held as pending intent and resume after successful workspace grant
- after grant, the connected shell exposes `Explore | Content`, a shell-level search bridge, and a secondary `Change workspace` utility action instead of a detached toolbar search field
- submitting the shell search routes the query into Explore, focuses `#gd-global-search`, and keeps Explore as the grouped `Documents` / `Headings` / `Content` results home
- Explore is the default post-grant panel when no pending deep link exists and presents the search command surface, grouped `Documents` / `Headings` / `Content` results, the semantic tree, and route-aware Quick family links from the granted live workspace
- Content renders live source-backed article reading with Source authority, section navigation, chain context, related-doc context, warnings, and live file metadata
- submitting the shell search from Content hands the query back to Explore search rather than keeping results inside the article panel
- Quick family links switch to Explore, update the family route, and reveal/focus the target family without opening a content document by default
- `preview/manifest.json` stays metadata-only bootstrap support state and does not store `contentHtml`, `fullHtml`, embedded Markdown bodies, or authoritative article content
- support output under `preview/**` remains non-authoritative runtime state owned by the index flow
- project Markdown/doc files remain the only content authority

Generated support state currently includes:

```text
index.html
preview/manifest.json
```

Fail-closed recovery in checked scope:
- unsupported Workspace Access API returns to the gate with an API-unavailable message
- denied/cancelled grant returns to the gate with retry messaging
- missing required markers block the selected workspace and report which markers are missing
- pre-grant document routes stay on a document-specific gate until access succeeds
- revoked/source-read failures return to a gate/retry surface such as `Choose workspace again` and do not fall back to cached or embedded governed content

---

## What this plugin is especially good at

This plugin is strongest when the problem is:
- cross-surface document drift
- uncertain document ownership
- release-readiness / no-drift review
- repair planning before mutation
- index-style governed document preview and exploration

It is weaker when the task is really about:
- product feature implementation
- semantic doctrine authoring itself
- destructive cleanup
- broad refactors that have not yet been reduced to a governed repair plan

---

## Project surfaces

Primary governed/current-state surfaces for this plugin-local chain:
- [README.md](README.md)
- [design/design.md](design/design.md)
- [changelog/changelog.md](changelog/changelog.md)
- [TODO.md](TODO.md)
- [phase/SUMMARY.md](phase/SUMMARY.md)
- [patch/](patch/)

Image assets used by this README:
- [`img/GOD.png`](img/GOD.png)

---

## Verification posture

Current local proof route for this chain is focused local verification:
- Python unit tests for scanner, evaluator, planner, executor-policy, release-gate, index flow, CLI routing, entry surfaces, and root-index script/runtime safety
- command smoke checks for repair-plan, release-gate, and `index`
- fresh local Chrome headless desktop + mobile screenshots for the centered cold gate on the generated root entry
- fresh local Chromium headless / Chrome DevTools Protocol walkthroughs using a mock directory-handle override for P003-06 shell search bridge routing, grouped Explore results, Content-to-Explore search handoff, route-aware Quick family reveal/focus, and `#doc=<sourcePath>&section=<anchor>` deep-link resume after grant
- checked local Chrome headless fail-closed recovery walkthroughs for unsupported access API, denied/cancelled grant, missing markers, and revoked/source-read failure

Evidence boundary:
- verified in checked local scope for the plugin workspace and the named target workspace used in verification
- the live article, marker-validation, fail-closed recovery, and post-grant shell proof used a checked local Chromium/Chrome DevTools Protocol headless runtime; the post-grant browser walkthroughs used a mock directory-handle override rather than real OS picker automation
- not a claim about external deployment, public hosting, real OS picker automation, or broader non-selected runtime environments
