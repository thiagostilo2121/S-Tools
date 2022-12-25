import os
from datetime import date
from datetime import datetime

lista_de_archivos = ['0.txt', 'ins.txt', 'ins.bat', '../pass.txt', '../crash.txt']

for archivo in lista_de_archivos:
    if os.path.exists(archivo): 
        os.remove(archivo)    
    else:
        print(f"AVISO: El archivo {archivo} no se encuentra")


exit()