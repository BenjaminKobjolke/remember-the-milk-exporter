@echo off
echo Running integration tests...

call uv run pytest tests/ -v -m integration
if %ERRORLEVEL% NEQ 0 (
    echo Integration tests failed.
    pause
    exit /b 1
)

echo.
echo All integration tests passed!
echo.
pause
