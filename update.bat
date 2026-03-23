@echo off
echo Updating Remember The Milk Exporter...

call git pull
if %ERRORLEVEL% NEQ 0 (
    echo Error pulling latest changes.
    pause
    exit /b 1
)

call uv sync --all-extras
if %ERRORLEVEL% NEQ 0 (
    echo Error updating dependencies.
    pause
    exit /b 1
)

echo.
echo Update completed successfully!
echo.
pause
