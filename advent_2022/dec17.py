import numpy as np
from common import *

sol = np.array([[3, 5, 2],
                [1, 4, 7],
                [6, 8, 9]])

box_solutions(
    2022,
    17,
    sol,
    product,
    True,
)
