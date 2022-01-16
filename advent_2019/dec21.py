import numpy as np
from common import *

sol = np.array([[8, 3, 4], [6, 2, 1], [9, 5, 7]])

box_solutions(
    2019,
    21,
    sol,
    lambda hl : anumber(sorted(hl)),
    True,
)
