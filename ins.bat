@echo off

pip install -r requirements.txt
cd PasswordGenerator
cd Data
py confirm.py
cls 
echo Finalizado...
echo .
echo .
echo .
echo Presiona una tecla para salir...
pause>nul
