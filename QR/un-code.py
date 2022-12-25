import qrcode
from PIL import Image
import pyzbar.pyzbar as pyzbar

def decode_qr(input_file):
  # Abrir la imagen del QR code
  img = Image.open(input_file)

  # Leer los datos del QR code
  decoded_data = pyzbar.decode(img)

  # Devolver los datos decodificados
  return decoded_data[0].data.decode()

nombre = input("¿Como se llama el archivo de QR? (sin la extencion .png): ")

decoded_data = decode_qr(nombre + ".png")
print("El texto o link del QR es: ", decoded_data)  # Imprimirá el contenido del QR code

listo = input("Presione una tecla para continuar: ") 

