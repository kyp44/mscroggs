import numpy as np
from common import *

sol = np.array([[6, 3, 2],
                [5, 8, 4],
                [1, 7, 9]])

box_solutions(
    "dec18-grid.txt",
    sol,
    lambda sol : sol[0,0] * sol[1,1] * sol[2,2],
    True,
)
