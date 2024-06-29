from src.utils.encription import Cifrado

if __name__ == '__main__':
    contrasenia1 = input("Ingrese la clave: ")
    encriptar1 = Cifrado.hash_password(contrasenia1)
    print("Contraseña encriptada: ", encriptar1)
    while True:
        contrasenia2 = input("Ingrese clave nuevante: ")
        desencriptar1 = Cifrado.check_password(contrasenia2, encriptar1)
        if desencriptar1:
            print("La contraseña es correcta")
            break
        else:
            print("La contraseña es incorrecta, intente nuevamente")
