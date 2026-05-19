[CmdletBinding()]
param(
  [string]$ProjectRoot = (Get-Location).Path,
  [string]$SourceRepo,
  [string]$RepoUrl = "https://github.com/DarKWinGTM/claude-code-rules.git",
  [string]$Ref = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Resolve-ExistingDirectory([string]$PathValue, [string]$Label) {
  if (-not (Test-Path -LiteralPath $PathValue -PathType Container)) {
    throw "$Label does not exist: $PathValue"
  }
  return (Resolve-Path -LiteralPath $PathValue).Path
}

$ProjectRoot = Resolve-ExistingDirectory $ProjectRoot 'Project root'

$clonedRepoDir = $null
$legacyBackupRunDir = $null

function Cleanup-TemporaryClone {
  if ($script:clonedRepoDir -and (Test-Path -LiteralPath $script:clonedRepoDir)) {
    Remove-Item -LiteralPath $script:clonedRepoDir -Recurse -Force -ErrorAction SilentlyContinue
  }
}

try {
  if (-not [string]::IsNullOrWhiteSpace($SourceRepo)) {
    $SourceRepo = Resolve-ExistingDirectory $SourceRepo 'Source repo'
  } else {
    $candidateRepo = $null
    if ($PSScriptRoot) {
      $candidateRepo = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..") -ErrorAction SilentlyContinue
      if ($candidateRepo) {
        $candidateRepo = $candidateRepo.Path
      }
    }

    if ($candidateRepo -and (Test-Path -LiteralPath (Join-Path $candidateRepo 'README.md')) -and (Test-Path -LiteralPath (Join-Path $candidateRepo 'accurate-communication.md'))) {
      $SourceRepo = $candidateRepo
    } else {
      $script:clonedRepoDir = Join-Path ([System.IO.Path]::GetTempPath()) ("claude-code-rules-" + [System.Guid]::NewGuid().ToString('N'))
      git clone $RepoUrl (Join-Path $script:clonedRepoDir 'claude-code-rules') | Out-Null
      $SourceRepo = Join-Path $script:clonedRepoDir 'claude-code-rules'
      if (-not [string]::IsNullOrWhiteSpace($Ref)) {
        git -C $SourceRepo checkout $Ref | Out-Null
      }
    }
  }

  if (-not (Test-Path -LiteralPath (Join-Path $SourceRepo 'README.md')) -or -not (Test-Path -LiteralPath (Join-Path $SourceRepo 'accurate-communication.md'))) {
    throw "Source repo does not look like claude-code-rules: $SourceRepo"
  }

  $rulesDir = Join-Path $ProjectRoot '.claude/rules'
  New-Item -ItemType Directory -Force -Path $rulesDir | Out-Null

  $manifestPath = Join-Path $rulesDir '.claude-code-rules-manifest.tsv'
  $legacyBackupRoot = Join-Path $rulesDir '.claude-code-rules-legacy-backup'

  $activeRuleFiles = @(
    'accurate-communication.md',
    'action-safety.md',
    'audience-surface-disclosure-control.md',
    'authority-and-scope.md',
    'coding-discipline.md',
    'communication-register.md',
    'document-governance.md',
    'document-integrity.md',
    'evidence-discipline.md',
    'execution-and-goal-frame.md',
    'explanation-and-presentation.md',
    'external-verification-and-source-trust.md',
    'memory-governance-and-session-boundary.md',
    'phase-todo-artifact.md',
    'portable-implementation-and-hardcoding-control.md',
    'refusal-and-recovery.md',
    'safe-io.md',
    'worker-routing-and-context.md'
  )

  $legacyCandidateFiles = @(
    'anti-mockup.md',
    'anti-sycophancy.md',
    'context-load-and-document-density-control.md',
    'custom-agent-selection-priority.md',
    'dan-safe-normalization.md',
    'development-verification-and-debug-strategy.md',
    'document-changelog-control.md',
    'document-consistency.md',
    'document-design-control.md',
    'document-patch-control.md',
    'emergency-protocol.md',
    'evidence-grounded-burden-of-proof.md',
    'execution-continuity-and-mode-selection.md',
    'explanation-quality.md',
    'flow-diagram-no-frame.md',
    'functional-intent-verification.md',
    'goal-set-review-and-priority-balance.md',
    'governed-document-rollover-control.md',
    'high-signal-communication.md',
    'maintainable-code-structure-and-decomposition.md',
    'native-worker-agent-routing-and-context-control.md',
    'natural-professional-communication.md',
    'no-variable-guessing.md',
    'operational-failure-handling.md',
    'phase-implementation.md',
    'project-documentation-standards.md',
    'recovery-contract.md',
    'refusal-classification.md',
    'refusal-minimization.md',
    'response-closing-and-action-framing.md',
    'runtime-topology-control.md',
    'safe-file-reading.md',
    'safe-terminal-output.md',
    'strict-file-hygiene.md',
    'tactical-strategic-programming.md',
    'technical-snapshot-communication.md',
    'todo-standards.md',
    'unified-version-control-system.md',
    'zero-hallucination.md',
    'answer-presentation.md',
    'artifact-initiation-control.md'
  )

  function Get-RuleHash([string]$PathValue) {
    (Get-FileHash -LiteralPath $PathValue -Algorithm SHA256).Hash.ToLowerInvariant()
  }

  function Get-GitBlobHash([string]$PathValue) {
    (git hash-object -- $PathValue).Trim().ToLowerInvariant()
  }

  function Ensure-LegacyBackupDir {
    if (-not $script:legacyBackupRunDir) {
      $script:legacyBackupRunDir = Join-Path $legacyBackupRoot (Get-Date -Format 'yyyyMMdd-HHmmss')
      New-Item -ItemType Directory -Force -Path $script:legacyBackupRunDir | Out-Null
    }
  }

  function Move-LegacyRuleToBackup([string]$File, [string]$Target) {
    Ensure-LegacyBackupDir
    $destination = Join-Path $script:legacyBackupRunDir $File
    Move-Item -LiteralPath $Target -Destination $destination -Force
    Write-Host "Quarantined legacy claude-code-rules file $File -> $destination"
  }

  function Test-RepoHistoricalBlob([string]$File, [string]$Blob) {
    if ([string]::IsNullOrWhiteSpace($Blob)) { return $false }
    foreach ($commit in (git -C $SourceRepo rev-list --all -- $File 2>$null)) {
      $historicalBlob = (git -C $SourceRepo rev-parse ("{0}:{1}" -f $commit, $File) 2>$null).Trim().ToLowerInvariant()
      if ($historicalBlob -eq $Blob) { return $true }
    }
    return $false
  }

  if (Test-Path -LiteralPath $manifestPath) {
    foreach ($line in Get-Content -LiteralPath $manifestPath) {
      if ([string]::IsNullOrWhiteSpace($line)) { continue }
      $parts = $line -split "`t", 3
      $file = $parts[0]
      $recordedSha256 = if ($parts.Count -gt 1) { $parts[1].Trim().ToLowerInvariant() } else { '' }
      $recordedBlob = if ($parts.Count -gt 2) { $parts[2].Trim().ToLowerInvariant() } else { '' }
      if ($activeRuleFiles -contains $file) { continue }
      $target = Join-Path $rulesDir $file
      if (Test-Path -LiteralPath $target) {
        $currentSha256 = Get-RuleHash $target
        $currentBlob = Get-GitBlobHash $target
        $manifestMatch = $false
        if (-not [string]::IsNullOrWhiteSpace($recordedBlob)) {
          $manifestMatch = ($currentBlob -eq $recordedBlob)
        } elseif (-not [string]::IsNullOrWhiteSpace($recordedSha256)) {
          $manifestMatch = ($currentSha256 -eq $recordedSha256)
        }
        if ($manifestMatch) {
          Remove-Item -LiteralPath $target -Force -ErrorAction SilentlyContinue
        } else {
          Write-Host "Skipping manifest cleanup for $file because it no longer matches the previous claude-code-rules install snapshot."
        }
      }
    }
  }

  foreach ($file in $legacyCandidateFiles) {
    if ($activeRuleFiles -contains $file) { continue }
    $target = Join-Path $rulesDir $file
    if (Test-Path -LiteralPath $target) {
      $currentBlob = Get-GitBlobHash $target
      if (Test-RepoHistoricalBlob $file $currentBlob) {
        Move-LegacyRuleToBackup $file $target
      }
    }
  }

  $manifestLines = New-Object System.Collections.Generic.List[string]
  foreach ($file in $activeRuleFiles) {
    $sourcePath = Join-Path $SourceRepo $file
    $installedPath = Join-Path $rulesDir $file
    Copy-Item -LiteralPath $sourcePath -Destination $installedPath -Force
    $manifestLines.Add("$file`t$(Get-RuleHash $installedPath)`t$(Get-GitBlobHash $installedPath)")
  }
  Set-Content -LiteralPath $manifestPath -Value $manifestLines

  Write-Host "Installed $($activeRuleFiles.Count) active Claude Code rules into $rulesDir"
  Write-Host "Manifest: $manifestPath"
}
finally {
  Cleanup-TemporaryClone
}
