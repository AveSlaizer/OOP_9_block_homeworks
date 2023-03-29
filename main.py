from typing import Dict


class Passport:

    def __init__(self, name: Dict[str, str] = None, gender: str = None, date_of_birthday: Dict[str, str] = None,
                 address: Dict[str, str] = None, date_of_issue: Dict[str, str] = None,
                 issued_at: str  = None, series: str  = None, number: str = None):
        self.__name = name
        self.__gender = gender
        self.__date_of_birthday = date_of_birthday
        self.__address = address
        self.__date_of_issue = date_of_issue
        self.__issued_at = issued_at
        self.__series = series
        self.__number = number


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
