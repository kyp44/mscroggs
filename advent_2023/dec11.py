import numpy as np
from common import *

sol = np.array([[3, 7, 5],
                [9, 2, 1],
                [4, 8, 6]])

box_solutions(
    2023,
    11,
    sol,
    product,
    True,
)
