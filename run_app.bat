REM Language: Batch
REM Key Libraries: None
REM Purpose: Execute the local python environment and launch the web server silently.
REM Book: Build a Smart Document Operations Center with Python

@echo off
cd /d "%~dp0"
call .venv\Scripts\activate.bat
start /B streamlit run app.py