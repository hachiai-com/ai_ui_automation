@echo off
echo Creating virtual environment...
uv venv --python 3.11.13

echo Activating environment...
call .venv\Scripts\activate

echo Installing requirements...
uv pip install -r requirements.txt
uv pip install browser-use

echo Installing Playwright...
uv run playwright install

echo Setup complete.
pause
