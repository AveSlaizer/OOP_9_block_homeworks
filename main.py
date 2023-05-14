from car import Car, CarPickleAdapter, CarJSONAdapter
from book import Book, BookJSONAdapter, BookPickleAdapter


def execute_application():
    car = Car("Лада", "Самара", "2000")
    print(car)
    data = CarJSONAdapter.to_json(car)
    print(data)
    obj = CarJSONAdapter.from_json(data)
    print(obj)

    book = Book("Book", "man", "2033")
    print(book)
    data = BookPickleAdapter.to_pickle(book)
    print(data)
    obj = BookPickleAdapter.from_pickle(data)
    print(obj)


if __name__ == "__main__":
    execute_application()
