@echo off

REM read properties file
setlocal EnableExtensions EnableDelayedExpansion

set scriptHome=%~dp0
FOR %%A IN ("%~dp0.") DO set atomRoot=%%~dpA

set propFile=%scriptHome%allure.properties

if not exist "%propFile%" (
  echo Error: %propFile% does not exist.
  exit /b 1
)

if %errorlevel% neq 0 (
    echo ERROR: The properties file "%propFile%" is not well-structured.
    exit /b 1
)

for /f "usebackq tokens=1* delims==" %%a in ("%propFile%") do (
    set "prop.%%a=%%b"
)

REM Set the path to the Allure root directory
set "allureDir=%atomRoot%.allure"

REM Create the Allure root directory if it doesn't exist
if not exist "%allureDir%" (
    mkdir "%allureDir%"
)

REM Download the Allure CLI zip file if it doesn't exist
set allurePath=%allureDir%\allure-%prop.version%\bin\allure.bat

if not exist "%allurePath%" (
    echo Downloading Allure CLI version %prop.version%...

    set allureUrl=%prop.commandLineUrl%/%prop.version%/allure-commandline-%prop.version%.zip
    powershell -NoLogo -windowstyle hidden -Command "Invoke-WebRequest -Uri '!allureUrl!' -OutFile '%allureDir%\allure.zip'"

    if !errorlevel! neq 0 (
        echo ERROR: Failed to download allure-commandline: [!return!].
        exit /b 1
    )

    powershell -Command "Expand-Archive -Path '%allureDir%\allure.zip' -DestinationPath '%allureDir%'"

    if !errorlevel! neq 0 (
        echo ERROR: Failed to extract allure.zip.
        exit /b 1
    )
    del "%allureDir%\allure.zip"
)

REM run allure command
call "%allurePath%" generate --single-file --clean --report-dir "%atomRoot%%prop.allureReportDirectory%" "%atomRoot%%prop.allureResultsDirectory%"

endlocal
