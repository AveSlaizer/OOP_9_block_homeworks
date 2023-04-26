"""
Задание 2.
Создайте класс Point (точка). Для данного класса реализуйте ряд
перегруженных операторов:
Проверка на равенство пар координат по осям X и Y (операция ==, !=);
Проверка сравнения пар координат (операции >, <, <=, >=);
"""


class Point:

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __is_point(self, other):
        if not isinstance(other, Point):
            raise TypeError(f"Невозможно выполнить сравнение между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __hash__(self):
        return hash((self.__x, self.__y))

    def __eq__(self, other):
        self.__is_point(other)
        return self.__x == other.__x and self.__y == other.__y

    def __ne__(self, other):
        self.__is_point(other)
        return self.__x != other.__x or self.__y != other.__y


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
