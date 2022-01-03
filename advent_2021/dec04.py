import numpy as np
from common import *

sol = np.array([[6, 4, 5],
                [3, 9, 7],
                [8, 2, 1]])

box_solutions(
    "dec04-grid.txt",
    sol,
    lambda sol : sol[0,1] * sol[0,2] *sol[2,0],
    True,
)
