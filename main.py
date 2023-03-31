"""
Задание 1.
Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте класс CoffeeMachine
(содержит информацию о кофемашине), класс Blender (содержит информацию
о блендере).
"""


class Device:

    def __init__(self, voltage: str, brand: str, kind: str):
        self.__voltage = voltage
        self.__brand = brand
        self.__kind = kind



def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
