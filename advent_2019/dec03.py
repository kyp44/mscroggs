import numpy as np
from common import *

sol = np.array([[8, 6, 7],
                [4, 5, 1],
                [9, 3, 2]])

box_solutions(
    2019,
    3,
    sol,
    lambda hl : number(sorted(hl)),
    True,
)
