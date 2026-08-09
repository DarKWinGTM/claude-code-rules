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

function Get-PathEntry([string]$PathValue) {
  Get-Item -LiteralPath $PathValue -Force -ErrorAction SilentlyContinue
}

function Test-LinkEntry($Entry) {
  if ($null -eq $Entry) { return $false }
  return (($Entry.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0)
}

function Assert-ManagedDirectory([string]$PathValue, [string]$Label) {
  $entry = Get-PathEntry $PathValue
  if (Test-LinkEntry $entry) { throw "$Label must not be a symbolic link or reparse point: $PathValue" }
  if ($entry -and -not $entry.PSIsContainer) { throw "$Label is not a directory: $PathValue" }
}

function Get-RuleHash([string]$PathValue) {
  (Get-FileHash -LiteralPath $PathValue -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Get-GitBlobHash([string]$PathValue) {
  $output = @(git hash-object -- $PathValue 2>$null)
  if ($LASTEXITCODE -ne 0 -or $output.Count -eq 0) { return '' }
  return $output[0].Trim().ToLowerInvariant()
}

function Test-SafeRuleFilename([string]$File) {
  if ([string]::IsNullOrWhiteSpace($File) -or $File -eq '.' -or $File -eq '..') { return $false }
  if ($File.Contains('/') -or $File.Contains('\')) { return $false }
  return ([System.IO.Path]::GetFileName($File) -eq $File)
}

function Test-ValidHashField([string]$Value) {
  if ([string]::IsNullOrWhiteSpace($Value)) { return $true }
  return ($Value -match '^[0-9a-fA-F]{40}$' -or $Value -match '^[0-9a-fA-F]{64}$')
}

$ProjectRoot = Resolve-ExistingDirectory $ProjectRoot 'Project root'
$script:clonedRepoDir = $null
$script:stagingDir = $null
$script:quarantineRunDir = $null
$script:quarantineRootPreexisting = $false
$script:mutationStarted = $false
$script:commitSucceeded = $false
$script:manifestBackedUp = $false
$script:manifestInstalled = $false
$script:quarantineMoved = New-Object System.Collections.Generic.List[object]
$script:activeInstalled = New-Object System.Collections.Generic.List[string]
$script:activeBackups = New-Object System.Collections.Generic.List[string]

function Rollback-Install {
  if (-not $script:mutationStarted -or $script:commitSucceeded) { return }

  if ($script:manifestInstalled) {
    Remove-Item -LiteralPath $manifestPath -Force -ErrorAction SilentlyContinue
  }
  $manifestBackup = if ($script:stagingDir) { Join-Path $script:stagingDir 'manifest-backup.tsv' } else { $null }
  if ($script:manifestBackedUp -and $manifestBackup -and (Test-Path -LiteralPath $manifestBackup -PathType Leaf)) {
    Move-Item -LiteralPath $manifestBackup -Destination $manifestPath -Force -ErrorAction SilentlyContinue
  }

  for ($index = $script:activeInstalled.Count - 1; $index -ge 0; $index--) {
    Remove-Item -LiteralPath (Join-Path $rulesDir $script:activeInstalled[$index]) -Force -ErrorAction SilentlyContinue
  }
  for ($index = $script:activeBackups.Count - 1; $index -ge 0; $index--) {
    $file = $script:activeBackups[$index]
    $backup = Join-Path (Join-Path $script:stagingDir 'active-backup') $file
    if (Test-Path -LiteralPath $backup -PathType Leaf) {
      Move-Item -LiteralPath $backup -Destination (Join-Path $rulesDir $file) -Force -ErrorAction SilentlyContinue
    }
  }

  for ($index = $script:quarantineMoved.Count - 1; $index -ge 0; $index--) {
    $move = $script:quarantineMoved[$index]
    if (Test-Path -LiteralPath $move.Destination) {
      if (-not (Get-PathEntry $move.Source)) {
        Move-Item -LiteralPath $move.Destination -Destination $move.Source -Force -ErrorAction SilentlyContinue
      } else {
        Write-Warning "Rollback could not restore quarantine source because it now exists: $($move.Source)"
      }
    }
  }

  if ($script:quarantineRunDir -and (Test-Path -LiteralPath $script:quarantineRunDir -PathType Container)) {
    Remove-Item -LiteralPath $script:quarantineRunDir -Force -ErrorAction SilentlyContinue
  }
  if (-not $script:quarantineRootPreexisting -and $quarantineRoot -and (Test-Path -LiteralPath $quarantineRoot -PathType Container)) {
    Remove-Item -LiteralPath $quarantineRoot -Force -ErrorAction SilentlyContinue
  }
}

function Cleanup-TemporaryState {
  if ($script:stagingDir -and (Test-Path -LiteralPath $script:stagingDir)) {
    Remove-Item -LiteralPath $script:stagingDir -Recurse -Force -ErrorAction SilentlyContinue
  }
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
      $candidateRepo = Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..') -ErrorAction SilentlyContinue
      if ($candidateRepo) { $candidateRepo = $candidateRepo.Path }
    }

    if ($candidateRepo -and (Test-Path -LiteralPath (Join-Path $candidateRepo 'README.md')) -and (Test-Path -LiteralPath (Join-Path $candidateRepo 'accurate-communication.md'))) {
      $SourceRepo = $candidateRepo
    } else {
      $script:clonedRepoDir = Join-Path ([System.IO.Path]::GetTempPath()) ("claude-code-rules-" + [System.Guid]::NewGuid().ToString('N'))
      git clone $RepoUrl (Join-Path $script:clonedRepoDir 'claude-code-rules') | Out-Null
      if ($LASTEXITCODE -ne 0) { throw 'Unable to clone claude-code-rules source.' }
      $SourceRepo = Join-Path $script:clonedRepoDir 'claude-code-rules'
      if (-not [string]::IsNullOrWhiteSpace($Ref)) {
        git -C $SourceRepo checkout $Ref | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "Unable to checkout source ref: $Ref" }
      }
    }
  }

  if (-not (Test-Path -LiteralPath (Join-Path $SourceRepo 'README.md')) -or -not (Test-Path -LiteralPath (Join-Path $SourceRepo 'accurate-communication.md'))) {
    throw "Source repo does not look like claude-code-rules: $SourceRepo"
  }

  $claudeDir = Join-Path $ProjectRoot '.claude'
  $rulesDir = Join-Path $claudeDir 'rules'
  $quarantineParent = Join-Path $claudeDir 'quarantine'
  $quarantineRoot = Join-Path $quarantineParent 'claude-code-rules'
  Assert-ManagedDirectory $claudeDir 'Claude directory'
  Assert-ManagedDirectory $rulesDir 'Rules directory'
  New-Item -ItemType Directory -Force -Path $rulesDir | Out-Null
  Assert-ManagedDirectory $claudeDir 'Claude directory'
  Assert-ManagedDirectory $rulesDir 'Rules directory'

  $manifestPath = Join-Path $rulesDir '.claude-code-rules-manifest.tsv'
  $priorInTreeQuarantine = Join-Path $rulesDir '.claude-code-rules-legacy-backup'

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
    'goal-authoring-and-route-support.md',
    'external-verification-and-source-trust.md',
    'memory-governance-and-session-boundary.md',
    'phase-todo-artifact.md',
    'portable-implementation-and-hardcoding-control.md',
    'refusal-and-recovery.md',
    'safe-io.md',
    'worker-routing-and-context.md'
  )

  $retiredRuleCandidates = @(
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

  $manifestRecords = @{}
  $manifestRecordList = New-Object System.Collections.Generic.List[object]
  $manifestEntry = Get-PathEntry $manifestPath
  if (Test-LinkEntry $manifestEntry) { throw "Manifest path must not be a symbolic link or reparse point: $manifestPath" }
  if ($manifestEntry -and $manifestEntry.PSIsContainer) { throw "Manifest path is not a regular file: $manifestPath" }
  if ($manifestEntry) {
    $lineNumber = 0
    foreach ($line in [System.IO.File]::ReadAllLines($manifestPath)) {
      $lineNumber++
      if ([string]::IsNullOrWhiteSpace($line)) { continue }
      $parts = $line -split "`t", 3
      $file = $parts[0]
      $recordedSha256 = if ($parts.Count -gt 1) { $parts[1].Trim().ToLowerInvariant() } else { '' }
      $recordedBlob = if ($parts.Count -gt 2) { $parts[2].Trim().ToLowerInvariant() } else { '' }
      if (-not (Test-SafeRuleFilename $file)) { throw "Unsafe filename in manifest line ${lineNumber}: $file" }
      if ($manifestRecords.ContainsKey($file)) { throw "Duplicate filename in manifest line ${lineNumber}: $file" }
      if (-not (Test-ValidHashField $recordedSha256)) { throw "Invalid SHA-256 in manifest line $lineNumber." }
      if (-not (Test-ValidHashField $recordedBlob)) { throw "Invalid Git blob hash in manifest line $lineNumber." }
      $record = [pscustomobject]@{ File = $file; Sha256 = $recordedSha256; Blob = $recordedBlob }
      $manifestRecords[$file] = $record
      $manifestRecordList.Add($record)
    }
  }

  function Test-RecordedSnapshot([string]$Target, $Record) {
    $currentSha256 = Get-RuleHash $Target
    $currentBlob = Get-GitBlobHash $Target
    if (-not [string]::IsNullOrWhiteSpace($Record.Blob)) { return ($currentBlob -eq $Record.Blob) }
    if (-not [string]::IsNullOrWhiteSpace($Record.Sha256)) { return ($currentSha256 -eq $Record.Sha256) }
    return $false
  }

  function Test-RepoHistoricalBlob([string]$File, [string]$Blob) {
    if ([string]::IsNullOrWhiteSpace($Blob)) { return $false }
    $commits = @(git -C $SourceRepo rev-list --all -- $File 2>$null)
    foreach ($commit in $commits) {
      $output = @(git -C $SourceRepo rev-parse ("{0}:{1}" -f $commit, $File) 2>$null)
      if ($LASTEXITCODE -eq 0 -and $output.Count -gt 0 -and $output[0].Trim().ToLowerInvariant() -eq $Blob) { return $true }
    }
    return $false
  }

  function Test-ActiveTargetOwned([string]$File) {
    $sourcePath = Join-Path $SourceRepo $File
    $sourceEntry = Get-PathEntry $sourcePath
    if (-not $sourceEntry -or $sourceEntry.PSIsContainer -or (Test-LinkEntry $sourceEntry)) {
      throw "Active source rule must be a regular non-link file: $sourcePath"
    }

    $target = Join-Path $rulesDir $File
    $targetEntry = Get-PathEntry $target
    if (Test-LinkEntry $targetEntry) { throw "Active rule target must not be a symbolic link or reparse point: $target" }
    if ($targetEntry -and $targetEntry.PSIsContainer) { throw "Active rule target is not a regular file: $target" }
    if (-not $targetEntry) { return $true }
    if ((Get-RuleHash $target) -eq (Get-RuleHash $sourcePath)) { return $true }
    if ($manifestRecords.ContainsKey($File) -and (Test-RecordedSnapshot $target $manifestRecords[$File])) { return $true }
    $currentBlob = Get-GitBlobHash $target
    if (Test-RepoHistoricalBlob $File $currentBlob) { return $true }
    throw "Refusing to overwrite modified or unowned active rule target: $target"
  }

  $plannedQuarantine = New-Object System.Collections.Generic.List[object]
  $plannedSources = @{}
  $plannedNames = @{}
  function Add-QuarantinePlan([string]$Label, [string]$Source, [string]$DestinationName, [bool]$IsDirectory) {
    if ($plannedSources.ContainsKey($Source)) { return }
    if ($plannedNames.ContainsKey($DestinationName)) { throw "Duplicate quarantine destination name: $DestinationName" }
    $plan = [pscustomobject]@{ Label = $Label; Source = $Source; DestinationName = $DestinationName; IsDirectory = $IsDirectory }
    $plannedQuarantine.Add($plan)
    $plannedSources[$Source] = $true
    $plannedNames[$DestinationName] = $true
  }

  foreach ($file in $activeRuleFiles) { [void](Test-ActiveTargetOwned $file) }

  $priorEntry = Get-PathEntry $priorInTreeQuarantine
  if (Test-LinkEntry $priorEntry) { throw "Prior in-tree quarantine path must not be a symbolic link or reparse point: $priorInTreeQuarantine" }
  if ($priorEntry) {
    if (-not $priorEntry.PSIsContainer) { throw "Prior in-tree quarantine path is not a directory: $priorInTreeQuarantine" }
    Add-QuarantinePlan 'prior in-tree quarantine directory' $priorInTreeQuarantine 'prior-in-tree-quarantine' $true
  }

  foreach ($record in $manifestRecordList) {
    $file = [string]$record.File
    if ($activeRuleFiles -contains $file) { continue }
    $target = Join-Path $rulesDir $file
    $entry = Get-PathEntry $target
    if (Test-LinkEntry $entry) { throw "Manifest-owned target must not be a symbolic link or reparse point: $target" }
    if ($entry -and $entry.PSIsContainer) { throw "Manifest-owned target is not a regular file: $target" }
    if ($entry) {
      if (Test-RecordedSnapshot $target $record) {
        Add-QuarantinePlan "obsolete manifest-owned rule $file" $target $file $false
      } else {
        Write-Host "Skipping manifest quarantine for $file because it no longer matches the previous claude-code-rules install snapshot."
      }
    }
  }

  foreach ($file in $retiredRuleCandidates) {
    if ($activeRuleFiles -contains $file) { continue }
    $target = Join-Path $rulesDir $file
    if ($plannedSources.ContainsKey($target)) { continue }
    $entry = Get-PathEntry $target
    if (Test-LinkEntry $entry) { throw "Retired rule candidate must not be a symbolic link or reparse point: $target" }
    if ($entry -and $entry.PSIsContainer) { throw "Retired rule candidate is not a regular file: $target" }
    if ($entry) {
      $currentBlob = Get-GitBlobHash $target
      if (Test-RepoHistoricalBlob $file $currentBlob) {
        Add-QuarantinePlan "retired historical rule $file" $target $file $false
      }
    }
  }

  Assert-ManagedDirectory $claudeDir 'Claude directory'
  Assert-ManagedDirectory $rulesDir 'Rules directory'
  $script:stagingDir = Join-Path $claudeDir ('.claude-code-rules-stage-' + [System.Guid]::NewGuid().ToString('N'))
  New-Item -ItemType Directory -Path $script:stagingDir | Out-Null
  Assert-ManagedDirectory $script:stagingDir 'Staging directory'
  $activeBackupDir = Join-Path $script:stagingDir 'active-backup'
  New-Item -ItemType Directory -Path $activeBackupDir | Out-Null
  $stagedManifest = Join-Path $script:stagingDir '.claude-code-rules-manifest.tsv'
  $manifestLines = New-Object System.Collections.Generic.List[string]
  foreach ($file in $activeRuleFiles) {
    $stagedPath = Join-Path $script:stagingDir $file
    Copy-Item -LiteralPath (Join-Path $SourceRepo $file) -Destination $stagedPath
    $manifestLines.Add("$file`t$(Get-RuleHash $stagedPath)`t$(Get-GitBlobHash $stagedPath)")
  }
  $manifestText = ($manifestLines -join "`n") + "`n"
  [System.IO.File]::WriteAllText($stagedManifest, $manifestText, [System.Text.UTF8Encoding]::new($false))

  $script:mutationStarted = $true

  if ($plannedQuarantine.Count -gt 0) {
    Assert-ManagedDirectory $claudeDir 'Claude directory'
    Assert-ManagedDirectory $quarantineParent 'Quarantine parent'
    Assert-ManagedDirectory $quarantineRoot 'Quarantine root'
    $quarantineEntry = Get-PathEntry $quarantineRoot
    $script:quarantineRootPreexisting = ($null -ne $quarantineEntry)
    New-Item -ItemType Directory -Force -Path $quarantineRoot | Out-Null
    Assert-ManagedDirectory $quarantineParent 'Quarantine parent'
    Assert-ManagedDirectory $quarantineRoot 'Quarantine root'
    $runId = "run-{0}-{1}" -f (Get-Date -Format 'yyyyMMdd-HHmmss'), [System.Guid]::NewGuid().ToString('N').Substring(0, 12)
    $script:quarantineRunDir = Join-Path $quarantineRoot $runId
    New-Item -ItemType Directory -Path $script:quarantineRunDir | Out-Null
    Assert-ManagedDirectory $script:quarantineRunDir 'Quarantine run directory'

    foreach ($plan in $plannedQuarantine) {
      $sourceEntry = Get-PathEntry $plan.Source
      if (-not $sourceEntry -or (Test-LinkEntry $sourceEntry)) { throw "Quarantine source changed after preflight: $($plan.Source)" }
      if ($plan.IsDirectory -and -not $sourceEntry.PSIsContainer) { throw "Quarantine directory source changed after preflight: $($plan.Source)" }
      if (-not $plan.IsDirectory -and $sourceEntry.PSIsContainer) { throw "Quarantine file source changed after preflight: $($plan.Source)" }
      $destination = Join-Path $script:quarantineRunDir $plan.DestinationName
      if (Get-PathEntry $destination) { throw "Quarantine destination already exists for $($plan.Label): $destination" }
      Move-Item -LiteralPath $plan.Source -Destination $destination
      $script:quarantineMoved.Add([pscustomobject]@{ Source = $plan.Source; Destination = $destination })
      Write-Host "Quarantined claude-code-rules $($plan.Label) -> $destination"
    }
  }

  foreach ($file in $activeRuleFiles) {
    [void](Test-ActiveTargetOwned $file)
    $target = Join-Path $rulesDir $file
    $entry = Get-PathEntry $target
    if ($entry) {
      Move-Item -LiteralPath $target -Destination (Join-Path $activeBackupDir $file)
      $script:activeBackups.Add($file)
    }
    Move-Item -LiteralPath (Join-Path $script:stagingDir $file) -Destination $target
    $script:activeInstalled.Add($file)
  }

  $manifestEntry = Get-PathEntry $manifestPath
  if (Test-LinkEntry $manifestEntry) { throw "Manifest path changed to a symbolic link or reparse point before replacement: $manifestPath" }
  if ($manifestEntry -and $manifestEntry.PSIsContainer) { throw "Manifest path changed to a non-regular file before replacement: $manifestPath" }
  if ($manifestEntry) {
    Move-Item -LiteralPath $manifestPath -Destination (Join-Path $script:stagingDir 'manifest-backup.tsv')
    $script:manifestBackedUp = $true
  }
  Move-Item -LiteralPath $stagedManifest -Destination $manifestPath
  $script:manifestInstalled = $true

  $script:commitSucceeded = $true
  Remove-Item -LiteralPath $script:stagingDir -Recurse -Force
  $script:stagingDir = $null

  Write-Host "Installed $($activeRuleFiles.Count) active Claude Code rules into $rulesDir"
  Write-Host "Manifest: $manifestPath"
  if ($script:quarantineRunDir) { Write-Host "Quarantine: $script:quarantineRunDir" }
}
finally {
  if ($script:mutationStarted -and -not $script:commitSucceeded) { Rollback-Install }
  Cleanup-TemporaryState
}
