from CapuletEngine import CapuletEngine
from WilloughbyEngine import WilloughbyEngine
from SternmanEngine import SternmanEngine

from SpindlerBattery import SpindlerBattery
from NubbinBattery import NubbinBattery

from Car import Car


class CarFactory:
    __engine = None
    __battery = None

    def __init__(self):
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.__engine = CapuletEngine(last_service_mileage, current_mileage)
        self.__battery = SpindlerBattery(last_service_date, current_date)
        return Car(self.__engine, self.__battery)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.__engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.__battery = SpindlerBattery(last_service_date, current_date)
        return Car(self.__engine, self.__battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        self.__engine = StermanEngine(warning_light_on)
        self.__battery = SpindlerBattery(last_service_date, current_date)
        return Car(self.__engine, self.__battery)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.__engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.__battery = NubbinBattery(last_service_date, current_date)
        return Car(self.__engine, self.__battery)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.__engine = CapuletEngine(last_service_mileage, current_mileage)
        self.__battery = NubbinBattery(last_service_date, current_date)
        return Car(self.__engine, self.__battery)
