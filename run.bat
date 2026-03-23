@echo off
echo Running Remember The Milk Tag Exporter...

call uv run python main.py

echo.
echo If the export was successful, you can find the tags in the configured output location.
echo Check the log messages for the exact file path.
echo.
pause
