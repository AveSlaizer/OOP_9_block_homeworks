"""
Задание 1.
Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте класс CoffeeMachine
(содержит информацию о кофемашине), класс Blender (содержит информацию
о блендере).
"""


class Device:

    def __init__(self, brand: str, kind: str):
        self.__brand = brand
        self.__kind = kind


    def info(self):
        print(f"\nКласс: {self.__class__.__name__}\n"
              f"Брэнд: {self.__brand}\n"
              f"Тип техники: {self.__kind}\n")

class CoffeeMachine(Device):

    def __init__(self, brand: str, kind: str, sub_type: str, model: str, voltage: str):
        super().__init__(brand, kind)
        self.__sub_type = sub_type
        self.__model = model
        self.__voltage = voltage

    def info(self):
        super().info()
        print(f"Подвид: {self.__sub_type}\n"
              f"Модель: {self.__model}\n"
              f"Потребляемое напряжение: {self.__voltage}")

def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
