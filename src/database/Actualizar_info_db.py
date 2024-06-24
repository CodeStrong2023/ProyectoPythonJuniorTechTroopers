from aifc import Error
from mysql.connector import Error
from src.database.Connection_db import Connection
class ActualizarInfo:

    def __init__(self, db_key='2'):
        self.conexion = Connection(db_key).connect()


    def actualizar_hospedaje(self, datos_hospedaje):
        sql = """
                UPDATE DB_STAYS.Hosting
                SET owner_id = %s,
                    name_hosting = %s,
                    address = %s,
                    location_id = %s,
                    depart_id = %s,
                    province_id = %s,
                    capacity = %s,
                    daily_cost = %s,
                    state = %s
                WHERE hosting_id = %s
                """
        try:
            cursor = self.conexion.cursor()
            cursor.execute(sql, (
                datos_hospedaje['owner_id'],
                datos_hospedaje['name_hosting'],
                datos_hospedaje['address'],
                datos_hospedaje['location_id'],
                datos_hospedaje['depart_id'],
                datos_hospedaje['province_id'],
                datos_hospedaje['capacity'],
                datos_hospedaje['daily_cost'],
                datos_hospedaje['state'],
                datos_hospedaje['hosting_id'],
            ))
            self.conexion.commit()
            cursor.close()
            print("Hospedaje actualizado correctamente.")
        except Error as e:
            print(f"Error al actualizar hospedaje: {e}")
            self.conexion.rollback()
