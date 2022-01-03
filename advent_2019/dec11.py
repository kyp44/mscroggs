import numpy as np
from common import *

sol = np.array([[7,5,6],[9,1,3],[8,4,2]])

box_solutions(
    "dec11-grid.txt",
    sol,
    lambda sol : sol[0,2] * sol[2,0] * sol[2,1],
    True,
)
