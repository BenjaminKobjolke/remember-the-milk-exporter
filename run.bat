@echo off
echo Running Remember The Milk Tag Exporter...

REM Activate virtual environment
call %~dp0\venv\Scripts\activate.bat

REM Run the application
call python main.py

echo.
echo If the export was successful, you can find the tags in the output/rtm_tags.txt file.
echo.
pause
