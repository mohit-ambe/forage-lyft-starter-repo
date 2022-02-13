class CarriganTires:

    def __init__(self, tire_wear):
        self.__tire_wear = tire_wear

    def needs_service(self):
        for number in self.__tire_wear:
            if number >= 0.9:
                return True
        return False
