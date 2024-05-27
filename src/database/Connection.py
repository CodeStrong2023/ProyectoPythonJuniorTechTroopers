# Importamos las librerías necesarias
import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

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