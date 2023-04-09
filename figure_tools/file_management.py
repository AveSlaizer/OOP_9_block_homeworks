from .figures import Square, Circle, Ellipse


class SquareFileManagement:

    @classmethod
    def write_in_file(cls, figure: Square, path: str) -> None:
        """
        Записывает данные фигуры класса Square в .txt файл

        :param figure (Square): экземпляр класса Square
        :param path (str): Путь до файла и название с расширением
        """
        with open(path, "w", encoding="UTF-8") as file:
            file.write(figure.__class__.__name__ + "\n")
            for value in figure.__dict__.values():
                file.write(str(value) + "\n")


    @classmethod
    def read_from_file(cls, path) -> Square:
        """
        Возвращает объект с полями заполненныеми данными из считанного файла

        :param path (str): Путь до файла и название с расширением
        :return:
                square (Square): экземпляр класса Square
        """
        square = Square()
        with open(path, "r", encoding="UTF-8") as file:
            class_name = file.readline().strip()
            if class_name != "Square":
                raise FileNotFoundError("Не верно выбран файл для чтения.")
            square.x = int(file.readline().strip())
            square.y = int(file.readline().strip())
            square.side = float(file.readline().strip())
        return square


class CircleFileManagement:

    @classmethod
    def write_in_file(cls, figure: Circle, path: str) -> None:
        """
        Записывает данные фигуры класса Circle в .txt файл

        :param figure (Circle): экземпляр класса Circle
        :param path (str): Путь до файла и название с расширением
        """
        with open(path, "w", encoding="UTF-8") as file:
            file.write(figure.__class__.__name__ + "\n")
            for value in figure.__dict__.values():
                file.write(str(value) + "\n")


    @classmethod
    def read_from_file(cls, path) -> Circle:
        """
        Возвращает объект с полями заполненныеми данными из считанного файла

        :param path (str): Путь до файла и название с расширением
        :return:
                circle (Circle): экземпляр класса Circle
        """
        circle = Circle()
        with open(path, "r", encoding="UTF-8") as file:
            class_name = file.readline().strip()
            if class_name != "Circle":
                raise FileNotFoundError("Не верно выбран файл для чтения.")
            circle.x = int(file.readline().strip())
            circle.y = int(file.readline().strip())
            circle.radius = float(file.readline().strip())
        return circle

