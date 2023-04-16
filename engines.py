class Engine:

    def __init__(self, model: str, power: str):
        self.__model = model
        self.__power = power
        self.__error_list = []

    def __str__(self):
        return f"Модель: {self.__model}, Мощность: {self.__power}"

    def add_error(self, error_code: str):
        self.__error_list.append(error_code)

    def get_failure_status(self):
        if not self.__error_list:
            return "Ошибки не обнаружены, двигатель работает в штатном режиме"
        return "Обнаружены ошибки в работе двигателя, обратитесь в сервисный центр"
