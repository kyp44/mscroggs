import numpy as np
from common import *

sol = np.array([[9, 5, 4],
                [7, 2, 3],
                [8, 1, 6]])

box_solutions(
    2020,
    22,
    sol,
    lambda hl : number(sorted(hl)),
    True,
)
