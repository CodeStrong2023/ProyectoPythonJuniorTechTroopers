from Principal.Stay import Stay


class StayBuilder:
    def __init__(self):
        self._stay_name = None
        self._location = None
        self._night_price = None
        self._capacity = None
        self._type = None
        self._image = None

    def set_stay_name(self, stay_name):
        self._stay_name = stay_name
        return self

    def set_location(self, location):
        self._location = location
        return self

    def set_night_price(self, night_price):
        self._night_price = night_price
        return self

    def set_capacity(self, capacity):
        self._capacity = capacity
        return self

    def set_type(self, stay_type):
        self._type = stay_type
        return self

    def set_image(self, image):
        self._image = image
        return self

    def build(self):
        return Stay(self._stay_name, self._location, self._night_price, self._capacity, self._type, self._image)

