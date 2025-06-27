@echo off
cd /d C:\Users\HachiAi\Desktop\browseruse

REM Step 1: Activate uv-managed virtual environment
call .venv\Scripts\activate.bat

REM Step 2: Install dependencies (only needed once – comment after first run)
uv pip install -r requirements.txt
uv pip install browser-use
uv run playwright install

REM Step 3: Run the pipeline
python run_pipeline.py

pause
