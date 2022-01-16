import numpy as np
from common import *

sol = np.array([[5, 6, 3],
                [7, 2, 1],
                [8, 4, 9]])

box_solutions(
    2015,
    20,
    sol,
    product,
    True,
)
