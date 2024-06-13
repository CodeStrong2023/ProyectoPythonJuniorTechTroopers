# src/model/SessionManager.py

from src.database.InsertInfo import InsertInfo
from src.utils.encription import Cifrado
from src.database.Getinfo import Getinfo

class SessionManager:
    """
    Clase para gestionar la sesión del usuario.

    Attributes:
        getinfo (Getinfo): Objeto para obtener información de la base de datos.
        insert_info (InsertInfo): Objeto para insertar información en la base de datos.
    """

    def __init__(self, db_key='1'):
        """
        Constructor de la clase.

        Args:
            db_key (str): Clave de la base de datos. Por defecto, '1'.
        """
        self.getinfo = Getinfo(db_key)
        self.insert_info = InsertInfo(db_key)

    def verificar_inicio_sesion(self, username, password):
        """
        Verifica el inicio de sesión del usuario.

        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña.

        Returns:
            tuple: Una tupla que indica si el inicio de sesión fue exitoso, el mensaje de estado y la información del usuario.
        """
        usuario_info, mensaje = self.getinfo.loguearse(username, password)
        if usuario_info:
            return True, "Inicio de sesión exitoso", usuario_info
        else:
            return False, "Usuario o contraseña incorrectos", None

    def registrar_usuario(self, datos_usuario):
        """
        Registra un nuevo usuario en la base de datos.

        Args:
            datos_usuario (dict): Datos del usuario a registrar.
        """
        datos_usuario['password'] = Cifrado.hash_password(datos_usuario['password'])
        datos_usuario['saldo'] = 0  # El saldo inicial es 0
        datos_usuario['activo'] = 1  # Usuario activo
        self.insert_info.insertar_usuario(datos_usuario)

    def salir_aplicacion(self, root):
        """
        Cierra la aplicación.

        Args:
            root: La ventana principal de la aplicación.
        """
        root.quit()
