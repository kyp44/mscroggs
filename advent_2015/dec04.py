import numpy as np
from common import *

sol = np.array([[1, 9, 4],
                [2, 7, 5],
                [3, 8, 6]])

box_solutions(
    2015,
    4,
    sol,
    product,
    True,
)
