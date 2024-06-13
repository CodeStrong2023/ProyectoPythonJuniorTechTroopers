class SingletonUser:
    _instance = None

    def __new__(cls):
        if not SingletonUser._instance:
            SingletonUser._instance = super(SingletonUser, cls).__new__(cls)
        return SingletonUser._instance

    def __init__(self, user_name="", password="", email="", first_name="", last_name="", edad=0, phone="", saldo=0.0):
        if SingletonUser._instance is not None:
            raise Exception("SingletonUser class can only have one instance.")
        self.user_name = user_name
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.edad = edad
        self.phone = phone
        self.saldo = saldo

    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, new_user_name):
        self._user_name = new_user_name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password
