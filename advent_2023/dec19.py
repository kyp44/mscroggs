import numpy as np
from common import *

sol = np.array([[8, 5, 6],
                [2, 7, 9],
                [4, 1, 3]])

box_solutions(
    2023,
    19,
    sol,
    product,
    True,
)
