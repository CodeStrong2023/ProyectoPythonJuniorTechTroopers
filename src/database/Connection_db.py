# Importamos las librerías necesarias
import os
import mysql.connector
from mysql.connector import Error


class Connection:
    """
    Clase Connection que implementa el patrón Singleton para gestionar conexiones a bases de datos.
    """

    _instances = {}

    def __new__(cls, db_key):
        """
        Método que controla la creación de nuevas instancias para cada base de datos específica.

        :param db_key: Clave identificadora de la base de datos (e.g., '1', '2').
        :return: Instancia única de la conexión para la base de datos especificada.
        """
        if db_key not in cls._instances:
            cls._instances[db_key] = super(Connection, cls).__new__(cls)
            cls._instances[db_key]._connection = None
            cls._instances[db_key]._db_key = db_key
        return cls._instances[db_key]

    def connect(self):
        """
        Método para establecer la conexión a la base de datos usando las credenciales especificadas en el archivo .env.

        :return: Objeto de conexión a la base de datos.
        """
        if self._connection is None or not self._connection.is_connected():
            try:
                self._connection = mysql.connector.connect(
                    host=os.getenv(f'DB_HOST_{self._db_key}'),
                    port=os.getenv(f'DB_PORT_{self._db_key}'),
                    user=os.getenv(f'DB_USER_{self._db_key}'),
                    password=os.getenv(f'DB_PASSWORD_{self._db_key}'),
                    database=os.getenv(f'DB_NAME_{self._db_key}')
                )
                if self._connection.is_connected():
                    print(f"Conexión exitosa a la base de datos {self._db_key}")
            except Error as e:
                print(f"Error al conectar a la base de datos {self._db_key}: {e}")
        return self._connection

    def close(self):
        """
        Método para cerrar la conexión a la base de datos si está abierta.
        """
        if self._connection is not None and self._connection.is_connected():
            self._connection.close()
            print(f"Conexión a la base de datos {self._db_key} cerrada")
