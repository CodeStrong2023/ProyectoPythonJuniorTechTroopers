class User:
    def __init__(self, id, username, password, email, first_name, last_name, age, phone, cash):
        self._id = id
        self._username = username
        self._password = password
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._age = age
        self._phone = phone
        self._cash = cash

    # Getters
    def get_id(self):
        return self._id

    def get_user_name(self):
        return self._username

    def get_password(self):
        return self._password

    def get_email(self):
        return self._email

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_age(self):
        return self._age

    def get_phone(self):
        return self._phone

    def get_cash(self):
        return self._cash

    # Setters
    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_email(self, email):
        self._email = email

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_age(self, age):
        self._age = age

    def set_phone(self, phone):
        self._phone = phone

    def set_cash(self, cash):
        self._cash = cash

    # Para aplicar el método Builder en la clase Start,
    # primero necesitamos entender que el patrón Builder
    # se utiliza para construir un objeto paso a paso.
    # Es particularmente útil cuando se trata de objetos que requieren muchos
    # parámetros para su construcción y estos parámetros no son siempre necesarios.
    class BuilderUser:
        def __init__(self):
            self._id = None
            self._username = None
            self._password = None
            self._email = None
            self._first_name = None
            self._last_name = None
            self._age = None
            self._phone = None
            self._cash = None

        def set_id(self, id):
            self._id = id
            return self

        def set_username(self, username):
            self._username = username
            return self

        def set_password(self, password):
            self._password = password
            return self

        def set_email(self, email):
            self._email = email
            return self

        def set_first_name(self, first_name):
            self._first_name = first_name
            return self

        def set_last_name(self, last_name):
            self._last_name = last_name
            return self

        def set_age(self, age):
            self._age = age
            return self

        def set_phone(self, phone):
            self._phone = phone
            return self

        def set_cash(self, cash):
            self._cash = cash
            return self

        def build(self):
            return User(self._id, self._username, self._password, self._email, self._first_name, self._last_name,
                        self._age, self._phone, self._cash)

"""
if __name__ == '__main__':
    usuario1 = User(1,"","","","","","",1,0)
    print(usuario1.get_user_name())


    # ----------------------------------
    usuario2 = User.BuilderUser()
    print(usuario2._username)
"""