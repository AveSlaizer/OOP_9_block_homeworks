"""
Задание 1.
Создайте класс «Самолет». Наполните его необходимыми характеристиками и методами. Реализуйте упаковку и
распаковку объектов класса «Самолет» с использованием
модуля pickle.
"""


class AirPlane:

    def __init__(self, name: str, engine_type: str, engine_qty: int):
        self.__name = name
        self.__engine_type = engine_type
        self.__engine_qty = engine_qty

    def __str__(self):
        return f"{self.__name}, тип двигателей: {self.__engine_type}, количество двигателей: {self.__engine_qty}"

    @property
    def name(self):
        return self.__name

    @property
    def engine_type(self):
        return self.__engine_type

    @property
    def engine_qty(self):
        return self.__engine_qty


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
