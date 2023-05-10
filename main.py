import pickle


"""
Задание 1.
Создайте класс «Самолет». Наполните его необходимыми характеристиками и методами. Реализуйте упаковку и
распаковку объектов класса «Самолет» с использованием модуля pickle.
"""


class AirPlane:

    def __init__(self, name: str, engine_type: str, engine_qty: int):
        self.__name = name
        self.__engine_type = engine_type
        self.__engine_qty = engine_qty

    def __str__(self):
        return f"Название: {self.__name}, " \
               f"тип двигателей: {self.__engine_type}, " \
               f"количество двигателей: {self.__engine_qty}"

    @property
    def name(self):
        return self.__name

    @property
    def engine_type(self):
        return self.__engine_type

    @property
    def engine_qty(self):
        return self.__engine_qty


class AirPlanePickleAdapter:

    @staticmethod
    def to_pickle(plane: AirPlane):
        if not isinstance(plane, AirPlane):
            raise TypeError(f"Недопустимый тип данных {plane.__class__.__name__}, ожидался 'AirPlane'")
        return pickle.dumps({
            "className": plane.__class__.__name__,
            "name": plane.name,
            "engine_type": plane.engine_type,
            "engine_qty": plane.engine_qty
        })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        try:
            if obj["className"] == "AirPlane":
                return AirPlane(obj["name"], obj["engine_type"], obj["engine_qty"])
        except AttributeError as e:
            print(e)


def execute_application():
    plane = AirPlane("Миг", "Реактивный", 2)
    print(plane)
    data = AirPlanePickleAdapter.to_pickle(plane)
    print(data)
    new_plane = AirPlanePickleAdapter.from_pickle(data)
    print(new_plane)


if __name__ == "__main__":
    execute_application()
