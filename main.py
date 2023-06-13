"""
    Задание 1.
    Создайте класс «Число», которое хранит его значение и информацию о
системе счисления. Создайте несколько экземпляров данного класса.
Создайте класс «Калькулятор СС». В классе должна быть реализована
следующая функциональность:
    Перевод числа в восьмеричную систему счисления.
    Перевод числа в шестнадцатеричную систему счисления.
    Перевод числа в двоичную систему счисления.
    Перевод числа в десятичную систему счисления.
"""


class Digit:
    __symbols = "0123456789abcdef"

    def __init__(self, value: str, number_system: int):
        self.__value, self.__number_system = self.__digit_validator(value, number_system)

    @staticmethod
    def __digit_validator(value: str, number_system: int):
        if not isinstance(value, str):
            raise ValueError(f"Недопустимый тип данных '{value.__class__.__name__}', ожидался 'str'.")
        if not isinstance(number_system, int):
            raise ValueError(f"Недопустимый тип данных '{number_system.__class__.__name__}', ожидался 'int'.")
        if not (2 <= number_system <= 16):
            raise ValueError(f"Недопустимое значение системы счисления. Ожидалось число от 2 до 16.")
        for symbol in value:
            if symbol.lower() not in Digit.__symbols[:number_system]:
                raise ValueError(f"Недопустимое числовое значение в {number_system}-ой системе счисления.")
        return value, number_system

    def __index__(self):
        return int(self.__value, self.__number_system)

    @property
    def value(self):
        return self.__value

    @property
    def number_system(self):
        return self.__number_system


class NSCalculator:

    @staticmethod
    def to_hex(digit: Digit) -> Digit:
        return Digit(hex(digit)[2:], 16)

    @staticmethod
    def to_oct(digit: Digit) -> Digit:
        return Digit(oct(digit)[2:], 8)

    @staticmethod
    def to_bin(digit: Digit) -> Digit:
        return Digit(bin(digit)[2:], 2)

    @staticmethod
    def to_dec(digit: Digit) -> Digit:
        return Digit(str(int(digit)), 10)


def execute_application():
    numb = Digit("11", 2)
    print(numb.__dict__)
    numb = NSCalculator.to_dec(numb)
    print(numb.__dict__)


if __name__ == "__main__":
    execute_application()
