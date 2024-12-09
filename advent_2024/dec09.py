import numpy as np
from common import *

sol = np.array([[7, 8, 9],
                [5, 4, 1],
                [6, 2, 3]])

box_solutions(
    2024,
    9,
    sol,
    product,
    True,
)
