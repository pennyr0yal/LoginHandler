@echo off

cd /d "%~dp0"

if not exist ".venv" (
    python -m venv .venv
)

call .venv\Scripts\activate.bat

python -m pip install --upgrade pip

pip install -r requirements.txt

cls

call .venv\Scripts\activate.bat

python Script\main.py

pause