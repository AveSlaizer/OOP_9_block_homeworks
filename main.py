import pickle, json

"""
Задание 1
К уже реализованному классу «Автомобиль» добавьте
возможность упаковки и распаковки данных с использованием json и pickle.
"""


class Car:

    def __init__(self, brand: str, model: str, year: str):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def __str__(self):
        return f"{self.__brand} {self.__model}, {self.__year} года выпуска"


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
