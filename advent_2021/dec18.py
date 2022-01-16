import numpy as np
from common import *

sol = np.array([[6, 3, 2],
                [5, 8, 4],
                [1, 7, 9]])

box_solutions(
    2021,
    18,
    sol,
    product,
    True,
)
