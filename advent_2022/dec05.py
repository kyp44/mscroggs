import numpy as np
from common import *

sol = np.array([[5, 6, 2],
                [7, 8, 4],
                [3, 9, 1]])

box_solutions(
    2022,
    5,
    sol,
    product,
    True,
)
