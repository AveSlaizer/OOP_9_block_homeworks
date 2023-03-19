"""
Задание 2.
Реализуйте класс «Книга». Необходимо хранить в полях класса:
название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
отдельным полям класса через методы класса (геттеры и сеттеры).
"""


class Book:

    def __init__(self, name: str, author: str, year: str, publisher: str, genre: str, price: float):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__price = price

    def __str__(self):
        return f"Название: {self.__name}\n" \
               f"Автор: {self.__author}\n" \
               f"Год издания: {self.__year}\n" \
               f"Издатель: {self.__publisher}\n" \
               f"Жанр: {self.__genre}\n" \
               f"Цена: {self.__price}\n"


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
