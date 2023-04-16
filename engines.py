class Engine:

    def __init__(self, model: str, power: str):
        self.__model = model
        self.__power = power
        self.__error_list = []

    def __str__(self):
        return f"Модель: {self.__model}, Мощность: {self.__power}"

    @property
    def model(self):
        return self.__model

    @property
    def power(self):
        return self.__power

    @property
    def error_list(self):
        if not self.__error_list:
            return
        return self.__error_list


    def add_error(self, error_code: str):
        self.__error_list.append(error_code)