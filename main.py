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

    name = {"фамилия": "Сушков", "имя": "Артем", "отчество": "Сергеевич"}
    birthday = {"число": "11", "месяц": "Апрель", "год": "1988"}
    phone = "+79201234567"
    country = "Российская Федерация"
    city = "Ярославль"
    address = "ул. Пушкина д. 2 кв. 1098"


    def __str__(self):
        return f"ФИО: {list(self.name.values())}\n" \
               f"Дата рождения: {list(self.birthday.values())}\n" \
               f"Номер телефона: {self.phone}\n" \
               f"Страна: {self.country}\n" \
               f"Город: {self.city}\n" \
               f"Адрес: {self.address}\n"


# Задание 2
class Book:

    name = "Вредные советы"
    author = "Остер Григорий Бенционович"
    year = "2014"
    publisher = "ACT"
    genre = "Библиотека начальной школы"
    price = 211.9

    def __str__(self):
        return f"Название: {self.name}\n" \
               f"Автор: {self.author}\n" \
               f"Год издания: {self.year}\n" \
               f"Издатель: {self.publisher}\n" \
               f"Жанр: {self.genre}\n" \
               f"Цена: {self.price}\n"


def execute_application():
    man = Human()
    print(man)

    book = Book()
    print(book)


if __name__ == "__main__":
    execute_application()
