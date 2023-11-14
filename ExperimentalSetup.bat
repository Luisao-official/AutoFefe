@echo off
setlocal EnableDelayedExpansion

REM Check if the script is running with administrative privileges
REM This is not the beds way to do it, but it works.
>nul 2>&1 net session
if %errorLevel% neq 0 (
    echo This script requires administrative privileges. Re-running with elevated permissions...
    set "scriptPath=%~0"
    set "scriptPath=!scriptPath:\=\\!"
    powershell Start-Process -FilePath "cmd.exe" -ArgumentList "/c %scriptPath%" -Verb RunAs
    exit /b
)

set "scriptDir=%~dp0"
set "currentPath=!PATH!"

REM Add Python interpreter directory to PATH
set "newPath=%scriptDir%;%currentPath%"


setx PATH "!newPath!" /M
echo Python interpreter added to PATH.

python AutoFefe.py

set "newPath=!currentPath:%scriptDir%;=!"
setx PATH "!newPath!" /M

echo Python interpreter removed from PATH.

REM Pause the script to allow the user to read the output
pause
endlocal
