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
            if symbol not in Digit.__symbols[:number_system]:
                raise ValueError(f"Недопустимое числовое значение в {number_system}-ой системе счисления.")
        return value, number_system

    @property
    def value(self):
        return self.__value

    @property
    def number_system(self):
        return self.__number_system


class NSCalculator:

    @staticmethod
    def __is_dec(number: Digit):
        if not number.number_system == "dec":
            raise ValueError(f"Недопустимое значение системы счисления '{number.number_system}' ожидалось 'dec'")

    @staticmethod
    def __is_bin(number: Digit):
        if not number.number_system == "bin":
            raise ValueError(f"Недопустимое значение системы счисления '{number.number_system}' ожидалось 'bin'")

    @staticmethod
    def __is_oct(number: Digit):
        if not number.number_system == "oct":
            raise ValueError(f"Недопустимое значение системы счисления '{number.number_system}' ожидалось 'oct'")

    @staticmethod
    def __is_hex(number: Digit):
        if not number.number_system == "hex":
            raise ValueError(f"Недопустимое значение системы счисления '{number.number_system}' ожидалось 'hex'")

    @staticmethod
    def dec_to_oct(number: Digit):
        NSCalculator.__is_dec(number)
        value = oct(int(number.value))[2:]
        number_system = "oct"
        return Digit(value, number_system)

    @staticmethod
    def dec_to_bin(number: Digit):
        NSCalculator.__is_dec(number)
        value = bin(int(number.value))[2:]
        number_system = "bin"
        return Digit(value, number_system)

    @staticmethod
    def dec_to_hex(number: Digit):
        NSCalculator.__is_dec(number)
        value = hex(int(number.value))[2:]
        number_system = "hex"
        return Digit(value, number_system)

    @staticmethod
    def bin_to_dec(number: Digit):
        NSCalculator.__is_bin(number)
        value = str(int(number.value, 2))
        number_system = "dec"
        return Digit(value, number_system)

    @staticmethod
    def oct_to_dec(number: Digit):
        NSCalculator.__is_oct(number)
        value = str(int(number.value, 8))
        number_system = "dec"
        return Digit(value, number_system)

    @staticmethod
    def hex_to_dec(number: Digit):
        NSCalculator.__is_hex(number)
        value = str(int(number.value, 16))
        number_system = "dec"
        return Digit(value, number_system)

    @staticmethod
    def bin_to_oct(number: Digit):
        return NSCalculator.dec_to_oct(NSCalculator.bin_to_dec(number))

    @staticmethod
    def bin_to_hex(number: Digit):
        return NSCalculator.dec_to_hex(NSCalculator.bin_to_dec(number))

    @staticmethod
    def oct_to_bin(number: Digit):
        return NSCalculator.dec_to_bin(NSCalculator.oct_to_dec(number))

    @staticmethod
    def oct_to_hex(number: Digit):
        return NSCalculator.dec_to_hex(NSCalculator.oct_to_dec(number))

    @staticmethod
    def hex_to_bin(number: Digit):
        return NSCalculator.dec_to_bin(NSCalculator.hex_to_dec(number))

    @staticmethod
    def hex_to_oct(number: Digit):
        return NSCalculator.dec_to_oct(NSCalculator.hex_to_dec(number))




def execute_application():
    numb = Digit("16", 16)


if __name__ == "__main__":
    execute_application()
