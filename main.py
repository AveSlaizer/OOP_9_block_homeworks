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
    def pay_web_money(self):
        pass


class CreditCardPayment(ABC):

    @abstractmethod
    def pay_credit_card(self):
        pass


class PhoneNumberPayment(ABC):

    @abstractmethod
    def pay_phone_number(self):
        pass


class InternetPaymentService(WedMoneyPayment, PhoneNumberPayment):

    def pay_web_money(self):
        # TODO оплата вэбманями
        pass

    def pay_phone_number(self):
        # TODO оплата по номеру телефона
        pass


class TerminalPaymentService(CreditCardPayment):

    def pay_credit_card(self):
        # TODO оплата кредитной картой
        pass


def execute_application():
    pass


if __name__ == "__main__":
    execute_application()
