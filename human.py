from typing import Dict


class Human:

    def __init__(self, name: Dict[str, str], birthday: Dict[str, str] = None, phone: str = None,
                 country: str = None, city: str = None, address: Dict[str, str] = None):
        self.name = name.copy()
        self.birthday = birthday.copy()
        self.phone = phone
        self.country = country
        self.city = city
        self.address = address.copy()

    def __str__(self):
        return f"ФИО: {list(self.name.values())}\n" \
               f"Дата рождения: {list(self.birthday.values())}\n" \
               f"Номер телефона: {self.phone}\n" \
               f"Страна: {self.country}\n" \
               f"Город: {self.city}\n" \
               f"Адрес: {list(self.address.values())}\n"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: Dict[str, str]):
        self.__name = name.copy()

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: Dict[str, str]):
        self.__birthday = birthday.copy()

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

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
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: Dict[str, str]):
        self.__address = address.copy()