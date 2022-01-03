import numpy as np
from common import *

sol = np.array([[9, 5, 4],
                [7, 2, 3],
                [8, 1, 6]])

box_solutions(
    "dec22-grid.txt",
    sol,
    lambda sol : number(sorted([sol[0,0], sol[0,2], sol[2,0]])),
    True,
)
