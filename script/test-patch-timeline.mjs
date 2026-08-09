import assert from 'node:assert/strict';
import { mkdtemp, mkdir, readFile, rename, rm, stat, symlink, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { spawnSync } from 'node:child_process';
import { dirname, join } from 'node:path';
import test from 'node:test';
import { fileURLToPath } from 'node:url';

import {
  applyManifest,
  buildManifest,
  canonicalManifest,
  classifyPatch,
  createPatch,
  inventoryPatches,
  parsePatchFilename,
  rollbackJournal,
  sha256,
  verifyManifest,
} from './patch-timeline.mjs';

async function fixture() {
  const root = await mkdtemp(join(tmpdir(), 'patch-timeline-'));
  await mkdir(join(root, 'patch'), { recursive: true });
  await mkdir(join(root, 'phase'), { recursive: true });
  await mkdir(join(root, 'design'), { recursive: true });
  await mkdir(join(root, 'changelog'), { recursive: true });
  await mkdir(join(root, 'todo', 'history'), { recursive: true });
  await mkdir(join(root, 'supplier-manager-runtime', 'archive', 'patch'), { recursive: true });
  return root;
}

async function put(root, relative, body) {
  const target = join(root, relative);
  await mkdir(dirname(target), { recursive: true });
  await writeFile(target, body);
  return target;
}

async function readJson(path) {
  return JSON.parse(await readFile(path, 'utf8'));
}

async function migrationFixture({ reference = true } = {}) {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  const originalReference = '../patch/legacy.patch.md\n';
  if (reference) await put(root, 'phase/phase-001.md', originalReference);
  const manifest = await buildManifest({ root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } });
  return { root, manifest, originalReference, journalPath: join(root, 'apply.journal.json') };
}

const legacyBody = `# Legacy Patch\n\n> **Current Version:** 1.0\n> **Session:** test-session\n> **Status:** active\n> **Target Design:** ../design/example.design.md\n> **Full history:** ../changelog/example.changelog.md\n`;

const evidence = {
  createdAt: '2026-08-09T07:15:30Z',
  source: 'verified transcript creator event',
};

const createMetadata = {
  session: 'test-session',
  targetDesign: '../design/example.design.md',
  fullHistory: '../changelog/example.changelog.md',
};

const toolPath = fileURLToPath(new URL('./patch-timeline.mjs', import.meta.url));

test('parses only canonical UTC filename grammar and valid calendar instants', () => {
  assert.deepEqual(parsePatchFilename('2026-08-09T07-15-30Z--payg-gateway.patch.md'), {
    createdAt: '2026-08-09T07:15:30Z',
    slug: 'payg-gateway',
  });
  for (const name of [
    '2026-08-09T07-15Z--missing-seconds.patch.md',
    '2026-08-09T07:15:30Z--colon.patch.md',
    '2026-08-09T07-15-30Z-single.patch.md',
    '2026-08-09T07-15-30Z--Upper.patch.md',
    '2026-08-09T07-15-30Z--under_score.patch.md',
    '2026-02-30T07-15-30Z--impossible.patch.md',
    '2026-08-09T07-15-30Z--ภาษาไทย.patch.md',
  ]) assert.equal(parsePatchFilename(name), null, name);
});

test('classifies compliant metadata and rejects filename metadata mismatch', () => {
  const compliant = `# Example\n\n> **Created At:** 2026-08-09T07:15:30Z\n> **Creation Evidence:** direct creator event\n`;
  assert.equal(classifyPatch('patch/2026-08-09T07-15-30Z--example.patch.md', compliant).status, 'compliant');
  const mismatch = compliant.replace('07:15:30Z', '07:15:31Z');
  assert.equal(classifyPatch('patch/2026-08-09T07-15-30Z--example.patch.md', mismatch).status, 'invalid');
});

test('legacy evidence must be authoritative and never mtime or ctime', () => {
  assert.equal(classifyPatch('patch/legacy.patch.md', legacyBody).status, 'legacy-ambiguous');
  assert.equal(classifyPatch('patch/legacy.patch.md', legacyBody, evidence).status, 'legacy-authoritative');
  assert.equal(classifyPatch('patch/legacy.patch.md', legacyBody, { ...evidence, source: 'filesystem mtime' }).status, 'legacy-ambiguous');
  assert.equal(classifyPatch('patch/legacy.patch.md', legacyBody, { ...evidence, source: 'ctime' }).status, 'legacy-ambiguous');
});

test('inventory separates selected and suspended archive patches', async () => {
  const root = await fixture();
  await put(root, 'patch/selected.patch.md', legacyBody);
  await put(root, 'supplier-manager-runtime/archive/patch/preserved.patch.md', legacyBody);
  const inventory = await inventoryPatches({ root, archivePrefixes: ['supplier-manager-runtime/archive/patch'] });
  assert.equal(inventory.selectedCount, 1);
  assert.equal(inventory.preservedCount, 1);
  assert.equal(inventory.files.find((row) => row.path.endsWith('preserved.patch.md')).status, 'preserved-suspended-archive');
});

test('explicit excluded prefixes are outside inventory and manifest scans', async () => {
  const root = await fixture();
  await put(root, 'patch/selected.patch.md', legacyBody);
  await put(root, 'runtime-data/private/ignored.patch.md', legacyBody);
  const inventory = await inventoryPatches({ root, archivePrefixes: [], excludePrefixes: ['runtime-data/private'] });
  assert.equal(inventory.totalCount, 1);
  assert.deepEqual(inventory.excludePrefixes, ['runtime-data/private']);
  const manifest = await buildManifest({ root, archivePrefixes: [], excludePrefixes: ['runtime-data/private'], evidenceByPath: {} });
  assert.equal(manifest.blockers.length, 1);
  assert.equal(manifest.blockers[0].path, 'patch/selected.patch.md');
});

test('create captures one clock value and refuses collisions exclusively', async () => {
  const root = await fixture();
  let calls = 0;
  const now = () => { calls += 1; return new Date('2026-08-09T07:15:30.999Z'); };
  const preview = await createPatch({ root, patchDir: 'patch', slug: 'safe-create', title: 'Safe Create', creationEvidence: 'direct creator event', ...createMetadata, now });
  assert.equal(preview.executed, false);
  assert.equal(calls, 1);
  assert.equal(preview.path, 'patch/2026-08-09T07-15-30Z--safe-create.patch.md');

  calls = 0;
  const created = await createPatch({ root, patchDir: 'patch', slug: 'safe-create', title: 'Safe Create', creationEvidence: 'direct creator event', ...createMetadata, now, execute: true, approvedManifestSha256: preview.manifestSha256 });
  assert.equal(created.executed, true);
  assert.equal(calls, 1);
  const before = await readFile(join(root, created.path));
  await assert.rejects(() => createPatch({ root, patchDir: 'patch', slug: 'safe-create', title: 'Safe Create', creationEvidence: 'direct creator event', ...createMetadata, now, execute: true, approvedManifestSha256: preview.manifestSha256 }), /already exists/);
  assert.deepEqual(await readFile(join(root, created.path)), before);
});

test('create requires exact manifest approval to mutate', async () => {
  const root = await fixture();
  await assert.rejects(() => createPatch({ root, patchDir: 'patch', slug: 'approval', title: 'Approval', creationEvidence: 'direct creator event', ...createMetadata, now: () => new Date('2026-08-09T07:15:30Z'), execute: true, approvedManifestSha256: 'wrong' }), /approval hash/);
});

test('manifest is deterministic and rewrites only exact governed references', async () => {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  await put(root, 'phase/phase-001.md', '[Patch](../patch/legacy.patch.md) and `../patch/legacy.patch.md`\n');
  await put(root, 'design/example.design.md', '`patch/legacy.patch.md`\n');
  await put(root, 'changelog/example.changelog.md', '../patch/legacy.patch.md\n');
  await put(root, 'todo/history/day.md', '../../patch/legacy.patch.md\n');
  await put(root, 'design/rooted.design.md', '/patch/legacy.patch.md\n');
  await put(root, 'design/absolute.design.md', `${join(root, 'patch/legacy.patch.md')}\n`);
  await put(root, 'design/uri.design.md', 'file://patch/legacy.patch.md repo://patch/legacy.patch.md https://example.test/patch/legacy.patch.md\n');
  await put(root, 'README.md', 'Generic `patch/*.patch.md` remains generic.\n');
  await put(root, 'request-details.json', '{"captured":"patch/legacy.patch.md"}\n');
  const opts = { root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } };
  const first = await buildManifest(opts);
  const second = await buildManifest(opts);
  assert.equal(canonicalManifest(first), canonicalManifest(second));
  assert.equal(first.rows.length, 1);
  assert.equal(first.rows[0].references.length, 6);
  assert.ok(first.rows[0].references.every((ref) => !ref.path.endsWith('.json')));
  assert.ok(first.rows[0].references.every((ref) => !ref.before.includes('*')));
  const newName = '2026-08-09T07-15-30Z--legacy.patch.md';
  assert.match(first.references.find((ref) => ref.path === 'design/rooted.design.md').after, new RegExp(`/patch/${newName}`));
  assert.match(first.references.find((ref) => ref.path === 'design/absolute.design.md').after, new RegExp(`${root.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}/patch/${newName}`));
  assert.equal(first.references.some((ref) => ref.path === 'design/uri.design.md'), false);
});

test('create rejects multiline governed metadata fields', async () => {
  const root = await fixture();
  const base = {
    root,
    patchDir: 'patch',
    slug: 'single-line-metadata',
    title: 'Single Line Metadata',
    creationEvidence: 'direct creator event',
    ...createMetadata,
    now: () => new Date('2026-08-09T07:15:30Z'),
  };
  for (const [field, value] of [
    ['title', 'Title\nInjected'],
    ['creationEvidence', 'direct creator event\n> **Created At:** 2000-01-01T00:00:00Z'],
    ['session', 'test-session\n> **Created At:** 2000-01-01T00:00:00Z'],
    ['targetDesign', '../design/example.design.md\rInjected'],
    ['fullHistory', '../changelog/example.changelog.md\nInjected'],
  ]) {
    await assert.rejects(() => createPatch({ ...base, [field]: value }), /single line/);
  }
});

test('manifest and plan selected counts include already-compliant patches', async () => {
  const root = await fixture();
  const compliant = `# Compliant\n\n> **Created At:** 2026-08-09T07:15:30Z\n> **Creation Evidence:** direct creator event\n`;
  await put(root, 'patch/2026-08-09T07-15-30Z--compliant.patch.md', compliant);
  const manifest = await buildManifest({ root });
  assert.equal(manifest.selectedCount, 1);
  assert.equal(manifest.preservedCount, 0);
  const planned = spawnSync(process.execPath, [toolPath, 'plan', '--root', root, '--expect-selected', '1', '--expect-preserved', '0'], { encoding: 'utf8' });
  assert.equal(planned.status, 0, planned.stderr);
});

test('manifest blocks ambiguous legacy rows and preserves archives', async () => {
  const root = await fixture();
  await put(root, 'patch/ambiguous.patch.md', legacyBody);
  await put(root, 'supplier-manager-runtime/archive/patch/preserved.patch.md', legacyBody);
  const manifest = await buildManifest({ root, archivePrefixes: ['supplier-manager-runtime/archive/patch'], evidenceByPath: {} });
  assert.equal(manifest.blockers.length, 1);
  assert.equal(manifest.preserved.length, 1);
  assert.equal(manifest.rows.length, 0);
});

test('manifest blocks duplicate proposed destinations before apply', async () => {
  const root = await fixture();
  await put(root, 'patch/first.patch.md', legacyBody);
  await put(root, 'patch/second.patch.md', legacyBody);
  const shared = { ...evidence, slug: 'shared-target' };
  const manifest = await buildManifest({
    root,
    archivePrefixes: [],
    evidenceByPath: {
      'patch/first.patch.md': shared,
      'patch/second.patch.md': shared,
    },
  });
  assert.equal(manifest.rows.length, 0);
  assert.equal(manifest.blockers.length, 2);
  assert.ok(manifest.blockers.every((row) => row.status === 'destination-collision'));
});

test('apply requires execute and manifest hash, then verify proves convergence', async () => {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  await put(root, 'phase/phase-001.md', '[Patch](../patch/legacy.patch.md)\n');
  const manifest = await buildManifest({ root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } });
  const dry = await applyManifest({ root, manifest });
  assert.equal(dry.executed, false);
  await assert.rejects(() => applyManifest({ root, manifest, execute: true, approvedManifestSha256: 'wrong' }), /approval hash/);
  const applied = await applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256, journalPath: join(root, 'apply.journal.json') });
  assert.equal(applied.executed, true);
  assert.equal((await stat(join(root, manifest.rows[0].newPath))).isFile(), true);
  await assert.rejects(() => stat(join(root, manifest.rows[0].oldPath)));
  assert.match(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), /2026-08-09T07-15-30Z--legacy\.patch\.md/);
  const verified = await verifyManifest({ root, manifest });
  assert.equal(verified.ok, true);
});

test('apply rejects stale source or reference hashes before mutation', async () => {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  await put(root, 'phase/phase-001.md', '../patch/legacy.patch.md\n');
  const manifest = await buildManifest({ root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } });
  await writeFile(join(root, 'phase/phase-001.md'), 'changed ../patch/legacy.patch.md\n');
  await assert.rejects(() => applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256 }), /hash changed/);
  assert.equal((await stat(join(root, 'patch/legacy.patch.md'))).isFile(), true);
});

test('rollback is explicit and refuses changed post-apply files', async () => {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  await put(root, 'phase/phase-001.md', '../patch/legacy.patch.md\n');
  const manifest = await buildManifest({ root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } });
  const applied = await applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256, journalPath: join(root, 'apply.journal.json') });
  const dry = await rollbackJournal({ root, journal: applied.journal });
  assert.equal(dry.executed, false);
  await writeFile(join(root, manifest.rows[0].newPath), 'operator change\n');
  await assert.rejects(() => rollbackJournal({ root, journal: applied.journal, execute: true, approvedJournalSha256: applied.journal.journalSha256 }), /changed after apply/);
});

test('rollback restores original paths and reference bytes when hashes match', async () => {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  const originalRef = '../patch/legacy.patch.md\n';
  await put(root, 'phase/phase-001.md', originalRef);
  const manifest = await buildManifest({ root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } });
  const applied = await applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256, journalPath: join(root, 'apply.journal.json') });
  const rolled = await rollbackJournal({ root, journal: applied.journal, execute: true, approvedJournalSha256: applied.journal.journalSha256 });
  assert.equal(rolled.executed, true);
  assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), originalRef);
  assert.equal(await readFile(join(root, 'patch/legacy.patch.md'), 'utf8'), legacyBody);
  await assert.rejects(() => stat(join(root, manifest.rows[0].newPath)));
});

test('apply reserves the rollback journal before mutation', async () => {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  const originalRef = '../patch/legacy.patch.md\n';
  await put(root, 'phase/phase-001.md', originalRef);
  const manifest = await buildManifest({ root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } });
  const journalPath = await put(root, 'existing-journal.json', '{"occupied":true}\n');
  await assert.rejects(
    () => applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256, journalPath }),
    /exist/i,
  );
  assert.equal(await readFile(join(root, 'patch/legacy.patch.md'), 'utf8'), legacyBody);
  assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), originalRef);
  await assert.rejects(() => stat(join(root, manifest.rows[0].newPath)));
});

test('explicit rollback converges a staged partial source state', async () => {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  const originalRef = '../patch/legacy.patch.md\n';
  await put(root, 'phase/phase-001.md', originalRef);
  const manifest = await buildManifest({ root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } });
  const applied = await applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256, journalPath: join(root, 'apply.journal.json') });
  await put(root, manifest.rows[0].oldPath, legacyBody);
  const rolled = await rollbackJournal({ root, journal: applied.journal, execute: true, approvedJournalSha256: applied.journal.journalSha256 });
  assert.equal(rolled.executed, true);
  assert.equal(await readFile(join(root, manifest.rows[0].oldPath), 'utf8'), legacyBody);
  assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), originalRef);
  await assert.rejects(() => stat(join(root, manifest.rows[0].newPath)));
});

test('journal durability barrier completes before any apply mutation', async () => {
  const { root, manifest, originalReference, journalPath } = await migrationFixture();
  await assert.rejects(
    () => applyManifest({
      root,
      manifest,
      execute: true,
      approvedManifestSha256: manifest.manifestSha256,
      journalPath,
      hooks: { afterJournalPersisted: () => { throw new Error('persistence barrier stopped'); } },
    }),
    /persistence barrier stopped/,
  );
  const journal = await readJson(journalPath);
  assert.match(journal.journalSha256, /^[a-f0-9]{64}$/);
  assert.equal((await stat(journalPath)).mode & 0o777, 0o600);
  assert.equal(await readFile(join(root, manifest.rows[0].oldPath), 'utf8'), legacyBody);
  assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), originalReference);
  await assert.rejects(() => stat(join(root, manifest.rows[0].newPath)));
});

test('explicit rollback recovers apply interruptions around source publication', async () => {
  for (const hookName of ['afterApplySourceTempWrite', 'afterApplySourcePublish']) {
    const { root, manifest, originalReference, journalPath } = await migrationFixture();
    await assert.rejects(
      () => applyManifest({
        root,
        manifest,
        execute: true,
        approvedManifestSha256: manifest.manifestSha256,
        journalPath,
        hooks: { [hookName]: () => { throw new Error(`interrupted at ${hookName}`); } },
      }),
      new RegExp(`interrupted at ${hookName}`),
    );
    const journal = await readJson(journalPath);
    const rolled = await rollbackJournal({ root, journal, execute: true, approvedJournalSha256: journal.journalSha256 });
    assert.equal(rolled.executed, true);
    assert.equal(await readFile(join(root, manifest.rows[0].oldPath), 'utf8'), legacyBody);
    assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), originalReference);
    await assert.rejects(() => stat(join(root, manifest.rows[0].newPath)));
  }
});

test('explicit rollback is restartable around source restoration publication', async () => {
  for (const hookName of ['afterRollbackSourceTempWrite', 'afterRollbackSourcePublish']) {
    const { root, manifest, originalReference, journalPath } = await migrationFixture();
    const applied = await applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256, journalPath });
    await assert.rejects(
      () => rollbackJournal({
        root,
        journal: applied.journal,
        execute: true,
        approvedJournalSha256: applied.journal.journalSha256,
        hooks: { [hookName]: () => { throw new Error(`interrupted at ${hookName}`); } },
      }),
      new RegExp(`interrupted at ${hookName}`),
    );
    const rolled = await rollbackJournal({ root, journal: applied.journal, execute: true, approvedJournalSha256: applied.journal.journalSha256 });
    assert.equal(rolled.executed, true);
    assert.equal(await readFile(join(root, manifest.rows[0].oldPath), 'utf8'), legacyBody);
    assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), originalReference);
    await assert.rejects(() => stat(join(root, manifest.rows[0].newPath)));
  }
});

test('apply revalidates reference and source bytes at final mutation boundaries', async () => {
  {
    const { root, manifest, journalPath } = await migrationFixture();
    const operatorReference = 'operator changed reference in place\n';
    await assert.rejects(
      () => applyManifest({
        root,
        manifest,
        execute: true,
        approvedManifestSha256: manifest.manifestSha256,
        journalPath,
        hooks: {
          beforeApplyReferencePublish: async () => {
            await writeFile(join(root, 'phase/phase-001.md'), operatorReference);
          },
        },
      }),
      /target hash changed before replacement/,
    );
    assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), operatorReference);
    assert.equal(await readFile(join(root, manifest.rows[0].oldPath), 'utf8'), legacyBody);
    assert.equal((await stat(join(root, manifest.rows[0].newPath))).isFile(), true);
  }

  {
    const { root, manifest, journalPath } = await migrationFixture();
    const operatorSource = 'operator changed source in place\n';
    await assert.rejects(
      () => applyManifest({
        root,
        manifest,
        execute: true,
        approvedManifestSha256: manifest.manifestSha256,
        journalPath,
        hooks: {
          beforeApplySourceRemoval: async () => {
            await writeFile(join(root, manifest.rows[0].oldPath), operatorSource);
          },
        },
      }),
      /file hash changed before removal/,
    );
    assert.equal(await readFile(join(root, manifest.rows[0].oldPath), 'utf8'), operatorSource);
    assert.equal((await stat(join(root, manifest.rows[0].newPath))).isFile(), true);
  }
});

test('rollback revalidates reference and target bytes at final mutation boundaries', async () => {
  {
    const { root, manifest, journalPath } = await migrationFixture();
    const applied = await applyManifest({
      root,
      manifest,
      execute: true,
      approvedManifestSha256: manifest.manifestSha256,
      journalPath,
    });
    const operatorReference = 'operator changed applied reference in place\n';
    await assert.rejects(
      () => rollbackJournal({
        root,
        journal: applied.journal,
        execute: true,
        approvedJournalSha256: applied.journal.journalSha256,
        hooks: {
          beforeRollbackReferencePublish: async () => {
            await writeFile(join(root, 'phase/phase-001.md'), operatorReference);
          },
        },
      }),
      /target hash changed before replacement/,
    );
    assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), operatorReference);
    assert.equal(await readFile(join(root, manifest.rows[0].oldPath), 'utf8'), legacyBody);
    assert.equal((await stat(join(root, manifest.rows[0].newPath))).isFile(), true);
  }

  {
    const { root, manifest, originalReference, journalPath } = await migrationFixture();
    const applied = await applyManifest({
      root,
      manifest,
      execute: true,
      approvedManifestSha256: manifest.manifestSha256,
      journalPath,
    });
    const operatorTarget = 'operator changed applied target in place\n';
    await assert.rejects(
      () => rollbackJournal({
        root,
        journal: applied.journal,
        execute: true,
        approvedJournalSha256: applied.journal.journalSha256,
        hooks: {
          afterRollbackReferencePublish: async () => {
            await writeFile(join(root, manifest.rows[0].newPath), operatorTarget);
          },
        },
      }),
      /file hash changed before removal/,
    );
    assert.equal(await readFile(join(root, manifest.rows[0].newPath), 'utf8'), operatorTarget);
    assert.equal(await readFile(join(root, manifest.rows[0].oldPath), 'utf8'), legacyBody);
    assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), originalReference);
  }
});

test('apply rejects source and destination ancestor symlink substitution', async () => {
  {
    const { root, manifest, journalPath } = await migrationFixture({ reference: false });
    const external = await mkdtemp(join(tmpdir(), 'patch-timeline-external-'));
    await put(external, 'legacy.patch.md', legacyBody);
    const backup = join(root, 'patch-original');
    await assert.rejects(
      () => applyManifest({
        root,
        manifest,
        execute: true,
        approvedManifestSha256: manifest.manifestSha256,
        journalPath,
        hooks: {
          afterJournalPersisted: async () => {
            await rename(join(root, 'patch'), backup);
            await symlink(external, join(root, 'patch'), 'dir');
          },
        },
      }),
      /symlink path component/,
    );
    assert.equal(await readFile(join(external, 'legacy.patch.md'), 'utf8'), legacyBody);
    await assert.rejects(() => stat(join(external, manifest.rows[0].newPath.split('/').at(-1))));
    await rm(join(root, 'patch'));
    await rename(backup, join(root, 'patch'));
  }

  {
    const { root, manifest, journalPath } = await migrationFixture({ reference: false });
    const external = await mkdtemp(join(tmpdir(), 'patch-timeline-external-'));
    const backup = join(root, 'patch-original');
    await assert.rejects(
      () => applyManifest({
        root,
        manifest,
        execute: true,
        approvedManifestSha256: manifest.manifestSha256,
        journalPath,
        hooks: {
          beforeApplySourcePublish: async () => {
            await rename(join(root, 'patch'), backup);
            await symlink(external, join(root, 'patch'), 'dir');
          },
        },
      }),
      /symlink path component|directory changed before publish/,
    );
    await assert.rejects(() => stat(join(external, manifest.rows[0].newPath.split('/').at(-1))));
    await rm(join(root, 'patch'));
    await rename(backup, join(root, 'patch'));
    const journal = await readJson(journalPath);
    await rollbackJournal({ root, journal, execute: true, approvedJournalSha256: journal.journalSha256 });
  }
});

test('apply and rollback never rewrite references through substituted parent symlinks', async () => {
  const { root, manifest, originalReference, journalPath } = await migrationFixture();
  const external = await mkdtemp(join(tmpdir(), 'patch-timeline-external-'));
  await put(external, 'phase-001.md', originalReference);
  const backup = join(root, 'phase-original');
  await assert.rejects(
    () => applyManifest({
      root,
      manifest,
      execute: true,
      approvedManifestSha256: manifest.manifestSha256,
      journalPath,
      hooks: {
        beforeApplyReferencePublish: async () => {
          await rename(join(root, 'phase'), backup);
          await symlink(external, join(root, 'phase'), 'dir');
        },
      },
    }),
    /symlink path component|directory changed before replacement/,
  );
  assert.equal(await readFile(join(external, 'phase-001.md'), 'utf8'), originalReference);
  await rm(join(root, 'phase'));
  await rename(backup, join(root, 'phase'));
  const journal = await readJson(journalPath);
  await rollbackJournal({ root, journal, execute: true, approvedJournalSha256: journal.journalSha256 });

  const next = await migrationFixture();
  const applied = await applyManifest({ root: next.root, manifest: next.manifest, execute: true, approvedManifestSha256: next.manifest.manifestSha256, journalPath: next.journalPath });
  const appliedReference = await readFile(join(next.root, 'phase/phase-001.md'), 'utf8');
  const rollbackExternal = await mkdtemp(join(tmpdir(), 'patch-timeline-external-'));
  await put(rollbackExternal, 'phase-001.md', appliedReference);
  const rollbackBackup = join(next.root, 'phase-original');
  await assert.rejects(
    () => rollbackJournal({
      root: next.root,
      journal: applied.journal,
      execute: true,
      approvedJournalSha256: applied.journal.journalSha256,
      hooks: {
        beforeRollbackReferencePublish: async () => {
          await rename(join(next.root, 'phase'), rollbackBackup);
          await symlink(rollbackExternal, join(next.root, 'phase'), 'dir');
        },
      },
    }),
    /symlink path component|directory changed before replacement/,
  );
  assert.equal(await readFile(join(rollbackExternal, 'phase-001.md'), 'utf8'), appliedReference);
  await rm(join(next.root, 'phase'));
  await rename(rollbackBackup, join(next.root, 'phase'));
  await rollbackJournal({ root: next.root, journal: applied.journal, execute: true, approvedJournalSha256: applied.journal.journalSha256 });
  assert.equal(await readFile(join(next.root, 'phase/phase-001.md'), 'utf8'), next.originalReference);
});

test('rollback rejects source ancestor symlink substitution without touching external files', async () => {
  {
    const { root, manifest, journalPath } = await migrationFixture({ reference: false });
    const applied = await applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256, journalPath });
    const external = await mkdtemp(join(tmpdir(), 'patch-timeline-external-'));
    const externalNew = manifest.rows[0].newPath.split('/').at(-1);
    await put(external, externalNew, manifest.rows[0].newContent);
    const backup = join(root, 'patch-original');
    await rename(join(root, 'patch'), backup);
    await symlink(external, join(root, 'patch'), 'dir');
    await assert.rejects(
      () => rollbackJournal({ root, journal: applied.journal, execute: true, approvedJournalSha256: applied.journal.journalSha256 }),
      /symlink path component/,
    );
    assert.equal(await readFile(join(external, externalNew), 'utf8'), manifest.rows[0].newContent);
    await rm(join(root, 'patch'));
    await rename(backup, join(root, 'patch'));
    await rollbackJournal({ root, journal: applied.journal, execute: true, approvedJournalSha256: applied.journal.journalSha256 });
  }

  {
    const { root, manifest, journalPath } = await migrationFixture({ reference: false });
    const applied = await applyManifest({ root, manifest, execute: true, approvedManifestSha256: manifest.manifestSha256, journalPath });
    const external = await mkdtemp(join(tmpdir(), 'patch-timeline-external-'));
    const backup = join(root, 'patch-original');
    await assert.rejects(
      () => rollbackJournal({
        root,
        journal: applied.journal,
        execute: true,
        approvedJournalSha256: applied.journal.journalSha256,
        hooks: {
          beforeRollbackSourcePublish: async () => {
            await rename(join(root, 'patch'), backup);
            await symlink(external, join(root, 'patch'), 'dir');
          },
        },
      }),
      /symlink path component|directory changed before publish/,
    );
    await assert.rejects(() => stat(join(external, 'legacy.patch.md')));
    await rm(join(root, 'patch'));
    await rename(backup, join(root, 'patch'));
    await rollbackJournal({ root, journal: applied.journal, execute: true, approvedJournalSha256: applied.journal.journalSha256 });
  }
});

test('CLI create replays the approved creation instant across wall-clock seconds', async () => {
  const root = await fixture();
  const args = [
    toolPath, 'create', '--root', root, '--patch-dir', 'patch', '--slug', 'cli-stable-create',
    '--title', 'CLI Stable Create', '--creation-evidence', 'direct creator event',
    '--session', 'test-session', '--target-design', '../design/example.design.md',
    '--full-history', '../changelog/example.changelog.md',
  ];
  const previewed = spawnSync(process.execPath, args, { encoding: 'utf8' });
  assert.equal(previewed.status, 0, previewed.stderr);
  const preview = JSON.parse(previewed.stdout);

  const missingReplay = spawnSync(process.execPath, [...args, '--execute', '--approve-manifest-sha256', preview.manifestSha256], { encoding: 'utf8' });
  assert.equal(missingReplay.status, 1);
  assert.match(missingReplay.stderr, /--created-at/);

  while (new Date().toISOString().slice(0, 19) + 'Z' === preview.createdAt) {
    Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 25);
  }
  const executed = spawnSync(process.execPath, [...args, '--created-at', preview.createdAt, '--execute', '--approve-manifest-sha256', preview.manifestSha256], { encoding: 'utf8' });
  assert.equal(executed.status, 0, executed.stderr);
  assert.equal(JSON.parse(executed.stdout).path, preview.path);
  assert.equal((await stat(join(root, preview.path))).isFile(), true);
});

test('CLI apply persists its journal and CLI rollback restores the fixture', async () => {
  const root = await fixture();
  await put(root, 'patch/legacy.patch.md', legacyBody);
  const originalRef = '../patch/legacy.patch.md\n';
  await put(root, 'phase/phase-001.md', originalRef);
  const manifest = await buildManifest({ root, archivePrefixes: [], evidenceByPath: { 'patch/legacy.patch.md': evidence } });
  const manifestPath = await put(root, 'manifest.json', `${JSON.stringify(manifest, null, 2)}\n`);
  const journalPath = join(root, 'apply.journal.json');
  const applied = spawnSync(process.execPath, [toolPath, 'apply', '--root', root, '--manifest', manifestPath, '--execute', '--approve-manifest-sha256', manifest.manifestSha256, '--journal', journalPath], { encoding: 'utf8' });
  assert.equal(applied.status, 0, applied.stderr);
  const applyOutput = JSON.parse(applied.stdout);
  assert.equal(applyOutput.journalPath, journalPath);
  assert.equal('journal' in applyOutput, false);
  assert.doesNotMatch(applied.stdout, /originalContentBase64/);
  const journal = JSON.parse(await readFile(journalPath, 'utf8'));
  assert.equal((await stat(journalPath)).mode & 0o777, 0o600);
  assert.equal(journal.manifestSha256, manifest.manifestSha256);
  const rolled = spawnSync(process.execPath, [toolPath, 'rollback', '--root', root, '--journal', journalPath, '--execute', '--approve-journal-sha256', journal.journalSha256], { encoding: 'utf8' });
  assert.equal(rolled.status, 0, rolled.stderr);
  assert.equal(await readFile(join(root, 'patch/legacy.patch.md'), 'utf8'), legacyBody);
  assert.equal(await readFile(join(root, 'phase/phase-001.md'), 'utf8'), originalRef);
  await assert.rejects(() => stat(join(root, manifest.rows[0].newPath)));
});

test('CLI help matches accepted inventory, audit, and plan options', () => {
  const help = spawnSync(process.execPath, [toolPath, '--help'], { encoding: 'utf8' });
  assert.equal(help.status, 0, help.stderr);
  assert.match(help.stdout, /audit-evidence[^\n]+--archive-prefix[^\n]+--expect-selected[^\n]+--expect-preserved/);
  assert.match(help.stdout, /plan[^\n]+--archive-prefix[^\n]+--expect-selected[^\n]+--expect-preserved/);
  assert.match(help.stdout, /create[^\n]+--created-at/);
});

test('CLI rejects unknown flags and conflicting execution modes', async () => {
  const root = await fixture();
  const unknown = spawnSync(process.execPath, [toolPath, 'inventory', '--root', root, '--bogus', 'value'], { encoding: 'utf8' });
  assert.equal(unknown.status, 1);
  assert.match(unknown.stderr, /unknown argument for inventory: --bogus/);
  const conflict = spawnSync(process.execPath, [toolPath, 'create', '--root', root, '--execute', '--dry-run'], { encoding: 'utf8' });
  assert.equal(conflict.status, 1);
  assert.match(conflict.stderr, /--execute and --dry-run cannot be combined/);
});

test('symlink patch candidates fail closed', async () => {
  const root = await fixture();
  await put(root, 'outside.patch.md', legacyBody);
  await symlink(join(root, 'outside.patch.md'), join(root, 'patch', 'link.patch.md'));
  await assert.rejects(() => inventoryPatches({ root, archivePrefixes: [] }), /symlink/);
});

test('hash helper is stable', () => {
  assert.equal(sha256('abc'), 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad');
});
