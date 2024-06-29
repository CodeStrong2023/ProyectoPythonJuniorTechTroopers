# src/utils/EmailVerification.py

import os
import re
import random
import smtplib
from email.message import EmailMessage


class EmailVerification:
    """
    Clase para la verificación de correos electrónicos y el envío de códigos de verificación.

    Attributes:
        email (str): Dirección de correo electrónico para enviar mensajes.
        password (str): Contraseña del correo electrónico.
        conexion: Conexión SMTP para el envío de correos electrónicos.
        codigo_aleatorio (int): Código de verificación generado aleatoriamente.
    """

    def __init__(self):
        """
        Constructor de la clase.
        """
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('KEY')
        self.conexion = None
        self.codigo_aleatorio = None

    def generar_codigo_aleatorio(self):
        """
        Genera un código de verificación aleatorio de seis dígitos.

        Returns:
            int: Código de verificación generado.
        """
        self.codigo_aleatorio = random.randint(100000, 999999)
        return self.codigo_aleatorio

    def es_correo_valido(self, correo):
        """
        Verifica si la dirección de correo electrónico proporcionada es válida.

        Args:
            correo (str): Dirección de correo electrónico a verificar.

        Returns:
            bool: True si la dirección de correo electrónico es válida, False de lo contrario.
        """
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, correo)

    def conectar_smtp(self):
        """
        Establece una conexión SMTP con el servidor de correo electrónico.
        """
        self.conexion = smtplib.SMTP(host='smtp.gmail.com', port=587)
        self.conexion.starttls()
        self.conexion.login(user=self.email, password=self.password)

    def enviar_correo(self, correo_destino):
        """
        Envía un correo electrónico con el código de verificación al destinatario.

        Args:
            correo_destino (str): Dirección de correo electrónico del destinatario.

        Raises:
            ValueError: Si la dirección de correo electrónico no es válida.
        """
        if not self.es_correo_valido(correo_destino):
            raise ValueError("Correo electrónico no válido, por favor ingrésalo nuevamente")

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

    def cerrar_conexion(self):
        """
        Cierra la conexión SMTP.
        """
        if self.conexion:
            self.conexion.quit()

    def verificar_codigo(self, codigo_ingresado):
        """
        Verifica si el código ingresado coincide con el código de verificación generado.

        Args:
            codigo_ingresado (str): Código ingresado por el usuario.

        Returns:
            bool: True si el código ingresado es correcto, False de lo contrario.
        """
        return str(codigo_ingresado) == str(self.codigo_aleatorio)
