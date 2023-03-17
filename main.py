"""
Задание 1.
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, цвет машины,
цену. Реализуйте конструктор по умолчанию и метод для вывода данных.

Задание 2.
Реализуйте класс «Стадион». Необходимо хранить в полях класса:
название стадиона, дату открытия, страну, город, вместимость. Реализуйте
конструктор по умолчанию и метод для вывода данных.
"""


# Задание 1
class Car:
    car_brand: str
    model: str
    year: int
    engine_volume: float
    color: str
    price: float

    def __init__(self, car_brand: str, model: str, year: int,
                 engine_volume: float, color: str, price: float):
        self.car_brand = car_brand
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.price = price


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
