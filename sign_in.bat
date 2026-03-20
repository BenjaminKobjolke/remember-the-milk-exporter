@echo off
echo Running Remember The Milk Sign In...

REM Activate virtual environment
call %~dp0\venv\Scripts\activate.bat

REM Run authentication only
call python main.py --auth-only

echo.
echo Sign in complete. You can now run run.bat to export your data.
echo.
pause
