class Stay:
    stay_counter = 0

    def __init__(self, stay_name, location, night_price, capacity, stay_type, image):
        Stay.stay_counter += 1
        self.id_stay = Stay.stay_counter
        self._stay_name = stay_name
        self._location = location
        self._night_price = night_price
        self._capacity = capacity
        self._type = stay_type
        self._image = image

    # Getters
    def get_stay_name(self):
        return self._stay_name

    def get_location(self):
        return self._location

    def get_night_price(self):
        return self._night_price

    def get_capacity(self):
        return self._capacity

    def get_type(self):
        return self._type

    def get_image(self):
        return self._image

    # Setters
    def set_stay_name(self, stay_name):
        self._stay_name = stay_name

    def set_location(self, location):
        self._location = location

    def set_night_price(self, night_price):
        self._night_price = night_price

    def set_capacity(self, capacity):
        self._capacity = capacity

    def set_type(self, stay_type):
        self._type = stay_type

    def set_image(self, image):
        self._image = image
