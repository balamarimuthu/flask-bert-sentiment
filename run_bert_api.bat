@echo off
cd /d "C:\Users\balap\for jupyter note book\BERT"
call .venv\Scripts\activate
start "" http://127.0.0.1:8000/docs
python -m uvicorn app:app --reload
pause
