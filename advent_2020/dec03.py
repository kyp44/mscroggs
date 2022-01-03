import numpy as np
from common import *

sol = np.array([[9, 1, 6],
                [4, 8, 2],
                [7, 3, 5]])

box_solutions(
    "dec03-grid.txt",
    sol,
    lambda sol : number(sorted([sol[0,1], sol[1,2], sol[2,1]])),
    True,
)
