import pickle, json


class Stadium:

    def __init__(self, name: str, date: str, country: str, city: str):
        self.__name = name
        self.__date_of_opening = date
        self.__country = country
        self.__city = city

    def __str__(self):
        return f"Название: {self.__name}\n" \
               f"Дата открытия: {self.__date_of_opening}\n" \
               f"Страна: {self.__country}\n" \
               f"Город: {self.__city}\n"

    @property
    def name(self):
        return self.__name

    @property
    def date(self):
        return self.__date_of_opening

    @property
    def country(self):
        return self.__country

    @property
    def city(self):
        return self.__city


class StadiumJSONAdapter:

    @staticmethod
    def to_json(stadium: Stadium):
        if not isinstance(stadium, Stadium):
            raise TypeError(f"Недопустимый тип данных {stadium.__class__.__name__}, ожидался 'Stadium'")
        return json.dumps({
            "className": stadium.__class__.__name__,
            "name": stadium.name,
            "date": stadium.date,
            "country": stadium.country,
            "city": stadium.city
        })

    @staticmethod
    def from_json(data):
        obj = json.loads(data)
        try:
            assert obj["className"] == "Stadium", "Ошибка обработки данных"
            return Stadium(obj["name"], obj["date"], obj["country"], obj["city"])
        except AttributeError:
            print("Ошибка обработки данных")
        except AssertionError as e:
            print(e)


class StadiumPickleAdapter:

    @staticmethod
    def to_pickle(stadium: Stadium):
        if not isinstance(stadium, Stadium):
            raise TypeError(f"Недопустимый тип данных {stadium.__class__.__name__}, ожидался 'Stadium'")
        return pickle.dumps({
            "className": stadium.__class__.__name__,
            "name": stadium.name,
            "date": stadium.date,
            "country": stadium.country,
            "city": stadium.city
        })

    @staticmethod
    def from_pickle(data):
        obj = pickle.loads(data)
        try:
            assert obj["className"] == "Stadium", "Ошибка обработки данных"
            return Stadium(obj["name"], obj["date"], obj["country"], obj["city"])
        except AttributeError:
            print("Ошибка обработки данных")
        except AssertionError as e:
            print(e)
