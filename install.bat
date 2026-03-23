@echo off
echo Installing Remember The Milk Exporter...

REM Check if uv is installed
call uv --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo uv is not installed or not in the PATH.
    echo Please install uv from https://docs.astral.sh/uv/getting-started/installation/
    pause
    exit /b 1
)

REM Check if Git is installed (needed for git dependencies)
call git --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Git is not installed or not in the PATH.
    echo Please install Git from https://git-scm.com/downloads
    echo It is required to install packages from GitHub.
    pause
    exit /b 1
)

echo Installing dependencies...
call uv sync --all-extras
if %ERRORLEVEL% NEQ 0 (
    echo Error installing dependencies.
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo Installation completed successfully!
echo.
echo Please copy settings_example.ini to settings.ini and add your Remember The Milk API credentials.
echo.
pause
