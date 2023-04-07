class __Shape:

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

    def info(self):
        print(f"Координаты начальной точки: ({self.__x}, {self.__y})")



class Square(__Shape):

    __NAME = "Квадрат"

    def __init__(self, x: int = None, y: int = None, side: float = None):
        super().__init__(x, y)
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side: float):
        self.__side = side

    def info(self):
        print(f"Фигура: {self.__NAME}")
        super().info()
        print(f"Сторона: {self.__side}")


class Circle(__Shape):

    __NAME = "Окружность"

    def __init__(self, x: int = None, y: int = None, radius: float = None):
        super().__init__(x, y)
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        self.__radius = radius

    def info(self):
        print(f"Фигура: {self.__NAME}")
        super().info()
        print(f"Радиус: {self.__radius}")


class Ellipse(__Shape):

    __NAME = "Эллипс"

    def __init__(self, x: int = None, y: int = None, width: float = None, height: float = None):
        super().__init__(x, y)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    def info(self):
        print(f"Фигура: {self.__NAME}")
        super().info()
        print(f"Стороны: {self.__width} x {self.__height}")
