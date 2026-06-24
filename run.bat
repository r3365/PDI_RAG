@echo off
title PDI_RAG - NCC2025 Building Code RAG Pipeline
cls
echo ============================================================
echo   PDI_RAG - NCC2025 Building Code Query Tool
echo ============================================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed. Please install Python 3.10+.
    pause
    exit /b 1
)

:: Create virtual environment if missing
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate and ensure deps
call venv\Scripts\activate.bat >nul 2>&1
echo Installing dependencies (first run only)...
pip install -q chromadb pymupdf4llm gradio 2>nul

set LLAMA_PORT=8080
set "LLAMA_ENDPOINT=http://127.0.0.1:%LLAMA_PORT%/v1"

:: Kill any existing llama-server on our port
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":%LLAMA_PORT%"') do (
    taskkill /f /pid %%a >nul 2>&1
)

:: Start llama-server in background
echo Starting local LLM server (llama-server)...
start /b "" "%~dp0llama\llama-server.exe" -m "%~dp0llama\model.gguf" -c 4096 --port %LLAMA_PORT% --host 127.0.0.1

:: Wait for server to come up
echo Waiting for server to be ready...
:waitloop
timeout /t 1 /nobreak >nul
curl -s http://127.0.0.1:%LLAMA_PORT%/health >nul 2>&1
if errorlevel 1 goto waitloop

echo Server is ready!
echo.
echo  [1] Start webapp (Desktop app)
echo  [2] Interactive query mode
echo  [3] Single question
echo.

choice /c 123 /n /m "Select option: "
if errorlevel 3 goto option3
if errorlevel 2 goto option2
if errorlevel 1 goto option1

:option3
set /p query="Enter your question: "
python rag_pipeline.py "%query%"
echo.
pause
goto cleanup

:option2
python rag_pipeline.py
echo.
pause
goto cleanup

:option1
:: Start webapp in background
echo Starting webapp (may take 30-60s first time)...
start "" /b python "%~dp0webapp.py" >"%TEMP%\webapp_portable.log" 2>&1
:: Wait for webapp to be ready
echo Waiting for webapp to be ready...
:webwait
timeout /t 2 /nobreak >nul
curl -s http://127.0.0.1:7860 >nul 2>&1
if errorlevel 1 goto webwait
:: Webapp is ready - launch desktop app or browser
if exist "%~dp0NCC Building Code.exe" (
    start "" "%~dp0NCC Building Code.exe"
) else (
    start http://127.0.0.1:7860
)
echo.
echo Desktop app launched. Press any key to shut down.
pause >nul
goto cleanup

:cleanup
:: Webapp cleanup
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":7860"') do taskkill /f /pid %%a >nul 2>&1
:: Cleanup - kill llama-server when done
taskkill /f /im llama-server.exe >nul 2>&1
