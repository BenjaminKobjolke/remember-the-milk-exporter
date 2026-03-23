@echo off
echo Running Remember The Milk Sign In...

call uv run python main.py --auth-only

echo.
echo Sign in complete. You can now run run.bat to export your data.
echo.
pause
