# PowerShell script to watch for file changes and auto-restart MkDocs server

# Set PYTHONPATH to current directory
$env:PYTHONPATH = $PWD.Path

Write-Host "Starting MkDocs with auto-reload on file changes..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
Write-Host ""

# Define paths to watch
$pathsToWatch = @(
    "docs",
    "mkdocs.yml",
    "extensions",
    "overrides"
)

# Start MkDocs server function
function Start-MkDocsServer {
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Starting MkDocs server..." -ForegroundColor Cyan
    
    # Start mkdocs in a new job
    $global:mkdocsJob = Start-Job -ScriptBlock {
        $env:PYTHONPATH = $using:PWD
        Set-Location $using:PWD
        mkdocs serve
    }
    
    Write-Host "MkDocs server started (Job ID: $($global:mkdocsJob.Id))" -ForegroundColor Green
    Write-Host ""
}

# Stop MkDocs server function
function Stop-MkDocsServer {
    if ($global:mkdocsJob) {
        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Stopping MkDocs server..." -ForegroundColor Yellow
        
        # Stop the job
        Stop-Job -Job $global:mkdocsJob -ErrorAction SilentlyContinue
        Remove-Job -Job $global:mkdocsJob -ErrorAction SilentlyContinue
        
        # Kill any remaining Python processes running mkdocs
        Get-Process python -ErrorAction SilentlyContinue | 
            Where-Object { $_.CommandLine -like "*mkdocs*" } | 
            Stop-Process -Force -ErrorAction SilentlyContinue
        
        Start-Sleep -Seconds 1
        Write-Host "MkDocs server stopped" -ForegroundColor Yellow
    }
}

# Cleanup on exit
$cleanup = {
    Write-Host "`nCleaning up..." -ForegroundColor Yellow
    Stop-MkDocsServer
    exit
}
Register-EngineEvent -SourceIdentifier PowerShell.Exiting -Action $cleanup | Out-Null

# Handle Ctrl+C
[Console]::TreatControlCAsInput = $false
try {
    # Start initial server
    Start-MkDocsServer
    
    # Create file watchers for each path
    $watchers = @()
    
    # Watch docs directory
    if (Test-Path "docs") {
        $watcher = New-Object System.IO.FileSystemWatcher
        $watcher.Path = Join-Path $PWD.Path "docs"
        $watcher.IncludeSubdirectories = $true
        $watcher.Filter = "*.*"
        $watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor 
                               [System.IO.NotifyFilters]::FileName -bor 
                               [System.IO.NotifyFilters]::DirectoryName
        $watcher.EnableRaisingEvents = $true
        $watchers += $watcher
    }
    
    # Watch extensions directory
    if (Test-Path "extensions") {
        $watcher = New-Object System.IO.FileSystemWatcher
        $watcher.Path = Join-Path $PWD.Path "extensions"
        $watcher.IncludeSubdirectories = $true
        $watcher.Filter = "*.py"
        $watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor 
                               [System.IO.NotifyFilters]::FileName
        $watcher.EnableRaisingEvents = $true
        $watchers += $watcher
    }
    
    # Watch overrides directory
    if (Test-Path "overrides") {
        $watcher = New-Object System.IO.FileSystemWatcher
        $watcher.Path = Join-Path $PWD.Path "overrides"
        $watcher.IncludeSubdirectories = $true
        $watcher.Filter = "*.*"
        $watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor 
                               [System.IO.NotifyFilters]::FileName
        $watcher.EnableRaisingEvents = $true
        $watchers += $watcher
    }
    
    # Watch mkdocs.yml
    if (Test-Path "mkdocs.yml") {
        $watcher = New-Object System.IO.FileSystemWatcher
        $watcher.Path = $PWD.Path
        $watcher.Filter = "mkdocs.yml"
        $watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite
        $watcher.EnableRaisingEvents = $true
        $watchers += $watcher
    }
    
    # Track last restart time to debounce
    $lastRestart = Get-Date
    $debounceSeconds = 2
    
    Write-Host "Watching for file changes..." -ForegroundColor Cyan
    Write-Host ""
    
    # Main loop
    while ($true) {
        # Check for file changes
        $changeDetected = $false
        
        foreach ($watcher in $watchers) {
            if ($watcher.WaitForChanged([System.IO.WatcherChangeTypes]::All, 1000).TimedOut -eq $false) {
                $changeDetected = $true
                break
            }
        }
        
        # Restart server if change detected and debounce period passed
        if ($changeDetected) {
            $timeSinceLastRestart = (Get-Date) - $lastRestart
            
            if ($timeSinceLastRestart.TotalSeconds -ge $debounceSeconds) {
                Write-Host "[$(Get-Date -Format 'HH:mm:ss')] File change detected! Restarting MkDocs server..." -ForegroundColor Magenta
                Write-Host ""
                
                Stop-MkDocsServer
                Start-Sleep -Seconds 1
                Start-MkDocsServer
                
                $lastRestart = Get-Date
            }
        }
        
        # Small delay to prevent high CPU usage
        Start-Sleep -Milliseconds 100
    }
}
finally {
    # Cleanup watchers
    foreach ($watcher in $watchers) {
        $watcher.Dispose()
    }
    
    # Stop server
    Stop-MkDocsServer
}
