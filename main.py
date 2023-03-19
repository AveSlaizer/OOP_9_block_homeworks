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
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def __str__(self):
        return f"Марка: {self.__brand}\n" \
               f"Модель: {self.__model}\n" \
               f"Год выпуска: {self.__year}\n" \
               f"Объем двигателя: {self.__engine_volume}\n" \
               f"Цвет: {self.__color}\n" \
               f"Цена: {self.__price}\n"


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
