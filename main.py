from typing import Dict


"""
Задание 1.
Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
дату рождения, контактный телефон, город, страну, домашний адрес.
Реализуйте конструктор по умолчанию и метод для вывода данных.
Реализуйте доступ к отдельным полям класса через методы класса (геттеры
и сеттеры).
"""


class Human:

    def __init__(self, name: Dict[str, str], birthday: Dict[str, str], phone: str,
                 country: str, city: str, address: Dict[str, str]):
        self.__name = name
        self.__birthday = birthday
        self.__phone = phone
        self.__country = country
        self.__city = city
        self.__address = address

    def __str__(self):
        return f"ФИО: {list(self.__name.values())}\n" \
               f"Дата рождения: {list(self.__birthday.values())}\n" \
               f"Номер телефона: {self.__phone}\n" \
               f"Страна: {self.__country}\n" \
               f"Город: {self.__city}\n" \
               f"Адрес: {list(self.__address.values())}\n"



def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
