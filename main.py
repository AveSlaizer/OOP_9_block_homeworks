from typing import Union

"""
    Задание 1.
    Реализуйте класс Retailltem (товарная единица), который содержит
данные о товаре в магазине. Этот класс должен хранить данные в атрибутах:
описание товара, количество единиц на складе и цена. После написания
этого класса напишите программу, которая создает три объекта Retailitem.

    Создайте класс CashRegister (Кассовый аппарат), который может
использоваться вместе с классом Retailltem. Класс CashRegister должен иметь
внутренний список объектов Retailltem, а также приведенные ниже методы:

    Метод purchase_item() (приобрести товар) в качестве аргумента
принимает объект Retailltem. При каждом вызове метода purchase_item()
объект Retailltem, переданный в качестве аргумента, должен быть добавлен в
список.

    Метод get_total () (получить сумму покупки) возвращает общую
стоимость всех объектов Retailltem, хранящихся во внутреннем списке
объекта CashRegister.

    Метод show_iterns () (показать товары) выводит данные об объектах
Retailltem, хранящихся во внутреннем списке объекта CashRegister.

    Метод clear () (очистить) должен очистить внутренний список объекта
CashRegister.

    Продемонстрируйте класс CashRegister в программе, которая
позволяет пользователю выбрать несколько товаров для покупки. Когда
пользователь готов рассчитаться за покупку, программа должна вывести
список всех товаров, которые он выбрал для покупки, а также их общую
стоимость.
"""


class RetailItem:

    def __init__(self, description: str, quantity: int, price: float):
        self.__description = self.__is_valid_description(description)
        self.__quantity = self.__is_valid_quantity(quantity)
        self.__price = self.__is_valid_price(price)

    @staticmethod
    def __is_valid_description(value):
        if not isinstance(value, str):
            raise TypeError(f"Не верный тип данных: \'{value.__class__.__name__}\' "
                            f"ожидался 'str'")
        return value

    @staticmethod
    def __is_valid_quantity(value):
        if not isinstance(value, int):
            raise TypeError(f"Не верный тип данных: \'{value.__class__.__name__}\' "
                            f"ожидался 'int'")
        if value <= 0:
            raise ValueError(f"Количество предметов не может быть равным {value}. Требуется число больше 0")
        return value

    @staticmethod
    def __is_valid_price(value):
        if not isinstance(value, Union[int, float]):
            raise TypeError(f"Не верный тип данных: \'{value.__class__.__name__}\' "
                            f"ожидался 'int' или 'float'")
        if value <= 0:
            raise ValueError(f"Стоимость не может быть равной {value}. Требуется число больше 0")
        return value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = self.__is_valid_description(description)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = self.__is_valid_quantity(quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = self.__is_valid_price(price)

    def __str__(self):
        return f"{self.__description}, {self.__quantity} шт., {self.__price} руб."


def execute_application():

    car = RetailItem("ААааавтомобиль", 10, 12)

    print(car)


if __name__ == "__main__":
    execute_application()
