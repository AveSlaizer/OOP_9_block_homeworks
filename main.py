"""
Задание 3.
Создайте класс Flat (квартира). Для данного класса реализуйте ряд
перегруженных операторов:
Проверка на равенство площадей квартир (операция ==);
Проверка на неравенство площадей квартир (операция !=);
Сравнение двух квартир по стоимости (операции >, <, <=, >=).
"""


class Flat:

    def __init__(self, square: float, price: float):
        self.__square = square
        self.__price = price




def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
