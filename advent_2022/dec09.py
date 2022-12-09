import numpy as np
from common import *

sol = np.array([[9, 7, 4],
                [5, 1, 6],
                [8, 2, 3]])

box_solutions(
    2022,
    9,
    sol,
    product,
    True,
)
