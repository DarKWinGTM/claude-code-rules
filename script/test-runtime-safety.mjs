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
  requiresClause(coding, /does not itself authorize[\s\S]*architecture/);
  requiresClause(coding, /no mandatory[\s\S]*worksheet/);
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

for (const name of ['action-safety', 'safe-io', 'coding-discipline', 'evidence-discipline', 'explanation-and-presentation']) {
  test(`${name} retains one aligned substantive runtime, design and changelog chain`, () => {
    const runtime = source(`${name}.md`);
    const design = source(`design/${name}.design.md`);
    const changelog = source(`changelog/${name}.changelog.md`);
    const version = (text) => text.match(/^> \*\*Current Version:\*\* ([\d.]+)/m)?.[1];
    assert.ok(version(runtime));
    assert.equal(version(design), version(runtime));
    assert.equal(version(changelog), version(runtime));
    assert.ok(runtime.includes(`[design/${name}.design.md](design/${name}.design.md) v${version(runtime)}`));
    requiresClause(runtime, /## (?:Integration and )?Boundaries|## Trigger Dispatch and Boundaries/);
    requiresClause(design, /## Verification/);
    assert.ok(runtime.length > 2000, 'metadata alone is not an active Runtime body');
  });
}
