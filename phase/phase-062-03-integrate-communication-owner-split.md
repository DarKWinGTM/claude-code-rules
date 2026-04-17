# Phase 062-03 - Integrate communication owner split

> **Summary File:** [SUMMARY.md](SUMMARY.md)
> **Phase ID:** 062-03
> **Status:** Completed
> **Design References:** [../design/technical-snapshot-communication.design.md](../design/technical-snapshot-communication.design.md), [../design/response-closing-and-action-framing.design.md](../design/response-closing-and-action-framing.design.md), [../design/accurate-communication.design.md](../design/accurate-communication.design.md), [../design/design.md](../design/design.md)
> **Patch References:** [../patch/accurate-communication-owner-extraction.patch.md](../patch/accurate-communication-owner-extraction.patch.md)

---

## Objective

Integrate the two new communication specialist owners into the touched runtime/design/changelog companions and master governance surfaces.

## Why this phase exists

The new owners only become operationally real when `accurate-communication` narrows cleanly, adjacent integrations stop pointing the extracted domains at the old owner, and the master surfaces record the new chains coherently.

## Entry conditions / prerequisites

- `062-01` and `062-02` are complete
- the governed patch artifact for this wave already exists
- the extraction remains bounded and avoids unnecessary expansion into unrelated owner chains

## Action points / execution checklist

- [x] narrow `accurate-communication` to the broader communication-owner role
- [x] retarget touched adjacent integrations where snapshot or closing/action ownership moved
- [x] update design/changelog companions for touched chains
- [x] update master design/README/changelog/TODO/phase surfaces
- [x] prepare runtime-install sync for all touched active rules

## Out of scope

- unrelated communication-owner rewrites
- moving execution-mode ownership into the new closing chain
- moving evidence taxonomy ownership into the new snapshot chain

## Affected artifacts

- `accurate-communication.md` and companions
- `answer-presentation.md` and companions
- `explanation-quality.md` and companions
- `design/design.md`
- `README.md`
- `changelog/changelog.md`
- `TODO.md`
- `phase/SUMMARY.md`
- installed runtime copies for touched rules

## Verification

- [x] `accurate-communication` now defers the extracted specialist domains instead of owning them directly
- [x] touched adjacent integrations point to the correct new owners where appropriate
- [x] master surfaces record both new chains coherently

## Risks / rollback notes

- sync drift can survive even if the new chains are sound, so master/install parity checks remain required
- rollback should narrow integrations before undoing the owner split entirely
- preserve wave history instead of silently erasing the integration slice

## Next possible phases

- `062-04` run the postflight overlap audit and final parity sweep

## Exit criteria

- [x] the repository-level governance surfaces reflect the new communication owner split coherently
- [x] touched integrations no longer leave the extracted domains under duplicate active authority
