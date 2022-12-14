@echo off

cd PasswordGenerator 
pip install werkzeug 
pip install progress 
echo "0123456789"
cd Data
py confirm.py
cls 
echo Finalizado...
echo .
echo .
echo .
echo Presiona una tecla para salir...
pause>nul
