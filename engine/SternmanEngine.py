from engine.Engine import Engine


class SternmanEngine(Engine):

    def __init__(self, warning_light_on):
        self.__warning_light_on = warning_light_on

    def needs_service(self):
        if self.__warning_light_on:
            self.__warning_light_on = False
            return True
        else:
            return False
