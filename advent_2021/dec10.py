import numpy as np
from common import *

sol = np.array([[4, 9, 7],
                [1, 6, 3],
                [2, 8, 5]])

box_solutions(
    "dec10-grid.txt",
    sol,
    lambda sol : number(sorted([sol[0,0], sol[1,1], sol[2,2]])),
    True,
)
