<<<<<<< HEAD
@echo off
setlocal enabledelayedexpansion

:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

REM Get existing value of PYTHON_DB or set it to an empty string if not defined
set "PYTHON_DB=!PYTHON_DB!"

REM Get user input for key name
set /p key_name=Enter key name (e.g., EMAIL_ADDRESS): 

REM Get user input for key value
set /p key_value=Enter key value for %key_name%: 

REM Format the key and value
set "formatted_key_value=!key_name!:!key_value!"

REM Check if PYTHON_DB is empty
if "!PYTHON_DB!"=="" (
    REM Set PYTHON_DB if empty
    set "PYTHON_DB=!formatted_key_value!"
) else (
    REM Append to existing PYTHON_DB with a semicolon separator
    set "PYTHON_DB=!PYTHON_DB!;!formatted_key_value!"
)

REM Set or update the system variable
setx PYTHON_DB "!PYTHON_DB!" /M

echo PYTHON_DB has been set or updated. Vai Corinthians!
=======
@echo off
setlocal enabledelayedexpansion

:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

REM Get existing value of PYTHON_DB or set it to an empty string if not defined
set "PYTHON_DB=!PYTHON_DB!"

REM Get user input for key name
set /p key_name=Enter key name (e.g., EMAIL_ADDRESS): 

REM Get user input for key value
set /p key_value=Enter key value for %key_name%: 

REM Format the key and value
set "formatted_key_value=!key_name!:!key_value!"

REM Check if PYTHON_DB is empty
if "!PYTHON_DB!"=="" (
    REM Set PYTHON_DB if empty
    set "PYTHON_DB=!formatted_key_value!"
) else (
    REM Append to existing PYTHON_DB with a semicolon separator
    set "PYTHON_DB=!PYTHON_DB!;!formatted_key_value!"
)

REM Set or update the system variable
setx PYTHON_DB "!PYTHON_DB!" /M

echo PYTHON_DB has been set or updated. Vai Corinthians!
>>>>>>> 7b0acce (adding readme, removing sensitive information and adding arduino sketch)
