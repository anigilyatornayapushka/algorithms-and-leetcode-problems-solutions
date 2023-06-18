from abc import (
    ABCMeta,
    abstractmethod,
)



class Figure(metaclass=ABCMeta):
    pass


class Figure2d(Figure):

    @abstractmethod
    def s(self) -> int | float:
        pass


class Figure3d(Figure2d):

    @abstractmethod
    def v(self) -> int | float:
        pass


class Square(Figure2d):

    def __init__(self, side: int | float) -> None:
        self.side = side

    def s(self) -> int | float:
        return pow(self.side, 2)


class Cube(Square):

    def __init__(self, side: int | float) -> None:
        self.side = side

    def s(self) -> int | float:
        return super().square() * 6

    def v(self) -> int | float:
        return pow(self.side, 3)


class Triangle(Figure2d):

    def __init__(self, side: int | float) -> None:
        self.side = side

    def s(self) -> int | float:
        return (3**0.5)/4 * self.side


class Pyramid(Triangle):

    def s(self) -> int | float:
        return self._s_side_triangles() + self._s_square_base()

    def v(self) -> int | float:
        return self._s_square_base() * self._h() / 3

    def _h(self) -> int | float:
        return self.side * (3**0.5) / 2

    def _s_side_triangles(self) -> int | float:
        return super().s() * 4

    def _s_square_base(self) -> int | float:
        return pow(self.side, 2)
