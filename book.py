from typing import Tuple


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

    @classmethod
    def init_from_file(cls, path: str):
        """
        Возвращает объект класса Book из файла

        :param path (str): Путь и название файла с расширением
        :return:
                объект класса Book
        """
        with open(path, "r", encoding="UTF-8") as file:
            name = file.readline().rstrip()
            author = file.readline().rstrip()
            year = file.readline().rstrip()
            publisher = file.readline().rstrip()
            genre = file.readline().rstrip()
            price = float(file.readline().rstrip())
            return cls(name, author, year, publisher, genre, price)

    @staticmethod
    def read_from_file(path: str) -> tuple[str, str, str, str, str, float]:
        """
        Возвращает кортеж с данными считанными из файла

        :param path (str): Путь и название файла с расширением
        :return:
                Tuple(str, str, str, str, str, float): Кортеж с данными
        """
        with open(path, "r", encoding="UTF-8") as file:
            name = file.readline().rstrip()
            author = file.readline().rstrip()
            year = file.readline().rstrip()
            publisher = file.readline().rstrip()
            genre = file.readline().rstrip()
            price = float(file.readline().rstrip())
            return name, author, year, publisher, genre, price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str):
        self.__publisher = publisher

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre: str):
        self.__genre = genre

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price
