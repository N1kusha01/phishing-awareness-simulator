@echo off
python -m venv venv
venv\Scripts\pip install -r requirements.txt
timeout /t 3 /nobreak
start http://127.0.0.1:5000
venv\Scripts\python app.py
pause