from engine.Battery import Battery


class NubbinBattery(Battery):

    def __init__(self, last_service_date, current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        if self.__current_date - self.__last_service_date >= (4 * 365):
            return True
        else:
            return False
