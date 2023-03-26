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