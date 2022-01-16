import numpy as np
from common import *

sol = np.array([[6, 3, 7],
                [1, 2, 5],
                [4, 9, 8]])

box_solutions(
    2020,
    17,
    sol,
    product,
    True,
)
