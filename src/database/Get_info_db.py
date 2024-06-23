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

    def obtener_provincias(self):
        consulta = "SELECT provincia_id, nombre FROM DB_STAYS.Provincias"
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta)
                resultados = cursor.fetchall()

            # Convertir resultados a una lista de diccionarios
            provincias = [{'provincia_id': row[0], 'nombre': row[1]} for row in resultados]
            return provincias

        except Error as e:
            print(f"Error al obtener las provincias: {e}")
            return []

    def obtener_departamentos(self, provincia_id):
        consulta = "SELECT departamento_id, nombre FROM DB_STAYS.Departamentos WHERE provincia_id = %s"
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, (provincia_id,))
                resultados = cursor.fetchall()

            # Convertir resultados a una lista de diccionarios
            departamentos = [{'departamento_id': row[0], 'nombre': row[1]} for row in resultados]
            return departamentos

        except Error as e:
            print(f"Error al obtener los departamentos: {e}")
            return []

    def obtener_localidades(self, departamento_id):
        consulta = "SELECT localidad_id, nombre FROM DB_STAYS.Localidades WHERE departamento_id = %s"
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, (departamento_id,))
                resultados = cursor.fetchall()

            # Convertir resultados a una lista de diccionarios
            localidades = [{'localidad_id': row[0], 'nombre': row[1]} for row in resultados]
            return localidades

        except Error as e:
            print(f"Error al obtener las localidades: {e}")
            return []

    from mysql.connector import Error

    def obtener_id_localidad(self, nombre_localidad):
        consulta = "SELECT localidad_id FROM DB_STAYS.Localidades WHERE nombre = %s"
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, (nombre_localidad,))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado[0]  # Devuelve solo el ID de la localidad
                else:
                    return None  # Si no se encuentra la localidad con el nombre dado
        except Error as e:
            print(f"Error al obtener el ID de la localidad: {e}")
            return None

    def obtener_hospedajes_disponibles(self, province_id=None, departament_id=None, location_id=None, start_date=None, end_date=None):
        consulta = """
            SELECT *
            FROM DB_STAYS.Hosting AS _hosting 
            WHERE 
                (
                    _hosting.province_id = %s
                    OR _hosting.depart_id = %s
                    OR _hosting.location_id = %s
                )
                AND _hosting.state = 1
                AND (
                    SELECT 
                        COUNT(*)
                    FROM DB_STAYS.Rental_Register AS _rental 
                    WHERE _rental.hosting_id = _hosting.hosting_id
                        AND (
                            (_rental.start_date <= %s AND _rental.end_date >= %s)
                )
                
                )=0
            ;
        """
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, (province_id, departament_id, location_id, end_date, start_date))
                resultado = cursor.fetchall()

                orden = ''




        except Error as e:
            print(f"Error al obtener los hospedajes disponibles: {e}")
            return []