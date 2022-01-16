import numpy as np
from common import *

sol = np.array([[3, 1, 6],
                [7, 9, 4],
                [8, 2, 5]])

box_solutions(
    "dec20-grid.txt",
    sol,
    lambda sol : product(sol[1,:]),
    True,
)
