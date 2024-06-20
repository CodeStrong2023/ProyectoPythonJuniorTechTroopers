# src/database/InsertInfo.py

import mysql.connector
from mysql.connector import Error
from src.database.Connection import Connection


class InsertInfo:
    """
    Clase para insertar información de usuario en la base de datos.

    Attributes:
        conexion: Conexión a la base de datos.
    """
    def __init__(self, db_key='1'):
        """
        Constructor de la clase.

        Args:
            db_key (str): Clave de la base de datos.
        """
        self.conexion = Connection(db_key).connect()

    def insertar_usuario(self, datos_usuario):
        """
        Inserta los datos de un usuario en la base de datos.

        Args:
            datos_usuario (dict): Datos del usuario a insertar.

        Raises:
            pymysql.Error: Si ocurre un error durante la inserción de datos.
        """
        sql = """
        INSERT INTO Usuarios (username, password, nombre, apellido, email, documento, fecha_nacimiento, edad, telefono, saldo, activo)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (
                datos_usuario['username'],
                datos_usuario['password'],
                datos_usuario['nombre'],
                datos_usuario['apellido'],
                datos_usuario['email'],
                datos_usuario['documento'],
                datos_usuario['fecha_nacimiento'],
                datos_usuario['edad'],
                datos_usuario['telefono'],
                datos_usuario['saldo'],
                datos_usuario['activo']
            ))
            self.conexion.commit()
            cursor.close()
        except Error as e:
            print(f"Error al insertar usuario: {e}")
            self.conexion.rollback()

