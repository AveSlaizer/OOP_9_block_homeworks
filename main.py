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
    NUMBER_SYSTEM_LIST = ["bin", "oct", "dec", "hex"]

    def __init__(self, value: str, number_system: str):
        self.__value = self.__is_valid_value(value)
        self.__number_system = self.__is_valid_number_system(number_system)

    @staticmethod
    def __is_valid_value(value):
        if not isinstance(value, str):
            raise TypeError(f"Недопустимый тип данных '{value.__class__.__name__}'. Ожидалось 'str'")
        return value

    @staticmethod
    def __is_valid_number_system(number_system):
        if not isinstance(number_system, str):
            raise TypeError(f"Недопустимый тип данных '{number_system.__class__.__name__}'. Ожидалось 'str'")
        if not number_system in Digit.NUMBER_SYSTEM_LIST:
            raise ValueError(f"Недопустимое значение '{number_system}'")
        return number_system

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
    numb = Digit("16", "dec")

    numb = NSCalculator.dec_to_bin(numb)

    print(numb.__dict__)

    numb = NSCalculator.bin_to_oct(numb)

    print(numb.__dict__)

    numb = NSCalculator.oct_to_dec(numb)
    print(numb.__dict__)


if __name__ == "__main__":
    execute_application()
