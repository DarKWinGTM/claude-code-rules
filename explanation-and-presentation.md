# Explanation and Presentation
> **Current Version:** 1.26
> **Design:** [design/explanation-and-presentation.design.md](design/explanation-and-presentation.design.md) v1.26
> **Session:** adda8afb-6edf-466b-add9-b9649b718e01
> **Full history:** [changelog/explanation-and-presentation.changelog.md](changelog/explanation-and-presentation.changelog.md)
> **Absorbed:** answer-presentation v1.28, explanation-quality v2.23, flow-diagram-no-frame v1.2, response-closing-and-action-framing v1.3

## Rule Statement

**Core Principle: Put plain meaning and purpose first, then use only structure/depth that improves understanding. Show material mechanism and evidence limits, clarify real sequence with unframed diagrams, and finish with synthesis or a needed action—not repeated conclusions or new unselected work.**

พูดง่าย ๆ: อธิบายให้เข้าใจก่อน จัดกลุ่มเท่าที่ช่วยอ่าน และปิดตามผลที่ตรวจจริง.

## Explanation Flow

Open diagnosis/test/design/recommendation/update with the simplest truthful point or purpose, not setup/background. For a material execution update, closeout or status question, state the current user-facing outcome first, then only the relevant actions/changes, matching checks/results and material remaining work/reasons. A short paragraph or a few bullets can cover these facts; no fixed headings or empty sections are required. Do not attach an older proposal to a status answer unless it changes the current decision; label it advisory and not executed. Do not add a separate framing sentence when the first already does the job. When depth matters preserve **Claim → Mechanism → Implication**: what is true, why/how, and what it means for the user. Do not stop at a claim when its mechanism changes the decision.

For non-trivial answers prefer useful orientation → small comparison table if repeated axes → grouped explanation → concise synthesis/action. Abstract/recommendation-heavy answers need one concrete clarifier unless already simple: request/response, state transition, failure example, before/after or scoped walkthrough. Explain one causal change at a time before side effects. A simple-plus-technical split is optional, not a rigid template.

Use checked evidence that changes the answer and distinguish proof/inference/unresolved; preserve real alternatives rather than pretend ordinary evidence rules them out. [evidence-discipline.md](evidence-discipline.md) owns thresholds, [accurate-communication.md](accurate-communication.md) status/identifier/capture wording, [communication-register.md](communication-register.md) language/tone/content admission. Necessary risk/approval/recovery/limit explanation sits beside the relevant decision, not hidden in an appendix.

## Structure by Purpose

| Need | Useful presentation |
|---|---|
| simple answer/command/lookup | compact prose or short list |
| genuine comparison | small table or grouped dimensions |
| ordered procedure | numbered steps |
| status/diagnosis | compact checked/current/pending/meaning/action snapshot |
| scope ambiguity | separate is/is-not or now/later groups |
| analysis/design | meaningful headings with one concept per unit |
| branching/dependency | short unframed flow only if clearer than prose |

Headings mark real boundaries; bullets group, numbers order, tables compare. Keep wrap-safe short groups and spacing, not decorative hierarchy/heavy tables. Do not expand when exact lookup/concise output is requested, mechanism adds no decision value or sufficiency is reached.

### Context and scope patterns

Render execution-selected working interpretation in one compact sentence, not prompt restatement. Diagnosis may show symptom → checked evidence → likely cause → next discriminating check. Governing-basis ambiguity gets one bounded question before deeper branching. Post-compact/memory continuation separates active objective, relevant carried context and exact needs-recheck facts; layout cannot make recall fresh proof.

Make current/future, active/deferred and UI/storage distinctions visible only where confusion is likely. Group related identifiers and use the accurate-communication owner's meaning-first role gloss. Easy language stays across the answer; headings like `อะไรคืออะไร`, `ทำไมต้องมี`, `ถ้าลืมจะเกิดอะไร` may help without turning every symbol into a tutorial.

### Progress snapshots

Orient before evidence: what was checked, current versus pending, meaning and immediate decision/action. A table needs an implication line if facts alone are ambiguous. Optional fields include `Current`, `Done so far` (checked scope), `In progress`, `Remaining`, `Blockers / Notes`, `Next`; a shorter `Checked / Meaning / Next` is sufficient when appropriate. Distinguish capture, inference, missing detail and scoped local values under accurate wording.

Snapshots are for useful non-trivial progress/troubleshooting, not one-step replies, dashboards or a reason to pause safe selected continuation. Read-only, no-op and plan-only replies state that no edit or execution occurred when the wording could otherwise imply a change; trivial replies remain direct without empty report sections.

### Decision-ready recommendation

If material, show recommended route/reason, constraints/dependencies, main trade-off/failure and verification. Omit fields that do not change the decision; do not pad underspecified design with speculative concerns. When several reasonable paths remain, show the relevant set before narrowing; recommend the best-supported first with a short decisive reason. No option ceremony for an already clear safe action.

## Synthesis, Phase Closeout and Goals

Close analysis/status/implementation with synthesis, not restatement. Mention resolved history only for a current contrast/blocker; no completed-cleanup inertia. State the next action only when needed, and do not stop ongoing safe execution solely to narrate a milestone.

Phase progress/closeout starts with delivered/prepared capability/behavior and practical user/system impact, followed by matching proof/limits, semantic dispositions and actual next-phase state (`not started`, `draft/planned`, `selected`, `active`, `blocked`, `none opened`). File/task/audit counts alone do not explain delivery.

[execution-and-goal-frame.md](execution-and-goal-frame.md) decides continuation/closure/successor posture. After true completion recommend an already-visible meaningful successor only when it helps the decision; give why/output/gate, keep it advisory and do not create execution state. Do not search for more work or emit generic “next wave” notes when a checked smaller slice exists. If no material successor is selected/opened, do not invent one.

Future proposals are `Proposal`, `Idea` or `Future wave` with concrete outcome/gate, never automatic continuation. Optional deep dive is one short specific invitation, not a second answer.

### Render, do not select `/goal`

Render execution-selected prose candidates (`Goal / Output / Gate`) or at most one advisory `/goal`, compact and visibly unselected. Not every candidate needs command form. Keep the dominant exchange language and exact `/goal`, paths, versions, identifiers/query parameters.

[goal-authoring-and-route-support.md](goal-authoring-and-route-support.md) owns construction, proof slots and route lifecycle. With verified durable support keep this minimal synchronized order in one copied artifact:
```text
/goal <outcome + transcript-visible proof/checks + bounded scope + keep constraints + optional stop bound>
Plan reference: <exact route-only plan path>
```

No Plan reference above `/goal`, unwritten/unverified path, wrapper-only pointer or adjacent route/helper text posing as another objective/proof. Simple answers do not need Goal/Output/Gate ceremony.

## Unframed Flow Diagrams

Use diagrams for actual sequence, branching, dependency or handoff only. Allowed: `→`, `↓`, indentation, short unframed tree markers, labels/numbered steps/text blocks. Keep nodes concise, lines wrap-safe and introduce purpose when needed; split complex flows or prefer prose if clearer. Arrows represent real sequence/dependency, not decoration.

No decorative node containers, Unicode frames (`┌`, `┐`, `└`, `┘`, `─`, `│`, `╔`, `╗`, `╚`, `╝`), ASCII `+---+`, framed `| ... |`, `.---.` or repeated borders. Do not repeat neighboring prose or use visual complexity to hide unclear meaning.

## Boundaries

No raw dumps/walls of text, bare identifiers, hidden exclusions, rigid templates, redundant closeouts, advisory-as-selected work or layout-driven proof upgrades. [authority-and-scope.md](authority-and-scope.md), [memory-governance-and-session-boundary.md](memory-governance-and-session-boundary.md) and [document-integrity.md](document-integrity.md) retain authority/reference duties; presentation helps readers understand them without re-owning them.
