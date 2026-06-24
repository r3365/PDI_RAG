# PDI_RAG - Portable Launcher (PowerShell)
$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LlamaPort = 8080
$env:LLAMA_ENDPOINT = "http://127.0.0.1:$LlamaPort/v1"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  PDI_RAG - NCC2025 Building Code Query Tool" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python
try {
    $pyVersion = python --version
    Write-Host "  Python: $pyVersion" -ForegroundColor Green
} catch {
    Write-Host "  ERROR: Python is not installed. Please install Python 3.10+." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Virtual environment
if (-not (Test-Path "$ScriptDir\venv\")) {
    Write-Host "  Creating virtual environment..." -ForegroundColor Yellow
    python -m venv "$ScriptDir\venv"
}

# Activate
$venvActivate = "$ScriptDir\venv\Scripts\Activate.ps1"
. $venvActivate

# Dependencies
Write-Host "  Checking dependencies..." -ForegroundColor Yellow
pip install -q chromadb pymupdf4llm gradio 2>&1 | Out-Null

# Stop any existing llama-server on our port
Get-Process -Name "llama-server" -ErrorAction SilentlyContinue | Stop-Process -Force

# Start llama-server in background
Write-Host "  Starting local LLM server (llama-server)..." -ForegroundColor Yellow
$llamaExe = Join-Path $ScriptDir "llama" "llama-server.exe"
$llamaModel = Join-Path $ScriptDir "llama" "model.gguf"
$llamaArgs = "-m `"$llamaModel`" -c 4096 --port $LlamaPort --host 127.0.0.1"
$llamaProcess = Start-Process -FilePath $llamaExe -ArgumentList $llamaArgs -WindowStyle Hidden -PassThru

# Wait for server
Write-Host "  Waiting for server to be ready..." -ForegroundColor Yellow
$ready = $false
for ($i = 0; $i -lt 30; $i++) {
    try {
        $resp = Invoke-WebRequest -Uri "http://127.0.0.1:$LlamaPort/health" -UseBasicParsing -TimeoutSec 1
        if ($resp.StatusCode -eq 200) { $ready = $true; break }
    } catch {}
    Start-Sleep -Seconds 1
}
if (-not $ready) {
    Write-Host "  ERROR: llama-server failed to start within 30s." -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host "  Server is ready!" -ForegroundColor Green
Write-Host ""

# Menu
Write-Host "  [1] Start webapp (Desktop app)" -ForegroundColor Green
Write-Host "  [2] Interactive query mode" -ForegroundColor Green
Write-Host "  [3] Single question" -ForegroundColor Green
Write-Host ""

$choice = Read-Host "Select option (1-3)"
try {
    switch ($choice) {
        "1" {
            $pakeApp = Join-Path $ScriptDir "NCC Building Code.exe"
            # Start webapp in background
            Write-Host "  Starting webapp..." -ForegroundColor Yellow
            $webLog = Join-Path $env:TEMP "webapp_portable.log"
            $webProcess = Start-Process -FilePath "python" -ArgumentList "`"$ScriptDir\webapp.py`"" -WindowStyle Hidden -RedirectStandardOutput $webLog -RedirectStandardError $webLog -PassThru
            # Wait for webapp to be ready
            Write-Host "  Waiting for webapp to be ready..." -ForegroundColor Yellow
            $webReady = $false
            for ($i = 0; $i -lt 60; $i++) {
                try {
                    $resp = Invoke-WebRequest -Uri "http://127.0.0.1:7860" -UseBasicParsing -TimeoutSec 2
                    if ($resp.StatusCode -eq 200) { $webReady = $true; break }
                } catch {}
                Start-Sleep -Seconds 1
            }
            if (-not $webReady) {
                Write-Host "  WARNING: webapp not ready yet, launching anyway..." -ForegroundColor Yellow
            }
            # Now launch the desktop app
            if (Test-Path $pakeApp) {
                Write-Host "  Launching desktop app..." -ForegroundColor Green
                $pakeProcess = Start-Process -FilePath $pakeApp -PassThru
            } else {
                Start-Process "http://127.0.0.1:7860"
            }
            Write-Host "  Close the desktop app or press Ctrl+C to shut down." -ForegroundColor Yellow
            # Wait for webapp or pake to close
            while ($true) {
                Start-Sleep -Seconds 2
                $wpAlive = Get-Process -Id $webProcess.Id -ErrorAction SilentlyContinue
                $ppAlive = $null
                if ($pakeApp -and (Test-Path $pakeApp)) {
                    $ppAlive = Get-Process -Id $pakeProcess.Id -ErrorAction SilentlyContinue
                }
                if (-not $wpAlive) { break }
                if ($ppAlive -eq $null -and (Test-Path $pakeApp)) { break }
            }
        }
        "2" {
            python "$ScriptDir\rag_pipeline.py"
        }
        "3" {
            $query = Read-Host "Enter your question"
            python "$ScriptDir\rag_pipeline.py" $query
        }
        default {
            Write-Host "Invalid option." -ForegroundColor Red
        }
    }
} finally {
    # Cleanup - kill llama-server when done
    Write-Host "  Shutting down llama-server..." -ForegroundColor Yellow
    Get-Process -Name "llama-server" -ErrorAction SilentlyContinue | Stop-Process -Force
}

Read-Host "Press Enter to exit"
