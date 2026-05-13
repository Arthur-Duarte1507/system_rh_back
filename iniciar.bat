@echo off
echo Iniciando API RH...

python -m venv venv

call venv\Scripts\activate.bat

pip install -r requirements.txt

uvicorn principal:app --reload --host 0.0.0.0

pause