from math import pi
"""
Задание 1.
Создайте класс Circle (окружность). Для данного класса реализуйте ряд
перегруженных операторов:
Проверка на равенство радиусов двух окружностей (операция ==, !=);
Проверка сравнения длин двух окружностей (операции >, <, <=,>=);
"""

class Circle:

    def __init__(self, radius: int):
        self.__radius = radius
        self.__length = self.__calc_circumference_length()

    def __calc_circumference_length(self):
        return self.__radius * 2 * pi

    @property
    def radius(self):
        return self.__radius

    @property
    def lenght(self):
        return self.__length

def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
