# src/utils/Get_info_db.py

import mysql.connector
from mysql.connector import Error
from src.database.Connection_db import Connection
from src.model.User import User
from src.utils.encription import Cifrado  # Asegurándonos que la clase Cifrado esté en utils


class Getinfo:
    def __init__(self, username="", db_key='1'):
        self.conexion = Connection(db_key).connect()
        self.username=username

    def loguearse(self, username, password):
        sql = "SELECT user_id, username, money, password FROM Usuarios WHERE username = %s"
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
                    'user_id': resultSet[0],
                    'username': resultSet[1],
                    'money': resultSet[2]
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

            return resultSet is not None

        except Error as e:
            print(f"Error al verificar el usuario: {e}")
            return False

    def informacion_panel(self, username):
        consulta = "SELECT user_id, username,email, firstname, lastname, money FROM Usuarios WHERE username=%s"
        try:
            cursor = self.conexion.cursor()

            cursor.execute(consulta, (username,))
            resultado = cursor.fetchone()
            cursor.close()

            # Y ahora esta asi
            usuario = (
                User.BuilderUser()
                .set_usuario_id(resultado[0])
                .set_username(resultado[1])
                .set_email(resultado[2])
                .set_firstname(resultado[3])
                .set_lastname(resultado[4])
                .set_money(resultado[5])
                .build()
            )
            return usuario

        except Error as e:
            print(f"Error al validar las credenciales: {e}")
            return False
