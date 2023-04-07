from .file_management import FigureFileManagement


class Shape:
    pass


class Square(Shape, FigureFileManagement):
    pass


class Circle(Shape, FigureFileManagement):
    pass


class Ellipse(Shape, FigureFileManagement):
    pass