from typing import Dict, List


class Passport:

    def __init__(self, name: Dict[str, str] = None, gender: str = None, date_of_birthday: Dict[str, str] = None,
                 place_of_birth: str = None, address: Dict[str, str] = None, date_of_issue: Dict[str, str] = None,
                 issued_at: str = None, series: str = None, number: str = None):
        self.__name = name
        self.__gender = gender
        self.__date_of_birthday = date_of_birthday
        self.__place_of_birth = place_of_birth
        self.__address = address
        self.__date_of_issue = date_of_issue
        self.__issued_at = issued_at
        self.__series = series
        self.__number = number

    def __str__(self):
        return f"\nФИО: {list(self.__name.values())}\n" \
               f"Пол: {self.__gender}\n" \
               f"Дата рождения: {list(self.__date_of_birthday.values())}\n" \
               f"Место рождения: {self.__place_of_birth}\n" \
               f"Адрес: {list(self.__address.values())}\n" \
               f"Дата выдачи: {list(self.__date_of_issue.values())}\n" \
               f"Выдано в: {self.__issued_at}\n" \
               f"Серия: {self.__series}\n" \
               f"Номер: {self.__number}"

    def info(self):
        print(f"\nКласс: {self.__class__.__name__}\n"
              f"ФИО: {list(self.__name.values())}\n"
              f"Пол: {self.__gender}\n"
              f"Дата рождения: {list(self.__date_of_birthday.values())}\n"
              f"Место рождения: {self.__place_of_birth}\n"
              f"Адрес: {list(self.__address.values())}\n"
              f"Дата выдачи: {list(self.__date_of_issue.values())}\n"
              f"Выдано в: {self.__issued_at}\n"
              f"Серия: {self.__series}\n"
              f"Номер: {self.__number}")


class ForeignPassport(Passport):

    def __init__(self, name: Dict[str, str] = None, gender: str = None, date_of_birthday: Dict[str, str] = None,
                 place_of_birth: str = None, citizenship: str = None, date_of_issue: Dict[str, str] = None,
                 expiration_date: Dict[str, str] = None, issued_at: str = None, series: str = None, number: str = None,
                 visas: List[object] = None):
        super().__init__(name, gender, date_of_birthday, place_of_birth)
        self.__citizenship = citizenship
        self.__date_of_issue = date_of_issue
        self.__expiration_date = expiration_date
        self.__issued_at = issued_at
        self.__series = series
        self.__number = number
        self.__visas = visas


def execute_application():
    name = {"имя": "Артем", "Фамилия": "Сушков", "Отчество": "Сергеевич"}
    gender = "м"
    date_of_birthday = {"день": "11", "месяц": "апрель", "год": "1988"}
    place_of_birth = "г. Ярославль"
    address = {"улица": "Пушкина", "дом": "3"}
    date_of_issue = {"день": "30", "месяц": "апрель", "год": "2000"}
    issued_at = "Ярославское РОВД"
    series = "1234"
    number = "123456789"

    passport = Passport(name, gender, date_of_birthday, place_of_birth,
                        address, date_of_issue, issued_at, series, number)

    print(passport)
    passport.info()


if __name__ == "__main__":
    execute_application()
