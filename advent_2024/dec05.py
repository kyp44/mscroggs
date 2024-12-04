import numpy as np
from common import *

sol = np.array([[2, 6, 7],
                [4, 3, 8],
                [9, 5, 1]])

box_solutions(
    2024,
    5,
    sol,
    product,
    True,
)
