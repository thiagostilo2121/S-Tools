@echo off
color A

cd PasswordGenerator 
pip uninstall werkzeug 
pip uninstall progress 
echo "0123456789"
cd Data
py unconfirm.py
cls
set ok= Se eliminaran los archivos 'pass.txt' y 'crash.txt' 

unconfirm2.py
goto siguiente

cls 
echo Finalizado...
echo .
echo .
echo .
echo Presiona una tecla para salir...
pause>nul