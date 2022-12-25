import qrcode
from PIL import Image
from tkinter import *

# Codificar un QR code
def encode_qr(data, output_file):
  # Crear el objeto QR code
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
  )
  # Agregar los datos al QR code
  qr.add_data(data)
  qr.make(fit=True)

  # Crear la imagen del QR code y guardarla en el archivo de salida
  img = qr.make_image(fill_color="black", back_color="white")
  img.save(output_file)

# Decodificar un QR code
def decode_qr(input_file):
  # Abrir la imagen del QR code
  img = Image.open(input_file)

  # Leer los datos del QR code
  qr = qrcode.QRCode()
  qr.scan(img)

  # Devolver los datos decodificados
  return qr.data

texto = input('Pon lo que quieres pasar a QR: ')
nombre = input('¿Como quieres que se llame el archivo.png? (si tiene el mismo nombre que otro se reemplazara): ')

app = Tk()
app.title('QR GENERADO')
app.geometry('400x400')
lab = Label(app, text="QR Generado con el nombre: '" + nombre + "' "  )
lab.pack(pady=150)
app.mainloop() 

encode_qr(texto, nombre + ".png")

