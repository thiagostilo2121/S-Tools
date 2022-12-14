# --_OPEN_--

#Importacion de paquetes

from progress.bar import Bar, ChargingBar
import random, time
from datetime import date
from datetime import datetime
import os 
from werkzeug.security import generate_password_hash, check_password_hash
from tkinter import *


#Primeras Variables

min = "abcdefghijklmnñopqrstuvwxyz"
may = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
num = "0123456789"
symbol = "@!;:.#$%&/\()=?¡¿" 
base = min + may + num + symbol #<--- Juntamos las minuscular, mayusculas, numeros y simbolos
long =  random.randrange(8, 12) #<--- Numero random o aleatorio de caracteres del 8 al 12

#Creacion de Contraseñas

bar1 = Bar('Procesando:', max=100)
tim = random.uniform(0.01, 0.1)
tim2 = str(tim)
print(tim2)
if(tim >= 0.08):
    time.sleep(0.9)
    print('Tiempo de carga elevado!\n Reintentando...')
    tim = random.uniform(0.01, 0.1)
    tim2 = str(tim)
    time.sleep(0.1)
    print("\n\n\n", tim2)    
if(tim >= 0.08):
    time.sleep(0.9)
    print('Tiempo de carga nuevamente elevado!\n Saliendo...')  
    now = str(datetime.now())
    ar = open('crash.txt', "w")
    ar.write(now + os.linesep)
    ar.write('Tiempo de carga: ' + tim2 + os.linesep)
    ar.write('Elevado a 0.08 Saliendo...')  
    ar.close()
    apperr2 = Tk()
    apperr2.title('ERROR')
    apperr2.geometry('400x400')
    lab = Label(apperr2, text="El tiempo de carga es elevado a 0.08!\nMas informacion en el archivo \"crash.txt\"")
    lab.pack(pady=150)
    apperr2.mainloop() 
    print('crash.txt creado')
    exit()
for num in range(100):
    time.sleep(tim)
    bar1.next()
bar1.finish()

for _ in range(10): #<--- Repeticion en 10
 #Creamos la muestra   
 muestra = random.sample(base, long)
 #Convertimos a "password"
 password = "".join(muestra)
 #Encriptamos la ultima "password"
 pass_en1 = generate_password_hash(password, 'pbkdf2:sha256:30', 30)

 print("password: ", password, "\n Encriptacion: ", pass_en1) #<--- Imprimimos en la consola las 10 contraseñas

# Hacemos que "Long" sea una String

long2 = str(long)

# A PARTIR DE AQUI SE USA LA ULTIMA CONTRASEÑA GENERADA

#password = 'A' #<--- Sirve para probar que la encriptacion sea Falsa (unicamente usar en caso de pruebas luego volver a poner el "#") 

# Chequeamos la Encriptacion y lo convertimos de Boolean a String

of = str(check_password_hash(pass_en1, password))

# Verificamos el chequeo de Encriptacion
if(of == 'True'): 
    of2 = 'Correcto' 


if(of == 'False'):
    nks = str(datetime.now())
    of2 = 'Error: La encriptacion no coincide con la contraseña'
    print('\nError: La encriptacion no coincide con la contraseña (contraseñas no seguras)!\n')
    ars = open('crash.txt', "w")
    ars.write(nks + os.linesep)
    ars.write('Error: La encriptacion no coincide con la ultima contraseña generada!' + os.linesep)
    ars.write('Saliendo...')
    ars.close()
    print('crash.txt creado')
    apperr = Tk()
    apperr.title('ERROR')
    apperr.geometry('400x400')
    lab = Label(apperr, text="La enciptacion no coincide con la ultima contraseña generada!\nMas informacion en el archivo \"crash.txt\"")
    lab.pack(pady=150)
    apperr.mainloop() 
    exit()

# Editamos arhivo

#Si la encriptacion es correcta
if(of == "True"): 
   file = open('pass.txt', 'w')
   file.write('Contraseña: ' + password + os.linesep)
   file.write('Caracteres de contraseña: ' + long2 + os.linesep)
   file.write('Encriptacion: ' + pass_en1 + os.linesep)
   file.write('Encriptacion comprobada: ' + of2 + " (contraseña segura)")
   file.close()

#Si la encriptacion es falsa (por el momento no se hace esta funcion)   
if(of == "False"):
    file = open('pass.txt', 'w')
    file.write('Error: La encriptacion no coincide con la contraseña (contraseñas no seguras)!')
    file.close()

# Datos de la contraseña en pass.txt
archiv = open('pass.txt', 'r')
cont = archiv.read()
print('\n\n\nFINALIZADO CORRECTAMENTE\n\n\nDatos de contraseña en pass.txt:\n',cont)
archiv.close()

app = Tk()
app.title('Generador de contraseñas')
app.geometry('300x400')
lab = Label(app, text="Tu contraseña generada es: \"" + password + "\"\nCaracteres: " + long2 + "\nEnciptacion Comprobada: " + of2 + "\n Mas informacion en el archivo \'pass.txt\'")
lab.pack(pady=150)
app.mainloop()

# --_CLOSE_--