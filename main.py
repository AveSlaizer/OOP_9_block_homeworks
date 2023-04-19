"""
Задание 1.
Допустим у нас есть класс RentCarService и в нем есть несколько
методов: найти машину по номеру, забронировать машину по номеру,
распечатать заказ на бронирование, получить информацию о машине,
отправить сообщение клиенту с информацией о его брони.
У данного класса есть несколько зон ответственности, что является
нарушением принципа единой ответственности, так как отвечает за разные
действия.
Необходимо создать класс PrinterService и вынести туда функционал по
печати.
Работу связанную с получением информации о машине перенести в
класс CarInfoService.
Метод по отправке сообщений перенести в класс NotificationService.
Метод поиска машины по номеру в класс CarService.
"""

CARS = {
    "A123XA76": ["KIA Ceed", 2016, 67000],
    "H567KO": ["VW Polo", 2020, 30500],
    "O768PY": ["Renault Logan", 2018, 45000],
}

class PrinterService:

    @staticmethod
    def print_rent_order(car_number: str, date: str, days: int):
        print(f"Автомобиль {CARS[car_number][0]}, номер {car_number} арендован на {days} суток.\n"
              f"Начало аренды: {date}")

class CarInfoService:

    @staticmethod
    def print_car_info(car_number: str, car_info: list[str]):
        print(f"Номер: {car_number}\n"
              f"Название: {car_info[0]}\n"
              f"Год выпуска: {car_info[1]}\n"
              f"Пробег: {car_info[2]}")

class NotificationService:

    @staticmethod
    def send_order_sms(car_number: str, date: str, days: int, client_number: str):
        print(f"SMS на номер {client_number} отправлено. Текст смс:\n"
              f"Автомобиль {CARS[car_number][0]}, номер {car_number} арендован на {days} суток.\n"
              f"Начало аренды: {date}")

class CarService:

    @staticmethod
    def find_car(car_number: str):
        if car_number in CARS.keys():
            return CARS[car_number]
        return


def execute_application():

    car_number = "A123XA76"
    date = "11.03.2023"
    days = 10
    client_number = "+79201234567"
    car = CarService.find_car(car_number)
    CarInfoService.print_car_info(car_number, car)
    PrinterService.print_rent_order(car_number, date, days)
    NotificationService.send_order_sms(car_number, date, days, client_number)



if __name__ == "__main__":
    execute_application()
