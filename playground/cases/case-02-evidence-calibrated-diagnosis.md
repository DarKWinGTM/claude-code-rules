# Case 02 — Evidence-Calibrated Diagnosis

## What this case proves

This case family shows how RULES stop diagnosis from turning a visible failure into a verified root cause before the checked evidence actually supports that jump.

---

## Scenario family

- Primary family: evidence-calibrated diagnosis
- Current status: transcript-grounded observed example present; virtual variants available

---

## Governing rules

- `evidence-discipline.md` — symptom vs hypothesis vs likely cause vs verified cause
- `accurate-communication.md` — scoped non-finding and claim-strength wording
- `communication-register.md` — avoid verdict-style contradiction without evidence
- `explanation-and-presentation.md` — root-cause walkthrough shape
- `safe-io.md` — bounded reads and scoped file/output checks

---

## Rule-enforced fact

Current RULES require the assistant to:
- separate symptom, checked evidence, working hypothesis, likely cause, and next-best check
- avoid stating a root cause as verified without enough evidence
- report checked scope when something was not found
- recalibrate earlier wording if new evidence shows the first claim was too strong
- bound large/unknown/untrusted evidence by input bytes, individual record size and retained results before decode/parse/materialization; output/count-only caps are not allocation bounds, and skipped/partial coverage must remain visible

---

## Observed case

Checked transcript-derived example:
- Transcript path: `<claude-project-scope-root>/0242764f-4e83-4651-bc03-3cc5c1055cd1.jsonl`
- Anchor hints: `internal_routing_failure`, `สิ่งที่ evidence ตัวนี้พิสูจน์ได้จริง`, `Diagnose gateway not-yet-product`
- Observed effect: after a user-facing auth/verifier error surfaced, the assistant explicitly recalibrated what the evidence proved, separated symptom from cause, and chose a bounded next-best check instead of endorsing the most convenient explanation.
- Scope note: this proves evidence-first diagnosis behavior in that checked session; it does not prove a universal root cause for similar errors.

---

## Virtual variant

- User says the config is definitely wrong, but only one source has been checked.
- A failing command suggests one likely branch, but several causes still remain live.
- A search misses a symbol in one folder, but the full repo has not been checked.

- A large growing JSONL log has unknown record sizes; a proposal uses `read_text().splitlines()` and prints only ten matches. Select byte/record/retention bounds and a fixed byte watermark before parse; skip or reject oversized records and disclose the limited coverage (M50–M52).
- A known-small exact file read fits the selected bound. Read it directly without a new runner or Product resource policy (M53).

Expected behavior: verify further or state the limit, rather than upgrading the concern into a verified cause. Bound evidence before allocation, not only terminal output; these are virtual interpretation cases, not measured memory savings or observed incidents.

---

### Decisive-assumption and receipt variants

These are declared virtual acceptance cases for Evidence1.10, not newly observed incidents.

| Input | Expected decision and nearest boundary |
|---|---|
| A recommendation is safe only if the shipped dependency does not call the consumer synchronously; a generic latest-version example is available. | Name that decisive assumption, inspect the actual shipped version/local patches and consumer timing, and select the smallest disproof check; do not infer the current implementation from the generic example. |
| A distant dependency cannot change the selected conclusion, or an exact small source check already settles it. | Stop at sufficient evidence; no full dependency checklist or new harness. |
| A timestamped structured receipt says PASS but omits argv/selector or matching reached assertions. | Treat the omitted binding as unobserved, not a pass; use the existing owner-produced witness or report the limit, without a second journal/schema. |
| The actual implementation contradicts the decisive assumption after an earlier recommendation. | Keep the goal, withdraw the unsupported route and state the smallest evidence-backed continuation; no architecture from the concern alone. |

## User objective

Understand a visible failure without turning the first plausible explanation into a verified root cause too early.

---

## Operational reality

- A concrete symptom is visible in the checked error or output.
- Some evidence exists, but it does not yet prove the underlying mechanism.
- The next safe move is cause narrowing, not confidence escalation.

---

## RULES effect on execution

- Split symptom, checked evidence, working hypothesis, likely cause so far, and next-best check.
- Recalibrate earlier wording if new evidence shows the first claim was too strong.
- Keep scoped non-findings scoped instead of treating them as absence proof.

---

## Decision

Diagnosis stays at working-hypothesis or likely-cause level until stronger evidence confirms the mechanism.

---

## What AI does next

- State what the checked evidence proves now.
- Name the leading hypothesis without upgrading it to verified cause.
- Choose the next discriminating check that can cut away major competing explanations.

---

## Recovery path

- Bring in the next relevant log, config source, or bounded reproduction result.
- Promote, downgrade, or replace the cause hypothesis only after that next check lands.

---

## User-visible reply example

`The checked error proves the auth path failed, but not yet why. Right now the safest reading is a working cause hypothesis, and the next check is to inspect the verifier path that produced this failure.`

---

## Flow diagram

```text
User reports visible symptom
  ↓
Initial error evidence is checked
  ↓
Symptom is separated from cause hypothesis
  ↓
New evidence forces wording recalibration
  ↓
Next-best check is chosen
  ↓
Scoped diagnosis is reported
```

---

## Matrix axes in play

- request type: diagnosis
- evidence state: partial → transcript-grounded
- scope clarity: mixed until broader checks happen
- risk level: medium
- expected rule response: verify first and keep cause wording scoped
- turn count: 3
- user behavior: clear request followed by evidence-based correction pressure
- evidence source: tool output plus transcript anchor
- failure mode: overclaim risk
- tool discovery or lane shape: bounded read-only follow-up
- completion state: not applicable

---

## Behavior delta

Without this family, the assistant can sound confident too early and turn a symptom into a verdict.

With RULES active, diagnosis becomes more trustworthy because claim strength stays proportional to checked evidence and can be recalibrated when stronger evidence arrives.
