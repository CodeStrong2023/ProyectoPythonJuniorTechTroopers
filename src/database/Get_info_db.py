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

    
    def obtener_hospedajes_disponibles(self, province_id, departament_id, location_id, start_date, end_date):
        print('Función hospedaje get')

        consulta = f"""
            SELECT 
                 _hosting.hosting_id,
                 _hosting.owner_id,
                 _hosting.name_hosting,
                 _hosting.address,
                 _hosting.capacity,
                 _hosting.daily_cost,
                 _departamento.nombre,
                 _localidades.nombre,
                 CONCAT(_user.firstname, ' ', _user.lastname),
                 _user.email,
                 _localidades.localidad_id

            FROM DB_STAYS.Hosting AS _hosting 
                LEFT JOIN DB_STAYS.Departamentos AS _departamento 
                    ON _departamento.departamento_id = _hosting.depart_id

                LEFT JOIN DB_STAYS.Localidades AS _localidades
                    ON _localidades.localidad_id = _hosting.location_id

                LEFT JOIN DB_USERS.Usuarios AS _user
                    ON _user.user_id = _hosting.owner_id

            WHERE 
                _hosting.state = 1
                AND (
                    (_hosting.province_id = {province_id})
                    AND ({location_id if location_id is not None else "NULL"} IS NULL OR _hosting.location_id = {location_id if location_id is not None else "NULL"})
                    AND ({departament_id if departament_id is not None else "NULL"} IS NULL OR _hosting.depart_id = {departament_id if departament_id is not None else "NULL"})
                )
                AND (
                    SELECT COUNT(*)
                    FROM DB_STAYS.Rental_Register AS _rental 
                    WHERE _rental.hosting_id = _hosting.hosting_id
                        AND (
                            (_rental.start_date <= '{end_date}' AND _rental.end_date >= '{start_date}')
                        )
                ) = 0
            ;
        """

        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta)
                resultado = cursor.fetchall()
                return resultado if resultado else []
        except Error as e:
            print(f"Error al obtener los hospedajes disponibles: {e}")
            return []


    def informacion_hospedaje(self, owner_id):
        consulta = "SELECT hosting_id,  name_hosting FROM DB_STAYS.Hosting WHERE owner_id=%s"

        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, (owner_id,))
                resultados = cursor.fetchall()

            # Convertir resultados a una lista de diccionarios
            hospedajes = [{'hosting_id': row[0], 'name_hosting': row[1]} for row in resultados]

            return hospedajes

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []

    def informacion_hospedaje_completa(self, hosting_id):
        consulta = "SELECT hosting_id, name_hosting, address, location_id, capacity, daily_cost, state, province_id, depart_id FROM DB_STAYS.Hosting WHERE hosting_id=%s"
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, (hosting_id,))
                resultados = cursor.fetchall()

            # Convertir resultados a una lista de diccionarios
            hospedajes = [{'hosting_id': row[0], 'name_hosting': row[1], 'address': row[2], 'location_id': row[3],
                           'capacity': row[4], 'daily_cost': row[5], 'state': row[6], 'province_id': row[7],
                           'depart_id': row[8]} for row in resultados]

            return hospedajes

        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            return []

    def obtener_registros_activos(self, hosting_id):
        consulta = """
        SELECT COUNT(*)
        FROM DB_STAYS.Rental_Register
        WHERE hosting_id = %s AND end_date > CURRENT_DATE;
        """
        try:
            with self.conexion.cursor() as cursor:
                cursor.execute(consulta, (hosting_id,))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado[0]  # Devuelve el conteo de registros activos
                else:
                    return 0  # Si no hay registros, devuelve 0
        except Error as e:
            print(f"Error al obtener el conteo de registros: {e}")
            return None
