# Playground Virtual Case Matrix

## Purpose

This file explores virtual-case combinations for the playground family.

Every row here is virtual unless it explicitly links to a checked observed case elsewhere.

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
| Request type | setup / diagnosis / implementation / docs sync / risky action / external fact / explanation |
| Evidence state | verified / partial / conflicting / missing / user concern only |
| Scope clarity | clear / mixed / ambiguous |
| Risk level | low / medium / high |
| Expected rule response | continue / verify first / ask / route worker / refuse with path / confirm before mutate |

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
| M04 | user proposal + material trade-offs + partial evidence | evaluate before agreeing | communication and presentation calibration |
| M05 | external SDK behavior + current version unclear | fetch authoritative external docs first | external, memory, and portability boundary |
| M06 | post-compact resume + stale option branches | re-anchor to latest user directive before continuing | authority collision resolver |
| M07 | customer-facing copy + sensitive internal mechanism | split direct-user explanation from external-safe wording | audience-safe disclosure split |
| M08 | implementation done + no tests run yet | report implemented, not fixed | coding change with verification discipline |
| M09 | active phase closed + next lane broad and noisy | continue through worker-routed next lane | execution continuity and worker routing |
| M10 | changelog/design/TODO/phase drift risk | sync owner surfaces before claiming release-ready | governed artifact lifecycle |
| M11 | user claim of root cause + only one plausible branch | state likely cause or working hypothesis, not verified cause | evidence-calibrated diagnosis |
| M12 | shared doc wants local absolute path as default | convert to placeholder or config binding | external, memory, and portability boundary |

---

## Matrix use rules

- matrix rows stay virtual unless linked to checked observed evidence
- matrix rows should point back to at least one scenario family
- matrix rows may explore several branches, but they must not invent new RULES capability
- when a virtual row later becomes a checked observed case, record it in `observed/YYYY-MM.md` and update the linked scenario file
