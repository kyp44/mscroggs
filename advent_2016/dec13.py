import numpy as np
from common import *

sol = np.array([[4, 7, 3],
                [5, 1, 2],
                [9, 6, 8]])

box_solutions(
    2016,
    13,
    sol,
    lambda a: min(a)**max(a),
    True,
)
