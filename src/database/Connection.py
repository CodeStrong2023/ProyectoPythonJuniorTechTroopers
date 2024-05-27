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

# Utilizando la clase Connection con Singleton para dos bases de datos
if __name__ == "__main__":
    # Conexión a la primera base de datos (DATABASE_USERS)
    db_connection_users = Connection("1")
    connection_users = db_connection_users.connect()

    # Ejemplo de operación: SELECT DATABASE() en la primera base de datos
    cursor_users = connection_users.cursor()
    cursor_users.execute("SELECT DATABASE();")
    record_users = cursor_users.fetchone()
    print("Conectado a la base de datos:", record_users)

    # Conexión a la segunda base de datos (DATABASE_STAIES)
    db_connection_stays = Connection("2")
    connection_stays = db_connection_stays.connect()

    # Ejemplo de operación: SELECT DATABASE() en la segunda base de datos
    cursor_stays = connection_stays.cursor()
    cursor_stays.execute("SELECT DATABASE();")
    record_stays = cursor_stays.fetchone()
    print("Conectado a la base de datos:", record_stays)

    # Cerrando las conexiones
    db_connection_users.close()
    db_connection_stays.close()