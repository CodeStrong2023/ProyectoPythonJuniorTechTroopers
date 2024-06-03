import bcrypt


# TODO pip install bcrypt
def hash_password(password: str) -> bytes:
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


if __name__ == '__main__':
    contraseña1 = input("Ingrese la clave: ")
    encriptar1 = hash_password(contraseña1)
    print("Contraseña encriptada: ", encriptar1)
    while True:
        contraseña2 = input("Ingrese clave nuevante: ")
        desencriptar1 = check_password(contraseña2, encriptar1)
        if desencriptar1:
            print("La contraseña es correcta")
            break
        else:
            print("La contraseña es incorrecta, intente nuevamente")
