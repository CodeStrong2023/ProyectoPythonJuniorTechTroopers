# src/utils/Getinfo.py

import mysql.connector
from mysql.connector import Error
from src.database.Connection import Connection
from src.utils.encription import Cifrado  # Asegurándonos que la clase Cifrado esté en utils

class Getinfo:
    def __init__(self, db_key='1'):
        self.conexion = Connection(db_key).connect()

    def loguearse(self, username, password):
        sql = "SELECT usuario_id, username, saldo, password FROM Usuarios WHERE username = %s"
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (username,))
            resultSet = cursor.fetchone()
            cursor.close()

            if not resultSet:
                return None, "Usuario incorrecto"

            hashed_password_db = resultSet[3]

            if Cifrado.check_password(password, hashed_password_db):
                user = {
                    'usuario_id': resultSet[0],
                    'username': resultSet[1],
                    'saldo': resultSet[2]
                }
                return user, "Inicio de sesión exitoso"
            else:
                return None, "Contraseña incorrecta"

        except Error as e:
            print(f"Error al intentar iniciar sesión: {e}")
            return None, "Error de conexión"

    def verificar_usuario(self, username):
        sql = "SELECT username FROM Usuarios WHERE username = %s"
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (username,))
            resultSet = cursor.fetchone()
            cursor.close()

            return resultSet is not None

        except Error as e:
            print(f"Error al verificar el usuario: {e}")
            return False
