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