"""
Задание 1.
Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте класс CoffeeMachine
(содержит информацию о кофемашине), класс Blender (содержит информацию
о блендере).
"""


class Device:

    def __init__(self, brand: str = None, kind: str = None, sub_type: str = None,
                 model: str = None, voltage: str = None):
        self.__brand = brand
        self.__kind = kind
        self.__sub_type = sub_type
        self.__model = model
        self.__voltage = voltage

    def info(self):
        print(f"\nКласс: {self.__class__.__name__}\n"
              f"Брэнд: {self.__brand}\n"
              f"Тип техники: {self.__kind}\n"
              f"Подвид: {self.__sub_type}\n"
              f"Модель: {self.__model}\n"
              f"Потребляемое напряжение: {self.__voltage}")


class CoffeeMachine(Device):

    def __init__(self, brand: str = None, kind: str = None, sub_type: str = None,
                 model: str = None, voltage: str = None):
        super().__init__(brand, kind, sub_type, model, voltage)

    def info(self):
        super().info()


class Blender(Device):
    pass


def execute_application():
    brand_2 = "Tefal"
    kind_2 = "Мелкая бытовая техника"
    sub_type_2 = "Капсульная кофемашина"
    model_2 = "adf213"
    voltage_2 = "220V"

    coffee_mach = CoffeeMachine(brand_2, kind_2, sub_type_2, model_2, voltage_2)

    coffee_mach.info()

    brand_3 = "Bosh"
    kind_3 = "Мелкая бытовая техника"
    sub_type_3 = "Погружной бледер"
    model_3 = "gf-1q-da"
    voltage_3 = "220V"

    blender = Blender(brand_3, kind_3, sub_type_3, model_3, voltage_3)

    blender.info()


if __name__ == "__main__":
    execute_application()
