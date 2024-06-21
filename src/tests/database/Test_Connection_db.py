from dotenv import load_dotenv

from src.database.Connection_db import Connection

# Cargar las variables de entorno desde el archivo ..env
load_dotenv()

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