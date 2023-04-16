class InvalidSpeed(Exception):

    def __init__(self, text: str):
        self.text = text


class Transmission:

    def __init__(self, model: str, shift_type: str, speed_qty: int, speed: int = 0):
        self.__model = model
        self.__shift_type = shift_type
        self.__speed_qty = speed_qty
        self.__speed = speed

    def __str__(self):
        return f"Модель: {self.__model}, тип: {self.__shift_type}, количество передач: {self.__speed_qty}"

    def gear_up(self):
        if self.__speed == self.__speed_qty:
            raise InvalidSpeed("Невозможно повысить передачу")
        self.__speed += 1

    def gear_down(self):
        if self.__speed == -1:
            raise InvalidSpeed("Невозможно понизить передачу")
        self.__speed -= 1

    @property
    def model(self):
        return self.__model

    @property
    def shift_type(self):
        return self.__shift_type

    def status(self):
        if self.__speed == -1:
            return "Включена задняя передача"
        elif self.__speed == 0:
            return "КПП в нейтральном положении"
        else:
            return f"Включена {self.__speed}-я передача"


class ManualTransmission(Transmission):
    pass


class AutomaticTransmission(Transmission):
    pass


class RoboticTransmission(Transmission):
    pass

# Миксин
class TransmissionSpeedStatus:

    @staticmethod
    def print_speed_status(transmission: Transmission):
        print(transmission.status())
