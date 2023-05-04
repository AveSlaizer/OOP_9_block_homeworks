from math import gcd
from typing import Union

"""
Задание 1.
Создайте класс Обыкновенная дробь. Используя перегрузку операторов
реализуйте для него арифметические операции и операции сравнения для
работы с обыкновенными дробями.
В классе должна быть реализована следующая функциональность:
    - Сложение дробей;
    - Вычитание дробей;
    - Умножение дробей;
    - Деление дробей.
    - Сравнение дробей
В т.ч. Перегрузка операций должна работать с целыми числам
"""


class InitializationFractionError(Exception):

    def __init__(self, text: str, value):
        self.text = text
        self.value = value


class MathematicalFraction:

    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int):
            raise InitializationFractionError("Не верный тип данных:", numerator.__class__.__name__)
        if not isinstance(denominator, int):
            raise InitializationFractionError("Не верный тип данных:", denominator.__class__.__name__)
        if denominator == 0:
            raise InitializationFractionError("Невозможно создать дробь со знаменателем равным", denominator)

        self.__numerator = abs(numerator)
        self.__denominator = abs(denominator)

        if numerator * denominator < 0:
            self.__numerator *= -1

    def shorten_fraction(self):
        """
        Сокращает дробь

        :return: None
        """
        value = gcd(self.__numerator, self.__denominator)
        if value > 1:
            self.__numerator = int(self.__numerator / value)
            self.__denominator = int(self.__denominator / value)

    def lead_to_common_denominator(self, other, denominator: bool = True)\
            -> Union[tuple[int, int], tuple[int, int, int]]:
        """
        Возвращает кортеж с числителем первой дроби, числителем второй дроби и общий знаменатель дробей.
        Если denominator == False, то общий знаменатель не будет возвращаться

        :param other MathematicalFraction: дробь
        :param denominator bool: триггер, определяет, вернется ли общий знаменатель
        :return:
                Union[tuple[int, int], tuple[int, int, int]]:
                 Числитель первой дроби, числитель второй дроби, общий знаменатель
        """
        self.__is_math_fraction(other)

        if denominator:
            value_tuple = (self.__numerator * other.__denominator,
            other.__numerator * self.__denominator,
            other.__denominator * self.__denominator)
        else:
            value_tuple = (self.__numerator * other.__denominator,
                           other.__numerator * self.__denominator)
        return value_tuple


    def __is_math_fraction(self, other):
        if not isinstance(other, MathematicalFraction):
            raise TypeError(f"Ошибка! Требуемый тип данных:\'{self.__class__.__name__}\', "
                            f"получен: \'{other.__class__.__name__}\'")

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    def __str__(self):
        return f"{'- ' if self.__numerator < 0 else ''}{abs(self.__numerator)} / {self.__denominator}"

    def __hash__(self):
        return hash(self.__numerator / self.__denominator)

    def __eq__(self, other):
        self.__is_math_fraction(other)
        numerator1, numerator2 = self.lead_to_common_denominator(other, denominator=False)
        return numerator1 == numerator2

    def __ne__(self, other):
        self.__is_math_fraction(other)
        numerator1, numerator2 = self.lead_to_common_denominator(other, denominator=False)
        return numerator1 != numerator2


def execute_application():

    fract = MathematicalFraction(1, 2)
    fract1 = MathematicalFraction(2, 4)
    print(fract == fract1)
    print(fract != fract1)




if __name__ == "__main__":
    execute_application()
