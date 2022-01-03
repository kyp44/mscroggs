import numpy as np
from common import *

sol = np.array([[4, 5, 6],
                [9, 8, 1],
                [2, 7, 3]])

box_solutions(
    "dec09-grid.txt",
    sol,
    lambda sol : sol[1,0] * sol[1,1] * sol[2,0],
    True,
)
