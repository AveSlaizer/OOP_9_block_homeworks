from .file_management import FigureFileManagement


class Shape:

    def __init__(self, x: int = None, y: int = None):
        self.verify_coord(x)
        self.verify_coord(y)

        self.__x = x
        self.__y = y

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise ValueError("Значение координаты должно быть вещественным числом")


class Square(Shape, FigureFileManagement):
    pass


class Circle(Shape, FigureFileManagement):
    pass


class Ellipse(Shape, FigureFileManagement):
    pass