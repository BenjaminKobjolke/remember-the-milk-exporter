@echo off
echo Running tests...

call uv run pytest tests/ -v
if %ERRORLEVEL% NEQ 0 (
    echo Tests failed.
    pause
    exit /b 1
)

echo.
echo All tests passed!
echo.
pause
