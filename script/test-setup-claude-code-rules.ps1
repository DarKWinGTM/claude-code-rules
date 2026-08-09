[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceRepo = (Resolve-Path (Join-Path $ScriptDir '..')).Path
$Installer = Join-Path $ScriptDir 'setup-claude-code-rules.ps1'
$TempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ('claude-code-rules-fixture-' + [System.Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $TempRoot | Out-Null

$ActiveRuleFiles = @(
  'accurate-communication.md', 'action-safety.md', 'audience-surface-disclosure-control.md',
  'authority-and-scope.md', 'coding-discipline.md', 'communication-register.md',
  'document-governance.md', 'document-integrity.md', 'evidence-discipline.md',
  'execution-and-goal-frame.md', 'explanation-and-presentation.md', 'goal-authoring-and-route-support.md',
  'external-verification-and-source-trust.md', 'memory-governance-and-session-boundary.md',
  'phase-todo-artifact.md', 'portable-implementation-and-hardcoding-control.md',
  'refusal-and-recovery.md', 'safe-io.md', 'worker-routing-and-context.md'
)

$RetiredRuleCandidates = @(
  'anti-mockup.md', 'anti-sycophancy.md', 'context-load-and-document-density-control.md',
  'custom-agent-selection-priority.md', 'dan-safe-normalization.md', 'development-verification-and-debug-strategy.md',
  'document-changelog-control.md', 'document-consistency.md', 'document-design-control.md', 'document-patch-control.md',
  'emergency-protocol.md', 'evidence-grounded-burden-of-proof.md', 'execution-continuity-and-mode-selection.md',
  'explanation-quality.md', 'flow-diagram-no-frame.md', 'functional-intent-verification.md',
  'goal-set-review-and-priority-balance.md', 'governed-document-rollover-control.md', 'high-signal-communication.md',
  'maintainable-code-structure-and-decomposition.md', 'native-worker-agent-routing-and-context-control.md',
  'natural-professional-communication.md', 'no-variable-guessing.md', 'operational-failure-handling.md',
  'phase-implementation.md', 'project-documentation-standards.md', 'recovery-contract.md',
  'refusal-classification.md', 'refusal-minimization.md', 'response-closing-and-action-framing.md',
  'runtime-topology-control.md', 'safe-file-reading.md', 'safe-terminal-output.md', 'strict-file-hygiene.md',
  'tactical-strategic-programming.md', 'technical-snapshot-communication.md', 'todo-standards.md',
  'unified-version-control-system.md', 'zero-hallucination.md', 'answer-presentation.md', 'artifact-initiation-control.md'
)

function Fail([string]$Message) { throw "FAIL: $Message" }
function Assert-File([string]$PathValue) { if (-not (Test-Path -LiteralPath $PathValue -PathType Leaf)) { Fail "expected file: $PathValue" } }
function Assert-Absent([string]$PathValue) { if (Test-Path -LiteralPath $PathValue) { Fail "expected absent path: $PathValue" } }
function Assert-Equal($Expected, $Actual, [string]$Message) { if ($Expected -ne $Actual) { Fail "$Message (expected $Expected, got $Actual)" } }
function Assert-Link([string]$PathValue, [string]$Message) {
  $entry = Get-Item -LiteralPath $PathValue -Force -ErrorAction SilentlyContinue
  if (-not $entry -or (($entry.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -eq 0)) { Fail $Message }
}
function Get-Hash([string]$PathValue) { (Get-FileHash -LiteralPath $PathValue -Algorithm SHA256).Hash.ToLowerInvariant() }
function Get-Blob([string]$PathValue) { (@(git hash-object -- $PathValue))[0].Trim().ToLowerInvariant() }
function Write-Utf8NoBom([string]$PathValue, [string]$Content) { [System.IO.File]::WriteAllText($PathValue, $Content, [System.Text.UTF8Encoding]::new($false)) }

function Write-ManifestLine([string]$Manifest, [string]$File, [string]$Snapshot) {
  [System.IO.File]::AppendAllText($Manifest, "$File`t$(Get-Hash $Snapshot)`t$(Get-Blob $Snapshot)`n", [System.Text.UTF8Encoding]::new($false))
}

function Write-HistoricalFile([string]$File, [string]$Target) {
  $commit = $null
  foreach ($item in @(git -C $SourceRepo rev-list --all -- $File)) {
    git -C $SourceRepo cat-file -e ("{0}:{1}" -f $item, $File) 2>$null
    if ($LASTEXITCODE -eq 0) { $commit = $item; break }
  }
  if (-not $commit) { Fail "no historical blob found for $File" }
  $archive = Join-Path $TempRoot ('historical-' + [System.Guid]::NewGuid().ToString('N') + '.tar')
  $extract = Join-Path $TempRoot ('historical-' + [System.Guid]::NewGuid().ToString('N'))
  New-Item -ItemType Directory -Path $extract | Out-Null
  git -C $SourceRepo archive --format=tar --output=$archive $commit $File
  if ($LASTEXITCODE -ne 0) { Fail "unable to archive historical blob for $File" }
  tar -xf $archive -C $extract
  if ($LASTEXITCODE -ne 0) { Fail "unable to extract historical blob for $File" }
  Copy-Item -LiteralPath (Join-Path $extract $File) -Destination $Target
  Remove-Item -LiteralPath $archive -Force
  Remove-Item -LiteralPath $extract -Recurse -Force
}

function Verify-Payload([string]$Project, [string]$ExpectedSource) {
  $rulesDir = Join-Path $Project '.claude/rules'
  $manifest = Join-Path $rulesDir '.claude-code-rules-manifest.tsv'
  Assert-File $manifest
  $manifestFiles = @([System.IO.File]::ReadAllLines($manifest) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) } | ForEach-Object { ($_ -split "`t", 2)[0] })
  Assert-Equal $ActiveRuleFiles.Count $manifestFiles.Count 'manifest file count mismatch'
  for ($index = 0; $index -lt $ActiveRuleFiles.Count; $index++) {
    $file = $ActiveRuleFiles[$index]
    Assert-Equal $file $manifestFiles[$index] "manifest order mismatch at index $index"
    $installed = Join-Path $rulesDir $file
    Assert-File $installed
    Assert-Equal (Get-Hash (Join-Path $ExpectedSource $file)) (Get-Hash $installed) "payload mismatch for $file"
    if ((Get-Item -LiteralPath $installed).Length -le 500) { Fail "body-sufficiency check failed for $file" }
  }
}

function Get-TreeHash([string]$Root) {
  $builder = New-Object System.Text.StringBuilder
  foreach ($file in (Get-ChildItem -LiteralPath $Root -Recurse -File | Sort-Object FullName)) {
    [void]$builder.Append($file.FullName.Substring($Root.Length)).Append(':').Append((Get-Hash $file.FullName)).Append("`n")
  }
  $bytes = [System.Text.Encoding]::UTF8.GetBytes($builder.ToString())
  $sha = [System.Security.Cryptography.SHA256]::Create()
  try { return ([System.BitConverter]::ToString($sha.ComputeHash($bytes))).Replace('-', '').ToLowerInvariant() }
  finally { $sha.Dispose() }
}

try {
  $Project = Join-Path $TempRoot 'project'
  $RulesDir = Join-Path $Project '.claude/rules'
  $PriorDir = Join-Path $RulesDir '.claude-code-rules-legacy-backup/nested'
  New-Item -ItemType Directory -Path $PriorDir | Out-Null
  Write-Utf8NoBom (Join-Path $PriorDir 'former.md') "opaque prior quarantine`n"

  Write-HistoricalFile 'anti-mockup.md' (Join-Path $RulesDir 'anti-mockup.md')
  Write-Utf8NoBom (Join-Path $RulesDir 'obsolete-owned.md') "obsolete owned snapshot`n"
  $ModifiedOriginal = Join-Path $TempRoot 'modified-original.md'
  Write-Utf8NoBom $ModifiedOriginal "modified original snapshot`n"
  Copy-Item -LiteralPath $ModifiedOriginal -Destination (Join-Path $RulesDir 'modified-owned.md')
  [System.IO.File]::AppendAllText((Join-Path $RulesDir 'modified-owned.md'), "modified by another owner`n")
  Write-Utf8NoBom (Join-Path $RulesDir 'unmatched-sentinel.md') "unmatched same-name sentinel`n"
  Write-Utf8NoBom (Join-Path $RulesDir 'shared-task-list-path-coordination.md') "unrelated runtime rule`n"

  $UnrelatedHash = Get-Hash (Join-Path $RulesDir 'shared-task-list-path-coordination.md')
  $ModifiedHash = Get-Hash (Join-Path $RulesDir 'modified-owned.md')
  $UnmatchedHash = Get-Hash (Join-Path $RulesDir 'unmatched-sentinel.md')
  $Manifest = Join-Path $RulesDir '.claude-code-rules-manifest.tsv'
  Write-ManifestLine $Manifest 'obsolete-owned.md' (Join-Path $RulesDir 'obsolete-owned.md')
  Write-ManifestLine $Manifest 'modified-owned.md' $ModifiedOriginal

  & $Installer -ProjectRoot $Project -SourceRepo $SourceRepo | Out-Null
  Verify-Payload $Project $SourceRepo

  $QuarantineRoot = Join-Path $Project '.claude/quarantine/claude-code-rules'
  $QuarantineRuns = @(Get-ChildItem -LiteralPath $QuarantineRoot -Directory)
  Assert-Equal 1 $QuarantineRuns.Count 'expected one quarantine run'
  $QuarantineRun = $QuarantineRuns[0].FullName
  Assert-File (Join-Path $QuarantineRun 'anti-mockup.md')
  Assert-File (Join-Path $QuarantineRun 'obsolete-owned.md')
  Assert-File (Join-Path $QuarantineRun 'prior-in-tree-quarantine/nested/former.md')
  Assert-Absent (Join-Path $RulesDir 'anti-mockup.md')
  Assert-Absent (Join-Path $RulesDir 'obsolete-owned.md')
  Assert-Absent (Join-Path $RulesDir '.claude-code-rules-legacy-backup')
  Assert-Equal $ModifiedHash (Get-Hash (Join-Path $RulesDir 'modified-owned.md')) 'modified manifest-owned file changed'
  Assert-Equal $UnmatchedHash (Get-Hash (Join-Path $RulesDir 'unmatched-sentinel.md')) 'unmatched file changed'
  Assert-Equal $UnrelatedHash (Get-Hash (Join-Path $RulesDir 'shared-task-list-path-coordination.md')) 'unrelated file changed'
  foreach ($file in $RetiredRuleCandidates) { Assert-Absent (Join-Path $RulesDir $file) }

  Write-Utf8NoBom (Join-Path $QuarantineRun 'poison.md') "poison that must never be read`n"
  $QuarantineHash = Get-TreeHash $QuarantineRoot
  $OfflineQuarantine = Join-Path $Project '.claude/quarantine/claude-code-rules-offline'
  Move-Item -LiteralPath $QuarantineRoot -Destination $OfflineQuarantine

  & $Installer -ProjectRoot $Project -SourceRepo $SourceRepo | Out-Null
  Verify-Payload $Project $SourceRepo
  Assert-Absent $QuarantineRoot
  Assert-Equal $QuarantineHash (Get-TreeHash $OfflineQuarantine) 'offline quarantine changed during reinstall'
  Assert-Equal $UnrelatedHash (Get-Hash (Join-Path $RulesDir 'shared-task-list-path-coordination.md')) 'unrelated file changed on rerun'

  & $Installer -ProjectRoot $Project -SourceRepo $SourceRepo | Out-Null
  Verify-Payload $Project $SourceRepo
  Assert-Absent $QuarantineRoot

  $KnownGood = Join-Path $TempRoot 'known-good-v10.57'
  git clone --quiet --no-local $SourceRepo $KnownGood
  if ($LASTEXITCODE -ne 0) { Fail 'unable to clone known-good fixture source' }
  git -C $KnownGood checkout --quiet v10.57
  if ($LASTEXITCODE -ne 0) { Fail 'unable to checkout v10.57 fixture source' }
  & $Installer -ProjectRoot $Project -SourceRepo $KnownGood | Out-Null
  Verify-Payload $Project $KnownGood
  Assert-Absent $QuarantineRoot
  Assert-Equal $QuarantineHash (Get-TreeHash $OfflineQuarantine) 'controlled restoration touched quarantine'
  Assert-Equal $UnrelatedHash (Get-Hash (Join-Path $RulesDir 'shared-task-list-path-coordination.md')) 'controlled restoration changed unrelated file'

  $TraversalProject = Join-Path $TempRoot 'traversal-project'
  $TraversalRules = Join-Path $TraversalProject '.claude/rules'
  New-Item -ItemType Directory -Path $TraversalRules | Out-Null
  Write-Utf8NoBom (Join-Path $TraversalProject 'escape.md') "escape sentinel`n"
  $Escape = Join-Path $TraversalProject 'escape.md'
  Write-Utf8NoBom (Join-Path $TraversalRules '.claude-code-rules-manifest.tsv') "../../escape.md`t$(Get-Hash $Escape)`t$(Get-Blob $Escape)`n"
  $TraversalFailed = $false
  try { & $Installer -ProjectRoot $TraversalProject -SourceRepo $SourceRepo | Out-Null }
  catch { $TraversalFailed = $true }
  if (-not $TraversalFailed) { Fail 'path-traversal manifest unexpectedly succeeded' }
  Assert-File $Escape
  Assert-Absent (Join-Path $TraversalRules 'accurate-communication.md')

  $CollisionProject = Join-Path $TempRoot 'collision-project'
  $CollisionRules = Join-Path $CollisionProject '.claude/rules'
  New-Item -ItemType Directory -Path $CollisionRules | Out-Null
  $CollisionFile = Join-Path $CollisionRules 'accurate-communication.md'
  Write-Utf8NoBom $CollisionFile "other-owner active-name collision`n"
  $CollisionHash = Get-Hash $CollisionFile
  $CollisionFailed = $false
  try { & $Installer -ProjectRoot $CollisionProject -SourceRepo $SourceRepo | Out-Null }
  catch { $CollisionFailed = $true }
  if (-not $CollisionFailed) { Fail 'unowned active-name collision unexpectedly succeeded' }
  Assert-Equal $CollisionHash (Get-Hash $CollisionFile) 'active-name collision was overwritten'
  Assert-Absent (Join-Path $CollisionRules '.claude-code-rules-manifest.tsv')

  $DuplicateActiveProject = Join-Path $TempRoot 'duplicate-active-project'
  $DuplicateActiveRules = Join-Path $DuplicateActiveProject '.claude/rules'
  New-Item -ItemType Directory -Path $DuplicateActiveRules | Out-Null
  $DuplicateActiveManifest = Join-Path $DuplicateActiveRules '.claude-code-rules-manifest.tsv'
  $DuplicateActiveText = "accurate-communication.md`t$(Get-Hash (Join-Path $SourceRepo 'accurate-communication.md'))`t$(Get-Blob (Join-Path $SourceRepo 'accurate-communication.md'))`n"
  $DuplicateActiveText += "accurate-communication.md`t$(Get-Hash (Join-Path $SourceRepo 'action-safety.md'))`t$(Get-Blob (Join-Path $SourceRepo 'action-safety.md'))`n"
  Write-Utf8NoBom $DuplicateActiveManifest $DuplicateActiveText
  $DuplicateActiveFailed = $false
  try { & $Installer -ProjectRoot $DuplicateActiveProject -SourceRepo $SourceRepo | Out-Null }
  catch { $DuplicateActiveFailed = $true }
  if (-not $DuplicateActiveFailed) { Fail 'duplicate active manifest record unexpectedly succeeded' }
  Assert-Absent (Join-Path $DuplicateActiveRules 'accurate-communication.md')

  $DuplicateObsoleteProject = Join-Path $TempRoot 'duplicate-obsolete-project'
  $DuplicateObsoleteRules = Join-Path $DuplicateObsoleteProject '.claude/rules'
  New-Item -ItemType Directory -Path $DuplicateObsoleteRules | Out-Null
  $DuplicateObsoleteFile = Join-Path $DuplicateObsoleteRules 'obsolete-owned.md'
  Write-Utf8NoBom $DuplicateObsoleteFile "duplicate obsolete sentinel`n"
  $DuplicateObsoleteHash = Get-Hash $DuplicateObsoleteFile
  $DuplicateObsoleteManifest = Join-Path $DuplicateObsoleteRules '.claude-code-rules-manifest.tsv'
  Write-ManifestLine $DuplicateObsoleteManifest 'obsolete-owned.md' $DuplicateObsoleteFile
  Write-ManifestLine $DuplicateObsoleteManifest 'obsolete-owned.md' $DuplicateObsoleteFile
  $DuplicateObsoleteFailed = $false
  try { & $Installer -ProjectRoot $DuplicateObsoleteProject -SourceRepo $SourceRepo | Out-Null }
  catch { $DuplicateObsoleteFailed = $true }
  if (-not $DuplicateObsoleteFailed) { Fail 'duplicate obsolete manifest record unexpectedly succeeded' }
  Assert-Equal $DuplicateObsoleteHash (Get-Hash $DuplicateObsoleteFile) 'duplicate obsolete preflight mutated target'
  Assert-Absent (Join-Path $DuplicateObsoleteProject '.claude/quarantine/claude-code-rules')

  $ManifestLinkProject = Join-Path $TempRoot 'manifest-link-project'
  $ManifestLinkRules = Join-Path $ManifestLinkProject '.claude/rules'
  New-Item -ItemType Directory -Path $ManifestLinkRules | Out-Null
  $ExternalManifest = Join-Path $TempRoot 'external-manifest.tsv'
  Write-Utf8NoBom $ExternalManifest "external manifest sentinel`n"
  $ExternalManifestHash = Get-Hash $ExternalManifest
  $ManifestLink = Join-Path $ManifestLinkRules '.claude-code-rules-manifest.tsv'
  New-Item -ItemType SymbolicLink -Path $ManifestLink -Target $ExternalManifest | Out-Null
  $ManifestLinkFailed = $false
  try { & $Installer -ProjectRoot $ManifestLinkProject -SourceRepo $SourceRepo | Out-Null }
  catch { $ManifestLinkFailed = $true }
  if (-not $ManifestLinkFailed) { Fail 'manifest symlink unexpectedly succeeded' }
  Assert-Link $ManifestLink 'manifest symlink was replaced'
  Assert-Equal $ExternalManifestHash (Get-Hash $ExternalManifest) 'manifest symlink target was modified'
  Assert-Absent (Join-Path $ManifestLinkRules 'accurate-communication.md')

  $BrokenManifestProject = Join-Path $TempRoot 'broken-manifest-link-project'
  $BrokenManifestRules = Join-Path $BrokenManifestProject '.claude/rules'
  New-Item -ItemType Directory -Path $BrokenManifestRules | Out-Null
  $BrokenManifestLink = Join-Path $BrokenManifestRules '.claude-code-rules-manifest.tsv'
  New-Item -ItemType SymbolicLink -Path $BrokenManifestLink -Target (Join-Path $TempRoot 'missing-manifest.tsv') | Out-Null
  $BrokenManifestFailed = $false
  try { & $Installer -ProjectRoot $BrokenManifestProject -SourceRepo $SourceRepo | Out-Null }
  catch { $BrokenManifestFailed = $true }
  if (-not $BrokenManifestFailed) { Fail 'broken manifest symlink unexpectedly succeeded' }
  Assert-Link $BrokenManifestLink 'broken manifest symlink was replaced'

  $ActiveLinkProject = Join-Path $TempRoot 'active-link-project'
  $ActiveLinkRules = Join-Path $ActiveLinkProject '.claude/rules'
  New-Item -ItemType Directory -Path $ActiveLinkRules | Out-Null
  $ExternalActive = Join-Path $TempRoot 'external-active.md'
  Write-Utf8NoBom $ExternalActive "external active target sentinel`n"
  $ExternalActiveHash = Get-Hash $ExternalActive
  $ActiveLink = Join-Path $ActiveLinkRules 'accurate-communication.md'
  New-Item -ItemType SymbolicLink -Path $ActiveLink -Target $ExternalActive | Out-Null
  $ActiveLinkFailed = $false
  try { & $Installer -ProjectRoot $ActiveLinkProject -SourceRepo $SourceRepo | Out-Null }
  catch { $ActiveLinkFailed = $true }
  if (-not $ActiveLinkFailed) { Fail 'active-target symlink unexpectedly succeeded' }
  Assert-Link $ActiveLink 'active-target symlink was replaced'
  Assert-Equal $ExternalActiveHash (Get-Hash $ExternalActive) 'active-target symlink destination was modified'

  $BrokenActiveProject = Join-Path $TempRoot 'broken-active-link-project'
  $BrokenActiveRules = Join-Path $BrokenActiveProject '.claude/rules'
  New-Item -ItemType Directory -Path $BrokenActiveRules | Out-Null
  $BrokenActiveLink = Join-Path $BrokenActiveRules 'accurate-communication.md'
  New-Item -ItemType SymbolicLink -Path $BrokenActiveLink -Target (Join-Path $TempRoot 'missing-active.md') | Out-Null
  $BrokenActiveFailed = $false
  try { & $Installer -ProjectRoot $BrokenActiveProject -SourceRepo $SourceRepo | Out-Null }
  catch { $BrokenActiveFailed = $true }
  if (-not $BrokenActiveFailed) { Fail 'broken active-target symlink unexpectedly succeeded' }
  Assert-Link $BrokenActiveLink 'broken active-target symlink was replaced'

  $PreflightProject = Join-Path $TempRoot 'preflight-project'
  $PreflightRules = Join-Path $PreflightProject '.claude/rules'
  $PreflightPrior = Join-Path $PreflightRules '.claude-code-rules-legacy-backup/nested'
  New-Item -ItemType Directory -Path $PreflightPrior | Out-Null
  Write-Utf8NoBom (Join-Path $PreflightPrior 'former.md') "opaque preflight quarantine`n"
  New-Item -ItemType Directory -Path (Join-Path $PreflightRules 'obsolete-directory') | Out-Null
  $ZeroSha = '0' * 64
  $ZeroBlob = '0' * 40
  Write-Utf8NoBom (Join-Path $PreflightRules '.claude-code-rules-manifest.tsv') "obsolete-directory`t$ZeroSha`t$ZeroBlob`n"
  $PreflightHash = Get-TreeHash $PreflightProject
  $PreflightFailed = $false
  try { & $Installer -ProjectRoot $PreflightProject -SourceRepo $SourceRepo | Out-Null }
  catch { $PreflightFailed = $true }
  if (-not $PreflightFailed) { Fail 'invalid later manifest target unexpectedly succeeded' }
  Assert-Equal $PreflightHash (Get-TreeHash $PreflightProject) 'failed deterministic preflight mutated project tree'
  Assert-Absent (Join-Path $PreflightProject '.claude/quarantine/claude-code-rules')

  $ClaudeLinkProject = Join-Path $TempRoot 'claude-link-project'
  $ClaudeLinkExternal = Join-Path $TempRoot 'claude-link-external'
  New-Item -ItemType Directory -Path $ClaudeLinkProject | Out-Null
  New-Item -ItemType Directory -Path (Join-Path $ClaudeLinkExternal 'rules') | Out-Null
  Write-Utf8NoBom (Join-Path $ClaudeLinkExternal 'sentinel.md') "external claude sentinel`n"
  $ClaudeLinkHash = Get-TreeHash $ClaudeLinkExternal
  New-Item -ItemType SymbolicLink -Path (Join-Path $ClaudeLinkProject '.claude') -Target $ClaudeLinkExternal | Out-Null
  $ClaudeLinkFailed = $false
  try { & $Installer -ProjectRoot $ClaudeLinkProject -SourceRepo $SourceRepo | Out-Null }
  catch { $ClaudeLinkFailed = $true }
  if (-not $ClaudeLinkFailed) { Fail 'symlinked .claude ancestor unexpectedly succeeded' }
  Assert-Link (Join-Path $ClaudeLinkProject '.claude') 'symlinked .claude ancestor was replaced'
  Assert-Equal $ClaudeLinkHash (Get-TreeHash $ClaudeLinkExternal) 'symlinked .claude ancestor mutated external tree'

  $RulesLinkProject = Join-Path $TempRoot 'rules-link-project'
  $RulesLinkExternal = Join-Path $TempRoot 'rules-link-external'
  New-Item -ItemType Directory -Path (Join-Path $RulesLinkProject '.claude') | Out-Null
  New-Item -ItemType Directory -Path $RulesLinkExternal | Out-Null
  Write-Utf8NoBom (Join-Path $RulesLinkExternal 'sentinel.md') "external rules sentinel`n"
  $RulesLinkHash = Get-TreeHash $RulesLinkExternal
  New-Item -ItemType SymbolicLink -Path (Join-Path $RulesLinkProject '.claude/rules') -Target $RulesLinkExternal | Out-Null
  $RulesLinkFailed = $false
  try { & $Installer -ProjectRoot $RulesLinkProject -SourceRepo $SourceRepo | Out-Null }
  catch { $RulesLinkFailed = $true }
  if (-not $RulesLinkFailed) { Fail 'symlinked rules directory unexpectedly succeeded' }
  Assert-Link (Join-Path $RulesLinkProject '.claude/rules') 'symlinked rules directory was replaced'
  Assert-Equal $RulesLinkHash (Get-TreeHash $RulesLinkExternal) 'symlinked rules directory mutated external tree'

  $QuarantineParentProject = Join-Path $TempRoot 'quarantine-parent-link-project'
  $QuarantineParentRules = Join-Path $QuarantineParentProject '.claude/rules'
  $QuarantineParentExternal = Join-Path $TempRoot 'quarantine-parent-external'
  New-Item -ItemType Directory -Path $QuarantineParentRules | Out-Null
  New-Item -ItemType Directory -Path $QuarantineParentExternal | Out-Null
  Write-HistoricalFile 'anti-mockup.md' (Join-Path $QuarantineParentRules 'anti-mockup.md')
  Write-Utf8NoBom (Join-Path $QuarantineParentExternal 'sentinel.md') "external quarantine parent sentinel`n"
  $QuarantineParentHash = Get-TreeHash $QuarantineParentExternal
  New-Item -ItemType SymbolicLink -Path (Join-Path $QuarantineParentProject '.claude/quarantine') -Target $QuarantineParentExternal | Out-Null
  $QuarantineParentFailed = $false
  try { & $Installer -ProjectRoot $QuarantineParentProject -SourceRepo $SourceRepo | Out-Null }
  catch { $QuarantineParentFailed = $true }
  if (-not $QuarantineParentFailed) { Fail 'symlinked quarantine parent unexpectedly succeeded' }
  Assert-File (Join-Path $QuarantineParentRules 'anti-mockup.md')
  Assert-Equal $QuarantineParentHash (Get-TreeHash $QuarantineParentExternal) 'symlinked quarantine parent mutated external tree'

  $QuarantineRootProject = Join-Path $TempRoot 'quarantine-root-link-project'
  $QuarantineRootRules = Join-Path $QuarantineRootProject '.claude/rules'
  $QuarantineRootParent = Join-Path $QuarantineRootProject '.claude/quarantine'
  $QuarantineRootExternal = Join-Path $TempRoot 'quarantine-root-external'
  New-Item -ItemType Directory -Path $QuarantineRootRules | Out-Null
  New-Item -ItemType Directory -Path $QuarantineRootParent | Out-Null
  New-Item -ItemType Directory -Path $QuarantineRootExternal | Out-Null
  Write-HistoricalFile 'anti-mockup.md' (Join-Path $QuarantineRootRules 'anti-mockup.md')
  Write-Utf8NoBom (Join-Path $QuarantineRootExternal 'sentinel.md') "external quarantine root sentinel`n"
  $QuarantineRootHash = Get-TreeHash $QuarantineRootExternal
  New-Item -ItemType SymbolicLink -Path (Join-Path $QuarantineRootParent 'claude-code-rules') -Target $QuarantineRootExternal | Out-Null
  $QuarantineRootFailed = $false
  try { & $Installer -ProjectRoot $QuarantineRootProject -SourceRepo $SourceRepo | Out-Null }
  catch { $QuarantineRootFailed = $true }
  if (-not $QuarantineRootFailed) { Fail 'symlinked quarantine root unexpectedly succeeded' }
  Assert-File (Join-Path $QuarantineRootRules 'anti-mockup.md')
  Assert-Equal $QuarantineRootHash (Get-TreeHash $QuarantineRootExternal) 'symlinked quarantine root mutated external tree'

  Write-Host 'PowerShell installer fixtures: PASS'
}
finally {
  if (Test-Path -LiteralPath $TempRoot) { Remove-Item -LiteralPath $TempRoot -Recurse -Force -ErrorAction SilentlyContinue }
}
