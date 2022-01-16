import numpy as np
from common import *

sol = np.array([[9, 1, 6],
                [4, 8, 2],
                [7, 3, 5]])

box_solutions(
    2020,
    3,
    sol,
    lambda hl : number(sorted(hl)),
    True,
)
