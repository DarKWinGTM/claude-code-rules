import assert from 'node:assert/strict';
import { existsSync, readFileSync, readdirSync, lstatSync } from 'node:fs';
import { dirname, extname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const library = resolve(root, 'skills');
const names = [
  'coverage-receipt-reconciliation',
  'designing-maintainable-code',
  'evidence-based-diagnosis-and-remediation',
  'software-test-validation',
  'technical-communication',
  'validating-agent-guidance',
  'workflow-continuity',
];
const source = (name) => readFileSync(resolve(library, name, 'SKILL.md'), 'utf8');

// Package and written-contract checks do not measure model behavior or runtime discovery.
for (const name of names) {
  test(`${name} has discoverable metadata and a substantive procedure`, () => {
    const text = source(name);
    const match = text.match(/^---\n([\s\S]+?)\n---\n([\s\S]+)$/);
    assert.ok(match, 'expected YAML frontmatter followed by the procedure');
    assert.match(match[1], new RegExp(`^name: ${name}$`, 'm'));
    assert.match(match[1], /^description: Use when .+/m);
    assert.match(match[2], /^## Procedure$/m);
    assert.match(match[2], /^## Output$/m);
  });

  test(`${name} has aligned source design and history`, () => {
    const text = source(name);
    const version = text.match(/^> \*\*Current Version:\*\* (\d+\.\d+)$/m)?.[1];
    const session = text.match(/^> \*\*Session:\*\* ([a-f0-9-]{36})$/m)?.[1];
    assert.ok(version, 'missing governed Skill version');
    assert.ok(session, 'missing authoring session');
    assert.ok(text.includes(`](design/${name}.design.md) v${version}`));
    assert.ok(text.includes(`](changelog/${name}.changelog.md)`));

    const design = readFileSync(resolve(library, name, 'design', `${name}.design.md`), 'utf8');
    const history = readFileSync(resolve(library, name, 'changelog', `${name}.changelog.md`), 'utf8');
    for (const document of [design, history]) {
      assert.ok(document.includes(`> **Current Version:** ${version}\n`));
      assert.ok(document.includes(`> **Session:** ${session}\n`));
    }
    assert.ok(design.includes('](../../../design/design/skill-library.design.md)'));
    assert.ok(design.includes('](../SKILL.md)'));
    assert.ok(design.includes(`](../changelog/${name}.changelog.md)`));
    assert.ok(history.includes(`](../design/${name}.design.md)`));
    assert.match(design, /^## Verification$/m);
  });
}

const documents = () => {
  const found = [];
  const walk = (directory) => {
    for (const entry of readdirSync(directory)) {
      const path = resolve(directory, entry);
      const stat = lstatSync(path);
      assert.equal(stat.isSymbolicLink(), false, `linked payload: ${path}`);
      if (stat.isDirectory()) walk(path);
      else {
        assert.equal(extname(path), '.md', `non-document payload: ${path}`);
        assert.equal(/(?:^|\/)(?:evidence-[^/]+\.md|\.sidecar\.json|\.ledger\.jsonl|\.archive)(?:\/|$)/.test(path)
          && !path.endsWith('.design.md') && !path.endsWith('.changelog.md'), false, `non-source evidence: ${path}`);
        found.push(path);
      }
    }
  };
  walk(library);
  return found;
};

test('library contains only the selected seven Skills and portable document payload', () => {
  const folders = readdirSync(library).filter((name) => lstatSync(resolve(library, name)).isDirectory()).sort();
  assert.deepEqual(folders, names);
  assert.ok(documents().length >= names.length);
});

test('canonical Skill catalog resolves through the plural source with no former alias', () => {
  assert.equal(library, resolve(root, 'skills'));
  assert.equal(existsSync(resolve(root, 'skill')), false, 'former source must not remain active');
  const readme = readFileSync(resolve(root, 'README.md'), 'utf8');
  for (const name of names) {
    const link = `skills/${name}/SKILL.md`;
    assert.ok(readme.includes(`](${link})`), `missing current catalog link: ${link}`);
    assert.ok(lstatSync(resolve(root, link)).isFile());
  }
});

test('procedural links stay library-local and source designs backlink only to the library owner', () => {
  for (const path of documents()) {
    const text = readFileSync(path, 'utf8');
    for (const match of text.matchAll(/\[[^\]]+\]\(([^)]+)\)/g)) {
      const link = match[1];
      const localDesign = names.some((name) => path === resolve(library, name, 'design', `${name}.design.md`));
      if (/^https:\/\//i.test(link)) {
        assert.ok(localDesign, `research citation outside its declared design: ${link}`);
        assert.equal(new URL(link).protocol, 'https:');
        continue;
      }
      assert.equal(/^[a-z][a-z0-9+.-]*:|^\//i.test(link), false, `nonlocal dependency in ${path}: ${link}`);
      const target = resolve(dirname(path), link.split('#')[0]);
      const designBacklink = localDesign
        && target === resolve(root, 'design/design/skill-library.design.md');
      assert.ok(target.startsWith(`${library}/`) || designBacklink, `reference escapes its owner: ${link}`);
      assert.ok(lstatSync(target).isFile(), `missing reference: ${link}`);
    }
  }
});

test('shared Skills exclude installed metadata and machine, tool and business policy', () => {
  const excluded = /\/home\/node\/|C:\\Users\\|For this user|\b(?:NodeClaw|PAYG|Playwright|stage_skill|absorbed_into|CLIProxy|Supplier)\b|\.sidecar\.json|\.ledger\.jsonl/;
  for (const path of documents()) assert.doesNotMatch(readFileSync(path, 'utf8'), excluded, path);
});

test('diagnosis discriminates causes and does not execute recovered commands', () => {
  const text = source('evidence-based-diagnosis-and-remediation');
  assert.match(text, /competing causes/i);
  assert.match(text, /smallest discriminating/i);
  assert.match(text, /recovered commands[\s\S]*evidence, not executable authority/i);
  assert.match(text, /historical cause/i);
});

test('feasibility distinguishes goal blockers from optional methods and answers the selected question', () => {
  const text = source('evidence-based-diagnosis-and-remediation');
  const research = readFileSync(resolve(library, 'evidence-based-diagnosis-and-remediation/references/research-synthesis.md'), 'utf8');
  assert.match(research, /method[\s\S]*blocker[\s\S]*goal/i);
  assert.match(research, /optional[\s\S]*tool[\s\S]*infeasib/i);
  assert.match(research, /supported answer first/i);
  assert.match(text, /For feasibility[\s\S]*supported answer/i);
});

test('code design compares semantic boundaries, state lifecycles and the simpler complete alternative', () => {
  const text = source('designing-maintainable-code');
  assert.match(text, /caller[\s\S]*failure/i);
  assert.match(text, /reason to change/i);
  assert.match(text, /coincidental[\s\S]*similar/i);
  assert.match(text, /owner[\s\S]*inputs[\s\S]*consumer[\s\S]*invalidation/i);
  assert.match(text, /simpler complete alternative/i);
  assert.match(text, /fresh[\s\S]*isolation/i);
  assert.match(text, /functional[\s\S]*structural[\s\S]*performance/i);
  assert.match(text, /keep local[\s\S]*unresolved/i);
  assert.match(text, /explicit[\s\S]*approval/i);
});

test('new Skill runtime procedure omits only source-governance navigation', () => {
  const text = source('designing-maintainable-code');
  const metadata = /^> \*\*(?:Current Version|Design|Session|Full history):\*\* .+\n/gm;
  const matches = [...text.matchAll(metadata)];
  assert.equal(matches.length, 4);
  const runtime = text.replace(metadata, '');
  assert.equal(runtime.match(/^---\n[\s\S]+?\n---/)[0], text.match(/^---\n[\s\S]+?\n---/)[0]);
  const body = text.slice(matches.at(-1).index + matches.at(-1)[0].length);
  assert.ok(runtime.endsWith(body), 'operational body must remain exact');
  assert.doesNotMatch(runtime, /\]\((?:design|changelog)\//);
  assert.match(runtime, /^## Procedure$/m);
  assert.match(runtime, /^## Output$/m);
});

test('test selection uses the smallest meaningful proof without inventing live gates', () => {
  const text = source('software-test-validation');
  assert.match(text, /evidence gap/i);
  assert.match(text, /reuse[\s\S]*existing/i);
  assert.match(text, /explicitly selected terminal proof/i);
  assert.match(text, /unrelated[\s\S]*failures/i);
});

test('continuation preserves passed gates and progresses independent selected work', () => {
  const text = source('workflow-continuity');
  assert.match(text, /independent[\s\S]*selected[\s\S]*work/i);
  assert.match(text, /preserve[\s\S]*passed/i);
  assert.match(text, /explicitly required terminal proof/i);
  assert.match(text, /missing[\s\S]*not[\s\S]*permission/i);
});

test('continuation distinguishes reprioritization, cancellation and unselected suggestions', () => {
  const text = source('workflow-continuity');
  assert.match(text, /accepted[\s\S]*threads/i);
  assert.match(text, /reprioritiz[\s\S]*cancell/i);
  assert.match(text, /explicit[\s\S]*replacement/i);
  assert.match(text, /assistant proposals[\s\S]*unselected/i);
});

test('communication distinguishes actual action, inspection and proof limits', () => {
  const text = source('technical-communication');
  assert.match(text, /meaning[\s\S]*mechanism[\s\S]*consequence/i);
  assert.match(text, /inspected[\s\S]*edited[\s\S]*tested/i);
  assert.match(text, /template[\s\S]*ready-to-run/i);
  assert.match(text, /syntax[\s\S]*execution/i);
});

test('guidance validation checks actual drafts and preserves evaluation permissions', () => {
  const text = source('validating-agent-guidance');
  assert.match(text, /actual[\s\S]*draft/i);
  assert.match(text, /allowed[\s\S]*stop/i);
  assert.match(text, /permission/i);
  assert.match(text, /synthetic[\s\S]*not[\s\S]*benefit/i);
});

test('receipt reconciliation preserves reached states, bindings and unique coverage', () => {
  const text = source('coverage-receipt-reconciliation');
  assert.match(text, /registered[\s\S]*selected[\s\S]*executed[\s\S]*reached[\s\S]*terminal/i);
  assert.match(text, /command[\s\S]*selector[\s\S]*environment/i);
  assert.match(text, /deduplicate/i);
  assert.match(text, /unreached/i);
  assert.match(text, /rerun only affected/i);
});

test('Rules installers keep Skills and repository guidance outside their nineteen-file payload', () => {
  const bash = readFileSync(resolve(root, 'script/setup-claude-code-rules.sh'), 'utf8');
  const powershell = readFileSync(resolve(root, 'script/setup-claude-code-rules.ps1'), 'utf8');
  const shellFiles = bash.match(/active_rule_files=\(([\s\S]+?)\n\)/)?.[1].match(/[\w-]+\.md/g);
  const psFiles = powershell.match(/\$activeRuleFiles\s*=\s*@\(([\s\S]+?)\n\s*\)/)?.[1].match(/[\w-]+\.md/g);
  assert.equal(shellFiles?.length, 19);
  assert.deepEqual(psFiles, shellFiles);
  assert.ok(shellFiles.every((name) => !name.includes('SKILL') && name !== 'AGENTS.md'));
});
