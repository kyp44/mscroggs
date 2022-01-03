import numpy as np
from common import *

sol = np.array([[1, 9, 4],
                [2, 7, 5],
                [3, 8, 6]])

box_solutions(
    "dec04-grid.txt",
    sol,
    lambda sol : sol[0, 1] * sol[1, 0] * sol[2, 2],
    True,
)
