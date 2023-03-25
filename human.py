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