"""
Задание 2.
Реализуйте класс «Книга». Необходимо хранить в полях класса:
название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
конструктор по умолчанию и метод для вывода данных. Реализуйте доступ к
отдельным полям класса через методы класса (геттеры и сеттеры).
"""


class Book:

    def __init__(self, name: str, author: str = None, year: str = None,
                 publisher: str = None, genre: str = None, price: float = None):
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

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_author(self):
        return self.__author

    def set_author(self, author: str):
        self.__author = author

    def get_year(self):
        return self.__year

    def set_year(self, year: str):
        self.__year = year

    def get_publisher(self):
        return self.__publisher

    def set_publisher(self, publisher: str):
        self.__publisher = publisher

    def get_genre(self):
        return self.__genre

    def set_genre(self, genre: str):
        self.__genre = genre

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
