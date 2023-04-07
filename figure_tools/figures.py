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

    def __int__(self, x: int, y: int, side: int):
        pass


class Circle(Shape, FigureFileManagement):
    pass


class Ellipse(Shape, FigureFileManagement):
    pass
