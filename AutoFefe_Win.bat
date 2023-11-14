@echo off
setlocal enabledelayedexpansion

REM Check for the presence of Python
where python >nul 2>&1
if %errorLevel% neq 0 (
    echo Python is not installed. Please install Python and run this script again.
    exit /b
)

REM Check for the existence of the "autofefe" folder
if not exist "autofefe" (
    echo "autofefe" folder not found. Running setup...
    call lib\setup.bat
)

call autofefe\Scripts\activate

:menu
cls
echo 1. Run AutoFefe.py
echo 2. Setup Keys
echo 3. Exit

set /p choice=Enter your choice (1-3): 

if "%choice%"=="1" (
    python AutoFefe.py
    goto menu
) else if "%choice%"=="2" (
    call lib\KeysSetup.bat
    goto menu
) else if "%choice%"=="3" (
    exit /b
) else (
    echo Invalid choice. Please enter a number between 1 and 3.
    timeout /nobreak /t 2 >nul
    goto menu
)
