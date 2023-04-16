class Transmission:

    def __init__(self, model: str, shift_type: str, speed_qty: int, speed: int = 0):
        self.__model = model
        self.__shift_type = shift_type
        self.__speed_qty = speed_qty
        self.__speed = speed

    def __str__(self):
        return f"Модель: {self.__model}, тип: {self.__shift_type}"

    def gear_up(self):
        pass

    @property
    def model(self):
        return self.__model

    @property
    def shift_type(self):
        return self.__shift_type



"""
    def get_status(self):
        if self.__speed == -1:
            return "Включена задняя передача"
        elif self.__speed == 0:
            return "КПП в нейтральном положении"
        else:
            return f"Включена {self.__speed}-я передача"
"""

