import smtplib
import random
from email.message import EmailMessage
from dotenv import load_dotenv
import os


# Carga de variables de entorno
load_dotenv()
email = os.getenv('EMAIL')
password = os.getenv('KEY')

# Método que genera un código aleatorio de 6 dígitos
def generar_codigo_aleatorio():
    return random.randint(100000, 999999)


# Establecemos conexión al servidor de correos SMTP
conexion = smtplib.SMTP(host='smtp.gmail.com', port=587)  # Viene dado por default al usar Gmail


# Información de inicio de sesión y correos como variables
usuario = 'EMAIL' #Agregar correo en .env
contraseña = 'KEY' #Agregar password en .env
correo_destino = input("Ingresar correo del destinatario: ")


# Encriptación TLS
conexion.starttls() #Encriptación TLS para asegurar que la conexión sea segura

# Iniciamos sesión en el servidor SMTP
conexion.login(user=email, password=password)

# Creamos variable del método de generacién del código aleatorio
codigo_aleatorio = generar_codigo_aleatorio()

# Info del mensaje como variable
remitente = usuario
destinatario = correo_destino
asunto = 'Validación '
contenido = f'Bienvenido, tu código de verificación es: {codigo_aleatorio}'

# Creamos el cuerpo del mensaje
mensaje = EmailMessage()
mensaje['From'] = remitente
mensaje['To'] = destinatario
mensaje['Subject'] = asunto
mensaje.set_content(contenido)

# Enviamos el correo con el mensaje que queremos
conexion.send_message(mensaje)

# Ahora finalizamos la conexión del servidor SMTP
conexion.quit()