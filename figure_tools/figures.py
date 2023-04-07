from .file_management import FigureFileManagement


class Shape:

    def __init__(self, x: int = None, y: int = None):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


class Square(Shape, FigureFileManagement):

    def __init__(self, x: int = None, y: int = None, side: float = None):
        super().__init__(x, y)
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side: float):
        self.__side = side


class Circle(Shape, FigureFileManagement):

    def __init__(self, x: int = None, y: int = None, radius: float = None):
        super().__init__(x, y)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius


class Ellipse(Shape, FigureFileManagement):
    pass
