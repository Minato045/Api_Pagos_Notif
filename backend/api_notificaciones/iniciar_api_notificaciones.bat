@echo off
cd /d %~dp0
call venv\Scripts\activate
set FLASK_APP=app.py
flask run --port=5002
pause
