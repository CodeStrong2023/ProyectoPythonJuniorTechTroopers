class User:
    def __init__(self, usuario_id, username, password, nombre, apellido, email, documento, fecha_nacimiento, edad, telefono, saldo, activo):
        self.usuario_id = usuario_id
        self._username = username
        self._password = password
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._documento = documento
        self._fecha_nacimiento = fecha_nacimiento
        self._edad = edad
        self._telefono = telefono
        self._saldo = saldo
        self._activo = activo
    # Getters
    def get_usuario_id(self):
        return self._usuario_id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_email(self):
        return self._email

    def get_documento(self):
        return self._documento

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def get_edad(self):
        return self._edad

    def get_telefono(self):
        return self._telefono

    def get_saldo(self):
        return self._saldo

    def get_activo(self):
        return self._activo

    # Setters
    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def set_email(self, email):
        self._email = email

    def set_documento(self, documento):
        self._documento = documento

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def set_edad(self, edad):
        self._edad = edad

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_saldo(self, saldo):
        self._saldo = saldo

    def set_activo(self, activo):
        self._activo = activo

    # Para aplicar el método Builder en la clase Start,
    # primero necesitamos entender que el patrón Builder
    # se utiliza para construir un objeto paso a paso.
    # Es particularmente útil cuando se trata de objetos que requieren muchos
    # parámetros para su construcción y estos parámetros no son siempre necesarios.
    class BuilderUser:
        def __init__(self):
            self._usuario_id = None
            self._username = None
            self._password = None
            self._nombre = None
            self._apellido = None
            self._email = None
            self._documento = None
            self._fecha_nacimiento = None
            self._edad = None
            self._telefono = None
            self._saldo = None
            self._activo = None

        def set_usuario_id(self, usuario_id):
            self._usuario_id = usuario_id
            return self

        def set_username(self, username):
            self._username = username
            return self

        def set_password(self, password):
            self._password = password
            return self

        def set_nombre(self, nombre):
            self._nombre = nombre
            return self

        def set_apellido(self, apellido):
            self._apellido = apellido
            return self

        def set_email(self, email):
            self._email = email
            return self

        def set_documento(self, documento):
            self._documento = documento
            return self

        def set_fecha_nacimiento(self, fecha_nacimiento):
            self._fecha_nacimiento = fecha_nacimiento
            return self

        def set_edad(self, edad):
            self._edad = edad
            return self

        def set_telefono(self, telefono):
            self._telefono = telefono
            return self

        def set_saldo(self, saldo):
            self._saldo = saldo
            return self

        def set_activo(self, activo):
            self._activo = activo
            return self



        def build(self):
            return User(self._usuario_id, self._username, self._password, self._nombre, self._apellido, self._email, self._documento,
                        self._fecha_nacimiento, self._edad, self._telefono, self._saldo, self._activo)

"""
if __name__ == '__main__':
    usuario1 = User(1,"","","","","","",1,0)
    print(usuario1.get_user_name())


    # ----------------------------------
    usuario2 = User.BuilderUser()
    print(usuario2._username)
"""