# Purpose, Scope, and Boundary

## 0) Document Control

> **Parent Scope:** governed-docs plugin-local governed design chain
> **Current Version:** 0.1.0
> **Session:** b7f7ee85-27ec-467a-ba63-568c831fcd36 (2026-05-31)
> **Parent Design:** [design.md](design.md)

---

## 1) Goal

Define the purpose, first-release scope, and hard boundaries for a deep companion plugin that helps keep governed RULES documents consistent, reviewable, and aligned to existing RULES doctrine.

## 2) Core direction

พูดง่าย ๆ: plugin นี้ไม่ใช่เจ้าของกฎใหม่ แต่เป็นผู้ช่วยคอยประกบงานเอกสาร governed surfaces ให้หลุดจาก RULES ยากขึ้น, ตรวจ drift ได้เร็วขึ้น, และเตรียมทางซ่อมให้เป็นระบบมากขึ้น.

## 3) Plugin purpose

The `governed-docs` plugin exists to:
- inspect governed document surfaces and their supporting doctrine inputs
- classify maintenance and consistency issues against existing RULES
- produce bounded maintenance recommendations or repair packages
- optionally normalize deterministic low-risk issues inside an approval-aware boundary
- help release/closeout wording stay aligned to checked evidence

## 4) Explicit v1 scope

V1 is intentionally narrow:
- RULES-specific first, not a generic framework
- design/docs wave only in the current goal
- target model covers only the governance companion concept and its design structure
- the intended document family is the RULES governed ecosystem: `README`, `design`, `changelog`, `TODO`, `phase`, `patch`, and related `history/` / `done/` surfaces
- every user-facing operation must be given an explicit target workspace path so the plugin knows exactly which governed project tree to inspect

## 5) Non-goals

### What v1 is not

V1 is not:
- a semantic authority replacement for RULES
- a repo-wide formatter bot
- an auto-cleanup engine
- a hidden hook-owned governance system
- a proof that the same model should apply to every other repo immediately
- a runtime implementation wave for skills, custom agents, or hooks

### Authority non-goal

The plugin must not become the semantic owner of governed surfaces. It may inspect, classify, and prepare maintenance work, but it must not replace root RULES as the meaning owner.

## 6) RULES-vs-plugin boundary

### RULES owns
- semantic meaning of document roles
- parent/shard/changelog chain doctrine
- phase identity and lineage doctrine
- rollover and preservation rules
- evidence wording and release-claim strength
- destructive and approval boundaries

### Plugin owns
- structured inspection of current state
- operational classification of drift against RULES
- maintenance recommendation packaging
- bounded normalization for deterministic low-risk issues once allowed
- release-gate style operator support
- strict target-workspace gating so user-facing operations fail closed when the working path is not explicitly provided

### Plugin must not do
- redefine RULES semantics locally
- auto-promote legacy observations into forward-valid doctrine
- decide that cleanup or file absence authorizes deletion
- become the semantic owner of `README`, `design`, `changelog`, `TODO`, `phase`, or `patch`

## 7) Before / After behavior

### Before
- operators must repeatedly remember RULES-specific document maintenance doctrine themselves
- malformed phase naming, stale summary layout, or role-drift problems can sit around until explicitly noticed
- release/closeout wording drift is easy to miss when the repo state spans many governed surfaces
- deterministic low-risk maintenance tasks still require manual orchestration each time

### After
- governed surfaces can be scanned through one consistent companion model
- the plugin can explain whether something is compliant, legacy-only, drift, or blocked
- deterministic maintenance work can be prepared in a predictable, reviewable way
- release/closeout support can catch cross-surface drift before stronger claims are made

## 8) Non-goals for automation risk

The plugin must not, by default:
- rename files because a pattern looks malformed
- rewrite authority boundaries silently
- move or delete history/done material without an explicit safe route
- patch release wording from assumptions rather than checked evidence
- auto-correct phase lineage or major/subphase meaning from filename shape alone
- escalate into a generic abstraction model before RULES-specific use proves the stable core
- continue from ambient cwd when a user-facing command omitted the target workspace path

---

> V1 stays RULES-specific on purpose. A generic framework may be extracted later only after repeated successful use shows which parts are truly reusable and which remain RULES doctrine-specific.
