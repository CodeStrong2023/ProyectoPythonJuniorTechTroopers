from src.model.User import User

if __name__ == '__main__':
    usuario1 = User(1, 'user_name_user_1', 'password', 'nombre', 'apellido', 'email', 'documento', 'fecha_nacimiento',
                    25, 'telefono', 1000, True)
    print(usuario1.get_username())

    # ----------------------------------
    usuario2 = User.BuilderUser()
    print(usuario2._username)
