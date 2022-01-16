import numpy as np
from common import *

sol = np.array([[4, 5, 6],
                [9, 8, 1],
                [2, 7, 3]])

box_solutions(
    2020,
    9,
    sol,
    product,
    True,
)
