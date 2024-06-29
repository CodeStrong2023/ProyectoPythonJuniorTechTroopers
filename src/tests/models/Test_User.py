from src.model.User import User

if __name__ == '__main__':
    usuario1 = User(1, 'user_name_user_1', 'password', 'firstname', 'lastname', 'email', 'birthdate',
                    25, 'phone', 1000, True)
    print(usuario1.get_username())

    # ----------------------------------
    usuario2 = User.BuilderUser()
    print(usuario2._username)
