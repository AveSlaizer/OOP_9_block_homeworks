from math import pi


"""
Задание 1.
Создайте класс Circle (окружность). Для данного класса реализуйте ряд
перегруженных операторов:
Проверка на равенство радиусов двух окружностей (операция ==, !=);
Проверка сравнения длин двух окружностей (операции >, <, <=,>=);
Пропорциональное изменение размеров окружности, путем изменения
ее радиуса (операции + - += -=)
"""


class Circle:
    def __init__(self, radius: int):
        self.__radius = radius

    def calc_circumference_length(self):
        self.__length = self.__radius * 2 * pi
        return self.__length

    @property
    def radius(self):
        return self.__radius

    @property
    def lenght(self):
        return self.__length

    def __is_circle(self, other: object):
        if not isinstance(other, Circle):
            raise TypeError(f"Невозможно выполнить сравнение между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __hash__(self):
        return hash(self.__radius)

    def __eq__(self, other):
        self.__is_circle(other)
        return self.__radius == other.__radius

    def __ne__(self, other):
        self.__is_circle(other)
        return self.__radius != other.__radius

    def __lt__(self, other):
        self.__is_circle(other)
        return self.__length < other.__length

    def __le__(self, other):
        self.__is_circle(other)
        return self.__length <= other.__length

    def __gt__(self, other):
        self.__is_circle(other)
        return self.__length > other.__length

    def __ge__(self, other):
        self.__is_circle(other)
        return self.__length >= other.__length


def execute_application():

     pass


if __name__ == "__main__":
    execute_application()
