from typing import Any
from numpy import floor
from common import *


class Grid:
    def __init__(self, w: int, h: int):
        self.w = w
        self.m = frc(h, w)

    def f(self, x) -> frc:
        return self.m * x

    def s(self, i: int) -> int:
        yl = self.f(i)
        yr = self.f(i+1)

        return floor(yr) - floor(yl) + (0 if yr.is_integer() else 1)

    def count_squares(self) -> int:
        return sum([self.s(i) for i in range(self.w)])


# Example:
print("Example:", Grid(5, 3).count_squares())

pans(Grid(272, 251).count_squares())
