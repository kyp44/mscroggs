import numpy as np
from common import *

sol = np.array([[1, 2, 3],
                [4, 5, 9],
                [8, 7, 6]])

box_solutions(
    2016,
    16,
    sol,
    lambda a: number(sorted(a)),
    True,
)
