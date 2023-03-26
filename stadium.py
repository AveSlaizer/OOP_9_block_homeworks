from typing import Dict


class Stadium:

    def __init__(self, name: str, date: Dict[str, str] = None,
                 country: str = None, city: str = None, capacity: int = None):
        self.__name = name
        self.__date_of_opening = date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def __str__(self):
        return f"Название: {self.__name}\n" \
               f"Дата открытия: {list(self.__date_of_opening.values())}\n" \
               f"Страна: {self.__country}\n" \
               f"Город: {self.__city}\n" \
               f"Вместимость: {self.__capacity}\n"

    @classmethod
    def init_from_file(cls, path: str):
        """
        Возвращает объект класса Stadium из файла
        :param path (str): Путь и название файла с расширением
        :return:
                объект класса Stadium
        """
        with open(path, "r", encoding="UTF-8") as file:
            name = file.readline().rstrip()
            temp = file.readline().rstrip().split(".")
            date = {"день": temp[0], "месяц": temp[1], "год": temp[2]}
            country = file.readline().rstrip()
            city = file.readline().rstrip()
            capacity = int(file.readline().rstrip())
            return cls(name, date, country, city, capacity)

    @staticmethod
    def read_from_file(path: str) -> tuple[str, Dict[str, str], str, str, int]:
        """
        Возвращает кортеж с данными считанными из файла

        :param path (str): Путь и название файла с расширением
        :return:
                Tuple(str, str, int, float, str, float): Кортеж с данными
        """
        with open(path, "r", encoding="UTF-8") as file:
            name = file.readline().rstrip()
            temp = file.readline().rstrip().split(".")
            date = {"день": temp[0], "месяц": temp[1], "год": temp[2]}
            country = file.readline().rstrip()
            city = file.readline().rstrip()
            capacity = int(file.readline().rstrip())
            return name, date, country, city, capacity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def date(self):
        return self.__date_of_opening

    @date.setter
    def date(self, date: Dict[str, str]):
        self.__date_of_opening = date

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: float):
        self.__capacity = capacity
