class Car:

    def __init__(self, brand: str, model: str, year: int = None,
                 engine_volume: float = None, color: str = None, price: float = None):
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

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def engine_volume(self):
        return self.__engine_volume

    @engine_volume.setter
    def engine_volume(self, engine_volume: float):
        self.__engine_volume = engine_volume

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price