# src/utils/Getinfo.py

from mysql.connector import Error

def validar_credenciales(conexion, usuario, contraseña):
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM USERS WHERE USERNAME = %s AND PASSWORD = %s"
        cursor.execute(consulta, (usuario, contraseña))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado is not None
    except Error as e:
        print(f"Error al validar las credenciales: {e}")
        return False


