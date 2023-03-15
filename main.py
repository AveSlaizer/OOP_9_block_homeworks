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
    phone: str
    country: str
    city: str
    address: str

    def __init__(self, name: Dict[str, str], birthday: Dict[str, str], phone: str,
                 country: str, city: str, address: str):
        self.name = name
        self.birthday = birthday
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address

    def __str__(self):
        return f"ФИО: {list(self.name.values())}\n" \
               f"Дата рождения: {list(self.birthday.values())}\n" \
               f"Номер телефона: {self.phone}\n" \
               f"Страна: {self.country}\n" \
               f"Город: {self.city}\n" \
               f"Адрес: {self.address}\n"


# Задание 2
class Book:
    name: str
    author: str
    year: str
    publisher: str
    genre: str
    price: float

    def __init__(self, name: str, author: str, year: str, publisher: str, genre: str, price: float):
        self.name = name
        self.author = author
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.price = price

    def __str__(self):
        return f"Название: {self.name}\n" \
               f"Автор: {self.author}\n" \
               f"Год издания: {self.year}\n" \
               f"Издатель: {self.publisher}\n" \
               f"Жанр: {self.genre}\n" \
               f"Цена: {self.price}\n"


def execute_application():
    # Задание 1
    name = {"фамилия": "Сушков", "имя": "Артем", "отчество": "Сергеевич"}
    birthday = {"число": "11", "месяц": "Апрель", "год": "1988"}
    phone = "+79201234567"
    country = "Российская Федерация"
    city = "Ярославль"
    address = "ул. Пушкина д. 2 кв. 1098"

    man = Human(name, birthday, phone, country, city, address)
    print(man)

    # Задание 2
    name = "Вредные советы"
    author = "Остер Григорий Бенционович"
    year = "2014"
    publisher = "ACT"
    genre = "Библиотека начальной школы"
    price = 211.9

    book = Book(name, author, year, publisher, genre, price)
    print(book)


if __name__ == "__main__":
    execute_application()

