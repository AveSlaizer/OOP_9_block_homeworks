from .figures import Square, Circle, Ellipse


class SquareFileManagement:

    @classmethod
    def write_in_file(cls, figure: Square, path: str):
        with open(path, "w", encoding="UTF-8") as file:
            file.write(figure.__class__.__name__ + "\n")
            for value in figure.__dict__.values():
                file.write(str(value) + "\n")


    @classmethod
    def read_from_file(cls, path) -> Square:
        pass

