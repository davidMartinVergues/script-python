@REM @echo off
@REM call .\venv_376\Scripts\activate.bat .\venv_376
@REM ".\venv_376\Scripts\python.exe" ".\my_watchdog.py"

@echo off
call ".\script-excel-to-sqlerver\venv_376\Scripts\activate.bat" ".\script-excel-to-sqlerver\venv_376"
".\script-excel-to-sqlerver\venv_376\Scripts\python.exe" ".\script-excel-to-sqlerver\my_watchdog.py"
pause
