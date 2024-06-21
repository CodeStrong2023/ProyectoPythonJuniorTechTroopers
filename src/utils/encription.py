import bcrypt


class Cifrado:
    # TODO pip install bcrypt

    @staticmethod
    def hash_password(password: str) -> str:
        """
        :param password:recibimos la contraseña como string
        :return: y retornamos la contraseña como bytes
        """
        # Convertir la contraseña a bytes con escritura utf-8
        password_bytes = password.encode('utf-8')

        # Generar una sal (salt) aleatoria (salto aleatorio)
        salt = bcrypt.gensalt()

        # Generar el hash de la contraseña
        hashed_password = bcrypt.hashpw(password_bytes, salt)

        # Convertir el hash a cadena de texto para almacenamiento en la base de datos
        hashed_password_db = hashed_password.decode('utf-8')

        return hashed_password_db

    @staticmethod
    def check_password(password: str, hashed_password_db: str) -> bool:
        """

        :param password: contraseña ingresada
        :param hased_password_db: contraseña haseada
        :return: retornamos un booleno de su verificación
        """
        # Convertir la contraseña a bytes con escritura utf-8
        password_bytes = password.encode('utf-8')

        # Convertir la contraseña hasheada almacenada a bytes
        hashed_password_bytes = hashed_password_db.encode('utf-8')

        # Verificamos la contraseña
        return bcrypt.checkpw(password_bytes, hashed_password_bytes)