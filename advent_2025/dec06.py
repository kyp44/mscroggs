import numpy as np
from common import *

sol = np.array([[1, 3, 5],
                [7, 6, 2],
                [4, 9, 8]])

box_solutions(
    2025,
    6,
    sol,
    product,
    True,
)
