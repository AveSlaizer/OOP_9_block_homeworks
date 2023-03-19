from typing import Dict

"""
Задание 2.
Реализуйте класс «Стадион». Необходимо хранить в полях класса:
название стадиона, дату открытия, страну, город, вместимость. Реализуйте
конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
отдельным полям класса через методы класса (геттеры и сеттеры).
"""


class Stadium:

    def __init__(self, name: str, date: Dict[str, str],
                 country: str, city: str, capacity: int):
        self.__name = name
        self.__date_of_opening = date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def __str__(self):
        return f"Название: {self.__name}\n" \
               f"Дата открытия: {list(self.__date_of_opening.values())}\n" \
               f"Страна: {self.__country}\n" \
               f"Город: {self.__city}\n" \
               f"Вместимость: {self.__capacity}\n"

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_date(self):
        return self.__date_of_opening

    def set_date(self, date: Dict[str, str]):
        self.__date_of_opening = date

    def get_country(self):
        return self.__country

    def set_country(self, country: str):
        self.__country = country

    def get_city(self):
        return self.__city

    def set_city(self, city: str):
        self.__city = city

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity: float):
        self.__capacity = capacity


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
