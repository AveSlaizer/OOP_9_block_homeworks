import pickle, json

"""
Задание 2
К уже реализованному классу «Книга» добавьте возможность
упаковки и распаковки данных с использованием json и pickle.
"""


class Book:

    def __init__(self, name: str, author: str = None, year: str = None):
        self.__name = name
        self.__author = author
        self.__year = year

    def __str__(self):
        return f"Название: {self.__name}\n" \
               f"Автор: {self.__author}\n" \
               f"Год издания: {self.__year}\n"

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year
