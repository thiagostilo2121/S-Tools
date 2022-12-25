@echo off
color A

pip uninstall -y -r requirements.txt
cd PasswordGenerator
cd Data
py unconfirm.py
cls
set ok= Se eliminaran los archivos 'pass.txt' y 'crash.txt' 

cls
echo Finalizado...
echo .
echo .
echo .
echo Presiona una tecla para salir...
pause>nul