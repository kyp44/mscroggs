import numpy as np
from common import *

sol = np.array([[6, 4, 5],
                [3, 9, 7],
                [8, 2, 1]])

box_solutions(
    2021,
    4,
    sol,
    product,
    True,
)
