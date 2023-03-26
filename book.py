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