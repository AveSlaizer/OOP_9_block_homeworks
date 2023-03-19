"""
Задание 1.
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, цвет машины,
цену. Реализуйте конструктор по умолчанию и метод для вывода данных.
Реализуйте доступ к отдельным полям класса через методы класса (геттеры
и сеттеры).
"""


class Car:

    def __init__(self, brand: str, model: str, year: int,
                 engine_volume: float, color: str, price: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def __str__(self):
        return f"Марка: {self.brand}\n" \
               f"Модель: {self.model}\n" \
               f"Год выпуска: {self.year}\n" \
               f"Объем двигателя: {self.engine_volume}\n" \
               f"Цвет: {self.color}\n" \
               f"Цена: {self.price}\n"


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
