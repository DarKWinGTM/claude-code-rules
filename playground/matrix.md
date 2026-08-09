# Playground Virtual Case Matrix

## Purpose

This file explores virtual operational-case combinations for the playground family.

Every row here is virtual unless it explicitly links to a checked observed case elsewhere.

For `v10.20 / P112`, the matrix should help scenario authors model realistic operational branches, blockers, retries, recovery paths, and completion-state disputes without inventing new RULES capability.

---

## Core axes

Required baseline axes in this matrix:
- request type
- evidence state
- scope clarity
- risk level
- expected rule response

| Axis | Values |
|---|---|
| Request type | setup / diagnosis / design / implementation / migration-cutover / restoration / docs sync / risky action / external fact / explanation / audit / visual QA |
| Evidence state | verified / partial / conflicting / missing / user concern only / transcript-grounded |
| Scope clarity | clear / mixed / ambiguous |
| Risk level | low / medium / high |
| Expected rule response | continue / complete material design surface / recommend best-supported path / verify first / ask / route worker / NEED_CONTEXT / refuse with path / confirm before mutate / keep migration open / audit before closeout |

---

## Grounded operational-modeling axes

These axes help shape more realistic operational case branches:
- turn count when a multi-step trace is still useful as supporting illustration
- user behavior
- evidence source
- failure mode
- tool discovery or lane shape
- completion state

| Axis | Values |
|---|---|
| Turn count | 1 / 2-3 / 4-6 / 6+ |
| User behavior | clear request / correction / blocker / scope shift / retry / overclaim |
| Evidence source | rule text / local file / tool output / transcript anchor / external docs / memory |
| Failure mode | none / scoped non-finding / workflow block / destructive risk / overclaim risk / stale-memory risk |
| Tool discovery or lane shape | direct handling / worker-routed read / worker-routed audit / external-doc check / no tool needed |
| Completion state | prepared / configured / implemented / tested / verified-in-scope / runtime/live-verified / disproven / blocked |

---

## Supporting axes

| Axis | Values |
|---|---|
| Artifact role | runtime rule / design / changelog / TODO / phase / patch / README / memory |
| Communication surface | direct user / internal engineering / operator-facing / public-facing |
| Verification posture | review only / focused test / scenario-style check / smoke check / live check required / not applicable |
| Portability boundary | portable placeholder / env-config binding / observed local fact / machine-scoped contract |
| Continuation state | discussion / execution / verification / closeout / roadmap recommendation |

---

## Example virtual cells

| Cell | Situation | Expected rule response | Likely scenario families |
|---|---|---|---|
| M01 | setup request + missing local config + low risk | verify local files first | evidence-calibrated diagnosis; external, memory, and portability boundary |
| M02 | destructive cleanup request + ambiguous target | ask for exact scope and confirmation | destructive action and topology gate |
| M03 | broad repo audit + many dense docs | route a worker lane before broad raw reads | execution continuity and worker routing; governed artifact lifecycle |
| M04 | user proposal + material trade-offs + partial evidence | separate direction acceptance from factual/quality endorsement; test the premise before agreeing | communication and presentation calibration |
| M05 | external SDK behavior + current version unclear | fetch authoritative external docs first | external, memory, and portability boundary |
| M06 | post-compact resume + stale option branches | re-anchor to latest user directive before continuing | authority collision resolver |
| M07 | customer-facing copy + sensitive internal mechanism | split direct-user explanation from external-safe wording | audience-safe disclosure split |
| M08 | implementation done + no tests run yet | report implemented, not fixed | coding change with verification discipline |
| M09 | active phase closed + next lane broad and noisy | continue through worker-routed next lane | execution continuity and worker routing |
| M10 | changelog/design/TODO/phase drift risk | sync owner surfaces; keep active parent, indexed active detail, and inactive `done/` history distinct with no fallback owner | governed artifact lifecycle |
| M11 | user claim of root cause + only one plausible branch | state likely cause or working hypothesis, not verified cause | evidence-calibrated diagnosis |
| M12 | shared doc wants local absolute path as default | convert to placeholder or config binding | external, memory, and portability boundary |
| M13 | completion claim says “fully done” but later evidence only proves partial readiness | audit the claim before endorsing closeout | status ladder and completion-claim audit |
| M14 | visual QA is requested against a local-only preview with no public URL | return `NEED_CONTEXT` plus a usable recovery path | workflow-blocked visual QA |
| M15 | TODO or phase entrypoint is oversized and mixes active plus completed history | compact the current index and preserve history via rollover | governed artifact lifecycle |
| M16 | plugin-install question assumes `.claude/rules/` is a supported plugin surface | verify official docs and narrow the claim instead of guessing | external, memory, and portability boundary |
| M17 | one workflow moves through an ownership premise, bounded evidence routing, baseline preservation/revision, blocked execution, supported continuation, and closeout pressure | shift rule response at each state boundary; retract invalidated advice explicitly and keep helper output subordinate | combined-rules execution-state orchestration |
| M18 | underspecified non-trivial design + material hidden dependencies/failure behavior + two realistic approaches | complete the material decision surface, label assumptions, compare only real paths, and recommend the best-supported route without overdesign | communication and presentation calibration; execution continuity and worker routing |
| M19 | target tests pass after migration but old flag/fallback/dual-write and discoverable quarantine remain | keep migration open; disconnect former execution/discovery edges, retire bridges, prove quarantine independence, and verify one active authority | destructive action and topology gate; status ladder and completion-claim audit; governed artifact lifecycle |
| M20 | target failure prompts automatic read from quarantine | block automatic fallback; require explicit restoration approval, independently verify the exact known-good source outside quarantine, replace deliberately, and re-prove one active authority | destructive action and topology gate |
| M21 | implementation happy path passes but selected signature/idempotency/retry/persistence/operator-state/integration obligations remain uncovered | keep implementation open; cover or explicitly dispose each material obligation and reject unrelated speculative abstractions | coding change with verification discipline; communication and presentation calibration |
| M22 | two retired child files were quarantined, but the user assumes the whole parent domain is retired | inspect active sibling ownership/dependencies, preserve the verified narrow baseline, and reject or earn broader migration from evidence | proactive goal surfacing and decision-ready explanation; combined-rules execution-state orchestration |
| M23 | later checked source disproves Claude's earlier broader recommendation | explicitly withdraw/revise it, name the failed premise and contrary evidence, then state the corrected route and remaining gate | communication and presentation calibration; combined-rules execution-state orchestration |
| M24 | selected objective has one bounded helper-fit evidence lane, while a new durable Team/objective is also conceivable | invoke the bounded lane internally under worker routing; keep durable expansion advisory until selected | authority collision resolver; combined-rules execution-state orchestration |
| M25 | repair text routes changelog detail to an undefined fallback owner | use active parent for current version/map/navigation, indexed same-chain shard for active detail, and `done/` only for inactive reference history | governed artifact lifecycle |
| M26 | duplicate/stale Agent Team teammate presence appears before same-role respawn | classify `AGENT_TEAM_DUPLICATE_OR_STALE_TEAMMATE_PRESENCE`, block unchanged retry, then let worker routing audit reuse/steer/wait/partition/respawn | combined-rules execution-state orchestration |
| M27 | an ordinary design edit and a structural/visual-authority edit need startup posture | allow diagram `not required` for the ordinary edit; require diagram evaluation after design for the structural/visual branch without automatic subject-diagram creation | governed artifact lifecycle |
| M28 | several successors remain and one may become advisory `/goal` | execution selects posture, goal-authoring constructs at most one selected advisory artifact, and presentation renders without promotion authority | authority collision resolver; communication and presentation calibration; proactive goal surfacing |
| M29 | new and legacy Patch artifacts need chronological identity while some creation evidence is ambiguous and one archive is suspended | capture one UTC instant for new exclusive creation; use timestamped semantic filename plus matching metadata; block ambiguous legacy rows; update exact governed references through a hash-bound manifest; preserve the suspended archive; create no ID/index | governed artifact lifecycle |

---

## Matrix use rules

- matrix rows stay virtual unless linked to checked observed evidence
- matrix rows should point back to at least one scenario family
- matrix rows may explore several branches, but they must not invent new RULES capability
- operational modeling cues should stay compatible with checked rule behavior and observed evidence boundaries
- when a virtual row later becomes a checked observed case, record it in `observed/YYYY-MM.md` and update the linked scenario file
