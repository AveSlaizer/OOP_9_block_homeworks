from typing import Dict


"""
Задание 2.
Реализуйте класс «Стадион». Необходимо хранить в полях класса:
название стадиона, дату открытия, страну, город, вместимость. Реализуйте
конструктор по умолчанию и метод для вывода данных.
"""

class Stadium:
    name: str
    date_of_opening: Dict[str, str]
    country: str
    city: str
    capacity: int

    def __init__(self, name: str, date: Dict[str, str],
                 country: str, city: str, capacity: int):
        self.name = name
        self.date_of_opening = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Название: {self.name}\n" \
               f"Дата открытия: {list(self.date_of_opening.values())}\n" \
               f"Страна: {self.country}\n" \
               f"Город: {self.city}\n" \
               f"Вместимость: {self.capacity}\n"


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
