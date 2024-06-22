class User:
    def __init__(self, user_id, username, password, firstname , lastname, email, birthdate, age, phone, money, active):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._birthdate = birthdate
        self._age = age
        self._phone = phone
        self._money = money
        self._active = active
    # Getters

    def get_user_id(self):
        return self._user_id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_firstname(self):
        return self._firstname

    def get_lastname(self):
        return self._lastname

    def get_email(self):
        return self._email

    def get_birthdate(self):
        return self._birthdate

    def get_age(self):
        return self._age

    def get_phone(self):
        return self._phone

    def get_money(self):
        return self._money

    def get_activo(self):
        return self._active

    # Setters
    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_firstname(self, firstname):
        self._firstname = firstname

    def set_lastname(self, lastname):
        self._lastname = lastname

    def set_email(self, email):
        self._email = email

    def set_birthdate(self, birthdate):
        self._birthdate = birthdate

    def set_age(self, age):
        self._age = age

    def set_phone(self, phone):
        self._phone = phone

    def set_money(self, money):
        self._money = money

    def set_active(self, active):
        self._active = active

    # Para aplicar el método Builder en la clase Start,
    # primero necesitamos entender que el patrón Builder
    # se utiliza para construir un objeto paso a paso.
    # Es particularmente útil cuando se trata de objetos que requieren muchos
    # parámetros para su construcción y estos parámetros no son siempre necesarios.
    class BuilderUser:
        def __init__(self):
            self._user_id = None
            self._username = None
            self._password = None
            self._firstname = None
            self._lastname = None
            self._email = None
            self._birthdate = None
            self._age = None
            self._phone = None
            self._money = None
            self._active = None

        def set_usuario_id(self, usuario_id):
            self._usuario_id = usuario_id
            return self

        def set_username(self, username):
            self._username = username
            return self

        def set_password(self, password):
            self._password = password
            return self

        def set_firstname(self, firstname):
            self._firstname = firstname
            return self

        def set_lastname(self, lastname):
            self._lastname = lastname
            return self

        def set_email(self, email):
            self._email = email
            return self

        def set_birthdate(self, birthdate):
            self._birthdate = birthdate
            return self

        def set_age(self, age):
            self._age = age
            return self

        def set_phone(self, phone):
            self._phone = phone
            return self

        def set_money(self, money):
            self._money = money
            return self

        def set_active(self, active):
            self._active = active
            return self



        def build(self):
            return User(self._usuario_id, self._username, self._password, self._firstname, self._lastname, self._email,
                        self._birthdate, self._age, self._phone, self._money, self._active)

