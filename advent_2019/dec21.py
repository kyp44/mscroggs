import numpy as np
from common import *

sol = np.array([[8, 3, 4], [6, 2, 1], [9, 5, 7]])

box_solutions(
    "dec21-grid.txt",
    sol,
    lambda sol : anumber(sorted([sol[0,1], sol[1,1], sol[1,2]])),
    True,
)
