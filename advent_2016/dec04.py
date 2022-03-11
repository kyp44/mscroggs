import numpy as np
from common import *

sol = np.array([[6, 8, 7],
                [9, 1, 4],
                [5, 3, 2]])

box_solutions(
    2016,
    4,
    sol,
    product,
    True,
)
