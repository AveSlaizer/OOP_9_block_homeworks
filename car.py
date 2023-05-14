import pickle, json

"""
Задание 1
К уже реализованному классу «Автомобиль» добавьте
возможность упаковки и распаковки данных с использованием json и pickle.
"""


class Car:

    def __init__(self, brand: str, model: str, year: str):
        self.__brand = brand
        self.__model = model
        self.__year = year

    def __str__(self):
        return f"{self.__brand} {self.__model}, {self.__year} года выпуска"

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

class CarPickleAdapter:

    @staticmethod
    def to_pickle(car: Car):
        if not isinstance(car, Car):
            raise TypeError(f"Недопустимый тип данных {car.__class__.__name__}, ожидался 'Car'")
        return pickle.dumps({
            "className": car.__class__.__name__,
            "brand": car.brand,
            "model": car.model,
            "year": car.year
        })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        try:
            assert obj["className"] == "Car", "Ошибка обработки данных"
            return Car(obj["brand"], obj["model"], obj["year"])
        except AttributeError:
            print("Ошибка обработки данных")
        except AssertionError as e:
            print(e)


class CarJSONAdapter:

    @staticmethod
    def to_json(car: Car):
        if not isinstance(car, Car):
            raise TypeError(f"Недопустимый тип данных {car.__class__.__name__}, ожидался 'Car'")
        return json.dumps({
            "className": car.__class__.__name__,
            "brand": car.brand,
            "model": car.model,
            "year": car.year
        })

    @staticmethod
    def from_json(data):
        obj = json.loads(data)
        try:
            assert obj["className"] == "Car", "Ошибка обработки данных"
            return Car(obj["brand"], obj["model"], obj["year"])
        except AttributeError:
            print("Ошибка обработки данных")
        except AssertionError as e:
            print(e)
