from math import pi
from typing import Union


"""
Задание 1.
Создайте класс Circle (окружность). Для данного класса реализуйте ряд
перегруженных операторов:
Проверка на равенство радиусов двух окружностей (операция ==, !=);
Проверка сравнения длин двух окружностей (операции >, <, <=,>=);
Пропорциональное изменение размеров окружности, путем изменения
ее радиуса (операции + - += -=)
"""
class InitializationCircleError(Exception):

    def __init__(self, text: str):
        self.text = text


class Circle:
    def __init__(self, radius: Union[int, float]):
        if radius <= 0:
            raise InitializationCircleError("Ошибка инициализации окружности. "
                                            "Радиус не может быть меньше или равен нулю")
        self.__radius = radius
        self.__length = None

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
            raise TypeError(f"Невозможно выполнить сравнение между типом \'{self.__class__.__name__}\' "
                            f"и \'{other.__class__.__name__}\'")

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

    def __add__(self, other):
        if isinstance(other, Union[int, float]):
            new_radius = self.__radius + other
            new_circle = Circle(new_radius)
            if not self.__length is None:
                new_circle.calc_circumference_length()
            return new_circle
        raise TypeError(f"Невозможно выполнить операцию сложения "
                        f"между типом \'{self.__class__.__name__}\' "
                        f"и \'{other.__class__.__name__}\'")

    def __iadd__(self, other):
        if isinstance(other, Union[int, float]):
            self.__radius = self.__radius + other
            if self.__radius <= 0:
                raise InitializationCircleError("Ошибка инициализации окружности. "
                                                "Радиус не может быть меньше или равен нулю")
            if not self.__length is None:
                self.calc_circumference_length()
            return self
        raise TypeError(f"Невозможно выполнить операцию сложения "
                        f"между типом \'{self.__class__.__name__}\' "
                        f"и \'{other.__class__.__name__}\'")



def execute_application():

    circ = Circle(5)
    circ.calc_circumference_length()
    print(circ.__dict__)
    circ += 5
    print(circ.__dict__)


if __name__ == "__main__":
    execute_application()
