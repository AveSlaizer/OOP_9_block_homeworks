class Stadium:

    def __init__(self, name: str, date: str, country: str, city: str):
        self.__name = name
        self.__date_of_opening = date
        self.__country = country
        self.__city = city

    def __str__(self):
        return f"Название: {self.__name}\n" \
               f"Дата открытия: {self.__date_of_opening}\n" \
               f"Страна: {self.__country}\n" \
               f"Город: {self.__city}\n"

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date_of_opening

    @property
    def country(self):
        return self.__country

    @property
    def city(self):
        return self.__city
