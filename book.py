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


class BookPickleAdapter:

    @staticmethod
    def to_pickle(book: Book):
        if not isinstance(book, Book):
            raise TypeError(f"Недопустимый тип данных {book.__class__.__name__}, ожидался 'Book'")
        return pickle.dumps({
            "className": book.__class__.__name__,
            "name": book.name,
            "author": book.author,
            "year": book.year
        })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        try:
            assert obj["className"] == "Book", "Ошибка обработки данных"
            return Book(obj["name"], obj["author"], obj["year"])
        except AttributeError:
            print("Ошибка обработки данных")
        except AssertionError as e:
            print(e)


class BookJSONAdapter:

    @staticmethod
    def to_json(book: Book):
        if not isinstance(book, Book):
            raise TypeError(f"Недопустимый тип данных {book.__class__.__name__}, ожидался 'Book'")
        return json.dumps({
            "className": book.__class__.__name__,
            "name": book.name,
            "author": book.author,
            "year": book.year
        })

    @staticmethod
    def from_json(data):
        obj = json.loads(data)
        try:
            assert obj["className"] == "Book", "Ошибка обработки данных"
            return Book(obj["name"], obj["author"], obj["year"])
        except AttributeError:
            print("Ошибка обработки данных")
        except AssertionError as e:
            print(e)
