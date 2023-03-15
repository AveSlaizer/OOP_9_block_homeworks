from typing import Dict

"""Задание 1.
Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
дату рождения, контактный телефон, город, страну, домашний адрес.
Реализуйте конструктор по умолчанию и метод для вывода данных.
"""
"""
Задание 2.
Реализуйте класс «Книга». Необходимо хранить в полях класса:
название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
конструктор по умолчанию и метод для вывода данных.
"""

# Задание 1
class Human:

    name: Dict[str, str]
    birthday: Dict[str, str]
    telephone: str
    country: str
    city: str
    address: str

    def __init__(self, name: Dict[str, str], birthday: Dict[str, str], telephone: str,
                 country: str, city: str, address: str):
        self.name = name
        self.birthday = birthday
        self.telephone = telephone
        self.country = country
        self.city = city
        self.address = address



def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
