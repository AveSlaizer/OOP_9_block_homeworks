class Car:

    def __init__(self, brand: str, model: str, year: str):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def __str__(self):
        return f"{self.__brand} {self.__model}, {self.__year} года выпуска"

