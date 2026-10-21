import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';
import test from 'node:test';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const source = (name) => readFileSync(resolve(root, name), 'utf8');
const action = source('action-safety.md');
const intake = source('safe-io.md');
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

for (const name of ['action-safety', 'safe-io']) {
  test(`${name} retains one aligned substantive runtime, design and changelog chain`, () => {
    const runtime = source(`${name}.md`);
    const design = source(`design/${name}.design.md`);
    const changelog = source(`changelog/${name}.changelog.md`);
    const version = (text) => text.match(/^> \*\*Current Version:\*\* ([\d.]+)/m)?.[1];
    assert.ok(version(runtime));
    assert.equal(version(design), version(runtime));
    assert.equal(version(changelog), version(runtime));
    assert.ok(runtime.includes(`[design/${name}.design.md](design/${name}.design.md) v${version(runtime)}`));
    requiresClause(runtime, /## Boundaries|## Trigger Dispatch and Boundaries/);
    requiresClause(design, /## Verification/);
    assert.ok(runtime.length > 2000, 'metadata alone is not an active Runtime body');
  });
}
