#!/usr/bin/env node

import {
  link,
  lstat,
  mkdir,
  open,
  readFile,
  readdir,
  realpath,
  rename,
  rm,
  stat,
} from 'node:fs/promises';
import { constants } from 'node:fs';
import { createHash } from 'node:crypto';
import { basename, dirname, isAbsolute, join, relative, resolve, sep } from 'node:path';
import process from 'node:process';
import { pathToFileURL } from 'node:url';

const PATCH_FILENAME = /^(\d{4}-\d{2}-\d{2}T\d{2}-\d{2}-\d{2}Z)--([a-z0-9]+(?:-[a-z0-9]+)*)\.patch\.md$/;
const ISO_SECONDS = /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$/;
const PATCH_TOKEN = /(?<![A-Za-z0-9_*])((?:\.{0,2}\/|\/)?[A-Za-z0-9._/-]+\.patch\.md)(?![A-Za-z0-9_*])/g;
const SKIP_DIRECTORIES = new Set(['.git', 'node_modules', '.claude', '.memsearch']);
const GOVERNED_REFERENCE_EXTENSIONS = new Set(['.md']);
const AUTHORITATIVE_EVIDENCE = [
  /direct creator/i,
  /creator event/i,
  /exclusive.*creat/i,
  /transcript.*creat/i,
  /filesystem birthtime/i,
  /operator[- ]provided/i,
  /authoritative external/i,
];
const PROHIBITED_EVIDENCE = [
  /\bmtime\b/i,
  /\bctime\b/i,
  /alphabet/i,
  /phase (?:number|date)/i,
  /changelog date/i,
  /git first[- ]add/i,
  /session uuid/i,
  /directory position/i,
];

function toPosix(value) {
  return value.split(sep).join('/');
}

function pathMode(value) {
  return value.mode & 0o777;
}

function modeString(mode) {
  return mode.toString(8).padStart(3, '0');
}

function parseMode(mode) {
  return typeof mode === 'number' ? mode : Number.parseInt(mode, 8);
}

function isContained(root, candidate) {
  const delta = relative(root, candidate);
  return delta === '' || (!delta.startsWith(`..${sep}`) && delta !== '..' && !isAbsolute(delta));
}

function assertContained(root, candidate, label = 'path') {
  if (!isContained(root, candidate)) throw new Error(`${label} escapes root: ${candidate}`);
}

function validUtcSecond(value) {
  if (!ISO_SECONDS.test(value)) return false;
  const parsed = new Date(value);
  return !Number.isNaN(parsed.valueOf()) && parsed.toISOString().replace(/\.000Z$/, 'Z') === value;
}

function filenameTimestamp(createdAt) {
  return createdAt.replaceAll(':', '-');
}

function metadataValue(content, label) {
  const escaped = label.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return content.match(new RegExp(`^> \\*\\*${escaped}:\\*\\*\\s*(.+?)\\s*$`, 'm'))?.[1] ?? null;
}

function singleLineValue(value, label) {
  if (typeof value !== 'string' || value.trim() === '') throw new Error(`${label} is required`);
  if (/[\r\n]/.test(value)) throw new Error(`${label} must be a single line`);
  return value.trim();
}

function authoritativeEvidence(source) {
  if (typeof source !== 'string' || source.trim() === '') return false;
  if (PROHIBITED_EVIDENCE.some((pattern) => pattern.test(source))) return false;
  return AUTHORITATIVE_EVIDENCE.some((pattern) => pattern.test(source));
}

function semanticSlug(path, evidence) {
  if (evidence?.slug && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(evidence.slug)) return evidence.slug;
  const stem = basename(path, '.patch.md')
    .normalize('NFKD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .replace(/-{2,}/g, '-');
  return /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(stem) ? stem : null;
}

export function sha256(value) {
  return createHash('sha256').update(value).digest('hex');
}

export function parsePatchFilename(name) {
  const match = PATCH_FILENAME.exec(name);
  if (!match) return null;
  const createdAt = match[1].replace(/T(\d{2})-(\d{2})-(\d{2})Z$/, 'T$1:$2:$3Z');
  if (!validUtcSecond(createdAt)) return null;
  return { createdAt, slug: match[2] };
}

export function classifyPatch(path, content, evidence = null, { preserved = false } = {}) {
  if (preserved) return { status: 'preserved-suspended-archive', path };

  const parsed = parsePatchFilename(basename(path));
  const metadataCreatedAt = metadataValue(content, 'Created At');
  const metadataEvidence = metadataValue(content, 'Creation Evidence');

  if (parsed) {
    const valid = metadataCreatedAt === parsed.createdAt
      && validUtcSecond(metadataCreatedAt)
      && authoritativeEvidence(metadataEvidence);
    return {
      status: valid ? 'compliant' : 'invalid',
      path,
      createdAt: parsed.createdAt,
      slug: parsed.slug,
      metadataCreatedAt,
      creationEvidence: metadataEvidence,
      reason: valid ? null : 'canonical filename requires matching Created At and authoritative Creation Evidence',
    };
  }

  const createdAt = evidence?.createdAt;
  const source = evidence?.source;
  const validEvidence = validUtcSecond(createdAt) && authoritativeEvidence(source);
  return {
    status: validEvidence ? 'legacy-authoritative' : 'legacy-ambiguous',
    path,
    createdAt: validEvidence ? createdAt : null,
    creationEvidence: validEvidence ? source : null,
    slug: validEvidence ? semanticSlug(path, evidence) : null,
    reason: validEvidence ? null : 'legacy Patch lacks admissible original-creation evidence',
  };
}

async function normalizedRoot(root) {
  if (!root) throw new Error('--root is required');
  const value = await realpath(resolve(root));
  const details = await stat(value);
  if (!details.isDirectory()) throw new Error(`root is not a directory: ${root}`);
  return value;
}

function sameIdentity(left, right) {
  return left.dev === right.dev && left.ino === right.ino;
}

async function assertNoSymlinkAncestors(root, candidate, { allowMissingFinal = false } = {}) {
  const target = resolve(candidate);
  assertContained(root, target);
  const delta = relative(root, target);
  if (delta === '') return;

  let current = root;
  const parts = delta.split(sep);
  for (let index = 0; index < parts.length; index += 1) {
    current = join(current, parts[index]);
    let details;
    try {
      details = await lstat(current);
    } catch (error) {
      if (error.code === 'ENOENT' && allowMissingFinal && index === parts.length - 1) return;
      throw error;
    }
    if (details.isSymbolicLink()) throw new Error(`symlink path component is not allowed: ${toPosix(relative(root, current))}`);
    if (index < parts.length - 1 && !details.isDirectory()) {
      throw new Error(`non-directory path component: ${toPosix(relative(root, current))}`);
    }
  }
}

async function syncDirectoryPath(directory) {
  let handle;
  try {
    handle = await open(directory, constants.O_RDONLY | (constants.O_DIRECTORY ?? 0) | (constants.O_NOFOLLOW ?? 0));
    await handle.sync();
  } catch (error) {
    if (process.platform === 'win32' && ['EACCES', 'EINVAL', 'EISDIR', 'ENOTSUP', 'EPERM'].includes(error.code)) return;
    throw error;
  } finally {
    await handle?.close().catch(() => {});
  }
}

async function openBoundDirectory(root, directory) {
  const lexicalDirectory = resolve(directory);
  assertContained(root, lexicalDirectory, 'directory');
  await assertNoSymlinkAncestors(root, lexicalDirectory);
  const before = await lstat(lexicalDirectory);
  if (!before.isDirectory()) throw new Error(`expected directory: ${toPosix(relative(root, lexicalDirectory))}`);

  let handle;
  try {
    handle = await open(lexicalDirectory, constants.O_RDONLY | (constants.O_DIRECTORY ?? 0) | (constants.O_NOFOLLOW ?? 0));
  } catch (error) {
    if (process.platform !== 'win32' || !['EACCES', 'EINVAL', 'EISDIR', 'ENOTSUP', 'EPERM'].includes(error.code)) throw error;
  }

  let ioDirectory = lexicalDirectory;
  try {
    if (handle) {
      const opened = await handle.stat();
      if (!opened.isDirectory() || !sameIdentity(before, opened)) throw new Error(`directory changed during binding: ${toPosix(relative(root, lexicalDirectory))}`);
      if (process.platform === 'linux') {
        const descriptorPath = `/proc/self/fd/${handle.fd}`;
        const [boundPath, expectedPath] = await Promise.all([realpath(descriptorPath), realpath(lexicalDirectory)]);
        if (boundPath !== expectedPath || !isContained(root, boundPath)) {
          throw new Error(`directory binding escaped root: ${toPosix(relative(root, lexicalDirectory))}`);
        }
        ioDirectory = descriptorPath;
      }
    }

    await assertNoSymlinkAncestors(root, lexicalDirectory);
    const after = await lstat(lexicalDirectory);
    if (!sameIdentity(before, after)) throw new Error(`directory changed during binding: ${toPosix(relative(root, lexicalDirectory))}`);
    return { handle, ioDirectory, lexicalDirectory, identity: before };
  } catch (error) {
    await handle?.close().catch(() => {});
    throw error;
  }
}

async function closeBoundDirectory(bound) {
  await bound.handle?.close();
}

async function syncBoundDirectory(bound) {
  if (bound.handle) await bound.handle.sync();
  else await syncDirectoryPath(bound.lexicalDirectory);
}

async function ensureSafeDirectory(root, directory) {
  const target = resolve(directory);
  assertContained(root, target, 'directory');
  const delta = relative(root, target);
  if (delta === '') return;

  let current = root;
  for (const part of delta.split(sep)) {
    const bound = await openBoundDirectory(root, current);
    try {
      const child = join(bound.ioDirectory, part);
      try {
        const details = await lstat(child);
        if (details.isSymbolicLink() || !details.isDirectory()) throw new Error(`unsafe directory path: ${toPosix(relative(root, join(current, part)))}`);
      } catch (error) {
        if (error.code !== 'ENOENT') throw error;
        await mkdir(child);
        await syncBoundDirectory(bound);
      }
    } finally {
      await closeBoundDirectory(bound);
    }
    current = join(current, part);
  }
  await assertNoSymlinkAncestors(root, target);
}

async function walkFiles(root, { patchOnly = false, excludePrefixes = [] } = {}) {
  const files = [];
  const excluded = normalizedPrefixes(excludePrefixes);
  async function visit(directory) {
    const entries = await readdir(directory, { withFileTypes: true });
    entries.sort((a, b) => a.name.localeCompare(b.name));
    for (const entry of entries) {
      if (SKIP_DIRECTORIES.has(entry.name)) continue;
      const target = join(directory, entry.name);
      const targetRelative = toPosix(relative(root, target));
      if (underPrefix(targetRelative, excluded)) continue;
      if (entry.isSymbolicLink()) {
        if (entry.name.endsWith('.patch.md')) throw new Error(`Patch symlink is not allowed: ${toPosix(relative(root, target))}`);
        continue;
      }
      if (entry.isDirectory()) {
        await visit(target);
      } else if (entry.isFile() && (!patchOnly || entry.name.endsWith('.patch.md'))) {
        files.push(target);
      }
    }
  }
  await visit(root);
  return files;
}

function normalizedPrefixes(prefixes = []) {
  return [...new Set(prefixes.map((item) => toPosix(item).replace(/^\.\//, '').replace(/\/$/, '')).filter(Boolean))].sort();
}

function underPrefix(path, prefixes) {
  return prefixes.some((prefix) => path === prefix || path.startsWith(`${prefix}/`));
}

async function fileRecord(root, absolute) {
  const target = resolve(absolute);
  assertContained(root, target);
  const bound = await openBoundDirectory(root, dirname(target));
  let handle;
  try {
    const boundTarget = join(bound.ioDirectory, basename(target));
    const before = await lstat(boundTarget);
    if (before.isSymbolicLink() || !before.isFile()) throw new Error(`expected regular file: ${toPosix(relative(root, target))}`);
    handle = await open(boundTarget, constants.O_RDONLY | (constants.O_NOFOLLOW ?? 0));
    const opened = await handle.stat();
    if (!opened.isFile() || !sameIdentity(before, opened)) throw new Error(`file changed during binding: ${toPosix(relative(root, target))}`);
    const bytes = await handle.readFile();
    const after = await lstat(boundTarget);
    if (!sameIdentity(before, after)) throw new Error(`file changed during read: ${toPosix(relative(root, target))}`);
    return {
      path: toPosix(relative(root, target)),
      sha256: sha256(bytes),
      mode: modeString(pathMode(opened)),
      size: bytes.length,
      content: bytes.toString('utf8'),
    };
  } finally {
    await handle?.close().catch(() => {});
    await closeBoundDirectory(bound);
  }
}

export async function inventoryPatches({ root, archivePrefixes = [], excludePrefixes = [], evidenceByPath = {} }) {
  const actualRoot = await normalizedRoot(root);
  const prefixes = normalizedPrefixes(archivePrefixes);
  const excluded = normalizedPrefixes(excludePrefixes);
  const paths = await walkFiles(actualRoot, { patchOnly: true, excludePrefixes: excluded });
  const files = [];
  for (const absolute of paths) {
    const record = await fileRecord(actualRoot, absolute);
    const preserved = underPrefix(record.path, prefixes);
    files.push({
      ...record,
      ...classifyPatch(record.path, record.content, evidenceByPath[record.path], { preserved }),
      content: undefined,
    });
  }
  files.sort((a, b) => a.path.localeCompare(b.path));
  return {
    root: actualRoot,
    archivePrefixes: prefixes,
    excludePrefixes: excluded,
    totalCount: files.length,
    selectedCount: files.filter((row) => row.status !== 'preserved-suspended-archive').length,
    preservedCount: files.filter((row) => row.status === 'preserved-suspended-archive').length,
    files,
  };
}

function insertCreationMetadata(content, createdAt, source) {
  if (metadataValue(content, 'Created At') || metadataValue(content, 'Creation Evidence')) {
    throw new Error('legacy Patch already contains partial creation metadata');
  }
  const lines = content.split('\n');
  const statusIndex = lines.findIndex((line) => /^> \*\*Status:\*\*/.test(line));
  const insertAt = statusIndex >= 0 ? statusIndex + 1 : Math.min(lines.length, 2);
  lines.splice(insertAt, 0,
    `> **Created At:** ${createdAt}`,
    `> **Creation Evidence:** ${source}`,
  );
  return lines.join('\n');
}

function governedReferenceFile(path) {
  if (path.endsWith('.patch.md')) return false;
  const extension = path.slice(path.lastIndexOf('.'));
  if (!GOVERNED_REFERENCE_EXTENSIONS.has(extension)) return false;
  const first = path.split('/')[0];
  return ['phase', 'design', 'changelog', 'todo', 'patch'].includes(first)
    || !path.includes('/');
}

function replacementToken({ root, token, referencePath, oldPath, newPath }) {
  const referenceDir = dirname(referencePath);
  if (isAbsolute(token)) {
    const absolute = resolve(token);
    return isContained(root, absolute) ? toPosix(resolve(root, newPath)) : `/${newPath}`;
  }
  if (token.startsWith('.')) {
    let value = toPosix(relative(referenceDir, newPath));
    if (!value.startsWith('.')) value = `./${value}`;
    return value;
  }
  if (token === oldPath || token.startsWith(oldPath.split('/')[0] + '/')) return newPath;
  let value = toPosix(relative(referenceDir, newPath));
  if (!value.startsWith('.')) value = `./${value}`;
  return value;
}

function uriShapedReference(content, offset, token) {
  const lineStart = content.lastIndexOf('\n', offset - 1) + 1;
  const throughToken = `${content.slice(lineStart, offset)}${token}`;
  return /[A-Za-z][A-Za-z0-9+.-]*:\/\/[^\s<>()\[\]`]*$/.test(throughToken);
}

function resolveReferenceToken(root, referencePath, token, oldPaths) {
  if (token.includes('*')) return null;
  const candidates = [];
  if (isAbsolute(token)) {
    const absolute = resolve(token);
    if (isContained(root, absolute)) candidates.push(absolute);
    else candidates.push(resolve(root, token.replace(/^\/+/, '')));
  } else {
    candidates.push(resolve(root, dirname(referencePath), token));
    candidates.push(resolve(root, token));
  }
  for (const candidate of candidates) {
    if (!isContained(root, candidate)) continue;
    const relativeCandidate = toPosix(relative(root, candidate));
    if (oldPaths.has(relativeCandidate)) return relativeCandidate;
  }
  return null;
}

async function referenceChanges(root, mappings, excludePrefixes = []) {
  const oldPaths = new Set(mappings.keys());
  const allFiles = await walkFiles(root, { excludePrefixes });
  const changes = [];
  for (const absolute of allFiles) {
    const path = toPosix(relative(root, absolute));
    if (!governedReferenceFile(path)) continue;
    const details = await fileRecord(root, absolute);
    const replacements = [];
    const after = details.content.replace(PATCH_TOKEN, (match, token, offset, content) => {
      if (uriShapedReference(content, offset, token)) return match;
      const oldPath = resolveReferenceToken(root, path, token, oldPaths);
      if (!oldPath) return match;
      const newPath = mappings.get(oldPath);
      const next = replacementToken({ root, token, referencePath: path, oldPath, newPath });
      replacements.push({ oldPath, newPath, before: token, after: next });
      return next;
    });
    if (after === details.content) continue;
    changes.push({
      path,
      sha256: details.sha256,
      mode: details.mode,
      before: details.content,
      after,
      afterSha256: sha256(after),
      replacements,
    });
  }
  changes.sort((a, b) => a.path.localeCompare(b.path));
  return changes;
}

function manifestCore(manifest) {
  const { manifestSha256, ...core } = manifest;
  return core;
}

export function canonicalManifest(manifest) {
  return `${JSON.stringify(manifestCore(manifest), null, 2)}\n`;
}

function withManifestHash(manifest) {
  return { ...manifest, manifestSha256: sha256(canonicalManifest(manifest)) };
}

export async function buildManifest({ root, archivePrefixes = [], excludePrefixes = [], evidenceByPath = {} }) {
  const actualRoot = await normalizedRoot(root);
  const prefixes = normalizedPrefixes(archivePrefixes);
  const excluded = normalizedPrefixes(excludePrefixes);
  const patchPaths = await walkFiles(actualRoot, { patchOnly: true, excludePrefixes: excluded });
  const rows = [];
  const blockers = [];
  const preserved = [];
  const mappings = new Map();

  for (const absolute of patchPaths) {
    const record = await fileRecord(actualRoot, absolute);
    const isPreserved = underPrefix(record.path, prefixes);
    const classified = classifyPatch(record.path, record.content, evidenceByPath[record.path], { preserved: isPreserved });
    if (classified.status === 'preserved-suspended-archive') {
      preserved.push({ path: record.path, sha256: record.sha256, mode: record.mode, size: record.size });
      continue;
    }
    if (classified.status === 'compliant') continue;
    if (classified.status !== 'legacy-authoritative' || !classified.slug) {
      blockers.push({ path: record.path, status: classified.status, reason: classified.reason ?? 'missing semantic slug' });
      continue;
    }
    const newName = `${filenameTimestamp(classified.createdAt)}--${classified.slug}.patch.md`;
    const newPath = toPosix(join(dirname(record.path), newName));
    if (newPath !== record.path) {
      const destination = join(actualRoot, newPath);
      assertContained(actualRoot, destination, 'destination');
      try {
        await lstat(destination);
        blockers.push({ path: record.path, status: 'destination-collision', reason: `destination exists: ${newPath}` });
        continue;
      } catch (error) {
        if (error.code !== 'ENOENT') throw error;
      }
    }
    const newContent = insertCreationMetadata(record.content, classified.createdAt, classified.creationEvidence);
    const row = {
      oldPath: record.path,
      newPath,
      sourceSha256: record.sha256,
      sourceMode: record.mode,
      createdAt: classified.createdAt,
      creationEvidence: classified.creationEvidence,
      slug: classified.slug,
      newContent,
      newContentSha256: sha256(newContent),
      references: [],
    };
    rows.push(row);
    mappings.set(record.path, newPath);
  }

  const destinationGroups = new Map();
  for (const row of rows) {
    const group = destinationGroups.get(row.newPath) ?? [];
    group.push(row);
    destinationGroups.set(row.newPath, group);
  }
  const duplicateSources = new Set();
  for (const [newPath, group] of destinationGroups) {
    if (group.length < 2) continue;
    for (const row of group) {
      duplicateSources.add(row.oldPath);
      mappings.delete(row.oldPath);
      blockers.push({ path: row.oldPath, status: 'destination-collision', reason: `multiple rows propose destination: ${newPath}` });
    }
  }
  for (let index = rows.length - 1; index >= 0; index -= 1) {
    if (duplicateSources.has(rows[index].oldPath)) rows.splice(index, 1);
  }

  const references = await referenceChanges(actualRoot, mappings, excluded);
  for (const row of rows) {
    row.references = references
      .filter((reference) => reference.replacements.some((replacement) => replacement.oldPath === row.oldPath))
      .map(({ path, sha256: digest, mode, before, after, afterSha256, replacements }) => ({
        path,
        sha256: digest,
        mode,
        before,
        after,
        afterSha256,
        replacements: replacements.filter((replacement) => replacement.oldPath === row.oldPath),
      }));
  }

  rows.sort((a, b) => a.oldPath.localeCompare(b.oldPath));
  blockers.sort((a, b) => a.path.localeCompare(b.path));
  preserved.sort((a, b) => a.path.localeCompare(b.path));

  return withManifestHash({
    schemaVersion: 1,
    tool: 'patch-timeline',
    root: actualRoot,
    archivePrefixes: prefixes,
    excludePrefixes: excluded,
    totalCount: patchPaths.length,
    selectedCount: patchPaths.length - preserved.length,
    preservedCount: preserved.length,
    rows,
    blockers,
    preserved,
    references,
  });
}

function createPatchBody({ title, createdAt, creationEvidence, session, targetDesign, fullHistory, body = '' }) {
  const suffix = body ? `\n${body.trimEnd()}\n` : '\n## Context\n\nThis governed Patch records a before/after review surface selected by the active execution authority.\n';
  return `# ${title}\n\n> **Current Version:** 1.0\n> **Session:** ${session}\n> **Status:** active\n> **Created At:** ${createdAt}\n> **Creation Evidence:** ${creationEvidence}\n> **Target Design:** ${targetDesign}\n> **Full history:** ${fullHistory}\n${suffix}`;
}

function createPreview({ root, path, content, createdAt, creationEvidence, slug }) {
  const core = {
    schemaVersion: 1,
    tool: 'patch-timeline',
    operation: 'create',
    root,
    path,
    createdAt,
    creationEvidence,
    slug,
    contentSha256: sha256(content),
  };
  return { ...core, manifestSha256: sha256(`${JSON.stringify(core, null, 2)}\n`) };
}

export async function createPatch({
  root,
  patchDir = 'patch',
  slug,
  title,
  creationEvidence,
  session,
  targetDesign,
  fullHistory,
  body = '',
  createdAt: requestedCreatedAt = null,
  now = () => new Date(),
  execute = false,
  approvedManifestSha256 = null,
}) {
  const actualRoot = await normalizedRoot(root);
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(slug ?? '')) throw new Error('slug must be lowercase ASCII kebab-case');
  const normalizedTitle = singleLineValue(title, 'title');
  const normalizedCreationEvidence = singleLineValue(creationEvidence, 'Creation Evidence');
  if (!authoritativeEvidence(normalizedCreationEvidence)) throw new Error('authoritative Creation Evidence is required');
  const normalizedSession = singleLineValue(session, 'session');
  const normalizedTargetDesign = singleLineValue(targetDesign, 'target design');
  const normalizedFullHistory = singleLineValue(fullHistory, 'full history');

  let createdAt;
  if (requestedCreatedAt !== null) {
    if (!validUtcSecond(requestedCreatedAt)) throw new Error('created at must be a valid UTC second');
    createdAt = requestedCreatedAt;
  } else {
    const captured = now();
    if (!(captured instanceof Date) || Number.isNaN(captured.valueOf())) throw new Error('clock returned an invalid Date');
    createdAt = captured.toISOString().replace(/\.\d{3}Z$/, 'Z');
  }
  const relativePath = toPosix(join(patchDir, `${filenameTimestamp(createdAt)}--${slug}.patch.md`));
  const target = resolve(actualRoot, relativePath);
  assertContained(actualRoot, target, 'Patch destination');
  const content = createPatchBody({
    title: normalizedTitle,
    createdAt,
    creationEvidence: normalizedCreationEvidence,
    session: normalizedSession,
    targetDesign: normalizedTargetDesign,
    fullHistory: normalizedFullHistory,
    body,
  });
  const preview = createPreview({ root: actualRoot, path: relativePath, content, createdAt, creationEvidence: normalizedCreationEvidence, slug });

  if (!execute) return { ...preview, executed: false, content };
  if (approvedManifestSha256 !== preview.manifestSha256) throw new Error('create approval hash does not match preview manifest approval hash');
  await ensureSafeDirectory(actualRoot, dirname(target));
  try {
    await publishExclusiveFile(actualRoot, relativePath, content, 0o644);
  } catch (error) {
    if (/destination already exists/.test(error.message) || error.code === 'EEXIST') throw new Error(`Patch destination already exists: ${relativePath}`);
    throw error;
  }
  return { ...preview, executed: true, content: undefined };
}

async function verifyManifestIdentity(manifest) {
  const expected = sha256(canonicalManifest(manifest));
  if (manifest.manifestSha256 !== expected) throw new Error('manifest SHA-256 is invalid');
  if (manifest.blockers?.length) throw new Error(`manifest has ${manifest.blockers.length} blocker(s)`);
}

async function currentRecord(root, path) {
  const target = resolve(root, path);
  assertContained(root, target);
  return fileRecord(root, target);
}

async function optionalRecord(root, path) {
  try {
    return await currentRecord(root, path);
  } catch (error) {
    if (error.code === 'ENOENT') return null;
    throw error;
  }
}

async function reserveTemporary(bound, targetName, mode) {
  for (let attempt = 0; attempt < 100; attempt += 1) {
    const name = `.${targetName}.patch-timeline-${process.pid}-${attempt}.tmp`;
    const path = join(bound.ioDirectory, name);
    try {
      const handle = await open(path, 'wx', mode);
      return { handle, path };
    } catch (error) {
      if (error.code !== 'EEXIST') throw error;
    }
  }
  throw new Error(`could not reserve atomic write beside: ${join(bound.lexicalDirectory, targetName)}`);
}

async function boundFileState(bound, targetName) {
  const target = join(bound.ioDirectory, targetName);
  const before = await lstat(target);
  if (before.isSymbolicLink() || !before.isFile()) throw new Error(`expected regular file: ${targetName}`);
  let handle;
  try {
    handle = await open(target, constants.O_RDONLY | (constants.O_NOFOLLOW ?? 0));
    const opened = await handle.stat();
    if (!opened.isFile() || !sameIdentity(before, opened)) throw new Error(`file changed during binding: ${targetName}`);
    const bytes = await handle.readFile();
    const after = await lstat(target);
    if (!sameIdentity(before, after)) throw new Error(`file changed during read: ${targetName}`);
    return { sha256: sha256(bytes), mode: modeString(pathMode(opened)) };
  } finally {
    await handle?.close().catch(() => {});
  }
}

async function publishExclusiveFile(root, path, content, mode, hooks = {}) {
  const target = resolve(root, path);
  assertContained(root, target);
  const bound = await openBoundDirectory(root, dirname(target));
  let temporary;
  let handle;
  try {
    const targetName = basename(target);
    const boundTarget = join(bound.ioDirectory, targetName);
    try {
      await lstat(boundTarget);
      throw new Error(`destination already exists: ${path}`);
    } catch (error) {
      if (error.code !== 'ENOENT') throw error;
    }

    ({ handle, path: temporary } = await reserveTemporary(bound, targetName, mode));
    await handle.writeFile(content);
    await handle.chmod(mode);
    await handle.sync();
    await hooks.afterTempWrite?.();
    await handle.close();
    handle = null;
    await hooks.beforePublish?.();

    await assertNoSymlinkAncestors(root, bound.lexicalDirectory);
    const currentDirectory = await lstat(bound.lexicalDirectory);
    if (!sameIdentity(bound.identity, currentDirectory)) throw new Error(`directory changed before publish: ${toPosix(relative(root, bound.lexicalDirectory))}`);
    await link(temporary, boundTarget);
    await syncBoundDirectory(bound);
    await hooks.afterPublish?.();
    await rm(temporary);
    temporary = null;
    await syncBoundDirectory(bound);
  } catch (error) {
    await handle?.close().catch(() => {});
    if (temporary) await rm(temporary, { force: true }).catch(() => {});
    throw error;
  } finally {
    await closeBoundDirectory(bound);
  }
}

async function atomicReplaceFile(root, path, content, mode, { expectedSha256 = null, expectedMode = null, hooks = {} } = {}) {
  const target = resolve(root, path);
  assertContained(root, target);
  const bound = await openBoundDirectory(root, dirname(target));
  let temporary;
  let handle;
  try {
    const targetName = basename(target);
    const boundTarget = join(bound.ioDirectory, targetName);
    const initial = await boundFileState(bound, targetName);
    if (expectedSha256 !== null && initial.sha256 !== expectedSha256) throw new Error(`target hash changed before replacement: ${path}`);
    if (expectedMode !== null && initial.mode !== expectedMode) throw new Error(`target mode changed before replacement: ${path}`);

    ({ handle, path: temporary } = await reserveTemporary(bound, targetName, mode));
    await handle.writeFile(content);
    await handle.chmod(mode);
    await handle.sync();
    await hooks.afterTempWrite?.();
    await handle.close();
    handle = null;
    await hooks.beforePublish?.();

    await assertNoSymlinkAncestors(root, bound.lexicalDirectory);
    const currentDirectory = await lstat(bound.lexicalDirectory);
    if (!sameIdentity(bound.identity, currentDirectory)) throw new Error(`directory changed before replacement: ${toPosix(relative(root, bound.lexicalDirectory))}`);
    const current = await boundFileState(bound, targetName);
    if (expectedSha256 !== null && current.sha256 !== expectedSha256) throw new Error(`target hash changed before replacement: ${path}`);
    if (expectedMode !== null && current.mode !== expectedMode) throw new Error(`target mode changed before replacement: ${path}`);
    await rename(temporary, boundTarget);
    temporary = null;
    await syncBoundDirectory(bound);
    await hooks.afterPublish?.();
  } catch (error) {
    await handle?.close().catch(() => {});
    if (temporary) await rm(temporary, { force: true }).catch(() => {});
    throw error;
  } finally {
    await closeBoundDirectory(bound);
  }
}

async function removeBoundFile(root, path, { expectedSha256 = null, expectedMode = null } = {}) {
  const target = resolve(root, path);
  assertContained(root, target);
  const bound = await openBoundDirectory(root, dirname(target));
  try {
    const targetName = basename(target);
    const boundTarget = join(bound.ioDirectory, targetName);
    const current = await boundFileState(bound, targetName);
    if (expectedSha256 !== null && current.sha256 !== expectedSha256) throw new Error(`file hash changed before removal: ${path}`);
    if (expectedMode !== null && current.mode !== expectedMode) throw new Error(`file mode changed before removal: ${path}`);
    await rm(boundTarget);
    await syncBoundDirectory(bound);
  } finally {
    await closeBoundDirectory(bound);
  }
}

async function expectAbsent(root, path) {
  const target = resolve(root, path);
  assertContained(root, target);
  const bound = await openBoundDirectory(root, dirname(target));
  try {
    const boundTarget = join(bound.ioDirectory, basename(target));
    try {
      await lstat(boundTarget);
      throw new Error(`destination already exists: ${path}`);
    } catch (error) {
      if (error.code !== 'ENOENT') throw error;
    }
  } finally {
    await closeBoundDirectory(bound);
  }
}

function assertUniqueManifestPaths(manifest) {
  const oldPaths = new Set();
  const newPaths = new Set();
  const referencePaths = new Set();
  for (const row of manifest.rows) {
    if (oldPaths.has(row.oldPath)) throw new Error(`duplicate manifest source path: ${row.oldPath}`);
    if (newPaths.has(row.newPath)) throw new Error(`duplicate manifest destination path: ${row.newPath}`);
    oldPaths.add(row.oldPath);
    newPaths.add(row.newPath);
  }
  for (const reference of manifest.references) {
    if (referencePaths.has(reference.path)) throw new Error(`duplicate manifest reference path: ${reference.path}`);
    referencePaths.add(reference.path);
  }
}

async function preflightApply(root, manifest) {
  assertUniqueManifestPaths(manifest);
  for (const row of manifest.rows) {
    const source = await currentRecord(root, row.oldPath);
    if (source.sha256 !== row.sourceSha256) throw new Error(`source hash changed: ${row.oldPath}`);
    if (source.mode !== row.sourceMode) throw new Error(`source mode changed: ${row.oldPath}`);
    await expectAbsent(root, row.newPath);
  }
  for (const reference of manifest.references) {
    const current = await currentRecord(root, reference.path);
    if (current.sha256 !== reference.sha256) throw new Error(`reference hash changed: ${reference.path}`);
    if (current.mode !== reference.mode) throw new Error(`reference mode changed: ${reference.path}`);
  }
  for (const preserved of manifest.preserved) {
    const current = await currentRecord(root, preserved.path);
    if (current.sha256 !== preserved.sha256 || current.mode !== preserved.mode) {
      throw new Error(`preserved archive changed: ${preserved.path}`);
    }
  }
}

function journalCore(journal) {
  const { journalSha256, ...core } = journal;
  return core;
}

function withJournalHash(journal) {
  const core = journalCore(journal);
  return { ...core, journalSha256: sha256(`${JSON.stringify(core, null, 2)}\n`) };
}

export async function applyManifest({ root, manifest, execute = false, approvedManifestSha256 = null, journalPath = null, hooks = {} }) {
  const actualRoot = await normalizedRoot(root);
  if (manifest.root !== actualRoot) throw new Error(`manifest root mismatch: ${manifest.root}`);
  await verifyManifestIdentity(manifest);
  await preflightApply(actualRoot, manifest);
  if (!execute) return { executed: false, manifestSha256: manifest.manifestSha256 };
  if (approvedManifestSha256 !== manifest.manifestSha256) throw new Error('apply approval hash does not match manifest approval hash');
  if (!journalPath) throw new Error('journal path is required for executed apply');

  const sourceSnapshots = [];
  for (const row of manifest.rows) {
    const current = await currentRecord(actualRoot, row.oldPath);
    sourceSnapshots.push({
      oldPath: row.oldPath,
      newPath: row.newPath,
      originalContentBase64: Buffer.from(current.content).toString('base64'),
      originalSha256: current.sha256,
      originalMode: current.mode,
      appliedSha256: row.newContentSha256,
    });
  }
  const referenceSnapshots = manifest.references.map((reference) => ({
    path: reference.path,
    originalContentBase64: Buffer.from(reference.before).toString('base64'),
    originalSha256: reference.sha256,
    originalMode: reference.mode,
    appliedSha256: reference.afterSha256,
  }));
  const journal = withJournalHash({
    schemaVersion: 1,
    tool: 'patch-timeline',
    operation: 'apply',
    root: actualRoot,
    manifestSha256: manifest.manifestSha256,
    sources: sourceSnapshots,
    references: referenceSnapshots,
    preserved: manifest.preserved,
  });

  await writeJson(journalPath, journal);
  try {
    await hooks.afterJournalPersisted?.({ journal, journalPath: resolve(journalPath) });
    for (const row of manifest.rows) {
      const source = await currentRecord(actualRoot, row.oldPath);
      if (source.sha256 !== row.sourceSha256 || source.mode !== row.sourceMode) throw new Error(`source changed during apply: ${row.oldPath}`);
      await publishExclusiveFile(actualRoot, row.newPath, row.newContent, parseMode(row.sourceMode), {
        afterTempWrite: () => hooks.afterApplySourceTempWrite?.(row),
        beforePublish: () => hooks.beforeApplySourcePublish?.(row),
        afterPublish: () => hooks.afterApplySourcePublish?.(row),
      });
    }
    for (const reference of manifest.references) {
      const current = await currentRecord(actualRoot, reference.path);
      if (current.sha256 !== reference.sha256 || current.mode !== reference.mode) throw new Error(`reference changed during apply: ${reference.path}`);
      await atomicReplaceFile(actualRoot, reference.path, reference.after, parseMode(reference.mode), {
        expectedSha256: reference.sha256,
        expectedMode: reference.mode,
        hooks: {
          afterTempWrite: () => hooks.afterApplyReferenceTempWrite?.(reference),
          beforePublish: () => hooks.beforeApplyReferencePublish?.(reference),
          afterPublish: () => hooks.afterApplyReferencePublish?.(reference),
        },
      });
    }
    for (const row of manifest.rows) {
      const source = await currentRecord(actualRoot, row.oldPath);
      if (source.sha256 !== row.sourceSha256 || source.mode !== row.sourceMode) throw new Error(`source changed before removal: ${row.oldPath}`);
      await hooks.beforeApplySourceRemoval?.(row);
      await removeBoundFile(actualRoot, row.oldPath, {
        expectedSha256: row.sourceSha256,
        expectedMode: row.sourceMode,
      });
    }
  } catch (error) {
    throw new Error(`apply stopped after the rollback journal was written to ${resolve(journalPath)}: ${error.message}`);
  }

  return { executed: true, manifestSha256: manifest.manifestSha256, journal };
}

export async function verifyManifest({ root, manifest }) {
  const actualRoot = await normalizedRoot(root);
  if (manifest.root !== actualRoot) throw new Error(`manifest root mismatch: ${manifest.root}`);
  await verifyManifestIdentity(manifest);
  const errors = [];
  for (const row of manifest.rows) {
    try {
      const target = await currentRecord(actualRoot, row.newPath);
      if (target.sha256 !== row.newContentSha256) errors.push(`target hash mismatch: ${row.newPath}`);
      if (target.mode !== row.sourceMode) errors.push(`target mode mismatch: ${row.newPath}`);
      const classification = classifyPatch(row.newPath, target.content);
      if (classification.status !== 'compliant') errors.push(`target metadata invalid: ${row.newPath}`);
    } catch (error) {
      errors.push(error.message);
    }
    try {
      await lstat(resolve(actualRoot, row.oldPath));
      errors.push(`former path remains active: ${row.oldPath}`);
    } catch (error) {
      if (error.code !== 'ENOENT') errors.push(error.message);
    }
  }
  for (const reference of manifest.references) {
    try {
      const current = await currentRecord(actualRoot, reference.path);
      if (current.sha256 !== reference.afterSha256) errors.push(`reference did not converge: ${reference.path}`);
    } catch (error) {
      errors.push(error.message);
    }
  }
  for (const preserved of manifest.preserved) {
    try {
      const current = await currentRecord(actualRoot, preserved.path);
      if (current.sha256 !== preserved.sha256 || current.mode !== preserved.mode) errors.push(`preserved archive changed: ${preserved.path}`);
    } catch (error) {
      errors.push(error.message);
    }
  }
  return { ok: errors.length === 0, errors };
}

function canonicalJournal(journal) {
  return `${JSON.stringify(journalCore(journal), null, 2)}\n`;
}

async function preflightRollback(root, journal) {
  const expected = sha256(canonicalJournal(journal));
  if (journal.journalSha256 !== expected) throw new Error('journal SHA-256 is invalid');
  if (journal.root !== root) throw new Error(`journal root mismatch: ${journal.root}`);

  const sources = [];
  for (const source of journal.sources) {
    const [original, applied] = await Promise.all([
      optionalRecord(root, source.oldPath),
      optionalRecord(root, source.newPath),
    ]);
    const originalMatches = original?.sha256 === source.originalSha256 && original?.mode === source.originalMode;
    const appliedMatches = applied?.sha256 === source.appliedSha256 && applied?.mode === source.originalMode;
    let state;
    if (originalMatches && !applied) state = 'untouched';
    else if (originalMatches && appliedMatches) state = 'staged';
    else if (!original && appliedMatches) state = 'applied';
    else throw new Error(`source state changed after apply started: ${source.oldPath}`);
    sources.push({ ...source, state });
  }

  const references = [];
  for (const reference of journal.references) {
    const current = await currentRecord(root, reference.path);
    let state;
    if (current.sha256 === reference.originalSha256 && current.mode === reference.originalMode) state = 'untouched';
    else if (current.sha256 === reference.appliedSha256 && current.mode === reference.originalMode) state = 'applied';
    else throw new Error(`reference changed after apply started: ${reference.path}`);
    references.push({ ...reference, state });
  }
  for (const preserved of journal.preserved ?? []) {
    const current = await currentRecord(root, preserved.path);
    if (current.sha256 !== preserved.sha256 || current.mode !== preserved.mode) throw new Error(`preserved archive changed: ${preserved.path}`);
  }
  return { sources, references };
}

export async function rollbackJournal({ root, journal, execute = false, approvedJournalSha256 = null, hooks = {} }) {
  const actualRoot = await normalizedRoot(root);
  const plan = await preflightRollback(actualRoot, journal);
  if (!execute) return { executed: false, journalSha256: journal.journalSha256 };
  if (approvedJournalSha256 !== journal.journalSha256) throw new Error('rollback approval hash does not match journal approval hash');

  for (const source of plan.sources.filter((item) => item.state === 'applied')) {
    await publishExclusiveFile(actualRoot, source.oldPath, Buffer.from(source.originalContentBase64, 'base64'), parseMode(source.originalMode), {
      afterTempWrite: () => hooks.afterRollbackSourceTempWrite?.(source),
      beforePublish: () => hooks.beforeRollbackSourcePublish?.(source),
      afterPublish: () => hooks.afterRollbackSourcePublish?.(source),
    });
  }
  for (const reference of plan.references.filter((item) => item.state === 'applied')) {
    await atomicReplaceFile(actualRoot, reference.path, Buffer.from(reference.originalContentBase64, 'base64'), parseMode(reference.originalMode), {
      expectedSha256: reference.appliedSha256,
      expectedMode: reference.originalMode,
      hooks: {
        afterTempWrite: () => hooks.afterRollbackReferenceTempWrite?.(reference),
        beforePublish: () => hooks.beforeRollbackReferencePublish?.(reference),
        afterPublish: () => hooks.afterRollbackReferencePublish?.(reference),
      },
    });
  }
  for (const source of plan.sources.filter((item) => item.state !== 'untouched')) {
    await removeBoundFile(actualRoot, source.newPath, {
      expectedSha256: source.appliedSha256,
      expectedMode: source.originalMode,
    });
  }
  return { executed: true, journalSha256: journal.journalSha256 };
}

function parseArgs(argv) {
  const [command, ...rest] = argv;
  const values = { archivePrefixes: [], excludePrefixes: [] };
  const booleanFlags = new Set(['--execute', '--dry-run']);
  const commonInventory = ['--root', '--archive-prefix', '--exclude-prefix', '--expect-selected', '--expect-preserved'];
  const allowedByCommand = {
    inventory: new Set(commonInventory),
    'audit-evidence': new Set([...commonInventory, '--evidence-file']),
    plan: new Set([...commonInventory, '--evidence-file', '--output']),
    create: new Set(['--root', '--patch-dir', '--slug', '--title', '--creation-evidence', '--session', '--target-design', '--full-history', '--body', '--created-at', '--execute', '--dry-run', '--approve-manifest-sha256']),
    apply: new Set(['--root', '--manifest', '--execute', '--dry-run', '--approve-manifest-sha256', '--journal']),
    verify: new Set(['--root', '--manifest']),
    rollback: new Set(['--root', '--journal', '--execute', '--dry-run', '--approve-journal-sha256']),
  };
  const allowed = allowedByCommand[command];
  for (let index = 0; index < rest.length; index += 1) {
    const flag = rest[index];
    if (!flag.startsWith('--')) throw new Error(`unexpected positional argument: ${flag}`);
    if (allowed && !allowed.has(flag)) throw new Error(`unknown argument for ${command}: ${flag}`);
    if (booleanFlags.has(flag)) {
      values[flag.slice(2).replace(/-([a-z])/g, (_, char) => char.toUpperCase())] = true;
      continue;
    }
    const value = rest[index + 1];
    if (value === undefined || value.startsWith('--')) throw new Error(`missing value for ${flag}`);
    index += 1;
    if (flag === '--archive-prefix') values.archivePrefixes.push(value);
    else if (flag === '--exclude-prefix') values.excludePrefixes.push(value);
    else values[flag.slice(2).replace(/-([a-z])/g, (_, char) => char.toUpperCase())] = value;
  }
  return { command, values };
}

async function readJson(path) {
  return JSON.parse(await readFile(path, 'utf8'));
}

async function writeJson(path, value) {
  const target = resolve(path);
  const directory = dirname(target);
  await mkdir(directory, { recursive: true });
  let handle;
  try {
    handle = await open(target, 'wx', 0o600);
    await handle.writeFile(`${JSON.stringify(value, null, 2)}\n`);
    await handle.chmod(0o600);
    await handle.sync();
    await handle.close();
    handle = null;
    await syncDirectoryPath(directory);
  } catch (error) {
    await handle?.close().catch(() => {});
    if (error.code !== 'EEXIST') await rm(target, { force: true }).catch(() => {});
    throw error;
  }
}

function assertExpectedCounts(result, values) {
  if (values.expectSelected !== undefined && result.selectedCount !== Number(values.expectSelected)) {
    throw new Error(`selected count mismatch: expected ${values.expectSelected}, got ${result.selectedCount}`);
  }
  if (values.expectPreserved !== undefined && result.preservedCount !== Number(values.expectPreserved)) {
    throw new Error(`preserved count mismatch: expected ${values.expectPreserved}, got ${result.preservedCount}`);
  }
}

async function cli(argv) {
  const { command, values } = parseArgs(argv);
  if (values.execute && values.dryRun) throw new Error('--execute and --dry-run cannot be combined');
  if (!command || ['-h', '--help', 'help'].includes(command)) {
    process.stdout.write(`Usage:\n  patch-timeline.mjs inventory --root <repo> [--archive-prefix <path>] [--exclude-prefix <path>] [--expect-selected <count>] [--expect-preserved <count>]\n  patch-timeline.mjs audit-evidence --root <repo> [--archive-prefix <path>] [--exclude-prefix <path>] [--evidence-file <json>] [--expect-selected <count>] [--expect-preserved <count>]\n  patch-timeline.mjs plan --root <repo> [--archive-prefix <path>] [--exclude-prefix <path>] [--evidence-file <json>] [--expect-selected <count>] [--expect-preserved <count>] [--output <manifest>]\n  patch-timeline.mjs create --root <repo> --patch-dir <dir> --slug <slug> --title <title> --creation-evidence <source> --session <id> --target-design <ref> --full-history <ref> [--created-at <UTC-second>] [--execute --approve-manifest-sha256 <sha>]\n  patch-timeline.mjs apply --root <repo> --manifest <json> [--execute --approve-manifest-sha256 <sha> --journal <json>]\n  patch-timeline.mjs verify --root <repo> --manifest <json>\n  patch-timeline.mjs rollback --root <repo> --journal <json> [--execute --approve-journal-sha256 <sha>]\n`);
    return 0;
  }
  const evidenceByPath = values.evidenceFile ? await readJson(values.evidenceFile) : {};
  if (command === 'inventory' || command === 'audit-evidence') {
    const result = await inventoryPatches({ root: values.root, archivePrefixes: values.archivePrefixes, excludePrefixes: values.excludePrefixes, evidenceByPath });
    assertExpectedCounts(result, values);
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
    return command === 'audit-evidence' && result.files.some((row) => ['legacy-ambiguous', 'invalid'].includes(row.status)) ? 2 : 0;
  }
  if (command === 'plan') {
    const manifest = await buildManifest({ root: values.root, archivePrefixes: values.archivePrefixes, excludePrefixes: values.excludePrefixes, evidenceByPath });
    assertExpectedCounts(manifest, values);
    if (values.output) await writeJson(values.output, manifest);
    else process.stdout.write(`${JSON.stringify(manifest, null, 2)}\n`);
    return manifest.blockers.length ? 2 : 0;
  }
  if (command === 'create') {
    if (values.execute && !values.createdAt) throw new Error('--created-at from the approved preview is required for executed create');
    const result = await createPatch({
      root: values.root,
      patchDir: values.patchDir ?? 'patch',
      slug: values.slug,
      title: values.title,
      creationEvidence: values.creationEvidence,
      session: values.session,
      targetDesign: values.targetDesign,
      fullHistory: values.fullHistory,
      body: values.body ?? '',
      createdAt: values.createdAt ?? null,
      execute: values.execute ?? false,
      approvedManifestSha256: values.approveManifestSha256,
    });
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
    return 0;
  }
  if (command === 'apply') {
    if (!values.manifest) throw new Error('--manifest is required');
    if (values.execute && !values.journal) throw new Error('--journal is required for executed apply');
    const manifest = await readJson(values.manifest);
    const result = await applyManifest({
      root: values.root,
      manifest,
      execute: values.execute ?? false,
      approvedManifestSha256: values.approveManifestSha256,
      journalPath: values.journal,
    });
    const output = result.executed
      ? {
          executed: true,
          manifestSha256: result.manifestSha256,
          journalPath: resolve(values.journal),
          journalSha256: result.journal.journalSha256,
        }
      : result;
    process.stdout.write(`${JSON.stringify(output, null, 2)}\n`);
    return 0;
  }
  if (command === 'verify') {
    if (!values.manifest) throw new Error('--manifest is required');
    const result = await verifyManifest({ root: values.root, manifest: await readJson(values.manifest) });
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
    return result.ok ? 0 : 2;
  }
  if (command === 'rollback') {
    if (!values.journal) throw new Error('--journal is required');
    const journal = await readJson(values.journal);
    const result = await rollbackJournal({ root: values.root, journal, execute: values.execute ?? false, approvedJournalSha256: values.approveJournalSha256 });
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
    return 0;
  }
  throw new Error(`unknown command: ${command}`);
}

if (process.argv[1] && pathToFileURL(resolve(process.argv[1])).href === import.meta.url) {
  cli(process.argv.slice(2))
    .then((code) => { process.exitCode = code; })
    .catch((error) => {
      process.stderr.write(`patch-timeline: ${error.message}\n`);
      process.exitCode = 1;
    });
}
