from figure_tools.figures import Square, Ellipse, Circle
from figure_tools.file_management import SquareFileManagement


"""
Задание 1.
Создайте базовый класс Shape для хранения плоских фигур.
Определите производные классы:
Square — квадрат, который характеризуется координатами левого
верхнего угла и длиной стороны;
Rectangle — прямоугольник с заданными координатами верхнего
левого угла и размерами;
Circle — окружность с заданными координатами цен-тра и радиусом;
Ellipse — эллипс с заданными координатами верхнего угла описанного
вокруг него прямоугольника со сторонами, параллельными осям координат,
и размерами этого прямоугольника.
Создайте список фигур. Определите класс, который сохраняет фигуры
в файлы, загружает из файла и отобразите информацию о каждой из фигур.
"""

def execute_application():
    shape = Square(1, 2, 90)
    #shape.info()

    circl = Circle(3, 6, 34)
    #circl.info()

    el = Ellipse(1, 4, 45, 23)
    #el.info()

    path = "12.txt"
    SquareFileManagement.write_in_file(shape, path)







if __name__ == "__main__":
    execute_application()
