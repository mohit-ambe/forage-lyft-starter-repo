class OctoprimeTires:

    def __init__(self, tire_wear):
        self.__tire_wear = tire_wear

    def needs_service(self):
        sum = 0
        for number in self.__tire_wear:
            sum += number
        if sum >= 3:
            return True
        else:
            return False
