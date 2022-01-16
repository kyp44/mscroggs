import numpy as np
from common import *

sol = np.array([[4, 9, 7],
                [1, 6, 3],
                [2, 8, 5]])

box_solutions(
    2021,
    10,
    sol,
    lambda hl : number(sorted(hl)),
    True,
)
