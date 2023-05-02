from abc import ABC, abstractmethod

"""
Задание 1.
Рассмотрим принцип разделения интерфейсов.
Допустим у нас имеется абстрактный класс Payments и в нем есть три метода:
оплата WebMoney, оплата банковской карточкой и оплата по номеру телефона.

class Payments(ABC):
    @abstarctmethod
    def payWebMoney(self):
        pass

    @abstarctmethod
    def payCreditCard(self):
        pass

    @abstarctmethod
    def payPhoneNumber(self):
        pass

Выполните разделение интерфейса таким образом, чтобы можно было реализовать
два класса-сервиса, которые будут у себя реализовывать различные виды проведения
оплат (класс InternetPaymentService и TerminalPaymentService). При этом
TerminalPaymentService не должен поддерживать проведение оплат по номеру телефона.
"""


class WedMoneyPayment(ABC):

    @abstractmethod
    def pay_web_money(self, value):
        pass


class CreditCardPayment(ABC):

    @abstractmethod
    def pay_credit_card(self, value):
        pass


class PhoneNumberPayment(ABC):

    @abstractmethod
    def pay_phone_number(self, value):
        pass


class InternetPaymentService(WedMoneyPayment, PhoneNumberPayment):

    def pay_web_money(self, value: float):
        # какая-то реализация
        print(f"Оплата на сумму \"{value}\" руб. прошла успешно.")

    def pay_phone_number(self, value: float):
        # какая-то реализация
        print(f"Оплата на сумму \"{value}\" руб. прошла успешно.")


class TerminalPaymentService(CreditCardPayment):

    def pay_credit_card(self, value: float):
        # какая-то реализация
        print(f"Оплата на сумму \"{value}\" руб. прошла успешно.")


def execute_application():

    payment1 = InternetPaymentService()

    payment1.pay_web_money(123)

    payment2 = TerminalPaymentService()
    payment2.pay_credit_card(10003)


if __name__ == "__main__":
    execute_application()
