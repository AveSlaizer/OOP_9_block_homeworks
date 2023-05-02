from abc import abstractmethod, ABC


"""
Задание 2.
Рассмотрим принцип инверсии зависимостей. Исправьте следующий код таким
образом, чтобы классы и верхних, и нижних уровней зависели от одних и тех же
абстракций, а не от конкретных реализаций.

class AnonymousAuthentication:
    def doAauthentication(self):
        pass
class GithubAuthentication:
    def doAuthentication(self):
        pass
class FacebookAuthentication:
    def doAuthentication(self):
        pass
class Permissions:
    def __init__(self, auth: AnonymousAuthentication)
        self.auth = auth
        def getPermissions(self):
        self.auth.doAuthentication()
"""


class Authentication(ABC):

    @abstractmethod
    def do_authentication(self):
        pass

class AnonymousAuthentication(Authentication):
    def do_authentication(self):
        print("Анонимная авторизация")
        pass
class GithubAuthentication(Authentication):
    def do_authentication(self):
        print("Авторизация в гитхаб")
        pass
class FacebookAuthentication(Authentication):
    def do_authentication(self):
        print("Авторизация в фэйсбук")
        pass
class Permissions:
    def __init__(self, auth: Authentication):
        self.auth = auth
    def get_permissions(self):
        self.auth.do_authentication()


def execute_application():

    auth = GithubAuthentication()

    perm = Permissions(auth)

    perm.get_permissions()




if __name__ == "__main__":
    execute_application()
