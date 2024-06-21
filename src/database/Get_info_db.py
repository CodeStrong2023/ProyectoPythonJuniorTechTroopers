# src/utils/Get_info_db.py

import mysql.connector
from mysql.connector import Error
from src.database.Connection_db import Connection
from src.model.User import User
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

            return resultSet is not None

        except Error as e:
            print(f"Error al verificar el usuario: {e}")
            return False

    def informacion_panel(self, username):
        consulta = "SELECT usuario_id, username,email, nombre, apellido,saldo FROM Usuarios WHERE username=%s"
        try:
            cursor = self.conexion.cursor()

            cursor.execute(consulta, (username,))
            resultado = cursor.fetchone()
            cursor.close()

            """
                        usuario = User.BuilderUser.build()
                        usuario.set_username(resultado[0])
                        usuario.set_email(resultado[1])
                        usuario.set_nombre(resultado[2])
                        usuario.set_apellido(resultado[3])
                        usuario.set_saldo(resultado[4])
            """
            # Y ahora esta asi
            usuario = (
                User.BuilderUser()
                .set_usuario_id(resultado[0])
                .set_username(resultado[1])
                .set_email(resultado[2])
                .set_nombre(resultado[3])
                .set_apellido(resultado[4])
                .set_saldo(resultado[5])
                .build()
            )
            return usuario

        except Error as e:
            print(f"Error al validar las credenciales: {e}")
            return False
