import smtplib
import random
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import re

class EmailVerification:
    def __init__(self):

# Carga de las variables de entorno desde un archivo .env
        load_dotenv()
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('KEY')
        self.conexion = None

#Método que genera un código aleatorio de 6 dígitos
    def generar_codigo_aleatorio(self):
        return random.randint(100000, 999999)

#Validación para ver si el formato de correo es correcto
    def es_correo_valido(self, correo):
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, correo)

#Establece la conexión con el servidor SMTP y realiza la autenticación
    def conectar_smtp(self):
        self.conexion = smtplib.SMTP(host='smtp.gmail.com', port=587)
        self.conexion.starttls()
        self.conexion.login(user=self.email, password=self.password)

#Creación y envio del correo electrónico con el código de verificación
    def enviar_correo(self, correo_destino):
        if not self.es_correo_valido(correo_destino):
            raise ValueError("Correo electrónico no válido, por favor ingresalo nuevamente")

        codigo_aleatorio = self.generar_codigo_aleatorio()
        asunto = 'Validación'
        contenido = f'Bienvenido, tu código de verificación es: {codigo_aleatorio}'
        mensaje = EmailMessage()
        mensaje['From'] = self.email
        mensaje['To'] = correo_destino
        mensaje['Subject'] = asunto
        mensaje.set_content(contenido)

        self.conexion.send_message(mensaje)
        print("Correo enviado exitosamente!")

#Cierre de la conexión con el servidor SMPT
    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.quit()

#Uso de la clase
if __name__ == "__main__":
    email_verification = EmailVerification()
    email_verification.conectar_smtp()
    try:
        correo_destino = input("Ingresa el correo del destinatario: ")
        email_verification.enviar_correo(correo_destino)
    except ValueError as e:
        print(e)
    finally:
        email_verification.cerrar_conexion()