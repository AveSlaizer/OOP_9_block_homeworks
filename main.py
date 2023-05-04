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
        if numerator * denominator > 0:
            self.__mark = "+"
        else:
            self.__mark = "-"

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @property
    def mark(self):
        return self.__mark

    def __str__(self):
        return f"{f'{self.__mark} ' if self.__mark == '-' else ''}{self.__numerator} / {self.__denominator}"


def execute_application():

    fract = MathematicalFraction(1, 2)

    print(fract)


if __name__ == "__main__":
    execute_application()
