import numpy as np
from common import *

sol = np.array([[8, 6, 7],
                [4, 5, 1],
                [9, 3, 2]])

box_solutions(
    "dec03-grid.txt",
    sol,
    lambda sol : number(sorted([sol[1,0], sol[2,1], sol[2,2]])),
    True,
)
