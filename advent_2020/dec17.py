import numpy as np
from common import *

sol = np.array([[6, 3, 7],
                [1, 2, 5],
                [4, 9, 8]])

box_solutions(
    "dec17-grid.txt",
    sol,
    lambda sol : sol[0,1] * sol[0,2] * sol[2,1],
    True,
)
