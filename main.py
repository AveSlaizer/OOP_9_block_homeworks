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


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
