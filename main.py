from typing import Dict

"""
Задание 1.
Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
дату рождения, контактный телефон, город, страну, домашний адрес.
Реализуйте конструктор по умолчанию и метод для вывода данных.
Реализуйте доступ к отдельным полям класса через методы класса (геттеры
и сеттеры).
"""


class Human:

    def __init__(self, name: Dict[str, str], birthday: Dict[str, str], phone: str,
                 country: str, city: str, address: Dict[str, str]):
        self.__name = name.copy()
        self.__birthday = birthday.copy()
        self.__phone = phone
        self.__country = country
        self.__city = city
        self.__address = address.copy()

    def __str__(self):
        return f"ФИО: {list(self.__name.values())}\n" \
               f"Дата рождения: {list(self.__birthday.values())}\n" \
               f"Номер телефона: {self.__phone}\n" \
               f"Страна: {self.__country}\n" \
               f"Город: {self.__city}\n" \
               f"Адрес: {list(self.__address.values())}\n"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: Dict[str, str]):
        self.__name = name.copy()

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: Dict[str, str]):
        self.__birthday = birthday.copy()

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: Dict[str, str]):
        self.__address = address.copy()


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
