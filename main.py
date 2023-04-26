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

    def __is_flat(self, other):
        if not isinstance(other, Flat):
            raise TypeError(f"Невозможно выполнить сравнение между типом {self.__class__.__name__} "
                            f"и {other.__class__.__name__}")

    def __hash__(self):
        return hash((self.__square, self.__price))

    def __eq__(self, other):
        self.__is_flat(other)
        return self.__square == other.__square

    def __ne__(self, other):
        self.__is_flat(other)
        return self.__square != other.__square

    def __lt__(self, other):
        self.__is_flat(other)
        return self.__price < other.__price

    def __gt__(self, other):
        self.__is_flat(other)
        return self.__price > other.__price

    def __le__(self, other):
        self.__is_flat(other)
        return self.__price <= other.__price

    def __ge__(self, other):
        self.__is_flat(other)
        return self.__price >= other.__price


def execute_application():

    flat1 = Flat(10, 9000)
    flat2 = Flat(10, 9500)
    print(flat1 == flat2)
    print(flat1 < flat2)


if __name__ == "__main__":
    execute_application()
