from figures import Square, Circle, Ellipse
from abc import ABC, abstractmethod
from typing import Union


class FigureFileManagement(ABC):

    @abstractmethod
    def write_in_file(self, figure: Union[Square, Circle, Ellipse], path: str):
        pass

    @abstractmethod
    def read_from_file(self, path) -> Union[Square, Circle, Ellipse]:
        pass
