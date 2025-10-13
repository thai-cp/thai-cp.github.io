# PowerShell script to watch for file changes and auto-restart MkDocs server
# Optimized for faster response and lower resource usage

# Set PYTHONPATH to current directory
$env:PYTHONPATH = $PWD.Path

Write-Host "Starting MkDocs with auto-reload on file changes..." -ForegroundColor Green
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
Write-Host ""

# Global variables for state management
$global:mkdocsJob = $null
$global:mkdocsProcess = $null
$global:restartTimer = $null
$global:watchers = @()
$global:events = @()

# Start MkDocs server function
function Start-MkDocsServer {
    Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Starting MkDocs server..." -ForegroundColor Cyan
    
    # Start mkdocs in a new job and capture the process
    $global:mkdocsJob = Start-Job -ScriptBlock {
        $env:PYTHONPATH = $using:PWD
        Set-Location $using:PWD
        mkdocs serve
    }
    
    # Wait briefly for process to start and capture its ID
    Start-Sleep -Milliseconds 500
    $global:mkdocsProcess = Receive-Job -Job $global:mkdocsJob -Keep | 
        Select-Object -First 1
    
    Write-Host "MkDocs server started (Job ID: $($global:mkdocsJob.Id))" -ForegroundColor Green
    Write-Host ""
}

# Stop MkDocs server function - optimized for speed
function Stop-MkDocsServer {
    if ($global:mkdocsJob) {
        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Stopping MkDocs server..." -ForegroundColor Yellow
        
        # Stop the job quickly
        Stop-Job -Job $global:mkdocsJob -ErrorAction SilentlyContinue
        Remove-Job -Job $global:mkdocsJob -Force -ErrorAction SilentlyContinue
        
        # Fast process cleanup - kill by name instead of searching CommandLine
        Get-Process -Name python -ErrorAction SilentlyContinue | 
            ForEach-Object {
                try {
                    $_.Kill()
                } catch {
                    # Ignore errors if process already died
                }
            }
        
        $global:mkdocsJob = $null
        $global:mkdocsProcess = $null
        Write-Host "MkDocs server stopped" -ForegroundColor Yellow
    }
}

# Restart server with debouncing using a timer
function Request-ServerRestart {
    # Cancel existing timer if any
    if ($global:restartTimer) {
        $global:restartTimer.Stop()
        $global:restartTimer.Dispose()
    }
    
    # Create new timer for debounced restart (500ms delay)
    $global:restartTimer = New-Object System.Timers.Timer
    $global:restartTimer.Interval = 200
    $global:restartTimer.AutoReset = $false
    
    Register-ObjectEvent -InputObject $global:restartTimer -EventName Elapsed -Action {
        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] File change detected! Restarting MkDocs server..." -ForegroundColor Magenta
        Write-Host ""
        
        Stop-MkDocsServer
        Start-MkDocsServer
    } | Out-Null
    
    $global:restartTimer.Start()
}

# File change event handler
$changeHandler = {
    Request-ServerRestart
}

# Cleanup function
function Cleanup {
    Write-Host "`nCleaning up..." -ForegroundColor Yellow
    
    # Stop timer
    if ($global:restartTimer) {
        $global:restartTimer.Stop()
        $global:restartTimer.Dispose()
    }
    
    # Unregister events
    foreach ($event in $global:events) {
        Unregister-Event -SourceIdentifier $event -ErrorAction SilentlyContinue
    }
    
    # Dispose watchers
    foreach ($watcher in $global:watchers) {
        $watcher.EnableRaisingEvents = $false
        $watcher.Dispose()
    }
    
    # Stop server
    Stop-MkDocsServer
}

# Cleanup on exit
Register-EngineEvent -SourceIdentifier PowerShell.Exiting -Action {
    Cleanup
    exit
} | Out-Null

# Handle Ctrl+C
try {
    # Start initial server
    Start-MkDocsServer
    
    # Create event-driven file watchers
    $watcherConfigs = @(
        @{ Path = "docs"; Filter = "*.*"; IncludeSubdirectories = $true },
        @{ Path = "extensions"; Filter = "*.py"; IncludeSubdirectories = $true },
        @{ Path = "overrides"; Filter = "*.*"; IncludeSubdirectories = $true },
        @{ Path = "."; Filter = "mkdocs.yml"; IncludeSubdirectories = $false }
    )
    
    $eventId = 0
    foreach ($config in $watcherConfigs) {
        $fullPath = Join-Path $PWD.Path $config.Path
        
        if (Test-Path $fullPath) {
            $watcher = New-Object System.IO.FileSystemWatcher
            $watcher.Path = $fullPath
            $watcher.Filter = $config.Filter
            $watcher.IncludeSubdirectories = $config.IncludeSubdirectories
            $watcher.NotifyFilter = [System.IO.NotifyFilters]::LastWrite -bor 
                                   [System.IO.NotifyFilters]::FileName -bor 
                                   [System.IO.NotifyFilters]::DirectoryName
            
            # Register events for Changed, Created, Deleted, Renamed
            foreach ($eventType in @('Changed', 'Created', 'Deleted', 'Renamed')) {
                $eventName = "FileWatcher_$($eventId)_$eventType"
                Register-ObjectEvent -InputObject $watcher -EventName $eventType `
                    -SourceIdentifier $eventName -Action $changeHandler | Out-Null
                $global:events += $eventName
                $eventId++
            }
            
            $watcher.EnableRaisingEvents = $true
            $global:watchers += $watcher
        }
    }
    
    Write-Host "Watching for file changes (event-driven mode)..." -ForegroundColor Cyan
    Write-Host "Monitoring: docs/, extensions/, overrides/, mkdocs.yml" -ForegroundColor Cyan
    Write-Host ""
    
    # Wait indefinitely - events will trigger restarts
    while ($true) {
        Start-Sleep -Seconds 1
        
        # Check if job is still running, restart if crashed
        if ($global:mkdocsJob -and $global:mkdocsJob.State -eq 'Failed') {
            Write-Host "[$(Get-Date -Format 'HH:mm:ss')] MkDocs server crashed! Restarting..." -ForegroundColor Red
            Start-MkDocsServer
        }
    }
}
catch {
    Write-Host "Error: $_" -ForegroundColor Red
}
finally {
    Cleanup
}
