class Engine:

    def __init__(self, model: str, power: str, fuel_type: str):
        self.__model = model
        self.__power = power
        self.__fuel_type = fuel_type
        self.__error_list = []

    def __str__(self):
        return f"Модель: {self.__model}, мощность: {self.__power}, используемое топливо: {self.__fuel_type}"

    @property
    def error_list(self):
        return self.__error_list

    def add_error(self, error_code: str):
        self.__error_list.append(error_code)

    def get_failure_status(self):
        if not self.__error_list:
            return "Ошибки не обнаружены, двигатель работает в штатном режиме"
        return "Обнаружены ошибки в работе двигателя, обратитесь в сервисный центр"


class GasEngine(Engine):
    pass


class DieselEngine(Engine):
    pass


class ElectricalEngine(Engine):
    pass


# Миксин
class FailureStatus:

    @staticmethod
    def print_failure_status(engine: Engine):
        if engine.error_list:
            print(f"Коды ошибок: {engine.error_list}")
        print(engine.get_failure_status())
