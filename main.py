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
        self._brand = brand
        self._kind = kind
        self._sub_type = sub_type
        self._model = model
        self._voltage = voltage

    def info(self):
        print(f"\nКласс: {self.__class__.__name__}\n"
              f"Брэнд: {self._brand}\n"
              f"Тип техники: {self._kind}\n"
              f"Подвид: {self._sub_type}\n"
              f"Модель: {self._model}\n"
              f"Потребляемое напряжение: {self._voltage}")


class CoffeeMachine(Device):

    def __init__(self, brand: str = None, kind: str = None, sub_type: str = None,
                 model: str = None, voltage: str = None, coffee_type: str = None):
        super().__init__(brand, kind, sub_type, model, voltage)
        self.__coffee_type = coffee_type

    def info(self):
        super().info()
        print(f"Вид используемого сырья: {self.__coffee_type}")


class Blender(Device):

    def __init__(self, brand: str = None, kind: str = None, sub_type: str = None,
                 model: str = None, voltage: str = None, accessory_qty: int = None):
        super().__init__(brand, kind, sub_type, model, voltage)
        self.__accessory_qty = accessory_qty

    def info(self):
        super().info()
        print(f"Количество насадок: {self.__accessory_qty}")


def execute_application():

    brand_2 = "Tefal"
    kind_2 = "Мелкая бытовая техника"
    sub_type_2 = "Автоматическая"
    model_2 = "adf213"
    voltage_2 = "220V"
    coffee_type = "Зерновой кофе"

    coffee_mach = CoffeeMachine(brand_2, kind_2, sub_type_2, model_2, voltage_2, coffee_type)

    coffee_mach.info()

    brand_3 = "Bosh"
    kind_3 = "Мелкая бытовая техника"
    sub_type_3 = "Погружной бледер"
    model_3 = "gf-1q-da"
    voltage_3 = "220V"
    accessories = 6

    blender = Blender(brand_3, kind_3, sub_type_3, model_3, voltage_3, accessories)

    blender.info()


if __name__ == "__main__":
    execute_application()
