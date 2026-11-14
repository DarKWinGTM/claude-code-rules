import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
import test from 'node:test';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const source = (name) => readFileSync(resolve(root, name), 'utf8');
const action = source('action-safety.md');
const intake = source('safe-io.md');
const coding = source('coding-discipline.md');
const evidence = source('evidence-discipline.md');
const execution = source('execution-and-goal-frame.md');
const presentation = source('explanation-and-presentation.md');
const requiresClause = (text, pattern) => assert.ok(pattern.test(text), `Missing written contract: ${pattern.source}`);

// These assert written contracts, not model compliance or live operation safety.
test('unknown consequential outcomes require same-operation reconciliation before replay', () => {
  const retry = action.split('## Part D — Failure Classification and Bounded Retry')[1];
  assert.ok(retry, 'the existing retry owner must remain active');
  requiresClause(retry, /unknown outcome after dispatch/i);
  requiresClause(retry, /same operation['’]s identity and canonical completion witness/i);
  requiresClause(retry, /existing idempotent replay contract/i);
  requiresClause(retry, /Preserve independently committed\/completed effects/);
  requiresClause(retry, /OPERATION_OUTCOME_UNKNOWN[^\n]*NO_RETRY_UNTIL_CHANGE/);
});

test('known-no-effect and contract-safe retries retain their existing gates and budget', () => {
  requiresClause(action, /Known-no-effect failure or checked safe replay[^\n]*profile, budget, approval and provider wait/);
  requiresClause(action, /no new writer, state, probe or rollback path is authorized/);
  requiresClause(action, /aggregate maximum \*\*3 autonomous retry rounds per turn\*\*/);
  requiresClause(action, /Provider `Retry-After` wins/);
});

test('large evidence has byte, record and retention bounds before parsing or allocation', () => {
  const bounded = intake.split('## Bounded File Intake')[1]?.split('## Aggregate Burst Gate')[0];
  assert.ok(bounded, 'the existing intake owner must remain active');
  requiresClause(bounded, /input byte, individual-record size and retained-result bounds before decoding, parsing or materializing/i);
  requiresClause(bounded, /cap\/reject oversized records before parse/);
  requiresClause(bounded, /Output truncation is not a memory bound/);
  requiresClause(bounded, /count-only limits do not cap record bytes or decoded expansion/);
});

test('bounded evidence reports coverage and preserves direct small reads', () => {
  requiresClause(intake, /report skipped records, byte limits and partial coverage/);
  requiresClause(intake, /fixed byte watermark/);
  requiresClause(intake, /Known small files and exact bounded reads stay direct/);
  requiresClause(intake, /do not authorize Product\/runtime resource policy, cgroup\/container changes or a new runner/);
  requiresClause(intake, /caps are not verification and cannot hide a failure/);
});

test('caller-first design and preventive controls stay at their checked owner', () => {
  requiresClause(coding, /caller usage[\s\S]*input\/output and failure[\s\S]*types\/signatures[\s\S]*module boundaries/i);
  requiresClause(coding, /code, type\/schema, validator, Tool, Skill or Rule/);
  requiresClause(coding, /Existing coverage identifies an absorption point, not proof that enrichment is unnecessary/);
  requiresClause(coding, /Risk\/test obligations do not themselves authorize[\s\S]*architecture/);
  requiresClause(coding, /no mandatory[\s\S]*worksheet/);
});

test('complexity admission compares a simpler complete alternative and its carrying cost', () => {
  const structure = coding.split('### Responsibility and smallest useful decomposition')[1]?.split('### Semantic source naming')[0];
  assert.ok(structure, 'the existing structure owner must remain active');
  requiresClause(structure, /overengineering[\s\S]*simpler complete alternative/i);
  requiresClause(structure, /boundary alone does not earn added machinery/i);
  requiresClause(structure, /state\/transitions[\s\S]*change propagation[\s\S]*maintenance cost/i);
  requiresClause(structure, /work created only to support the addition/i);
  requiresClause(structure, /allocation[\s\S]*serialization[\s\S]*hash[\s\S]*retention[\s\S]*synchronization/i);
  requiresClause(structure, /guards\/tests[\s\S]*not independent evidence[\s\S]*safeguards before first use/i);
  requiresClause(structure, /hard-to-reverse contracts[\s\S]*required safeguards/i);
  requiresClause(structure, /Passing tests[\s\S]*not necessity/i);
});

test('data representations follow purpose and lifecycle rather than copy counts', () => {
  const state = coding.split('### Canonical state and deliberate transformations')[1]?.split('### Names, comments and governed references')[0];
  assert.ok(state, 'the existing state owner must remain active');
  requiresClause(state, /purpose[\s\S]*consumer[\s\S]*protocol\/operator[\s\S]*existing data/i);
  requiresClause(state, /unknown purpose[\s\S]*bounded diagnosis[\s\S]*not[\s\S]*creation or deletion/i);
  requiresClause(state, /reuse, derive, transform, copy\/snapshot and persist/i);
  requiresClause(state, /one object or format[\s\S]*read-heavy[\s\S]*staleness[\s\S]*historical truth/i);
  requiresClause(state, /rebuildability[\s\S]*not deletion permission/i);
});

test('hash selection preserves input meaning and logical operation intent', () => {
  const state = coding.split('### Canonical state and deliberate transformations')[1]?.split('### Names, comments and governed references')[0];
  requiresClause(state, /required guarantee[\s\S]*collision[\s\S]*threat\/entropy/i);
  requiresClause(state, /exact bytes[\s\S]*deterministic serialization[\s\S]*domain meaning/i);
  requiresClause(state, /key sorting[\s\S]*precision[\s\S]*absence\/null[\s\S]*ordering/i);
  requiresClause(state, /trusted digest[\s\S]*retained digest alone[\s\S]*fresh bytes/i);
  requiresClause(state, /unkeyed hash[\s\S]*authentication[\s\S]*confidentiality[\s\S]*password[\s\S]*high-entropy token/i);
  requiresClause(state, /content equality[\s\S]*operation intent[\s\S]*retries[\s\S]*intentional new operations/i);
});

test('computation placement preserves validity isolation and failure ordering', () => {
  const state = coding.split('### Canonical state and deliberate transformations')[1]?.split('### Names, comments and governed references')[0];
  requiresClause(state, /owner → inputs → result\/digest → consumer → invalidation/i);
  requiresClause(state, /parse\/normalize\/clone\/serialize\/hash\/snapshot[\s\S]*discarded or overwritten/i);
  requiresClause(state, /immutable snapshots[\s\S]*mutable isolation[\s\S]*evaluation\/error\/side-effect ordering/i);
  requiresClause(state, /fresh[\s\S]*hashing inside loops[\s\S]*not[\s\S]*cache/i);
  requiresClause(coding, /primitive benchmark[\s\S]*not whole-path CPU\/memory evidence/i);
});

test('loop hashing distinguishes stable identity freshness and required unique nonces', () => {
  const state = coding.split('### Canonical state and deliberate transformations')[1]?.split('### Names, comments and governed references')[0];
  requiresClause(state, /frequency[\s\S]*cardinality[\s\S]*per-item[\s\S]*rebuild\/write/i);
  requiresClause(state, /deterministic rehash[\s\S]*not nonce generation/i);
  requiresClause(state, /time\/random\/counter[\s\S]*stable identity[\s\S]*self-invalidating/i);
  requiresClause(state, /freshness\/audit[\s\S]*not[\s\S]*exclude fields/i);
  requiresClause(state, /nonce[\s\S]*salt[\s\S]*protocol\/security[\s\S]*never reuse a required-unique nonce/i);
  requiresClause(state, /hash-until-condition[\s\S]*equality\/versioning[\s\S]*checked implementations/i);
});

test('structural assessment catches cumulative growth without mandatory splitting', () => {
  requiresClause(coding, /affected structure before material additions, during cumulative growth and before non-trivial closeout/i);
  requiresClause(coding, /cohesion\/coupling[\s\S]*state\/dependency[\s\S]*test boundaries/i);
  requiresClause(coding, /large cohesive unit[\s\S]*no hard LOC/i);
  requiresClause(coding, /Do not silently accumulate mixed responsibilities/i);
});

test('every refactor requires a concrete proportional plan and explicit approval', () => {
  requiresClause(coding, /Before any refactor[\s\S]*including local or low-risk[\s\S]*explicit user approval/i);
  requiresClause(coding, /before\/after responsibilities and dependencies[\s\S]*scope\/exclusions[\s\S]*callers\/failures\/side effects/i);
  requiresClause(coding, /ordered small transformations[\s\S]*functional and structural proof[\s\S]*stop\/recovery/i);
  requiresClause(coding, /short chat plan[\s\S]*no mandatory new artifact/i);
  requiresClause(coding, /Structural transformations below are recommendations[\s\S]*plan and approval/i);
  assert.doesNotMatch(coding, /Proceed with clear low-risk touched repair/i);
  assert.doesNotMatch(execution, /Proceed with safe local cohesive repair/i);
});

test('approved refactors continue while material deviations wait for consultation', () => {
  requiresClause(execution, /approved plan[\s\S]*without repeat permission/i);
  requiresClause(execution, /material scope, contract, ownership or risk[\s\S]*before the affected action/i);
  requiresClause(execution, /Independent authorized work continues[\s\S]*proposal waits/i);
  requiresClause(coding, /feature\/fix request is not consent[\s\S]*ordinary scoped edits[\s\S]*not automatically refactors/i);
  requiresClause(coding, /actual transformation[\s\S]*not its label/i);
});

test('material user ambiguity is clarified without outsourcing checkable facts', () => {
  requiresClause(execution, /user intent, required output, scope, acceptance or material trade-off[\s\S]*ask one bounded substantive question[\s\S]*before the affected action/i);
  requiresClause(execution, /Inspect checkable technical facts directly/i);
  requiresClause(execution, /Do not invent a broader objective/i);
});

test('test admission requires a distinct evidence gap without count-based quotas', () => {
  const proof = coding.split('### Select the smallest meaningful proof')[1]?.split('### Debug and root-cause discrimination')[0];
  assert.ok(proof, 'the existing verification owner must remain active');
  requiresClause(proof, /evidence gap[\s\S]*failure[\s\S]*existing proof cannot/i);
  requiresClause(proof, /Reuse or extend the fitting case first/i);
  requiresClause(proof, /multiple layers[\s\S]*distinct faults/i);
  requiresClause(proof, /LOC ratios alone justify neither growth nor removal/i);
  requiresClause(proof, /helper does not itself require a new test/i);
  requiresClause(proof, /brittleness[\s\S]*selected acceptance and safety proof/i);
});

test('selected workflow proof distinguishes admission, reached assertions and terminal outcome', () => {
  requiresClause(coding, /selected core contract[\s\S]*owner case and selector admission[\s\S]*execution and assertions reached[\s\S]*terminal outcome[\s\S]*remaining proof/);
  requiresClause(coding, /A registered or selected case is not executed coverage/);
  requiresClause(coding, /existing runner\/report owner/);
  requiresClause(coding, /not a new inventory, runner or receipt mandate for small work/);
});

test('decisive assumptions use relevant implementation evidence rather than universal checklists', () => {
  requiresClause(evidence, /decisive assumption/);
  requiresClause(evidence, /indirect consumers, dependencies, shipped versions, local patches or timing/);
  requiresClause(evidence, /only when they can change that conclusion/);
  requiresClause(evidence, /smallest check that could disprove it/);
  requiresClause(evidence, /missing or contrary evidence keeps the claim conditional/);
});

test('structured receipts remain bound witnesses and cannot certify their own claims', () => {
  requiresClause(evidence, /Structured or timestamped receipts do not certify their own claims/);
  requiresClause(evidence, /actual command\/selector, artifact\/environment binding and reached terminal evidence/);
  requiresClause(evidence, /missing fields are unobserved, not a pass/);
  requiresClause(evidence, /does not authorize a new journal or receipt schema/);
});

test('complete requested inventories retain disposition before recommendation priority', () => {
  requiresClause(presentation, /requested complete inventory/);
  requiresClause(presentation, /retain every in-scope item and its disposition/);
  requiresClause(presentation, /do not silently replace it with a shortlist/);
  requiresClause(presentation, /Completeness and priority are separate/);
});

test('material next actions are visible without rigid templates or invented rendering', () => {
  requiresClause(presentation, /needed action or decision, its dependency and consequence[\s\S]*easy to locate/);
  requiresClause(presentation, /grouping and selective emphasis/);
  requiresClause(presentation, /not fixed headings or emphasis on every term/);
  requiresClause(presentation, /Do not promise color, underline or other renderer effects that were not actually shown/);
});

test('tentative user methods stay distinct from binding constraints and technical facts', () => {
  const premise = execution.split('### Premise and completed-baseline protection')[1]?.split('### Architecture-bearing action')[0];
  assert.ok(premise, 'the existing premise owner must remain active');
  requiresClause(premise, /tentative user method[\s\S]*explicit constraint/i);
  requiresClause(premise, /Investigate decision-changing technical unknowns/);
  requiresClause(premise, /user-owned preferences[\s\S]*approval/);
  requiresClause(premise, /provisional design[\s\S]*reversible experiments/);
  requiresClause(premise, /settled facts[\s\S]*costly dependent/);
});

test('pivotal design checks connect an actual control boundary to the intended outcome', () => {
  const decision = execution.split('## 2. Scope and Simplest Complete Decision')[1]?.split('### Architecture-bearing action')[0];
  assert.ok(decision, 'the existing decision owner must remain active');
  requiresClause(decision, /pivotal design assumption/);
  requiresClause(decision, /actual platform[\s\S]*control boundary[\s\S]*intended consumer[\s\S]*desired outcome/);
  requiresClause(decision, /component[\s\S]*defined ourselves[\s\S]*causal link/);
  requiresClause(decision, /source\/contract inspection[\s\S]*smallest authorized[\s\S]*reversible experiment/);
  requiresClause(decision, /not a PoC, live check, alternative count or artifact mandate for every design/);
});

test('missing precedent supports neither impossibility nor a world-first claim', () => {
  requiresClause(evidence, /Missing precedent[\s\S]*neither impossibility nor novelty/);
  requiresClause(evidence, /mechanistic hypothesis[\s\S]*conditional research[\s\S]*safe experiments/);
  requiresClause(evidence, /not verified capability, suitability or measured benefit/);
  requiresClause(evidence, /contradiction rejects the affected method[\s\S]*not automatically the goal/);
  requiresClause(evidence, /no precedent search or experiment is required for every idea/);
});

test('feasibility enrichment preserves selected proof and consequential-action boundaries', () => {
  requiresClause(execution, /Source\/code goals close at source\/non-live proof unless user or checked governed authority explicitly selects live acceptance/);
  requiresClause(execution, /Explicitly required terminal proof remains binding/);
  requiresClause(execution, /Do not silently fork/);
  requiresClause(evidence, /Fake\/local checks prove their scope, not live\/provider\/runtime\/deploy behavior/);
});

test('material handoff identifies the action owner and consequence without inventing activation', () => {
  const communication = source('accurate-communication.md');
  requiresClause(communication, /needed application step[\s\S]*action, owner[\s\S]*not done[\s\S]*consequence/i);
  requiresClause(communication, /ask the user directly[\s\S]*exact enabling action/i);
  requiresClause(communication, /not assume[\s\S]*restart[\s\S]*source[\s\S]*live/i);
});

test('complex explanations include plain synthesis without mandating its position', () => {
  requiresClause(presentation, /plain-language synthesis[\s\S]*central problem[\s\S]*causal/i);
  requiresClause(presentation, /details may come first/i);
  requiresClause(presentation, /not[\s\S]*fixed opening[\s\S]*template/i);
  requiresClause(presentation, /intermediate completion[\s\S]*user['’]s goal/i);
});

test('status groups distinguish obligations and unselected proposals without a fixed report', () => {
  requiresClause(presentation, /completed[\s\S]*remaining[\s\S]*blocked[\s\S]*unselected proposals/i);
  requiresClause(presentation, /owner[\s\S]*enabling condition/i);
  requiresClause(presentation, /not[\s\S]*mandatory[\s\S]*template/i);
});

test('issue review reconciles selected obligations at meaningful continuity boundaries', () => {
  requiresClause(execution, /start or resume[\s\S]*correction, failure or scope change[\s\S]*material status or closeout/i);
  requiresClause(execution, /selected obligations[\s\S]*current evidence[\s\S]*remaining/i);
  requiresClause(execution, /not[\s\S]*every command[\s\S]*rerun/i);
});

test('artifact placement follows required lifetime rather than temporary path names', () => {
  requiresClause(coding, /required lifetime[\s\S]*resume[\s\S]*recreat[\s\S]*loss[\s\S]*sensitivity/i);
  requiresClause(coding, /run-bound[\s\S]*manifest[\s\S]*retained[\s\S]*owner-controlled/i);
  requiresClause(coding, /sandbox[\s\S]*cache[\s\S]*container[\s\S]*tool workspace/i);
  requiresClause(coding, /project[\s\S]*`\.tmp\/`[\s\S]*not[\s\S]*durability/i);
  requiresClause(coding, /missing[\s\S]*approved baseline[\s\S]*not[\s\S]*invent/i);
  requiresClause(intake, /capture[\s\S]*required lifetime[\s\S]*coding-discipline/i);
});

const runtimeFiles = source('script/setup-claude-code-rules.sh')
  .match(/active_rule_files=\(([\s\S]+?)\n\)/)?.[1].match(/[\w-]+\.md/g);
assert.equal(runtimeFiles?.length, 19, 'retain the selected nineteen-owner payload');

for (const file of runtimeFiles) {
  const name = file.replace(/\.md$/, '');
  test(`${name} retains one aligned substantive runtime, design and changelog chain`, () => {
    const runtime = source(`${name}.md`);
    const design = source(`design/${name}.design.md`);
    const changelog = source(`changelog/${name}.changelog.md`);
    const version = (text) => text.match(/^> \*\*Current Version:\*\* ([\d.]+)/m)?.[1];
    assert.ok(version(runtime));
    assert.equal(version(design), version(runtime));
    assert.equal(version(changelog), version(runtime));
    assert.ok(runtime.includes(`[design/${name}.design.md](design/${name}.design.md) v${version(runtime)}`));
    assert.ok(runtime.includes(`[changelog/${name}.changelog.md](changelog/${name}.changelog.md)`));
    requiresClause(runtime, /## /);
    requiresClause(design, /verif(?:y|ication)|validation/i);
    if (['action-safety', 'safe-io', 'coding-discipline', 'evidence-discipline', 'execution-and-goal-frame', 'explanation-and-presentation'].includes(name)) {
      requiresClause(runtime, /## (?:Integration and )?Boundaries|## Trigger Dispatch and (?:Boundaries|Anti-Drift)/);
      requiresClause(design, /## Verification/);
    }
    assert.ok(runtime.length > 2000, 'metadata alone is not an active Runtime body');
  });
}
