from abc import ABC, abstractmethod


"""
Задание 1.
Принцип открытости-закрытости закрепим на примере созданного в
задании 1 класса по отправке сообщений NotificationService.
Допустим нам необходимо кроме отправки сообщения по электронной
почте отправлять еще смс сообщения. И мы можем дописать метод sendMessage
таким образом:
def sendMessage(typeMessage: str, message: str) {
if (typeMessage == "email") {
//send email
}
if (typeMessage == "sms") {
//send sms
}
Но в данном случае мы нарушим второй принцип, потому что класс
должен быть закрыт для модификации, но открыт для расширения.
Для того чтобы придерживаться принципа открытости-закрытости,
нам необходимо спроектировать наш код таким образом, чтобы каждый мог
повторно использовать нашу функцию, просто расширив ее. Поэтому
определим абстрактный класс NotificationService и в нем поместим метод
sendMessage.
Далее создайте класс EmailNotification, который наследуется от
NotificationService и реализует метод отправки сообщений по электронной
почте.
Создайте аналогично класс MobileNotification, который будет отвечать
за отправку смс сообщений.
Проектируя таким образом код мы не будем нарушать принцип
открытости-закрытости, так как мы расширяем нашу функциональность, а не
изменяем (модифицируем) наш класс.
"""


class NotificationService(ABC):
    @staticmethod
    @abstractmethod
    def send_message(*args):
        pass

class EmailNotification(NotificationService):

    @staticmethod
    def send_message(email: str, text: str):
        print(f"Получатель: {email}\n"
              f"{text}")

class MobileNotification(NotificationService):

    @staticmethod
    def send_message(phone: str, text: str):
        print(f"Получатель: {phone}\n"
              f"{text}")



def execute_application():

    email = "email@mail.com"
    phone = "+78901234567"
    text = "<<< message text >>>"
    EmailNotification.send_message(email, text)
    MobileNotification.send_message(phone, text)


if __name__ == "__main__":
    execute_application()
